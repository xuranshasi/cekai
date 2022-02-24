# 字符串匹配
# name = 'Tom'
# print(f'my name is {name}')


# 文件读取
# a = open('testfile','r')
# print(a.read())
# print(a.readline())
# print(a.readline())
# print(a.readlines())
#
# a.close()

# with open('testfile','rt') as f:
#     # print(f.read())
#     while True:
#         line = f.readline()
#         if line:
#             print(line)
#         else:
#             break


# json
import json
# info = [{"err_no":0,"errmsg":"","queryid":"0x190fd5ae222e78"}]

# 字典转字符串
# data = json.dumps(info,sort_keys=True, indent=4)
# print(data)

# 写文件 dump
# data = json.dump(info,open('test.json','w'))

# loads
# info = '''[{"err_no":0,"errmsg":"","queryid":"0x190fd5ae222e78"}]'''
# print(json.loads(info))

# load 读取文件
# jsObj = json.load(open('test.json','r'))
# print(jsObj)
# print(jsObj[0]['err_no'])
