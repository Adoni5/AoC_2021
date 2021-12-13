from typing import List
from collections import defaultdict

test_input = """3,4,3,1,2"""

# class School:
#     def __init__(self, ages):
#         self.school = []
#         self.new_school = []
#         self.ages = ages
#
#     def parse(self):
#         lfishes = map(int, self.ages.split(","))
#         for x in lfishes:
#             self.school.append(LFish(x, self, 6))
#
#     def grow(self):
#         days = 256
#         for i in range(1, days + 1):
#             for fish in self.school:
#                 fish.age_up(i)
#             if self.new_school:
#                 self.school.extend(self.new_school)
#             self.new_school = []
#
#
#
#
# class LFish:
#     def __init__(self, c_ctd: int, school: School, countdown: int = 6,):
#         self.original_countdown = countdown
#         self.current_countdown = c_ctd
#         self.school = school
#
#
#     def age_up(self, day=0):
#         self.current_countdown -= 1
#         if self.current_countdown == -1:
#             self.current_countdown = 6
#             self.school.new_school.append(LFish(8, self.school, 8))
def grow(ages, days):
    age_counts = defaultdict(int)
    for age in ages:
        age_counts[age] += 1

    for i in range(days):
        d = defaultdict(int)
        for age, n in age_counts.items():
            if age > 0:
                d[age - 1] += n
            else:
                d[6] += n
                d[8] += n
        age_counts = d
    return sum(age_counts.values())



if __name__ == "__main__":

    with open("input") as fh:
        line = list(map(int, fh.read().split(",")))



        print(f"Part 1: {grow_days(line, 80)}")
        print(f"Part 2: {grow_days(line, 256)}")

