/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ev_formativa;

/**
 *
 * @author Asus
 */

import java.util.Scanner;
import java.util.ArrayList;

public class Ev_formativa {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       Scanner teclado = new Scanner(System.in);
        ArrayList<Estudiante> listaEstudiantes = new ArrayList<>();
        ArrayList<Profesor> listaProfesores = new ArrayList<>();
        ArrayList<Asignatura> listaAsignaturas = new ArrayList<>();
        
        int opcion = 0;

        while (opcion != 4) {
            System.out.println("--- Menú del Sistema ---");
            System.out.println("1. Agregar Estudiante");
            System.out.println("2. Agregar Profesor");
            System.out.println("3. Agregar Asignatura");
            System.out.println("4. Calcular Nota Final de Asignatura");
            System.out.println("5. Salir");
            System.out.print("Elija una opción: ");
            opcion = teclado.nextInt();
            teclado.nextLine(); // Consumir el salto de línea

            switch (opcion) {
                case 1:
                    agregarEstudiante(teclado, listaEstudiantes);
                    break;
                case 2:
                    agregarProfesor(teclado, listaProfesores);
                    break;
                case 3:
                    agregarAsignatura(teclado, listaAsignaturas);
                    break;
                case 4:
                    calcularNotaFinal(teclado, listaAsignaturas);
                    break;
                case 5:
                        
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opción inválida. Intente de nuevo.");
            }
            System.out.println(); // Imprimir línea en blanco para mejor formato
        }
        
        teclado.close();
    }
    
    // Método para agregar un nuevo estudiante
    private static void agregarEstudiante(Scanner teclado, ArrayList<Estudiante> lista) {
        System.out.println("--- Agregando Estudiante ---");
        System.out.print("Ingrese RUT: ");
        String rut = teclado.nextLine();
        System.out.print("Ingrese nombre: ");
        String nombre = teclado.nextLine();
        System.out.print("Ingrese edad: ");
        int edad = teclado.nextInt();
        teclado.nextLine(); 
        System.out.print("Ingrese fecha de nacimiento: ");
        String fechaNacimiento = teclado.nextLine();

        Estudiante nuevoEstudiante = new Estudiante(rut, nombre, edad, fechaNacimiento);
        lista.add(nuevoEstudiante);
        System.out.println("Estudiante " + nuevoEstudiante.getNombre() + " agregado exitosamente.");
    }

    // Método para agregar un nuevo profesor
    private static void agregarProfesor(Scanner teclado, ArrayList<Profesor> lista) {
        System.out.println("--- Agregando Profesor ---");
        System.out.print("Ingrese RUT: ");
        String rut = teclado.nextLine();
        System.out.print("Ingrese nro_profesor: ");
        int nroProfesor = teclado.nextInt();
        teclado.nextLine();
        System.out.print("Ingrese nombre: ");
        String nombre = teclado.nextLine();
        System.out.print("Ingrese fecha de ingreso: ");
        String fechaIngreso = teclado.nextLine();
        System.out.print("Ingrese sede: ");
        String sede = teclado.nextLine();

        Profesor nuevoProfesor = new Profesor(rut, nroProfesor, nombre, fechaIngreso, sede);
        lista.add(nuevoProfesor);
        System.out.println("Profesor " + nuevoProfesor.getNombre() + " agregado exitosamente.");
    }
    
    // Método para agregar una nueva asignatura
    private static void agregarAsignatura(Scanner teclado, ArrayList<Asignatura> lista) {
        System.out.println("--- Agregando Asignatura ---");
        System.out.print("Ingrese código: ");
        String codigo = teclado.nextLine();
        System.out.print("Ingrese nombre de la asignatura: ");
        String nombreAsignatura = teclado.nextLine();
        System.out.print("Ingrese nombre del estudiante: ");
        String nombreEstudiante = teclado.nextLine();
        System.out.print("Ingrese nombre del profesor: ");
        String nombreProfesor = teclado.nextLine();
        System.out.print("Ingrese nota 1: ");
        double nota1 = teclado.nextDouble();
        System.out.print("Ingrese nota 2: ");
        double nota2 = teclado.nextDouble();
        System.out.print("Ingrese nota 3: ");
        double nota3 = teclado.nextDouble();
        teclado.nextLine();

        Asignatura nuevaAsignatura = new Asignatura(codigo, nombreAsignatura, nombreEstudiante, nombreProfesor, nota1, nota2, nota3);
        lista.add(nuevaAsignatura);
        System.out.println("Asignatura " + nuevaAsignatura.getNombreAsignatura() + " agregada exitosamente.");
    }
    
     // Nuevo método para calcular la nota final
    private static void calcularNotaFinal(Scanner teclado, ArrayList<Asignatura> lista) {
        if (lista.isEmpty()) {
            System.out.println("No hay asignaturas registradas para calcular la nota.");
            return;
        }

        System.out.println("--- Cálculo de Nota Final ---");
        System.out.print("Ingrese el nombre de la asignatura: ");
        String nombreAsignatura = teclado.nextLine();

        // Buscar la asignatura en la lista
        boolean encontrada = false;
        for (Asignatura a : lista) {
            if (a.getNombreAsignatura().equalsIgnoreCase(nombreAsignatura)) {
                double notaFinal = a.calcularNotaFinal();
                System.out.println("La nota final para " + a.getNombreAsignatura() + " es: " + String.format("%.2f", notaFinal));
                encontrada = true;
                break; // Salir del bucle una vez que la asignatura ha sido encontrada
            }
        }

        if (!encontrada) {
            System.out.println("Asignatura no encontrada. Por favor, verifique el nombre.");
        }
    }
}
