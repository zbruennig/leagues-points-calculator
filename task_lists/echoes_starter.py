from classes import Task

starter_tasks = [
    Task('Achieve Your First Level 10', '', 'Reach level 10 in any skill (not including Agility and Hitpoints)', 10),
    Task('Achieve Your First Level 20', '', 'Reach level 20 in any skill', 10),
    Task('Achieve Your First Level 5', '', 'Reach level 5 in any skill (not including Agility, Hitpoints and Runecraft)', 10),
    Task('Achieve Your First Level Up', '', 'Level up any of your skills for the first time', 10),
    Task('Burn Some Food', '', 'Burn any kind of food while trying to cook it', 10),
    Task('Burn Some Normal Logs', '', 'Burn some Normal Logs', 10),
    Task('Burn Some Oak Logs', '', 'Burn some Oak Logs', 10),
    Task('Bury Some Bones', '', 'Bury any kind of Bones', 10),
    Task('Buy Something From Trader Crewmembers', '', 'Buy something from the Trader Crewmembers', 10),
    Task('Cast Home Teleport', '', 'Cast the Home Teleport spell', 10),
    Task('Catch a Baby Impling', '', 'Catch a Baby Impling', 10),
    Task('Catch a Herring', '', 'Catch a Raw Herring whilst Fishing', 10),
    Task('Catch a Shrimp', '', 'Catch Raw Shrimp while Fishing', 10),
    Task('Catch an Anchovy', '', 'Catch a Raw Anchovy whilst Fishing', 10),
    Task('Check Your Slayer Task', '', 'Use an Enchanted Gem to check your Slayer Task', 10),
    Task('Chop Some Logs', '', 'Chop any kind of logs', 10),
    Task('Chop Some Logs With a Steel Axe', '', 'Chop any kind of logs using a Steel Axe', 10),
    Task('Clean 15 Grimy Tarromin', '', 'Clean 15 Grimy Tarromin', 10),  # New!
    Task('Clean 25 Grimy Guam Leafs', '', 'Clean 25 Grimy Guam Leafs', 10),  # New!
    Task('Complete the Leagues Tutorial', '', 'Complete the Leagues Tutorial and begin your adventure', 10),
    Task('Cook Shrimp', '', 'Cook Raw Shrimp', 10),
    Task('Craft a Leather Body', '', 'Craft a Leather Body', 10, 'a | k | z | d | m | f'),
    Task('Create a Compost Potion', '', 'Create a Compost Potion', 10),
    Task('Create an Antipoison', '', 'Create an Antipoison', 10),
    Task('Cry in a wheat field', '', 'Cry in a wheat field', 10),
    Task('Cut a Sapphire', '', 'Cut a Sapphire', 10),
    Task('Dance in a graveyard', '', 'Dance in a graveyard', 10),
    Task('Defeat a Goblin', '', 'Defeat a Goblin', 10),
    Task('Defeat a Guard', '', 'Defeat a Guard', 10),
    Task('Defeat a Moss Giant', '', 'Defeat a Moss Giant', 10),
    Task('Drink a Strength Potion', '', 'Drink a Strength Potion', 10),
    Task('Dye a cape orange', '', 'Dye a cape orange', 10),
    Task('Eat a Banana', '', 'Eat a Banana', 10),  # New!
    Task('Enter Puro Puro from Gielinor', '', 'Enter Puro Puro from a crop circle in mainland Gielinor', 10),
    Task('Enter your Player Owned House', '', 'Enter your Player Owned House', 10),
    Task('Equip a Spiny Helmet', '', 'Equip a Spiny Helmet', 10),
    Task('Equip a Studded Body and Chaps', '', 'Equip a Studded Body along with some Studded Chaps', 10),
    Task('Equip an Elemental Staff', '', 'Equip a basic elemental staff', 10),
    Task('Fletch an Oak Shortbow', '', 'Fletch an Oak Shortbow', 10),
    Task('Fletch Some Arrow Shafts', '', 'Fletch some Arrow Shafts', 10),
    Task('Kill a Necromancer', '', 'Kill a Necromancer', 10, 'k | z'),
    Task('Light a Torch', '', 'Light a Torch', 10),
    Task('Locate a Runecrafting Altar With a Talisman', '', 'Use any talisman to check the location of a Runecrafting Altar', 10),
    Task('Make an Attack Potion', '', 'Make an Attack Potion', 10),
    Task('Mine 5 Tin Ore', '', 'Mine 5 Tin Ore', 10),
    Task('Mine some Copper Ore', '', 'Mine some Copper Ore', 10),
    Task('Mine some essence', '', 'Mine some essence', 10),  # New!
    Task('Mine some Ore With a Steel Pickaxe', '', 'Mine any ore using a Steel Pickaxe', 10),
    Task('Obtain a Bird Nest', '', 'Obtain a Bird Nest whilst cutting down trees', 10),
    Task('Obtain a Casket from Fishing', '', 'Obtain a Casket from Fishing', 10),
    Task('Open the Leagues Menu', '', 'Open the Leagues Menu found within the Journal Panel', 10),
    Task('Perform a Special Attack', '', 'Perform any special attack', 10),
    Task('Pickpocket a Citizen', '', 'Pickpocket a Man or a Woman', 10),
    Task('Plant Seeds in an Allotment Patch', '', 'Plant some seeds in an Allotment patch', 10, 'a | m | k | z | t | v'),
    Task('Protect Your Crops', '', 'Pay a farmer to protect any of your crops', 10),
    Task('Purchase a Player Owned House', '', 'Purchase a Player Owned House', 10),
    Task('Rake a Farming Patch', '', 'Rake any Farming patch', 10),
    Task('Reach Combat Level 10', '', 'Reach Combat Level 10', 10),
    Task('Reach Combat Level 25', '', 'Reach Combat Level 25', 10),
    Task('Restore 5 Prayer Points at an Altar', '', 'Restore 5 or more Prayer Points at any altar', 10),
    Task('Scatter some Ashes', '', 'Scatter some Ashes', 10),  # New!
    Task('Smelt a Bronze Bar', '', 'Use a Furnace to smelt a Bronze Bar', 10),
    Task('Smelt an Iron Bar', '', 'Use a Furnace to smelt an Iron Bar', 10),
    Task('Smith a Bronze full helm', '', 'Use an Anvil to smith a Bronze full helm', 10),
    Task('Smith a Bronze plateskirt', '', 'Use an Anvil to smith a Bronze plateskirt', 10),
    Task('Snare a Bird', '', 'Catch any bird with a Bird Snare', 10),
    Task('Spin a Ball of Wool', '', 'Use a Spinning Wheel to spin a Ball of Wool', 10),
    Task('Steal a Chocolate Slice', '', 'Steal a Chocolate Slice from a Bakery Stall', 10, 'f | k | z | v'),
    Task('Steal Some Silk', '', 'Steal some silk from a silk stall', 10, 'k | z | t | v'),
    Task('Successfully Cut a Red Topaz', '', 'Successfully Cut a Red Topaz', 10),
    Task('Superhuman Strength and Improved Reflexes', '', 'Use both the Superhuman Strength prayer and the Improved Reflexes prayer at the same time', 10),
    Task('Turn any Logs Into a Plank', '', 'Use a Sawmill to turn Logs into a Plank', 10),
    Task('Use a Hat Stand', '', 'Put a hat on a hat stand, or try at least', 10),  # New!
    Task('Visit Deaths Domain', '', 'Visit Deaths Domain', 10),
    Task('Visit the Rune Essence Mine', '', 'Visit the Rune Essence Mine', 10),
    Task('Catch a Karambwanji', 's', 'Catch a Karambwanji on Karamja', 10, 's'),
    Task('Fill a Crate With Bananas', 's', 'Fill a crate with Bananas for Luthas at Musa Point', 10, 's'),
    Task('Kill a Snake in Karamja', 's', 'Kill a Snake in Karamja', 10, 's'),  # New!
    Task('Pick a Pineapple on Karamja', 's', 'Pick a Pineapple on Karamja', 10, 's'),
    Task('Receive an Agility Arena Ticket', 's', 'Receive an Agility Arena Ticket from the Brimhaven Agility Arena', 10, 's'),
    Task('Ask for a Quest from Bob', 's', 'Talk to Bob in Lumbridge axe shop and ask for a Quest', 10, 's'),  # New!
    Task('Chop a log from a potato tree', 's', 'Chop a log from a tree that is curiously in a potato field', 10, 's'),
    Task('Complete the Draynor Agility Course', 's', 'Complete a lap of the Draynor Rooftop Agility Course', 10, 's'),
    Task('Complete the Natural History Quiz', 's', 'Complete the Natural History Quiz in the Varrock Museum', 10, 's'),
    Task('Complete the Varrock Agility Course', 's', 'Complete a lap of the Varrock Rooftop Agility Course', 10, 's'),
    Task('Defeat the Lesser Demon in the Wizards Tower', 's', 'Defeat the Lesser Demon at the top of the Wizards Tower', 10, 's'),
    Task('Drink a beer in the Longhall', 's', 'Drink a beer in the Longhall in Barbarian Village', 10, 's'),  # New!
    Task('Eat an Onion', 's', 'Eat an Onion, raw', 10, 's'),  # New!
    Task('Enter Zanaris', 's', 'Enter the lost city of Zanaris', 10, 's'),
    Task('Equip an Iron dagger', 's', 'Equip an Iron dagger', 10, 's'),  # New!
    Task('Get a chair to follow you', 's', 'Get a chair to follow you', 10, 's'),
    Task('Get a haircut', 's', 'Go and get a haircut', 10, 's'),  # New!
    Task('Get your revenge against a Dark Wizard', 's', 'Get your revenge against a Dark Wizard, south of Varrock', 10, 's'),
    Task('Have Elsie tell you a story', 's', 'Have Elsie tell you a story in Varrock', 10, 's'),
    Task('Have Ned make you some rope', 's', 'Have Ned make you some rope using a ball of wool in Draynor Village', 10, 's'),
    Task('Insult Aggie the Witch', 's', 'Insult Aggie the Witch in Draynor Village', 10, 's'),
    Task('Kill a Barbarian in the Barbarian Village', 's', 'Kill a Barbarian in Barbarian Village', 10, 's'),  # New!
    Task('Kill a Chicken with your fists', 's', 'Kill a Chicken with your fists', 10, 's'),  # New!
    Task('Kill a Cow in one hit', 's', 'Kill a Cow in one hit', 10, 's'),  # New!
    Task('Kill a Duck with a fire spell', 's', 'Kill a Duck with a fire spell', 10, 's'),  # New!
    Task('Kill a Frog', 's', 'Kill a Frog', 10, 's'),  # New!
    Task('Kill a Goblin holding a spear', 's', 'Kill a Goblin holding a spear', 10, 's'),  # New!
    Task('Kill a Mugger', 's', 'Kill a Mugger', 10, 's'),  # New!
    Task('Kill a Ram', 's', 'Kill a Ram', 10, 's'),  # New!
    Task('Kill a Rat', 's', 'Kill a Rat', 10, 's'),  # New!
    Task('Kill a Spider by kicking it', 's', 'Kill a Spider in Lumbridge by kicking it', 10, 's'),  # New!
    Task('Kill an Imp with an earth spell', 's', 'Kill an Imp with an earth spell', 10, 's'),  # New!
    Task('Milk a cow', 's', 'Milk a cow in Lumbridge', 10, 's'),
    Task('Pan for an Uncut Jade', 's', 'Pan for an Uncut Jade', 10, 's'),
    Task('Pet a Stray Dog in Varrock', 's', 'Pet a Stray Dog in Varrock', 10, 's'),
    Task('Pet the Museum Camp dog', 's', 'Pet the dog in the Museum Camp on Fossil Island', 10, 's'),
    Task('Pick a Cabbage in Varrock', 's', 'Pick a Cabbage in Varrock', 10, 's'),  # New!
    Task('Pray at an Altar in Lumbridge', 's', 'Pray at an Altar in Lumbridge', 10, 's'),  # New!
    Task('Slash a web in varrock sewers', 's', 'Slash a web in Varrock sewers', 10, 's'),
    Task('Steal From the Varrock Tea Stall', 's', 'Steal from the Tea Stall in Varrock', 10, 's'),
    Task('Stroke your cat', 's', 'Get a cat and stroke it!', 10, 's'),  # New!
    Task('Take a Canoe to Champions Guild', 's', 'Take a Canoe from Lumbridge to the Champions Guild', 10, 's'),  # New!
    Task('Talk to Hans', 's', 'Talk to Hans and have him tell you how old you are', 10, 's'),  # New!
    Task('Travel to Fossil Island', 's', 'Take the Museum Barge to Fossil Island', 10, 's'),
    Task('Upset the homeless', 's', 'Anger the Tramp, in south east Varrock', 10, 's'),  # New!
    Task('Use a Fairy Ring', 's', 'Use any Fairy Ring', 10, 's'),
    Task('Use the Northern Staircase in Lumbridge', 's', 'Use the Northern Staircase in Lumbridge Castle to go upstairs from the bottom floor', 10, 's'),  # New!
    Task('1 Easy Clue Scroll', '', 'Open a Reward casket for completing an easy clue scroll', 30),
    Task('1 Elite Clue Scroll', '', 'Open a Reward casket for completing an elite clue scroll', 30),
    Task('1 Hard Clue Scroll', '', 'Open a Reward casket for completing a hard clue scroll', 30),
    Task('1 Medium Clue Scroll', '', 'Open a Reward casket for completing a medium clue scroll', 30),
    Task('15 Collection log slots', '', 'Obtain 15 unique Collection Log slots', 30),
    Task('25 Easy Clue Scrolls', '', 'Open 25 Reward caskets for completing easy clue scrolls', 30),
    Task('25 Elite Clue Scrolls', '', 'Open 25 Reward caskets for completing elite clue scrolls', 30),
    Task('25 Hard Clue Scrolls', '', 'Open 25 Reward caskets for completing hard clue scrolls', 30),
    Task('25 Medium Clue Scrolls', '', 'Open 25 Reward caskets for completing medium clue scrolls', 30),
    Task('25 Superior Slayer Encounters', '', 'Defeat 25 superior foes while on a Slayer Task', 30),
    Task('30 Collection log slots', '', 'Obtain 30 unique Collection Log slots', 30),
    Task('5 Collection log slots', '', 'Obtain 5 unique Collection Log slots', 30),
    Task('50 Collection log slots', '', 'Obtain 50 unique Collection Log slots', 30),
    Task('75 Easy Clue Scrolls', '', 'Open 75 Reward caskets for completing easy clue scrolls', 30),
    Task('75 Medium Clue Scrolls', '', 'Open 75 Reward caskets for completing medium clue scrolls', 30),
    Task('75 Superior Slayer Encounters', '', 'Defeat 75 superior foes while on a Slayer Task', 30),
    Task('Achieve Your First Level 30', '', 'Reach level 30 in any skill', 30),
    Task('Achieve Your First Level 40', '', 'Reach level 40 in any skill', 30),
    Task('Achieve Your First Level 50', '', 'Reach level 50 in any skill', 30),
    Task('Achieve Your First Level 60', '', 'Reach level 60 in any skill', 30),
    Task('Build a Mahogany Portal', '', 'Build a Mahogany Portal in a Portal Chamber in your Player Owned House', 30),
    Task('Build a Room in Your Player Owned House', '', 'Build a room in your Player Owned House', 30),
    Task('Build a Waka Canoe', '', 'Build a Waka Canoe', 30),
    Task('Build an Oak Larder', '', 'Build an Oak Larder in a Kitchen in your Player Owned House', 30),
    Task('Burn 100 Willow Logs', '', 'Burn 100 Willow Logs', 30),
    Task('Burn 25 Maple Logs', '', 'Burn 25 Maple Logs', 30),  # New!
    Task('Burn Some Coloured Logs', '', 'Burn some logs that have been coloured with a firelighter', 30),
    Task('Bury Some Wyvern or Dragon Bones', '', 'Bury either some Wyvern Bones or some Dragon Bones', 30),
    Task('Buy a candle in Lumbridge', '', 'Buy a candle in Lumbridge', 30),  # New!
    Task('Cast a Blast Spell', '', 'Cast any blast spell', 30),
    Task('Cast High Level Alchemy', '', 'Cast the High Level Alchemy spell', 30),
    Task('Catch 10 Pike', '', 'Catch 10 Pike', 30),  # New!
    Task('Catch 100 Lobsters', '', 'Catch 100 Raw Lobsters whilst Fishing', 30),
    Task('Catch 25 Sardines', '', 'Catch 25 Sardines', 30),  # New!
    Task('Catch 50 Salmon', '', 'Catch 50 Raw Salmon whilst Fishing', 30),
    Task('Catch 50 Swordfish', '', 'Catch 50 Raw Swordfish whilst Fishing', 30),
    Task('Catch a Grey Chinchompa', '', 'Catch a Grey Chinchompa', 30),  # New!
    Task('Catch a Swamp Lizard or Salamander', '', 'Catch either a Swamp Lizard or any kind of Salamander', 30, 'm | d | k | w | v'),
    Task('Check a grown Fruit Tree', '', 'Check the health of any Fruit Tree youve grown', 30),
    Task('Chop 100 Willow Logs', '', 'Chop 100 Willow Logs from Willow Trees', 30),
    Task('Chop Some Logs With a Rune Axe', '', 'Chop any kind of logs using a Rune Axe', 30),
    Task('Chop some Rising Roots', '', 'Chop some Rising Roots spawned via Forestry', 30),
    Task('Clean 50 Grimy Cadantine', '', 'Clean 50 Grimy Cadantine', 30),  # New!
    Task('Clean 50 Grimy Ranarr Weed', '', 'Clean 50 Grimy Ranarr Weed', 30),  # New!
    Task('Clean a Grimy Avantoe', '', 'Clean a Grimy Avantoe', 30),
    Task('Clean a Grimy Guam', '', 'Clean a Grimy Guam', 30),
    Task('Complete 1 Slayer Task', '', 'Complete 1 Slayer Task', 30),
    Task('Complete 10 Mahogany homes contracts', '', 'Complete 10 Mahogany homes contracts', 30, ''),  # TODO this may require grimoire, or a | f depending on specific implementation
    Task('Complete 25 Mahogany homes contracts', '', 'Complete 25 Mahogany homes contracts', 30, ''),  # TODO this may require grimoire, or a | f depending on specific implementation
    Task('Complete 50 Laps of a Rooftop Agility Course', '', 'Complete 50 laps of any Rooftop Agility Course', 30),
    Task('Complete a Mahogany homes adept contract', '', 'Complete a  Mahogany Homes adept contract', 30, 'a'),
    Task('Complete a Mahogany homes beginner contract', '', 'Complete a  Mahogany Homes beginner contract', 30, 'a'),
    Task('Complete a Mahogany homes novice contract', '', 'Complete a  Mahogany Homes novice contract', 30, 'a'),
    Task('Complete the Easy Western Provinces Diary', '', 'Complete all of the easy tasks in the  Western Provinces Achievement Diary', 30, 'k'),
    Task('Complete the Evil Bob random event', '', 'Complete the Evil Bob random event', 30),  # New!
    Task('Complete the Flowering Bush event', '', 'Complete the Flowering Bush event spawned via Forestry', 30),
    Task('Complete the Maze random event', '', 'Complete the Maze random event', 30),  # New!
    Task('Complete the Medium Western Provinces Diary', '', 'Complete all of the medium tasks in the  Western Provinces Achievement Diary', 30, 'k'),
    Task('Complete the Pheasant Forestry Event', '', 'Complete the Pheasant event spawned via Forestry', 30),
    Task('Complete the Pillory random event', '', 'Complete the Pillory random event', 30),  # New!
    Task('Complete the Pinball random event', '', 'Complete the Pinball random event', 30),  # New!
    Task('Complete the Postie Pete random event', '', 'Complete the Postie Pete random event', 30),  # New!
    Task('Complete the Prison Pete random event', '', 'Complete the Prison Pete random event', 30),  # New!
    Task('Complete the Ritual Forestry Event', '', 'Complete the Ritual event spawned via Forestry', 30),
    Task('Complete the Struggling Sapling event', '', 'Complete the Struggling Sapling event spawned via Forestry', 30),
    Task('Complete the Surprise Exam random event', '', 'Complete the Surprise Exam random event', 30),  # New!
    Task('Cook 10 Sardines', '', 'Cook 10 Raw Sardines', 30),  # New!
    Task('Cook 100 Lobsters', '', 'Cook 100 Raw Lobsters', 30),
    Task('Cook 20 Pike', '', 'Cook 20 Raw Pike', 30),  # New!
    Task('Craft 200 Essence Into Runes', '', 'Use Runecrafting Altars to craft 200 essence into runes of any type', 30),
    Task('Craft 4 Runes With 1 Essence', '', 'Use a Runecrafting Altar to craft 4 of any type of rune using a single essence', 30),
    Task('Craft a Ruby Amulet', '', 'Craft a Ruby Amulet', 30),
    Task('Craft an Emerald Ring', '', 'Craft an Emerald Ring', 30),
    Task('Craft Any Combination Rune', '', 'Use a Runecrafting Altar to craft any type of combination rune', 30),
    Task('Create a green dhide shield', '', 'Create a green dhide shield', 30),
    Task('Create a Guthix Rest Tea', '', 'Create a Guthix Rest Tea', 30, 'f | d | k'),
    Task('Cut 50 Maple Logs', '', 'Cut 50 Maple Logs', 30),  # New!
    Task('Defeat a Lesser Demon', '', 'Defeat a Lesser Demon', 30),
    Task('Defeat a Superior Slayer Creature', '', 'Defeat any Superior Slayer Creature', 30),
    Task('Eat some Purple Sweets', '', 'Eat some Purple Sweets', 30),
    Task('Equip a frog mask', '', 'Equip a frog mask', 30),
    Task('Equip a Full Adamant Set', '', 'Equip an Adamant Platebody, a Adamant Full Helm and either some Adamant Platelegs or an Adamant Plateskirt', 30),
    Task('Equip a Full Blue Dragonhide Set', '', 'Equip a Blue Dragonhide Body, some Blue Dragonhide Chaps and some Blue Dragonhide Vambraces', 30),
    Task('Equip a Full Green Dragonhide Set', '', 'Equip a Green Dragonhide Body, some Green Dragonhide Chaps and some Green Dragonhide Vambraces', 30),
    Task('Equip a Full Mithril Set', '', 'Equip a Mithril Platebody, a Mithril Full Helm and either some Mithril Platelegs or a Mithril Plateskirt', 30),
    Task('Equip a Full Red Dragonhide Set', '', 'Equip a Red Dragonhide Body, some Red Dragonhide Chaps and some Red Dragonhide Vambraces', 30),
    Task('Equip a Granite Shield', '', 'Equip a Granite Shield', 30, 'k | a | f'),
    Task('Equip a Lava Battlestaff', '', 'Equip a Lava Battlestaff', 30, 'k | a | w | m | d'),
    Task('Equip a Leaf-Bladed Sword', '', 'Equip a Leaf-Bladed Sword', 30, 'f | t'),
    Task('Equip a Maple Shortbow', '', 'Equip a Maple Shortbow', 30),
    Task('Equip a Mithril Weapon', '', 'Equip any Mithril weapon', 30),
    Task('Equip a Piece of a Mystic Set', '', 'Equip any piece of any Mystic robe set', 30),
    Task('Equip a piece of Beekeepers Outfit', '', 'Equip a piece of Beekeepers Outfit', 30),  # New!
    Task('Equip a piece of Camouflage outfit', '', 'Equip a piece of Camouflage outfit', 30),  # New!
    Task('Equip a piece of Mime Outfit', '', 'Equip a piece of Mime Outfit', 30),  # New!
    Task('Equip a piece of Zombie Outfit', '', 'Equip a piece of Zombie Outfit', 30),  # New!
    Task('Equip a Rune Weapon', '', 'Equip any Rune weapon', 30),
    Task('Equip a Trimmed Amulet', '', 'Equip a Trimmed Amulet', 30),
    Task('Equip a Willow Shield', '', 'Equip a Willow Shield', 30),
    Task('Equip a Wizard Robe and Hat', '', 'Equip any wizard robe along with any wizard hat', 30),
    Task('Equip a Yew Shortbow', '', 'Equip a Yew Shortbow', 30),
    Task('Equip an Adamant Weapon', '', 'Equip any Adamant weapon', 30),
    Task('Equip an Elemental Battlestaff or Mystic Staff', '', 'Equip either an elemental battlestaff or an elemental mystic staff', 30),
    Task('Equip full Graahk, Larupia or Kyatt', '', 'Equip a full set of Graahk, Larupia or Kyatt attire', 30),
    Task('Equip some Black armour', '', 'Equip either a Black Platebody, some Black Platelegs or a Black Full Helm', 30),
    Task('Equip some Steel armour', '', 'Equip either a Steel Platebody, some Steel Platelegs or a Steel Full Helm', 30),
    Task('Fill 15 Hard Clue Collection Log Slots', '', 'Fill 15 slots in the Hard Clue section of the Collection Log', 30),
    Task('Fill 20 Easy Clue Collection Log Slots', '', 'Fill 20 slots in the Easy Clue section of the Collection Log', 30),
    Task('Fill 20 Medium Clue Collection Log Slots', '', 'Fill 20 slots in the Medium Clue section of the Collection Log', 30),
    Task('Fill 3 Elite Clue Collection Log Slots', '', 'Fill 3 slots in the Elite Clue section of the Collection Log', 30),
    Task('Fill 3 Hard Clue Collection Log Slots', '', 'Fill 3 slots in the Hard Clue section of the Collection Log', 30),
    Task('Fill 5 Beginner Clue Collection Log Slots', '', 'Fill 5 slots in the Beginner Clue section of the Collection Log', 30),
    Task('Fill 5 Easy Clue Collection Log Slots', '', 'Fill 5 slots in the Easy Clue section of the Collection Log', 30),
    Task('Fill 5 Medium Clue Collection Log Slots', '', 'Fill 5 slots in the Medium Clue section of the Collection Log', 30),
    Task('Fill a Bucket With Supercompost', '', 'Fill a Bucket with Supercompost from a Compost Bin', 30, 'a | m | k | z | t | v'),
    Task('Fill a Large Pouch', '', 'Fill a Large Pouch with Essence', 30),
    Task('Fill a Medium S.T.A.S.H. Unit', '', 'Build a Medium S.T.A.S.H. unit and fill it with the relevant items', 30),
    Task('Find the Needle', '', 'Dig in a hay stack for a needle', 30),  # New!
    Task('Fletch 1000 arrow shafts', '', 'Fletch 1000 arrow shafts', 30),
    Task('Fletch 150 Iron Arrows', '', 'Fletch 150 Iron Arrows', 30),
    Task('Fletch 25 Oak Stocks', '', 'Fletch 25 Oak Stocks', 30),
    Task('Fletch a Willow Shortbow (u)', '', 'Fletch a Willow Shortbow (u)', 30),  # New!
    Task('Fletch some Broad Arrows or Bolts', '', 'Fletch either some Broad Arrows or some Broad Bolts', 30),
    Task('Gain 10 Unique Items From Beginner Clues', '', 'Gain 10 unique items from Beginner Clue Scroll Reward Caskets', 30),
    Task('Gain 10 Unique Items From Easy Clues', '', 'Gain 10 unique items from Easy Clue Scroll Reward Caskets', 30),
    Task('Gain 10 Unique Items From Medium Clues', '', 'Gain 10 unique items from Medium Clue Scroll Reward Caskets', 30),
    Task('Gain 20 Unique Items From Hard Clues', '', 'Gain 20 unique items from Hard Clue Scroll Reward Caskets', 30),
    Task('Gain 35 Unique Items From Easy Clues', '', 'Gain 35 unique items from Easy Clue Scroll Reward Caskets', 30),
    Task('Gain 5 Unique Items From Hard Clues', '', 'Gain 5 unique items from Hard Clue Scroll Reward Caskets', 30),
    Task('Gain a Unique Item From a Beginner Clue', '', 'Gain a unique item from a Beginner Clue Scroll Reward Casket', 30),
    Task('Gain a Unique Item From a Hard Clue', '', 'Gain a unique item from a Hard Clue Scroll Reward Casket', 30),
    Task('Gain a Unique Item From a Master Clue', '', 'Gain a unique item from a Master Clue Scroll Reward Casket', 30),
    Task('Gain a Unique Item From a Medium Clue', '', 'Gain a unique item from a Medium Clue Scroll Reward Casket', 30),
    Task('Gain a Unique Item From an Easy Clue', '', 'Gain a unique item from an Easy Clue Scroll Reward Casket', 30),
    Task('Harvest an Irit Leaf', '', 'Harvest an Irit Leaf from any Herb patch', 30, 'a | m | k | f | z | v'),
    Task('Kill 5 Bunnies', '', 'Kill 5 Bunnies', 30),  # New!  TODO do rabbits count? If not bunnies are frem only
    Task('Kill three chickens in 6 seconds', '', 'Kill three chickens in 6 seconds', 30),
    Task('Land a hoop on a stick', '', 'Successfully land a hoop on a stick in the PoH minigame', 30),  # New!
    Task('Light a Bullseye Lantern', '', 'Light a Bullseye Lantern', 30),
    Task('Make 20 Stamina Potions', '', 'Make 20 Stamina Potions', 30),
    Task('Make 30 Prayer Potions', '', 'Make 30 Prayer Potions', 30),
    Task('Make a 4 dose potion', '', 'Make any 4 dose potion using an Amulet of Chemistry', 30),
    Task('Make a Pineapple Pizza', '', 'Make a Pineapple Pizza', 30),
    Task('Make some Flour', '', 'Make some Flour in a windmill', 30),
    Task('Mine 15 coal', '', 'Mine 15 coal', 30),
    Task('Mine 50 Iron Ore', '', 'Mine 50 Iron Ore', 30),
    Task('Mine 50 Mithril Ore', '', 'Mine 50 Mithril Ore', 30),  # New!
    Task('Mine some Ore With a Rune Pickaxe', '', 'Mine any ore using a Rune Pickaxe', 30),
    Task('Obtain 800 Coins From Coin Pouches At Once', '', 'Open a stack of Coin Pouches and obtain at least 800 Coins', 30),
    Task('Obtain a Clue Geode While Mining', '', 'Obtain any kind of clue geode whilst Mining a rock', 30),
    Task('Obtain a Gem While Mining', '', 'Obtain any kind of gem whilst Mining a rock', 30),
    Task('Obtain a Mark of Grace', '', 'Obtain a Mark of Grace from any Rooftop Agility Course', 30),
    Task('Open 28 Coin Pouches At Once', '', 'Open 28 Coin Pouches at once', 30),
    Task('Open the Mystery Box', '', 'A boat is a boat, but the mystery box could be anything, even a boat!', 30),  # New!
    Task('Pickpocket a Master Farmer', '', 'Successfully pickpocket from a Master farmer', 30),
    Task('Reach a Prayer Bonus of 15', '', 'Equip enough item to reach a Prayer bonus of 15 or more', 30),
    Task('Reach Base Level 10', '', 'Reach level 10 in every skill', 30),
    Task('Reach Base Level 20', '', 'Reach level 20 in every skill', 30),
    Task('Reach Base Level 30', '', 'Reach level 30 in every skill', 30),
    Task('Reach Base Level 5', '', 'Reach level 5 in every skill', 30),
    Task('Reach Combat Level 50', '', 'Reach Combat Level 50', 30),
    Task('Reach Combat Level 75', '', 'Reach Combat Level 75', 30),
    Task('Reach Total Level 100', '', 'Reach a Total Level of 100', 30),
    Task('Reach Total Level 250', '', 'Reach a Total Level of 250', 30),
    Task('Reach Total Level 500', '', 'Reach a Total Level of 500', 30),
    Task('Reach Total Level 750', '', 'Reach a Total Level of 750', 30),
    Task('Read a prayer book near a lectern', '', 'Read a Prayer book near a lectern', 30, 'm | f'),
    Task('Scrape some blue dragonhide', '', 'Scrape some blue dragonhide', 30),
    Task('Slay 250 Creatures', '', 'Slay 250 creatures whilst on a Slayer Task', 30),
    Task('Smelt a Steel Bar', '', 'Use a Furnace to smelt a Steel Bar', 30),
    Task('Smith 10 Steel bolts (unf)', '', 'Use an Anvil to smith 10 Steel bolts (unf)', 30),
    Task('Smith 150 Iron Arrowtips', '', 'Use an Anvil to smith 150 Iron Arrowtips', 30),
    Task('Smith 250 Mithril bolts (unf)', '', 'Use an Anvil to smith 250 Mithril bolts (unf)', 30),  # New!
    Task('Smith a Steel Platebody', '', 'Use an Anvil to smith a Steel Platebody', 30),
    Task('Successfully Cook 5 Pieces of Food', '', 'Cook 5 pieces of food in a row without burning them', 30),
    Task('Teleport Using Law Runes', '', 'Cast any teleport spell that uses Law Runes', 30),
    Task('Trade a herb with Jekyll', '', 'Trade a herb with Jekyll for a potion', 30),  # New!
    Task('Use the Protect from Melee Prayer', '', 'Use the Protect from Melee Prayer', 30),
    Task('Buy a Snapdragon From Pirate Jackie the Fruit', 's', 'Buy a Snapdragon From Pirate Jackie the Fruit in Brimhaven', 30, 's'),
    Task('Catch 50 Karambwan', 's', 'Catch 50 Karambwan on Karamja', 30, 's'),
    Task('Catch a Salmon on Karamja', 's', 'Catch a Salmon on Karamja', 30, 's'),
    Task('Complete the Easy Karamja Diary', 's', 'Complete all of the easy tasks in the  Karamja Achievement Diary', 30, 's'),
    Task('Complete the Medium Karamja Diary', 's', 'Complete all of the medium tasks in the  Karamja Achievement Diary', 30, 's'),
    Task('Craft 50 Nature Runes', 's', 'Craft 50 Nature Runes from Essence at the Nature Altar', 30, 's'),
    Task('Defeat a Greater Demon on Karamja', 's', 'Defeat a Greater Demon on Karamja', 30, 's'),
    Task('Defeat a Steel Dragon on Karamja', 's', 'Defeat a Steel Dragon on Karamja', 30, 's'),
    Task('Defeat a TzHaar', 's', 'Defeat any TzHaar in Mor Ul Rek', 30, 's'),
    Task('Enter the Brimhaven Dungeon', 's', 'Enter the Brimhaven Dungeon', 30, 's'),
    Task('Enter the Tai Bwo Wannai Hardwood Grove', 's', 'Enter the Hardwood Grove in Tai Bwo Wannai', 30, 's'),
    Task('Equip a Toktz-Ket-Xil', 's', 'Equip a Toktz-Ket-Xil', 30, 's'),
    Task('Equip a Toktz-Xil-Ak', 's', 'Equip a Toktz-Xil-Ak', 30, 's'),
    Task('Equip a Toktz-Xil-Ek', 's', 'Equip a Toktz-Xil-Ek', 30, 's'),
    Task('Equip an Obsidian Cape', 's', 'Equip an Obsidian Cape', 30, 's'),
    Task('Sleep in Paramaya Inn', 's', 'Pay the barkeep to sleep in Paramaya Inn, in Shilo Village ', 30, 's'),  # New!
    Task('Take a Shortcut Across the Shilo Village River', 's', 'Use the Stepping Stones Agility Shortcut in Shilo Village ', 30, 's'),
    Task('Build a Bank on Fossil Island', 's', 'Build a Bank at the Museum Camp on Fossil Island', 30, 's'),
    Task('Catch 50 Implings in Puro-Puro', 's', 'Catch 50 Implings in Puro-Puro', 30, 's'),
    Task('Chop a Sulliuscep Cap', 's', 'Chop a Sulliuscep Cap on Fossil Island', 30, 's'),
    Task('Churn some butter', 's', 'Use a churn to make some butter', 30, 's'),
    Task('Complete 10 Laps of the Draynor Agility Course', 's', 'Complete 10 laps of the Draynor Rooftop Agility Course', 30, 's'),
    Task('Complete 10 Laps of the Varrock Agility Course', 's', 'Complete 10 laps of the Varrock Rooftop Agility Course', 30, 's'),
    Task('Complete a Volcanic Mine Game', 's', 'Complete a Volcanic Mine game on Fossil Island', 30, 's'),
    Task('Complete Demon Slayer', 's', 'Complete the  Demon Slayer  quest', 30, 's'),
    Task('Complete Sheep Shearer', 's', 'Complete the  Sheep Shearer  quest', 30, 's'),
    Task('Complete the Easy Lumbridge & Draynor Diary', 's', 'Complete all of the easy tasks in the  Lumbridge & Draynor Achievement Diary', 30, 's'),
    Task('Complete the Easy Varrock Diary', 's', 'Complete all of the easy tasks in the  Varrock Achievement Diary', 30, 's'),
    Task('Complete the Medium Lumbridge & Draynor Diary', 's', 'Complete all of the medium tasks in the  Lumbridge & Draynor Achievement Diary', 30, 's'),
    Task('Complete the Medium Varrock Diary', 's', 'Complete all of the medium tasks in the  Varrock Achievement Diary', 30, 's'),
    Task('Complete Vampyre Slayer', 's', 'Complete the  Vampyre Slayer  quest', 30, 's'),
    Task('Craft 50 Cosmic Runes', 's', 'Craft 50 Cosmic Runes from Essence at the Cosmic Altar from Essence', 30, 's'),
    Task('Craft 50 Water Runes', 's', 'Craft 50 Water Runes from Essence at the Water Altar', 30, 's'),
    Task('Defeat 50 Tormented Demons', 's', 'Defeat 50 Tormented Demons', 30, 's'),
    Task('Defeat a Fossil Island Wyvern', 's', 'Defeat any type of Wyvern on Fossil Island', 30, 's'),
    Task('Defeat a Tormented Demon', 's', 'Defeat a Tormented Demon', 30, 's'),
    Task('Defeat Bryophyta', 's', 'Defeat Bryophyta in Varrock Sewers', 30, 's'),
    Task('Defeat Obor', 's', 'Defeat Obor in Edgeville Dungeon', 30, 's'),
    Task('Defeat Scurrius', 's', 'Defeat Scurrius', 30, 's'),
    Task('Defeat Scurrius 10 times', 's', 'Defeat Scurrius 10 times', 30, 's'),
    Task('Defeat Scurrius 25 times', 's', 'Defeat Scurrius 25 times', 30, 's'),  # New!
    Task('Dismantle 20 Filled Bird Houses', 's', 'Dismantle 20 filled Bird Houses on Fossil Island', 30, 's'),
    Task('Drink From the Tears of Guthix', 's', 'Drink from the Tears of Guthix  in the Lumbridge Swamp Caves', 30, 's'),
    Task('Eat Eel sushi', 's', 'Eat the Dorgeshuun delicacy, Eel sushi', 30, 's'),  # New!
    Task('Enter the Cooks Guild', 's', 'Enter the Cooks Guild west of Varrock', 30, 's'),
    Task('Equip a Dorgeshuun Crossbow', 's', 'Equip a Dorgeshuun Crossbow', 30, 's'),
    Task('Equip a Rat Bone Weapon', 's', 'Obtain and equip any Rat Bone weaponry', 30, 's'),
    Task('Equip Some Fancy Boots or Fighting Boots', 's', 'Equip either a pair of Fancy Boots or a pair of Fighting Boots', 30, 's'),  # New!
    Task('Equip the Forestry Basket', 's', 'Obtain and Equip the Forestry Basket', 30, 's'),
    Task('Fully Unlock the Mycelium Transportation System', 's', 'Unlock every destination for the Mycelium Transportation System on Fossil Island', 30, 's'),
    Task('Get a Gem from a Gorak', 's', 'Obtain a gem drop from a Gorak', 30, 's'),  # New!
    Task('Make a pie for Romily', 's', 'Make a pie for Romily, north west of Varrock', 30, 's'),  # New!
    Task('Mine 25 Pure Essence', 's', 'Mine 25 Pure Essence', 30, 's'),  # New!
    Task('Open the Dark Chest', 's', 'Open the Dark Chest', 30, 's'),
    Task('Pickpocket a Bullseye Lantern From a Cave Goblin', 's', 'Pickpocket a Bullseye Lantern from a Cave Goblin', 30, 's'),
    Task('Pickpocket a H.A.M. Member', 's', 'Pickpocket any H.A.M. member at their hideout', 30, 's'),
    Task('Pickpocket a Varrock Guard', 's', 'Pickpocket any Varrock Guard', 30, 's'),  # New!
    Task('Provide Terry a buckle', 's', 'Show Terry Balando in the Digsite a Belt Buckle', 30, 's'),  # New!
    Task('Use a Digsite Pendant to Teleport to Fossil Island', 's', 'Use a Digsite Pendant to teleport to Fossil Island', 30, 's'),
    Task('Use the Range in Lumbridge Castle', 's', 'Use the Range in Lumbridge Castle to cook some food', 30, 's'),
    Task('Win a Game of Soul Wars', 's', 'Win a game of Soul Wars', 30, 's'),
]