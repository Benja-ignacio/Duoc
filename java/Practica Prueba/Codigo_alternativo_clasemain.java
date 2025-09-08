package registroinstituto;

import java.time.LocalDate; //Qué es: una fecha sin hora ni zona (solo AAAA-MM-DD) Se usa en Campos y variables
import java.time.format.DateTimeFormatter; //Qué es: define el formato de texto para parsear/mostrar fechas.
import java.time.format.DateTimeParseException; //Qué es: la excepción que lanza LocalDate.parse(...) Capturar el error y volver a pedir la fecha, en lugar de que el programa se caiga.

public class Registroinstituto {

    // lector
    private final java.util.Scanner sc = new java.util.Scanner(System.in); //clase que permite leer texto y convertirlo a tipos (String, int, double, etc.).
    //new Scanner(System.in): crea el lector conectado a la entrada estándar (el teclado/console).
    
    //definimos las variables que trabajaran con los datos de las clases
    private Estudiante estudiante_var;
    private Docente docente_var;
    private Sede sede_var;
    private Asignatura asignatura_var;

    private final DateTimeFormatter DATE_FMT = DateTimeFormatter.ofPattern("yyyy-MM-dd");
    //define un formateador de fechas que toda tu clase usa para parsear (leer) y formatear (mostrar) fechas siempre con el mismo formato yyyy-MM-dd.
    
    
    public static void main(String[] args) {
        Registroinstituto menuPrincipal = new Registroinstituto();
        menuPrincipal.ejecutar();
    }

    // menu principal: termina cuando op == 0
    private void ejecutar() {
        int op;
        do {
            System.out.println();
            System.out.println("=== Sistema de Registro de Asignaturas ===");
            System.out.println("1. Registrar Sede");
            System.out.println("2. Registrar Estudiante");
            System.out.println("3. Registrar Docente");
            System.out.println("4. Registrar Asignatura (asociar estudiante y docente)");
            System.out.println("5. Ingresar/Actualizar Notas (N1, N2, N3)");
            System.out.println("6. Calcular Nota de Presentacion");
            System.out.println("7. Registrar Examen y Calcular Nota Final");
            System.out.println("8. Ver Asignatura con detalle");
            System.out.println("0. Salir");
            System.out.println("Seleccione opcion:");
            op = leerEnteroLibre();

            if (op == 1) registrarSede();
            else if (op == 2) registrarEstudiante();
            else if (op == 3) registrarDocente();
            else if (op == 4) registrarAsignatura();
            else if (op == 5) ingresarNotas();
            else if (op == 6) calcularPresentacion();
            else if (op == 7) registrarExamenYCalcular();
            else if (op == 8) verAsignatura();
            else if (op != 0) System.out.println("Opcion invalida.");
        } while (op != 0);

        System.out.println("Hasta luego.");
    }

    // ==============================
    //         Acciones
    // ==============================

    private void registrarSede() {
        System.out.println("--- Registrar Sede ---");
        int numero = leerEntero("Numero de sede (entero >=1):", 1, Integer.MAX_VALUE);
        String nombre = leerNoVacio("Nombre de sede:");
        String comuna = leerNoVacio("Comuna:");
        sede_var = new Sede(numero, nombre, comuna);
        System.out.println("OK: " + sede_var);
    }

    private void registrarEstudiante() {
        System.out.println("--- Registrar Estudiante ---");
        String rut = leerNoVacio("RUT:");
        String nombre = leerNoVacio("Nombre:");
        int edad = leerEntero("Edad (>=18 y <100):", 18, 99);
        LocalDate fn = leerFecha("Fecha de nacimiento (yyyy-MM-dd):");
        estudiante_var = new Estudiante(rut, nombre, edad, fn);
        System.out.println("OK: " + estudiante_var);
    }

