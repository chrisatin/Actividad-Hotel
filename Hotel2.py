#Corregí asignación de habitación mediante la creación de un objeto
#agregando parametros de entrada 
class NodoHuesped:
    def __init__(self, nombre, cedula, habitacion):
        self.nombre = nombre
        self.cedula = cedula
        self.habitacion = habitacion
        self.siguiente = None

class ListaHuespedes:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, nombre, cedula, habitacion):
        nuevo_nodo = NodoHuesped(nombre, cedula, habitacion)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir(self):
        nodo_recorre = self.cabeza
        while nodo_recorre:
            huesped = nodo_recorre
            print(f"Nombre: {huesped.nombre}, Cédula: {huesped.cedula}, Habitación: {huesped.habitacion}")
            nodo_recorre = nodo_recorre.siguiente

    def buscar_por_cedula(self, cedula):
        nodo_recorre = self.cabeza
        while nodo_recorre:
            huesped = nodo_recorre
            if huesped.cedula == cedula:
                return huesped
            nodo_recorre = nodo_recorre.siguiente
        return None

class NodoHabitacion:
    def __init__(self, numero, ocupada=False):
        self.numero = numero
        self.ocupada = ocupada
        self.siguiente = None

class ListaHabitaciones:
    def __init__(self, num_habitaciones):
        self.cabeza = None
        self.num_habitaciones = num_habitaciones

        
        for i in range(num_habitaciones):
            self.insertar_inicio(i + 1, False)

    def insertar_inicio(self, numero, ocupada=False):
        nuevo_nodo = NodoHabitacion(numero, ocupada)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def habitaciones_disponibles(self):
        habitaciones = []
        nodo_recorre = self.cabeza
        while nodo_recorre:
            habitacion = nodo_recorre
            if not habitacion.ocupada:
                habitaciones.append(habitacion.numero)
            nodo_recorre = nodo_recorre.siguiente
        return habitaciones

def asignar_habitacion(huespedes, habitaciones, nombre, cedula):
    numero_habitacion = habitaciones.habitaciones_disponibles()
    if numero_habitacion:
        habitaciones.cabeza.ocupada = True
        huespedes.insertar_inicio(nombre, cedula, numero_habitacion[0])
        return True
    return False

def liberar_habitacion(huespedes, habitaciones, cedula):
    huesped_anterior = None
    nodo_recorre = huespedes.cabeza
    while nodo_recorre:
        huesped = nodo_recorre
        if huesped.cedula == cedula:
            habitacion = habitaciones.cabeza
            while habitacion:
                if habitacion.numero == huesped.habitacion:
                    habitacion.ocupada = False
                    break
                habitacion = habitacion.siguiente
            if huesped_anterior:
                huesped_anterior.siguiente = nodo_recorre.siguiente
            else:
                huespedes.cabeza = nodo_recorre.siguiente
            return True
        huesped_anterior = nodo_recorre
        nodo_recorre = nodo_recorre.siguiente
    return False

def consultar_huesped_individual(huespedes, cedula):
    return huespedes.buscar_por_cedula(cedula)

def consultar_huespedes_total(huespedes, por_cedula=True):
    if por_cedula:
        huespedes.imprimir()

def consultar_habitaciones_disponibles(habitaciones):
    return habitaciones.habitaciones_disponibles()


lista_huespedes = ListaHuespedes()
lista_habitaciones = ListaHabitaciones(8) 

# Ejemplos de uso
asignar_habitacion(lista_huespedes, lista_habitaciones, "Pedro", "598")
asignar_habitacion(lista_huespedes, lista_habitaciones, "Jose", "748")
liberar_habitacion(lista_huespedes, lista_habitaciones, "748")

print("Habitaciones disponibles:")
print(consultar_habitaciones_disponibles(lista_habitaciones))

print("La cedula corresponde al huesped:")
print(consultar_huesped_individual(lista_huespedes, "598").nombre)

print("Huéspedes:")
consultar_huespedes_total(lista_huespedes)
