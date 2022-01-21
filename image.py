import sys
import os
from PIL import Image

#grab first and second argument
image_folder =sys.argv[1]
output_folder = sys.argv[2]


#check is new exists , if not create
if os.path.exists(output_folder):

     print(image_folder,output_folder)

else :
    print("somthing went wrong")
#loop through Pokedex,
#convert images to png
#save to the new folder
