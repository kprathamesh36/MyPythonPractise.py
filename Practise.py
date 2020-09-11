attack = 0
defense = 0
hp = 0
while True:
    attack = int(input("Enter attack between 1-15:"))
    if 1 <= int(attack) <= 15:
        break
    print("Error Invalid Input")
while True:
    defense = int(input("Enter defense between 1-15:"))
    if 1 <= int(defense) <= 15:
        break
    print("Error Invalid Input")
while True:
    hp = int(input("Enter hp between 1-15:"))
    if 1 <= int(hp) <= 15:
        break
    print("Error Invalid Input")

count = attack + defense + hp
ivcalc = round((count * 100) / 45)
print(ivcalc)
