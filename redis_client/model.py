import json
from dataclasses import dataclass


@dataclass
class User:
    uid: int
    name: str
    passwd: str


@dataclass
class Election:
    eid: int
    name: str


def testy():
    u = User(1, 'Czesław Szczęsny', passwd='11-22-33-11')
    d = u.__dict__
    print(u)
    print(d)

    js = json.dumps(d)
    print(js)
    ###
    d_ = json.loads(js)
    print(d_)
    u_ = User(**d)
    print(u_)