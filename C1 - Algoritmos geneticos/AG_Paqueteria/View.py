# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'visual_paqueteria (2).ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(536, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(240, 20, 81, 31))
        self.label.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QtCore.QRect(70, 70, 311, 31))
        self.label_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QtCore.QRect(70, 120, 271, 31))
        self.label_3.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QtCore.QRect(70, 170, 191, 31))
        self.label_4.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QtCore.QRect(70, 220, 211, 41))
        self.label_5.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QtCore.QRect(70, 260, 141, 31))
        self.label_6.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QtCore.QRect(70, 300, 161, 31))
        self.label_7.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.line_Prob_Mut_Ind = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Prob_Mut_Ind.setObjectName(u"line_Prob_Mut_Ind")
        self.line_Prob_Mut_Ind.setGeometry(QtCore.QRect(390, 80, 71, 20))
        self.line_Prob_Mut_Ind.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Prob_Mut_Gen = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Prob_Mut_Gen.setObjectName(u"line_Prob_Mut_Gen")
        self.line_Prob_Mut_Gen.setGeometry(QtCore.QRect(390, 130, 71, 20))
        self.line_Prob_Mut_Gen.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Tam_Pob_Inic = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Tam_Pob_Inic.setObjectName(u"line_Tam_Pob_Inic")
        self.line_Tam_Pob_Inic.setGeometry(QtCore.QRect(350, 270, 111, 20))
        self.line_Tam_Pob_Inic.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Tam_Pob_Max = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Tam_Pob_Max.setObjectName(u"line_Tam_Pob_Max")
        self.line_Tam_Pob_Max.setGeometry(QtCore.QRect(350, 310, 111, 20))
        self.line_Tam_Pob_Max.setAlignment(QtCore.Qt.AlignCenter)
        self.line_contenedor = QtWidgets.QLineEdit(self.centralwidget)
        self.line_contenedor.setObjectName(u"line_contenedor")
        self.line_contenedor.setGeometry(QtCore.QRect(330, 230, 131, 21))
        self.line_contenedor.setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(330, 370, 41, 22))
        self.comboBox.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.line_Precio_Publico = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Precio_Publico.setObjectName(u"line_Precio_Publico")
        self.line_Precio_Publico.setEnabled(False)
        self.line_Precio_Publico.setGeometry(QtCore.QRect(70, 380, 71, 20))
        self.line_Precio_Publico.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Tam_paquete = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Tam_paquete.setObjectName(u"line_Tam_paquete")
        self.line_Tam_paquete.setEnabled(False)
        self.line_Tam_paquete.setGeometry(QtCore.QRect(150, 380, 71, 20))
        self.line_Tam_paquete.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Cantidad_Paquetes = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Cantidad_Paquetes.setObjectName(u"line_Cantidad_Paquetes")
        self.line_Cantidad_Paquetes.setEnabled(False)
        self.line_Cantidad_Paquetes.setGeometry(QtCore.QRect(260, 370, 71, 20))
        self.line_Cantidad_Paquetes.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Costo_Envio = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Costo_Envio.setObjectName(u"line_Costo_Envio")
        self.line_Costo_Envio.setEnabled(False)
        self.line_Costo_Envio.setGeometry(QtCore.QRect(380, 370, 71, 20))
        self.line_Costo_Envio.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton_iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_iniciar.setObjectName(u"pushButton_iniciar")
        self.pushButton_iniciar.setGeometry(QtCore.QRect(40, 360, 461, 51))
        self.pushButton_iniciar.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 12px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0.534091 rgba(255, 174, 5, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton_modificar = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_modificar.setObjectName(u"radioButton_modificar")
        self.radioButton_modificar.setEnabled(False)
        self.radioButton_modificar.setGeometry(QtCore.QRect(250, 390, 171, 17))
        self.radioButton_modificar.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.spinBoxGeneraciones = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxGeneraciones.setObjectName(u"spinBoxGeneraciones")
        self.spinBoxGeneraciones.setGeometry(QtCore.QRect(380, 170, 81, 31))
        self.spinBoxGeneraciones.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.spinBoxGeneraciones.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxGeneraciones.setValue(5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.radioButton_modificar.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.line_Prob_Mut_Ind.raise_()
        self.line_Prob_Mut_Gen.raise_()
        self.line_Tam_Pob_Inic.raise_()
        self.line_Tam_Pob_Max.raise_()
        self.line_contenedor.raise_()
        self.comboBox.raise_()
        self.line_Precio_Publico.raise_()
        self.line_Tam_paquete.raise_()
        self.line_Cantidad_Paquetes.raise_()
        self.line_Costo_Envio.raise_()
        self.pushButton_iniciar.raise_()
        self.spinBoxGeneraciones.raise_()
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","MainWindow",))
        self.label.setText(_translate("MainWindow","191214",))
        self.label_2.setText(_translate("MainWindow","Prob. de mutaci\u00f3n del Individuo:  %",))
        self.label_3.setText(_translate("MainWindow","Prob. de mutaci\u00f3n gen\u00e9tica:  %",))
        self.label_4.setText(_translate("MainWindow","No. de Generaciones:",))
        self.label_5.setText(_translate("MainWindow","Tama\u00f1o del contenedor:",))
        self.label_6.setText(_translate("MainWindow","Poblaci\u00f3n inicial:",))
        self.label_7.setText(_translate("MainWindow","Poblaci\u00f3n m\u00e1xima:",))
        self.line_Prob_Mut_Ind.setText(_translate("MainWindow","30",))
        self.line_Prob_Mut_Gen.setText(_translate("MainWindow","5.5",))
        self.line_Tam_Pob_Inic.setText(_translate("MainWindow","3",))
        self.line_Tam_Pob_Max.setText(_translate("MainWindow","7",))
        self.line_contenedor.setText(_translate("MainWindow","294",))
        self.comboBox.setItemText(0, _translate("MainWindow","A",))
        self.comboBox.setItemText(1, _translate("MainWindow","B",))
        self.comboBox.setItemText(2, _translate("MainWindow","C",))
        self.comboBox.setItemText(3, _translate("MainWindow","D",))
        self.comboBox.setItemText(4, _translate("MainWindow","E",))

        self.line_Precio_Publico.setText(_translate("MainWindow","100",))
        self.line_Tam_paquete.setText(_translate("MainWindow","7",))
        self.line_Cantidad_Paquetes.setText(_translate("MainWindow", u"9",))
        self.line_Costo_Envio.setText(_translate("MainWindow","35",))
        self.pushButton_iniciar.setText(_translate("MainWindow","INICIAR",))
        self.radioButton_modificar.setText(_translate("MainWindow","Modificar Campos",))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

