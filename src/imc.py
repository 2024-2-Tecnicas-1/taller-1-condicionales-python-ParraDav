def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
    imc = ((peso)/(estatura * estatura))
    if((imc<22) & (edad <45)):
        return "bajo"
    elif(((imc<22) & (edad >=45))|((imc>=22) & (edad<45))):
        return "medio"
    elif((imc>=22) & (edad>=45)):
         return "alto"
    return ""
 
if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
