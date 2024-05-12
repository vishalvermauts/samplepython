x = 3.0
y = x
z = 4.5
z -= 1.5

print(y is x)
print(y==z)
print(z is x)

print(z==x)

print(id(x))
print(id(y))
print(id(z))
