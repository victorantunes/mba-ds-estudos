"""Figuras REAIS do cap. 14 (cluster), a partir dos dados da aula.
Uso: python tools/make_figures5.py <pasta com vestibular.xlsx e cartao_credito.csv>"""
import sys, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy as sch
from scipy.stats import zscore
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import make_figures as mf
from make_figures import save, C1, C2, C3, GR

pasta = sys.argv[1]


def vestibular():
    d = pd.read_excel(os.path.join(pasta, "vestibular.xlsx"))
    X = d.drop(columns="estudante")
    Z = sch.linkage(X, method="single", metric="euclidean")
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    sch.dendrogram(Z, labels=list(d.estudante), ax=ax, color_threshold=4.5, above_threshold_color=GR)
    ax.axhline(4.5, color=C2, ls="--", lw=1.2)
    ax.text(0.02, 4.65, "corte em 4,5 → 3 clusters", color=C2, fontsize=9, transform=ax.get_yaxis_transform())
    ax.set_ylabel("distância euclidiana")
    ax.set_title("Dendrograma (single linkage): 5 estudantes")
    save(fig, "14_dendrograma")


def cartao():
    d = pd.read_csv(os.path.join(pasta, "cartao_credito.csv"))
    X = d.drop(columns=["Sl_No", "Customer Key"]).apply(zscore, ddof=1)
    k = range(1, 11)
    w = [KMeans(n_clusters=i, init="random", random_state=100).fit(X).inertia_ for i in k]
    s = [silhouette_score(X, KMeans(n_clusters=i, init="random", random_state=100).fit(X).labels_) for i in range(2, 11)]
    fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
    ax[0].plot(list(k), w, "-o", color=C1); ax[0].axvline(3, color=C2, ls="--")
    ax[0].set_title("Cotovelo (WCSS)"); ax[0].set_xlabel("K"); ax[0].set_ylabel("WCSS (soma dos quadrados)")
    ax[1].plot(range(2, 11), s, "-o", color=C3); ax[1].axvline(3, color=C2, ls="--")
    ax[1].set_title("Silhueta média"); ax[1].set_xlabel("K"); ax[1].set_ylabel("silhueta média")
    fig.tight_layout()
    save(fig, "14_cotovelo_silhueta")
    print([round(v, 1) for v in w], [round(v, 3) for v in s])


if __name__ == "__main__":
    vestibular(); cartao()
