#This program converts a jpg picture to ASCII art.

from PIL import Image
import numpy as np
import textwrap
ASCII_CHARACTERS=['@', '%', '#', '*', '+', '=', '-', ':', '.']
NEW_WIDTH=150
name_of_picture=input("File name of picture to be converted: ")
img=Image.open(name_of_picture)
img=img.convert('L')
(height, width)=img.size
aspect_ratio=height/width
new_height=int(aspect_ratio*NEW_WIDTH)
new_img=img.resize((NEW_WIDTH,new_height))
pixels=np.asarray(new_img.getdata())
ascii=''
#Since we are using 9 characters and pixel values range from 0 to 255 the width of range for each character is 29.
for i in range(len(pixels)):
	ascii=ascii+ASCII_CHARACTERS[int(pixels[i]/29)]
rows=textwrap.wrap(ascii,NEW_WIDTH)
with open('ascii_art', 'w') as f:
	for j in range(len(rows)):
		print(rows[j], file=f)
