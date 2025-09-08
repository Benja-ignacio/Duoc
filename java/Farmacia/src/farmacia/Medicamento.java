package farmacia;


/**
 *
 * @author benjamin
 */
public class Medicamento {
    
    // Atributos
    private String codigo, nombre, tipo, fecha;
    private int precio, stock;
    
    // constructores 

    public Medicamento() {
    }

    public Medicamento(String codigo, String nombre, String tipo, int precio, int stock, String fecha) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.tipo = tipo;
        this.precio = precio;
        this.stock = stock;
        this.fecha = fecha;
    }
    
    //getters

    public String getCodigo() {
        return codigo;
    }

    public String getNombre() {
        return nombre;
    }

    public String getTipo() {
        return tipo;
    }

    public int getPrecio() {
        return precio;
    }

    public int getStock() {
        return stock;
    }

    public String getFecha() {
        return fecha;
    }
    
    //setters

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public void setPrecio(int precio) {
        this.precio = precio;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    @Override
    public String toString() {
        return "Medicamento{" + "codigo=" + codigo + ", nombre=" + nombre + ", tipo=" + tipo + ", precio=" + precio + ", stock=" + stock + ", fecha=" + fecha + '}';
    }
    
    
    
    
}
