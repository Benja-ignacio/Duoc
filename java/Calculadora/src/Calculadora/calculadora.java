package Calculadora;
import java.util.Scanner;


public class calculadora {
        Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        calculadora app = new calculadora();
        app.run();
    }

    private void run() {
        while (true) {
            System.out.println("=== CALCULADORA ===");
            System.out.println("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n: ");

            int opcion = input.nextInt();

            switch (opcion) {
                case 1:
                    
                    break;
                case 2:

                    break;

                case 3:
                    break;

                case 4:
                    break;
                default:
                    break;
            }
        }
    }

    private void escogerNumeros() {
        System.out.println("Ingrese el primer numero: ");
        int num1 = input.nextInt();
        System.out.println("Ingrese el segundo numero: ");
        int num2 = input.nextInt();

        par numeros = new par(num1, num2);
        RealizarCalculo(numeros.num1, numeros.num2);
    }

    private int RealizarCalculo(int num1, int num2, int opcion) {
        switch (opcion) {
            case 1:
                return num1 + num2;
            case 2:
                return num1 - num2;
            case 3:
                return num1 * num2;
            case 4:
                return num1 / num2;
            default:
                System.out.println("Opcion no valida.");
                break;
        }
    }
}
