package ToDoList;

public class Tareas {

    private String codigo;
    private String descripcion;
    private String estado;
    
    public Tareas() {
    }

    public Tareas(String codigo, String descripcion, String estado) {
        this.codigo = codigo;
        this.descripcion = descripcion;
        this.estado = estado;
    }

    public String getCodigo() {
        return codigo;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public String getEstado() {
        return estado;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    @Override
    public String toString() {
        return "Tareas [codigo=" + codigo + ", descripcion=" + descripcion + ", estado=" + estado + "]";
    }

    

    
}
