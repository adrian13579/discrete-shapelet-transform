from sympy import symbols
from scipy.optimize import fsolve 

# ejemplo del paper
N = 8
q = symbols(''.join('q'+str(i) + ' ' for i in range(N)))
p = symbols(''.join('p'+str(i) + ' ' for i in range(N)))
m = [(0, 0.20), (1, 0.50), (2, 0.45), ( 3, 0.85), (4, 0.80), (5, -0.75), (6, 0.25), (7, 0.20), (8, 0.55)]

q_values = { q[0]: -1*0.0834, q[1]: 0.1505, q[2]:0.5719,q[3]: -1* 0.7055,q[4]: -1*0.0091,
q[5]:0.2784, q[6]:-1*0.2277,q[7]: 0.1263 }

q_values = {q[0]:-0.07245596 , q[1]: 0.14279704, q[2]: 0.50013281, q[3]: -0.69941235, q[4]: -0.06124007, q[5]: -0.33979503, q[6]:0.30351335, q[7]: 0.15400424}

# ecuación de energía unitaria
unitary_energy = q[0]**2
for i in range(1, N):
    unitary_energy += q[i]**2
unitary_energy -= 1
print(unitary_energy)
print(unitary_energy.evalf(subs=q_values))

# ecuación de vanish moments
vanish_moments = []
for b in range(int(N/2 - 3)+1):
    vm = 0
    for k in range(1,N):
        vm += q[k]*k**b
    vanish_moments.append(vm)
for vm in vanish_moments:
    print(vm.evalf(subs=q_values))
    print(vm)

# 
def Dirac_delta(l):
    return 0 if l != 0 else 1

# ecuación de ortogonalidad
orthogonality = []
for l in range(1, int(N/2 -1)+1): 
    ot = 0
    for k in range(N - 2 * l):
        ot += q[k]*q[k+2*l]
        ot -= Dirac_delta(l)
    orthogonality.append(ot)

for ot in orthogonality:
    print(ot.evalf(subs=q_values))
    print(ot)

# ecuaciones de matching
def matching_conditions(m, N, q):
    matching_1 = 0
    for k in range(N):
        matching_1 += q[k]*m[k][1]
    
    matching_2 = 0
    for k in range(N):
        matching_2 += q[k]*m[k+1][1]
    
    return matching_1, matching_2

matching_1, matching_2 = matching_conditions(m, N, q)

print(matching_1.evalf(subs=q_values))
print(matching_1)


print(matching_2.evalf(subs=q_values))
print(matching_2)

# evaluaciones de prueba
import scipy.optimize
def fun(x):
    values = {}
    for var, val in zip(q, x):
        values[var] = val
    ue_sol = [unitary_energy.evalf(subs=values)]
    vm_sol = [ vm.evalf(subs=values) for vm in vanish_moments]
    ot_sol = [ ot.evalf(subs=values) for ot in orthogonality ]
    mc_sol = [ mc.evalf(subs=values) for mc in [matching_1,matching_2] ]
    return  ue_sol + vm_sol + ot_sol + mc_sol

x= scipy.optimize.fsolve(fun,[0,0,0,0,0,0,0,0])
print (x)

x= scipy.optimize.newton(fun,[0,0,0,0,0,0,0,0])
print(x)

