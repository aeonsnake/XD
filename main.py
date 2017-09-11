class Char(object):
    def __init__(self):
        self.dex = 0
        self.str = 0
        self.wis = 0
        self.char = 0
        self.con = 0
        self.intel = 0
        self.traits = ""
        self.level = 1
        self.cla = ""
        self.fp = ""
player = Char()
R = input("What is your race?")
r = R.lower()
player.cla = R
if "dragonborn" in r:
    player.str += 2
    player.char += 1
    player.traits += input("Choose one Chromatic or Metallic Dragon") + ",'breath weapon shape, breath weapon damage, and damage resistance based on what they chose (cold for Silver Dragonborn, acid for Black, etc),'/n"
if "aasimar" in r:
    player.wis += 1
    player.char += 2
    player.traits = "resistance to necrotic and radiant damages, and the spell-like abilities Light (level 1), Lesser Restoration (1/day at level 3) and Daylight (1/day at level 5)./n"
if "standard dwarf" in r:
    player.con += 2
    player.traits += "Darkvision, protection against poison, training with axe and hammer weapons, training with several kinds of artisan's tools, the usual dwarven armored movement and stone knowledge./n"
if "hill dwarf" in r:
    player.wis += 2
    player.traits = "Even tougher than normal dwarves, giving them extra maximum hit points equal to their character level/n"
if "mountain dwarf" in r:
    player.str += 2
    player.traits += "free proficiency with light armor and medium armor./n"
if "elf" in r:
    player.dex += 2
    player.traits += "Darkvison, proficiency in perception, resistant to charming and immune to sleep, and they trance instead of sleeping"
if "high elf" in r:
    player.intel += 1
    player.traits += "proficiency with long & short swords and bows, an extra language, and the ability to cast one wizard cantrip of the player's choice."
if "wood elf" in r:
    player.wis += 1
    player.traits = "proficiency with long & short swords and bows."
if "dark elf" in r:
    player.traits += " innate magic (Dancing Lights cantrip at level 1, Faerie Fire 1/day at level 3, Darkness 1/day at level 5), Superior Darkvision (Darkvision to 120 feet), proficiency with rapiers, shortswords and hand crossbows, and are the only (sub)race in the corebook with any kind of racial penalty; they take disadvantage to attack rolls and Perception checks when they or their target is in direct sunlight."
    player.char += 1
if "eladrin" in r:
    player.traits += "proficiency with long & short swords and bows. Misty step, like Fey Step from 4E"
    player.intel += 1
if "gnome" in r:
    player.intel += 2
    player.traits += "small sized darkvision, advantage to any saving throw against magic that relies on intelligence,wisdom or charisma"
if "forest gnome" in r:
    player.dex += 1
    player.traits += " minor illusion cantrip as a racial ability, and being able to speak with any natural animal that is Small or smaller. With Dragonlance supported"
if "rock gnome" in r:
    player.con += 1
    player.traits += " adept at puzzling out magic items, alchemical objects and technological devices, and starting the game with a set of tinker's tools that let them cobble together small, harmless gizmos like clockwork toys, fire starters and music boxes. In the corebook, it's explicitly stated that these should be used for playing Tinker Gnomes if you're running a Dragonlance game."
if "half elf" in r:
    player.char += 2
    player.fp += 2
    player.traits += "automatically proficient in two skills of their choice, as well as retaining the darkvision and resistances to charming and sleep of their elven ancestors. They can also grow beards, something that may have been in previous editions, but is directly addressed in this one"
    print("also get +1 to two other ability scores of their choice, this is added to your free points pool cant use it towards your charisma.")
    print("Any kind of half-elf can trade for an upgrade to darkvision and proficiency in perception, half-high elves can gain a wizard cantrip, half-wood elves can gain a five foot speed boost or an improved ability to hide in the wild, and both of the above can gain elf weapon training. Meanwhile, half-drow gain drow magic, while half-Aquatic Elves have a 30-ft swim speed. ")
if "half-orc" in r:
    player.str += 2
    player.con += 1
    player.traits += "automatically proficient in the Intimidation skill, are harder to kill than other races, and deal much nastier criticals with melee weapons."
if "halfling" in r:
    player.dex += 2
    player.traits += "lucky trait lets them reroll various results of one"
    player.traits += "they're resistant to fear effects and they can move through spaces occupied by creatures that are Medium-sized or bigger."
if "lightfoot halfling" in r:
    



attrs = vars(player)
print(attrs)