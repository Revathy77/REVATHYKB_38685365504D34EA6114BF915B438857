#Sort_students function takes a list of student objects and sort them based on cgpa

class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  sorted_students =sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  return sorted_students


students =[
  Student("Anu","1234",7.9),
  Student("Abi","1233",8.7),
  Student("Reva","1236",8.1),
  Student("Raga","1235",8.9)
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name : {} , Roll Number : {} , CGPA : {}".format(student.name,student.roll_number,student.cgpa))
