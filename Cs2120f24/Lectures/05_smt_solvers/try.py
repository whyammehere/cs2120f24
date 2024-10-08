from z3 import *

# declare names for 3 distinct Z3 integer variable expressions and a PL variable expr
M = Int('M')
N = Int('N')
P = Int('P')
B = Bool('B')

# a few arithmetic relational expressions
c1 = M + N < 10
c2 = M > 3
c3 = N > 5

# a few propositional logic expressions involving arithmetic relational expressions 
p = And(c1, c2, c3)
q = And(Or(c1, c2), c3)
r = And(q, B) 


def report(e):
    s = Solver()
    s.reset()
    s.add(e)
    print("Satisfiability property of ", e, " is ", s.check())
    if (s.check() == sat):
        print("Model: ", s.model())

report(p) 
report(q)
report(r)








C = Int('c')
D = Int('d')
E = Int('e')
val = C + 15*D + 0.25*E
num = C + D + E
cats_and_dogs_and_mice = And(C > 0, D > 0, E > 0, val == 100, num == 100)

report(cats_and_dogs_and_mice)