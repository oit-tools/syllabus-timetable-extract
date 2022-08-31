"""
zipを展開する
"""
import shutil


def unpack(year: str, name: str) -> None:
    source = f"./data/{year}/{name}.zip"
    destination = f"./data/{year}/{name}"
    shutil.unpack_archive(source, destination)
