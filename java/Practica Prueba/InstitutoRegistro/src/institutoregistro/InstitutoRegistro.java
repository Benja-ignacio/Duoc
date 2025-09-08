package institutoregistro;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;
import java.util.List;

public class InstitutoRegistro {
    private final java.util.Scanner sc = new java.util.Scanner(System.in);

    private final List<Estudiante> estudiantes = new ArrayList<>();
    private final List<Docente> docentes = new ArrayList<>();
    private final List<Sede> sedes = new ArrayList<>();
    private final List<Asignatura> asignaturas = new ArrayList<>();

    private final DateTimeFormatter DATE_FMT = DateTimeFormatter.ofPattern("yyyy-MM-dd");

    public static void main(String[] args) {
        InstitutoRegistro app = new InstitutoRegistro();
        app.run();
    }

    private void run() {
        while (true) {
            System.out.println();
            System.out.println("=== Sistema de Registro de Asignaturas ===");
            System.out.println("1. Registrar Sede");
            System.out.println("2. Registrar Estudiante");
            System.out.println("3. Registrar Docente");
            System.out.println("4. Registrar Asignatura (asociar estudiante y docente)");
            System.out.println("5. Ingresar/Actualizar Notas (N1, N2, N3)");
            System.out.println("6. Calcular Nota de Presentacion");
            System.out.println("7. Registrar Examen y Calcular Nota Final");
            System.out.println("8. Listar Asignaturas con detalle");
            System.out.println("9. Cargar datos de prueba (tabla de la pauta)");
            System.out.println("0. Salir");
            System.out.print("Seleccione opcion: ");
            int op = leerEnteroLibre();
            if (op == 0) { System.out.println("Hasta luego."); return; }

            if (op == 1) registrarSede();
            else if (op == 2) registrarEstudiante();
            else if (op == 3) registrarDocente();
            else if (op == 4) registrarAsignatura();
            else if (op == 5) ingresarNotas();
            else if (op == 6) calcularPresentacion();
            else if (op == 7) registrarExamenYCalcular();
            else if (op == 8) listarAsignaturas();
            else if (op == 9) cargarDatosDePrueba();
            else System.out.println("Opción inválida.");
        }
    }

    // ==============================
    //         Menú / Acciones
    // ==============================

    private void registrarSede() {
        System.out.println("--- Registrar Sede ---");
        int numero = leerEntero("Número de sede: ", 1, Integer.MAX_VALUE);
        String nombre = leerNoVacio("Nombre de sede: ");
        String comuna = leerNoVacio("Comuna: ");
        if (buscarSedePorNumero(numero) != null) {
            System.out.println("Ya existe una sede con ese número.");
            return;
        }
        Sede s = new Sede(numero, nombre, comuna);
        sedes.add(s);
        System.out.println("OK: " + s);
    }

    private void registrarEstudiante() {
        System.out.println("--- Registrar Estudiante ---");
        String rut = leerNoVacio("RUT: ");
        if (buscarEstudiantePorRut(rut) != null) {
            System.out.println("Ya existe un estudiante con ese RUT.");
            return;
        }
        String nombre = leerNoVacio("Nombre: ");
        int edad = leerEntero("Edad (>=18 y <100): ", 18, 99);
        LocalDate fn = leerFecha("Fecha de nacimiento (yyyy-MM-dd): ");
        Estudiante e = new Estudiante(rut, nombre, edad, fn);
        estudiantes.add(e);
        System.out.println("OK: " + e);
    }

    private void registrarDocente() {
        System.out.println("--- Registrar Docente ---");
        String rut = leerNoVacio("RUT: ");
        if (buscarDocentePorRut(rut) != null) {
            System.out.println("Ya existe un docente con ese RUT.");
            return;
        }
        String nroDoc = leerNoVacio("Nro docente: ");
        String nombre = leerNoVacio("Nombre: ");
        LocalDate fi = leerFechaNoFutura("Fecha de ingreso (yyyy-MM-dd, no posterior a hoy): ");
        if (sedes.isEmpty()) {
            System.out.println("Primero debe registrar una sede.");
            return;
        }
        int nroSede = leerEntero("Número de sede (existente): ", Integer.MIN_VALUE, Integer.MAX_VALUE);
        Sede sede = buscarSedePorNumero(nroSede);
        if (sede == null) {
            System.out.println("Sede no encontrada.");
            return;
        }
        Docente d = new Docente(rut, nroDoc, nombre, fi, sede);
        docentes.add(d);
        System.out.println("OK: " + d);
    }

