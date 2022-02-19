"""Testing the bullshit in the practice for QZ01."""

x: int = 5
y: int = 3

x = x - 1
if x < y:
    z = x ** y / 2
else:
    if x == y:
        z = y % x
    else:
        x = x / 2 # Fucking whyyyyyy
        z = y - x
    z = z + 1
print(z)