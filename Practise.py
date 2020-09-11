n = int(input("Enter number of families"))
p = []
j = []
for i in range(0, n):
    ele = int(input("Enter the income of each family"))
    p.append(ele)
for i in range(0, n):
    e = int(input("Enter the number of childrens for each family"))
    j.append(e)
b = 0
count = 0
for m in p:
    for n in j:
        if n > 2:
            b = b + m
            count = count + 1

b = b / count
print(b)
