# Name: Arkenah Mhyssy A. Salvador
# Grade and Section: 8-Adelfa


name = input("Enter Student Name: ")
assessment1 = int(input("Enter Assesment 1: "))
assessment2 = int(input("Enter Assesment 2: "))
assessment3 = int(input("Enter Assesment 3: "))
assessment_average = (assessment1 + assessment2 + assessment3)/ 3


def display_header():
    print("===============================")
    print("STUDENT PERFORMANCE EVALUATOR")
    print("===============================")

def get_student_info():
   print(f"Enter student name: {name}")
   print(f"Enter assessment 1: {assessment1}")
   print(f"Enter assessment 2: {assessment2}")
   print(f"Enter assessment 3: {assessment3}")

assessment_scores = (assessment1, assessment2, assessment3)

def evaluate_performance():
    print(f"Average Score: {assessment_average:.2f}")
    if assessment_average >= 90:
        performance_level = "Outstanding"
        print(performance_level)

    elif assessment_average >= 85:
        performance_level = "Very Satisfactory"
        print(performance_level)

    elif assessment_average >= 80:
        performance_level = "Satisfactory"
        print(performance_level)

    elif assessment_average >= 75:
        performance_level = "Fairly Satisfactory"
        print(performance_level)

    else:
        performance_level = "Needs Improvement"
        print(performance_level)

def display_report():
    display_header()
    get_student_info()
    print("STUDENT PERFORMANCE REPORT")
    print("===============================")
    print(f"Student Name: {name}")
    print(assessment_scores)
    evaluate_performance()


display_report()




