from dataclasses import dataclass, asdict
from json import dumps

@dataclass
class User:
    name: str
    surname: str
    email: str
    password: str

    @property
    def __dict__(self):
        return asdict(self)

    @property
    def json(self):
        return dumps(self.__dict__)
