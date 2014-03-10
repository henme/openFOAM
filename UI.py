# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openFOAM.ui'
#
# Created: Tue Feb 18 13:37:16 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_openFOAM(object):
    def setupUi(self, openFOAM):
        openFOAM.setObjectName(_fromUtf8("openFOAM"))
        openFOAM.resize(844, 641)
        self.gridLayout = QtGui.QGridLayout(openFOAM)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(openFOAM)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Schemes = QtGui.QTabWidget(openFOAM)
        self.Schemes.setObjectName(_fromUtf8("Schemes"))
        self.Solver = QtGui.QWidget()
        self.Solver.setObjectName(_fromUtf8("Solver"))
        self.comboBox = QtGui.QComboBox(self.Solver)
        self.comboBox.setGeometry(QtCore.QRect(40, 180, 311, 29))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton_2 = QtGui.QPushButton(self.Solver)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 360, 98, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.Solver)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 360, 98, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.Solver)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 440, 98, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.textEdit_11 = QtGui.QTextEdit(self.Solver)
        self.textEdit_11.setGeometry(QtCore.QRect(410, 70, 311, 241))
        self.textEdit_11.setObjectName(_fromUtf8("textEdit_11"))
        self.Schemes.addTab(self.Solver, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(570, 220, 98, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 220, 511, 33))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_18 = QtGui.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(40, 160, 391, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(40, 310, 181, 26))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.Schemes.addTab(self.tab_2, _fromUtf8(""))
        self.Controls = QtGui.QWidget()
        self.Controls.setObjectName(_fromUtf8("Controls"))
        self.pushButton_5 = QtGui.QPushButton(self.Controls)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 230, 98, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.Schemes.addTab(self.Controls, _fromUtf8(""))
        self.fvSchemes = QtGui.QWidget()
        self.fvSchemes.setObjectName(_fromUtf8("fvSchemes"))
        self.comboBox_5 = QtGui.QComboBox(self.fvSchemes)
        self.comboBox_5.setGeometry(QtCore.QRect(260, 70, 211, 29))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_6 = QtGui.QComboBox(self.fvSchemes)
        self.comboBox_6.setGeometry(QtCore.QRect(260, 110, 211, 29))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_7 = QtGui.QComboBox(self.fvSchemes)
        self.comboBox_7.setGeometry(QtCore.QRect(260, 150, 211, 29))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_8 = QtGui.QComboBox(self.fvSchemes)
        self.comboBox_8.setGeometry(QtCore.QRect(260, 310, 211, 29))
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_10 = QtGui.QComboBox(self.fvSchemes)
        self.comboBox_10.setGeometry(QtCore.QRect(260, 390, 211, 29))
        self.comboBox_10.setObjectName(_fromUtf8("comboBox_10"))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.textEdit_2 = QtGui.QTextEdit(self.fvSchemes)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 190, 91, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(self.fvSchemes)
        self.textEdit_3.setGeometry(QtCore.QRect(260, 430, 91, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.label_4 = QtGui.QLabel(self.fvSchemes)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 66, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.fvSchemes)
        self.label_5.setGeometry(QtCore.QRect(30, 270, 66, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.fvSchemes)
        self.label_6.setGeometry(QtCore.QRect(170, 70, 51, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.fvSchemes)
        self.label_7.setGeometry(QtCore.QRect(180, 310, 51, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.fvSchemes)
        self.label_8.setGeometry(QtCore.QRect(120, 110, 111, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.fvSchemes)
        self.label_9.setGeometry(QtCore.QRect(130, 350, 111, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.fvSchemes)
        self.label_10.setGeometry(QtCore.QRect(150, 150, 81, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.fvSchemes)
        self.label_11.setGeometry(QtCore.QRect(160, 390, 81, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.fvSchemes)
        self.label_12.setGeometry(QtCore.QRect(150, 200, 71, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.fvSchemes)
        self.label_13.setGeometry(QtCore.QRect(150, 430, 71, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.comboBox_9 = QtGui.QComboBox(self.fvSchemes)
        self.comboBox_9.setGeometry(QtCore.QRect(260, 350, 211, 29))
        self.comboBox_9.setObjectName(_fromUtf8("comboBox_9"))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.label_23 = QtGui.QLabel(self.fvSchemes)
        self.label_23.setGeometry(QtCore.QRect(170, 240, 51, 21))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.fvSchemes)
        self.label_24.setGeometry(QtCore.QRect(170, 480, 51, 21))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.textEdit_7 = QtGui.QTextEdit(self.fvSchemes)
        self.textEdit_7.setGeometry(QtCore.QRect(260, 230, 91, 31))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.textEdit_8 = QtGui.QTextEdit(self.fvSchemes)
        self.textEdit_8.setGeometry(QtCore.QRect(260, 470, 91, 31))
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.Schemes.addTab(self.fvSchemes, _fromUtf8(""))
        self.fvSolution = QtGui.QWidget()
        self.fvSolution.setObjectName(_fromUtf8("fvSolution"))
        self.label_15 = QtGui.QLabel(self.fvSolution)
        self.label_15.setGeometry(QtCore.QRect(50, 90, 151, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.fvSolution)
        self.label_16.setGeometry(QtCore.QRect(130, 180, 71, 21))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.fvSolution)
        self.label_17.setGeometry(QtCore.QRect(100, 280, 101, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.textEdit_4 = QtGui.QTextEdit(self.fvSolution)
        self.textEdit_4.setGeometry(QtCore.QRect(240, 90, 104, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.textEdit_5 = QtGui.QTextEdit(self.fvSolution)
        self.textEdit_5.setGeometry(QtCore.QRect(240, 180, 104, 31))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_6 = QtGui.QTextEdit(self.fvSolution)
        self.textEdit_6.setGeometry(QtCore.QRect(240, 270, 104, 31))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.Schemes.addTab(self.fvSolution, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(30, 20, 191, 26))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(230, 120, 151, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.comboBox_4 = QtGui.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(200, 70, 201, 29))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(65, 120, 141, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 240, 731, 201))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 729, 199))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.textEdit_9 = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_9.setGeometry(QtCore.QRect(0, 0, 731, 201))
        self.textEdit_9.setObjectName(_fromUtf8("textEdit_9"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 460, 551, 33))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_6 = QtGui.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(610, 460, 98, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_19 = QtGui.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(140, 180, 66, 21))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.textEdit_10 = QtGui.QTextEdit(self.tab)
        self.textEdit_10.setGeometry(QtCore.QRect(230, 180, 151, 31))
        self.textEdit_10.setObjectName(_fromUtf8("textEdit_10"))
        self.Schemes.addTab(self.tab, _fromUtf8(""))
        self.Boundary_Conditions = QtGui.QWidget()
        self.Boundary_Conditions.setObjectName(_fromUtf8("Boundary_Conditions"))
        self.Schemes.addTab(self.Boundary_Conditions, _fromUtf8(""))
        self.gridLayout.addWidget(self.Schemes, 1, 0, 1, 1)

        self.retranslateUi(openFOAM)
        self.Schemes.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), openFOAM.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), openFOAM.reject)
        QtCore.QMetaObject.connectSlotsByName(openFOAM)

    def retranslateUi(self, openFOAM):
        openFOAM.setWindowTitle(_translate("openFOAM", "openFOAM", None))
        self.comboBox.setItemText(0, _translate("openFOAM", "None", None))
        self.comboBox.setItemText(1, _translate("openFOAM", "icoFoam", None))
        self.comboBox.setItemText(2, _translate("openFOAM", "simpleFoam", None))
        self.comboBox.setItemText(3, _translate("openFOAM", "pisoFoam", None))
        self.comboBox.setItemText(4, _translate("openFOAM", "nonNewtonianIcoFoam", None))
        self.comboBox.setItemText(5, _translate("openFOAM", "pimpleFoam", None))
        self.pushButton_2.setText(_translate("openFOAM", "New Case", None))
        self.pushButton_3.setText(_translate("openFOAM", "Load Case", None))
        self.pushButton_4.setText(_translate("openFOAM", "paraFOAM", None))
        self.textEdit_11.setHtml(_translate("openFOAM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Use the combobox to choose an appropriate solver</span></p></body></html>", None))
        self.Schemes.setTabText(self.Schemes.indexOf(self.Solver), _translate("openFOAM", "Solver", None))
        self.pushButton.setText(_translate("openFOAM", "Load", None))
        self.lineEdit.setText(_translate("openFOAM", "Path", None))
        self.label_18.setText(_translate("openFOAM", "Import Mesh", None))
        self.checkBox_2.setText(_translate("openFOAM", "Suply  mesh manually", None))
        self.Schemes.setTabText(self.Schemes.indexOf(self.tab_2), _translate("openFOAM", "Mesh", None))
        self.pushButton_5.setText(_translate("openFOAM", "Edit Manually", None))
        self.Schemes.setTabText(self.Schemes.indexOf(self.Controls), _translate("openFOAM", "fvSchemes", None))
        self.comboBox_5.setItemText(0, _translate("openFOAM", "GAMG", None))
        self.comboBox_5.setItemText(1, _translate("openFOAM", "PBiCG", None))
        self.comboBox_5.setItemText(2, _translate("openFOAM", "DIC", None))
        self.comboBox_5.setItemText(3, _translate("openFOAM", "diagonal", None))
        self.comboBox_5.setItemText(4, _translate("openFOAM", "smoothSolver", None))
        self.comboBox_6.setItemText(0, _translate("openFOAM", "DILU", None))
        self.comboBox_6.setItemText(1, _translate("openFOAM", "None", None))
        self.comboBox_6.setItemText(2, _translate("openFOAM", "DIC", None))
        self.comboBox_6.setItemText(3, _translate("openFOAM", "FDIC", None))
        self.comboBox_6.setItemText(4, _translate("openFOAM", "GAMG", None))
        self.comboBox_6.setItemText(5, _translate("openFOAM", "diagonal", None))
        self.comboBox_7.setItemText(0, _translate("openFOAM", "GaussSeidel", None))
        self.comboBox_7.setItemText(1, _translate("openFOAM", "None", None))
        self.comboBox_7.setItemText(2, _translate("openFOAM", "DIC", None))
        self.comboBox_7.setItemText(3, _translate("openFOAM", "DICGaussSeidel", None))
        self.comboBox_8.setItemText(0, _translate("openFOAM", "GAMG", None))
        self.comboBox_8.setItemText(1, _translate("openFOAM", "PBiCG", None))
        self.comboBox_8.setItemText(2, _translate("openFOAM", "DIC", None))
        self.comboBox_8.setItemText(3, _translate("openFOAM", "diagonal", None))
        self.comboBox_8.setItemText(4, _translate("openFOAM", "smoothSolver", None))
        self.comboBox_10.setItemText(0, _translate("openFOAM", "GaussSeidel", None))
        self.comboBox_10.setItemText(1, _translate("openFOAM", "None", None))
        self.comboBox_10.setItemText(2, _translate("openFOAM", "DIC", None))
        self.comboBox_10.setItemText(3, _translate("openFOAM", "DICGaussSeidel", None))
        self.textEdit_2.setToolTip(_translate("openFOAM", "<html><head/><body><p><span style=\" font-family:\'arial,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">Solver tolerance</span></p></body></html>", None))
        self.textEdit_2.setHtml(_translate("openFOAM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.00001</p></body></html>", None))
        self.textEdit_3.setToolTip(_translate("openFOAM", "<html><head/><body><p><span style=\" font-family:\'arial,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">Solver tolerance</span></p></body></html>", None))
        self.textEdit_3.setHtml(_translate("openFOAM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.00001</p></body></html>", None))
        self.label_4.setText(_translate("openFOAM", "Pressure", None))
        self.label_5.setText(_translate("openFOAM", "Velocity\n"
"", None))
        self.label_6.setText(_translate("openFOAM", "Solver:", None))
        self.label_7.setText(_translate("openFOAM", "Solver:", None))
        self.label_8.setText(_translate("openFOAM", "Preconditioner:", None))
        self.label_9.setText(_translate("openFOAM", "Preconditioner:", None))
        self.label_10.setText(_translate("openFOAM", "Smoother:", None))
        self.label_11.setText(_translate("openFOAM", "Smoother:", None))
        self.label_12.setText(_translate("openFOAM", "Tolerance:", None))
        self.label_13.setText(_translate("openFOAM", "Tolerance:", None))
        self.comboBox_9.setItemText(0, _translate("openFOAM", "DILU", None))
        self.comboBox_9.setItemText(1, _translate("openFOAM", "None", None))
        self.comboBox_9.setItemText(2, _translate("openFOAM", "DIC", None))
        self.comboBox_9.setItemText(3, _translate("openFOAM", "FDIC", None))
        self.comboBox_9.setItemText(4, _translate("openFOAM", "GAMG", None))
        self.comboBox_9.setItemText(5, _translate("openFOAM", "diagonal", None))
        self.label_23.setText(_translate("openFOAM", "Reltol:", None))
        self.label_24.setText(_translate("openFOAM", "Reltol:", None))
        self.textEdit_7.setToolTip(_translate("openFOAM", "<html><head/><body><p><span style=\" font-family:\'arial,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">Solver relative tolerance</span></p></body></html>", None))
        self.textEdit_7.setHtml(_translate("openFOAM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.01</p></body></html>", None))
        self.textEdit_8.setToolTip(_translate("openFOAM", "<html><head/><body><p><span style=\" font-family:\'arial,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">Solver relative tolerance</span></p></body></html>", None))
        self.textEdit_8.setHtml(_translate("openFOAM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.01</p></body></html>", None))
        self.Schemes.setTabText(self.Schemes.indexOf(self.fvSchemes), _translate("openFOAM", "fvSolutions", None))
        self.label_15.setText(_translate("openFOAM", "Lenght of simulation:", None))
        self.label_16.setText(_translate("openFOAM", "Timestep:", None))
        self.label_17.setText(_translate("openFOAM", "Write interval:", None))
        self.textEdit_4.setHtml(_translate("openFOAM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.textEdit_5.setHtml(_translate("openFOAM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.01</p></body></html>", None))
        self.textEdit_6.setHtml(_translate("openFOAM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>", None))
        self.Schemes.setTabText(self.Schemes.indexOf(self.fvSolution), _translate("openFOAM", "ControlDict", None))
        self.checkBox.setText(_translate("openFOAM", "Turbulence", None))
        self.textEdit.setHtml(_translate("openFOAM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.comboBox_4.setItemText(0, _translate("openFOAM", "kEpsilon", None))
        self.label_14.setText(_translate("openFOAM", "Turbulence viscosity:", None))
        self.textEdit_9.setHtml(_translate("openFOAM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">---------------------------------------Run Additional Terminal Commands-----------------------------------------</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Helpful suggestions:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- checkMesh</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- renumberMesh</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_6.setText(_translate("openFOAM", "Send", None))
        self.label_19.setText(_translate("openFOAM", "Viscosity:", None))
        self.textEdit_10.setHtml(_translate("openFOAM", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.Schemes.setTabText(self.Schemes.indexOf(self.tab), _translate("openFOAM", "Properties", None))
        self.Schemes.setTabText(self.Schemes.indexOf(self.Boundary_Conditions), _translate("openFOAM", "Boundary Conditions", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    openFOAM = QtGui.QDialog()
    ui = Ui_openFOAM()
    ui.setupUi(openFOAM)
    openFOAM.show()
    sys.exit(app.exec_())