    private void registrarAsignatura() {
        System.out.println("--- Registrar Asignatura ---");
        if (estudiantes.isEmpty() || docentes.isEmpty()) {
            System.out.println("Antes debe registrar al menos un estudiante y un docente.");
            return;
        }
        String codigo = leerNoVacio("Código de la asignatura: ");
        if (buscarAsignaturaPorCodigo(codigo) != null) {
            System.out.println("Ya existe una asignatura con ese código.");
            return;
        }
        String nombre = leerNoVacio("Nombre de la asignatura: ");
        String rutEst = leerNoVacio("RUT del estudiante: ");
        Estudiante est = buscarEstudiantePorRut(rutEst);
        if (est == null) { System.out.println("Estudiante no encontrado."); return; }
        String rutDoc = leerNoVacio("RUT del docente: ");
        Docente doc = buscarDocentePorRut(rutDoc);
        if (doc == null) { System.out.println("Docente no encontrado."); return; }

        Asignatura a = new Asignatura(codigo, nombre, est, doc);
        asignaturas.add(a);
        System.out.println("OK: Asignatura registrada.");
    }

    private void ingresarNotas() {
        System.out.println("--- Ingresar/Actualizar Notas ---");
        Asignatura a = seleccionarAsignatura();
        if (a == null) return;

        double n1 = leerNota("Nota 1 (1.0 - 7.0): ");
        double n2 = leerNota("Nota 2 (1.0 - 7.0): ");
        double n3 = leerNota("Nota 3 (1.0 - 7.0): ");

        a.setNota1(n1);
        a.setNota2(n2);
        a.setNota3(n3);

        // Limpiamos cálculos previos (se recalculan en otras opciones)
        a.setNotaPresentacion(null);
        a.setExamen(null);
        a.setNotaFinal(null);
        a.setEstado(null);

        System.out.println("OK: Notas actualizadas.");
    }

    private void calcularPresentacion() {
        System.out.println("--- Calcular Nota de Presentación ---");
        Asignatura a = seleccionarAsignatura();
        if (a == null) return;

        if (a.getNota1() == null || a.getNota2() == null || a.getNota3() == null) {
            System.out.println("Primero debe ingresar N1, N2 y N3 (opción 5).");
            return;
        }

        double p = 0.3 * a.getNota1() + 0.3 * a.getNota2() + 0.4 * a.getNota3();
        a.setNotaPresentacion(p);

        if (p >= 5.0) {
            a.setEstado("Eximido");
            a.setNotaFinal(p);
        }

        System.out.printf("Presentación: %.2f%n", p);
        if ("Eximido".equals(a.getEstado())) {
            System.out.println("Estado: Eximido (nota final = presentación)");
        }
    }

    private void registrarExamenYCalcular() {
        System.out.println("--- Registrar Examen y Calcular Nota Final ---");
        Asignatura a = seleccionarAsignatura();
        if (a == null) return;

        if (a.getNotaPresentacion() == null) {
            System.out.println("Primero calcule la nota de presentación (opción 6).");
            return;
        }
        if ("Eximido".equals(a.getEstado())) {
            System.out.printf("El estudiante está EXIMIDO. Nota Final: %.2f%n", a.getNotaFinal());
            return;
        }

        double ex = leerNota("Nota de Examen (1.0 - 7.0): ");
        a.setExamen(ex);

        double nf = 0.6 * a.getNotaPresentacion() + 0.4 * ex;
        a.setNotaFinal(nf);
        a.setEstado(nf >= 4.0 ? "Aprobado" : "Reprobado");

        System.out.printf("Nota Final: %.2f | Estado: %s%n", nf, a.getEstado());
    }

