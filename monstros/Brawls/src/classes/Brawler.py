from random import randint


class Brawler:

    def __init__(self, name, damage, defense, agility, hp):
        self.name = name
        self.damage = damage
        self.defense = defense
        self.hp = hp
        self.max_hp = hp
        self.agility = agility

    def generate_damage(self) -> int:
        return self.damage * ((randint(-30, 30) / 100) + 1)

    def generate_defense(self) -> int:
        return self.defense * ((randint(-20, 20) / 100) + 1)

    def generate_agility(self):
        return self.agility * ((randint(-50, 50) / 100) + 1)

    def receive_attack(self, attacker: 'Brawler'):
        if self.hp > 0:
            damage = attacker.generate_damage()
            defense = self.generate_defense()
            total_damage = damage - defense
            self.hp -= total_damage

            if self.hp < 0:
                self.hp = 0

    def __str__(self):
        return self.name
