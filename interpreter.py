expression = input("Expression:").lower().strip()

x, y, z = expression.split(" ")

x = float(x)
z = float(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*" or y == "x":
    result = x * z
elif y == "/":
    result = x / z

print(f"{result:.1f}")
