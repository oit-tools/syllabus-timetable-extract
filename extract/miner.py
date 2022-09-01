"""
講義コードを抽出する
"""
import os
import re

from pdfminer.high_level import extract_text
from tqdm import tqdm


def pdf(year: str) -> dict:
    path: str = f"./data/{year}/pdf"
    files: list[str] = os.listdir(path)
    numbering_dict: dict = dict()

    for file in tqdm(files):
        # テキストの抽出
        text: str = extract_text(f"{path}/{file}")

        # 英数字6桁を抽出後、末尾にA0を付加
        if file[0] == "X":
            text = re.sub(r"[0-9a-zA-Z]{6}", r"\g<0>A0", text)
        # 英数字8桁のみを抽出
        numbering: str = re.findall(r"[0-9a-zA-Z]{8}", text)

        # ファイル名を取得
        name: str = file.split(".")[0]
        # 講義コードを辞書に追加
        numbering_dict[name] = numbering

    return numbering_dict


def csv(year: str) -> dict:
    path: str = f"./data/{year}/csv"
    files: list[str] = os.listdir(path)
    numbering_dict: dict = dict()

    for file in tqdm(files):
        with open(f"{path}/{file}", "r", encoding="utf-8") as f:
            # ファイルの中身をコンマ区切りでリストに変換
            numbering: list[str] = f.read().split(",")

        # ファイル名を取得
        name: str = file.split(".")[0]
        # 講義コードを辞書に追加
        numbering_dict[name] = numbering

    return numbering_dict
