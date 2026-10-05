from json import load


class Country_data:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = self.read_data()
        self.country = self.file_data["country"]
        self.max_temp = self.file_data["max_temp"]
        self.min_temp = self.file_data["min_temp"]

    def read_data(self):
        with open(self.file_path) as file:
            return load(file)

egypt = Country_data("java.json")
print(*egypt.file_data.keys())
print(egypt.country)
print(egypt.max_temp)
print(egypt.min_temp)