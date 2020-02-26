# Pregunta y valida un dato, de acuerdo a un patrón regex

# Módulo requerido para la validación de expresiones regulares
importar  re
# Módulo para trabajar con datos de tipo datetime
 fecha y hora de importación

# Se declara una variable de paso, que solicite preguntar y validar información.
captura = ""

# Función que valida un dato, y si es correcto, lo coloca en captura, si no,
# se mantiene preguntando. Los argumentos que acepta una función, simplemente se
# enumeran entre los paréntesis.
def  askandcheck ( _patron , _pregunta = "Dame un dato:" ):
    # Se especifica que captura es global, para que el programa no asuma que es
    # local para esta función.
     captura global
    mientras  cierto :
        _fxvalor  =  input ( _pregunta )
        coincidir  =  re . buscar ( _patron , _fxvalor )
        si ( coincidir ):
            captura =  _fxvalor
            descanso
        más :
            print ( "El dato no es correcto. Intenta de nuevo." )

# Función que convierte una expresión AAAA-MM-DD a fecha y hora
fecha  estándar ( _dtoconv ):
     Fecha y hora de retorno . datetime ( int ( _dtoconv [ 0 : 4 ]), int ( _dtoconv [ 5 : 7 ]), int ( _dtoconv [ - 2 :]))


def  main ():
    # Solo acepta un código de 4 dígitos
    askandcheck ( "^ [0-9] {4} $" , "Identificación (4 Dígitos):" )
    numeroID = captura
    # Nombre, de 1 a 20 letras mayúsculas, o espacio.
    askandcheck ( "^ ([AZ]) {1,20} $" , "Nombre:" )
    nombre = captura
    # S o N
    Askandcheck ( "^ [S | N] $" , "Acepta (S / N):" )
    acepta = captura
    # Fecha
    askandcheck ( "^ (19 | 20) \ d \ d [-] (0 [1-9] | 1 [012]) [-] (0 [1-9] | [12] [0-9] | 3 [01]) $ " , " Dame una fecha (AAAA-MM-DD): " )
    fecha = captura

    imprimir ( numeroID )
    imprimir ( nombre )
    imprimir ( acepta )
    imprimir ( fecha )