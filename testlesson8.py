# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#
#     def __repr__(self):
#         return self.brand
#
# items_list = [
#     Item(1000, "Apple"),
#     Item(1200, "Apple"),
#     Item(342, "Apple"),
#     Item(5464, "Apple"),
#     Item(900, "Samsung"),
#     Item(700, "Samsung"),
#     Item(660, "Xiaomi")
# ]
# print([x for x in items_list if x.brand == 'Apple'])

names_list = ['данил', 'артём', 'никита', 'влад']
for i in names_list:
    str(names_list[i]) = names_list[i].title