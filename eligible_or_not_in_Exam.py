total_classes_held = int(input("Enter total class held:"))
total_attended = int(input("Enter total attended class:"))
percentage = (total_attended/total_classes_held)*100
if percentage>= 75:
    print(f"your attendence is {percentage}%. So, you are eligible for exam.")
else:
    print(f"your attendence is {percentage}%. So, you are not eligible for exam.")
