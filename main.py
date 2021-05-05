class ColorText():
    ORANGE = '\033[38;5;172m'
    BLUE = '\033[38;5;45m'
    ENDC = '\033[0m'


class Student(ColorText):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f"{other} is not Student")
        else: return self.avg_score() < other.avg_score()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print(f"{other} is not Student")
        else: return self.avg_score() == other.avg_score()

    def rate_lession(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses_in_progress \
            and course in lector.courses_attached and 1 <= grade <= 10:
            lector.grades.append(grade)
        else: 
            print('Error')

    def __list_to_str(self, input):
        out = f""
        for num, word in enumerate(input):
            if num < len(input) - 1:
                out += f"{self.ORANGE}{word}{self.ENDC}, "
            else: out += f"{self.ORANGE}{word}{self.ENDC}"
        return out

    def avg_score(self):
        hw_grades = [k for val in self.grades.values() for k in val]
        return sum(hw_grades)/len(hw_grades) if hw_grades else 0

    def __str__(self):
        return f"\rName: {self.ORANGE}{self.name}{self.ENDC}\n\
                \rSurname: {self.ORANGE}{self.surname}{self.ENDC}\n\
                \rAVG score: {self.BLUE}{self.avg_score():.{2}f}{self.ENDC}\n\
                \rCourses in progress: {self.__list_to_str(self.courses_in_progress)}\n\
                \rFinished courses: {self.__list_to_str(self.finished_courses)}\n"


class Mentor(ColorText):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __lt__(self, other):
        if not isinstance(other, Lector):
            print(f"{other} is not Lector")
        else: return self.avg_rate() < other.avg_rate()

    def __eq__(self, other):
        if not isinstance(other, Lector):
            print(f"{other} is not Lector")
        else: return self.avg_rate() == other.avg_rate()
    
    def avg_rate(self):
        return sum(self.grades)/len(self.grades) if self.grades else 0

    def __str__(self):
        return f"\rName: {self.ORANGE}{self.name}{self.ENDC}\n\
            \rSurname: {self.ORANGE}{self.surname}{self.ENDC}\n\
            \rAVG lession rate: {self.BLUE}{self.avg_rate():.{2}f}{self.ENDC}\n"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached\
             and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'
    
    def __str__(self):
        return f"\rName: {self.ORANGE}{self.name}{self.ENDC} \n\
            \rSurname: {self.ORANGE}{self.surname}{self.ENDC}\n"


# функция для подсчета средней оценки за домашние задания по всем студентам в рамках 
# конкретного курса (в качестве аргументов принимаем список студентов и название курса);
def avg_rate_course(student_list, course):
    grades = [grad for student in student_list if course in student.grades\
         for grad in student.grades[course]]
    # grades = []
    # for student in student_list:
    #     course_grades = student.grades.get(course, None)
    #     if course_grades is not None:
    #         grades += course_grades 
    return sum(grades)/len(grades) if grades else 0


# функция для подсчета средней оценки за лекции всех лекторов в рамках конкретного курса 
# (в качестве аргументов принимаем список лекторов и название курса).
def avg_rate_lession(lector_list, course):
    grades = [grad for lector in lector_list if course in lector.courses_attached\
         for grad in lector.grades]
    return sum(grades)/len(grades)

    
if __name__ == '__main__':
    alex = Student("Alex", "Alexeev", "male")
    alex.finished_courses = ["BASIC Corvet", "ADA", "Hystory of KPSS", "Marks Theory"]
    alex.courses_in_progress = ["Python", "HTML"]
    
    nina = Student("Nina", "Petrova", "female")
    nina.finished_courses = ["PR", "Marketing", "GIT"]
    nina.courses_in_progress = ["Python", "HTML", "C++", "OS", "Verilog HDL"]
    
    burov = Lector("Vadim", "Burov")
    burov.courses_attached = ["Python", "C++", "OS", "Verilog HDL"]

    smernova = Lector("Natalia", "Smernova")
    smernova.courses_attached = ["HTML", "Python", "GIT"]

    kononov = Reviewer("Igor", "Kononov")
    kononov.courses_attached = ["HTML"]

    krasnyh = Reviewer("Polina", "Krasnyh")
    krasnyh.courses_attached = ["Python", "C++", "OS", "Verilog HDL", "HTML"]

    alex.rate_lession(burov, "Python", 10)
    alex.rate_lession(smernova, "HTML", 7)

    nina.rate_lession(burov, "Python", 9)
    nina.rate_lession(burov, "C++", 10)
    nina.rate_lession(burov, "OS", 8)
    nina.rate_lession(burov, "Verilog HDL", 4)
    nina.rate_lession(smernova, "HTML", 8)

    kononov.rate_hw(alex, "HTML", 2)
    kononov.rate_hw(nina, "HTML", 10)

    krasnyh.rate_hw(alex, "Python", 10)
    krasnyh.rate_hw(alex, "HTML", 7)
    krasnyh.rate_hw(nina, "Python", 7)
    krasnyh.rate_hw(nina, "C++", 6)
    krasnyh.rate_hw(nina, "OS", 8)
    krasnyh.rate_hw(nina, "Verilog HDL", 10)
    krasnyh.rate_hw(nina, "HTML", 10)

    if alex > nina:
        print(f"{alex.name} {alex.surname} is the best student")
    elif (nina > alex):
        print(f"{nina.name} {nina.surname} is the best student")
    else: print(f"{nina.name} {nina.surname} and {alex.name} {alex.surname} equal students")

    if burov > smernova:
        print(f"{burov.name} {burov.surname} is the best lector")
    elif (nina > alex):
        print(f"{smernova.name} {smernova.surname} is the best lector")
    else: print(f"{burov.name} {burov.surname} and {smernova.name} {smernova.surname} equal lectors")

    print('\n', alex, '\n',  nina, '\n', burov, '\n', smernova, '\n', kononov, '\n', krasnyh )

    lectors = [burov, smernova]
    students = [alex, nina]
    print(avg_rate_lession(lectors, "Python"))
    print(avg_rate_course(students, "HTML"))

 