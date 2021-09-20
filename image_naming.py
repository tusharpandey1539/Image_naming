# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:28:22 2021

@author: tushar
"""
from PIL import Image, ImageDraw, ImageFont
#PIL = Python imaging library.

def naming_image(city_name):
    image = Image.open('{}.jpg'.format(city_name))
    # Creating a image object.
    
    font_type = ImageFont.load_default()
    # This function truetype takes two arguments, 1. Font type 2. Font size
    
    image_draw = ImageDraw.Draw(image)
    # This function is used to convert the image in editable format.
    
    image_draw.text((15,15), city_name, fill = (237, 230, 211), font=font_type)
    # Rendering the image: Starting coordinates, Text, Text color, Font style.
    
    image.save('{}.jpg'.format(city_name))
        
    image.show()
    #function displays image
    

city_name = input('Enter the city name: ')
    # Taking user input for the file name.

naming_image(city_name)
