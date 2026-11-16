"""Figuras do cap. 22 (séries temporais), com as séries usadas na aula.
- decomposição: série trimestral de 16 valores do script da aula;
- ACF/PACF: AR(1) com phi = 0,8 e MA(1) com theta = -0,3 (500 pontos, seed 42), como no script da aula.
Uso: python tools/make_figures8.py"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.stattools import acf, pacf
import make_figures as mf
from make_figures import save, C1, C2, C3, GR


def decomposicao():
    vals = [10, 14, 8, 25, 16, 22, 14, 35, 15, 27, 18, 40, 28, 40, 25, 65]
    s = pd.Series(vals, index=pd.date_range("2019-03-31", periods=16, freq="QE"))
    d = seasonal_decompose(s, model="additive", period=4)
    t = np.arange(1, 17)
    fig, ax = plt.subplots(4, 1, figsize=(6.6, 6.4), sharex=True)
    ax[0].plot(t, s.values, "-o", color=C1, ms=4); ax[0].set_ylabel("série")
    ax[1].plot(t, d.trend.values, "-o", color=C2, ms=4); ax[1].set_ylabel("tendência")
    ax[2].plot(t, d.seasonal.values, "-o", color=C3, ms=4); ax[2].set_ylabel("sazonal")
    ax[3].bar(t, d.resid.values, color=GR); ax[3].set_ylabel("resíduo"); ax[3].axhline(0, color="black", lw=.6)
    ax[3].set_xlabel("trimestre (1 = 1º tri de 2019)")
    ax[0].set_title("Decomposição aditiva da série trimestral da aula")
    fig.tight_layout()
    save(fig, "22_decomposicao")


def acfpacf():
    np.random.seed(42)
    ar = ArmaProcess(np.array([1, -0.8]), np.array([1])).generate_sample(nsample=500)
    np.random.seed(42)
    ma = ArmaProcess(np.array([1]), np.array([1, -0.3])).generate_sample(nsample=500)
    L = 10
    fig, ax = plt.subplots(2, 2, figsize=(8, 5))
    for r, (nome, x) in enumerate([("AR(1), φ = 0,8", ar), ("MA(1), θ = −0,3", ma)]):
        for c, (fn, tit) in enumerate([(acf, "ACF"), (pacf, "PACF")]):
            v = fn(x, nlags=L)[1:]
            ax[r, c].bar(range(1, L + 1), v, color=C1 if c == 0 else C3)
            ax[r, c].axhline(1.96 / np.sqrt(len(x)), color=C2, ls="--", lw=.8)
            ax[r, c].axhline(-1.96 / np.sqrt(len(x)), color=C2, ls="--", lw=.8)
            ax[r, c].axhline(0, color="black", lw=.6)
            ax[r, c].set_title("%s · %s" % (tit, nome), fontsize=10)
            ax[r, c].set_ylim(-.5, 1)
    ax[1, 0].set_xlabel("defasagem (lag)"); ax[1, 1].set_xlabel("defasagem (lag)")
    fig.tight_layout()
    save(fig, "22_acf_pacf")


if __name__ == "__main__":
    decomposicao(); acfpacf()
