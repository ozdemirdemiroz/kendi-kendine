# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hesap_mak.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(171, 221)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.sifir())
        self.pushButton_0.setGeometry(QtCore.QRect(20, 140, 61, 30))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.bir())
        self.pushButton_1.setGeometry(QtCore.QRect(20, 110, 30, 30))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.iki())
        self.pushButton_2.setGeometry(QtCore.QRect(50, 110, 30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.uc())
        self.pushButton_3.setGeometry(QtCore.QRect(80, 110, 30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.dort())
        self.pushButton_4.setGeometry(QtCore.QRect(20, 80, 30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.bes())
        self.pushButton_5.setGeometry(QtCore.QRect(50, 80, 30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.alti())
        self.pushButton_6.setGeometry(QtCore.QRect(80, 80, 30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.yedi())
        self.pushButton_7.setGeometry(QtCore.QRect(20, 50, 30, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.sekiz())
        self.pushButton_8.setGeometry(QtCore.QRect(50, 50, 30, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.dokuz())
        self.pushButton_9.setGeometry(QtCore.QRect(80, 50, 30, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 20, 131, 23))
        self.lcdNumber.setStyleSheet("""QLCDNumber { background-color: black; color: white;}""")            
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_topla = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.topla())
        self.pushButton_topla.setGeometry(QtCore.QRect(120, 140, 30, 30))
        self.pushButton_topla.setObjectName("pushButton_topla")
        self.pushButton_cikar = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.cikart())
        self.pushButton_cikar.setGeometry(QtCore.QRect(120, 110, 30, 30))
        self.pushButton_cikar.setObjectName("pushButton_cikar")
        self.pushButton_carp = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.carp())
        self.pushButton_carp.setGeometry(QtCore.QRect(120, 80, 30, 30))
        self.pushButton_carp.setObjectName("pushButton_carp")
        self.pushButton_bol = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.bol())
        self.pushButton_bol.setGeometry(QtCore.QRect(120, 50, 30, 30))
        self.pushButton_bol.setObjectName("pushButton_bol")
        self.pushButton_nokta = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_nokta.setGeometry(QtCore.QRect(80, 140, 30, 30))
        self.pushButton_nokta.setObjectName("pushButton_nokta")
        self.pushButton_Enter = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.islem())
        self.pushButton_Enter.setGeometry(QtCore.QRect(20, 170, 90, 30))
        self.pushButton_Enter.setObjectName("pushButton_Enter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.sayi=''
        self.sayi1=''
        self.dortislem=''
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    
    def sifir(self):
        self.sayi=self.sayi+"0"
        self.lcdNumber.display(int(self.sayi))
    def bir(self):
        self.sayi=self.sayi+"1"
        self.lcdNumber.display(int(self.sayi))
    def iki(self):
        self.sayi=self.sayi+"2"
        self.lcdNumber.display(int(self.sayi))
    def uc(self):
        self.sayi=self.sayi+"3"
        self.lcdNumber.display(int(self.sayi))
    def dort(self):
        self.sayi=self.sayi+"4"
        self.lcdNumber.display(int(self.sayi))
    def bes(self):
        self.sayi=self.sayi+"5"
        self.lcdNumber.display(int(self.sayi))
    def alti(self):
        self.sayi=self.sayi+"6"
        self.lcdNumber.display(int(self.sayi))
    def yedi(self):
        self.sayi=self.sayi+"7"
        self.lcdNumber.display(int(self.sayi))
    def sekiz(self):
        self.sayi=self.sayi+"8"
        self.lcdNumber.display(int(self.sayi))
    def dokuz(self):
        self.sayi=self.sayi+"9"
        self.lcdNumber.display(int(self.sayi))
    
    def topla(self):
        self.sayi1=self.sayi
        self.sayi=""
        self.dortislem="to"
        
    def cikart(self):
        self.sayi1=self.sayi
        self.sayi=""
        self.dortislem="ci"
    
    def carp(self):
        self.sayi1=self.sayi
        self.sayi=""    
        self.dortislem="ca"
    
    def bol(self):
        self.sayi1=self.sayi
        self.sayi=""
        self.dortislem="bo"
    
    def islem(self):
        if self.dortislem=="to":
            sonuc = int(self.sayi1)+int(self.sayi)
        elif self.dortislem=="ci":
            sonuc = int(self.sayi1)-int(self.sayi)
        elif self.dortislem=="ca":
            sonuc = int(self.sayi1)*int(self.sayi)
        elif self.dortislem=="bo":
            sonuc = int(self.sayi1)/int(self.sayi)
        else: 
            sonuc = "0000"
        self.sayi=""
        self.sayi1=""
        self.lcdNumber.display(int(sonuc))
        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_topla.setText(_translate("MainWindow", "+"))
        self.pushButton_cikar.setText(_translate("MainWindow", "-"))
        self.pushButton_carp.setText(_translate("MainWindow", "*"))
        self.pushButton_bol.setText(_translate("MainWindow", "/"))
        self.pushButton_nokta.setText(_translate("MainWindow", "."))
        self.pushButton_Enter.setText(_translate("MainWindow", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())