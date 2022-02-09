from game.game import Game


class HouYi(Game):
    # 如果在子类中定义了__init__就会覆盖父类__init__
    def __init__(self, defense):
        super().__init__(1000,200)
        self.defense = defense

    def houyi_fight(self, enemy_power, enemy_hp):
        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            print(self.hp)
            print(enemy_hp)
            if self.hp <= 0:
                if self.hp == enemy_hp:
                    raise Exception("平局")
                print("我输了")
                break
            elif enemy_hp <= 0:
                print("我赢了")
                break


hp = 1000
power = 300

houyi = HouYi(0)
houyi.houyi_fight(hp,power)
