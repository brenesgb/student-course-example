from errors.CourseFullError import CourseFullError
from errors.EnrollmentError import EnrollmentError


class Course:
    def __init__(self, course_code: str, capacity: int):
        self.__course_code = course_code
        self._capacity = capacity
        self.__enrolled_students = []

    @property
    def course_code(self):
        return self.__course_code

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, cap: int):
        if cap < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = cap

    @property
    def enrollment_count(self):
        return len(self.__enrolled_students)

    def is_full(self) -> bool:
        return self.enrollment_count >= self._capacity

    def add_student(self, student: "Student"):
        if student in self.__enrolled_students:
            raise EnrollmentError(f"{student} already enrolled in {self.course_code}")
        if self.is_full():
            raise CourseFullError(f"Course {self.course_code} is full")
        self.__enrolled_students.append(student)

    def remove_student(self, student: "Student"):
        if student not in self.__enrolled_students:
            raise EnrollmentError(f"{student} is not enrolled in {self.course_code}")
        self.__enrolled_students.remove(student)

    def __eq__(self, other):
        if not isinstance(other, Course):
            return NotImplemented
        return self.course_code == other.course_code

    def __hash__(self):
        return hash(self.course_code)

    def __str__(self):
        return f"{self.course_code}: ({self.enrollment_count}/{self._capacity})"
