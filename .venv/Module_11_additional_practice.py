#Модуль 11. Дополнительная практика

from PIL import Image
from PIL import ImageDraw, ImageFont
import subprocess
import os



def resize_foto(name, multi):
    image = Image.open(name)
    w, h = image.size
    return image.resize((round(w * multi), round(h * multi)))

def paste_foto(base_image, foto_4_paste, position):
    base_image.paste(foto_4_paste, position, foto_4_paste)
#    base_image.show()
    return base_image

def text_insert(image_4_text, font, text, fill, position):
    fin_image = image_4_text.copy()
    draw = ImageDraw.Draw(fin_image)
    draw.text(position, text, fill, font)
    return fin_image



image_1 = resize_foto("/Users/vladimirchi/PycharmProjects/pythonProject_2/.venv/images/img_3.jpg", 2)
image_2 = resize_foto("/Users/vladimirchi/PycharmProjects/pythonProject_2/.venv/images/girl_-no-bg.png", 0.2)
image_4_text = paste_foto(image_1, image_2, (400, 350))

font = ImageFont.truetype('Comic Sans MS Bold.ttf', 18)
text = 'Привет, Пупсик'
fill =(255, 20, 147)
position = (520, 400)
fin_image = text_insert(image_4_text, font, text, fill, position)

fin_image.show()
fin_image.save('fon_pillow_paste_pos.png')
fin_image.close()

subprocess.call(["/usr/bin/open", "/System/Library/CoreServices/Finder.app"])
