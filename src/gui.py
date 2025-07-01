from PyQt6 import QtCore, QtGui, QtWidgets
import algo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 358)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.inpBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.inpBox.setGeometry(QtCore.QRect(40, 70, 621, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inpBox.setFont(font)
        self.inpBox.setObjectName("inpBox")
        self.in_str = QtWidgets.QLineEdit(parent=self.inpBox)
        self.in_str.setGeometry(QtCore.QRect(10, 20, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.in_str.setFont(font)
        self.in_str.setText("")
        self.in_str.setObjectName("in_str")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.inpBox)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.oke_bt = QtWidgets.QPushButton(parent=self.inpBox)
        self.oke_bt.setGeometry(QtCore.QRect(510, 20, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.oke_bt.setFont(font)
        self.oke_bt.setObjectName("oke_bt")
        self.random_bt = QtWidgets.QPushButton(parent=self.inpBox)
        self.random_bt.setGeometry(QtCore.QRect(510, 50, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.random_bt.setFont(font)
        self.random_bt.setObjectName("random_bt")
        self.oupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.oupBox.setGeometry(QtCore.QRect(40, 170, 621, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.oupBox.setFont(font)
        self.oupBox.setObjectName("oupBox")
        self.out_str = QtWidgets.QPlainTextEdit(parent=self.oupBox)
        self.out_str.setGeometry(QtCore.QRect(10, 20, 601, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.out_str.setFont(font)
        self.out_str.setPlainText("")
        self.out_str.setObjectName("out_str")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connect buttons to functions    
        self.oke_bt.clicked.connect(self.oke_bt_clicked)
        self.random_bt.clicked.connect(self.random_bt_clicked)
        
        #enter key
        self.in_str.returnPressed.connect(self.oke_bt_clicked)

    current_graph = None
    def oke_bt_clicked(self):
        #close previous graph if existed
        if self.current_graph:
            self.current_graph.close()

        #get input
        s = self.in_str.text()

        #check if input is valid
        for i in range(len(s)):
            if s[i] not in ['_', '\\', '/', ' ']:
                self.out_str.setPlainText('Invalid input!')
                return   
                 
        #clear output
        self.out_str.setPlainText('')

        #run algorithms & plot graph
        self.current_graph = algo.main(s) 

        #output
        self.out_str.setPlainText(algo.output_str())

    def random_bt_clicked(self):
        #close previous graph if existed
        if self.current_graph:
            self.current_graph.close()

        #get random input
        s = algo.auto_input()
        self.in_str.setText(s)

        #clear output
        self.out_str.setPlainText('')

        #run algorithms & plot graph
        self.current_graph = algo.main(s)   
           
        #output
        self.out_str.setPlainText(algo.output_str())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Floodwater Calculation App"))
        self.inpBox.setTitle(_translate("MainWindow", "Input"))
        self.pushButton_2.setText(_translate("MainWindow", "OK"))
        self.oke_bt.setText(_translate("MainWindow", "OK"))
        self.random_bt.setText(_translate("MainWindow", "Go random!"))
        self.oupBox.setTitle(_translate("MainWindow", "Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

#testcase
# //\//\_\_/_///_\\__/\_\\_/_\\/\//\
# /\\///\/\\\\\/\\///////\\/\//\//
# //\\/\/\\/\\\//\/////\/\//\\\/\/\\\\////\/\
# \\\\/\/\\\////\\/\/\///\\/\\
# ///\//_\\\\\//_////\/\/\\///\///\\\/\/\\
