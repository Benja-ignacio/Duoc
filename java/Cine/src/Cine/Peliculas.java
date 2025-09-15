package Cine;

public class Peliculas {

    private String codigo;
    private String titulo;
    private String genero;
    private String duracion;
    private String clasificacion;
    
    public Peliculas() {
    }

    public Peliculas(String codigo, String titulo, String genero, String duracion, String clasificacion) {
        this.codigo = codigo;
        this.titulo = titulo;
        this.genero = genero;
        this.duracion = duracion;
        this.clasificacion = clasificacion;
    }

    public String getCodigo() {
        return codigo;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getGenero() {
        return genero;
    }

    public String getDuracion() {
        return duracion;
    }

    public String getClasificacion() {
        return clasificacion;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public void setDuracion(String duracion) {
        this.duracion = duracion;
    }

    public void setClasificacion(String clasificacion) {
        this.clasificacion = clasificacion;
    }

    @Override
    public String toString() {
        return "Peliculas [codigo=" + codigo + ", titulo=" + titulo + ", genero=" + genero + ", duracion=" + duracion
                + ", clasificacion=" + clasificacion + "]";
    }

    


    
}
