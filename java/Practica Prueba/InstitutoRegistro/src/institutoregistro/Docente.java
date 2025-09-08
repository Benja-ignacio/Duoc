package institutoregistro;

import java.time.LocalDate;

public class Docente {
    private String rut;
    private String numeroDocente;
    private String nombre;
    private LocalDate fechaIngreso;
    private Sede sede;

    public Docente(String rut, String numeroDocente, String nombre, LocalDate fechaIngreso, Sede sede) {
        this.rut = rut;
        this.numeroDocente = numeroDocente;
        this.nombre = nombre;
        this.fechaIngreso = fechaIngreso;
        this.sede = sede;
    }

    public String getRut() { return rut; }
    public void setRut(String rut) { this.rut = rut; }

    public String getNumeroDocente() { return numeroDocente; }
    public void setNumeroDocente(String numeroDocente) { this.numeroDocente = numeroDocente; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public LocalDate getFechaIngreso() { return fechaIngreso; }
    public void setFechaIngreso(LocalDate fechaIngreso) { this.fechaIngreso = fechaIngreso; }

    public Sede getSede() { return sede; }
    public void setSede(Sede sede) { this.sede = sede; }

    @Override
    public String toString() {
        return "Docente{" +
               "rut='" + rut + "'" +
               ", numeroDocente='" + numeroDocente + "'" +
               ", nombre='" + nombre + "'" +
               ", fechaIngreso=" + fechaIngreso +
               ", sede=" + (sede != null ? sede.getNombre() : "sin sede") +
               "}";
    }
}
