# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nur\dam\Alia\ddd.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 605)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(320, 90, 361, 371))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);\n"
"border-radius: 5px;")
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 540, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 540, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 851, 401))
        self.label.setStyleSheet("image: url(:/imge/image.PNG);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Слушать"))
        self.pushButton_2.setText(_translate("MainWindow", "Стоп"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

import source_imege_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
