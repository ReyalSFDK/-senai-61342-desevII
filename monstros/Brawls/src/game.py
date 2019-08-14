from src.classes.Tournament import Tournament
from src.brawlers import competitive_brawlers

tournament = Tournament(
    competitive_brawlers
)
tournament.start_quarterfinals()

