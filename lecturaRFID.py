import RPi.GPIO as GPIO
import MFRC522
import signal
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

continue_reading =True


def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()
    
signal.signal(signal.SIGINT, end_read)
# create the reader object

def readRFID():
            print("Hold a tag near the reader")
            id, text = reader.read()
            print("ID: %s\nText: %s" % (id,text))
            print()
            
menu = "Menú de opciones\n\t1. Leer registros.\n\t2. Agregar registro.\n\t3. Eliminar registro.\n\t4. Terminar.\nIngrese la opción que desea ejecutar (ej: 4)\n"

def showTerminal():
    while True:
        option = input(menu)
        if option == "1":
            print("Leyendo registro")
            readRFID()
        else:
            print("Opción no válida.")
showTerminal()