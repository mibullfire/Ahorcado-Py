from posiciones import *
import getpass

def inicio():
    palabra = getpass.getpass('Bienvenido, elija una palabra: ') # Empezamos el programa solicitando al usuario una palabra, la cual no se imprimirá en pantalla y permanecerá oculta.
    letras = [letra for letra in palabra] # Creamos una lista con cada una de las letras de la palabra.
    return palabra, letras

def ahorcado(palabra, letras):
    vida = 0 # Iniciamos con un valor cero de vidas, si llega a 7 perderá todas (definido en el bucle while).
    jugada = 0 # Contador simple para indicar al jugador cuantas jugadas lleva.
    numero_letras = len(letras)
    
    # A continuación, creamos una lista en la que vamos a ir rellenando la palabra:
    x = []
    for i in letras:
        x.append('_')

    final = str
    
    while final != palabra and vida < 7:
        selección = input('\n\nElija una letra: ')
        print(f'Jugada Número {jugada}.')

        # Creamos un if y un else para ver si la letra esta en la palabra o no.
        if selección in letras:
            print(f'La letra {selección} está en la palabra')

            # Lista para almacenar las posiciones
            posiciones = []

            # Usamos un bucle para encontrar todas las posiciones
            for index, value in enumerate(letras):
                if value == selección:
                    posiciones.append(index)
            
            for posicion in posiciones:
                x[posicion] = selección

            print(x)
            numero_letras = numero_letras - len(posiciones)

        else:
            print(f'Has fallado!')
            print(x)
            print(errores[vida])
            vida = vida + 1

        final = "".join(x)
        jugada = jugada + 1
    
    print(f'Has ganado! La palabra era: {palabra}')
