# -*- coding: utf-8 -*-
"""\
This is a python port of "Goose" orignialy licensed to Gravity.com
under one or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.

Python port was written by Xavier Grangier for Recrutae

Gravity.com licenses this file
to you under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
class Image(object):
    
    def __init__(self):
        # holds the Element node of the image we think is top dog
        self.topImageNode = None
        
        # holds the src of the image
        self.imageSrc = ""
        
        # how confident are we in this image extraction?
        # the most images generally the less confident
        self.confidenceScore = float(0.0)
        
        # Height of the image in pixels
        self.height = 0
        
        # width of the image in pixels
        self.width = 0
        
        # what kind of image extraction was used for this?
        # bestGuess, linkTag, openGraph tags?
        self.imageExtractionType = "NA"
        
        # stores how many bytes this image is.
        self.bytes = long(0)
    
    
    def getImageSrc(self):
        return self.imageSrc
    


        
        