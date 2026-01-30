dicts = [{"a": 2, "b": 3}, {"a": 4, "c": 1}]

merged = {}

for d in dicts:
    for k, v in d.items():
        merged[k] = merged.get(k, 0) + v

print(merged)
