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

# RecognizedObjectVisualizer.py
import os

from PIL import Image, ImageDraw, ImageFont
#import traceback2 as traceback
import traceback

TEXT_HORIZONTAL = 0
TEXT_VERTICAL   = 1

class RecognizedObjectsVisualizer:

  def __init__(self, font_name= "BIZ-UDMinchoM.ttc"):
    self.font_name  = font_name
 

  def get_font(self, height, width):

    fsize = 14
    direction = TEXT_VERTICAL
    try:
      #if height % 2 == 1:
      #  height += 1
      fsize = width

      if height < width:
        fsize = height
        direction = TEXT_HORIZONTAL
      fsize = int(fsize)
      #print("----- font_name {}  fsize {}".format(self.font_name, fsize))
      font = ImageFont.truetype(self.font_name, fsize) 
    except IOError:
      print("Failed to font_name {} size {} ".format(self.font_name, fsize))
      try:
       font = ImageFont.truetype(self.font_name, 20)
      except IOError:
       font = ImageFont.truetype('arial.ttf', 20)
    
    return (font, direction)


  def visualize(self, recognized_objects, image_file, output_dir, draw_boundingbox, expanding_ratio):
    org = Image.open(image_file)
    w, h = org.size
    if recognized_objects.preprocessing == False:
      scaling_ratio = recognized_objects.scaling_on_nonpreprocessing
      w = int(w * scaling_ratio)
      h = int(h * scaling_ratio)
    
    #2023/01/05 
    w = int (w * expanding_ratio)
    h = int (h * expanding_ratio)
    self.draw_recognized_objects(w, h, recognized_objects, image_file, output_dir, draw_boundingbox)


  def draw_recognized_objects(self, width, height, recognized_objects, image_file, output_dir, draw_boundingbox):

    img = Image.new("RGB", (width,  height), (255, 255, 255))
    texts      = recognized_objects.texts
    rectangles = recognized_objects.rectangles

    draw = ImageDraw.Draw(img)
    list_len =len(rectangles)
    for i in range(list_len):
      (min_x, min_y, max_x, max_y) = rectangles[i]
      #print(" {}".format(texts[i]))
      #print(" ({}, {})  ({}, {})".format(min_x, min_y, max_x, max_y))
      # [(x0, y0), (x1, y1)]
      if draw_boundingbox:
        draw.rectangle([(min_x, min_y), (max_x, max_y)], fill=None, outline="red", width=1)
      h = max_y - min_y
      w = max_x - min_x
      (font, direction) = self.get_font(h, w)
      if direction == TEXT_HORIZONTAL:
        draw.text((min_x, min_y), texts[i], fill='black', font=font)
      else:
        print("VERT {}".format(texts[i]))
        y = min_y
        for ch in texts[i]:
          draw.text((min_x, y), ch, fill="black", font=font)
          #print(ch)
          y += w

    basename = os.path.basename(image_file)
    
    output_file = os.path.join(output_dir,basename)
    print("--- output_file {}".format(output_file))

    img.save(output_file) #, "PNG") 

