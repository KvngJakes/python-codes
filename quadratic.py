a = 1
b = -3
c = 2

D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + D ** 0.5) / (2*a)
    x2 = (-b - D ** 0.5) / (2*a)
    print("X1=", x1)
    print("X2=", x2)
elif D == 0:
    x = -b / (2*a)
    print("X+", x)
else:
    print("no real root")
