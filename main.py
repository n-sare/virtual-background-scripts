from PIL import Image
import os
path="./mask/"
dosyanumara=0
for root, dirs, files in os.walk(path):
    for filename in files:
      dosyanumara=dosyanumara+1
      im = Image.open(path+filename)
      pix = im.load()
      print(filename)

      for i in range(im.width):
        for j in range(im.height):
          if (pix[i,j]==(0, 0, 0, 0)):
            pix[i,j]=(0,0,0)

          else:
            pix[i, j]=(255,255,255)
      im.save('./mask2/'+filename)



