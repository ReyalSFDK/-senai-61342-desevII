from src.classes.Brawler import Brawler


class Battle:

    def __init__(self, brawler1: 'Brawler', brawler2: 'Brawler'):
        self.brawler1 = brawler1
        self.brawler2 = brawler2
        self.fasted = brawler1
        self.slower = brawler2

    def get_fasted(self):
        vel1 = self.brawler1.generate_agility()
        vel2 = self.brawler2.generate_agility()

        if vel1 > vel2:
            self.fasted = self.brawler1
        elif vel2 > vel1:
            self.slower = self.brawler2
        else:
            self.get_fasted()

    def do_battle(self) -> Brawler:
        rounds = 0

        while True:
            self.get_fasted()
            rounds += 1
            # Fasted's attack
            self.slower.receive_attack(self.fasted)
            if self.slower.hp == 0:
                winner = self.fasted
                looser = self.slower
                break
            # Slower's attack
            self.fasted.receive_attack(self.slower)
            if self.fasted.hp == 0:
                winner = self.slower
                looser = self.fasted
                break
        print(
            "Em %s rodadas, %s [lvl %s] derrotou %s [lvl %s] na batalha restando %s de vida."
            % (rounds, winner, winner.level, looser, looser.level, int(winner.hp))
        )
        winner.hp = winner.max_hp
        winner.level_up()
        return winner
