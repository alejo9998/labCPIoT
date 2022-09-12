import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading =True

def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read. ")
    continue_reading= False
    GPIO.cleanup()

signal.signal(signal.SIFINT, end_read)

MIFAREReader = MFRC522.MFRC%""()

print("Welcome to MFRC522 RFID Read example")