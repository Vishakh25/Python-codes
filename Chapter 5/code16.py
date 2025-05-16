n = [7,9,34,18,20]

max = n[0]
min = n[0]

for i in n:
    if i > max:
        max = i
    if i < min:
        min = i
print("Maximum: ", max)
print("Minimun: ", min)