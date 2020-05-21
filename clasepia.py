
import datetime


class Contacto:

  def __init__(self, telefono, nombre,correo,registro=datetime.datetime.now(),UIValido=False):
    self.telefono=telefono
    self.nombre=nombre
    self.correo=correo
    self.registro=registro
    self.UIValido=UIValido