import Gui
import CSVHandler

class SystemHandling():
    
    gui_display = Gui.GuiDisplay()
    gui_input = Gui.GuiInputHandling()
    csv_handler = None
    options = ['1. List Employee Info', '2. Add New Employee', '3. Update Employee Information', '4. Remove Employees', '5. Exit']
    file_name = 'employees'
    
    def systemNavigation(self):
        self.csv_handler = CSVHandler.csvHandling(self.file_name)
        valid_input = 'false'
        while valid_input == 'false':
            self.gui_display.list_options(self.options)
            choice = self.gui_input.take_input("int5")
            match choice:
                case '1':
                    self.gui_display.printALine('id, first_name, last_name,date_of_employment, salery, department')
                    self.csv_handler.readFile(self.file_name)
                case '2':
                    employee = self.gui_input.create_employee()
                    self.csv_handler.addEmployee(employee)
                case '3':
                    self.gui_display.printALine('Select employee id to update')
                    id = self.gui_input.take_input('int')
                    employee_update = self.csv_handler.getEmployee(id)
                    new_employee = self.gui_input.update_employee(employee_update)
                    self.csv_handler.updateEmployee(id, new_employee)
                case '4':
                    id = self.gui_input.remove_employee()
                    self.csv_handler.removeEmployee(id)
                case '5':
                    valid_input = 'true'
                    return
                case _:
                    print('input invalid, try again')
            
        
        
        
        