from sympy import symbols
from scipy.optimize import fsolve, newton


# Dirac delta function
def Dirac_delta(l):
    return 0 if l != 0 else 1

def get_filters(m, method = 'Powell', verbose = False):
    N = len(m)-1
    q = symbols(''.join('q'+str(i) + ' ' for i in range(N)))
    
    # ecuación de energía unitaria
    unitary_energy = q[0]**2
    for i in range(1, N):
        unitary_energy += q[i]**2
    unitary_energy -= 1
    
    # ecuación de vanish moments
    vanish_moments = []
    for b in range(int(N/2 - 3)+1):
        vm = 0
        for k in range(1,N):
            vm += q[k]*k**b
        vanish_moments.append(vm)
    
    # ecuación de ortogonalidad
    orthogonality = []
    for l in range(1, int(N/2 -1)+1): 
        ot = 0
        for k in range(N - 2 * l):
            ot += q[k]*q[k+2*l]
            ot -= Dirac_delta(l)
        orthogonality.append(ot)
    
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
    
    def fun(x):
        values = {}
        for var, val in zip(q, x):
            values[var] = val
        ue_sol = [unitary_energy.evalf(subs=values)]
        vm_sol = [ vm.evalf(subs=values) for vm in vanish_moments]
        ot_sol = [ ot.evalf(subs=values) for ot in orthogonality ]
        mc_sol = [ mc.evalf(subs=values) for mc in [matching_1,matching_2] ]
        return  ue_sol + vm_sol + ot_sol + mc_sol
    
    q_dic = {}
    
    ###########################################
    # The method to solve the non-linear system
    if method == 'Powell':
        q_values = fsolve(fun, [0 for _ in range(N)])
    # add the other 2 methods
    else: # Newton
        q_values = newton(fun, [0 for _ in range(N)])
    ###########################################

    for var, val in zip(q, q_values):
        q_dic[var] = val
    
    def get_p_from_q(q, N):
        # p = [0 for i in range(N)]
        # for k in range(N):
        #     p[k] = (((-1)**(k+1))*q[N-1-k])
        # return p
        return [(((-1)**(k+1))*q[N-1-k]) for k in range(len(q))]
    
    p = symbols(''.join('p'+str(i) + ' ' for i in range(N)))
    
    p_dic = {}
    
    p_values = get_p_from_q(q_values, N)

    for var, val in zip(p, p_values):
        p_dic[var] = val
    
    # getting p bar
    def get_p_bar(p, N):
        # p_bar = [0 for i in range(N)]
        # for k in range(N):
        #     p_bar[k] = p[N-1-k]
        # return p_bar
        return [p[N-1-k] for k in range(len(p))]

    p_bar = symbols(''.join('p_'+str(i) + ' ' for i in range(N)))
    
    p_bar_dic = {}

    p_bar_values = get_p_bar(p_values, N)
    
    for var, val in zip(p_bar, p_bar_values):
        p_bar_dic[var] = val
        
    # getting q bar
    def get_q_bar(p):
        return [(((-1)**(k+1))*val) for k, val in enumerate(p)]

    q_bar = symbols(''.join('q_'+str(i) + ' ' for i in range(N)))

    q_bar_dic = {}

    q_bar_values = get_q_bar(q_values)

    for var, val in zip(q_bar, q_bar_values):
        q_bar_dic[var] = val
    
    if verbose:
        # print('-----------------------------------------------------------')
        # print('                                                           ')
        print('----------------The Unitary Energy equation----------------')
        print(unitary_energy)
        print('---------------The evaluation of the results---------------')
        print(unitary_energy.evalf(subs=q_values))
        print('-----------------------------------------------------------')
        print('                                                           ')
        print('----------------The Vanish Moment equations----------------')
        for vm in vanish_moments:
            print(vm.evalf(subs=q_values))
            print('---------------The evaluation of the results---------------')
            print(vm)
        print('-----------------------------------------------------------')
        print('                                                           ')
        print('----------------The Orthogonality equations----------------')
        for ot in orthogonality:
            print(ot.evalf(subs=q_values))
            print('---------------The evaluation of the results---------------')
            print(ot)
        print('-----------------------------------------------------------')
        print('                                                           ')
        print('------------------The Matching equations------------------')
        print(matching_1)
        print('                                                           ')
        print(matching_2)
        print('---------------The evaluation of the results---------------')
        print(matching_1.evalf(subs=q_values))
        print('                                                           ')
        print(matching_2.evalf(subs=q_values))
        print('-----------------------------------------------------------')
    #    dec_low, dec_high, rec_low, rec_high
    return q_dic, p_dic, q_bar_dic, p_bar_dic
