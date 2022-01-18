def report_generator(grades_input):
    grades_list = grades_input.split(", ")
    
    green_grade_counter = 0

    for grade in grades_list:
        if grade == "Green":
            green_grade_counter += 1
            report = f"Green: {green_grade_counter}"
        elif grades_input == "Amber":
            return "Amber: 1"
        elif grades_input == "Red":
            return "Red: 1"
        
        

    return report