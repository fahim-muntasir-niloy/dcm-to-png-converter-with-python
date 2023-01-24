# This file is ready for fully drag and drop into any folder to convert files from dcm to png or jpg format.
# For jpg just change .png to .jpg in the rename section

import numpy as np
from PIL import Image
import pydicom as dcm
import os

cwd = os.getcwd()

# function to read files from the directory one by one
dcmFiles = []
for dirpath,dirnames, filename in os.walk(cwd):
    # print("current path: ",dirpath)
    # print("directories: ",dirnames)
    # print("files: ",filename)
    for fp in filename:
        ext = os.path.splitext(fp)[-1]
        if (ext == ".dcm"):
            dcmFiles.append(fp)

# dcmFiles
    
# Function to convert dcm to jpg
#* ===================================================>

def dcm_to_jpg(file):
    ds = dcm.dcmread(file)
    newimg = ds.pixel_array.astype(float)
    scaledImage = (np.maximum(newimg,0)/newimg.max()) * 255.0
    scaledImage = np.uint8(scaledImage)
    finalImage = Image.fromarray(scaledImage)
    return finalImage



#* Rename Section. Use any of the for loops.
#* ===================================================>



# This below code will rename files chronologically.
#* ========================================================>
for name in dcmFiles:
    image = dcm_to_jpg(name)
    image.save(f"{(dcmFiles.index(name)+1)}.png")
  
    
    
    
# This below code will rename files giving them random number
#* ============================================================>

for name in files:
    new_file_name = round(np.random.rand()*100000000)
    image = dcm_to_jpg(name)
    image.save( f"{new_file_name}.png")