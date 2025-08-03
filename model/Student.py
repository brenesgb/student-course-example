from errors.CourseFullError import CourseFullError
from errors.EnrollmentError import EnrollmentError


class Student:
    def __init__(self, student_id: str, name: str):
        self.__student_id = student_id
        self._name = name
        self._enrolled_courses = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def courses(self):
        return list(self._enrolled_courses)

    def enroll_course(self, new_course: "Course"):
        if new_course in self._enrolled_courses:
            raise EnrollmentError(f"Already enrolled in {new_course.course_code}")
        if len(self._enrolled_courses) >= 4:
            raise EnrollmentError("Cannot enroll in more than 4 courses")
        if new_course.is_full():
            raise CourseFullError(f"Course {new_course.course_code} is full")
        new_course.add_student(self)
        self._enrolled_courses.append(new_course)

    def drop_course(self, course: "Course"):
        if course not in self._enrolled_courses:
            raise EnrollmentError(f"Not enrolled in {course.course_code}")
        if len(self._enrolled_courses) <= 1:
            raise EnrollmentError("Student must be enrolled in at least one course")
        course.remove_student(self)
        self._enrolled_courses.remove(course)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.__student_id == other.__student_id

    def __str__(self):
        course_codes = ", ".join(c.course_code for c in self._enrolled_courses)
        return f"{self._name} enrolled in: [{course_codes}]"

    def __hash__(self):
        return hash(self.__student_id)
