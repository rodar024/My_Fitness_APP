import sys
import json

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QCheckBox, 
    QListWidgetItem,
    QMessageBox
)
from main_ui import Ui_MainWindow

with open ("foods.json", "r") as file:
    foods= json.load(file)
#need to then create another file for foods. 

daily_goal= 2000
cal_buffer = 0

class My_APP (Ui_MainWindow, QMainWindow):

    def __init__(self):
        super().__init__()
        self.current_cals = 0

        self.setupUi(self)
        self.w = None

        self.generate_checkboxes()
        self.pushButton_ok.clicked.connect(lambda: self.total_value_cal())
        self.progressBar.setRange(0, 2000)
        self.progressBar.setValue(0)
        self.pushButton_cancel.clicked.connect(lambda: self.canceled())


# When wanting to add differnt foods in the app. Go inside the food_list and add teh calories the
# type and the name. 

        
    def generate_checkboxes(self):
        for food in foods:
            checkbox = CustomCheckBox(food)
            item = QListWidgetItem()
            type = foods[food]["type"]
            if type == "Fruit":
                self.listWidget_fruit.addItem(item) #missing something
                self.listWidget_fruit.setItemWidget(item, checkbox) 
                #originally had: self.listWidget_fruit.addWidget(checkbox)
            elif type =="Protein":
                self.listWidget_protein.addItem(item)
                self.listWidget_protein.setItemWidget(item, checkbox)
            elif type== "Vegetables":
                self.listWidget_vegetables.addItem(item)
                self.listWidget_vegetables.setItemWidget(item, checkbox)
   

    #calculating the calories left and seeing if it over exceeds the goal

    def total_value_cal(self):
        global cal_buffer
        global daily_goal

        total_cal= daily_goal - cal_buffer
        if total_cal < 0:
            print("You have exceeded your daily goal!")
            ret = self.warning_box()
            if not ret:
                return
        else:
            print("You have these many calories left: " + str(total_cal) + "\nYour current Calories: " + str(cal_buffer))
        
        self.current_cals= 0
        self.current_cals +=cal_buffer
        self.label_num_cal.setText(str(total_cal))
        self.update_progress_bar()
    
    def update_progress_bar(self): 
        self.progressBar.setValue(self.current_cals)
        if self.current_cals> daily_goal:
            self.progressBar.setValue(2000)
    
    def warning_box(self):
        cal_warning= QMessageBox.warning(
            self,
            "Warning",
            "You are about to exceed daily goal. Do you want to continue?",
            buttons =QMessageBox.StandardButton.Yes,
            defaultButton= QMessageBox.StandardButton.No,
        )
        if cal_warning == QMessageBox.StandardButton.Yes:
            self.update_progress_bar()
            return True
        elif cal_warning == QMessageBox.StandardButton.No:
            return False

class CustomCheckBox(QCheckBox):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.stateChanged.connect(self.update_calories)

    def update_calories(self):
        global cal_buffer
        if self.isChecked():
            cal_buffer += foods[self.text()]["calories"]
        else:
            cal_buffer -= foods[self.text()]["calories"]
        print(str(cal_buffer))


app= QApplication(sys.argv)
window= My_APP()
window.show()
app.exec()