from typing import List
from random import randrange
from src.classes.Brawler import Brawler
from src.classes.Battle import Battle


class Tournament:
    battle = None
    semifinals = List[Brawler]
    finals = List[Brawler]

    def __init__(self, brawlers: List[Brawler]):
        if len(brawlers) != 8:
            raise ValueError("Sua lista de participantes tem que ter exatamente 8 participantes")
        self.quarterfinals = brawlers
        self.semifinals = []
        self.finals = []
        self.winner = None

    def start_quarterfinals(self):
        print()
        print("# - Inicio das quartas de finais!")
        print()
        while len(self.semifinals) < 4:
            self.semifinals.append(
                Battle(
                    self.quarterfinals.pop(randrange(len(self.quarterfinals))),
                    self.quarterfinals.pop(randrange(len(self.quarterfinals))),
                ).do_battle()
            )
        self.start_semifinals()

    def start_semifinals(self):
        print()
        print("# - Inicio das semifinais!")
        print()
        while len(self.finals) < 2:
            self.finals.append(
                Battle(
                    self.semifinals.pop(randrange(len(self.semifinals))),
                    self.semifinals.pop(randrange(len(self.semifinals))),
                ).do_battle()
            )
        self.start_finals()

    def start_finals(self):
        print()
        print("# - Inicio da grande final!")
        print()
        self.winner = Battle(
            self.finals.pop(),
            self.finals.pop(),
        ).do_battle()
        print()
        print("E %s vence o torneio!" % self.winner)


