# Edit this cell to write the corrected code
data = [1, 4, 2, 5, 4]
result = 0

for entry in data:
    result = result + entry
print("sum of data is:", result)

result = data[0]
for entry in data:
    if entry > result:
        result = entry
print("max of data is:", result)

result = data[0]
for entry in data:
    if entry < result:
        result = entry
print("min of data is:", result)
