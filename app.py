# Find roots using Vieta's formulas

b = int(input("Enter -b: "))

c = int(input("Enter c: "))

found = False
for i in range(-100, 101):
    for j in range(-100, 101):
        if i == 0 or j == 0:
            continue
        if i * j == c:
            with open("log.txt", "a") as f:
                f.write(f"[ i ({i}) ] + [ j ({j}) ] = [ {i + j} ]\n")
                f.write(f"[ i ({i}) ] * [ j ({j}) ] = [ {i * j} ]\n")
                f.write("\n")
        if i + j == b and i * j == c:
            print(f"x1 = {i}, x2 = {j}")
            found = True
            break
    if found:
        break

if not found:
    print("No roots found")