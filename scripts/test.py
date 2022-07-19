# from os import MFD_HUGE_1GB
# from sympy import symbols, solve
# import sympy as sp
# import numpy as np
# from values import q_solved_by_guido_values

# def get_p_from_q(q, N):
#     p = [0 for i in range(N)]
#     for k in range(N):
#         p[N-1-k] = (((-1)**k)*q[k])
#     # p = reversed(p)
#     return p

# def Ro_(N, p):
#     equations = []
#     matrix = [[0 for _ in range(N)] for _ in range(N)]
#     matrix.append([1 for _ in range(N)])
#     Ro = symbols(''.join('Ro'+str(i) + ' ' for i in range(N)))
#     for x in range(N):
#         eq = 0
#         for k in range(N):
#             if (2*x-k) >=0 and (2*x-k) <= N-1: 
#                 eq += p[k]*Ro[(2*x-k)]
#                 matrix[x][(2*x-k)] = p[k] if 2*x-k != x else p[k] - 1
#                 # matrix[x][k] = p[k] if 2*x-k != x else p[k] - 1
#             else:
#                 matrix[x][k] = 0
#         equations.append(eq - Ro[x])
#     eq = 0
#     for i in range(N):
#         eq += Ro[i]
#     # equations = equations[:len(equations)-1]
#     equations.append(eq - 1)
#     for i, row in enumerate(matrix):
#         if row[0] != 0:
#             a = equations[i]
#             b = row[0]*Ro[0]
#             c = equations[i] - row[0]*Ro[0]
#             equations[i] = c
#         if row[-1] != 0:
#             equations[i] -= row[-1]*Ro[-1]

#     # equations[0] = Ro[0]-Ro[-1]
#     return equations[1:-1], matrix, Ro

# N = 8
# q = symbols(''.join('q'+str(i) + ' ' for i in range(N)))
# p = symbols(''.join('p'+str(i) + ' ' for i in range(N)))
# m = [(0, 0.20), (1, 0.50), (2, 0.45), ( 3, 0.85), (4, 0.80), (5, -0.75), (6, 0.25), (7, 0.20), (8, 0.55)]

# p_ = get_p_from_q(q_solved_by_guido_values, N)
# equations_, matrix_, Ro = Ro_(N, p_)

# for eq in equations_:
#     print(eq)
# # sol = np.linalg.solve(matrix_, [0 for _ in range(N)]+[1],)
# # sol = np.linalg.lstsq(matrix_, [0 for _ in range(N)],)
# # print(sol)
# sol = sp.solvers.linsolve(equations_, Ro[1:-1])#[0 for _ in range(N)])
# print(sol)
# sol = solve(equations_, Ro)#[0 for _ in range(N)])
# print(sol)
# a = 0

p = [1,2,3,4,5]
N = 5
p_bar = [0 for _ in range(N)]
for k in range(N):
    p_bar[N-1-k] = p[k]
print(p_bar)
