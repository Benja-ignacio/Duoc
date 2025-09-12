package farmacia_comunitaria;

public class Cliente {
    
    //Atributos 
    private String NumeroCliente;
    private String nombre;
    private String MedicamentoAdquirido; // Medicamento adquirido por el cliente 
   
    
    //Constructores
    public Cliente(String NumeroCliente, String nombre, String MedicamentoAdquirido) {
        this.NumeroCliente = NumeroCliente;
        this.nombre = nombre;
        this.MedicamentoAdquirido = MedicamentoAdquirido;
    }

    //getters

    public String getNumeroCliente() {
        return NumeroCliente;
    }

    public String getNombre() {
        return nombre;
    }

    public String getMedicamentoAdquirido() {
        return MedicamentoAdquirido;
    }

    //seters

    public void setNumeroCliente(String NumeroCliente) {
        this.NumeroCliente = NumeroCliente;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setMedicamentoAdquirido(String MedicamentoAdquirido) {
        this.MedicamentoAdquirido = MedicamentoAdquirido;
    }
    
    
}
