package tienda;

import java.time.LocalDate;
import java.util.Scanner;


public class Tienda {
    
    static Scanner teclado = new Scanner(System.in);
    static int op;

    public static void main(String[] args) {
        Medicamento m1 = new Medicamento("abc123", "Paracetamol", "Analgesico", 100, LocalDate.of(2024, 12, 31));

        Tienda app = new Tienda();
        app.run();

        // TODO code application logic here
        //System.out.println("Ingrese un numero: ");
        //op = teclado.nextInt();
        //System.out.println("Ingreso el numero: " + op);
        //String datos = "Codigo: " + m1.getCodigo() + " Nombre: " + m1.getNombre() + " Tipo: " + m1.getTipo() + " Stock: " + m1.getStock() + " Fecha: " + m1.getFecha();
        //System.out.println(datos);
        //Cambiar nombre
        //m1.setNombre("hola");        
        //Obtener nombre
        //String nombre = m1.getNombre();
        //System.out.println("Usted ha comprado un " + nombre);
    }