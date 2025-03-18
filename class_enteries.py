no_of_students = int(input("Enter the amount of students in your classroom: "))



class Students:
    def __init__(self, name, roll, grades, avg):
        self.name = name
        self.roll = roll
        self.grades = subject_marks
        self.avg = avg

    
subject_marks = {}
subjects_list = []
marks = []
no_of_subjects = int(input("Enter the amount of subjects in your classroom: "))
for s in range(no_of_subjects):
     subject = input("Enter a subject: ")
     subjects_list.append(subject)


for i in range (no_of_students):
    name_input = input("Enter the name of the student: ")
    roll_input = int(input("Enter the age of the student: "))

    for x in range(len(subjects_list)):
     sub = subjects_list[x]
     mark = int(input(f"Enter the marks achieved in {sub}: "))
     subject_marks[sub] = mark
     marks.append(mark)

    avg = sum(marks)/len(marks)

    i = Students(name_input, roll_input, subject_marks, avg)
    print(i.name)
    print(i.roll)
    print(i.grades)
    print(i.avg)
    