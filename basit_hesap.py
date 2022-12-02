# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basit_hesap.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(237, 199)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sonuc = QtWidgets.QTextBrowser(self.centralwidget)
        self.sonuc.setGeometry(QtCore.QRect(10, 90, 211, 81))
        self.sonuc.setObjectName("sonuc")
        self.kos = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.hesapla() )
        self.kos.setGeometry(QtCore.QRect(130, 60, 75, 23))
        self.kos.setObjectName("kos")
        self.input_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.input_1.setGeometry(QtCore.QRect(10, 10, 104, 31))
        self.input_1.setObjectName("input_1")
        self.input_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.input_2.setGeometry(QtCore.QRect(10, 50, 104, 31))
        self.input_2.setObjectName("input_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def hesapla(self):
        
        x=int(self.input_1.toPlainText())
        y=int(self.input_2.toPlainText())
        toplama=x+y
        cikarma=x-y
        carpma=x*y
        bolme=x/y
        self.sonuc.setText("iki sayının toplamı = "+ str(toplama)
                           +" dır \n iki sayının farkı = "+ str(cikarma)
                           +" dır \n ki sayının çarpımı = "+ str(carpma)
                           +" dır \n ki sayının ölümü = "+ str(bolme)+" dır")
        print("iki sayının toplamı = " + str(toplama))
        print("iki sayının farkı = " + str(cikarma))
        print("iki sayının çarpımı = " + str(carpma))
        print("iki sayının bölümü = " + str(bolme))
   
    def yazdir(self):
        
        self.sonuc.setText(str(self.input_1.toPlainText()))
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.kos.setText(_translate("MainWindow", "işlem yap"))

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
