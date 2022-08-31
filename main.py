import json
import os

import extract


def main():
    YEAR = "2022"
    numbering = dict()

    # pdfの展開
    if not os.path.exists(f"./data/{YEAR}/pdf"):
        extract.unpack(YEAR, "pdf")
    # csvの展開
    if not os.path.exists(f"./data/{YEAR}/csv"):
        extract.unpack(YEAR, "csv")

    # pdfから講義コードを抽出して辞書に追加
    pdf_numbering = extract.pdf(YEAR)
    numbering.update(pdf_numbering)
    # csvから講義コードを抽出して辞書に追加
    csv_numbering = extract.csv(YEAR)
    numbering.update(csv_numbering)

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
