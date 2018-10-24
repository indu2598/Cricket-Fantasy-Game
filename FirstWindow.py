
from PyQt5 import QtCore, QtGui, QtWidgets
from SecondPage import Ui_SecondPage

class Ui_FirstWindow(object):

    def openWindow(self):
        self.window= QtWidgets.QMainWindow()
        self.ui = Ui_SecondPage()
        self.ui.setupUi(self.window)
        FirstWindow.hide()
        self.window.show()
        
    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(403, 281)
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(128, 190, 155, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.b1 = QtWidgets.QPushButton(self.splitter)
        self.b1.setObjectName("b1")
        
        self.b1.clicked.connect(self.openWindow)
        
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 70, 326, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        FirstWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FirstWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menubar.setObjectName("menubar")
        FirstWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FirstWindow)
        self.statusbar.setObjectName("statusbar")
        FirstWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "MainWindow"))
        self.b1.setText(_translate("FirstWindow", "Enter "))
        self.label.setText(_translate("FirstWindow", "    Welcome to Cricket Fantasy Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirstWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(FirstWindow)
    FirstWindow.show()
    sys.exit(app.exec_())

