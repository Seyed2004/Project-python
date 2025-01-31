import json
class Student:
    def __init__(self):
        self.student_list = []

    # 1 => Add student name and number to the list

    def add_list(self, name, number):
        self.student_list.append({
            "name": name,
            "number": number
        })

    # 2 => Search in the list

    def Search_student(self, name): 
        result = []
        for i in self.student_list:
            if name.lower() in self.student_list["name"].lower():
                result.append(i)
                return result
            
    # 3 => Delete the student from list

    def delete_student(self, name):
        result = [len(self.student_list)]
        for i in self.student_list:
            if name.lower() in result("name").lower:
                result.pip(i)
                print(f"Student whit {name} is delete ")
            else:
                print(f"Student with {name} not found ")

    # 4 => Get backup from student list

    def backup(self):
        with open("./studentlist.json","w") as f:
            f.write(json.dumps(self.student_list))

    # 5 => show the list information 

    def show_list(self):
        print(f"Student list is :{self.student_list} ")

    # 6 => Make menu part one

def menu():
    print()
    print(" 1) Add student to list : ")
    print(" 2) Search in the list : ")
    print(" 3) Delete student from list : ")
    print(" 4) Get the backup from list : ")
    print(" 5) Show the list : ")
    print(" 6) Exit ")
    choice = int(input("Enter a number to do : "))
    return choice
    
    # 7 => Make menu part two

student = Student()
while True:
   c = menu()
   if c == 1:
       name = input("enter a name : ")
       number = input("enter the number : ")
       student.add(name, number)
    


