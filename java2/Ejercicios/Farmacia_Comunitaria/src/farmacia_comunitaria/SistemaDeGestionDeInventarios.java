package farmacia_comunitaria;


public class SistemaDeGestionDeInventarios {
    
    //atributos
    private String medicamentoActual; //Medicamento actualmente destacado en el sistema
    private String clienteActual; //Cliente actualmente en interaccion con el sistema

    
    //constructores
    public SistemaDeGestionDeInventarios(String medicamentoActual, String clienteActual) {
        this.medicamentoActual = medicamentoActual;
        this.clienteActual = clienteActual;
    } 
    
    
    //getters 
    public String getMedicamentoActual() {
        return medicamentoActual;
    }

    public String getClienteActual() {
        return clienteActual;
    }
    
    //setters
    public void setMedicamentoActual(String medicamentoActual) {
        this.medicamentoActual = medicamentoActual;
    }

    public void setClienteActual(String clienteActual) {
        this.clienteActual = clienteActual;
    }
    
}
