/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ev_formativa;

/**
 *
 * @author Asus
 */
public class Asignatura {
// Atributos de la clase Asignatura.
    private String codigo;
    private String nombreAsignatura;
    private String nombreEstudiante;
    private String nombreProfesor;
    private double nota1;
    private double nota2;
    private double nota3;

    // Constructor para inicializar una nueva asignatura con sus datos.
    public Asignatura(String codigo, String nombreAsignatura, String nombreEstudiante, String nombreProfesor, double nota1, double nota2, double nota3) {
        this.codigo = codigo;
        this.nombreAsignatura = nombreAsignatura;
        this.nombreEstudiante = nombreEstudiante;
        this.nombreProfesor = nombreProfesor;
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.nota3 = nota3;
    }
    
     // Este método debe ser público para ser accesible desde otras clases.
    public double calcularNotaFinal() {
        return (nota1 + nota2 + nota3) / 3.0;
    }

    public String getNombreAsignatura() {
        return nombreAsignatura;
    }
}
