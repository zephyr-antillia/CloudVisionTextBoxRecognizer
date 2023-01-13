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

# RecognizedObjecs.py


import traceback

class RecognizedObjects:

  def __init__(self, annotations, preprocessing, scaling_on_nonpreprocessing):
    self.texts      = []
    self.rectangles = []
    self.preprocessing = preprocessing
    self.scaling_on_nonpreprocessing = scaling_on_nonpreprocessing
    sentences = annotations[0].description.split("\n")
    #self.dump(sentences)
    text     = "" 
    poly_vertices = []

    sentence_index = 0

    for annotation in annotations[1:]:
        text += annotation.description
        
        print("--- text {} ".format(text))
        
        poly_vertices.append(annotation.bounding_poly.vertices)

        print("--- poly_vertices {}".format(poly_vertices))

        if sentences[sentence_index].replace(' ', '') == text:
          vertices = []

          for vertex in poly_vertices:
            for v in vertex:
              vertices.append([v.x, v.y])
        
          (min_x, min_y, max_x, max_y) = self.get_bounding_box(vertices)

          self.texts.append(sentences[sentence_index])
          self.rectangles.append((min_x, min_y, max_x, max_y))
          text = ""
          poly_vertices = []
          sentence_index += 1
    if self.preprocessing == False:
      self.resize_rectangles(self.scaling_on_nonpreprocessing)


  def dump(self, sentences):
    index = 0
    for s in sentences:
      index += 1
      print(" {} {}".format(index, s))


  def get_bounding_box(self, vertices):

    min_x = 100000
    min_y = 100000
    max_x = 0
    max_y = 0
    for vertex in vertices:
        #print("--- vertex {}".format(vertex))
        #for v in vertex:
        #print("--- v {}".format(v))
        (x, y) = vertex
        if x <= min_x:
          min_x = x
        if y <= min_y:
          min_y = y

        if x >= max_x:
          max_x = x
        if y >= max_y:
          max_y = y
    
    return (min_x, min_y, max_x, max_y)

  def resize_rectangles(self, ratio):
    resized_rectangles = []
    for rectangle in self.rectangles:
      (min_x, min_y, max_x, max_y) = rectangle
      min_x = float(min_x) * float(ratio)
      min_y = float(min_y) * float(ratio)
      max_x = float(max_x) * float(ratio)
      max_y = float(max_y) * float(ratio)
      resized_rectangles.append( (min_x, min_y, max_x, max_y))
    self.rectangles = resized_rectangles

