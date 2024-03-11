class GuiDisplay:
    
    def list_options(self, choices):
        print(*choices, sep = "\n")
    def printALine(line):
        print(line)

class GuiInputHandling:
    
    def take_input(self, input_type):
        choice = input()
        return choice
    def create_employee(self):
        employee = list()
        GuiDisplay.printALine('Input first name:')
        first_name = self.take_input("string")
        GuiDisplay.printALine('Input last name:')
        last_name = self.take_input("string")
        GuiDisplay.printALine('Input date of employment:')
        date_of_employment = self.take_input("date")
        GuiDisplay.printALine('Input salery:')
        salery = self.take_input("money")
        GuiDisplay.printALine('Input department:')
        department = self.take_input("string")
        employee.append(first_name)
        employee.append(last_name)
        employee.append(date_of_employment)
        employee.append(salery)
        employee.append(department)
        return employee
    def remove_employee(self):
        GuiDisplay.printALine('Input id to be deleted:')
        id = self.take_input("int")
        return id
        
        