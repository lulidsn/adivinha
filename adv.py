import random

usu = int(input("tente adivinhar um número de 0 a 10:"))
num = random.randint(0,10)
tent = 1
if(usu==num):
    print("você acertou!")
    print('\ntentativas: ', tent)
while(usu != num):
    usu = int(input("tente adivinhar um número de 0 a 10:"))
    num = random.randint(0, 10)
    tent = tent + 1
    if(usu==num):
        print("você acertou!")
        print('\ntentativas: ', tent)
