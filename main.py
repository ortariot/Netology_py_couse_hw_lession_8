class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lession(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses_in_progress and course in lector.courses_attached and 1 <= grade <= 10:
            lector.grades.append(grade)
        else: 
            print('Error')
    
    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nAVG score: {sum(self.grades)/len(self.grades)}"


        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

 
class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
    
    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nAVG lession rate: {sum(self.grades)/len(self.grades)}"



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'
    
    def __str__(self):
        return f"Name: {self.name} \nSurname: {self.surname}"


petrov = Lector("Igor", "Petrov")
chernov = Reviewer("Nikita", "chernov")
petrov.courses_attached.append("GIT")
petrov.courses_attached.append("GITHUB")
chernov.courses_attached.append("Hystory")
sergey =  Student("Serega", "Kamarov", "mail")
sergey.courses_in_progress.append("GIT")
sergey.courses_in_progress.append("GITHUB")
sergey.rate_lession(petrov, "GIT", 77)
sergey.rate_lession(petrov, "GITHUB", 1)
sergey.rate_lession(petrov, "GIT", 5)
sergey.rate_lession(petrov, "GIT", 12)
sergey.rate_lession(chernov, "GIT", 10)

print(petrov.surname)
print(petrov.grades)
print(chernov)
print(petrov)
