import random

def suma():
    x = int(input("Ingrese el valor de x: "))
    sum = lambda x : x + 15
    print(f"{x} + 15 = {sum(x)}")

def multiplicacion():
    x = int(input("Ingrese el valor de x: "))
    y = int(input("Ingrese el valor de y: "))
    mult = lambda x, y : x * y
    print(f"{x} * {y} = {mult(x, y)}")

def dividir():
    x = int(input("Ingrese el valor de x: "))
    y = random.randint(1, 10)
    div = lambda x, y : x / y
    print(f"{x} / {y} = {div(x, y)}")

def  main():
    suma()
    multiplicacion()
    dividir()

if __name__ == "__main__":
    main()