# Ahorcado

Este es un sencillo juego del **Ahorcado** desarrollado en Python. El objetivo del juego es adivinar una palabra oculta antes de que se agoten las vidas del jugador.

## Descripción

El programa solicita al jugador que introduzca una palabra secreta, la cual será adivinada por otro jugador. Se le presenta al adivinador una serie de guiones bajos (`_`), uno por cada letra de la palabra. El jugador debe ir adivinando letras y, si acierta, estas se mostrarán en su respectiva posición dentro de la palabra.

El juego tiene un máximo de 7 intentos. Si se alcanzan 7 fallos antes de adivinar la palabra, el jugador pierde.

## Requisitos

- Python 3.x
- La librería `getpass` (incluida en la instalación base de Python)

## Instalación

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/mibullfire/ahorcado.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd ahorcado
    ```

## Ejecución del programa

Para iniciar el juego, ejecuta el siguiente comando en tu terminal:

```bash
python main.py
