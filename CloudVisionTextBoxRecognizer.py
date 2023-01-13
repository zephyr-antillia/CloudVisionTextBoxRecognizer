# Copyright 2023 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# CloudVisionTextBoxRecognizer.py

# This works on Windows11

# 2022/12/24 
# Added save_annotation

import os
import sys
import time
import glob
import csv
import json
import pprint
from PIL import Image, ImageDraw, ImageFont
#import traceback2 as traceback
import traceback
#2 as traceback
#pip install google-cloud-vision
from google.cloud import vision
from google.cloud.vision_v1 import types

import io

from ConfigParser   import ConfigParser
from ImagePreprocessor import ImagePreprocessor

from RecognizedObjects import RecognizedObjects
from RecognizedObjectsVisualizer import RecognizedObjectsVisualizer


class CloudVisionTextBoxRecongizer:
  def __init__(self, config_file):
    self.config    = ConfigParser(config_file)
  
    PARAMETER           = "parameter"
    self.images_dir     = self.config.get(PARAMETER, "images_dir")
    self.recognize_oneimage_format   = self.config.get(PARAMETER, "image_format")
    self.output_dir     = self.config.get(PARAMETER, "output_dir")
    self.language_hints = self.config.get(PARAMETER, "language_hints")
    self.image_format   = self.config.get(PARAMETER, "image_format")

    PREPROCESSOR        = "preprocessor"
    self.preprocessing  = self.config.get(PREPROCESSOR, "preprocessing") 
    self.image_scaling  = self.config.get(PREPROCESSOR, "image_scaling")
    self.contrast       = self.config.get(PREPROCESSOR, "contrast")
    self.gray_image     = self.config.get(PREPROCESSOR, "gray_image")
    self.sharpness      = self.config.get(PREPROCESSOR, "sharpness")
  
    VISUALIZER          = "visualizer"
    self.font_name      = self.config.get(VISUALIZER, "font_name")
    self.draw_boundingbox  = self.config.get(VISUALIZER, "draw_boundingbox")
    self.expanding_ratio   = self.config.get(VISUALIZER, "expanding_ratio")
    self.scaling_on_nonpreprocessing = self.config.get(VISUALIZER, "scaling_on_nonpreprocessing", 1.0)

  def recognize(self): 
    if not os.path.exists(self.images_dir):
      raise Exception("Not found dir " + self.images_dir)

    if not os.path.exists(self.output_dir):
      os.makedirs(self.output_dir)  

    image_files     = glob.glob(self.images_dir +  "./*" + self.image_format)
    image_files     = sorted(image_files)
    print("--- image files {}".format(image_files))
    for image_file in image_files:
      print("image_file {}".format(image_file))
      self.recognize_one(image_file, self.output_dir)

#--
  def recognize_one(self, image_file, output_dir):
    try:
      
      preprocessor = ImagePreprocessor(gray_image=self.gray_image, preprocessing=self.preprocessing)

      img = preprocessor.read(image_file, image_scaling=self.image_scaling, 
                              contrast=self.contrast, sharpness=self.sharpness)
    
      basename = os.path.basename(image_file)
      if self.preprocessing:
        save_image_name = "preprocessed_" + "scaling_" + str(self.image_scaling) + "_contrast_" + str(self.contrast) + "_sharpness_" + str(self.sharpness) + "_" +basename
      else:
        save_image_name = "non_preprocessed_" + basename

      enhanced_image_file = os.path.join(output_dir, save_image_name)
      img.save(enhanced_image_file) #, "PNG")
      
      content = None
      with io.open(enhanced_image_file, 'rb') as f:
        content = f.read()        
      image  = vision.Image(content=content)
      client = vision.ImageAnnotatorClient()

      image_context = types.ImageContext(language_hints=self.language_hints) 

      response = client.text_detection(image=image, image_context=image_context)
      annotations = response.text_annotations

      pprint.pprint(annotations)

      recognized  = RecognizedObjects(annotations, self.preprocessing, self.scaling_on_nonpreprocessing)
      
      visualizer  = RecognizedObjectsVisualizer(font_name=self.font_name)
      
      visualizer.visualize(recognized, enhanced_image_file, output_dir, 
                self.draw_boundingbox,
                self.expanding_ratio)

    except:
      traceback.print_exc()


##
# 
#  
if __name__ == "__main__":
  
  try:
    config_file = "./recognition.conf"
 
    start_time = time.time()

    recognizer = CloudVisionTextBoxRecongizer(config_file)

    recognizer.recognize() 
    end_time = time.time()
    ellapsed = round(end_time - start_time, 4)
    print("--- time       = {}".format(ellapsed))
  except:
    traceback.print_exc()
