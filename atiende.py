import threading
import time



class atiende (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      run(self.name)
      print ("Exiting " + self.name)

def run(algo):
    print("hola soy "+ algo )