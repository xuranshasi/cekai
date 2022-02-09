# 函数
# 默认值只会执行一次
# def method(a,b=[]):
#     """
#
#     :param a:
#     :return:
#     """
#     # print(a)
#     b.append(a)
#     return b
#
# print(method(1))
# print(method(2))

# def method(*a):
#     """
#
#     :param a:
#     :param b:
#     :return b:
#     """
#     print(a[0])
#     print(a[1])
#     print(a[2])
#     print(a[3])
#     print(a[4])
#
# method(1,2,3,4,5,6)


# 解包
# *解元组
# **解字典


# lamada


# 列表推导式
# list = [i**2 for i in range(1,10)]
# print(list)

# list = [i**2 for i in range(1,10) if i !=1]
# print(list)

# list = [i*j for i in range(1,10) for j in range(1,10)]
# print(list)


# 元组
# tuple_test = 1,2,3
# tuple_test1 = (1,2,3)
# print(*tuple_test)
# print(*tuple_test1)


# 集合
# a = {1,2,3}
# b = {1,4,5}
#
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
#
# print({i for i in "asdjoasdnfidsofsasada"})


# 字典
# dict_test = {}
# dict_test1 = dict(a=1,b=2)
# print(dict_test,dict_test1)

# print(dict_test1.keys())
# print(dict_test1.values())

# a = {}
# b = a.fromkeys((1,2,3),"a")
# print(b)

# print({i: i**2 for i in range(1,10)})


