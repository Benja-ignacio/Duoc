/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package tienda;

/**
 *
 * @author Admin
 */
public class CarritoCompra {
    
    //Atributos
    private String producto;
    private double total;

    public CarritoCompra(String producto, double total) {
        this.producto = producto;
        this.total = total;
    }

    //Getters
    public String getProducto() {
        return producto;
    }

    public double getTotal() {
        return total;
    }

    //Setters
    public void setProducto(String producto) {
        this.producto = producto;
    }

    public void setTotal(double total) {
        this.total = total;
    }

    @Override
    public String toString() {
        return "CarritoCompra{" + "producto=" + producto + ", total=" + total + '}';
    }
    
    
    
}
