# Find roots using Vieta's formulas

b = int(input("Enter -b: "))
c = int(input("Enter c: "))

found = False
for i in range(-100, 101):
    if found:
        break
    for j in range(-100, 101):
        if i == 0 or j == 0:
            continue
        if i + j == b and i * j == c:
            print(f"x1 = {i}, x2 = {j}")
            found = True
            break

if not found:
    print("No roots found")