# 1450. Number of Students Doing Homework at a Given Time
def busyStudent(self, start: List[int], end: List[int], t: int) -> int:
    good_student = 0

    for i in range(0, len(start)):
        if t in range(start[i], end[i] + 1):
            good_student += 1

    return good_student

