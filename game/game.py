

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