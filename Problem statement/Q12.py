dict={"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}
res = set()
for lst in dict.values():
    for num in lst:
        res.add(num)

result = sorted(res)
print(result)