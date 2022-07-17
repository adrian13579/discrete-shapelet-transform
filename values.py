from sympy import symbols, solve
import sympy as sp
import numpy as np

N = 8
q = symbols(''.join('q'+str(i) + ' ' for i in range(N)))
p = symbols(''.join('p'+str(i) + ' ' for i in range(N)))
q_ = symbols(''.join('q_'+str(i) + ' ' for i in range(N)))
p_ = symbols(''.join('p_'+str(i) + ' ' for i in range(N)))
ro = symbols(''.join('ro'+str(i) + ' ' for i in range(N)))
sigma = symbols(''.join('sigma'+str(i) + ' ' for i in range(N)))
m = [(0, 0.20), (1, 0.50), (2, 0.45), ( 3, 0.85), (4, 0.80), (5, -0.75), (6, 0.25), (7, 0.20), (8, 0.55)]


q_solved_by_guido = {
    q[0]: -0.0834, 
    q[1]: 0.1505,
    q[2]: 0.5719, 
    q[3]: -0.7055, 
    q[4]: -0.0091, 
    q[5]: -0.2784, 
    q[6]: 0.2277, 
    q[7]: 0.1263
}
q_solved_by_guido_values = [-0.0834, 0.1505, 0.5719, -0.7055, -0.0091, -0.2784, 0.2277, 0.1263]
p_solved_by_guido = {
    p[0]: -0.1263, 
    p[1]: 0.2277,
    p[2]: 0.2784, 
    p[3]: 0.0091, 
    p[4]: 0.7055, 
    p[5]: 0.2784, 
    p[6]: 0.2277, 
    p[7]: 0.1263
}
q_barra_solved_by_guido = {
    q_[0]: -0.0834, 
    q_[1]: 0.1505,
    q_[2]: 0.5719, 
    q_[3]: -0.7055, 
    q_[4]: -0.0091, 
    q_[5]: 0.2784, 
    q_[6]: 0.2277, 
    q_[7]: 0.1263
}
p_barra_solved_by_guido = {
    p_[0]: -0.0834, 
    p_[1]: 0.1505,
    p_[2]: 0.5719, 
    p_[3]: -0.7055, 
    p_[4]: -0.0091, 
    p_[5]: 0.2784, 
    p_[6]: 0.2277, 
    p_[7]: 0.1263
}
ro_solved_by_guido = {
    ro[0]: -0.0834, 
    ro[1]: 0.1505,
    ro[2]: 0.5719, 
    ro[3]: -0.7055, 
    ro[4]: -0.0091, 
    ro[5]: 0.2784, 
    ro[6]: 0.2277, 
    ro[7]: 0.1263
}
sigma_solved_by_guido = {
    sigma[0]: -0.0834, 
    sigma[1]: 0.1505,
    sigma[2]: 0.5719, 
    sigma[3]: -0.7055, 
    sigma[4]: -0.0091, 
    sigma[5]: 0.2784, 
    sigma[6]: 0.2277, 
    sigma[7]: 0.1263
}