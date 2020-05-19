# Implementación de datos de tipo fecha.
import datetime

# Declaracion de una clase.
# Nombre utiliza Pascal Casing.
class Pais:
  # Constructor. Metodo que se encarga de generar un objeto
  # parametrizado. Esta clase tiene 5 propiedades, mismas que 
  # están descritas entre parentesis (argumentos). self no es
  # una propiedad, porque es la referencia que hace el objeto 
  # a si mismo.
  def _init_(self,NombreIng,NombreEsp,Fallecidos,
           Contagiados, PDC):
       # NombreIng: Nombre del país, en inglés (str)
       # NombreEsp: Nombre del país, en español (str)
       # Fallecidos: Total de fallecidos registrados en el pais (int)
       # PDC: Primer dia de contagio (datetime)
       self.NombreIng = NombreIng
       self.NombreEsp = NombreEsp
       self.Fallecidos = Fallecidos
       self.PDC = PDC

class Incidente:
  def _init_(self,Pais,Fecha,NContagios,NFallecidos):
       # Fecha: Fecha de los datos (datetima)
       # Pais: Nombre del pais que reporta los datos (str)
       # NContagios: Nuevos contagios presentados en Pais y Fecha (int)
       # NFallecidos: Nuevos fallecimientos presentados en Pais y Fecha (int)
       self.Fecha = Fecha
       self.Pais = Pais
       self.NContagios = NContagios
       self.NFallecidos = NFallecidos

# Probar el funcionamiento de nuestras clases.

# Instanciar la clase Pais (creamos un objeto de tipo Pais).
miPais = Pais(str("Mexico"),str("Mexico"),int(1000),int(5000),datetime.datetime(2020, 5, 18))
print(miPais.PDC)

# Instanciar la clase Incidente. Generación de 2 objetos.
incidenteAyer = Incidente(datetime.datetime(2020, 5, 17),str("Mexico"),int(1500), int(18))
incidenteHoy = Incidente(datetime.datetime.now(), str("Mexico"), int(1400), int(12))
print(incidenteAyer.Pais)
