from sympy import symbols


def dirac_delta(l):
    return 0 if l != 0 else 1


def get_q_filter_equations(pattern, verbose=False):
    N = len(pattern) - 1
    if N < 6:
        raise Exception("The filter support size must be N>=6")

    if N % 2 != 0:
        raise Exception(
            "The signal to be match must be must have odd size and filter support size must be even "
        )

    q = symbols("".join("q" + str(i) + " " for i in range(N)))

    #  unitary energy equation
    unitary_energy = q[0] ** 2
    for i in range(1, N):
        unitary_energy += q[i] ** 2
    unitary_energy -= 1
    if verbose:
        print("Unitary Energy Equation:")
        print(unitary_energy)

    # vanishing moments equations
    vanishing_moments = []
    for b in range(int(N / 2 - 3) + 1):
        vm = 0
        for k in range(1, N):
            vm += q[k] * k**b
        vanishing_moments.append(vm)
    if verbose:
        print("Vanishing Moments Equations:")
        for vn in vanishing_moments:
            print(vn)

    # orthogonality equations
    orthogonality = []
    for l in range(1, int(N / 2 - 1) + 1):
        ot = 0
        for k in range(N - 2 * l):
            ot += q[k] * q[k + 2 * l]
            ot -= dirac_delta(l)
        orthogonality.append(ot)
    if verbose:
        print("Orthogonality Equations:")
        for ot in orthogonality:
            print(ot)

    # matching conditions
    matching_cond_1 = 0
    for k in range(1, N + 1):
        matching_cond_1 += q[(N - k) % N] * pattern[k - 1]

    matching_cond_2 = 0
    for k in range(1, N + 1):
        matching_cond_2 += q[(N - k) % N] * pattern[k]

    # matching_cond_1 = 0
    # for k in range(1, N + 1):
    #     matching_cond_1 += q[k % N] * pattern[k - 1]

    # matching_cond_2 = 0
    # for k in range(1, N + 1):
    #     matching_cond_2 += q[k % N] * pattern[k]

    # Original DST-II matching conditions
    # matching_cond_1 = 0
    # for k in range(0, N):
    #     matching_cond_1 += q[k % N] * pattern[k]

    # matching_cond_2 = 0
    # for k in range(0, N ):
    #     matching_cond_2 += q[k % N] * pattern[k+1]
    if verbose:
        print("Matching Condition Equations:")
        print(matching_cond_1)
        print(matching_cond_2)

    equations = (
        [unitary_energy]
        + vanishing_moments
        + orthogonality
        + [matching_cond_1, matching_cond_2]
    )

    return q, equations


def compute_abs_error(q, q_values, equations, verbose=True):
    error = 0
    values = {}
    for var, val in zip(q, q_values):
        values[var] = val

    for eq in equations:
        print(eq.evalf(subs=values))
        error += abs(eq.evalf(subs=values))
    if verbose:
        print(f"Absolute Error: {error}")
    return error


def system_function(q, equations):
    def fun(x):
        values = {}
        for var, val in zip(q, x):
            values[var] = val
        return [eq.evalf(subs=values) for eq in equations]

    return fun


def get_q_filter(q):
    N = len(q)
    return [q[k] for k in range(N)]


def get_p_filter(q):
    N = len(q)
    return [(((-1) ** (k + 1)) * q[N - 1 - k]) for k in range(N)]


def get_p_bar_filter(p):
    N = len(p)
    return [p[(N - k) % N] for k in range(N)]


def get_q_bar_filter(q):
    # N = len(q)
    # return [q[(N - k) % N] for k in range(N)]
    N = len(q)
    return [(-1)**( (k+1) % N)*q[k] for k in range(N)]


def get_filters(q):
    p = get_p_filter(q)
    p_bar = get_p_bar_filter(p)
    q_bar = get_q_bar_filter(q)
    return p, q_bar, p_bar
