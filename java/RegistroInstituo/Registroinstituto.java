package registroinstituto;

import java.time.LocalDate; //Qué es: una fecha sin hora ni zona (solo AAAA-MM-DD) Se usa en Campos y variables
import java.time.format.DateTimeFormatter; //Qué es: define el formato de texto para parsear/mostrar fechas.
// NOTA: En esta versión simple NO usamos DateTimeParseException (quitar el import evita error de import no usado).

public class Registroinstituto {

    // lector
    private final java.util.Scanner sc = new java.util.Scanner(System.in); //clase que permite leer texto y convertirlo a tipos (String, int, double, etc.).
    //new Scanner(System.in): crea el lector conectado a la entrada estándar (el teclado/console).
    
    //definimos las variables que trabajaran con los datos de las clases
    private Estudiante estudiante_var;
    private Docente docente_var;
    private Sede sede_var;
    private Asignatura asignatura_var;

    private final DateTimeFormatter DATE_FMT = DateTimeFormatter.ofPattern("dd-MM-yyyy");
    //define un formateador de fechas que toda tu clase usa para parsear (leer) y formatear (mostrar) fechas siempre con el mismo formato MM-dd-yyyy.
    
    
    public static void main(String[] args) {
        Registroinstituto menuPrincipal = new Registroinstituto();
        menuPrincipal.ejecutar();
    }

    // menu principal: termina cuando op == 0
    private void ejecutar() {
        int opcionMenu;
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
            opcionMenu = leerEnteroLibre(); // lectura básica (asume que el usuario digita un entero)

            if (opcionMenu == 1) registrarSede();
            else if (opcionMenu == 2) registrarEstudiante();
            else if (opcionMenu == 3) registrarDocente();
            else if (opcionMenu == 4) registrarAsignatura();
            else if (opcionMenu == 5) ingresarNotas();
            else if (opcionMenu == 6) calcularPresentacion();
            else if (opcionMenu == 7) registrarExamenYCalcular();
            else if (opcionMenu == 8) verAsignatura();
            else if (opcionMenu != 0) System.out.println("Opcion invalida.");
        } while (opcionMenu != 0);

