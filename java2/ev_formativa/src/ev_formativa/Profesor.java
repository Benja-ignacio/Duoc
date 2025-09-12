/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ev_formativa;

/**
 *
 * @author Asus
 */
public class Profesor {
     // Atributos de la clase Profesor.
    private String rut;
    private int nroProfesor;
    private String nombre;
    private String fechaIngreso;
    private String sede;

    // Constructor para inicializar un nuevo objeto Profesor.
    public Profesor(String rut, int nroProfesor, String nombre, String fechaIngreso, String sede) {
        this.rut = rut;
        this.nroProfesor = nroProfesor;
        this.nombre = nombre;
        this.fechaIngreso = fechaIngreso;
        this.sede = sede;
    }
    
    // Getters
    public String getNombre() {
        return nombre;
    }
}
