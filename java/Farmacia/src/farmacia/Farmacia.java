package farmacia;
import java.util.Scanner;
import java.time.LocalDate;
import java.util.ArrayList;


public class Farmacia {

    //static Scanner input = new Scanner(System.in);
    //ArrayList<Medicamento> listaMedicamento = new ArrayList<>();
    static Scanner input = new Scanner(System.in);
    ArrayList<Medicamento> listaMedicamento = new ArrayList<>();

    public static void main(String[] args) {
        Farmacia app = new Farmacia();
        app.run();
    }
    
    
    
    private void run() {
        // OBJETO
        Medicamento m1 = new Medicamento("abc1", "paracetamol", "analgesico", 1100, 20, "08-09-25");
        listaMedicamento.add(m1);
        while (true) {
            System.out.println("TIENDA DE FARMACIA");
            System.out.println("1. Consultar medicamento.");
            System.out.println("2. Comprar medicamento.");
            System.out.println("3. ver stock");            
            System.out.println("4. Agregar Medicamento");            
            System.out.println("5. Salir");
                    
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
                    System.out.println("Codigo: " + listaMedicamento.get(0) + " Nombre: " + listaMedicamento.get(1) + " Tipo: " + listaMedicamento.get(2) + " Precio: " + listaMedicamento.get(3) + " Stock: " + listaMedicamento.get(4) + " Fecha: " + listaMedicamento.get(5));
                    break;  
                case 4:
                    AgregarMedicamento(input, listaMedicamento);
                    break;
                case 5:
                    return;
                default:
                    System.out.println("Opcion invalida");
            }
                    
        }   
    }
    private void AgregarMedicamento(Scanner input, ArrayList<Medicamento> lista) {
        System.out.println("Ingrese el codigo del medicamento: ");
        String codigo = input.next();
        System.out.println("Ingrese el nombre del medicamento: ");
        String nombre = input.next();
        System.out.println("Ingrese el tipo del medicamento: ");
        String tipo = input.next();
        System.out.println("Ingrese el precio del medicamento: ");
        int precio = input.nextInt();
        System.out.println("Ingrese el stock del medicamento: ");
        int stock = input.nextInt();
        System.out.println("Ingrese la fecha de ingreso del medicamento: ");
        String fecha = input.next();
        
        Medicamento MedicamentoNuevo = new Medicamento(codigo, nombre, tipo, precio, stock, fecha);
        lista.add(MedicamentoNuevo);
        
        System.out.println("Medicamento" + MedicamentoNuevo.getNombre() + " agregado correctamente.");
    }
}
