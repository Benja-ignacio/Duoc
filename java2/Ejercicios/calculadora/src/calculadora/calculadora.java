package calculadora;
import java.util.Scanner;

import javax.swing.plaf.basic.BasicInternalFrameTitlePane.SystemMenuBar;


public class calculadora {
    private final java.util.Scanner input = new Scanner(System.in);

    public static void main(String[] args) {

        calculadora app = new calculadora();
        app.run();
    }

    private void run() {
        while (true) {
            System.out.println("---CALCULADORA---");
            System.out.println("\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Salir\n: ");

            int opcion = input.nextInt();

            switch (opcion) {
                case 1:
                    
                    break;
            
                case 2:

                case 3:

                case 4:
                return;

                default:
                System.out.println("Opcion invalida.");
            }

        }
    }

    private void ingresarDosNumeros(int num1, int num2) {
        System.out.println("Ingrese el numero 1: ");
        num1 = input.nextInt();
        System.out.println("Ingrese el numero 2: ");
        num2 = input.nextInt();
    }

    private void realizarCalculo(int num1, int num2, int opcion) {
        if (opcion == 1) {
            System.out.println(num1 + num2);
        }
        else if (opcion == 2) {
            System.out.println(num1 - num2);
            }
        else {
            System.out.println(num1 * num2);
        } 
    }
}

