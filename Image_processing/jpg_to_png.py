import sys
import os
from PIL import Image

imagefolder = sys.argv[1]
outputfolder = sys.argv[2]
directory = os.listdir(f'{sys.argv[1]}')
for file in directory :
    img = Image.open(f'{imagefolder}\\{file}')
    if os.path.exists(f'{outputfolder}') == True:
        img.save(f'{outputfolder}\\{file[:-4]}.png')
    elif os.path.exists(f'{outputfolder}') == False:
        os.mkdir(f'{outputfolder}')
        continue
