import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading =True


def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()
    
signal.signal(signal.SIGINT, end_read)
# create the reader object
MIFAREReader = MFRC522.MFRC522()

def readRFID():
    while True:
        # detect touch of the card, get status and tag type
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        # check if card detected or not

        # Get the RFID card uid and status
        (status, uid) = MIFAREReader.MFRC522_Anticoll()
        # If status is alright, continue to the next stage
        if status == MIFAREReader.MI_OK:
            try:
                print(uid)
                
            except:
                break
                
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