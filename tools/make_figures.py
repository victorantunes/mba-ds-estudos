"""Gera as figuras didáticas em docs/img/. Uso: python tools/make_figures.py [nome ...]"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "img")
os.makedirs(OUT, exist_ok=True)
C1, C2, C3, GR = "#2f5bea", "#d9480f", "#12805c", "#667085"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": False, "figure.dpi": 130, "savefig.bbox": "tight"})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name + ".png"), facecolor="white")
    plt.close(fig)
    print("ok", name)


def f01_normal():
    x = np.linspace(-4, 4, 400)
    y = stats.norm.pdf(x)
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.plot(x, y, color="black", lw=1.6)
    for k, col, lab in [(3, "#cfd8ff", "99,7%"), (2, "#9db4ff", "95%"), (1, C1, "68%")]:
        m = (x >= -k) & (x <= k)
        ax.fill_between(x[m], y[m], color=col, alpha=.85 if k == 1 else .6)
    for k, lab in [(1, "68%"), (2, "95%"), (3, "99,7%")]:
        ax.annotate(lab, (0, 0), xytext=(0, 0.12 - 0.035 * (k - 1)), ha="center", color="white" if k == 1 else "black", fontsize=10)
    ax.set_xticks(range(-3, 4))
    ax.set_xticklabels(["−3σ", "−2σ", "−1σ", "μ", "+1σ", "+2σ", "+3σ"])
    ax.set_yticks([])
    ax.set_title("Distribuição normal e a regra empírica")
    save(fig, "01_normal")


def f01_assimetria():
    rng = np.random.default_rng(3)
    d = rng.lognormal(mean=1.0, sigma=0.55, size=4000)
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.hist(d, bins=60, color="#9db4ff", edgecolor="white")
    ax.axvline(np.median(d), color=C3, lw=2, label="mediana")
    ax.axvline(d.mean(), color=C2, lw=2, label="média")
    ax.legend(frameon=False)
    ax.set_yticks([])
    ax.set_title("Cauda à direita: a média (laranja) é puxada para além da mediana (verde)")
    save(fig, "01_assimetria")


def f01_teste_t():
    df = 24
    x = np.linspace(-4.5, 4.5, 500)
    y = stats.t.pdf(x, df)
    c5, c1 = stats.t.ppf(0.05, df), stats.t.ppf(0.01, df)
    fig, ax = plt.subplots(figsize=(7, 3.4))
    ax.plot(x, y, color="black", lw=1.5)
    ax.fill_between(x[x <= c5], y[x <= c5], color="#f4b183", alpha=.7)
    ax.fill_between(x[x <= c1], y[x <= c1], color=C2, alpha=.8)
    ax.axvline(-2.181, color=C1, lw=2)
    ax.text(-2.1, 0.30, "t calculado = −2,181\n(p unicaudal = 0,0196)", color=C1, ha="left", fontsize=9)
    ax.text(c5 - .05, 0.12, "crítico 5%\n−1,711", color=C2, ha="right", fontsize=8.5)
    ax.text(c1 - .05, 0.03, "crítico 1%\n−2,492", color=C2, ha="right", fontsize=8.5)
    ax.text(1.2, 0.18, "não rejeita H0", ha="center", color=GR)
    ax.set_yticks([])
    ax.set_title("Teste t unicaudal (24 gl): rejeita a 5%, mas não a 1%")
    save(fig, "01_teste_t")


ALL = {k[1:]: v for k, v in globals().items() if k.startswith("f") and callable(v) and k[1:3].isdigit()}

if __name__ == "__main__":
    names = sys.argv[1:] or list(ALL)
    for n in names:
        ALL[n]()
