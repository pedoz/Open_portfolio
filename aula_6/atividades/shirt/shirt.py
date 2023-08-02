from PIL import Image, ImageOps
import sys
import os.path


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()
elif len(sys.argv) > 3:
    print("Too may command-line arguments")
    sys.exit()

ref = sys.argv[1]
new_file = sys.argv[2]
dot1 = ref.rfind('.')
dot2 = new_file.rfind('.')
ext1 = ref[dot1:]
ext2 = new_file[dot2:]


if not os.path.exists(ref):
    print("Input does not exist")
    sys.exit()
elif ref.endswith((".jpg", ".jpeg", ".png")) == False:
    print("Invalid output")
    sys.exit()
elif ext1 != ext2:
    print("Input and output have different extensions")
    sys.exit()

old_photo = Image.open(ref)
camisa = Image.open("shirt.png")
size = camisa.size
new_photo = ImageOps.fit(old_photo, size, method=0, bleed=0.0, centering=(0.5, 0.5))

new_photo.paste(camisa, (0,0), camisa)
new_photo.save(new_file)