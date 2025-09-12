package farmacia_comunitaria;


public class ProveedorFarmaceutico {
    
    //atributos
    private String codigoProveedor;
    private String nombre;
    private String medicamentoSuministrado; // Ultimo medicamento suministrado por el proveedor

    
    //constructores
    public ProveedorFarmaceutico(String codigoProveedor, String nombre, String medicamentoSuministrado) {
        this.codigoProveedor = codigoProveedor;
        this.nombre = nombre;
        this.medicamentoSuministrado = medicamentoSuministrado;
    }
    
    
    //getters
    public String getCodigoProveedor() {
        return codigoProveedor;
    }

    public String getNombre() {
        return nombre;
    }

    public String getMedicamentoSuministrado() {
        return medicamentoSuministrado;
    }
    
    //setters
    public void setCodigoProveedor(String codigoProveedor) {
        this.codigoProveedor = codigoProveedor;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setMedicamentoSuministrado(String medicamentoSuministrado) {
        this.medicamentoSuministrado = medicamentoSuministrado;
    }
    
}
