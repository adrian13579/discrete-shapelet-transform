from .filters import (
    get_q_filter_equations,
    get_filters,
    system_function,
    compute_abs_error,
    get_q_filter
)

import pywt
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import root

MAXITER = 5000


def build_shapelet(pattern, numeric_method="lm", verbose=False):
    q_symbols, equations = get_q_filter_equations(pattern, verbose)
    fun = system_function(q_symbols, equations)

    opt = {"maxfev": MAXITER} if numeric_method == "hybr" else {"maxiter": MAXITER}
    sol = root(
        fun, [0 for _ in range(len(q_symbols))], method=numeric_method, options=opt
    )

    q = get_q_filter(sol.x)
    p, q_bar, p_bar = get_filters(q)
    # filter_bank = [p_bar, q_bar, p, q]
    filter_bank = [p, q, p_bar, q_bar, ]
    if verbose:
        print(f"solution: {sol.x}")
        print(f"success: {sol.success}")
        compute_abs_error(q_symbols, sol.x, equations)
        print(f"p_bar: {p_bar}")
        print(f"q_bar: {q_bar}")
        print(f"p: {p}")
        print(f"q: {q}")
    shapelet = pywt.Wavelet(name="Shapelet-II", filter_bank=filter_bank)

    if verbose:
        level = 2
        phi_d, psi_d, phi_r, psi_r, x = shapelet.wavefun(level)

        step = 2
        psi_x = [i for i in range(0, len(psi_d), step)]
        psi_d_ = [psi_d[i] for i in range(0, len(psi_d), step)]
        matplotlib.pyplot.figure(dpi=600)
        plt.plot(psi_x, psi_d_, "b-")
        plt.show()

        step = 2
        phi_x = [i for i in range(0, len(phi_d), step)]
        phi_d_ = [phi_d[i] for i in range(0, len(phi_d), step)]
        matplotlib.pyplot.figure(dpi=600)
        plt.plot(phi_x, phi_d_, "r-")
        plt.show()

    return shapelet
