"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = tuple(range(1, 100))
# q = tuple(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

def printSumDiff(q):
    add = {}
    sub = {}
    solutions = {}

    for x in q:
        for y in q:
            num_sum = f(x) + f(y)
            if num_sum in add:
                add[num_sum].append((x, y))
            else:
                add[num_sum] = [(x, y)]

            num_sub = None
            if x > y:
                num_sub = f(x) - f(y)
                if num_sub in sub:
                    sub[num_sub].append((x, y))
                else:
                    sub[num_sub] = [(x, y)]
            else:
                num_sub = f(y) - f(x)
                if num_sub in sub:
                    sub[num_sub].append((y, x))
                else:
                    sub[num_sub] = [(y, x)]

            if num_sum in sub:
                for c, d in sub[num_sum]:
                    equation = [f(x), f(y), f(c), f(d)]
                    if tuple(equation) not in solutions:
                        solutions[tuple(equation)] = equation
                        print(f"{equation[0]} + {equation[1]} = {equation[2]} - {equation[3]}")

            if num_sub in add:
                for c, d in add[num_sub]:
                    if x > y:
                        equation = [f(c), f(d), f(x), f(y)]
                        if tuple(equation) not in solutions:
                            solutions[tuple(equation)] = equation
                            print(f"{equation[0]} + {equation[1]} = {equation[2]} - {equation[3]}")
                    else:
                        equation = [f(c), f(d), f(y), f(x)]
                        if tuple(equation) not in solutions:
                            solutions[tuple(equation)] = equation
                            print(f"{equation[0]} + {equation[1]} = {equation[2]} - {equation[3]}")

printSumDiff(q)