import RPi.GPIO as GPIO
import MFRC522
import signal
from mfrc522 import SimpleMFRC522

continue_reading =True


def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()
    
signal.signal(signal.SIGINT, end_read)
# create the reader object
MIFAREReader = MFRC522.MFRC522()
reader = SimpleMFRC522()

def griteRegistro():
    print("==================\n Agregar registro\n==================\n")
    nombres = input('Ingrese su(s) nombre(s):\n')
    apellidos = input('Inrgese sus apellidos:\n')
    print("Now place your tag to write")
    text = nombres + '$' + apellidos
    reader.write(text)
    print("Written")
menu = "Menú de opciones\n\t1. Leer registros.\n\t2. Agregar registro.\n\t3. Eliminar registro.\n\t4. Terminar.\nIngrese la opción que desea ejecutar (ej: 4)\n"

def showTerminal():
    while True:
        option = input(menu)
        if option == "1":
            print("Leyendo registro")
            readRFID()
        elif option == "2":
            griteRegistro()
        else:
            print("Opción no válida.")
showTerminal()