    private void listarAsignaturas() {
        System.out.println("--- Asignaturas ---");
        if (asignaturas.isEmpty()) {
            System.out.println("No hay asignaturas registradas.");
            return;
        }
        for (Asignatura a : asignaturas) {
            System.out.print(a.toString());

            // Estudiante
            System.out.print(" — Estudiante: ");
            if (a.getEstudiante() != null && a.getEstudiante().getNombre() != null) {
                System.out.print(a.getEstudiante().getNombre());
            } else {
                System.out.print("sin estudiante");
            }

            // Docente
            System.out.print(", Docente: ");
            if (a.getDocente() != null && a.getDocente().getNombre() != null) {
                System.out.print(a.getDocente().getNombre());
            } else {
                System.out.print("sin docente");
            }

            // Notas y estado (solo si existen)
            if (a.getNota1() != null) System.out.printf(" | N1: %.2f", a.getNota1());
            if (a.getNota2() != null) System.out.printf(" | N2: %.2f", a.getNota2());
            if (a.getNota3() != null) System.out.printf(" | N3: %.2f", a.getNota3());
            if (a.getNotaPresentacion() != null) System.out.printf(" | Presentación: %.2f", a.getNotaPresentacion());
            if (a.getExamen() != null) System.out.printf(" | Examen: %.2f", a.getExamen());
            if (a.getNotaFinal() != null) System.out.printf(" | Final: %.2f", a.getNotaFinal());
            if (a.getEstado() != null) System.out.print(" | Estado: " + a.getEstado());

            System.out.println();
        }
    }

    private void cargarDatosDePrueba() {
        System.out.println("--- Cargando datos de prueba ---");

        // Sede
        Sede s1 = buscarSedePorNumero(1);
        if (s1 == null) {
            s1 = new Sede(1, "San Joaquín", "San Joaquín");
            sedes.add(s1);
        }

        // Docentes
        Docente d1 = buscarDocentePorRut("15.111.111-1");
        if (d1 == null) {
            d1 = new Docente("15.111.111-1", "DOC-001", "Juan Soto",
                    LocalDate.now().minusYears(5), s1);
            docentes.add(d1);
        }
        Docente d2 = buscarDocentePorRut("16.222.222-2");
        if (d2 == null) {
            d2 = new Docente("16.222.222-2", "DOC-002", "Pedro Suazo",
                    LocalDate.now().minusYears(3), s1);
            docentes.add(d2);
        }

        // Estudiantes
        Estudiante e1 = buscarEstudiantePorRut("18.333.333-3");
        if (e1 == null) {
            e1 = new Estudiante("18.333.333-3", "Amalia Nunes", 20,
                    LocalDate.of(2005, 1, 15));
            estudiantes.add(e1);
        }
        Estudiante e2 = buscarEstudiantePorRut("19.444.444-4");
        if (e2 == null) {
            e2 = new Estudiante("19.444.444-4", "Francisco Fuentes", 22,
                    LocalDate.of(2003, 6, 10));
            estudiantes.add(e2);
        }

        // Asignaturas y notas (usando solo setters y cálculos aquí)
        Asignatura a1 = buscarAsignaturaPorCodigo("MAT0101");
        if (a1 == null) {
            a1 = new Asignatura("MAT0101", "Matemática Aplicada", e1, d1);
            a1.setNota1(4.5);
            a1.setNota2(3.8);
            a1.setNota3(4.5);
            double p1 = 0.3 * a1.getNota1() + 0.3 * a1.getNota2() + 0.4 * a1.getNota3(); // ≈ 4.29
            a1.setNotaPresentacion(p1);
            double ex1 = 3.3;
            a1.setExamen(ex1);
            double nf1 = 0.6 * a1.getNotaPresentacion() + 0.4 * ex1; // ≈ 3.89
            a1.setNotaFinal(nf1);
            a1.setEstado(nf1 >= 4.0 ? "Aprobado" : "Reprobado");
            asignaturas.add(a1);
        }

        Asignatura a2 = buscarAsignaturaPorCodigo("PBD2208");
        if (a2 == null) {
            a2 = new Asignatura("PBD2208", "Programación de BD", e2, d2);
            a2.setNota1(5.2);
            a2.setNota2(4.7);
            a2.setNota3(5.1);
            double p2 = 0.3 * a2.getNota1() + 0.3 * a2.getNota2() + 0.4 * a2.getNota3(); // ≈ 5.01
            a2.setNotaPresentacion(p2);
            if (p2 >= 5.0) {
                a2.setEstado("Eximido");
                a2.setNotaFinal(p2);
            }
            asignaturas.add(a2);
        }

        System.out.println("Datos de prueba cargados. Use opción 8 para ver detalle.");
    }

