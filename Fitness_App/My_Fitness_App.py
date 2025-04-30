import sys
import json
import os
import pandas as pd

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QCheckBox, 
    QListWidgetItem,
    QMessageBox,
)
from gen.main_ui import Ui_MainWindow

foods= "Fitness_App/helpers/foods.json"
daily_goal= 2000
cal_buffer = 0
selected_foods = []

class My_APP (Ui_MainWindow, QMainWindow):

    def __init__(self):
        super().__init__()
        global foods

        self.setupUi(self)
        self.w = None

        if os.path.exists(foods):
            with open (foods, "r") as file:
                foods = json.load(file)

        else:
            print("File does not exist. Nothing to load")
            foods= None
            return

        self.generate_checkboxes()
        self.pushButton_ok.clicked.connect(lambda: self.total_value_cal())
        self.progressBar.setRange(0, 2000)
        self.progressBar.setValue(0)
        self.pushButton_cancel.clicked.connect(lambda: self.canceled()) 
 
    def food_selected(self, checkbox):
        print(checkbox.text())

    def canceled(self):
        global daily_goal
        self.progressBar.reset()
        self.label_num_cal.setText(str(daily_goal))
        self.uncheck()

    def generate_checkboxes(self):
        for food in foods:
            checkbox = CustomCheckBox(food)
            item = QListWidgetItem()
            type = foods[food]["type"]
            if type == "Fruit":
                self.listWidget_fruit.addItem(item) 
                self.listWidget_fruit.setItemWidget(item, checkbox) 
            elif type =="Protein":
                self.listWidget_protein.addItem(item)
                self.listWidget_protein.setItemWidget(item, checkbox)
            elif type== "Vegetables":
                self.listWidget_vegetables.addItem(item)
                self.listWidget_vegetables.setItemWidget(item, checkbox)

    def total_value_cal(self):
        global cal_buffer
        global daily_goal

        remaining_calories= daily_goal- self.progressBar.value()
        total_cal= remaining_calories - cal_buffer
        if total_cal < 0:
            print("You have exceeded your daily goal!")
            ret = self.warning_box()
            total_cal= str(total_cal) + " over."
            if not ret:
                return
        else:
            print("You have these many calories left: " + str(total_cal) + "\nYour current Calories: " + str(cal_buffer))
            total_cal= str(total_cal) + " left."

        self.label_num_cal.setText(str(total_cal))
        self.update_progress_bar(cal_buffer)
        self.save_data()
        self.uncheck()

    def uncheck(self):
        global selected_foods
        list_copy = selected_foods.copy()
        for item in list_copy:
            item.click()

    def save_data(self):
        data = {
            "Name": [],
            "Calories": [],
            "Type": [] 
        }

        global selected_foods
        for item in selected_foods:
            name= item.text()
            calories= foods[name]['calories']
            type= foods[name]['type']
            data['Name'].append(name)
            data['Calories'].append(calories)
            data['Type'].append(type)

        Date= self.dateEdit.date()
        date= Date.toString()
        date = date.replace(" ", "_")
        date += ".csv"
        df= pd.DataFrame(data)
        output_path= os.path.join('Fitness_App', 'output', date)
        if os.path.exists(output_path):
            df.to_csv(output_path, mode='a', index=False, header=False)
        else:
            df.to_csv(output_path, index=False)


    def update_progress_bar(self, new_cals):
        current = self.progressBar.value()
        new_total = current + new_cals
        self.progressBar.setValue(new_total)
        if new_total> daily_goal:
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
            return True
        elif cal_warning == QMessageBox.StandardButton.No:
            return False

class CustomCheckBox(QCheckBox):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.stateChanged.connect(self.update_calories)

    def update_calories(self):
        global cal_buffer
        global selected_foods
        if self.isChecked():
            cal_buffer += foods[self.text()]["calories"]
            selected_foods.append(self)
        else:
            cal_buffer -= foods[self.text()]["calories"]
            selected_foods.remove(self)



app= QApplication(sys.argv)
window= My_APP()
window.show()
app.exec()