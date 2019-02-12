import copy

from game_data import *

data = GameData()
data2 = GameData()

data.set("test", 18)
print(data2.get("test"))
print(data.get("test"))
print(data.get("foo", "Nothing here"))
print(data.get("foo"))

print(0.5 if 4 > 0 else 2)

