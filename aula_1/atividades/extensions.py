e = str(input("Qual o nome do arquivo? ")).casefold()

imagem = str(".gif") and str(".jpeg") and str(".jpg") and str(".png")
texto = str(".pdf") and str(".txt")
zip = str(".zip")

if str(e).endswith(imagem):
    print("Imagem")
elif str(e).endswith(texto):
    print("Texto")
elif str(e).endswith(zip):
    print("Zip_file")
else:
    print("application/octet-stream")