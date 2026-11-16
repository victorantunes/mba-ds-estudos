"""Figuras REAIS do cap. 18 (logística), a partir do banco 'atrasado.csv' da aula.
Uso: python tools/make_figures7.py <caminho do atrasado.csv>"""
import sys
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score
import make_figures as mf
from make_figures import save, C1, C2, C3, GR

d = pd.read_csv(sys.argv[1])
m = sm.Logit.from_formula("atrasado ~ dist + sem", d).fit(disp=0)
d["z"] = m.fittedvalues
d["p"] = m.predict(d)


def sigmoide():
    z = np.linspace(-9, 9, 300)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(z, 1 / (1 + np.exp(-z)), color=C1, lw=2)
    ax.axhline(0.5, color=GR, ls="--", lw=1); ax.axvline(0, color=GR, ls="--", lw=1)
    ax.scatter(d.z, d.atrasado, s=14, color=C3, alpha=.5, zorder=2, label="estudantes (0 ou 1)")
    zx = -26.1665 + 0.1904 * 20 + 2.3629 * 10
    ax.scatter([zx], [1 / (1 + np.exp(-zx))], color=C2, zorder=4, s=50)
    ax.annotate("20 km e 10 semáforos:\nZ = 1,27 → p = 0,78", (zx, 1 / (1 + np.exp(-zx))), xytext=(2.5, 0.28), color=C2, fontsize=9,
                arrowprops=dict(arrowstyle="-", color=C2))
    ax.set_xlabel("logito Z estimado"); ax.set_ylabel("probabilidade de atraso")
    ax.set_title("A sigmoide transforma o logito em probabilidade")
    ax.legend(frameon=False, loc="upper left", fontsize=8)
    save(fig, "18_sigmoide")


def roc():
    fpr, tpr, thr = roc_curve(d.atrasado, d.p)
    auc = roc_auc_score(d.atrasado, d.p)
    fig, ax = plt.subplots(figsize=(4.8, 4.4))
    ax.plot(fpr, tpr, color=C1, label="modelo (AUC = %s)" % f"{auc:.2f}".replace(".", ","))
    ax.plot([0, 1], [0, 1], color=GR, ls="--", label="aleatório (AUC = 0,5)")
    for c in (0.3, 0.5, 0.7):
        pr = d.p >= c
        s = (pr & (d.atrasado == 1)).sum() / (d.atrasado == 1).sum()
        e = (~pr & (d.atrasado == 0)).sum() / (d.atrasado == 0).sum()
        ax.scatter([1 - e], [s], color=C2, zorder=3)
        ax.annotate("cutoff %s" % str(c).replace(".", ","), (1 - e, s), xytext=(6, -12), textcoords="offset points", fontsize=8, color=C2)
    ax.set_xlabel("1 − especificidade"); ax.set_ylabel("sensibilidade")
    ax.legend(frameon=False, loc="lower right", fontsize=8)
    ax.set_title("Curva ROC do modelo de atrasos")
    save(fig, "18_roc")


if __name__ == "__main__":
    sigmoide(); roc()
