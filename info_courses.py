## Daniel Ham
## INFO Courses


## Open file and read lines
with open("INFOcourses.txt", "r") as f:
    course_list = f.readlines()

courses = {}

for line in course_list:
    code, name = line.split(", ")
    courses[code] = name.strip()

print("Information on", len(courses.keys()), "courses loaded.")
while True:
    search_course = input("Enter a course code or STOP: ")

    if search_course.upper() == 'STOP':
        break
    else:
        print("The name of that course is", courses.get(search_course, "not found"), ".")

    
