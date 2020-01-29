'''
Intall Pillow on raspberry pi with:
sudo pip install Pillow

'''
from PIL import Image

path = 'car0.1.png'

try:  
    img  = Image.open(path)  # open image given a path
except IOError: 
    pass