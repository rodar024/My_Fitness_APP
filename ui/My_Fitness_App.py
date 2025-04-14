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

        self.setupUi(self)

        self.generate_checkboxes()
    
        self.checkBox.clicked.connect(lambda: self.protein()) #Chicken, used to see if the if statement works
        self.checkBox_6.clicked.connect(lambda: self.fruit())

        self.pushButton_2.clicked.connect(lambda: self.amount_needed())

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

    def print_test(self, food_name):
        # for food in foods:
         #   print( food + " is " + str(foods[food]["calories"]))
         print (food_name)

    def protein (self):
        if self.checkBox.isChecked():
            chicken=284
            print(chicken)
            return chicken 
    
    def fruit (self):
        if self.checkBox_6.isChecked():
            Apple=95
            print(Apple)
            return Apple

    def sum_calories (self):
        total_cal= self.protein + self.fruit
        return total_cal

    def amount_needed(self):
        amount_left = daily_goal - self.sum_calories
        print ("You have this amount left:"+ amount_left)
        return amount_left


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
        
        
# Trying to Use classes instead of hardcoding. 
    
class Food ():
    def __init__(self, name, calories):

        self.name= name
        self.calories= calories

class Protein(Food):
    def __init__(self, name, calories):
        super().__init__(name, calories)

        self.type = "Protein"

class Fruit(Food):
    def __init__(self, name, calories):
        super().__init__(name, calories)

        self.type= "Fruit"

class Vegetables(Food):
    def __init__(self, name, calories):
        super().__init__(name, calories)

        self.type = "Vegetable"


app= QApplication(sys.argv)
window= My_APP()
window.show()

# test = Fruit("Apple", 100)
# print(test.name + " has " + str(test.calories) + " calories and is a " + test.type)
app.exec()