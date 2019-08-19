from random import randint

brawler_types = ("ranged", "melee", "tanker")


class Brawler:

    def __init__(self, name, damage, defense, agility, hp, brawler_type):
        self.name = name
        self.damage = damage
        self.defense = defense
        self.hp = hp
        self.max_hp = hp
        self.agility = agility
        self.type = brawler_type
        self.level = 1

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
            if total_damage < 0:
                total_damage = 1
            self.hp -= total_damage

            if self.hp < 0:
                self.hp = 0

    def level_up(self):
        self.level += 1

        # Ranged
        if self.type == brawler_types[0]:
            self.agility *= 1.5
            self.damage *= 1.5

        # Melee
        elif self.type == brawler_types[1]:
            self.damage *= 1.5
            self.max_hp *= 1.5

        # Tanker
        elif self.type == brawler_types[2]:
            self.max_hp *= 1.5
            self.defense *= 1.5

    def __str__(self):
        return self.name
