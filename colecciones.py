# Implementación de datos de tipo fecha.
import datetime

# Declaracion de una clase.

class Incidente:
  def _init_(self,Fecha,Pais,NContagios,NFallecidos):
       # Fecha: Fecha de los datos (datetima)
       # Pais: Nombre del pais que reporta los datos (str)
       # NContagios: Nuevos contagios presentados en Pais y Fecha (int)
       # NFallecidos: Nuevos fallecimientos presentados en Pais y Fecha (int)
       self.Fecha = Fecha
       self.Pais = Pais
       self.NContagios = NContagios
       self.NFallecidos = NFallecidos


# Instanciar la clase Incidente. Generación de 2 objetos.
incidenteAyer = Incidente(datetime.datetime(2020, 5, 17),str("Mexico"),int(1500), int(18))
incidenteHoy = Incidente(datetime.datetime.now(), str("Mexico"), int(1400), int(12))

# Creación de una lista. Se usa snake_notation. La lista está vacía.
mi_lista = []

# Podemos agregas elementos con append.
mi_lista.append(incidenteAyer)
mi_lista.append(incidenteHoy)

# Mostrar el número de elementos de la lista.
print(len(mi_lista))

# Barrido secuencial de la lista.
for elemento in mi_lista:
    print(elemento.Fecha)