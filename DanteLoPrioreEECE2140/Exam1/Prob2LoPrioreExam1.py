 
student_list = {'Alice':(2023, [3.5, 2.9, 3.1, 3.8]), 'Bob':(2024, [3.0, 2.6]), 'Morgan':(2024, [2.8, 3.9, 3.7]), 'Tim':(2023, [2.5])}

def process_students(dict_student_lineup):
    sorted_graduating_student = {}
    total_grades = 0
    freq = []

    # iterates through dictionary
    for key_name, value_grades in dict_student_lineup.items():
        # computes the gpa for a single student
        total_grades = sum(value_grades[1])
        gpa_caluculation = total_grades/len(value_grades[1])

        # determines whether the a student has the same graduation year as another student
        # require to check this since dictionaries dont have dups
        if value_grades[0] in freq:
            # concats student to same graduation year
            sorted_graduating_student[value_grades[0]] += [(key_name, f'{gpa_caluculation:.2f}')]
        else:
            # creates the student to a new graduation year
            sorted_graduating_student[value_grades[0]] = [(key_name, f'{gpa_caluculation:.2f}')]
            freq.append(value_grades[0])
    return sorted_graduating_student

print(process_students(student_list))