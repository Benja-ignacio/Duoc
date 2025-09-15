package Cine;
import java.util.Scanner;
import java.util.ArrayList;


public class Cine {

    static Scanner input = new Scanner(System.in);
    ArrayList<Peliculas> listaPeliculas = new ArrayList<>();

    public static void main(String[] args) {
        Cine app = new Cine();
        app.run();
    }

    private void run() {
        Peliculas p1 = new Peliculas("Abc123", "Batman", "Accion", "2:00:00", "+18");
        Peliculas p2 = new Peliculas("owo123", "test", "test", "2:00:00", "+18");

        listaPeliculas.add(p1);
        listaPeliculas.add(p2);



        while (true) {
            System.out.println(" === CINE ===\n1. Registrar pelicula\n2. Mostrar todas las peliculas\n3. Buscar por genero\n4. Actualizar duracion\n5. Eliminar pelicula\n0. Salir");
            int opcion = input.nextInt();
            input.nextLine(); //Limpiar buffer

            switch (opcion) {

                case 1:
                    registrarPelicula(listaPeliculas);
                    break;
                case 2:
                    mostrarPeliculas(listaPeliculas);
                    break;
                case 3:
                    buscarPorGenero(listaPeliculas);
                    break;
                case 4:
                    actualizarDuracion(listaPeliculas);
                    break;
                case 5:
                    eliminarPelicula(listaPeliculas);
                    break;
                case 0:
                    return;
                default:
                    System.out.println("Opcion invalida.");
            }
        }
    }

    private String validarString(String prompt) {
        String texto;

        do {
            System.out.println(prompt);
            texto = input.nextLine().trim();
        } while (texto.isEmpty());
        return texto;
    } 

    private void registrarPelicula(ArrayList<Peliculas> peliculas) {
        String codigo = validarString("Codigo:");
        String titulo = validarString("Titulo:");
        String genero = validarString("Genero:");
        String duracion = validarString("Duracion:");
        String clasificacion = validarString("Clasificacion:");

        Peliculas nuevaPelicula = new Peliculas(codigo, titulo, genero, duracion, clasificacion);
        peliculas.add(nuevaPelicula);
        System.out.println("Pelicula " + nuevaPelicula.getTitulo() + " agregada.");
    }

    private void mostrarPeliculas(ArrayList<Peliculas> peliculas) {
        for (Peliculas i: peliculas) {
            System.out.println("Codigo: " + i.getCodigo() + "\nTitulo: " + i.getTitulo() + "\nGenero: " + i.getGenero() + "\nDuracion: " + i.getDuracion() + "\nClasificacion: " + i.getClasificacion() + "\n");
        }
    }

    private void buscarPorGenero(ArrayList<Peliculas> peliculas) {
        String genero = validarString("Genero de la pelicula: ");
        boolean encontrado = false;
        for (Peliculas i: peliculas) {
            if (i.getGenero().equals(genero)) {
                System.out.println("Titulo: " + i.getTitulo());
                encontrado = true;
            }
        }

        if (!encontrado) {
            System.out.println("\nNo se encontraron peliculas de genero " + genero);
        }
        pausa();
    }

    private void pausa() {
        System.out.println("\nPresione ENTER para continuar... ");
        input.nextLine();
    }

    private void actualizarDuracion(ArrayList<Peliculas> peliculas) {
        String codigo = validarString("Codigo de la pelicula:");
        boolean encontrado = false;
        
        for (Peliculas i: peliculas) {
            if (i.getCodigo().equals(codigo)) {
                encontrado = true;
                System.out.println("\nTitulo: " + i.getTitulo() + "\nDuracion: " + i.getDuracion());
                String nuevaDuracion = validarString("\nNueva duracion: ");
                i.setDuracion(nuevaDuracion);
                System.out.println("Se ha actualizado la duracion de " + i.getDuracion() + " a la nueva duracion de " + nuevaDuracion);   
                pausa();             
            }
        }
        if (!encontrado) {
            System.out.println("No se ha encontrado ninguna pelicula.");
        } 
        pausa();
    }

    private void eliminarPelicula(ArrayList<Peliculas> peliculas) {
        String codigo = validarString("Codigo de la pelicula:");
        boolean eliminado = listaPeliculas.removeIf(i -> i.getCodigo().equals(codigo));

        if (eliminado) {
            System.out.println("Pelicula eliminada.");
        } else {
            System.out.println("No se encontro ninguna pelicula");
        }
    }
}