package calculadora1;
import java.util.Scanner;

import javax.swing.plaf.basic.BasicInternalFrameTitlePane.SystemMenuBar;


public class calculadora1 {
    private final java.util.Scanner input = new Scanner(System.in);

    public static void main(String[] args) {

        calculadora1 app = new calculadora1();
        app.run();
    }

    private void run() {
        while (true) {
            System.out.println("---CALCULADORA---");
            System.out.println("\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Salir\n: ");

            int opcion = input.nextInt();

            switch (opcion) {
                case 1:
                    par sumar = ingresarDosNumeros();
                    realizarCalculo(sumar.num1, sumar.num2, 1);
                    break;
                case 2:
                    par restar = ingresarDosNumeros();
                    realizarCalculo(restar.num1, restar.num2, 2);

                case 3:
                    par multiplicar = ingresarDosNumeros();
                    realizarCalculo(multiplicar.num1, multiplicar.num2, 3);
                    
                case 4:
                return;
                default:
                System.out.println("Opcion invalida.");
            }

        }
    }

    private par ingresarDosNumeros() {
        System.out.println("Ingrese el numero 1: ");
        int num1 = input.nextInt();
        System.out.println("Ingrese el numero 2: ");
        int num2 = input.nextInt();
        
        return new par(num1, num2);
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

