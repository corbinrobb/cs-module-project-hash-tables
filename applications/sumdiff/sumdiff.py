"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = tuple(range(1, 10))
# q = tuple(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

add = {}
sub = {}
solutions = {}

for x in q:
    for y in q:
        num_sum = f(x) + f(y)
        add[num_sum] = (x, y)

        num_sub = None
        if x > y:
            num_sub = f(x) - f(y)
            sub[num_sub] = (x, y)
        else:
            num_sub = f(y) - f(x)
            sub[num_sub] = (y, x)

        if sub.get(num_sum) != None:
            c, d = sub[num_sum]
            equation = [f(x), f(y), f(c), f(d)]
            if solutions.get(tuple(equation)) == None:
                solutions[tuple(equation)] = equation


        if add.get(num_sub) != None:
            c, d = add[num_sub]
            if x > y:
                equation = [f(c), f(d), f(x), f(y)]
                equation2 = [f(d), f(c), f(x), f(y)]
                if solutions.get(tuple(equation)) == None:
                    solutions[tuple(equation)] = equation
                if solutions.get(tuple(equation2)) == None:
                    solutions[tuple(equation2)] = equation2
            else:
                equation = [f(c), f(d), f(y), f(x)]
                equation2 = [f(d), f(c), f(y), f(x)]
                if solutions.get(tuple(equation)) == None:
                    solutions[tuple(equation)] = equation
                if solutions.get(tuple(equation2)) == None:
                    solutions[tuple(equation2)] = equation2


for i in solutions:
    print(f"{i[0]} + {i[1]} = {i[2]} - {i[3]}")
