package AutoMotora.src;

public class AutoMotora {
    public static void main(String[] args) {
        System.out.println("Bienvenido a la Automotora!");

        // Crear un objeto de la clase auto

        Auto auto1 = new Auto();
        auto1.color = "Rojo";
        auto1.marca = "Nissan";
        auto1.modelo = "Liqui Pathfinder";
        auto1.anio = 1987;
        auto1.precio = 5_000_000;

    }
}

class Auto {
    // Atributos
    String color;
    String marca; 
    String modelo;
    int anio;
    double precio;

    // Metodos 
    void MostrarInfo() {
        System.err.println("Marca: " + marca);
        System.err.println("Color: " + color);
        System.err.println("Modelo: " + modelo);
        System.err.println("Año: " + anio);
        System.err.println("Precio " + precio);
    }
}

