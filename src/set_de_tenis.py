def evaluar(A, B):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    if ((A >= 6) | (B >= 6)):
            if (((A > 7) & (B >= 6))|((B > 7) & (A >= 6))):
                return "Inválido"
            
            if (((A == 7) & (B < 5)) | ((B == 7) & (A < 5))):
                return "Inválido"
            
            if (((A >= 6) & (A <= 7)) & (A >= (B + 2))):
                return "Ganó A"
            elif (((B >= 6) & (B <= 7)) & (B >= (A + 2))): 
                return "Ganó B"
            
            if ((A == 7) & (B == 6)):
                return "Ganó A"
            elif ((B == 7) & (A == 6)):
                return "Ganó B"
    return "Aún no termina"

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    A = int(input())
    print("Los juegos ganaddor por B:", end="")
    B = int(input())

    respuesta = evaluar(A, B)
    print(respuesta)
