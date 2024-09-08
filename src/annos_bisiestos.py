def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 2: Años bisiestos
    
    if anno%4==0:
        if anno%100==0:
            if anno%400==0:
                
                return str(anno) + " es bisiesto"
            else:
                
                return str(anno) + " no es bisiesto"
        else:
            
            return str(anno) + " es bisiesto"
    else:
        
        return str(anno) + " no es bisiesto"
    

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
