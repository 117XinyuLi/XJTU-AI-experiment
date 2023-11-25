import math
import matplotlib.pyplot as plt

# 不确定性的传递算法


def LS(P_E_given_H, P_E_given_notH):
    return P_E_given_H / P_E_given_notH


def LN(P_E_given_H, P_E_given_notH):
    return (1 - P_E_given_H) / (1 - P_E_given_notH)


def P_H_given_E(P_H, P_S_given_H, P_S_given_notH):
    ls = LS(P_S_given_H, P_S_given_notH)
    return ls * P_H / ((ls - 1) * P_H + 1)


def P_H_given_notE(P_H, P_S_given_H, P_S_given_notH):
    ln = LN(P_S_given_H, P_S_given_notH)
    return ln * P_H / ((ln - 1) * P_H + 1)


def P_H_given_S(P_E_given_S, P_H, P_E, P_E_given_H, P_E_given_notH):
    if P_E_given_S < 0 or P_E_given_S > 1:
        raise Exception("P_E_given_S should be in [0, 1]")
    p_h_given_e = P_H_given_E(P_H, P_E_given_H, P_E_given_notH)
    p_h_given_notE = P_H_given_notE(P_H, P_E_given_H, P_E_given_notH)
    if P_E_given_S <= P_E:
        return p_h_given_notE + ((P_H - p_h_given_notE)/P_E * P_E_given_S)
    else:
        return P_H + ((p_h_given_e - P_H)/(1-P_E) * (P_E_given_S - P_E))


def P_H_given_S_using_C_E_given_S(C_E_given_S, P_H, P_E, P_E_given_H, P_E_given_notH):
    if C_E_given_S < -5 or C_E_given_S > 5:
        raise Exception("C_E_given_S should be in [-5, 5]")
    p_h_given_e = P_H_given_E(P_H, P_E_given_H, P_E_given_notH)
    p_h_given_notE = P_H_given_notE(P_H, P_E_given_H, P_E_given_notH)
    if C_E_given_S <= 0:
        return p_h_given_notE + ((P_H - p_h_given_notE) * (1/5 * C_E_given_S + 1))
    else:
        return P_H + ((p_h_given_e - P_H) * (1/5 * C_E_given_S))


def draw_linear_interpolation_function(P_H, P_E, P_E_given_H, P_E_given_notH):
    x = []
    y = []
    p_h_given_e = P_H_given_E(P_H, P_E_given_H, P_E_given_notH)
    p_h_given_notE = P_H_given_notE(P_H, P_E_given_H, P_E_given_notH)
    for i in range(0, 101):
        x.append(i/100)
        y.append(P_H_given_S(i/100, P_H, P_E, P_E_given_H, P_E_given_notH))
    plt.plot(x, y, 'r-', linewidth=2)

    plt.plot([P_E, P_E], [0, P_H], 'b--')
    plt.plot([0, P_E], [P_H, P_H], 'b--')
    plt.plot([1, 1], [0, p_h_given_e], 'b--')
    plt.plot([0, 1], [p_h_given_e, p_h_given_e], 'b--')

    plt.text(P_E + 0.005, 0.005, "P(E)", ha='left', va='bottom', fontsize=10)
    plt.text(0.005, P_H - 0.005, "P(H)", ha='left', va='top', fontsize=10)

    plt.text(0.005, p_h_given_notE - 0.005, "P(H|~E)", ha='left', va='top', fontsize=10)
    plt.text(0.005, p_h_given_e - 0.005, "P(H|E)", ha='left', va='top', fontsize=10)

    plt.xlabel("P(E|S)")
    plt.ylabel("P(H|S)")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.title("Piecewise linear interpolation of EH formula")
    plt.show()


def get_P_E_given_S_using_C_E_given_S(C_E_given_S, P_E):
    if C_E_given_S < -5 or C_E_given_S > 5:
        raise Exception("C_E_given_S should be in [-5, 5]")
    if C_E_given_S >= 0:
        return (C_E_given_S + P_E * (5-C_E_given_S))/5
    else:
        return (P_E * (C_E_given_S+5))/5


if __name__ == '__main__':
    P_H = 0.8
    P_E = 0.4
    P_E_given_H = 0.1
    P_E_given_notH = 0.8

    P_E_given_S = 0.5

    print(P_H_given_S(P_E_given_S, P_H, P_E, P_E_given_H, P_E_given_notH))

    draw_linear_interpolation_function(P_H, P_E, P_E_given_H, P_E_given_notH)




