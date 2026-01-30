attendance = {"Ravi": ["P","P","A","A"], "Neha": ["P","P","P","P"]}

result = {}

for name, record in attendance.items():
    present_count = record.count("P")
    percentage = (present_count / len(record)) * 100
    result[name] = round(percentage, 2)

print(result)
