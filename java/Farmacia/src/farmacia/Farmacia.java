
package farmacia;
import java.util.Scanner;
import java.time.LocalDate;
/**
 *
 * @author benjamin
 */
public class Farmacia {

    static Scanner input = new Scanner(System.in);
    
    public static void main(String[] args) {
        Farmacia app = new Farmacia();
        app.run();
    }
    
    private void run() {
        // OBJETO
        Medicamento m1 = new Medicamento("abc1", "paracetamol", "analgesico", 1100, 20, LocalDate.of(2024, 12, 31));
        
        while (true) {
            System.out.println("TIENDA DE FARMACIA");
            System.out.println("1. Consultar medicamento.");
            System.out.println("2. Comprar medicamento.");
            System.out.println("3. ver stock");            
            System.out.println("4. Salir");
                    
            int opcion = input.nextInt();
            
            switch (opcion) {
                case 1:
                    System.out.println("Ingrese el nombre del medicamento que busca: ");
                    
                    String buscar = input.next();
                    
                    System.out.println("El medicamento " + buscar + " Se encuentra disponible");
                    
                    break;
                case 2:
                    System.out.println("Comprando...");
                    break;
                case 3:
                    System.out.println(m1);
                    break;
                case 4:
                    return;
                default:
                    System.out.println("Opcion invalida");
            }
                    
        }
    }
}
