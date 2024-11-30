import sys
from copy import deepcopy

# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPen, QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 51, 31))
        self.label.setObjectName("label")
        self.LE_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_1.setGeometry(QtCore.QRect(70, 20, 100, 20))
        self.LE_1.setObjectName("LE_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 51, 31))
        self.label_2.setObjectName("label_2")
        self.LE_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_2.setGeometry(QtCore.QRect(250, 20, 100, 20))
        self.LE_2.setObjectName("LE_2")
        self.B = QtWidgets.QPushButton(self.centralwidget)
        self.B.setGeometry(QtCore.QRect(380, 20, 75, 23))
        self.B.setObjectName("B")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "K = "))
        self.label_2.setText(_translate("MainWindow", "N = "))
        self.B.setText(_translate("MainWindow", "Рисовать"))

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.do_paint = False

        self.coords = [(100, 100), (400, 100), (400, 400), (100, 400)]

        self.B.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_square(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.coords = [(100, 100), (400, 100), (400, 400), (100, 400)]

        self.K, self.N = float(self.LE_1.text()), int(self.LE_2.text())
        self.repaint()

    def draw_square(self, qp):
        self.do_paint = False
        for i in range(self.N):
            new_coords = []
            for j in range(4):
                new_coords.append((int(self.coords[j][0] + (1 - self.K) * (
                        self.coords[(j + 1) % 4][0] - self.coords[j][0])),
                                   int(self.coords[j][1] + (1 - self.K) * (
                                           self.coords[(j + 1) % 4][1] -
                                           self.coords[j][1]))))

            for x in range(4):
                point_1, point_2 = self.coords[x], self.coords[(x + 1) % 4]

                qp.setPen(QColor(255, 0, 0))

                qp.drawLine(point_1[0], point_1[1], point_2[0], point_2[1])
            self.coords = deepcopy(new_coords)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec())