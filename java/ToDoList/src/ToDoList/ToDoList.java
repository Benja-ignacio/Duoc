package ToDoList;
import java.util.ArrayList;
import java.util.Scanner;

public class ToDoList {
    
    static Scanner input = new Scanner(System.in);
    ArrayList<Tareas> listaTareas = new ArrayList<>();
    public static void main(String[] args) {

        ToDoList app = new ToDoList();
        app.run();
    }

    private void run() {
        Tareas t1 = new Tareas("abc123", "Estudiar", "Pendiente");
        listaTareas.add(t1);

        
        while (true) {
            System.out.println("1. Agregar tarea\n2. Mostrar todas\n3. Filtrar por estado\n4. Marcar tarea como completada\n5. Eliminar tarea\n0. Salir:");

            int opcion = input.nextInt();
            input.nextLine(); // limpiar buffer

            switch (opcion) {
                case 1:
                    agregarTarea(listaTareas);
                    break;
                case 2:
                    mostrarTareas(listaTareas);
                    break;
                case 3:
                filtrarPorEstado(listaTareas);
                    break;
                case 4:
                marcarTareaCompletada(listaTareas);
                    break;
                case 5: 
                eliminarTarea(listaTareas);
                    break;
                case 0:
                    return;
                default:
                    System.out.println("Opcion invalida.");;
            }

        }
    }

    private String validarString(String prompt) {
        String texto;

        do {
            System.out.println(prompt);
            texto = input.nextLine().trim();
        } while (texto.isEmpty());
        return texto;
    }

    private void agregarTarea(ArrayList<Tareas> tareas) {
        String codigo = validarString("Codigo:");
        String descripcion = validarString("Descripcion:");
        String estado = validarString("Estado:");

        Tareas nuevaTarea = new Tareas(codigo, descripcion, estado);
        listaTareas.add(nuevaTarea);
        System.out.println("Tarea agregada correctamente!");
    }

    private void mostrarTareas(ArrayList<Tareas> tareas) {
        for (Tareas i: tareas) {
            System.out.println("Codigo: " + i.getCodigo() + " Descripcion: " + i.getDescripcion() + " Estado: " + i.getEstado() + "\n");
        }
    }

    private void filtrarPorEstado(ArrayList<Tareas> tareas) {
        String estado = validarString("Estado: ");
        boolean encontrado = false;
        
        for (Tareas i: tareas) {
            if (i.getEstado().equals(estado)) {
            System.out.println("Codigo: " + i.getCodigo() + " Descripcion: " + i.getDescripcion() + " Estado: " + i.getEstado() + "\n");
            encontrado = true;
            }
        }
        if (!encontrado) {
            System.out.println(("No se encontraron tareas."));
        }
    }
    
    private void marcarTareaCompletada(ArrayList<Tareas> tareas) {
        String codigo = validarString("Codigo: ");
        boolean encontrado = false;
        for (Tareas i: tareas) {
            if (i.getCodigo().equals(codigo)) {
                i.setEstado("Completado");
                encontrado = true;
            }
        }
        if (!encontrado) {
            System.out.println("No se encontro ninguna tarea.");
        }
    }

    private void eliminarTarea(ArrayList<Tareas> tareas) {
        String codigo = validarString("Codigo:");
        boolean eliminado = listaTareas.removeIf(i -> i.getCodigo().equals(codigo));
        
        if (eliminado) {
            System.out.println("Tarea eliminada");
        } else {
            System.out.println("No se encontro ninguna tarea");
        }
    }
}


