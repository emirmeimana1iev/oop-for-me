                                                            # import os
# rename(), path.isfile(), path.exists(), remove(), getcwd()[get current working directory   получить текушую рабочую папку], mkdir(), rmdir(), listdir(), replase(), chdir()!

base_salary = 30000
ex = int(input("Enter the experience: "))
def get_salary(experience):
    salary = base_salary
    if experience <= 3:
        print(salary)
    else:
        for _ in range(experience - 3):
            salary *= 1.05
        print(salary)
get_salary(ex)