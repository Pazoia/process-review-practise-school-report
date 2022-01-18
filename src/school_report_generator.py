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

    count = 0
    for key, value in grades_counter.items():
        if value > 0:
            count += 1
            
    for key, value in grades_counter.items():
        if count == 1 and value > 0:
            report += f"{key}: {value}"
        elif count > 1 and value > 0:
            if key == "Red":
                report += f"{key}: {value}"
            else:
                report += f"{key}: {value}\n"
    
    return report