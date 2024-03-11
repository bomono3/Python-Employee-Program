import csv
import os.path

class csvHandling():
    writer = None
    reader = None
    file1 = None
    file2 = None
    name = None
    def __init__(self, name):
        self.name = name
        path = './' + name + '.csv'
        check_file = os.path.isfile(path)
        if check_file:
            self.file1 = open(name + '.csv', 'a', newline='')
            self.writer = csv.writer(self.file1)
            self.file2 = open(name + '.csv', 'r')
            self.reader = csv.reader(self.file2)
            return
        self.file1 = open(name + '.csv', 'w', newline='')
        self.writer = csv.writer(self.file1)
        self.file2 = open(name + '.csv', 'r')
        self.reader = csv.reader(self.file2)
    def readFile(self, name):
        for row in self.reader:
            print(row)
            self.__init__(self.name)
    def addEmployee(self, employee):
        try:
            new_id = max(self.reader, key=lambda row: int(row[0]))
            new_id_number = int(new_id[0])
        except ValueError:
            new_id_number = 0
            employee.insert(0, new_id_number)
            self.writer.writerow(employee)
            self.__init__(self.name)
            return
        new_id_number += 1
        new_id_number = str(new_id_number)
        employee.insert(0, new_id_number)
        self.writer.writerow(employee)
        self.__init__(self.name)
    def removeEmployee(self, id):
        with open('temp.csv', 'w', newline='') as out:
            temp_writer = csv.writer(out)
            temp_list = [row for row in self.reader if row[0] != f"{id}"]
            #for row in self.reader:
            #    if row[0] != f"{id}":
            #        temp_writer.writerow(row)
            temp_writer.writerows(temp_list)
        self.file1.close()
        self.file2.close()
        os.remove(self.name + '.csv')
        os.rename("temp.csv", self.name + '.csv')
        self.__init__(self.name)
        return
    def getEmployee(self, id):
        
        employee = [row for row in self.reader if row[0] == f"{id}"]
        self.file1.close()
        self.file2.close()
        self.__init__(self.name)
        try:
            return employee[0]
        except IndexError:
            raise IndexError
    def updateEmployee(self, id, employee):
        with open('temp.csv', 'w', newline='') as out:
            temp_writer = csv.writer(out)
            temp_list = [(employee if row[0] == f"{id}" else row) for row in self.reader]
            temp_writer.writerows(temp_list)
        self.file1.close()
        self.file2.close()
        os.remove(self.name + '.csv')
        os.rename("temp.csv", self.name + '.csv')
        self.__init__(self.name)
        return
    