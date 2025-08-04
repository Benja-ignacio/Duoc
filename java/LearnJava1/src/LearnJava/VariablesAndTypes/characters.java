package LearnJava.VariablesAndTypes;

public class characters {
    public static void main (String[] args) {

        // char = unico caracter 
        char c = 'c';
        System.out.println(c);

        // Crear string con un contructor 
        String s1 = new String("Hello :)");

        // Solo unsando "" Crea un string asi que no es necesario de la forma anterior 
        String s2 = "who who who who";

        // java define el operador + en strings para concatenar 
        String s3 = s1 + s2;
        System.out.println(s3);
    }
}