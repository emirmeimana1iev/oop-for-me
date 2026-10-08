# data = input("введите текст: ")
#
#
# file = open("data/text.txt", "a")
#
#
# file.write(data + "\n")
# file.close()


# file = open("data/text.txt", "r")
# # print(file.read())
#
# for line in file:
#     print(line, end="")
# file.close()
# import os
# os.replace("emir.py", "Emir/emir.py")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model

    def describe(self):
        print(self.make, self.model)


porter = Car("Ford", "Mustang", 19)
print(porter.__init__())
porter.describe()