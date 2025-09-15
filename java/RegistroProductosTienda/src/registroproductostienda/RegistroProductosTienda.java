package registroproductostienda;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Scanner;


public class RegistroProductosTienda {
    static Scanner input = new Scanner(System.in);
    ArrayList<Producto> listaProductos = new ArrayList<>();
    private final DateTimeFormatter DATE_FMT = DateTimeFormatter.ofPattern("dd-MM-yyyy");

    public static void main(String[] args) {
    RegistroProductosTienda app = new RegistroProductosTienda();
    app.run();
    }
    
    private void run() {
        Producto p1 = new Producto("ab123", "Chocman", 500, LocalDate.of(2025,9,14));
        listaProductos.add(p1);
        
        while (true) {
            System.out.println(" === REGISTRO DE PRODUCTOS DE TIENDA ===\n1. Agregar producto\n2. Listar productos\n3. Actualizar producto (Nombre, Fecha, Precio)\n4. Eliminar producto\n0. Salir ");
        
            int opcion = input.nextInt();
            input.nextLine();
            
            switch (opcion) {
                case 1:
                    agregarProducto(listaProductos);
                    break;
                case 2:
                    listarProductos(listaProductos);
                    break;
                case 3:
                    actualizarProducto(listaProductos);
                    break;
                case 4:
                    eliminarProducto(listaProductos);
                    break;
                case 0:
                    return;
            }    
        }
    }
    
    
    //METODOS
    
    private void agregarProducto(ArrayList<Producto> productos) {
        String codigo = validarString("Codigo del producto: ");
        String nombre = validarString("Nombre del producto");
        Double precio = validarDouble("Precio del producto:");
        LocalDate fechaVencimiento = validarFecha("Fecha de vencimiento del producto:");
        
        Producto nuevoProducto = new Producto(codigo, nombre, precio, fechaVencimiento);
        listaProductos.add(nuevoProducto);
        System.out.println("Producto " + nuevoProducto.getNombre() + "agregado.");
    }
    
    private void listarProductos(ArrayList<Producto> productos) {
        for (Producto i: productos) {
            System.out.println("Codigo: " + i.getCodigo() + " Nombre: " + i.getNombre() + " Precio: " +  i.getPrecio() + " Fecha: " + i.getFechaVencimiento().format(DATE_FMT) + "\n");
        }
    }
    
    private void actualizarProducto(ArrayList<Producto> productos){
        String codigo = validarString("Codigo del producto:");
        
        for (Producto i: productos) {
            if (i.getCodigo().equals(codigo)) {
                System.out.println("1. Cambiar nombre \n2. Cambiar fecha\n 3. Cambiar precio");
                int opcion = input.nextInt();
                input.nextLine();
                
                switch (opcion) {
                    case 1:
                           String nuevoNombre = validarString("Nuevo nombre:");
                           i.setNombre(nuevoNombre);
                           System.out.println("Nombre actualizado correctamente!");
                           break;
                    case 2:
                           LocalDate nuevaFechaVencimiento = validarFecha("Nueva fecha de vencimiento:");
                           i.setFechaVencimiento(nuevaFechaVencimiento);
                           System.out.println("Fecha actualizada correctamente!");
                           break;
                    case 3:
                           double nuevoPrecio = validarDouble("Nuevo precio:");
                           i.setPrecio(nuevoPrecio);
                           System.out.println("Precio actualizado correctamente!");
                           break;
                    default:
                        return;
                }
                return;
            }
        }
        System.out.println("No se encontro ningun producto.");
    }
    
    private void eliminarProducto(ArrayList<Producto> productos) {
        String codigo = validarString("Codigo del producto:");
        boolean eliminado = listaProductos.removeIf(i -> i.getCodigo().equals(codigo));
        
        if (eliminado) {
            System.out.println("Producto eliminado correctamente!");
        } else {
            System.out.println("No se encontro ningun producto.");
        }

    }
    // validaciones
    private double validarDouble(String prompt) {
        double numero;

        do {
            System.out.println(prompt);
            numero = input.nextDouble();
            input.nextLine(); //Limpiar buffer
           
        } while (numero < 0);
        return numero;
    } 
    
    private LocalDate validarFecha(String prompt) {
    System.out.println(prompt);                   // 1) mostramos el mensaje (ej: "Fecha (dd-MM-yyyy):")
    String textoFecha = input.nextLine();            // 2) leemos la línea completa como texto
    if (textoFecha != null) textoFecha = textoFecha.trim(); // 3) quitamos espacios al inicio y final
        return LocalDate.parse(textoFecha, DATE_FMT); // 4) convertimos el texto a LocalDate usando el formato fijo
        // (si el usuario escribe algo que no calza con "dd-MM-yyyy", el programa se cae)
    }
   
    private String validarString(String prompt) {
        String texto;
        do {
            System.out.println(prompt);
            texto = input.nextLine().trim();
        } while (texto.isEmpty());
        return texto;
    }
}

   