        System.out.println("Hasta luego.");
    }

    // ==============================
    //         Acciones
    // ==============================

    private void registrarSede() {
        System.out.println("--- Registrar Sede ---");
        System.out.println("Numero de sede (entero):");
        int numeroSedeIngresado = leerEnteroLibre(); // simple: nextInt()
        String nombreSedeIngresado = leerNoVacio("Nombre de sede:"); // no vacío
        String comunaIngresada = leerNoVacio("Comuna:");             // no vacío
        sede_var = new Sede(numeroSedeIngresado, nombreSedeIngresado, comunaIngresada);
        System.out.println("OK: " + sede_var);
    }

    private void registrarEstudiante() {
        System.out.println("--- Registrar Estudiante ---");
        String rutIngresado = leerNoVacio("RUT:");              // no vacío
        String nombreIngresado = leerNoVacio("Nombre:");        // no vacío
        int edadIngresada = leerEnteroEnRango("Edad (>=18 y <100):", 18, 99); // rango básico con do-while
        LocalDate fechaNacimientoIngresada = leerFecha("Fecha de nacimiento (dd-MM-yyyy):");
        estudiante_var = new Estudiante(rutIngresado, nombreIngresado, edadIngresada, fechaNacimientoIngresada);
        System.out.println("OK: " + estudiante_var);
    }

    private void registrarDocente() {
        System.out.println("--- Registrar Docente ---");
        String rutIngresado = leerNoVacio("RUT:");                  // no vacío
        String numeroDocenteIngresado = leerNoVacio("Numero de docente:"); // no vacío
        String nombreIngresado = leerNoVacio("Nombre:");            // no vacío
        LocalDate fechaIngresoIngresada = leerFechaNoFutura("Fecha de ingreso (dd-MM-yyyy, no posterior a hoy):");
        // sede_var puede ser null (codigo simple). Si no hay sede, se asocia null.
        docente_var = new Docente(rutIngresado, numeroDocenteIngresado, nombreIngresado, fechaIngresoIngresada, sede_var);
        System.out.println("OK: " + docente_var);
    }

    private void registrarAsignatura() {
        System.out.println("--- Registrar Asignatura ---");
        String codigoAsignaturaIngresado = leerNoVacio("Codigo de la asignatura:");
        String nombreAsignaturaIngresado = leerNoVacio("Nombre de la asignatura:");
        asignatura_var = new Asignatura(codigoAsignaturaIngresado, nombreAsignaturaIngresado, estudiante_var, docente_var);
        System.out.println("OK: Asignatura registrada.");
    }

    private void ingresarNotas() {
        System.out.println("--- Ingresar/Actualizar Notas ---");
        if (asignatura_var == null) {
            System.out.println("No hay asignatura registrada.");
            return;
        }
        double nota1Ingresada = leerNota("Nota 1 (1.0 - 7.0):"); // sin validación de rango
        double nota2Ingresada = leerNota("Nota 2 (1.0 - 7.0):");
        double nota3Ingresada = leerNota("Nota 3 (1.0 - 7.0):");

        asignatura_var.setNota1(nota1Ingresada);
        asignatura_var.setNota2(nota2Ingresada);
        asignatura_var.setNota3(nota3Ingresada);

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
            System.out.println("Faltan notas. Ingrese N1, N2 y N3 (opcion 5).");
            return;
        }

        double presentacionCalculada = 0.3 * asignatura_var.getNota1() + 0.3 * asignatura_var.getNota2() + 0.4 * asignatura_var.getNota3();
        asignatura_var.setNotaPresentacion(presentacionCalculada);

        if (presentacionCalculada >= 5.0) {
            asignatura_var.setEstado("Eximido");
            asignatura_var.setNotaFinal(presentacionCalculada);
        }

        System.out.println("Presentacion: " + presentacionCalculada);
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
            System.out.println("El estudiante esta EXIMIDO. Nota Final: " + asignatura_var.getNotaFinal());
            return;
        }

        double examenIngresado = leerNota("Nota de Examen (1.0 - 7.0):"); // sin validación de rango
        asignatura_var.setExamen(examenIngresado);

        double notaFinalCalculada = 0.6 * asignatura_var.getNotaPresentacion() + 0.4 * examenIngresado;
        asignatura_var.setNotaFinal(notaFinalCalculada);
        if (notaFinalCalculada >= 4.0) {
            asignatura_var.setEstado("Aprobado");
        } else {
            asignatura_var.setEstado("Reprobado");
        }

        System.out.println("Nota Final: " + notaFinalCalculada + " | Estado: " + asignatura_var.getEstado());
    }

    private void verAsignatura() {
        System.out.println("--- Asignatura (detalle) ---");
        if (asignatura_var == null) {
            System.out.println("No hay asignatura registrada.");
            return;
        }

        System.out.println(asignatura_var.toString());
        if (asignatura_var.getEstudiante() != null && asignatura_var.getEstudiante().getNombre() != null) {
            System.out.println("Estudiante: " + asignatura_var.getEstudiante().getNombre());
        } else {
            System.out.println("Estudiante: sin estudiante");
        }
        if (asignatura_var.getDocente() != null && asignatura_var.getDocente().getNombre() != null) {
            System.out.println("Docente: " + asignatura_var.getDocente().getNombre());
        } else {
            System.out.println("Docente: sin docente");
        }
        if (asignatura_var.getNota1() != null) System.out.println("N1: " + asignatura_var.getNota1());
        if (asignatura_var.getNota2() != null) System.out.println("N2: " + asignatura_var.getNota2());
        if (asignatura_var.getNota3() != null) System.out.println("N3: " + asignatura_var.getNota3());
        if (asignatura_var.getNotaPresentacion() != null) System.out.println("Presentacion: " + asignatura_var.getNotaPresentacion());
        if (asignatura_var.getExamen() != null) System.out.println("Examen: " + asignatura_var.getExamen());
        if (asignatura_var.getNotaFinal() != null) System.out.println("Final: " + asignatura_var.getNotaFinal());
        if (asignatura_var.getEstado() != null) System.out.println("Estado: " + asignatura_var.getEstado());
    }

    // ==============================
    //      Lectura validada (I/O)
    // ==============================

    // No-vacío con do-while (básico)
    private String leerNoVacio(String prompt) {
    String textoIngresado;                // 1) Declaras una variable para guardar lo que escriba el usuario
    do {                                  // 2) do-while: el bloque se ejecuta AL MENOS una vez
        System.out.println(prompt);       // 3) Muestras el mensaje (ej: "Nombre:")
        textoIngresado = sc.nextLine();   // 4) Lees la línea completa que escribió el usuario
        if (textoIngresado != null)       // 5) Si no es null (normalmente no lo será),
            textoIngresado = textoIngresado.trim(); //    le quitas espacios al inicio y al final
    } while (textoIngresado == null || textoIngresado.isEmpty()); // 6) Repite si es null o está vacía ("")
    return textoIngresado;                // 7) Si NO está vacía, la devuelves
    }

    // Entero con rango usando do-while (para edad)
    private int leerEnteroEnRango(String prompt, int minIncl, int maxIncl) {
    int numeroIngresado;                   // 1) variable para guardar el número que escriba el usuario
    do {                                   // 2) do-while: se ejecuta al menos una vez
        System.out.println(prompt);        // 3) mostramos el mensaje (ej: "Edad (>=18 y <100):")
        numeroIngresado = sc.nextInt();    // 4) leemos el número entero que ingresa el usuario
        sc.nextLine();                     // 5) limpiamos el salto de línea que queda pendiente
    } while (numeroIngresado < minIncl     // 6) repetimos mientras esté fuera del rango: menor que mínimo
          || numeroIngresado > maxIncl);   //    o mayor que máximo
    return numeroIngresado;                // 7) si está dentro del rango, lo devolvemos
    }

    // Entero libre (sin validaciones) 
    private int leerEnteroLibre() {
    System.out.println("Ingrese un numero entero:"); // 1) pedimos el número
    int numero = sc.nextInt();                       // 2) leemos el entero (si no es entero, el programa se cae)
    sc.nextLine();                                   // 3) limpiamos el salto de línea pendiente
    return numero;                                   // 4) devolvemos el número leído
    }

    // Validación Fecha (asume formato correcto "yyyy-MM-dd"; si no, se cae)
    private LocalDate leerFecha(String prompt) {
    System.out.println(prompt);                   // 1) mostramos el mensaje (ej: "Fecha (dd-MM-yyyy):")
    String textoFecha = sc.nextLine();            // 2) leemos la línea completa como texto
    if (textoFecha != null) textoFecha = textoFecha.trim(); // 3) quitamos espacios al inicio y final
        return LocalDate.parse(textoFecha, DATE_FMT); // 4) convertimos el texto a LocalDate usando el formato fijo
        // (si el usuario escribe algo que no calza con "dd-MM-yyyy", el programa se cae)
    }

    // Fecha no futura (repite con do-while hasta que no sea posterior a hoy)
    private LocalDate leerFechaNoFutura(String prompt) {
    LocalDate fechaIngresada;                                  // 1) variable para guardar la fecha escrita
    do {                                                       // 2) do-while: se ejecuta al menos una vez
        fechaIngresada = leerFecha(prompt);                    // 3) pedimos la fecha con el método anterior
        if (fechaIngresada.isAfter(LocalDate.now())) {         // 4) si la fecha es posterior a hoy
            System.out.println("La fecha no puede ser posterior a hoy."); // 5) avisamos y repetimos
        }
    } while (fechaIngresada.isAfter(LocalDate.now()));         // 6) repetir mientras sea futura
    return fechaIngresada;                                     // 7) devolver la fecha válida (hoy o antes)
    }

    // Valida Nota (sin validación de rango)
    private double leerNota(String prompt) {
    System.out.println(prompt);              // 1) mostramos el mensaje (ej: "Nota 1 (1.0 - 7.0):")
    double nota = sc.nextDouble();           // 2) leemos el número decimal (si no es número, el programa se cae)
    sc.nextLine();                           // 3) limpiamos el salto de línea pendiente
    return nota;                              // 4) devolvemos la nota leída (sin controlar el rango aquí)
    }

}
