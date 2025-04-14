# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QHBoxLayout,
    QLabel, QListView, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(270, 40, 161, 41))
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(40, 100, 110, 22))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(560, 90, 121, 61))
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(40, 180, 181, 251))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 190, 49, 16))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 220, 161, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout.addWidget(self.checkBox_5)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout.addWidget(self.checkBox_4)

        self.listView_2 = QListView(self.centralwidget)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(260, 180, 181, 251))
        self.listView_3 = QListView(self.centralwidget)
        self.listView_3.setObjectName(u"listView_3")
        self.listView_3.setGeometry(QRect(480, 180, 181, 251))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 190, 49, 16))
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(270, 220, 161, 201))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout_2.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout_2.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.verticalLayout_2.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.verticalLayout_2.addWidget(self.checkBox_10)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(490, 220, 161, 201))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox_11 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.verticalLayout_3.addWidget(self.checkBox_11)

        self.checkBox_12 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.verticalLayout_3.addWidget(self.checkBox_12)

        self.checkBox_13 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.verticalLayout_3.addWidget(self.checkBox_13)

        self.checkBox_14 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.verticalLayout_3.addWidget(self.checkBox_14)

        self.checkBox_15 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.verticalLayout_3.addWidget(self.checkBox_15)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(490, 190, 71, 16))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(240, 470, 224, 81))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 500, 118, 23))
        self.progressBar.setValue(24)
        MainWindow.setCentralWidget(self.centralwidget)
        self.listView.raise_()
        self.listView_2.raise_()
        self.textEdit.raise_()
        self.dateEdit.raise_()
        self.textEdit_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.listView_3.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.horizontalLayoutWidget.raise_()
        self.progressBar.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; text-decoration: underline;\">   My Fitness   </span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Daily Goal:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">2,000</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Protein:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Chicken", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Pork", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Salmon", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Eggs", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Greek Yogurt", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Fruit:", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Apple", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Strawberries", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Pineapple", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Banana", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Avocado", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"Carrot", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"Spinach", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"Lettuce", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"Kale", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"Tumeric", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vegetables:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

