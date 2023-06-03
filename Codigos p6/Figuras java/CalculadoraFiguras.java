import java.util.Scanner;


public class CalculadoraFiguras {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcion;
        double base, altura, lado, radio;

        do {
            System.out.println("Calculadora de Figuras");
            System.out.println("1. Triángulo");
            System.out.println("2. Círculo");
            System.out.println("3. Rectángulo");
            System.out.println("4. Hexágono");
            System.out.println("0. Salir");
            System.out.print("Ingrese una opción: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese la base del triángulo: ");
                    base = scanner.nextDouble();
                    System.out.print("Ingrese la altura del triángulo: ");
                    altura = scanner.nextDouble();
                    System.out.print("Ingrese el primer lado del triángulo: ");
                    double lado1 = scanner.nextDouble();
                    System.out.print("Ingrese el segundo lado del triángulo: ");
                    double lado2 = scanner.nextDouble();
                    System.out.print("Ingrese el tercer lado del triángulo: ");
                    double lado3 = scanner.nextDouble();

                    Triangulo triangulo = new Triangulo(base, altura, lado1, lado2, lado3);
                    System.out.println("Área del triángulo: " + triangulo.calcularArea());
                    System.out.println("Perímetro del triángulo: " + triangulo.calcularPerimetro());
                    break;

                case 2:
                    System.out.print("Ingrese el radio del círculo: ");
                    radio = scanner.nextDouble();

                    Circulo circulo = new Circulo(radio);
                    System.out.println("Área del círculo: " + circulo.calcularArea());
                    System.out.println("Perímetro del círculo: " + circulo.calcularPerimetro());
                    break;

                case 3:
                    System.out.print("Ingrese la base del rectángulo: ");
                    base = scanner.nextDouble();
                    System.out.print("Ingrese la altura del rectángulo: ");
                    altura = scanner.nextDouble();

                    Rectangulo rectangulo = new Rectangulo(base, altura);
                    System.out.println("Área del rectángulo: " + rectangulo.calcularArea());
                    System.out.println("Perímetro del rectángulo: " + rectangulo.calcularPerimetro());
                    break;

                case 4:
                    System.out.print("Ingrese el lado del hexágono: ");
                    lado = scanner.nextDouble();

                    Hexagono hexagono = new Hexagono(lado);
                    System.out.println("Área del hexágono: " + hexagono.calcularArea());
                    System.out.println("Perímetro del hexágono: " + hexagono.calcularPerimetro());
                    break;

                case 0:
                    System.out.println("¡Hasta luego!");
                    break;

                default:
                    System.out.println("Opción inválida. Intente nuevamente.");
            }

            System.out.println();
        } while (opcion != 0);

        scanner.close();
    }
}
