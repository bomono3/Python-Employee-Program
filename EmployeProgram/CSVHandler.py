import csv
import os.path

class csvHandling():
    def createFile(self, name):
        path = './' + name + '.csv'
        check_file = os.path.isfile(path)
        if check_file:
            return
        with open(name + '.csv', 'w', newline='') as file:
            writer = csv.writer(file)

