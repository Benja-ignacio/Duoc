package LearnJava.VariablesAndTypes;

public class numbers {
    public static void main(String[] args) {
        // Definir un entero
        int myNumber;
        myNumber = 5;
        // Puedes conbinarlos int Mynumber = 5;
        System.out.println("The number is: " + myNumber);

        // Definir un numero float doble -> 64 bytes 15 decimales aprox
        double d = 4.5;
        d = 3.0; // cambia el valor de d 
        

        // Definir un numero float -> 32 bytes 7 decimales aprox 
        float f = (float) 4.5;

        float g = 4.5f; // manera mas corta 



        System.out.println("numbers: " + d + f + g);
    }
}