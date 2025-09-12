/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tienda;

/**
 *
 * @author Admin
 */
public class Tienda {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Producto p1 = new Producto("a1", "Helado", 1000);
        CarritoCompra carrito = new CarritoCompra(p1.toString(), 0);
        Cliente c1 = new Cliente("abc1", "Benjamin", carrito);
        
        c1.getCarrito().getTotal();
        System.out.println(c1);
    }
    
}
