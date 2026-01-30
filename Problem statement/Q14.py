text = "banana"

index_map = {}

for i, ch in enumerate(text):
    if ch not in index_map:
        index_map[ch] = []
    index_map[ch].append(i)

# convert lists to tuples
for ch in index_map:
    index_map[ch] = tuple(index_map[ch])

print(index_map)
