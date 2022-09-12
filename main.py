import RPi.GPIO as GPIO
import signal
import time
from mfrc522 import SimpleMFRC522


reader = SimpleMFRC522()

continue_reading =True


def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()
    
signal.signal(signal.SIGINT, end_read)

def griteRegistro():
    print("==================\n Agregar registro\n==================\n")
    nombres = input('Ingrese su(s) nombre(s):\n')
    apellidos = input('Inrgese sus apellidos:\n')
    nid = input('Ingrese el id correspondiente\n')
    print("Por favor coloque el tag sobre el lector")
    text = nombres + '$' + apellidos + '$' + nid
    reader.write(text)
    print('Valores escritos:\n'+'nombre(s):' + nombres +'\nApellidos:' + apellidos + '\nCodigo:' + nid)
    time.sleep(0.5)
   
    
def readRFID():
            print("Coloque la tarjeta sobre el lector")
            id, text = reader.read()
            print("ID: %s\nText: %s" % (id,text))
            time.sleep(0.5)
          
            
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