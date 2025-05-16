l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

merged = []
i = 0
j = 0

while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]: 
        merged.append(l1[i])
        i += 1
    else:
        merged.append(l2[j])
        j += 1

while i < len(l1):
    merged.append(l1[i])
    i += 1

while j < len(l2):
    merged.append(l2[j])
    j += 1

print("Merged List:", merged)