    private void registrarDocente() {
        System.out.println("--- Registrar Docente ---");
        if (sede_var == null) {
            System.out.println("Primero debe registrar una sede.");
            return;
        }
        String rut = leerNoVacio("RUT:");
        String nroDoc = leerNoVacio("Numero de docente:");
        String nombre = leerNoVacio("Nombre:");
        LocalDate fi = leerFechaNoFutura("Fecha de ingreso (yyyy-MM-dd, no posterior a hoy):");
        docente_var = new Docente(rut, nroDoc, nombre, fi, sede_var);
        System.out.println("OK: " + docente_var);
    }

    private void registrarAsignatura() {
        System.out.println("--- Registrar Asignatura ---");
        if (estudiante_var == null || docente_var == null) {
            System.out.println("Debe existir al menos un estudiante y un docente registrados.");
            return;
        }
        String codigo = leerNoVacio("Codigo de la asignatura:");
        String nombre = leerNoVacio("Nombre de la asignatura:");
        asignatura_var = new Asignatura(codigo, nombre, estudiante_var, docente_var);
        System.out.println("OK: Asignatura registrada.");
    }

    private void ingresarNotas() {
        System.out.println("--- Ingresar/Actualizar Notas ---");
        if (asignatura_var == null) {
            System.out.println("No hay asignatura registrada.");
            return;
        }
        double n1 = leerNota("Nota 1 (1.0 - 7.0):");
        double n2 = leerNota("Nota 2 (1.0 - 7.0):");
        double n3 = leerNota("Nota 3 (1.0 - 7.0):");

        asignatura_var.setNota1(n1);
        asignatura_var.setNota2(n2);
        asignatura_var.setNota3(n3);

        // limpiar calculos previos
        asignatura_var.setNotaPresentacion(null);
        asignatura_var.setExamen(null);
        asignatura_var.setNotaFinal(null);
        asignatura_var.setEstado(null);

        System.out.println("OK: Notas actualizadas.");
    }

    private void calcularPresentacion() {
        System.out.println("--- Calcular Nota de Presentacion ---");
        if (asignatura_var == null) {
            System.out.println("No hay asignatura registrada.");
            return;
        }
        if (asignatura_var.getNota1() == null || asignatura_var.getNota2() == null || asignatura_var.getNota3() == null) {
            System.out.println("Primero debe ingresar N1, N2 y N3 (opcion 5).");
            return;
        }

        double p = 0.3 * asignatura_var.getNota1() + 0.3 * asignatura_var.getNota2() + 0.4 * asignatura_var.getNota3();
        asignatura_var.setNotaPresentacion(p);

        if (p >= 5.0) {
            asignatura_var.setEstado("Eximido");
            asignatura_var.setNotaFinal(p);
        }

        System.out.println(String.format("Presentacion: %.2f", p));
        if ("Eximido".equals(asignatura_var.getEstado())) {
            System.out.println("Estado: Eximido (nota final = presentacion)");
        }
    }

    private void registrarExamenYCalcular() {
        System.out.println("--- Registrar Examen y Calcular Nota Final ---");
        if (asignatura_var == null) {
            System.out.println("No hay asignatura registrada.");
            return;
        }
        if (asignatura_var.getNotaPresentacion() == null) {
            System.out.println("Primero calcule la nota de presentacion (opcion 6).");
            return;
        }
        if ("Eximido".equals(asignatura_var.getEstado())) {
            System.out.println(String.format("El estudiante esta EXIMIDO. Nota Final: %.2f", asignatura_var.getNotaFinal()));
            return;
        }

        double ex = leerNota("Nota de Examen (1.0 - 7.0):");
        asignatura_var.setExamen(ex);

        double nf = 0.6 * asignatura_var.getNotaPresentacion() + 0.4 * ex;
        asignatura_var.setNotaFinal(nf);
        asignatura_var.setEstado(nf >= 4.0 ? "Aprobado" : "Reprobado");

        System.out.println(String.format("Nota Final: %.2f | Estado: %s", nf, asignatura_var.getEstado()));
    }

