import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Set Year'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        year = self.initUI()
        


 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        year = self.getDate()
        self.show()
        self.close()
        return(year)
 
    def getDate(self):
        i, okPressed = QInputDialog.getInt(self, "Select a Year","Year:", 2018, 2013, 2030  , 1)
        if okPressed:
            return i

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())