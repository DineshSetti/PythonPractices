# from enum import Enum
# class Countries(Enum):
#     india=1
#     usa=2
#     uk=3
#
# print(Countries.india)
#
# print(Countries(2))
#
# for i in Countries:
#     print(i)
#


from enum import Enum
class Countries(Enum):
    india=1
    usa=2
    uk=3

obj=Countries.uk
print(obj.name,obj.value)