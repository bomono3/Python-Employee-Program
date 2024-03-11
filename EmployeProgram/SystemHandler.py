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
        self.gui_display.list_options(self.options)
        choice = self.gui_input.take_input("int5")
        valid_input = 'false'
        while valid_input == 'false':
            match choice:
                case '1':
                    self.csv_handler.readFile(self.file_name)
                    valid_input = 'true'
                case '2':
                    employee = self.gui_input.create_employee()
                    self.csv_handler.AddEmployee(employee)
                    valid_input = 'true'
                case '3':
                    print('case 3')
                    valid_input = 'true'
                case '4':
                    id = self.gui_input.remove_employee()
                    self.csv_handler.removeEmployee(id)
                    valid_input = 'true'
                case '5':
                    valid_input = 'true'
                    return
                case _:
                    print('input invalid, try again')
            
        
        
        
        