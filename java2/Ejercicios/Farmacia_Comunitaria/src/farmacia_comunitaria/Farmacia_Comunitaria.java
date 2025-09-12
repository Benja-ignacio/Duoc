package farmacia_comunitaria;
import java.util.ArrayList;
import java.time.LocalDate;
import java.util.List;
import java.time.format.DateTimeParseException;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Farmacia_Comunitaria {
    private final List<Medicamento> medicamento = new ArrayList<>();
    private final List<Cliente> cliente = new ArrayList<>();
    private final List<ProveedorFarmaceutico> proveedor = new ArrayList<>();
    private final List<SistemaDeGestionDeInventarios> inventario = new ArrayList<>();
    private final Scanner teclado = new Scanner(System.in);
    private int opcion;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Farmacia_Comunitaria app = new Farmacia_Comunitaria();
        app.run();
    }
    
    private void run(){
        while (true){
            System.out.println("=== Farmacia Comunitaria===");
            System.out.println("1. Comprar Medicamento");
            System.out.println("2. Consultar Medicamento");
            System.out.println("3. Salir");
            
            opcion = teclado.nextInt();
            
            if (opcion == 1) System.out.println("op1");
            else if (opcion == 2) System.out.println("op2");
            else if (opcion == 3) break;
            else System.out.println("Opcion invalida");
        }
    }
    
}
