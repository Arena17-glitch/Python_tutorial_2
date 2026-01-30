students = [("Alice", [80, 90]), ("Bob", [70, 85, 90])]

result = {}
for name, marks in students:
    avg = sum(marks) / len(marks)
    result[name.lower()] = round(avg, 2)

print(result)
