"""Gera docs/data.js (conteúdo do site de estudo) a partir de resumos/*.md e plano_de_estudos.md.
Uso: python tools/build_site.py   (requer: pip install markdown)"""
import glob, json, os, re
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "data.js")

GROUPS = [
    ("Estatística e modelos supervisionados", [1, 17, 18, 19, 20, 22]),
    ("Machine Learning", [2, 14, 15, 16, 27, 28, 25]),
    ("Dados, engenharia e plataformas", [3, 4, 21, 23, 24, 7, 29]),
    ("Decisão, risco e otimização", [13, 26, 10, 9, 8, 6]),
    ("Gestão, pessoas e legislação", [5, 11, 12, 30]),
]


SHORT = {1:"Estatística",2:"Python e mapa de ML",3:"BI e Data Viz",4:"Engenharia de Dados",5:"Metodologias Ágeis",6:"Comp. Evolucionária",7:"Cloud Computing",8:"Análise de Redes (SNA)",9:"Conjuntura Econômica",10:"Riscos e Analytics",11:"Liderança em DS",12:"LGPD",13:"Modelagem / AHP",14:"Clustering",15:"Fatorial e PCA",16:"ANACOR e ACM",17:"Regressão",18:"Logística",19:"Dados de Contagem",20:"Multinível",21:"Big Data e MLOps",22:"Séries Temporais",23:"Data Wrangling",24:"Web Scraping",25:"Text Mining / NLP",26:"Pesquisa Operacional",27:"Árvores e Ensemble",28:"Deep Learning",29:"APIs e LLMs",30:"Gestão da Mudança"}


def fix_md(text):
    """python-markdown exige linha em branco antes de listas/tabelas e 4 espaços no aninhamento."""
    out, prev = [], ""
    for line in text.split("\n"):
        m = re.match(r"^( *)([-*]|\d+\.) ", line)
        if m:
            n = len(m.group(1))
            if n:
                line = " " * (n * 2) + line[n:]
            if prev.strip() and not re.match(r"^ *([-*]|\d+\.) ", prev):
                out.append("")
        elif line.startswith("|") and prev.strip() and not prev.startswith("|"):
            out.append("")
        elif line.strip() and prev.startswith("|") is False and False:
            pass
        out.append(line)
        prev = line
    return "\n".join(out)


def _protect_math(text):
    r"""Isola fórmulas \( ... \) e \[ ... \] antes do markdown (que comeria as barras)."""
    store = []

    def keep(kind):
        def f(m):
            store.append((kind, m.group(1)))
            return "@@MATH%d@@" % (len(store) - 1)
        return f
    text = re.sub(r"\\\[(.+?)\\\]", keep("d"), text, flags=re.S)
    text = re.sub(r"\\\((.+?)\\\)", keep("i"), text, flags=re.S)
    return text, store


def _restore_math(html, store):
    import html as H
    for i, (kind, body) in enumerate(store):
        b = H.escape(body.strip(), quote=False)
        rep = ("\\[" + b + "\\]") if kind == "d" else ("\\(" + b + "\\)")
        html = html.replace("@@MATH%d@@" % i, rep)
    return html


def render(text):
    text, store = _protect_math(text)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc", "md_in_html"],
                           extension_configs={"toc": {"toc_depth": "2-3"}})
    html = md.convert(fix_md(text))
    html = _restore_math(html, store)
    return html, md.toc_tokens


def plain(s):
    s = re.sub(r"\\\((.+?)\\\)", lambda m: m.group(1), s)
    s = re.sub(r"\*\*|__|`|\*", "", s)
    s = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", s)
    return s.strip()


def questions(text):
    m = re.search(r"##\s*Pergunta típica\s*\n(.*?)(?:\n## |\Z)", text, re.S)
    if not m:
        return []
    body = " ".join(l.strip() for l in m.group(1).strip().split("\n"))
    qs = [plain(q).strip(" .") for q in re.split(r"\s+·\s+", body)]
    return [q for q in qs if len(q) > 8]


def cards(text):
    res = []
    for line in text.split("\n"):
        m = re.match(r"^\s*[-*] \*\*([^*]{2,90}?)\*\*\s*(.*)$", line)
        if not m:
            continue
        term, rest = m.group(1).strip(), m.group(2).strip()
        if term.endswith(":"):
            term = term[:-1].strip()
        elif rest.startswith(":"):
            rest = rest[1:].strip()
        else:
            continue
        rest = plain(rest)
        if 25 <= len(rest) <= 420 and len(term) >= 2:
            res.append({"q": f"{plain(term)}?", "a": rest})
    return res


def main():
    discs = []
    for f in sorted(glob.glob(os.path.join(ROOT, "resumos", "*.md"))):
        text = open(f, encoding="utf-8").read()
        num = int(os.path.basename(f)[:2])
        title = re.sub(r"^#\s*\d+\s*·\s*", "", text.split("\n")[0].lstrip("# ").strip())
        title = re.sub(r"^\d+\s*·\s*", "", title)
        html, toc = render(text)
        prio = re.search(r"Prioridade[^A-Za-zÁ-ú]*([A-ZÁ-Ú][A-ZÁ-Ú-]+(?: [A-ZÁ-Ú-]+)?)", text)
        discs.append({
            "id": num, "title": title, "short": SHORT.get(num, title), "file": os.path.basename(f),
            "priority": prio.group(1).strip() if prio else "",
            "html": html,
            "toc": [{"id": t["id"], "name": t["name"]} for t in toc[0]["children"]] if toc and False else
                   [{"id": c["id"], "name": c["name"]} for t in toc for c in ([t] + t.get("children", [])) if c["level"] == 2],
            "questions": questions(text), "cards": cards(text),
            "text": plain(re.sub(r"\n+", " ", text)).lower(),
        })
    plan_text = open(os.path.join(ROOT, "plano_de_estudos.md"), encoding="utf-8").read()
    plan_html, _ = render(plan_text)
    data = {"groups": [{"name": n, "ids": ids} for n, ids in GROUPS], "disciplines": discs, "plan": plan_html}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("window.STUDY_DATA = " + json.dumps(data, ensure_ascii=False) + ";")
    nq = sum(len(d["questions"]) for d in discs)
    nc = sum(len(d["cards"]) for d in discs)
    print(f"{len(discs)} disciplinas, {nq} perguntas, {nc} flashcards -> {OUT}")


if __name__ == "__main__":
    main()
