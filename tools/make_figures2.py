"""Figuras dos capítulos 14-22. Uso: python tools/make_figures2.py"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.cluster import hierarchy as sch
import make_figures as mf
from make_figures import save, C1, C2, C3, GR


# (os gráficos do cap. 14 agora vêm de dados reais: tools/make_figures5.py)


def f15_scree():
    ev = np.array([2.6, 1.1, 0.2, 0.1])
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.plot(range(1, 5), ev, "-o", color=C1)
    ax.axhline(1, color=C2, ls="--")
    ax.text(3.2, 1.08, "critério de Kaiser: λ > 1", color=C2)
    ax.set_xticks(range(1, 5)); ax.set_xlabel("fator"); ax.set_ylabel("autovalor")
    ax.set_title("Gráfico de autovalores: mantêm-se 2 fatores")
    save(fig, "15_autovalores")


def f17_regressao():
    x = np.array([1, 2, 3, 4, 5]); y = np.array([2, 4, 5, 4, 5])
    b, a = 0.6, 2.2
    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.scatter(x, y, color=C1, zorder=3, s=45)
    xs = np.linspace(0.7, 5.3, 10)
    ax.plot(xs, a + b * xs, color=C2, lw=2, label="Ŷ = 2,2 + 0,6·X")
    for xi, yi in zip(x, y):
        ax.plot([xi, xi], [yi, a + b * xi], color=GR, ls=":", lw=1.2)
    ax.axhline(4, color=C3, lw=1, ls="--", label="média de Y")
    ax.legend(frameon=False)
    ax.set_xlabel("X"); ax.set_ylabel("Y")
    ax.set_title("OLS: a reta minimiza a soma dos resíduos² (linhas pontilhadas)")
    save(fig, "17_regressao")


# (os gráficos do cap. 18 agora vêm de dados reais: tools/make_figures7.py)


def f22_decomposicao():
    t = np.arange(48)
    tend = 100 + 1.2 * t
    saz = 12 * np.sin(2 * np.pi * t / 12)
    rng = np.random.default_rng(5)
    ruido = rng.normal(0, 3, size=48)
    y = tend + saz + ruido
    fig, ax = plt.subplots(4, 1, figsize=(7, 6), sharex=True)
    for a, s, t_, c in zip(ax, [y, tend, saz, ruido], ["Série (Y)", "Tendência (T)", "Sazonalidade (S)", "Erro (E)"], [C1, C2, C3, GR]):
        a.plot(t, s, color=c); a.set_ylabel(t_, fontsize=9)
    ax[-1].set_xlabel("mês")
    fig.suptitle("Decomposição aditiva: Y = T + S + E", y=0.995)
    save(fig, "22_decomposicao")


def f22_acf_pacf():
    lags = np.arange(1, 11)
    ar_acf = 0.8 ** lags
    ar_pacf = np.array([0.8] + [0] * 9)
    ma_acf = np.array([0.6] + [0] * 9)
    ma_pacf = (-0.6) ** lags * 0.6 ** 0 * 0.55
    fig, ax = plt.subplots(2, 2, figsize=(8, 5))
    data = [("AR(1): ACF decai", ar_acf), ("AR(1): PACF corta no lag 1", ar_pacf), ("MA(1): ACF corta no lag 1", ma_acf), ("MA(1): PACF decai", ma_pacf)]
    for a, (tt, v) in zip(ax.ravel(), data):
        a.bar(lags, v, color=C1, width=.35); a.axhline(0, color="black", lw=.8)
        a.set_title(tt, fontsize=10); a.set_ylim(-1, 1)
    save(fig, "22_acf_pacf")


ALL = {k[1:]: v for k, v in list(globals().items()) if k.startswith("f") and k[1:3].isdigit() and callable(v)}
if __name__ == "__main__":
    for n, f in ALL.items():
        f()
