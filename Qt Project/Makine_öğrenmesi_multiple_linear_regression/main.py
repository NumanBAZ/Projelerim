import sys
import pickle
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from tasarim import Ui_Form  # QT Designer'dan oluşturulan dosya

class PredictionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()

        self.ui.setupUi(self)
        
        # Modeli yükle
        self.load_model()
        self.ui.pushButton.clicked.connect(self.predict)


    def load_model(self):
            with open('model.pkl', 'rb') as file:
                self.model = pickle.load(file)
            print("Model başarıyla yüklendi.")
      


    def predict(self):
     

            # Input değerlerini al
            input1 = float(self.ui.lineEdit.text())
            input2 = float(self.ui.lineEdit_2.text())
            input3 = float(self.ui.lineEdit_3.text())
            input4 = float(self.ui.lineEdit_4.text())
            input5 = float(self.ui.lineEdit_5.text())

            # Model tahmini
            inputs = [[input1, input2, input3, input4, input5]]
            prediction = self.model.predict(inputs)
         
            # Sonucu 'sonuc' adlı label'a yazdır
            self.ui.predict.setText(f"{prediction[0]:.2f}")

     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PredictionApp()
    window.show()
    sys.exit(app.exec_())
