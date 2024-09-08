def evaluar(a, b, c):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    if ((a>= (b+c))|(b>= (a+c))|(c>=(a+b))):
        return "No es un triángulo válido"
    elif ((a==b) & (b==c)):
        return "El triángulo es equilátero"
    elif (((a==b) & (b!=c))|((a==c)&(c!=b))|((b==c)&(c!=a))):
        return "El triángulo es isósceles"
    else:   
        return "El triángulo es escaleno"

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
