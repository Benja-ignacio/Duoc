package escuela;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Escuela {
    private final Scanner input = new Scanner(System.in);
    private final List<Libro> libros = new ArrayList<>();

    public static void main(String[] args) {
        Escuela app = new Escuela();
        Biblioteca bib = new Biblioteca();

        // Crear libros
        Libro libro1 = new Libro("abc123", "Bleach", "Tite Kubo", 2002);
        Libro libro2 = new Libro("uwu123", "Naruto", "Masashi Kishimoto", 2001);
        Libro libro3 = new Libro("owo123", "Burn the Witch", "Tite Kubo", 2018);

        // Agregar libros a la lista
        app.libros.add(libro1);
        app.libros.add(libro2);
        app.libros.add(libro3);

        // Mostrar libros
        for (Libro l : app.libros) {
            System.out.println(l);
        }

        // Pedir código al usuario
        System.out.print("\nIngrese el código del libro a buscar: ");
        String test = app.input.nextLine();

        // Buscar libro
        Libro buscar = bib.buscarLibroPorCodigo(test, app.libros);

        if (buscar != null) {
            System.out.println("Libro encontrado: " + buscar.getTitulo() + " de " + buscar.getAutor() + " (" + buscar.getAnioPublicacion() + ")");
        } else {
            System.out.println("No se encontró un libro con ese código.");
        }
    }
}
