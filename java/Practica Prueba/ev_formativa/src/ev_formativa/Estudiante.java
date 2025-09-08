/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ev_formativa;

/**
 *
 * @author Asus
 */
public class Estudiante {
    // Atributos de la clase Estudiante, definidos como privados para encapsular la información.
    private String rut;
    private String nombre;
    private int edad;
    private String fechaNacimiento;

    // Constructor de la clase Estudiante. Se usa para inicializar un objeto con todos sus datos.
    public Estudiante(String rut, String nombre, int edad, String fechaNacimiento) {
        this.rut = rut;
        this.nombre = nombre;
        this.edad = edad;
        this.fechaNacimiento = fechaNacimiento;
    }
    
    // Getters para acceder a los atributos
    public String getNombre() {
        return nombre;
    }
}
