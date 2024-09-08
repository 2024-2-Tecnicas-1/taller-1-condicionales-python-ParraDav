from time import localtime
from datetime import datetime 
def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    
    nacimiento = datetime(anno, mes, dia)
    hoy = datetime.now()
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day)<(nacimiento.month, nacimiento.day))
    return "Usted tiene " + str(edad) + " años"

def main():
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anno = int(input("Año: "))
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
    if __name__ == "__main__":
        main()
