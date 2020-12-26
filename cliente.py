import threading

class atiende (threading.Thread):
    def __init__(self, id, comio):
        self.id = id
        self.comio = comio
        

    def run(self):
        pass