/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package tienda;

/**
 *
 * @author Admin
 */
public class Cliente {
    
    //Atributos
    private String idCliente;
    private String nombre;
    private CarritoCompra carrito;
    
    // Constructor
    public Cliente(String idCliente, String nombre, CarritoCompra carrito) {
        this.idCliente = idCliente;
        this.nombre = nombre;
        this.carrito = carrito;
    }

    public Cliente() {
    }
 
    //Getters
    public String getIdCliente() {
        return idCliente;
    }

    public String getNombre() {
        return nombre;
    }

    public CarritoCompra getCarrito() {
        return carrito;
    }

    
    //Setters
    public void setIdCliente(String idCliente) {
        this.idCliente = idCliente;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setCarrito(CarritoCompra carrito) {
        this.carrito = carrito;
    }

    @Override
    public String toString() {
        return "Cliente{" + "idCliente=" + idCliente + ", nombre=" + nombre + ", carrito=" + carrito + '}';
    }
    
    
}
