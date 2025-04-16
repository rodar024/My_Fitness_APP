import sys
# import math

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QCheckBox
from main_ui import Ui_MainWindow
from food_list import foods

daily_goal= 2000
cal_buffer = 0

class My_APP (Ui_MainWindow, QMainWindow):
    #daily_goal= 2000

    def __init__(self):
        super().__init__()
        self.current_cals = 0

        self.setupUi(self)

        self.generate_checkboxes()
        self.pushButton_2.clicked.connect(lambda: self.total_value())
        self.progressBar.setRange(0, 2000)
        self.progressBar.setValue(0)
        self.pushButton.clicked.connect(lambda: self.canceled())


# When wanting to add differnt foods in the app. Go inside the food_list and add teh calories the
# type and the name. 

    def generate_checkboxes(self):
        for food in foods:
            checkbox = CustomCheckBox(food)
            type = foods[food]["type"]
            if type == "Protein":
                self.verticalLayout.addWidget(checkbox)
            elif type =="Fruit":
                self.verticalLayout_2.addWidget(checkbox)
            elif type== "Vegetables":
                self.verticalLayout_3.addWidget(checkbox)
   

    #calculating the calories left and seeing if it over exceeds the goal

    def total_value(self):
        global cal_buffer
        global daily_goal
        total_cal= daily_goal - cal_buffer
        if total_cal < 0:
            print("You have exceeded your daily goal!")
        else:
            print("You have these many calories left: " + str(total_cal))
        self.current_cals +=cal_buffer
        self.update_progress_bar()
    
    def update_progress_bar(self):
        self.progressBar.setValue(self.current_cals)

    def canceled(self):
        print ("You have canceled.")

class CustomCheckBox(QCheckBox):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        global cal_buffer
        if not self.isChecked():
            cal_buffer += foods[self.text()]["calories"]
        else:
            cal_buffer -= foods[self.text()]["calories"]
        print(str(cal_buffer))


app= QApplication(sys.argv)
window= My_APP()
window.show()

# test = Fruit("Apple", 100)
# print(test.name + " has " + str(test.calories) + " calories and is a " + test.type)
app.exec()