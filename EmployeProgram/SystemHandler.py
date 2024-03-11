import Gui
import CSVHandler

class SystemHandling():
    
    gui_display = Gui.GuiDisplay()
    gui_input = Gui.GuiInputHandling()
    csv_handler = CSVHandler.csvHandling()
    options = ['1. List Employee Info', '2. Add New Employee', '3. Update Employee Information', '4. Remove Employees', '5. Exit']
    
    def systemNavigation(self):
        self.csv_handler.createFile('employees')
        self.gui_display.list_options(self.options)
        choice = self.gui_input.take_input("int5")
        
        
        