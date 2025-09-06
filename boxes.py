import math
item_number = int(input("The number of manufactured items "))
per_box = int(input("The number of item the user will pack per box "))

needed_box = item_number / per_box
check_a = math.ceil(needed_box)
print()
print(f"For {item_number} items, packing {per_box} item per box, you'll need {check_a} boxes. ")