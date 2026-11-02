#!/usr/bin/python3

from pathlib import Path
import json
from typing import List

class Storage:
    def __init__(self, path: str='history.json'):
        self._path: str = path
        self._dir: Path  = Path('./data')
        self._dir.mkdir(parents=True, exist_ok=True)

    def init_storage(self) -> Path:
        full_path: Path = self._dir / self._path
        if not full_path.exists():
            with open(full_path, 'w', encoding='utf-8') as fd:
                json.dump([
                    {"role": "system", "content": "You are a helpfull assistant"}
                ], fd, indent=4)
        return full_path

    def load(self, storage_path: str ='history.json') -> List[dict]:
        path: Path = self._dir / storage_path
        with open(path, 'r', encoding='utf-8') as fd:
            data: List[dict] = json.load(fd)
        return data

    def save(self, data: List[dict]) -> None:
        path: Path = self._dir / self._path
        with open(path, 'w', encoding='utf-8') as fd:
            json.dump(data, fd, indent=4)

storage = Storage()
