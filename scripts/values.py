from sympy import symbols

N = 8
q = symbols("".join("q" + str(i) + " " for i in range(N)))
p = symbols("".join("p" + str(i) + " " for i in range(N)))
q_bar = symbols("".join("q_bar" + str(i) + " " for i in range(N)))
p_bar = symbols("".join("p_bar" + str(i) + " " for i in range(N)))
gamma = symbols("".join("gamma" + str(i) + " " for i in range(N)))
theta = symbols("".join("theta" + str(i) + " " for i in range(N)))


m = [0.20, 0.50, 0.45, 0.85, 0.80, -0.75, 0.25, 0.20, 0.55]

q_values = {
    q[0]: -0.0834,
    q[1]: 0.1505,
    q[2]: 0.5719,
    q[3]: -0.7055,
    q[4]: -0.0091,
    q[5]: -0.2784,
    q[6]: 0.2277,
    q[7]: 0.1263,
}
p_values = {
    p[0]: -0.1263,
    p[1]: 0.2277,
    p[2]: 0.2784,
    p[3]: 0.0091,
    p[4]: 0.7055,
    p[5]: 0.5719,
    p[6]: -0.1505,
    p[7]: -0.0834,
}
q_bar_values = {
    q_bar[0]: 0.0834,
    q_bar[1]: 0.1505,
    q_bar[2]: -0.5719,
    q_bar[3]: -0.7055,
    q_bar[4]: 0.0091,
    q_bar[5]: -0.2784,
    q_bar[6]: -0.2277,
    q_bar[7]: 0.1263,
}
p_bar_values = {
    p_bar[0]: -0.0834,
    p_bar[1]: -0.1505,
    p_bar[2]: 0.5719,
    p_bar[3]: 0.7055,
    p_bar[4]: -0.0091,
    p_bar[5]: 0.2784,
    p_bar[6]: 0.2277,
    p_bar[7]: -0.1263,
}
gamma_values = {
    gamma[0]: -0.0834,
    gamma[1]: 0.1505,
    gamma[2]: 0.5719,
    gamma[3]: -0.7055,
    gamma[4]: -0.0091,
    gamma[5]: 0.2784,
    gamma[6]: 0.2277,
    gamma[7]: 0.1263,
}
theta_values = {
    theta[0]: -0.0834,
    theta[1]: 0.1505,
    theta[2]: 0.5719,
    theta[3]: -0.7055,
    theta[4]: -0.0091,
    theta[5]: 0.2784,
    theta[6]: 0.2277,
    theta[7]: 0.1263,
}
