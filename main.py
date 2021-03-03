print()
print("Project Three: Class Rosters")
print()
print()

class_a = ["Harris", "Ashton", "Leah", "Patricia"]
class_b = ["Jaden", "Gus", "Lilly", "Clara"]
class_a.append(class_b)
class_roster = class_a
print(class_roster)
print()
class_a = ["Harris", "Ashton", "Leah", "Patricia"]
class_roster = class_a + class_b
print(class_roster)
print()
class_roster.insert(5, "Mitchell")
print(class_roster)
print()
class_roster.remove("Ashton")
print(class_roster)
print()
class_project_group_1 = class_roster [0:4]
class_project_group_2 = class_roster [4:8]
print("Project Group 1: Bird Migration")
print("Students in group:", class_project_group_1)
print()
print("Project Group 2: Volcanoes")
print("Students in group:", class_project_group_2)
print()
student_trade_1 = class_project_group_1.pop(1)
student_trade_2 = class_project_group_2.pop(2)
class_project_group_1.insert(1, student_trade_2)
class_project_group_2.insert(2, student_trade_1)
print("Project Group 1: Bird Migration")
print("Students in group:", class_project_group_1)
print()
print("Project Group 2: Volcanoes")
print("Students in group:", class_project_group_2)
class_roster.clear()