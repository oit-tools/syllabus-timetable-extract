import json
import os

import extract


def main():
    YEAR: str = "2022"
    numbering: dict = dict()

    # pdfの展開
    if not os.path.exists(f"./data/{YEAR}/pdf"):
        extract.unpack(YEAR, "pdf")
    # csvの展開
    if not os.path.exists(f"./data/{YEAR}/csv"):
        extract.unpack(YEAR, "csv")

    # pdfから講義コードを抽出して辞書に追加
    numbering.update(extract.pdf(YEAR))
    # csvから講義コードを抽出して辞書に追加
    numbering.update(extract.csv(YEAR))

    # 値の重複を削除、ソート
    for key in numbering.keys():
        numbering[key] = sorted(list(set(numbering[key])))
    # キーをソート
    numbering = dict(sorted(numbering.items()))

    # jsonに保存
    with open(f"./data/{YEAR}/numbering.json", "w") as f:
        json.dump(numbering, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
