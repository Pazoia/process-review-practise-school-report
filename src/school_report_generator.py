def report_generator(grades_input):
    report = ""
    grades_list = grades_input.split(", ")
    grades_counter = {
        "Green": 0,
        "Amber": 0,
        "Red": 0,
    }

    for grade in grades_list:
        for key, value in grades_counter.items():
            if grade == key:
                grades_counter[grade] += 1

    for key, value in grades_counter.items():
        if value > 0:
            report += f"{key}: {value}"
    
    return report