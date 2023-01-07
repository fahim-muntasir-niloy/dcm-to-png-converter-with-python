import numpy as np
from PIL import Image
import pydicom as dcm
import os

cwd = os.getcwd()

# function to read files one by one
dcmFiles = []
for dirpath,dirnames, filename in os.walk(cwd):
    print("current path: ",dirpath)
    print("directories: ",dirnames)
    print("files: ",filename)
    for fp in filename:
        ext = os.path.splitext(fp)[-1]
        if (ext == ".dcm"):
            dcmFiles.append(fp)

# dcmFiles
    
# convert dcm to jpg
def dcm_to_jpg(file):
    ds = dcm.dcmread(file)
    newimg = ds.pixel_array.astype(float)
    scaledImage = (np.maximum(newimg,0)/newimg.max()) * 255.0
    scaledImage = np.uint8(scaledImage)
    finalImage = Image.fromarray(scaledImage)
    return finalImage


for name in dcmFiles:
    image = dcm_to_jpg(name)
    image.save(name+'.png')