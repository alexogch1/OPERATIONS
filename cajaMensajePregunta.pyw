import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class BoxMessageQuestion(QWidget):

    def __init__(self,title, question):
        super().__init__()
        global answer
        self.title = 'Caja de Mensaje'
        self.left = 500
        self.top = 350
        self.width = 320
        self.height = 200
        self.title = title
        self.question = question
        self.initUI()

    def initUI(self):
        global buttonReply
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        title = "Add Product"
        question = "Do you want to add a new product?"
        buttonReply = QMessageBox.question(self, self.title, self.question, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            answer = "YES"
            print('THE ANSWER IS ', answer,buttonReply)
            
        else:
            answer = "NO"
            print('THE ANSWER IS ', answer, buttonReply)
        buttonReply = (buttonReply)    
       
        print('el valor del boton es:',buttonReply)
        self.pregunta()
        return buttonReply
    
    def pregunta (self):
        respuesta = buttonReply
        return respuesta
        print(respuesta)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    title = "hola"
    question = "que onda"
    ex = BoxMessageQuestion(title,question )
    #print('el valor del boton es:',buttonReply)
    sys.exit(app.exec_())