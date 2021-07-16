
from PIL import Image
import os
path="./Boyutlanmadi/"


for root, dirs, files in os.walk(path):
    for filename in files:
      image = Image.open(path+filename)
      pix = image.load()
      print(filename)

      #if image.width>=2400:
       #   new_image = image.resize((2400, 1350))
        #  print("2400")
      #elif image.width >=2200:
       #   new_image = image.resize((2200, 1237))
        #  print("2200")
      #elif image.width >=2000:
       #   new_image = image.resize((2000, 1125))
        #  print("2000")
      #elif image.width >=1800:
          #new_image = image.resize((1800, 1012))
          #print("1800")
      #elif image.width>=1600:
       #   new_image = image.resize((1600, 900))
        #  print("1600")
      #elif image.width>=1400:
       #   new_image = image.resize((1400, 787))
        #  print("1400")
      #elif image.width>=1200:
       #   new_image = image.resize((1200, 675))
        #  print("1200")
      if image.width>=1024:
          new_image = image.resize((1024, 576))
          print("1000")
      #elif image.width>=800:
       #   new_image = image.resize((800, 450))
        #  print("800")
      else:
          new_image = image.resize((640, 360))
          print("640")
      new_image.save('./Boyutlandi/' + filename)
