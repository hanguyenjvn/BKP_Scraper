# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(413, 230)
        self.timer=QtCore.QTimer()
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.cB_province = QtGui.QComboBox(self.centralwidget)
        self.cB_province.setGeometry(QtCore.QRect(10, 120, 201, 22))
        self.cB_province.setObjectName(_fromUtf8("cB_province"))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_province.addItem(_fromUtf8(""))
        self.cB_month = QtGui.QComboBox(self.centralwidget)
        self.cB_month.setGeometry(QtCore.QRect(230, 120, 69, 22))
        self.cB_month.setObjectName(_fromUtf8("cB_month"))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_month.addItem(_fromUtf8(""))
        self.cB_year = QtGui.QComboBox(self.centralwidget)
        self.cB_year.setGeometry(QtCore.QRect(320, 120, 69, 22))
        self.cB_year.setObjectName(_fromUtf8("cB_year"))
        self.cB_year.addItem(_fromUtf8(""))
        self.cB_year.addItem(_fromUtf8(""))
        self.cB_year.addItem(_fromUtf8(""))
        self.cB_year.addItem(_fromUtf8(""))
        self.cB_year.addItem(_fromUtf8(""))
        self.cB_year.addItem(_fromUtf8(""))
        self.cB_year.addItem(_fromUtf8(""))
        self.cB_year.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 51, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 90, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 90, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pB_ok = QtGui.QPushButton(self.centralwidget)
        self.pB_ok.setGeometry(QtCore.QRect(230, 170, 75, 23))
        self.pB_ok.setObjectName(_fromUtf8("pB_ok"))
        self.pB_close = QtGui.QPushButton(self.centralwidget)
        self.pB_close.setGeometry(QtCore.QRect(320, 170, 75, 23))
        self.pB_close.setObjectName(_fromUtf8("pB_close"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 161, 51))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("tp7.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 10, 101, 81))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("wfp.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, -10, 91, 91))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("jvn.png")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BKP Scraper", None))
        self.cB_province.setItemText(0, _translate("MainWindow", "All", None))
        self.cB_province.setItemText(1, _translate("MainWindow", "Aceh", None))
        self.cB_province.setItemText(2, _translate("MainWindow", "Bali", None))
        self.cB_province.setItemText(3, _translate("MainWindow", "Banten", None))
        self.cB_province.setItemText(4, _translate("MainWindow", "Bengkulu ", None))
        self.cB_province.setItemText(5, _translate("MainWindow", "D I Yogyakarta ", None))
        self.cB_province.setItemText(6, _translate("MainWindow", "DKI Jakarta", None))
        self.cB_province.setItemText(7, _translate("MainWindow", "Gorontalo ", None))
        self.cB_province.setItemText(8, _translate("MainWindow", "Jambi ", None))
        self.cB_province.setItemText(9, _translate("MainWindow", "Jawa Barat", None))
        self.cB_province.setItemText(10, _translate("MainWindow", "Jawa Tengah ", None))
        self.cB_province.setItemText(11, _translate("MainWindow", "Jawa Timur ", None))
        self.cB_province.setItemText(12, _translate("MainWindow", "Kalimantan Barat ", None))
        self.cB_province.setItemText(13, _translate("MainWindow", "Kalimantan Selatan ", None))
        self.cB_province.setItemText(14, _translate("MainWindow", "Kalimantan Tengah ", None))
        self.cB_province.setItemText(15, _translate("MainWindow", "Kalimantan Timur ", None))
        self.cB_province.setItemText(16, _translate("MainWindow", "Kalimantan Utara", None))
        self.cB_province.setItemText(17, _translate("MainWindow", "Kepulauan Babel", None))
        self.cB_province.setItemText(18, _translate("MainWindow", "Kepulauan Riau", None))
        self.cB_province.setItemText(19, _translate("MainWindow", "Lampung ", None))
        self.cB_province.setItemText(20, _translate("MainWindow", "Maluku", None))
        self.cB_province.setItemText(21, _translate("MainWindow", "Maluku Utara", None))
        self.cB_province.setItemText(22, _translate("MainWindow", "Nusa Tenggara Barat ", None))
        self.cB_province.setItemText(23, _translate("MainWindow", "Nusa Tenggara Timur ", None))
        self.cB_province.setItemText(24, _translate("MainWindow", "Papua", None))
        self.cB_province.setItemText(25, _translate("MainWindow", "Papua Barat", None))
        self.cB_province.setItemText(26, _translate("MainWindow", "Riau", None))
        self.cB_province.setItemText(27, _translate("MainWindow", "Sulawesi Barat ", None))
        self.cB_province.setItemText(28, _translate("MainWindow", "Sulawesi Selatan ", None))
        self.cB_province.setItemText(29, _translate("MainWindow", "Sulawesi Tengah ", None))
        self.cB_province.setItemText(30, _translate("MainWindow", "Sulawesi Tenggara ", None))
        self.cB_province.setItemText(31, _translate("MainWindow", "Sulawesi Utara ", None))
        self.cB_province.setItemText(32, _translate("MainWindow", "Sumatera Barat", None))
        self.cB_province.setItemText(33, _translate("MainWindow", "Sumatera Selatan", None))
        self.cB_province.setItemText(34, _translate("MainWindow", "Sumatera Utara", None))
        self.cB_month.setItemText(0, _translate("MainWindow", "01", None))
        self.cB_month.setItemText(1, _translate("MainWindow", "02", None))
        self.cB_month.setItemText(2, _translate("MainWindow", "03", None))
        self.cB_month.setItemText(3, _translate("MainWindow", "04", None))
        self.cB_month.setItemText(4, _translate("MainWindow", "05", None))
        self.cB_month.setItemText(5, _translate("MainWindow", "06", None))
        self.cB_month.setItemText(6, _translate("MainWindow", "07", None))
        self.cB_month.setItemText(7, _translate("MainWindow", "08", None))
        self.cB_month.setItemText(8, _translate("MainWindow", "09", None))
        self.cB_month.setItemText(9, _translate("MainWindow", "10", None))
        self.cB_month.setItemText(10, _translate("MainWindow", "11", None))
        self.cB_month.setItemText(11, _translate("MainWindow", "12", None))
        self.cB_year.setItemText(0, _translate("MainWindow", "2010", None))
        self.cB_year.setItemText(1, _translate("MainWindow", "2011", None))
        self.cB_year.setItemText(2, _translate("MainWindow", "2012", None))
        self.cB_year.setItemText(3, _translate("MainWindow", "2013", None))
        self.cB_year.setItemText(4, _translate("MainWindow", "2014", None))
        self.cB_year.setItemText(5, _translate("MainWindow", "2015", None))
        self.cB_year.setItemText(6, _translate("MainWindow", "2016", None))
        self.cB_year.setItemText(7, _translate("MainWindow", "2017", None))
        self.label.setText(_translate("MainWindow", "Province", None))
        self.label_2.setText(_translate("MainWindow", "Month", None))
        self.label_3.setText(_translate("MainWindow", "Year", None))
        self.pB_ok.setText(_translate("MainWindow", "OK", None))
        self.pB_close.setText(_translate("MainWindow", "Close", None))

