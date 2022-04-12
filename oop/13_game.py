from math import sqrt
import queue


class BaseCharacter:
    def __init__(self, x, y, hp):
        self.pos = [x, y]
        self.hp = hp
        if hp > 0:
            self.alive = True
        else:
            self.alive = False

    def move(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy

    def is_alive(self):
        return self.alive

    def get_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.alive = False
        
    def get_coords(self):
        return self.pos


class BaseEnemy(BaseCharacter):
    def __init__(self, x, y, hp, weapon):
        super().__init__(x, y, hp)
        self.weapon = weapon
    
    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print("Can only hit main character")
            

    def __str__(self):
        return f"pos {self.pos} with wep {self.weapon}"


class MainHero(BaseCharacter):
    def __init__(self, x, y, hp, name):
        super().__init__(x, y, hp)
        self.name = name
        self.weapon = None
        self.weapon_wheel = []
        self.weapon_idx = None
        
    def hit(self, target):
        if self.weapon:
            if isinstance(target, BaseEnemy):
                self.weapon.hit(self, target)
            else:
                print("can only hit enemies")
        else:
            print("no weapon")
    
    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            if self.weapon is None:
                self.weapon = weapon
                self.weapon_idx = 0
            self.weapon_wheel.append(weapon)
            print(f"acquired {weapon}")
        else:
            print("this is not a weapon")
    
    def next_weapon(self):
        if not self.weapon:
            print("no weapon")
        elif len(self.weapon_wheel) <= 1:
            print("only one weapon")
        else:
            # print(f"before putting {self.weapon_wheel}")
            self.weapon_wheel.append(self.weapon)
            if self.weapon_idx == len(self.weapon_wheel)-1:
                self.weapon_idx == 0
            else:
                self.weapon_idx += 1
            self.weapon = self.weapon_wheel[self.weapon_idx]
            # print(f"after {self.weapon_wheel}")
            print(f"equipped {self.weapon}")
    
    def heal(self, hp):
        self.hp += hp
        if self.hp > 200:
            self.hp = 200
        print(f"healed, hp: {self.hp}")

def dist(p1, p2):
    X, Y = 0, 1
    return sqrt((p2[X] - p1[X]) ** 2 + (p2[Y] - p1[Y]) ** 2)

class Weapon:
    def __init__(self, name, dmg, range):
        self.name = name
        self.dmg = dmg
        self.range = range
    
    def __str__(self):
        return self.name
    
    def hit(self, actor, target):
        if not target.is_alive():
            print("target already dead")
        elif self.range < dist(actor.get_coords(), target.get_coords()):
            print(f"too far for {self}")
        else:
            print(f"damaged {target} for {self.dmg}")
            target.get_damage(self.dmg)


w1 = Weapon("короткий", 5, 1)
w2 = Weapon("длинный", 7, 2)
w3 = Weapon("лук", 3, 10)
w4 = Weapon("лазер", 1000, 1000)

p = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, 100, w3)
armored = BaseEnemy(10, 10, 500, w2)
archer.hit(armored)
armored.move(10, 10)

print(armored.get_coords())

main = MainHero(0, 0, 200, "a")
main.hit(armored)
main.next_weapon()
main.add_weapon(w1)
main.hit(armored)
main.add_weapon(w4)
main.hit(armored)
main.next_weapon()
main.hit(p)
main.hit(armored)
main.hit(armored)

