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
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(566, 399)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget_fruit = QListWidget(self.centralwidget)
        self.listWidget_fruit.setObjectName(u"listWidget_fruit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_fruit.sizePolicy().hasHeightForWidth())
        self.listWidget_fruit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.listWidget_fruit, 3, 2, 1, 2)

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


        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.label_Vegetables = QLabel(self.centralwidget)
        self.label_Vegetables.setObjectName(u"label_Vegetables")
        font = QFont()
        font.setFamilies([u"Trebuchet MS"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.label_Vegetables.setFont(font)

        self.gridLayout.addWidget(self.label_Vegetables, 2, 4, 1, 1)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit, 0, 0, 1, 1)

        self.listWidget_protein = QListWidget(self.centralwidget)
        self.listWidget_protein.setObjectName(u"listWidget_protein")

        self.gridLayout.addWidget(self.listWidget_protein, 3, 0, 1, 2)

        self.label_Protein = QLabel(self.centralwidget)
        self.label_Protein.setObjectName(u"label_Protein")
        self.label_Protein.setFont(font)

        self.gridLayout.addWidget(self.label_Protein, 2, 0, 1, 1)

        self.label_fruit = QLabel(self.centralwidget)
        self.label_fruit.setObjectName(u"label_fruit")
        self.label_fruit.setFont(font)

        self.gridLayout.addWidget(self.label_fruit, 2, 2, 1, 1)

        self.label_num_cal = QLabel(self.centralwidget)
        self.label_num_cal.setObjectName(u"label_num_cal")
        font1 = QFont()
        font1.setFamilies([u"Trebuchet MS"])
        font1.setPointSize(11)
        self.label_num_cal.setFont(font1)

        self.gridLayout.addWidget(self.label_num_cal, 5, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 6, 0, 1, 2)

        self.listWidget_vegetables = QListWidget(self.centralwidget)
        self.listWidget_vegetables.setObjectName(u"listWidget_vegetables")

        self.gridLayout.addWidget(self.listWidget_vegetables, 3, 4, 1, 2)

        self.label_daily_goal_title = QLabel(self.centralwidget)
        self.label_daily_goal_title.setObjectName(u"label_daily_goal_title")
        font2 = QFont()
        font2.setFamilies([u"Trebuchet MS"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_daily_goal_title.setFont(font2)

        self.gridLayout.addWidget(self.label_daily_goal_title, 4, 0, 1, 1)

        self.label_app_title = QLabel(self.centralwidget)
        self.label_app_title.setObjectName(u"label_app_title")
        font3 = QFont()
        font3.setFamilies([u"Trebuchet MS"])
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setUnderline(True)
        self.label_app_title.setFont(font3)

        self.gridLayout.addWidget(self.label_app_title, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.listWidget_protein.raise_()
        self.listWidget_fruit.raise_()
        self.listWidget_vegetables.raise_()
        self.progressBar.raise_()
        self.label_fruit.raise_()
        self.label_Vegetables.raise_()
        self.dateEdit.raise_()
        self.label_Protein.raise_()
        self.label_num_cal.raise_()
        self.label_daily_goal_title.raise_()
        self.label_app_title.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 566, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_ok.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_Vegetables.setText(QCoreApplication.translate("MainWindow", u"Vegetables:", None))
        self.label_Protein.setText(QCoreApplication.translate("MainWindow", u"Protein:", None))
        self.label_fruit.setText(QCoreApplication.translate("MainWindow", u"Fruit:", None))
        self.label_num_cal.setText(QCoreApplication.translate("MainWindow", u"2,000", None))
        self.label_daily_goal_title.setText(QCoreApplication.translate("MainWindow", u"Daily Goal: 2,000 Cal", None))
        self.label_app_title.setText(QCoreApplication.translate("MainWindow", u"My Fitness", None))
    # retranslateUi

