import math

def delta(a, b, c):
    return b**2-4*a*c

def main():
    a = int(input("Digite um valor para A: "))
    b = int(input("Digite um valor para B: "))
    c = int(input("Digite um valor para C: "))
    imprime_raizes(a,b,c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        x1 = ((-b)+ math.sqrt((b**2)-(4*a*c)))/(2*a)
        print("A Unica raiz é: ", x1)
    else:
        if d < 0:
            print("Esta equação não possui raizes!")
        else:
            x1 = ((-b)+ math.sqrt((b**2)-(4*a*c)))/(2*a)
            x2 = ((-b)- math.sqrt((b**2)-(4*a*c)))/(2*a)
            print("A primeira raiz é: ",x1)
            print("A segunda raiz é: ",x2)








