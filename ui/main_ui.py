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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLabel, QListView, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 364)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamilies([u"Trebuchet MS"])
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        self.label_title.setFont(font)

        self.gridLayout.addWidget(self.label_title, 0, 2, 1, 1)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit, 0, 0, 1, 1)

        self.listView_vegetables = QListView(self.centralwidget)
        self.listView_vegetables.setObjectName(u"listView_vegetables")

        self.gridLayout.addWidget(self.listView_vegetables, 3, 4, 1, 2)

        self.label_daily_goal_title = QLabel(self.centralwidget)
        self.label_daily_goal_title.setObjectName(u"label_daily_goal_title")
        font1 = QFont()
        font1.setFamilies([u"Trebuchet MS"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_daily_goal_title.setFont(font1)

        self.gridLayout.addWidget(self.label_daily_goal_title, 0, 4, 1, 1)

        self.label_fruit = QLabel(self.centralwidget)
        self.label_fruit.setObjectName(u"label_fruit")
        font2 = QFont()
        font2.setFamilies([u"Trebuchet MS"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_fruit.setFont(font2)

        self.gridLayout.addWidget(self.label_fruit, 2, 2, 1, 1)

        self.listView_protein = QListView(self.centralwidget)
        self.listView_protein.setObjectName(u"listView_protein")

        self.gridLayout.addWidget(self.listView_protein, 3, 0, 1, 2)

        self.label_Protein = QLabel(self.centralwidget)
        self.label_Protein.setObjectName(u"label_Protein")
        self.label_Protein.setFont(font2)

        self.gridLayout.addWidget(self.label_Protein, 2, 0, 1, 1)

        self.label_num_cal = QLabel(self.centralwidget)
        self.label_num_cal.setObjectName(u"label_num_cal")
        font3 = QFont()
        font3.setFamilies([u"Trebuchet MS"])
        font3.setPointSize(11)
        self.label_num_cal.setFont(font3)

        self.gridLayout.addWidget(self.label_num_cal, 0, 5, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 2)

        self.label_Vegetables = QLabel(self.centralwidget)
        self.label_Vegetables.setObjectName(u"label_Vegetables")
        self.label_Vegetables.setFont(font2)

        self.gridLayout.addWidget(self.label_Vegetables, 2, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_ok = QPushButton(self.centralwidget)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_3.addWidget(self.pushButton_ok)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_cancel = QPushButton(self.centralwidget)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_3.addWidget(self.pushButton_cancel)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 2, 1, 2)

        self.listView_fruit = QListView(self.centralwidget)
        self.listView_fruit.setObjectName(u"listView_fruit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_fruit.sizePolicy().hasHeightForWidth())
        self.listView_fruit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.listView_fruit, 3, 2, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.listView_protein.raise_()
        self.listView_fruit.raise_()
        self.listView_vegetables.raise_()
        self.progressBar.raise_()
        self.label_fruit.raise_()
        self.label_Vegetables.raise_()
        self.dateEdit.raise_()
        self.label_daily_goal_title.raise_()
        self.label_num_cal.raise_()
        self.label_title.raise_()
        self.label_Protein.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 520, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"My Fitness", None))
        self.label_daily_goal_title.setText(QCoreApplication.translate("MainWindow", u"Daily Goal:", None))
        self.label_fruit.setText(QCoreApplication.translate("MainWindow", u"Fruit:", None))
        self.label_Protein.setText(QCoreApplication.translate("MainWindow", u"Protein:", None))
        self.label_num_cal.setText(QCoreApplication.translate("MainWindow", u"2,000", None))
        self.label_Vegetables.setText(QCoreApplication.translate("MainWindow", u"Vegetables:", None))
        self.pushButton_ok.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

