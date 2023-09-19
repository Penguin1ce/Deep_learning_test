class Student:
    def __init__(self, name, s_id):
        self.name = name
        self.id = s_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grades(self, course, grades):
        if course in self.grades:
            self.grades[course] = grades
        else:
            print("科目不存在")

    def print_grades(self):
        print(f"学生:{self.name} 学号:{self.id} ")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")


Zakary = Student("Zakary", "20230941")
print(Zakary.name)
Zakary.set_grades("数学", 95)
Zakary.set_grades("语文", 100)
Zakary.set_grades("英语", 98)

Zakary.print_grades()
