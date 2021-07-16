from PIL import Image
import os
path="./isimlendi/b_yg13_"
dosyanumara=0
for i in range(1, 257):
    with open(path+str(i)+'.jpg', 'w') as im:
      dosyanumara=dosyanumara+1
      im = Image.open(path+filename)
      pix = im.load()

      for i in range(im.width):
        for j in range(im.height):
          if (pix[i,j]==(0, 0, 0, 0)):
            pix[i,j]=(0,0,0)

          else:
            pix[i, j]=(255,255,255)
      im.save('./maskelendi-web/'+str(dosyanumara) +'.png')



