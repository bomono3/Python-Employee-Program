class GuiDisplay:
    
    def list_options(self, choices):
        print(*choices, sep = "\n")
    def printALine(self, line):
        print(line)

class GuiInputHandling:
    
    def take_input(self, input_type):
        choice = input()
        
        return choice
    def create_employee(self):
        employee = list()
        GuiDisplay.printALine(GuiDisplay, 'Input first name:')
        first_name = self.take_input("string")
        GuiDisplay.printALine(GuiDisplay, 'Input last name:')
        last_name = self.take_input("string")
        GuiDisplay.printALine(GuiDisplay, 'Input date of employment:')
        date_of_employment = self.take_input("date")
        GuiDisplay.printALine(GuiDisplay, 'Input salery:')
        salery = self.take_input("money")
        GuiDisplay.printALine(GuiDisplay, 'Input department:')
        department = self.take_input("string")
        employee.append(first_name)
        employee.append(last_name)
        employee.append(date_of_employment)
        employee.append(salery)
        employee.append(department)
        return employee
    def remove_employee(self):
        GuiDisplay.printALine(GuiDisplay, 'Input id to be deleted:')
        id = self.take_input("int")
        return id
    def update_employee(self, employee):
        GuiDisplay.printALine(GuiDisplay, 'which field would you like to change?')
        options = ['1. First name', '2. Last name', '3. date of employment', '4. Salery', '5. Department']
        GuiDisplay.list_options(GuiDisplay, options)
        choice = self.take_input("int5")
        match choice:
                case '1':
                    GuiDisplay.printALine(GuiDisplay, 'Input new first name:')
                    first_name = self.take_input("string")
                    employee.pop(1)
                    employee.insert(1, first_name)
                case '2':
                    GuiDisplay.printALine(GuiDisplay, 'Input new last name:')
                    last_name = self.take_input("string")
                    employee.pop(2)
                    employee.insert(2, last_name)
                case '3':
                    GuiDisplay.printALine(GuiDisplay, 'Input new date of employment:')
                    date_of_employment = self.take_input("date")
                    employee.pop(3)
                    employee.insert(3, date_of_employment)
                case '4':
                    GuiDisplay.printALine(GuiDisplay, 'Input new salery:')
                    salery = self.take_input("money")
                    employee.pop(4)
                    employee.insert(4, salery)
                case '5':
                    GuiDisplay.printALine(GuiDisplay, 'Input new department:')
                    department = self.take_input("string")
                    employee.pop(5)
                    employee.insert(5, department)
                case _:
                    print('input invalid, try again')
        return employee
        
        