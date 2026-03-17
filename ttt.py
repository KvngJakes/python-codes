# a = 1
# b = 3
# c = 2
# x1 = (-b + ((b**2 - 4*a*c) ** 0.5))/(2*a)
# x2 = (-b - ((b**2 - 4*a*c) ** 0-5))/(2*a)

# print (x1)
# print (x2)

def quadratic(a, b, c):
    x1 = (-b + ((b**2 - 4*a*c) ** 0.5))/(2*a)
    x2 = (-b - ((b**2 - 4*a*c) ** 0-5))/(2*a)

    return x1, x2

# a1 = 1
# b1 = 3
# c1 = 2

# w1, w2 = quadratic(a1, b1, c1)
# print(f"The roots of the equation {a1}x^2 + {b1}x + {c1} are {w1} and {w2}")

#q = [1, 2, 3, 4, 1, 2]
#for i in q:
#    print(i)

#w = set(q)
#print(w)

#y = {'a': 1, 2: 'b'}

#print(y['a'])
#q[-3] = "tea"
#print(q)

matrix = [[1, 2, 3, 4] [4, 6, 7, 2] [8, 5, 9, 3]]    
