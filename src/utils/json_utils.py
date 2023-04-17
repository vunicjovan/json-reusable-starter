from json import load, dump
from typing import Any


class JsonUtils:
    @staticmethod
    def load(file_path: str) -> dict:
        with open(file_path, mode="r") as json_file:
            return load(json_file)

    @staticmethod
    def create(obj: Any, file_path: str) -> None:
        with open(file_path, mode="w") as outfile:
            dump(obj, outfile)
