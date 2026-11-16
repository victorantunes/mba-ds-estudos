"""Figuras do exemplo completo do cap. 15 (Atlas Ambiental de SP).
Uso: python tools/make_figures4.py <pasta com atlas_ambiental.xlsx e DEINFO_DISTRITO.*>
A PCA é feita com numpy (autodecomposição da matriz de correlações), equivalente a
FactorAnalyzer(method='principal', rotation=None) usado na aula."""
import sys, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import make_figures as mf
from make_figures import save, C1, C2, C3, GR

pasta = sys.argv[1]
atlas = pd.read_excel(os.path.join(pasta, "atlas_ambiental.xlsx"))
X = atlas.drop(columns=["cód_ibge", "distritos"])
R = X.corr().values
w, V = np.linalg.eigh(R)
o = np.argsort(w)[::-1]
w, V = w[o], V[:, o]
if V[X.columns.get_loc("renda"), 0] < 0:
    V[:, 0] *= -1
L = V[:, :2] * np.sqrt(w[:2])
Z = (X - X.mean()) / X.std(ddof=0)
F = Z.values @ (V[:, :2] / np.sqrt(w[:2]))
atlas["F1"], atlas["F2"] = F[:, 0], F[:, 1]
nomes = {"renda": "renda", "quota": "quota", "escolaridade": "escolaridade", "idade": "idade", "mortalidade": "mortalidade",
         "txcresc": "txcresc", "causasext": "causasext", "favel": "favel", "denspop": "denspop"}


def corr():
    fig, ax = plt.subplots(figsize=(6.4, 5.4))
    im = ax.imshow(X.corr().values, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(9)); ax.set_yticks(range(9))
    ax.set_xticklabels(X.columns, rotation=45, ha="right"); ax.set_yticklabels(X.columns)
    for i in range(9):
        for j in range(9):
            v = X.corr().values[i, j]
            ax.text(j, i, f"{v:.2f}".replace(".", ","), ha="center", va="center", fontsize=7.5, color="white" if abs(v) > .6 else "black")
    ax.spines[:].set_visible(False)
    fig.colorbar(im, shrink=.8)
    ax.set_title("Matriz de correlações de Pearson (96 distritos)")
    save(fig, "15_atlas_corr")


def autov():
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    cores = [C1 if v > 1 else "#c4ccd8" for v in w]
    ax.bar(range(1, 10), w, color=cores)
    ax.axhline(1, color=C2, ls="--", lw=1.2)
    ax.text(9.4, 1.08, "Kaiser: λ = 1", color=C2, ha="right", fontsize=9)
    for i, v in enumerate(w, 1):
        ax.text(i, v + .08, f"{v:.2f}".replace(".", ","), ha="center", fontsize=8.5)
    ax.set_xticks(range(1, 10)); ax.set_xlabel("Fator"); ax.set_ylabel("Autovalor")
    ax.set_title("Autovalores: só dois passam de 1")
    save(fig, "15_atlas_autovalores")


def loadings():
    fig, ax = plt.subplots(figsize=(6, 5.2))
    ax.axhline(0, color=GR, ls="--", lw=.8); ax.axvline(0, color=GR, ls="--", lw=.8)
    ax.scatter(L[:, 0], L[:, 1], color=C2, s=40, zorder=3)
    for n, (x, y) in zip(X.columns, L):
        ax.annotate(n, (x, y), xytext=(5, 4), textcoords="offset points", fontsize=9)
    ax.set_xlim(-1.1, 1.2); ax.set_ylim(-1.1, 1.1)
    ax.set_xlabel("Fator 1 (55,07% da variância)"); ax.set_ylabel("Fator 2 (12,94% da variância)")
    ax.set_title("Loading plot: cargas = correlações com os fatores")
    save(fig, "15_atlas_loadings")


def ranking():
    d = atlas[["distritos", "F1"]].sort_values("F1")
    sel = pd.concat([d.head(8), d.tail(8)])
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    ax.barh(sel["distritos"], sel["F1"], color=[C2 if v < 0 else C1 for v in sel["F1"]])
    ax.axvline(0, color="black", lw=.8)
    ax.set_xlabel("Fator 1 (indicador socioeconômico)")
    ax.set_title("Os 8 distritos mais baixos e os 8 mais altos no Fator 1")
    save(fig, "15_atlas_ranking")


def mapa():
    import shapefile as shp
    sf = shp.Reader(os.path.join(pasta, "DEINFO_DISTRITO"))
    campos = [x[0] for x in sf.fields][1:]
    dist = pd.DataFrame(columns=campos, data=[r[:] for r in sf.records()])
    dist["coords"] = [s.points for s in sf.shapes()]
    dist["COD_DIST"] = pd.to_numeric(dist["COD_DIST"])
    dist = dist.sort_values("COD_DIST").reset_index(drop=True)
    d = atlas.sort_values("cód_ibge").reset_index(drop=True)
    faixas = pd.qcut(d["F1"], 6, labels=False)
    paleta = plt.get_cmap("YlOrBr")(np.linspace(.12, .95, 6))
    fig, ax = plt.subplots(figsize=(5.6, 7))
    for i, pts in enumerate(dist.coords):
        x = [p[0] for p in pts]; y = [p[1] for p in pts]
        ax.fill(x, y, color=paleta[faixas[i]], lw=0)
        ax.plot(x, y, color="black", lw=.4)
    ax.axis("off"); ax.set_aspect("equal")
    ax.set_title("Indicador socioeconômico (Fator 1) por distrito, em 6 faixas")
    save(fig, "15_atlas_mapa")


if __name__ == "__main__":
    corr(); autov(); loadings(); ranking(); mapa()
