import APIHandler
from course import Course
from schedule import Schedule
from pprint import pp

def main():
    MATH140 = Course("MATH140")
    CMSC131 = Course("CMSC131")
    MATH141 = Course("MATH141")
    CMSC132 = Course("CMSC132")
    CMSC216 = Course("CMSC216")
    CMSC250 = Course("CMSC250")
    CMSC330 = Course("CMSC330")
    CMSC351 = Course("CMSC351")
    MATH240 = Course("MATH240")
    STAT400 = Course("STAT400")


    prev_courses = [MATH140, CMSC131]
    schedule = Schedule()
    for course in prev_courses:
        schedule.add_previous_course(course)
    schedule.math_course = "MATH140"
    print(schedule.calculate_requirements())

    course_list = [MATH141, CMSC132, CMSC216, CMSC250, MATH240, CMSC330, CMSC351, STAT400]

    print(schedule.build_schedule(course_list))


if __name__ == "__main__":
    main()
