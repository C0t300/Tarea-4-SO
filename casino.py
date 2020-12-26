import threading
import time
from queue import Queue
from atiende import atiende
from cliente import cliente

fila = Queue() #fila.put() | fila.get()
dejarBandeja = threading.Semaphore()
cantBandejas = int(input("¿Cuantas bandejas existen?: "))
cantClientes= int(input("¿Cuantos clientes llegaran?: "))
bandejero = 0

fila.put(cliente(0, True))
i = 1
while i < cantClientes:
    fila.put(cliente(i, False))
    i += 1






# Create new threads
thread1 = atiende(1, "Thread-1", 1)
thread2 = atiende(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print ("Exiting Main Thread")