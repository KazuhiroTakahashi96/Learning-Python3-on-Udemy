# ------------------------------------------------------------
# ---------------**## Data Types part 2 ##**------------------

"""
--Data Type--         --Class--                 --Value--
integers               -> int                     -> 45
floating point numbers -> float                   -> 4.5
booleans               -> bool                    -> True/False
strings                -> str                     -> "Muslim Helalee"
list                   -> list                    -> [1, 2, 3]
dictionary             -> dict                    -> {"user_name": "awesome50", "user_id": 56}
tuple                  -> tuple                   -> (10, 20, 30)
set                    -> set                     -> {"cat", 99}
"""

# *-*-*-*-*--------------- List ********************************
# []に囲まれて、,で区切る　JSでいうところの配列？
# Ordered
mixed = [1, 2, 3.2, 5.4, True, "Muslim Helalee", [1, 2, 3]]
# print(mixed)
# print(type(mixed))

# *-*-*-*-*--------------- Dictionary **************************
# key: value の組み合わせで、 ,で区切る　JSのオブジェクト？
# unordered
user_info = {"user_name": "awesome50", "user_id": 56}
# print(user_info["user_name"])
# print(type(user_info))

# *-*-*-*-*--------------- Tuple *******************************
# tupleはimmutable(不変)
# ordered
mixed_tuple = (1, 2, 3.2, 5.4, True, "Muslim Helalee", [1, 2, 3])
print(mixed_tuple)
print(type(mixed_tuple))

# *-*-*-*-*--------------- Set *********************************
# key: valueの組み合わせではなく、itemの羅列？
# unordered
mixed_set = {1, 2, 3.2, 5.4, "Python", "Muslim Helalee", 101}
# print(mixed_set)
# print(type(mixed_set))