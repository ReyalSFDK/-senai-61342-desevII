from src.classes.Tournament import Tournament
from src.brawlers import competitive_brawlers

tournament = Tournament(
    competitive_brawlers,
    ("Quartas de Final", "Semi-final", "Finais")
)
tournament.start_tournament()
# tournament.start_quarterfinals()

