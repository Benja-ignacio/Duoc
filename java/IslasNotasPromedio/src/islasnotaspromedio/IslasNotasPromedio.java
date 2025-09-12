package islasnotaspromedio;
import java.util.Scanner;

/**
 *
 * @author benjamin
 */
public class IslasNotasPromedio {
    
    
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        
        //Nota 1: do-while hasta que este en rango
        
        double nota1;
        
        do {
            System.out.println("Ingrese la nota 1: ");
            nota1 = input.nextDouble();
        } while (nota1 < 1.0  || nota1 > 7.0);        
        
        
        
        //Nota2
        double nota2;
        
        do {
            System.out.println("Ingrese la nota 2: ");
            nota2 = input.nextDouble();
        } while (nota1 < 1.0  || nota1 > 7.0);        
        
        //Nota 3
        double nota3;
        
        do {
            System.out.println("Ingrese la nota 3: ");
            nota3 = input.nextDouble();
        } while (nota1 < 1.0  || nota1 > 7.0);
   
        //Promedio
        double promedio = (nota1 + nota2 + nota3) / 3.0;
        
        //Mostrar resultado
        System.out.println("Notas ingresadas: " + nota1 + " , " + nota2 + " , " + nota3);
        System.out.println("Promedio: " + promedio);
    }
}
