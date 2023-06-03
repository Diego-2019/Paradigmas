class Figura:
    def calcularArea(this):
        raise
    
    def calcularPerimetro(this):
        raise

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def calcularPerimetro(self):
        return self.lado1 + self.lado2 + self.lado3


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return 3.14159 * (self.radio ** 2)

    def calcularPerimetro(self):
        return 2 * 3.14159 * self.radio


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)


class Hexagono(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return (3 * (3 ** 0.5) * (self.lado ** 2)) / 2

    def calcularPerimetro(self):
        return 6 * self.lado


def main():
    opcion = -1
    fig = Figura()

    while opcion != 0:
        print("Calculadora de Figuras")
        print("1. Triángulo")
        print("2. Círculo")
        print("3. Rectángulo")
        print("4. Hexágono")
        print("0. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            lado1 = float(input("Ingrese el primer lado del triángulo: "))
            lado2 = float(input("Ingrese el segundo lado del triángulo: "))
            lado3 = float(input("Ingrese el tercer lado del triángulo: "))

            fig = Triangulo(base, altura, lado1, lado2, lado3)
            print("Área del triángulo:", fig.calcularArea())
            print("Perímetro del triángulo:", fig.calcularPerimetro())

        elif opcion == 2:
            radio = float(input("Ingrese el radio del círculo: "))

            fig = Circulo(radio)
            print("Área del círculo:", fig.calcularArea())
            print("Perímetro del círculo:", fig.calcularPerimetro())

        elif opcion == 3:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))

            fig = Rectangulo(base, altura)
            print("Área del rectángulo:", fig.calcularArea())
            print("Perímetro del rectángulo:", fig.calcularPerimetro())

        elif opcion == 4:
            lado = float(input("Ingrese el lado del hexágono: "))

            fig = Hexagono(lado)
            print("Área del hexágono:", fig.calcularArea())
            print("Perímetro del hexágono:", fig.calcularPerimetro())

        elif opcion == 0:
            print("¡Hasta luego!")

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == '__main__':
    main()
