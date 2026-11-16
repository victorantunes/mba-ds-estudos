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


# (os gráficos do cap. 22 agora vêm da série e da simulação da aula: tools/make_figures8.py)


ALL = {k[1:]: v for k, v in list(globals().items()) if k.startswith("f") and k[1:3].isdigit() and callable(v)}
if __name__ == "__main__":
    for n, f in ALL.items():
        f()
