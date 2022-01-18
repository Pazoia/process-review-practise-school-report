def report_generator(grades_input):
    grades_list = grades_input.split(", ")
    
    green_grade_counter = 0
    amber_grade_counter = 0
    red_grade_counter = 0

    report = ""

    for grade in grades_list:
        if grade == "Green":
            green_grade_counter += 1
            report = f"Green: {green_grade_counter}"
        elif grade == "Amber":
            amber_grade_counter += 1
            report = f"Amber: {amber_grade_counter}"
        elif grade == "Red":
            red_grade_counter += 1
            report = f"Red: {red_grade_counter}"
        
        

    return report