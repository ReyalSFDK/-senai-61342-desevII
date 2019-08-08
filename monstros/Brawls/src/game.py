from src.classes.Brawler import Brawler

bibi = Brawler(name="Bibi", attack=10, defense=5, hp=5000, power=3, rarity=3)
pipe = Brawler(name="Pipe", attack=10, defense=0, hp=2000, power=10, rarity=5)

rounds = 0
while bibi.hp > 0 and pipe.hp > 0:
    rounds += 1
    print()
    print("# Round %s #" % rounds)
    # Pipe's attack
    bibi.receive_attack(pipe)
    if bibi.hp == 0:
        break
    print(bibi.status())
    print()
    # Bibi's attack
    pipe.receive_attack(bibi)
    if pipe.hp == 0:
        break
    print(pipe.status())
