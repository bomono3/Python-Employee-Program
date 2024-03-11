import InvalidInputException
from datetime import datetime
import re

class GuiDisplay:
    
    def list_options(self, choices):
        print(*choices, sep = "\n")
    def printALine(self, line):
        print(line)

class GuiInputHandling:
    
    def take_input(self, input_type):
        
        valid_input = 'false'
        format = "%d/%m/%Y"
        
        while valid_input == 'false':
            choice = input()
            try:
                match input_type:
                        case 'int':
                            int(choice)
                            valid_input = 'true'
                        case 'string':
                            valid_input = 'true'
                        case 'date':
                            valid_input = bool(datetime.strptime(choice, format))
                            valid_input = 'true'
                        case 'money':
                            result = re.match("\$?(-?(\d+[,.])*\d+)", choice)
                            if result == None:
                                raise InvalidInputException
                            re.match("\$?(-?(\d+[,.])*\d+)", choice).group(1)
                            re.sub('[,$]', '', choice)  
                            float(re.sub('[,$]', '', choice))
                            valid_input = 'true'
                        case 'int5':
                            if 6 < int(choice) < 1:
                                raise InvalidInputException
                            valid_input = 'true'
                        case _:
                            print('No input type specified')
                            return
            except (InvalidInputException.InvalidInputException, ValueError):
                valid_input = 'false'
            if valid_input == 'false':
                GuiDisplay.printALine(GuiDisplay, 'Invalid input, try again.')
        return str(choice)
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
        
        