
from server import *
from adapter import*
from threading import Thread
from mainUI import *

class MainApplication:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        sys.exit(app.exec_())
        # adpt = Adapter(file_name)
        # self.s = Server()
        # print(adpt.longest_column)
        # print(adpt.nrows)

        # self.server_thread = Thread(target=self.start_server)
        # self.server_thread.start()
        
        print("HEY HEY")

    def start_server(self):
        self.s.run()

if __name__ == "__main__":
    MainApplication()
    