    private void verAsignatura() {
        System.out.println("--- Asignatura (detalle) ---");
        if (asignatura_var == null) {
            System.out.println("No hay asignatura registrada.");
            return;
        }

        // armamos una sola linea de salida usando StringBuilder y println
        StringBuilder sb = new StringBuilder();
        sb.append(asignatura_var.toString());
        sb.append(" — Estudiante: ");
        if (asignatura_var.getEstudiante() != null && asignatura_var.getEstudiante().getNombre() != null) {
            sb.append(asignatura_var.getEstudiante().getNombre());
        } else {
            sb.append("sin estudiante");
        }
        sb.append(", Docente: ");
        if (asignatura_var.getDocente() != null && asignatura_var.getDocente().getNombre() != null) {
            sb.append(asignatura_var.getDocente().getNombre());
        } else {
            sb.append("sin docente");
        }
        if (asignatura_var.getNota1() != null) sb.append(" | N1: ").append(String.format("%.2f", asignatura_var.getNota1()));
        if (asignatura_var.getNota2() != null) sb.append(" | N2: ").append(String.format("%.2f", asignatura_var.getNota2()));
        if (asignatura_var.getNota3() != null) sb.append(" | N3: ").append(String.format("%.2f", asignatura_var.getNota3()));
        if (asignatura_var.getNotaPresentacion() != null) sb.append(" | Presentacion: ").append(String.format("%.2f", asignatura_var.getNotaPresentacion()));
        if (asignatura_var.getExamen() != null) sb.append(" | Examen: ").append(String.format("%.2f", asignatura_var.getExamen()));
        if (asignatura_var.getNotaFinal() != null) sb.append(" | Final: ").append(String.format("%.2f", asignatura_var.getNotaFinal()));
        if (asignatura_var.getEstado() != null) sb.append(" | Estado: ").append(asignatura_var.getEstado());

        System.out.println(sb.toString());
    }

        // ==============================
    //      Lectura validada (I/O)
    // ==============================

    private String leerNoVacio(String prompt) {
        while (true) {
            System.out.println(prompt);
            String s = sc.nextLine();
            if (s != null) s = s.trim();
            if (s != null && !s.isEmpty()) return s;
            System.out.println("El valor no puede estar vacio.");
        }
    }

    private int leerEntero(String prompt, int minIncl, int maxIncl) {
        while (true) {
            System.out.println(prompt);
            String s = sc.nextLine();
            if (s != null) s = s.trim();
            try {
                int v = Integer.parseInt(s);
                if (v < minIncl || v > maxIncl) {
                    System.out.println("Fuera de rango (" + minIncl + " - " + maxIncl + ").");
                } else {
                    return v;
                }
            } catch (NumberFormatException e) {
                System.out.println("Ingrese un numero entero valido.");
            }
        }
    }

    private int leerEnteroLibre() {
        while (true) {
            String s = sc.nextLine();
            if (s != null) s = s.trim();
            try {
                return Integer.parseInt(s);
            } catch (NumberFormatException e) {
                System.out.println("Ingrese un numero entero valido:");
            }
        }
    }

    private LocalDate leerFecha(String prompt) {
        while (true) {
            System.out.println(prompt);
            String s = sc.nextLine();
            if (s != null) s = s.trim();
            try {
                return LocalDate.parse(s, DATE_FMT);
            } catch (DateTimeParseException e) {
                System.out.println("Formato invalido. Use yyyy-MM-dd.");
            }
        }
    }

    private LocalDate leerFechaNoFutura(String prompt) {
        while (true) {
            LocalDate d = leerFecha(prompt);
            if (!d.isAfter(LocalDate.now())) return d;
            System.out.println("La fecha no puede ser posterior a hoy.");
        }
    }

    private double leerNota(String prompt) {
        while (true) {
            System.out.println(prompt);
            String s = sc.nextLine();
            if (s != null) s = s.trim().replace(',', '.');
            try {
                double n = Double.parseDouble(s);
                if (n < 1.0 || n > 7.0) {
                    System.out.println("La nota debe estar entre 1.0 y 7.0.");
                } else {
                    return n;
                }
            } catch (NumberFormatException e) {
                System.out.println("Ingrese un numero valido (ej: 4.5).");
            }
        }
    }
}