    // ==============================
    //        Búsquedas simples
    // ==============================

    private Estudiante seleccionarAsignaturaYRetornarEstudiante() { // (no usado, ejemplo)
        return null;
    }

    private Asignatura seleccionarAsignatura() {
        if (asignaturas.isEmpty()) {
            System.out.println("No hay asignaturas registradas.");
            return null;
        }
        String codigo = leerNoVacio("Código de la asignatura: ");
        Asignatura a = buscarAsignaturaPorCodigo(codigo);
        if (a == null) System.out.println("Asignatura no encontrada.");
        return a;
    }

    private Estudiante buscarEstudiantePorRut(String rut) {
        for (Estudiante e : estudiantes) {
            if (e.getRut() != null && e.getRut().equals(rut)) return e;
        }
        return null;
    }

    private Docente buscarDocentePorRut(String rut) {
        for (Docente d : docentes) {
            if (d.getRut() != null && d.getRut().equals(rut)) return d;
        }
        return null;
    }

    private Sede buscarSedePorNumero(int numero) {
        for (Sede s : sedes) {
            if (s.getNumero() == numero) return s;
        }
        return null;
    }

    private Asignatura buscarAsignaturaPorCodigo(String codigo) {
        for (Asignatura a : asignaturas) {
            if (a.getCodigo() != null && a.getCodigo().equals(codigo)) return a;
        }
        return null;
    }

    // ==============================
    //      Lectura validada (I/O)
    // ==============================

    private String leerNoVacio(String prompt) {
        while (true) {
            System.out.print(prompt);
            String s = sc.nextLine();
            if (s != null) s = s.trim();
            if (s != null && !s.isEmpty()) return s;
            System.out.println("El valor no puede estar vacío.");
        }
    }

    private int leerEntero(String prompt, int minIncl, int maxIncl) {
        while (true) {
            System.out.print(prompt);
            String s = sc.nextLine().trim();
            try {
                int v = Integer.parseInt(s);
                if (v < minIncl || v > maxIncl) {
                    System.out.println("Fuera de rango (" + minIncl + " - " + maxIncl + ").");
                } else {
                    return v;
                }
            } catch (NumberFormatException e) {
                System.out.println("Ingrese un número entero válido.");
            }
        }
    }

    private int leerEnteroLibre() {
        while (true) {
            String s = sc.nextLine().trim();
            try {
                return Integer.parseInt(s);
            } catch (NumberFormatException e) {
                System.out.print("Ingrese un número entero válido: ");
            }
        }
    }

    private LocalDate leerFecha(String prompt) {
        while (true) {
            System.out.print(prompt);
            String s = sc.nextLine().trim();
            try {
                return LocalDate.parse(s, DATE_FMT);
            } catch (DateTimeParseException e) {
                System.out.println("Formato inválido. Use yyyy-MM-dd.");
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
            System.out.print(prompt);
            String s = sc.nextLine().trim().replace(',', '.');
            try {
                double n = Double.parseDouble(s);
                if (n < 1.0 || n > 7.0) {
                    System.out.println("La nota debe estar entre 1.0 y 7.0.");
                } else {
                    return n;
                }
            } catch (NumberFormatException e) {
                System.out.println("Ingrese un número válido (ej: 4.5).");
            }
        }
    }
}
