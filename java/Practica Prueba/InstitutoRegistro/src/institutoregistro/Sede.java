package institutoregistro;

public class Sede {
    private int numero;
    private String nombre;
    private String comuna;

    public Sede(int numero, String nombre, String comuna) {
        this.numero = numero;
        this.nombre = nombre;
        this.comuna = comuna;
    }

    public int getNumero() { return numero; }
    public void setNumero(int numero) { this.numero = numero; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getComuna() { return comuna; }
    public void setComuna(String comuna) { this.comuna = comuna; }

    @Override
    public String toString() {
        return "Sede{" +
               "numero=" + numero +
               ", nombre='" + nombre + "'" +
               ", comuna='" + comuna + "'" +
               "}";
    }
}
