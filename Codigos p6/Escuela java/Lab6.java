
package lab6;

import java.util.Scanner;

public class Lab6 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int op;
        Persona persona = null;
        
        do {
            System.out.println("\nMenu de opciones:");
            System.out.println("1. Obtener información de Estudiante");
            System.out.println("2. Obtener información de Docente");
            System.out.println("3. Obtener información de PAAE");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");
            op = scanner.nextInt();

            switch (op) {
                case 1:
                    persona = new Estudiante(123, "Juan", "ABCD123", "Calle 123");
                    System.out.println("\n\tEstudiante:");
                    break;
                case 2:
                    persona = new Docente(456, "Maria", "EFGH456", "Avenida 456");
                    System.out.println("\n\tDocente:");
                    break;
                case 3:
                    persona = new PAAE(789, "Pedro", "IJKL789", "Plaza 789");
                    System.out.println("\n\tPAAE:");
                    break;
                case 4:
                    System.out.println("\nSaliendo del programa...");
                    break;
                default:
                    System.out.println("\nOpción inválida. Intente nuevamente.");
                    break;
            }
            
            if((op >= 1) && (op < 4)){
                System.out.println("Id: " + persona.obtenerId());
                System.out.println("Nombre: " + persona.obtenerNombre());
                System.out.println("CURP: " + persona.obtenerCURP());
                System.out.println("Domicilio: " + persona.obtenerDomicilio());
            }
            
        } while (op != 4);
        
    }
    
}
