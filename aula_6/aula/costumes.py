import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    #colocar no terminal os argumentos para criar um GIF
    images.append(image)

images[0].save(
    "costume.gif", save_all=True, append_images=[images[1]], duration = 200, loop = 0
)
#pillow lib faz a mão de abrir, fechar e salvar automaticamente