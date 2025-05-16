a = [10,90,40,76,80,20,6]
print("Original List: ", a)

for i in range (0,len(a)):
    for j in range (i+1, len(a)):
        if a[i] >= a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print("The Sorted List: ", a)