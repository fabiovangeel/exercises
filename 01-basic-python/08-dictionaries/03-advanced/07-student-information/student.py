def process_data(string_data):
    d = {}
    for i in string_data:
        name, age, *courses = i.split(",")
        d[name] = {'age': int(age), 'courses': courses}
    return d


def average_age(data):
    total = 0
    numb_student = 0
    for i in data.values():
        total += i['age']
        numb_student += 1
    return total/numb_student


def courses(data):
    courses = set()
    for i in data.values():
        courses.update(i['courses'])
    return courses


def most_common_courses(data):
    course_counts = {}
    for student in data.values():
        for course in student['courses']:
            if course not in course_counts:
                course_counts[course] = 0
            course_counts[course] += 1
    max_count = max(course_counts.values())
    return {
        course
        for course in course_counts.keys()
        if course_counts[course] == max_count
    }
