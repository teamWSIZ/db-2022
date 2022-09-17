import json
from dataclasses import dataclass


@dataclass
class A:
    x: int
    y: str

a = A(1,'gg')
dc = a.__dict__
s = json.dumps(dc)
print(dc)
print(s)

dd = json.loads(s)
a_ = A(**dd)
print(a_)