"""Figuras REAIS do cap. 16 (ANACOR e ACM), a partir dos dados da aula.
Uso: python tools/make_figures6.py <pasta com perfil_aplicacao.xlsx e perfil_aplicacao_civil.xlsx>"""
import sys, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import make_figures as mf
from make_figures import save, C1, C2, C3, GR

pasta = sys.argv[1]


def ca(P):
    r, c = P.sum(1), P.sum(0)
    S = (P - np.outer(r, c)) / np.sqrt(np.outer(r, c))
    U, s, Vt = np.linalg.svd(S, full_matrices=False)
    return r, c, U, s, Vt


def anacor():
    d = pd.read_excel(os.path.join(pasta, "perfil_aplicacao.xlsx"))
    t = pd.crosstab(d["Perfil"], d["Tipo de Aplicação"])
    P = t.values / t.values.sum()
    r, c, U, s, Vt = ca(P)
    R = (U / np.sqrt(r)[:, None]) * s
    C = (Vt.T / np.sqrt(c)[:, None]) * s
    fig, ax = plt.subplots(figsize=(6, 4.6))
    ax.axhline(0, color=GR, ls="--", lw=.8); ax.axvline(0, color=GR, ls="--", lw=.8)
    ax.scatter(R[:, 0], R[:, 1], color=C1, s=60, zorder=3, label="Perfil do investidor")
    ax.scatter(C[:, 0], C[:, 1], color=C2, s=60, marker="s", zorder=3, label="Tipo de aplicação")
    for n, (x, y) in zip(t.index, R[:, :2]):
        ax.annotate(n, (x, y), xytext=(6, 5), textcoords="offset points", color=C1, fontsize=10)
    for n, (x, y) in zip(t.columns, C[:, :2]):
        ax.annotate(n, (x, y), xytext=(6, 5), textcoords="offset points", color=C2, fontsize=10)
    i = s ** 2 / (s ** 2).sum()
    ax.set_xlabel("Dimensão 1 (%s%% da inércia)" % f"{100*i[0]:.1f}".replace(".", ","))
    ax.set_ylabel("Dimensão 2 (%s%%)" % f"{100*i[1]:.1f}".replace(".", ","))
    ax.set_title("Mapa perceptual: perfil × tipo de aplicação")
    ax.legend(loc="lower left", fontsize=8, frameon=False)
    save(fig, "16_anacor_mapa")


def acm():
    d = pd.read_excel(os.path.join(pasta, "perfil_aplicacao_civil.xlsx"))
    Z = pd.get_dummies(d[["perfil", "aplicacao", "estado.civil"]]).astype(float)
    P = Z.values / Z.values.sum()
    r, c, U, s, Vt = ca(P)
    C = (Vt.T / np.sqrt(c)[:, None]) * s
    inertia = s ** 2
    fig, ax = plt.subplots(1, 2, figsize=(9.4, 4.2), gridspec_kw={"width_ratios": [1, 1.3]})
    k = 5
    ax[0].bar(range(1, k + 1), inertia[:k], color=[C1 if v > inertia[:k].mean() else "#c4ccd8" for v in inertia[:k]])
    ax[0].axhline(inertia[:k].mean(), color=C2, ls="--", lw=1)
    ax[0].text(k + .4, inertia[:k].mean() + .015, "média = 0,333", color=C2, ha="right", fontsize=8.5)
    for i in range(k):
        ax[0].text(i + 1, inertia[i] + .01, f"{inertia[i]:.3f}".replace(".", ","), ha="center", fontsize=8.5)
    ax[0].set_xlabel("Dimensão"); ax[0].set_ylabel("Inércia principal (autovalor)")
    ax[0].set_title("5 dimensões = J − Q = 8 − 3")
    cols = [C1] * 3 + [C2] * 3 + [C3] * 2
    ax[1].axhline(0, color=GR, ls="--", lw=.8); ax[1].axvline(0, color=GR, ls="--", lw=.8)
    ax[1].scatter(C[:, 0], C[:, 1], c=cols, s=55, zorder=3)
    for n, (x, y), col in zip(Z.columns, C[:, :2], cols):
        ax[1].annotate(n.replace("_", ": ").replace("Acoes", "Ações").replace("Poupanca", "Poupança"), (x, y),
                       xytext=(5, 4), textcoords="offset points", fontsize=8, color=col)
    ax[1].set_xlim(-1.9, 1.6)
    ax[1].set_xlabel("Dimensão 1 (36,1% da inércia)"); ax[1].set_ylabel("Dimensão 2 (26,2%)")
    ax[1].set_title("Mapa perceptual da ACM")
    fig.tight_layout()
    save(fig, "16_acm_mapa")


if __name__ == "__main__":
    anacor(); acm()
