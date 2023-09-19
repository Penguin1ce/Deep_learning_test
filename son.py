# 人力系统 全职员工 兼职员工
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工:{self.name}\t工号:{self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def Calculate_monthly_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def Calculate_monthly_pay(self):
        return self.daily_salary * self.work_days


Zakary = FullTimeEmployee("Zakary", "20230941", 12000)
John = PartTimeEmployee("Jphn", "20230942", 100, 20)

Zakary.print_info()
print(f"{Zakary.Calculate_monthly_pay()}")
John.print_info()
print(f"{John.Calculate_monthly_pay()}")
