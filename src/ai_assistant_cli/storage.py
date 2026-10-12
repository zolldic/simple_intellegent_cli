#!/usr/bin/python3

from pathlib import Path
import json
from typing import List

class Storage:
    def __init__(self, path: str='history.json'):
        self._path: str = path
        self._dir: Path  = Path('./data')
        self._dir.mkdir(parents=True, exist_ok=True)
        self.init_storage()

    def init_storage(self) -> None:
        full_path: Path = self._dir / self._path
        if not full_path.exists():
            with open(full_path, 'w', encoding='utf-8') as fd:
                json.dump([], fd, indent=4)

    def load(self, storage_path: str ='history.json') -> List[dict]:
        path: Path = self._dir / storage_path
        with open(path, 'r', encoding='utf-8') as fd:
            data: List[dict] = json.load(fd)
        return data


storage = Storage()
