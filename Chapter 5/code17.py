n = [1,2,2,3,3,4,4,5]
duplicate = []

for i in n:
    if i not in duplicate:
        duplicate.append(i)

print("List without duplicates:", duplicate)