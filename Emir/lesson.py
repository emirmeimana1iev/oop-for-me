class Building:
    counter = 0
    def __init__(self, year=2000, city="los"):
        self.year = year
        self.city = city
        Building.counter += 1

    def get_info(self):
        print("Year:", self.year, ". City:", self.city)

class School(Building):
    def __init__(self, children, year=2000, city="Tokmok"):
        self.children = children
        super().__init__(year, city)
    def get_info(self):
        print("Это про школы")
        super().get_info()
        print("Children:", self.children)

    def change_children(self, new_children):
        old_children, self.children = self.children, new_children
        print(F"Children was changed from {old_children} to {new_children}")


class House(Building):
    pass

class Store(Building):
    def __init__(self, year, city, replicas):
        super().__init__(year, city)
        self.replicas = replicas
    def get_info(self):
        print("А это про магазин")
        super().get_info()
        print("Replicas:", self.replicas)

print(Building.counter)
school= School(100, 2000, "bishkek")
school.get_info()
school.change_children(200)
school.get_info()
school.change_children(300)
school.get_info()
store = Store(2006, "Aksy", "apples")
store.get_info()
house = House(2012, "kerb")
house.get_info()
print(Building.counter)