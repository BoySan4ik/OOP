# class Goods():
#     title = "Мороженое"
#     weight = 151
#     tp = "Еда"
#     price = 12321

# goods = Goods()
# print(goods.price)
# print(goods.weight)
# goods.price = 100
# goods.weight = 101
# print(goods.price)
# print(goods.weight)

# from io import TextIOWrapper
# import re


# class UserSchem():
#     pass

# class DataBase:
#     def get_data(self, url):
#         with open(url, "r", encoding='UTF-8') as f:
#             result = f.readlines()
#             f.close()
#             return result
#     def serializers(self, data:TextIOWrapper):
#         content = []
#         for i in data:
#             schema=dict()
#             line = [i for i in re.split(r'\s', i) if i != ""]
#             for index in range(0,len(line)-1, 2):
#                 schema[line[index]] = line[index+1]
#             content.append(schema)
#         return content
#     def create(self, data):
#         for i in data:
#             user = UserSchem()
#             for key, item in i.items():
#                 setattr(user, key, item)
                
# class Resource:
#     def __init__(self, name: str, resource_type:str):
#         self.name = name
#         self.resource_type = resource_type
#     def __del__(self):
#         print(f"{self.name} {self.resource_type}")

# r1 = Resource("1", "2")
# r2 = Resource("3", "4")

# for _ in range(1, 11):
#         print(_)
#         if _ == 5:
#             del r2

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    start = None
    end = None
    