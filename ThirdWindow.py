# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Cricket\ThirdWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ThirdWindow(object):
    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("ThirdWindow")
        ThirdWindow.resize(259, 286)
        self.centralwidget = QtWidgets.QWidget(ThirdWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 186, 126))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l1 = QtWidgets.QLabel(self.layoutWidget)
        self.l1.setObjectName("l1")
        self.horizontalLayout.addWidget(self.l1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.t1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.t1.setInputMask("")
        self.t1.setText("")
        self.t1.setClearButtonEnabled(True)
        self.t1.setObjectName("t1")
        self.verticalLayout.addWidget(self.t1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b1 = QtWidgets.QPushButton(self.layoutWidget)
        self.b1.setObjectName("b1")
        self.horizontalLayout_2.addWidget(self.b1)
        self.b2 = QtWidgets.QPushButton(self.layoutWidget)
        self.b2.setObjectName("b2")
        self.horizontalLayout_2.addWidget(self.b2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        ThirdWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ThirdWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 259, 21))
        self.menubar.setObjectName("menubar")
        ThirdWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThirdWindow)
        self.statusbar.setObjectName("statusbar")
        ThirdWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

    def retranslateUi(self, ThirdWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow.setWindowTitle(_translate("ThirdWindow", "MainWindow"))
        self.l1.setText(_translate("ThirdWindow", "Player Name:"))
        self.b1.setText(_translate("ThirdWindow", "Find Player"))
        self.b2.setText(_translate("ThirdWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThirdWindow = QtWidgets.QMainWindow()
    ui = Ui_ThirdWindow()
    ui.setupUi(ThirdWindow)
    ThirdWindow.show()
    sys.exit(app.exec_())

