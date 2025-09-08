/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pizzeria;

/**
 *
 * @author benjamin
 */
public class Pizza {
    
    // Atributos
    private String nombre, tamano, masa;

    // Constructor con parametro
    public Pizza(String nombre, String tamano, String masa) {
        this.nombre = nombre;
        this.tamano = tamano;
        this.masa = masa;
    }

    // Accesadores y mutadores
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTamano() {
        return tamano;
    }

    public void setTamano(String tamano) {
        this.tamano = tamano;
    }

    public String getMasa() {
        return masa;
    }

    public void setMasa(String masa) {
        this.masa = masa;
    }
    
    
    
    
    // Metodos 
    public void preparar() {
        System.out.println("Se esta preparando la pizza.");
    }
    
    public void calentar(){
        System.out.println("Se esta horneando la pizza");
    }
}
