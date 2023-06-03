
package lab6;

public class Docente implements Persona {
    int id;
    String nombre, curp, domicilio;

    public Docente(int id, String nombre, String curp, String domicilio) {
        this.id = id;
        this.nombre = nombre;
        this.curp = curp;
        this.domicilio = domicilio;
    }
    
    @Override
    public int obtenerId() {
        return id;
    }

    @Override
    public String obtenerNombre() {
        return nombre;
    }

    @Override
    public String obtenerCURP() {
        return curp;
    }

    @Override
    public String obtenerDomicilio() {
        return domicilio;
    }
}
