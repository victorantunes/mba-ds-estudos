"""Figuras dos capítulos 26-28. Uso: python tools/make_figures3.py"""
import numpy as np
import matplotlib.pyplot as plt
import make_figures as mf
from make_figures import save, C1, C2, C3, GR


def f26_regiao():
    fig, ax = plt.subplots(figsize=(6.2, 4.6))
    L = np.linspace(0, 12, 200)
    ax.plot(L, 10 - L, color=C1, label="L + M ≤ 10")
    ax.plot(L, (40 - 6 * L) / 2, color=C3, label="6L + 2M ≥ 40")
    ax.axhline(3, color=GR, ls="--", lw=1, label="M ≥ 3")
    ax.axhline(7, color=GR, ls=":", lw=1, label="M ≤ 7")
    poly = np.array([[17 / 3, 3], [7, 3], [5, 5]])
    ax.fill(poly[:, 0], poly[:, 1], color="#9db4ff", alpha=.6, label="região factível")
    for q, ls in [(55, ":"), (63, ":"), (65, "-")]:
        ax.plot(L, (q - 6 * L) / 7, color=C2, ls=ls, lw=1.4 if q < 65 else 2, alpha=.9)
    ax.scatter(poly[:, 0], poly[:, 1], color=C2, zorder=3, s=26)
    ax.annotate("ótimo (5; 5)\nQ = 65", (5, 5), xytext=(1.0, 8.2), color=C2, arrowprops=dict(arrowstyle="->", color=C2))
    ax.annotate("(7; 3)\nQ = 63", (7, 3), xytext=(8.6, 1.4), color=C2, fontsize=9, arrowprops=dict(arrowstyle="->", color=C2))
    ax.annotate("(5,67; 3)\nQ = 55", (17 / 3, 3), xytext=(2.2, 1.0), color=C2, fontsize=9, arrowprops=dict(arrowstyle="->", color=C2))
    ax.set_xlim(0, 12); ax.set_ylim(0, 10)
    ax.set_xlabel("L (caixas leves)"); ax.set_ylabel("M (caixas mistas)")
    ax.legend(frameon=False, loc="upper right", fontsize=8)
    ax.set_title("Região factível e retas de Q = 6L + 7M (laranja)")
    save(fig, "26_regiao_factivel")

def f27_vies_variancia():
    rng = np.random.default_rng(2)
    x = np.sort(rng.uniform(0, 1, 18))
    y = np.sin(2 * np.pi * x) + rng.normal(0, .25, x.size)
    xs = np.linspace(0, 1, 300)
    fig, ax = plt.subplots(1, 3, figsize=(10, 3), sharey=True)
    for a, (deg, tt) in zip(ax, [(1, "Subajuste (viés alto)"), (3, "Equilíbrio"), (13, "Sobreajuste (variância alta)")]):
        a.scatter(x, y, color=C1, s=18)
        c = np.polyfit(x, y, deg)
        a.plot(xs, np.clip(np.polyval(c, xs), -2.5, 2.5), color=C2, lw=2)
        a.set_title(tt, fontsize=10); a.set_xticks([])
    save(fig, "27_vies_variancia")


def f28_ativacoes():
    z = np.linspace(-6, 6, 300)
    fig, ax = plt.subplots(1, 3, figsize=(10, 2.9))
    ax[0].plot(z, 1 / (1 + np.exp(-z)), color=C1); ax[0].set_title("Sigmoid: satura nas pontas")
    ax[1].plot(z, np.maximum(0, z), color=C2); ax[1].set_title("ReLU = max(0, z)")
    e = np.exp(np.array([2.0, 1.0, 3.5])); sm = e / e.sum()
    ax[2].bar(["2,0", "1,0", "3,5"], sm, color=C3); ax[2].set_title("Softmax: soma 1"); ax[2].set_xlabel("logits")
    for a in ax[:2]:
        a.axhline(0, color=GR, lw=.6); a.axvline(0, color=GR, lw=.6)
    save(fig, "28_ativacoes")


def f28_gradiente():
    w = np.linspace(-3, 3, 200)
    J = w ** 2
    fig, ax = plt.subplots(1, 3, figsize=(10, 2.9), sharey=True)
    def run(lr, n=8, w0=-2.6):
        ws = [w0]
        for _ in range(n):
            ws.append(ws[-1] - lr * 2 * ws[-1])
        return np.array(ws)
    for a, (lr, tt) in zip(ax, [(0.05, "LR pequeno: lento"), (0.4, "LR adequado"), (1.05, "LR grande: oscila e diverge")]):
        a.plot(w, J, color="black", lw=1)
        ws = run(lr)
        ws = np.clip(ws, -3, 3)
        a.plot(ws, ws ** 2, "-o", color=C2, ms=4)
        a.set_title(tt, fontsize=10); a.set_xlabel("peso w")
    ax[0].set_ylabel("loss J(w)")
    save(fig, "28_gradient_descent")


ALL = {k[1:]: v for k, v in list(globals().items()) if k.startswith("f") and k[1:3].isdigit() and callable(v)}
if __name__ == "__main__":
    for n, f in ALL.items():
        f()
