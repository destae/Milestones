
from server import *
from adapter import*
from threading import Thread

class MainApplication:
    def __init__(self, file_name: str):
        adpt = Adapter(file_name)
        self.s = Server()
        print(adpt.longest_column)
        print(adpt.nrows)

        self.server_thread = Thread(target=self.start_server)
        self.server_thread.start()
        
        print("HEY HEY")

    def start_server(self):
        self.s.run()

if __name__ == "__main__":
    MainApplication("/home/eden/Desktop/Milestones/7DegreesOfLinus/data/data.sor")
