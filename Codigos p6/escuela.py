from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def obtener_id(self):
        pass
    
    @abstractmethod
    def obtener_nombre(self):
        pass
    
    @abstractmethod
    def obtener_CURP(self):
        pass
    
    @abstractmethod
    def obtener_domicilio(self):
        pass

class Estudiante(Persona):
    def __init__(self, id, nombre, curp, domicilio):
        self.id = id
        self.nombre = nombre
        self.curp = curp
        self.domicilio = domicilio
    
    def obtener_id(self):
        return self.id
    
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_CURP(self):
        return self.curp
    
    def obtener_domicilio(self):
        return self.domicilio

class Docente(Persona):
    def __init__(self, id, nombre, curp, domicilio):
        self.id = id
        self.nombre = nombre
        self.curp = curp
        self.domicilio = domicilio
    
    def obtener_id(self):
        return self.id
    
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_CURP(self):
        return self.curp
    
    def obtener_domicilio(self):
        return self.domicilio

class PersonalApoyoAdministrativo(Persona):
    def __init__(self, id, nombre, curp, domicilio):
        self.id = id
        self.nombre = nombre
        self.curp = curp
        self.domicilio = domicilio
    
    def obtener_id(self):
        return self.id
    
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_CURP(self):
        return self.curp
    
    def obtener_domicilio(self):
        return self.domicilio

def menu():
    print("1. Estudiante")
    print("2. Docente")
    print("3. PAAE")
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        persona = Estudiante("123", "Juan", "ABCD123", "Calle 123")
    elif opcion == "2":
        persona = Docente("456", "María", "EFGH456", "Avenida 456")
    elif opcion == "3":
        persona = PersonalApoyoAdministrativo("789", "Pedro", "IJKL789", "Plaza 789")
    else:
        print("Opción inválida")
        return
    
    print("ID:", persona.obtener_id())
    print("Nombre:", persona.obtener_nombre())
    print("CURP:", persona.obtener_CURP())
    print("Domicilio:", persona.obtener_domicilio())

menu()
