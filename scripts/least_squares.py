from sympy import symbols, solve
import sympy as sp
import numpy as np
from segundo_sistema import get_p_from_q
import matplotlib.pyplot as plt

# ejemplo del paper

N = 8

q_solved_values = [-0.0834, 0.1505, 0.5719, -0.7055, -0.0091, -0.2784, 0.2277, 0.1263]
Ro_2 = symbols(''.join('Ro'+str(i*2+1) + '_2 ' for i in range(N-1)))
p_ = get_p_from_q(q_solved_values, N)
Sig_2 = symbols(''.join('Sig'+str(i*2+1) + '_2 ' for i in range(N)))

# sistema de ecuaciones lineales de Ro
def Ro_(N, p):
    equations = []
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    # matrix.append([1 for _ in range(N)])
    Ro = symbols(''.join('Ro'+str(i) + ' ' for i in range(N)))
    ros = []
    for x in range(N):
        eq = 0
        ros_ = []
        for k in range(N):
            if (2*x-k) >= 0 and (2*x-k) <= N-1: 
                eq += p[k]*Ro[(2*x-k)]
                ros_.append((2*x-k))
                # matrix[x][k] = p[k] if 2*x-k != x else p[k] - 1
                if (2*x-k) != 0 and (2*x-k) != N-1:
                    matrix[x][k] = p[k] if 2*x-k != x else p[k] - 1
            # else:
            #     matrix[x][k] = 0
        equations.append(eq - Ro[x])
        ros.append(ros_)
    eq = 0
    matrix = matrix[1:]
    matrix1 = matrix
    for i in range(len(matrix)):
        if i < len(matrix)/2:
            matrix1[i] = matrix[i][:len(matrix[i])-2]
        else:
            matrix1[i] = matrix[i][2:]
    for i in range(len(matrix1[0])):
        matrix1[-1][i] = 1
    for i in range(N):
        eq += Ro[i]
    equations = equations[:len(equations)-1]+[eq - 1]
    # equations.append(eq - 1)
    equations[0] = Ro[0]-Ro[-1]
    
    return equations, matrix1, Ro, ros

def Ro_2_(N, p, Ro_2, Ro, Ro_vals):
    dic_eval = {}
    equations = []
    for x in range(N-1):
        mid_eq = 0
        mid_ro = 0
        for k in range(N):
            if ((2*x+1)-k) >= 0 and ((2*x+1)-k) <= N-1: 
                mid_eq += p[k]*Ro[(2*x+1)-k]
                mid_ro += p[k]*Ro_vals[(2*x+1)-k]
        
        equations.append(mid_eq)
        dic_eval[Ro_2[x]] = mid_ro
    return equations, dic_eval

# evaluaciones

equations_, matrix_, Ro, ros = Ro_(N, p_)
ros = ros[1:-1]
_matrix = []
for i, eq in enumerate(equations_[1:-1]):
    row = [0 for _ in range(len(Ro))]
    for j in ros[i]:
        if j == 0 or j == len(Ro)-1:
            continue
        eval_array = [1 if j == k else 0 for k in range(len(Ro))]
        dic_eval = {}
        for k, ro in enumerate(Ro):
            dic_eval[ro] = eval_array[k]
        row[j] = float(eq.evalf(subs=dic_eval))
    _matrix.append(row[1:-1])
_matrix.append([1 for i in range(len(Ro)-2)])
# _matrix.append([1 for _ in range(len(Ro)-2)])



print('------------our solution----------------')
_sol = np.linalg.lstsq(_matrix, [0,0,0,0,0,0,1], rcond=None)
sol = _sol[0]
sol = [sol[i] for i in range(N-2)]
sol = [0]+sol+[0]
sol_eval = {}
for i, ro in enumerate(Ro):
    sol_eval[ro] = sol[i]

ro_2_equations, ro_2_sol_eval = Ro_2_(N, p_, Ro_2, Ro, sol)
sol_2 = [i for i in ro_2_sol_eval.values()]
sol_eval.update(ro_2_sol_eval)
print(sol_eval)
x = [i for i in range(len(sol_eval))]
x = np.arange(0, len(sol_eval)/2, 0.5)
y = []
i_1 = 0
i_2 = 0
for i in range(len(sol_eval)):
    if i%2 == 0:
        y.append(sol[i_1])
        i_1+=1
    else:
        y.append(sol_2[i_2])
        i_2+=1
plt.plot(x,y,'r-')
plt.show()
print('----------------------------------------')
for eq in equations_:
    print(eq.evalf(subs=sol_eval))

print('------------guido solution--------------')
guido_sol = [0, -9.483, 35.987, 12.157, -99.513, 68.523, -6.670, 0]
p_solved_by_guido = [-0.1263, 0.2277, 0.2784, -0.0091, 0.7055, 0.5719, -0.1505, -0.0834 ]
sol_eval = {}
for i, ro in enumerate(Ro):
    sol_eval[ro] = guido_sol[i]
    
ro_2_equations, ro_2_sol_eval = Ro_2_(N, p_solved_by_guido, Ro_2, Ro, guido_sol)
sol_eval.update(ro_2_sol_eval)
print(sol_eval)
print('----------------------------------------')
for eq in equations_:
    print(eq.evalf(subs=sol_eval))
# sol_eval = {}


# calculo de Sigma
def get_sigma(N, q, Ro, Ro_vals):
    Sig = symbols(''.join('Sig'+str(i) + ' ' for i in range(N)))
    equations = []
    dic_eval = {}
    for x in range(N):
        eq = 0
        value = 0
        for k in range(N):
            if (2*x-k) >= 0 and (2*x-k) <= N-1: 
                eq += q[k]*Ro[(2*x-k)]
                value += q[k]*Ro_vals[(2*x-k)]
        
        dic_eval[Sig[x]] = value
            # else:
            #     matrix[x][k] = 0
        equations.append(eq)
    return Sig, dic_eval, equations

def get_sigma_2(N, q, Sig_2, Ro, Ro_vals):
    dic_eval = {}
    equations = []
    for x in range(N-1):
        mid_sig = 0
        mid_sig = 0
        for k in range(N):
            if ((2*x+1)-k) >= 0 and ((2*x+1)-k) <= N-1: 
                mid_sig += q[k]*Ro[(2*x+1)-k]
                mid_sig += q[k]*Ro_vals[(2*x+1)-k]
        
        equations.append(mid_sig)
        dic_eval[Sig_2[x]] = mid_sig
    return equations, dic_eval

a = 0

# 