from random import randint


class Brawler:
    name = ""
    type = ""
    attack = 0
    defense = 0
    hp = 0
    rarity = 0
    power = 1

    def __init__(self, name, attack, defense, hp, power, rarity):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.power = power
        self.rarity = rarity

    def generate_damage(self) -> int:
        return self.attack * self.rarity * self.power * randint(1, 5)

    def generate_defense(self) -> int:
        return self.defense * self.rarity * self.power * randint(1, 3)

    def receive_attack(self, attacker: 'Brawler'):

        if self.hp > 0:
            damage = attacker.generate_damage()
            defense = self.generate_defense()
            total_damage = damage - defense
            self.hp -= total_damage

            print("%s ataca %s!" % (attacker.name, self.name))
            print("%s sofre %s de dano!" % (self.name, total_damage))

            if self.hp < 0:
                self.hp = 0

                print("%s morreu no combate!" % (self.name))
                print("%s ganhou a batalha!" % (attacker.name))
        else:
            print("%s já está em outro mundo!" % (self.name))

    def status(self):
        return "%s ainda tem %s de HP" % (self.name, self.hp)
