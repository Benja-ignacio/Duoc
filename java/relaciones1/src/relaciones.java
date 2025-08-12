package relaciones1.src;

public class relaciones {
    // 1:1 (uno a uno)
    class Persona {
        Pasaporte pasaporte; // Una persona tiene un pasaporte 
    }

    class Pasaporte {
        Persona persona; // Un pasaporte pertenece a una persona
    }

    // 1:N (uno a muchos)
    
    class CLiente {
        List<Pedido> pedidos; // Un cliente tiene muchos pedidos
    }

    class Pedido {
        CLiente cliente; // Un pedido pertenece a un cliente
    }

    //N:M (muchos a muchos)

    class Estudiante {
        List<Curso> cursos; // Un estudiante puede estar en muchos cursos
    }

    class Curso {
        List<Estudiante> estudiantes; // un curso puede tener muchos estudiantes
    }

    

}
