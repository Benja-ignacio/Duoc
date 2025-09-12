package farmacia_comunitaria;
import java.time.LocalDate;

public class Medicamento {
    
    //Atributos 
    private String codigo;
    private String nombre;
    private String tipo; // Tipo de medicamento
    private int stock;
    private LocalDate fecha;

    //constructores
    public Medicamento(String codigo, String nombre, String tipo, int stock, LocalDate fecha) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.tipo = tipo;
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

    public int getStock() {
        return stock;
    }

    public LocalDate getFecha() {
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

    public void setStock(int stock) {
        this.stock = stock;
    }

    public void setFecha(LocalDate fecha) {
        this.fecha = fecha;
    }

    
    
}

