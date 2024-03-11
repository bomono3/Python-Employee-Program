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
    def AddEmployee(self, employee):
        new_id = sum(1 for line in self.file2)
        employee.insert(0, new_id)
        self.writer.writerow(employee)
    def removeEmployee(self, id):
        with open('temp.csv', 'w', newline='') as out:
            temp_writer = csv.writer(out)
            for row in self.reader:
                if row[0] != f"{id}":
                    temp_writer.writerow(row)
        self.file1.close()
        self.file2.close()
        os.remove(self.name + '.csv')
        os.rename("temp.csv", self.name + '.csv')
        self.__init__(self.name)
        return