from sympy import symbols, solve
import sympy as sp
import numpy as np
# from segundo_sistema import get_p_from_q

# ejemplo del paper

N = 8
q = symbols(''.join('q'+str(i) + ' ' for i in range(N)))
p = symbols(''.join('p'+str(i) + ' ' for i in range(N)))
m = [(0, 0.20), (1, 0.50), (2, 0.45), ( 3, 0.85), (4, 0.80), (5, -0.75), (6, 0.25), (7, 0.20), (8, 0.55)]
q_solved_values = [-0.0834, 0.1505, 0.5719, -0.7055, -0.0091, -0.2784, 0.2277, 0.1263]


q_solved = {
    q[0]: -0.0834, 
    q[1]: 0.1505,
    q[2]: 0.5719, 
    q[3]: -0.7055, 
    q[4]: -0.0091, 
    q[5]: -0.2784, 
    q[6]: 0.2277, 
    q[7]: 0.1263
}

# el vector P a partir de la solución de q
def get_p_from_q(q, N):
    p = [0 for i in range(N)]
    for k in range(N):
        p[N-1-k] = (((-1)**k)*q[k])
    # p = reversed(p)
    return p

p_ = get_p_from_q(q_solved_values, N)

# sistema de ecuaciones lineales de Ro
def Ro_(N, p):
    equations = []
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    matrix.append([1 for _ in range(N)])
    Ro = symbols(''.join('Ro'+str(i) + ' ' for i in range(N)))
    for x in range(N):
        eq = 0
        for k in range(N):
            if (2*x-k) >=0 and (2*x-k) <= N-1: 
                eq += p[k]*Ro[(2*x-k)]
                matrix[x][k] = p[k] if 2*x-k != x else p[k] - 1
            else:
                matrix[x][k] = 0
        equations.append(eq - Ro[x])
    eq = 0
    for i in range(N):
        eq += Ro[i]
    equations = equations[:len(equations)-1]
    equations.append(eq - 1)
    equations[0] = Ro[0]-Ro[-1]
    return equations, matrix[1:], Ro

# evaluaciones

equations_, matrix_, Ro = Ro_(N, p_)

# values_ = {Ro[0]:0, Ro[7]:0}
# equations_ = [ mc.evalf(subs=values_) for mc in equations_ ]

for eq in equations_:
    print(eq)
    
# intentando solución con numpy.linalg.solve

# sol = np.linalg.solve(matrix_, [0 for _ in range(N)]+[1],)
sol = np.linalg.solve(matrix_, [0 for _ in range(N)],)
print(sol)

# intentando solución con scypy.solvers.linsolve
sol = sp.solvers.linsolve(equations_, Ro)#[0 for _ in range(N)])
print(sol)

# intentando solución con sympy.solve
sol = solve(equations_, Ro)#[0 for _ in range(N)])
print(sol)
a = 0

# intentando con fsolve

# import scipy.optimize
# def fun(x):
#     values = {}
#     for var, val in zip(Ro, x[:-1]):
#         values[var] = val
#     vm_sol = [ mc.evalf(subs=values) for mc in equations_ ]
#     vm_sol.append(sum(x)-1)
#     return  vm_sol

# sol= scipy.optimize.fsolve(fun,[0,0,0,0,0,0,0,0,0])
# print (sol)


