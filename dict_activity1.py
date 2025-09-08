students_data= {
    {"id": 1, "name": "Sara", "class": "5A", "subject": "Math"},
    {"id": 2, "name": "John", "class": "5A", "subject": "Science"},
    {"id": 1, "name": "Sara","class": "5A", "subject": "Math"}, 
    {"id": 4, "name": "syra", "class": "4B", "subject": "English"},
    }


unique_students = {}
for key,value in students_data:
    if value not in unique_students.values():
        unique_students[key] = value


print(unique_students)
