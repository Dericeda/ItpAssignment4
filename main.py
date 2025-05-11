class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"


class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__grade = grade

    def get_student_id(self):
        return self.__student_id

    def get_grade(self):
        return self.__grade

    def get_details(self):
        return f"{super().__str__()}, ID: {self.__student_id}, Grade: {self.__grade}"


class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        super().__init__(name, age)
        self.__teacher_id = teacher_id
        self.__subject = subject

    def get_teacher_id(self):
        return self.__teacher_id

    def get_subject(self):
        return self.__subject

    def get_details(self):
        return f"{super().__str__()}, ID: {self.__teacher_id}, Subject: {self.__subject}"


class Classroom:
    def __init__(self, room_number):
        self.__room_number = room_number
        self.__students = []
        self.__teacher = None

    def add_student(self, student):
        if isinstance(student, Student):
            self.__students.append(student)
            return True
        return False

    def get_student_list(self):
        return self.__students

    def set_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.__teacher = teacher
            return True
        return False

    def get_classroom_info(self):
        info = f"Classroom {self.__room_number}:\n"
        if self.__teacher:
            info += f"Teacher: {self.__teacher.get_name()}, Subject: {self.__teacher.get_subject()}\n"
        else:
            info += "No teacher assigned yet.\n"

        if self.__students:
            info += "Students:\n"
            for student in self.__students:
                info += f"- {student.get_name()} (ID: {student.get_student_id()}, Grade: {student.get_grade()})\n"
        else:
            info += "No students added yet.\n"

        return info


def search_students_by_grade(classroom, grade):
    return list(filter(lambda s: s.get_grade() == grade, classroom.get_student_list()))



school = {}
while True:
    print("\nMenu:\n""1. Add a student\n2. Add a teacher\n3. Create a classroom\n4. Assign teacher to a classroom\n5. Add student to a classroom\n6. Display classroom information\n7. Search for students by grade\n8. Exit")


    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        student_id = int(input("Enter student ID: "))
        grade = input("Enter grade: ")
        school[student_id] = Student(name, age, student_id, grade)
        print(f"Student \"{name}\" added successfully!")

    elif choice == '2':
        name = input("Enter teacher name: ")
        age = int(input("Enter age: "))
        teacher_id = int(input("Enter teacher ID: "))
        subject = input("Enter subject: ")
        school[teacher_id] = Teacher(name, age, teacher_id, subject)
        print(f"Teacher \"{name}\" added successfully!")

    elif choice == '3':
        room_number = int(input("Enter classroom number: "))
        school[room_number] = Classroom(room_number)
        print(f"Classroom {room_number} was successfully created!")

    elif choice == '4':
        room_number = int(input("Enter classroom number: "))
        teacher_id = int(input("Enter teacher ID to assign: "))
        if room_number in school and teacher_id in school:
            school[room_number].set_teacher(school[teacher_id])
            print(f"Teacher \"{school[teacher_id].get_name()}\" assigned to classroom {room_number} successfully!")

    elif choice == '5':
        room_number = int(input("Enter classroom number: "))
        student_id = int(input("Enter student ID: "))
        if room_number in school and student_id in school:
            school[room_number].add_student(school[student_id])
            print(f"Student \"{school[student_id].get_name()}\" added to classroom {room_number} successfully!")


    elif choice == '6':
        room_number = int(input("Enter classroom number: "))
        if room_number in school:
            print(school[room_number].get_classroom_info())


    elif choice == '7':
        room_number = int(input("Enter classroom number: "))
        grade = input("Enter grade to search for: ")
        if room_number in school:
            students = search_students_by_grade(school[room_number], grade)
            print(f"Students with grade {grade} in classroom {room_number}:")
            for student in students:
                print(f"- {student.get_name()} (ID: {student.get_student_id()})")



    elif choice == '8':
        break

    else:
        print("Invalid choice. Please try again.")

