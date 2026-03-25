text = "programming"

unique = []
for ch in text:
    if ch not in unique:
        unique.append(ch)

result = tuple(unique)
print(result)
