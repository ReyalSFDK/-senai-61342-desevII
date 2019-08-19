from src.classes.Brawler import Brawler
import json

brawlers = open('brawlers.json', 'r')
brawlers = brawlers.read()

all_brawlers = json.loads(brawlers)

competitive_brawlers = []

for brawler in all_brawlers["brawlers"]:
    competitive_brawlers.append(
        Brawler(
            brawler["name"],
            brawler["damage"],
            brawler["defense"],
            brawler["hp"],
            brawler["agility"],
            brawler["brawler_type"],
        )
    )
