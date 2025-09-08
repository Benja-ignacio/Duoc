package tienda;

import java.time.LocalDate;

/**
 *
 * @author benjamin
 */
public class Medicamento {
    // ATRIBUTOS
    private String codigo;
    private String nombre;
    private String tipo;
    private int stock;
    private LocalDate fecha;
    
    // Constructores
    public Medicamento() {
    }

    public Medicamento(String codigo, String nombre, String tipo, int stock, LocalDate fecha) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.tipo = tipo;
        this.stock = stock;
        this.fecha = fecha;
    }
     
    // Getters
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

    // Setters
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
    
    // Método toString para representación en texto
    @Override
    public String toString() {
        return "Medicamento{" +
                "codigo='" + codigo + '\'' +
                ", nombre='" + nombre + '\'' +
                ", tipo='" + tipo + '\'' +
                ", stock=" + stock +
                ", fecha=" + fecha +
                '}';
    }
}
