x = 1
y = 2
z = 5
#Insertion Sort
a = [741, 222, 456, 430, 124, 419, 101, 170, 930, 347, 179, 799, 461, 528, 870]
j = 2
for j in range(len(a)):
    while j > 0 and a[j] > a[j - 1]:
        a[j], a[j - 1] = a[j - 1], a[j]
        j -= 1
print(a)

if z <= 1 :
    print("Hey")
else:
    print("Ho")
#Sort by selection
a = [792, 803, 982, 904, 436, 679, 583, 942, 85, 857, 812, 27, 95, 613, 674]
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[j] > a[i]:
            a[i], a[j] = a[j], a[i]
print(a)  

#Bubble sort
a = [451, 196, 113, 593, 343, 314, 486, 79, 980, 648, 850, 900, 500, 46, 781]
for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if a[j] < a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
