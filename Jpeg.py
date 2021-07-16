from PIL import Image
import os
from natsort import natsorted

path = "./isimlendirilmedi/"
dosyanumara = 4436
orderedFilename = ""

files = os.listdir(path)
files = natsorted(files)


for filename in files:
    dosyanumara = dosyanumara + 1
    orderedFilename = str(dosyanumara)
    im = Image.open(path + filename)
    im.convert('RGB').save('./isimlendirildi/b_yg13_'+str(dosyanumara)+ '_mask.jpg', "JPEG")  # , "JPEG")