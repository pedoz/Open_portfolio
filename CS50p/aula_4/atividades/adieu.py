import sys
import inflect

p = inflect.engine()

lista = []

while True:
    
    try:
        lista.append(input("Nome: "))

    except EOFError:
        print(p.join(lista))
        sys.exit()




#Adieu, adieu, to Liesl
#Adieu, adieu, to Liesl and Friedrich
#Adieu, adieu, to Liesl, Friedrich, and Louisa
#Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl