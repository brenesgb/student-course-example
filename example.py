from model.Student import Student
from model.Course import Course
from errors.EnrollmentError import EnrollmentError


def print_status(student, courses):
    print("=" * 60)
    print("STUDENT:", student)
    for c in courses:
        print(f"  {c} | full? {c.is_full()} | enrolled: {c.enrollment_count}/{c.capacity}")
    print("=" * 60)
    print()


def main():
    # Create some courses
    cs235 = Course("CS235", 1)
    cs245 = Course("CS245", 245)
    cs360 = Course("CS360", 150)
    cs399 = Course("CS399", 300)
    des702 = Course("DES702", 40)

    # Create a student and enrol in courses up to the limit (4)
    brene = Student("abcd123", "Brene")
    brene.enroll_course(cs235)
    brene.enroll_course(cs245)
    brene.enroll_course(cs360)
    brene.enroll_course(cs399)

    print("After Brene enroled in 4 courses:")
    print_status(brene, [cs235, cs245, cs360, cs399, des702])

    # Attempt to enroll Brene in a 5th course
    try:
        brene.enroll_course(des702)
    except EnrollmentError as e:
        print("Expected error enrolling 5th course for Brene:", e)
        print()

    print("Using the special methods")

    # __str__ is used by print()
    print("Overriding __Str__ we can print:", brene)

    # __eq__ is used by ==
    another_brene = Student("bsan361", "Brene")
    same_brene = Student("abcd123", "Brenda San G")
    print("Overriding __eq__ we can compare two students by UPI:")
    print("Is abcd123 Brene the same student as bsan361 Brene?", brene == another_brene)
    print("Is abcd123 Brene the same student as bsan361 Brenda San G?", brene == same_brene)



if __name__ == "__main__":
    main()
