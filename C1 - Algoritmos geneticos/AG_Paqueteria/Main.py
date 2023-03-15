from Logica import AG_Paqueteria
from PyQt5 import QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox, QButtonGroup

import sys, subprocess

from View import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):

# Archivo principal

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        mywindow.setWindowTitle(self,"Algoritmos Genéticos - Paqueteria")

        self.ui.pushButton_iniciar.clicked.connect(self.boton_iniciar)
        self.ui.line_Tam_Pob_Inic.setValidator(QtGui.QIntValidator())
        self.ui.line_Tam_Pob_Max.setValidator(QtGui.QIntValidator())
        self.ui.line_Tam_paquete.setValidator(QtGui.QIntValidator())
        self.ui.line_Cantidad_Paquetes.setValidator(QtGui.QIntValidator())
        self.ui.line_Precio_Publico.setValidator(QtGui.QIntValidator())
        self.ui.line_Costo_Envio.setValidator(QtGui.QIntValidator())
        self.ui.line_contenedor.setValidator(QtGui.QIntValidator())
        self.ui.comboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.ui.spinBoxGeneraciones.setMinimum(1)
        self.ui.spinBoxGeneraciones.setMaximum(1000)
        self.ui.radioButton_modificar.clicked.connect(self.radio)
        self.Categoria = 'A'


        Tam_Pob_Inic = int(self.ui.line_Tam_Pob_Inic.text())
        Tam_Pob_Max  = int(self.ui.line_Tam_Pob_Max.text())
        Prob_Mut_inic = float(self.ui.line_Prob_Mut_Ind.text())
        Prob_Mut_Gen = float(self.ui.line_Prob_Mut_Gen.text())
        generaciones = self.ui.spinBoxGeneraciones.value()
        contenedor = int(self.ui.line_contenedor.text())


        self.clase = AG_Paqueteria(Tam_Pob_Inic,Tam_Pob_Max,Prob_Mut_inic,Prob_Mut_Gen,generaciones,contenedor)
    

    def radio(self):
        if self.ui.radioButton_modificar.isChecked():
            self.ui.line_Tam_paquete.setDisabled(False)
            self.ui.line_Cantidad_Paquetes.setDisabled(False)
            self.ui.line_Precio_Publico.setDisabled(False)
            self.ui.line_Costo_Envio.setDisabled(False)
        else:
            self.ui.line_Tam_paquete.setDisabled(True)
            self.ui.line_Cantidad_Paquetes.setDisabled(True)
            self.ui.line_Precio_Publico.setDisabled(True)
            self.ui.line_Costo_Envio.setDisabled(True)

    def on_combobox_changed(self):
        lista = []
        lista.append(int(self.ui.line_Tam_paquete.text()))
        lista.append(int(self.ui.line_Cantidad_Paquetes.text()))
        lista.append(int(self.ui.line_Precio_Publico.text()))
        lista.append(int(self.ui.line_Costo_Envio.text()))

        if self.Categoria =='A':
            self.clase.setPaqueteA(lista)
        if self.Categoria =='B':
            self.clase.setPaqueteB(lista)
        if self.Categoria =='C':
            self.clase.setPaqueteC(lista)
        if self.Categoria =='D':
            self.clase.setPaqueteD(lista)
        if self.Categoria =='E':
            self.clase.setPaqueteE(lista)

        valor = str(self.ui.comboBox.currentText())

        if valor =='A':
            self.Categoria = 'A'
            lista = self.clase.getPaqueteA()
            self.ui.line_Tam_paquete.setText(str(lista[0]))
            self.ui.line_Cantidad_Paquetes.setText(str(lista[1]))
            self.ui.line_Precio_Publico.setText(str(lista[2]))
            self.ui.line_Costo_Envio.setText(str(lista[3]))

        if valor =='B':
            self.Categoria = 'B'
            lista = self.clase.getPaqueteB()
            self.ui.line_Tam_paquete.setText(str(lista[0]))
            self.ui.line_Cantidad_Paquetes.setText(str(lista[1]))
            self.ui.line_Precio_Publico.setText(str(lista[2]))
            self.ui.line_Costo_Envio.setText(str(lista[3]))

        if valor =='C':
            self.Categoria = 'C'
            lista = self.clase.getPaqueteC()
            self.ui.line_Tam_paquete.setText(str(lista[0]))
            self.ui.line_Cantidad_Paquetes.setText(str(lista[1]))
            self.ui.line_Precio_Publico.setText(str(lista[2]))
            self.ui.line_Costo_Envio.setText(str(lista[3]))

        if valor =='D':
            self.Categoria = 'D'
            lista = self.clase.getPaqueteD()
            self.ui.line_Tam_paquete.setText(str(lista[0]))
            self.ui.line_Cantidad_Paquetes.setText(str(lista[1]))
            self.ui.line_Precio_Publico.setText(str(lista[2]))
            self.ui.line_Costo_Envio.setText(str(lista[3]))

        if valor =='E':
            self.Categoria = 'E'
            lista = self.clase.getPaqueteE()
            self.ui.line_Tam_paquete.setText(str(lista[0]))
            self.ui.line_Cantidad_Paquetes.setText(str(lista[1]))
            self.ui.line_Precio_Publico.setText(str(lista[2]))
            self.ui.line_Costo_Envio.setText(str(lista[3]))


    def boton_iniciar(self):
        msg = QMessageBox()
        Tam_Pob_Inic = int(self.ui.line_Tam_Pob_Inic.text())
        Tam_Pob_Max  = int(self.ui.line_Tam_Pob_Max.text())
        Prob_Mut_inic = float(self.ui.line_Prob_Mut_Ind.text())
        Prob_Mut_Gen = float(self.ui.line_Prob_Mut_Gen.text())
        generaciones = self.ui.spinBoxGeneraciones.value()
        tamaño_contenedor = int(self.ui.line_contenedor.text())



        lista = []
        lista.append(int(self.ui.line_Tam_paquete.text()))
        lista.append(int(self.ui.line_Cantidad_Paquetes.text()))
        lista.append(int(self.ui.line_Precio_Publico.text()))
        lista.append(int(self.ui.line_Costo_Envio.text()))

        if self.Categoria =='A':
            self.clase.setPaqueteA(lista)
        if self.Categoria =='B':
            self.clase.setPaqueteB(lista)
        if self.Categoria =='C':
            self.clase.setPaqueteC(lista)
        if self.Categoria =='D':
            self.clase.setPaqueteD(lista)
        if self.Categoria =='E':
            self.clase.setPaqueteE(lista)

        if Tam_Pob_Max < Tam_Pob_Inic:

            msg.setWindowTitle("ERROR")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("La población Máxima no puede ser igual o menor a la población inicial!")
            msg.exec_()
            return
        
        if Prob_Mut_Gen >100 or Prob_Mut_Gen <=0 or Prob_Mut_inic >100 or Prob_Mut_inic <=0:
            msg.setWindowTitle("ERROR")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("La probabilidad de mutación por gen e individuo no puede superar del 100% o ser inferior del 0%!")
            msg.exec_()
            return
        
        self.clase.setTam_Pob_Inic(Tam_Pob_Inic)
        self.clase.setTam_Pob_Max(Tam_Pob_Max)
        self.clase.setProb_Mut_Ind(Prob_Mut_inic)
        self.clase.setProb_Mut_Gen(Prob_Mut_Gen)
        self.clase.setnumGeneraciones(generaciones)
        self.clase.setEspacio_contenedor(tamaño_contenedor)

        self.clase.iniciar_programa()

        # msg.setWindowTitle("Exito!")
        # msg.setIcon(QMessageBox.Information)
        # msg.setStandardButtons(QMessageBox.Open | QMessageBox.Close)
        # msg.setDefaultButton(QMessageBox.Close) 
        # boton_abrir = msg.button(QMessageBox.Open)
        # boton_abrir.setText("Abrir Carpeta")
        # boton_cerrar =  msg.button(QMessageBox.Close)
        # boton_cerrar.setText("Cerrar ventana")
        # msg.setText("El algoritmo de paqueteria ha terminado exitosamente!, deseas ver el resultado?")
        # msg.exec()
        # if msg.clickedButton() == boton_abrir:
        #     subprocess.Popen(r'explorer /select,"Resultados\"')
        subprocess.Popen(r'explorer /select,"Resultados\"')


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())