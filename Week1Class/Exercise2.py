import random

# Define objects
students = ["Alice", "Bob", "Charlie"]
courses = {
    "CS101": {"difficulty": 0.7},   # Hard course, low chance to get A
    "CS102": {"difficulty": 0.3}    # Easy course, high chance to get A
}

# Probabilistic rule: P(student gets A | course difficulty)
def grade_student(course):
    difficulty = courses[course]["difficulty"]
    # Probability to get an A is inversely proportional to difficulty
    return random.random() < (1 - difficulty)

# Simulate
results = []
for student in students:
    for course in courses:
        got_A = grade_student(course)
        results.append((student, course, "A" if got_A else "Not A"))

# Print results
for r in results:
    print(r)
