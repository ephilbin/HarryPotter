#students = ["Hermione", "Ron", "Harry", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
            }
            
for student in students:
    print(student, students[student], sep=", ") 

#iterative method, not having to print each element individually
#instead of typing the names out one by one we used a for loop