package escuela;

import java.util.List;

public class Biblioteca {

    // Método para buscar un libro por su código
    public Libro buscarLibroPorCodigo(String codigo, List<Libro> libros) {
        for (Libro libro : libros) {
            if (libro.getCodigo().equals(codigo)) {
                return libro; // devuelve el objeto completo
            }
        }
        return null; // no se encontró
    }
}
