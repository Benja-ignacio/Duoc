package registroproductostienda;
import java.time.LocalDate;

public class Producto {
    private String codigo;
    private String nombre;
    private double precio;
    private LocalDate fechaVencimiento;

    public Producto() {
    }

    public Producto(String codigo, String nombre, double precio, LocalDate fecha) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.precio = precio;
        this.fechaVencimiento = fecha;
    }

    public String getCodigo() {
        return codigo;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public LocalDate getFechaVencimiento() {
        return fechaVencimiento;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public void setFechaVencimiento(LocalDate fechaVencimiento) {
        this.fechaVencimiento = fechaVencimiento;
    }

    @Override
    public String toString() {
        return "Producto{" + "codigo=" + codigo + ", nombre=" + nombre + ", precio=" + precio + ", fechaVencimiento=" + fechaVencimiento + '}';
    }

  
            
}
