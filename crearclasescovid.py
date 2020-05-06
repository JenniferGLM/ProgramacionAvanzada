#class <<NombreDeClase(argumento u objeto):
class Paises():
      #def _init_
    def __init__(self,NombreIng,NombreEsp,Fallecidos,
                PDC,Contagiados):
        self.NombreIng = NombreIng
        self.NombreEsp = NombreEsp
        self.Fallecidos = Fallecidos
        self.PDC = PDC
        self.Contangiados = Contagiados

class  Incidentes():
      def __init__(self,Pais,Fecha,NContangios,NFallecidos):
            self.Fecha = Fecha
            self.Pais = Pais
            self.NContangios = NContangios
            self.NFallecidos = NFallecidos
