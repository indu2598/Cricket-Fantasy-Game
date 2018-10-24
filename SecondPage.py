# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Cricket\SecondPage.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
conn = sqlite3.connect("C:\sqlite\Cricket.db")
c = conn.cursor()

class Ui_SecondPage(object):

    def showbats(self):
        self.list1.clear()
        c.execute("select Player from MainTable WHERE Category = 1")
        for j in c.fetchall():
            self.list1.addItem(str(*j))
        self.list1.show()

    def showbowl(self):
        self.list1.clear()
        c.execute("select Player from MainTable WHERE Category = 2")
        for j in c.fetchall():
            self.list1.addItem(str(*j))
        self.list1.show()

    def showwk(self):
        self.list1.clear()
        c.execute("select Player from MainTable WHERE Category = 3")
        for j in c.fetchall():
            self.list1.addItem(str(*j))
        self.list1.show()
        
    def showar(self):
        self.list1.clear()
        c.execute("select Player from MainTable WHERE Category = 4")
        for j in c.fetchall():
            self.list1.addItem(str(*j))
        self.list1.show()

    def thirdWindow(self):
        self.window= QtWidgets.QApplication()
        self.ui = Ui_ThirdWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, SecondPage):
        SecondPage.setObjectName("SecondPage")
        SecondPage.resize(534, 478)
        self.centralwidget = QtWidgets.QWidget(SecondPage)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 180, 341, 252))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list1 = QtWidgets.QListWidget(self.layoutWidget)
        self.list1.setObjectName("list1")
        self.horizontalLayout.addWidget(self.list1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.b1 = QtWidgets.QPushButton(self.layoutWidget)
        self.b1.setObjectName("b1")
        
        self.b1.clicked.connect(self.showbats)
        
        self.verticalLayout.addWidget(self.b1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.b2 = QtWidgets.QPushButton(self.layoutWidget)
        self.b2.setObjectName("b2")

        self.b2.clicked.connect(self.showbowl)
        
        self.verticalLayout.addWidget(self.b2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.b3 = QtWidgets.QPushButton(self.layoutWidget)
        self.b3.setObjectName("b3")

        self.b3.clicked.connect(self.showwk)
        
        self.verticalLayout.addWidget(self.b3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.b4 = QtWidgets.QPushButton(self.layoutWidget)
        self.b4.setObjectName("b4")

        self.b4.clicked.connect(self.showar)
        
        self.verticalLayout.addWidget(self.b4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 491, 121))
        self.label.setMinimumSize(QtCore.QSize(191, 0))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/cricket-fantasy-logo-1.png"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.layoutWidget.raise_()
        SecondPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Players = QtWidgets.QMenu(self.menubar)
        self.menuManage_Players.setObjectName("menuManage_Players")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        SecondPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondPage)
        self.statusbar.setObjectName("statusbar")
        SecondPage.setStatusBar(self.statusbar)
        self.p1 = QtWidgets.QAction(SecondPage)
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QAction(SecondPage)
        self.p2.setObjectName("p2")

        self.p2.triggered.connect(self.thirdWindow)
        
        self.a3 = QtWidgets.QAction(SecondPage)
        self.a3.setObjectName("a3")
        self.tm1 = QtWidgets.QAction(SecondPage)
        self.tm1.setObjectName("tm1")
        self.tm2 = QtWidgets.QAction(SecondPage)
        self.tm2.setObjectName("tm2")
        self.tm3 = QtWidgets.QAction(SecondPage)
        self.tm3.setObjectName("tm3")
        self.p3 = QtWidgets.QAction(SecondPage)
        self.p3.setObjectName("p3")
        self.p11 = QtWidgets.QAction(SecondPage)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/addicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p11.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.p11.setFont(font)
        self.p11.setObjectName("p11")
        self.p12 = QtWidgets.QAction(SecondPage)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/findicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p12.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.p12.setFont(font)
        self.p12.setObjectName("p12")
        self.p13 = QtWidgets.QAction(SecondPage)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/deleteicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.p13.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.p13.setFont(font)
        self.p13.setObjectName("p13")
        self.t11 = QtWidgets.QAction(SecondPage)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/newteam.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.t11.setIcon(icon3)
        self.t11.setObjectName("t11")
        self.t12 = QtWidgets.QAction(SecondPage)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/Open team.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.t12.setIcon(icon4)
        self.t12.setObjectName("t12")
        self.t13 = QtWidgets.QAction(SecondPage)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/Evaluate team.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.t13.setIcon(icon5)
        self.t13.setObjectName("t13")
        self.menuManage_Players.addAction(self.p11)
        self.menuManage_Players.addAction(self.p12)
        self.menuManage_Players.addAction(self.p13)
        self.menuManage_Teams.addAction(self.t11)
        self.menuManage_Teams.addAction(self.t12)
        self.menuManage_Teams.addAction(self.t13)
        self.menubar.addAction(self.menuManage_Players.menuAction())
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(SecondPage)
        QtCore.QMetaObject.connectSlotsByName(SecondPage)

    def retranslateUi(self, SecondPage):
        _translate = QtCore.QCoreApplication.translate
        SecondPage.setWindowTitle(_translate("SecondPage", "MainWindow"))
        self.b1.setText(_translate("SecondPage", "Batsman"))
        self.b2.setText(_translate("SecondPage", "Bowler"))
        self.b3.setText(_translate("SecondPage", "Wiket-Keeper"))
        self.b4.setText(_translate("SecondPage", "All-rounder"))
        self.menuManage_Players.setTitle(_translate("SecondPage", "Manage Players"))
        self.menuManage_Teams.setTitle(_translate("SecondPage", "Manage Teams"))
        self.p1.setText(_translate("SecondPage", "Add "))
        self.p2.setText(_translate("SecondPage", "Find"))
        self.a3.setText(_translate("SecondPage", "Remove"))
        self.tm1.setText(_translate("SecondPage", "New Team"))
        self.tm2.setText(_translate("SecondPage", "OpenTeam"))
        self.tm3.setText(_translate("SecondPage", "Evaluate Team"))
        self.p3.setText(_translate("SecondPage", "Remove"))
        self.p11.setText(_translate("SecondPage", "Add Player"))
        self.p11.setShortcut(_translate("SecondPage", "Ctrl+N"))
        self.p12.setText(_translate("SecondPage", "Find Player"))
        self.p12.setShortcut(_translate("SecondPage", "Ctrl+F"))
        self.p13.setText(_translate("SecondPage", "Delete Player"))
        self.p13.setShortcut(_translate("SecondPage", "Ctrl+D"))
        self.t11.setText(_translate("SecondPage", "New Team"))
        self.t11.setShortcut(_translate("SecondPage", "Ctrl+T"))
        self.t12.setText(_translate("SecondPage", "Open Team"))
        self.t12.setShortcut(_translate("SecondPage", "Ctrl+O"))
        self.t13.setText(_translate("SecondPage", "Evaluate Team"))
        self.t13.setShortcut(_translate("SecondPage", "Ctrl+E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondPage = QtWidgets.QMainWindow()
    ui = Ui_SecondPage()
    ui.setupUi(SecondPage)
    SecondPage.show()
    sys.exit(app.exec_())

