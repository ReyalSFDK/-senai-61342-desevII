from typing import List
from random import randrange
from src.classes.Brawler import Brawler
from src.classes.Battle import Battle


class Tournament:
    battle = None
    levels = []
    semifinals = List[Brawler]
    finals = List[Brawler]

    def __init__(self, brawlers: List[Brawler], levels):
        self.winner = None
        self.competitors = brawlers
        self.levels = levels

    # Incia o torneio
    def start_tournament(self):
        for level in range(1, self.calc_max_levels(len(self.competitors)) + 1):
            self.competitors = self.start_level(level, self.competitors)

        self.winner = self.competitors.pop()
        print()
        print("E %s vence o torneio!" % self.winner)

    # Inicia uma fase do torneio
    @staticmethod
    def start_level(current_level, competitors):
        print()
        print("# - Inicio da fase", current_level, "!")
        print()
        next_level = []
        max_duels = len(competitors) / 2
        while len(next_level) < max_duels:
            if len(competitors) != 1:
                brawler1 = competitors.pop(randrange(len(competitors)))
                brawler2 = competitors.pop(randrange(len(competitors)))

                next_level.append(
                    Battle(
                        brawler1,
                        brawler2,
                    ).do_battle()
                )
            else:
                wo_winner = competitors.pop()
                print("Sem adversários, %s passa para próxima fase!" % wo_winner)
                next_level.append(wo_winner)

        return next_level

    @staticmethod
    def calc_max_levels(competitors_amount):
        result = 0
        while competitors_amount > 1:
            competitors_amount /= 2
            result += 1

        return result
