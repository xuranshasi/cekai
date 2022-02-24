# 异常
# try:
#     num1 = int(input("请输入一个数"))
#     num2 = int(input("请输入一个数"))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("被除数不能为0")
# except ValueError:
#     print("输入的数值需要为数值型")

# 系统异常类
# x = 10
# if x>5:
#     raise Exception("这是抛出的异常信息")

# 自定义异常类
# class MyException(Exception):
#     def __init__(self,value1,value2):
#         self.value1 = value1
#         self.value2 = value2
#
# raise MyException("a","b")

# 面向对象
# 类
# class Person():
#     name = "noname"
#
#     def get_name(self):
#         return self.name
#
#
# print(Person.name)
# p = Person()
# print(p.name)
# print(p.get_name())
# p.name = 'xiaoming'
#
# # 修改类无法影响实例
# Person.name = 'lili'
# print(p.name)
#
# p1 = Person()
# print(p1.name)


# 实例引用
# class Person():
#     # 公共属性
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     # 特有属性
#     def set_attr(self,value):
#         self.value = value
#
#     def eat(self):
#         print(f"name:{self.name}, age:{self.age}, gender:{self.gender} 我在吃")
#
#     def drink(self):
#         print(f"name:{self.name}, age:{self.age}, gender:{self.gender} 我在喝")
#
#     def run(self):
#         print(f"name:{self.name}, age:{self.age}, gender:{self.gender} 我在跑")
#
# xiaoming = Person("xiaoming", 10, "male")
# xiaohong = Person("xiaohong", 18, "female")
#
# print(xiaoming.name)
# xiaoming.run()
#
#
# xiaoming.set_attr("fit")
# print(xiaoming.value)


# 实战
# 回合制游戏
class Game():
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power


    def fight(self, enemy_power, enemy_hp):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp>enemy_final_hp:
            print("我赢了")
        elif final_hp<enemy_final_hp:
            print("我输了")
        else:
            print("平局")

# hp = 1000
# power = 200
# game = Game(hp,power)
# game.fight(1000,200)

class HouYi(Game):
    # 如果在子类中定义了__init__就会覆盖父类__init__
    def __init__(self, defense):
        super().__init__(1000,200)
        self.defense = defense

    def houyi_fight(self, enemy_power, enemy_hp):
        final_hp = self.hp + self.defense - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp>enemy_final_hp:
            print("我赢了")
        elif final_hp<enemy_final_hp:
            print("我输了")
        else:
            print("平局")

hp = 1000
power = 200

houyi = HouYi(300)
houyi.houyi_fight(hp,power)
