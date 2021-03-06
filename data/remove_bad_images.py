from PIL import Image
import os
for directory in ('chickens', 'not_chickens'):
  img_names  = os.listdir(directory)
  for img_name in img_names:
    img_path = os.path.join(directory, img_name)
    try:
      image = Image.open(img_path)
      image.load()
      image.close()
    except IOError:
      os.remove(img_path)
  
