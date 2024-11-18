from classes import Boss

# Going to assume that CAs which are region locked are autoed, like they were changed in the middle of leagues 4
# Applies to ones needing specific lunar/ancient/arceuus spells, items from other regions, etc.
# Basically, if the boss is available with your regions then its CAs are all doable.

bosses = [
    Boss("Abyssal Sire", "", 8, 28),
    Boss("Alchemical Hydra", "z", 12, 61, speed_tasks=2),
    Boss("Amoxliatl", "v", 9, 27, speed_tasks=2),  # New
    Boss("Araxxor", "m", 12, 60, speed_tasks=3),  # New
    Boss("Barrows", "m", 7, 14),
    Boss("Bryophyta", "", 7, 9),
    Boss("Callisto", "w", 2, 7),
    Boss("Cerberus", "a", 6, 26),
    Boss("Chaos Elemental", "w", 4, 13),
    Boss("Chaos Fanatic", "w", 4, 10),
    Boss("Crazy Archaeologist", "w", 4, 9),
    Boss("Chambers of Xeric", "z", 29, 138, speed_tasks=6),
    Boss("Chambers CM", "z", 11, 58, speed_tasks=7),
    Boss("Corporeal Beast", "w", 5, 21),
    Boss("Commander Zilyana", "a", 7, 31),
    Boss("Crystalline Hunllef", "t", 10, 46, speed_tasks=2),
    Boss("Corrupted Hunllef", "t", 11, 57, speed_tasks=2),
    Boss("Dagannoth Prime", "f", 4, 13),
    Boss("Dagannoth Rex", "f", 5, 15),
    Boss("Dagannoth Supreme", "f", 4, 13),
    Boss("Deranged Archaeologist", "", 4, 7),
    Boss("Duke Sucellus", "f", 9, 46, speed_tasks=3),  # DT2
    Boss("Fortis Colosseum", "v", 13, 67, speed_tasks=2),  # New
    Boss("General Graardor", "a", 8, 35),
    Boss("Giant Mole", "a", 6, 15),
    Boss("Grotesque Guardians", "m", 15, 59, speed_tasks=3),
    Boss("Hespori", "z", 6, 22, speed_tasks=2),
    Boss("Hueycoatl", "v", 11, 41, speed_tasks=3),  # New
    Boss("Kalphite Queen", "d", 5, 18),
    Boss("KBD", "w", 6, 12),
    Boss("Kraken", "k", 5, 18),
    Boss("Kree'arra", "a", 7, 32),
    Boss("K'ril Tsutsaroth", "a", 9, 36),
    Boss("Leviathan", "d", 9, 46, speed_tasks=3),  # DT2
    Boss("Mimic", "z", 1, 4),
    Boss("Moons of Peril", "v", 12, 33, speed_tasks=2),  # New
    Boss("Nex", "a", 11, 56),
    Boss("Nightmare", "m", 14, 67, speed_tasks=6),
    Boss("Phosani's Nightmare", "m", 10, 53, speed_tasks=2),
    Boss("Obor", "", 6, 9),
    Boss("Phantom Muspah", "f", 13, 61, speed_tasks=3),
    Boss("Sarachnis", "z", 5, 11),
    Boss("Scorpia", "w", 4, 13),
    Boss("Scurrius", "", 5, 8),  # New
    Boss("Skotizo", "z", 7, 22),
    Boss("Tempoross", "d", 8, 14),
    Boss("ToB Entry", "m", 12, 48, speed_tasks=1),
    Boss("Theatre of Blood", "m", 24, 126, speed_tasks=7),
    Boss("ToB HM", "m", 14, 83, speed_tasks=4),
    Boss("Thermy", "k", 3, 12),
    Boss("ToA Entry", "d", 5, 16),
    # Assuming timed individual rooms don't count as speed tasks, need to verify
    Boss("Tombs of Amascut", "d", 23, 104, speed_tasks=1),
    Boss("ToA Expert", "d", 23, 126, speed_tasks=2),
    Boss("TzHaar Challenges", "", 11, 55, speed_tasks=3),
    Boss("Inferno", "", 12, 69, speed_tasks=1),
    Boss("Fight Caves", "", 10, 50, speed_tasks=2),
    Boss("Vardorvis", "v", 9, 46, speed_tasks=3),  # DT2
    Boss("Venenatis", "w", 2, 7),
    Boss("Vet'ion", "w", 2, 7),
    Boss("Vorkath", "f", 11, 55, speed_tasks=2),
    Boss("Whisperer", "a", 9, 45, speed_tasks=3),  # DT2
    Boss("Wintertodt", "z", 8, 13),
    Boss("Zalcano", "t", 4, 16),
    Boss("Zulrah", "t", 9, 40, speed_tasks=3),

    # Other CAs
    Boss("Aberrant Spectre", "m | k", 1, 1),
    # Evil Chicken's Lair is off limits because locked behind Legend's Quest?
    Boss("Black Dragon", "w | a | f | t", 1, 1),
    # Can Mutated Bloodveld be killed for this?
    Boss("Bloodveld", "m | k | a | w", 1, 1),
    Boss("Fire Giant", "", 1, 1),
    # Everyone should be able to get Emberlight
    Boss("Greater Demon", "", 2, 2),
    Boss("Lizardman Shaman", "z", 2, 2),
    Boss("Into the Den of Giants", "z", 1, 1),
    # Do Varlamore wyrmlings count?
    Boss("Wyrm", "z", 1, 1),
    Boss("Hellhound", "w | z | a | k", 1, 1),
    Boss("Brutal Black Dragon", "z", 1, 2),
    Boss("Gargoyle", "m", 1, 2),
    Boss("Kurask", "f | t", 1, 2),
    # Unless some relic lets you use thralls w/o Zeah
    Boss("Sit Back and Relax", "z", 1, 2),
    Boss("Skeletal Wyvern", "a", 1, 2),
    Boss("Basilisk Knight", "f", 1, 4),
    Boss("Demonic Gorilla", "k", 2, 8),
    Boss("Fragment of Seren", "t", 1, 4, speed_tasks=1),
    Boss("Galvek", "fk", 1, 4, speed_tasks=1),
    Boss("Glough", "k", 1, 4, speed_tasks=1),
    # Assuming these are all available somehow
    Boss("Tormented Demons", "", 5, 21)  # New
]