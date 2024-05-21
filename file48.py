class Student:
    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores
    
    def average_score_stats(self):
        self.sr_int = sum(self.scores) / len(self.scores)
        return (f"Name: {self.name} \nAge: {self.age} \nGrade: {self.grade} \nAverage score: {self.sr_int}")


a = Student('John', 16, '9-A', [5,5,5,4,4,4])
print(a.average_score_stats())