from classes import Task

routed_tasks = [
    # Lumbridge - RAKE to at least 3 by the time we barley!
    Task('Complete the Leagues Tutorial', '', 'Complete the Leagues Tutorial and begin your adventure', 10),
    Task('Open the Leagues Menu', '', 'Open the Leagues Menu found within the Journal Panel', 10),
    Task('Achieve Your First Level Up', '', 'Level up any of your skills for the first time', 10),
    Task('Achieve Your First Level 5', '', 'Reach level 5 in any skill (not including Agility, Hitpoints and Runecraft)', 10),
    Task('Achieve Your First Level 10', '', 'Reach level 10 in any skill (not including Agility and Hitpoints)', 10),
    Task('Use the Northern Staircase in Lumbridge', 's', 'Use the Northern Staircase in Lumbridge Castle to go upstairs from the bottom floor', 10, 's'),
    # Get Anti-Dragon - 1-Spacebar
    # CLAIM RUNES, Ironman Armor if possible
    # Bank / Prepare Inv - FIGURE OUT WHAT TO BUY FROM GENERAL STORE, Bucket, Shears, Pot, Chisel, sell starting weps/shield
    Task('Kill a Spider by kicking it', 's', 'Kill a Spider in Lumbridge by kicking it', 10, 's'),  # New!
    Task('Rake a Farming Patch', '', 'Rake any Farming patch', 10),  # Store rake on leprechaun
    # Start restless ghost by talking with Father Aerick
    Task('Dance in a graveyard', '', 'Dance in a graveyard', 10),
    # BANK @Castle top floor,
    Task('Catch a Shrimp', '', 'Catch Raw Shrimp while Fishing', 10),
    Task('Cook Shrimp', '', 'Cook Raw Shrimp', 10),
    Task('Successfully Cook 5 Pieces of Food', '', 'Cook 5 pieces of food in a row without burning them', 30),

    # Zanaris
    Task('Enter Zanaris', 's', 'Enter the lost city of Zanaris', 10, 's'),
    Task('Chop Some Logs', '', 'Chop any kind of logs', 10),
    Task('Burn Some Normal Logs', '', 'Burn some Normal Logs', 10),
    # SHEAR SHEEP! Need 4 for Ned to make rope !!!FIXME BOTTLENECK
    Task('Cry in a wheat field', '', 'Cry in a wheat field', 10),
    # Grab a grain in the wheat field to make flour with
    Task('Make some Flour', '', 'Make some Flour in a windmill', 30),
    # Bank / Prepare Inv, Food, Bucket, Runes, Shears for possible wool KC. Dramen/ADS/Ironman armor equipped
    Task('Use a Fairy Ring', 's', 'Use any Fairy Ring', 10, 's'),  # Edgeville - DKR
    # Can kill a rat in 2nd room of floor 2
    Task('Equip Some Fancy Boots or Fighting Boots', 's', 'Equip either a pair of Fancy Boots or a pair of Fighting Boots', 30, 's'),  # New!
    Task('Cast Home Teleport', '', 'Cast the Home Teleport spell', 10),

    # North to Varrock - shear sheep on the way?? RAKE!
    Task('Milk a cow', 's', 'Milk a cow in Lumbridge', 10, 's'),
    Task('Find the Needle', '', 'Dig in a hay stack for a needle', 30),  # New, can do with potato tree if you cba
    # NEED to pick up an egg for cook's assistant here
    Task('Kill a Chicken with your fists', 's', 'Kill a Chicken with your fists', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    # If spear goblin is up, do that now by safespotting on fence
    Task('Kill a Ram', 's', 'Kill a Ram', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    # Grab Redberries

    # Varrock - RAKE!
    # Can bank if you need to here, tbd. Bank redberries, wool, flour, milk, needle
    # BUY RUNES - 200 Air, 200 Mind, 30 earth, 30 water = like 2k
    # Go to southeast Biohazard area, buy hat from fancy clothes store
    Task('Get a haircut', 's', 'Go and get a haircut', 10, 's'),  # New!
    Task('Purchase a Player Owned House', '', 'Purchase a Player Owned House', 10),
    Task('Kill a Rat', 's', 'Kill a Rat', 10, 's'),  # New!
    Task('Use a Hat Stand', '', 'Put a hat on a hat stand, or try at least', 10),  # New!
    Task('Pet a Stray Dog in Varrock', 's', 'Pet a Stray Dog in Varrock', 10, 's'),  # TODO is he not always in range
    Task('Defeat a Guard', '', 'Defeat a Guard', 10),  # Use ones by tea stall  # !!!FIXME BOTTLENECK
    Task('Bury Some Bones', '', 'Bury any kind of Bones', 10),
    Task('Upset the homeless', 's', 'Anger the Tramp, in south east Varrock', 10, 's'),  # 2 option
    # Kill him from inside Yarlo's house, he won't enter
    Task('Kill a Mugger', 's', 'Kill a Mugger', 10, 's'),  # New!
    Task('Pick a Cabbage in Varrock', 's', 'Pick a Cabbage in Varrock', 10, 's'),  # New!
    # Buy Fire, should have about 5.5k left, tbd also get air
    Task('Equip an Elemental Staff', '', 'Equip a basic elemental staff', 10),
    Task('Stroke your cat', 's', 'Get a cat and stroke it!', 10, 's'),  # New, -100 for Gertrude

    # Minigame to Soul Wars, Combat Mastery 1, Edgeville
    Task('Defeat a Moss Giant', '', 'Defeat a Moss Giant', 10),  # Or just do on isle of souls?
    Task('Mine some Copper Ore', '', 'Mine some Copper Ore', 10), # Tin ore on jatizso just get the copper
    # Don't do clay if you're worried about demon?
    Task('Kill an Imp with an earth spell', 's', 'Kill an Imp with an earth spell', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    Task('Scatter some Ashes', '', 'Scatter some Ashes', 10),  # New!
    Task('Visit Deaths Domain', '', 'Visit Deaths Domain', 10),
    # Can bank if needed - need pickaxe for essence, axe for tree spirits
    Task('Kill a Goblin holding a spear', 's', 'Kill a Goblin holding a spear', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    Task('Defeat a Goblin', '', 'Defeat a Goblin', 10),

    # Wizards Tower - DIS
    Task('Defeat a Lesser Demon', '', 'Defeat a Lesser Demon', 30),  # !!!FIXME BOTTLENECK
    Task('Defeat the Lesser Demon in the Wizards Tower', 's', 'Defeat the Lesser Demon at the top of the Wizards Tower', 10, 's'),  # !!!FIXME BOTTLENECK
    # Do restless ghost step
    Task('Visit the Rune Essence Mine', '', 'Visit the Rune Essence Mine', 10),
    Task('Mine some essence', '', 'Mine some essence', 10),  # New!

    # Enchanted Valley - BKQ, Nature Spirits for a while maybe get lucky
    Task('Kill 5 Bunnies', '', 'Kill 5 Bunnies', 30),  # New!  # !!!FIXME BOTTLENECK
    Task('Achieve Your First Level 20', '', 'Reach level 20 in any skill', 10),

    # Abyssal Area - ALR, get an air/earth/water? (or any) talisman
    # Task('Locate a Runecrafting Altar With a Talisman', '', 'Use any talisman to check the location of a Runecrafting Altar', 10),  # !!!FIXME BOTTLENECK

    # CKR for Karams, need net
    Task('Catch a Karambwanji', 's', 'Catch a Karambwanji on Karamja', 10, 's'),

    # Leagues Tele to Karamja / Brimhaven - RAKE Hardwood / Fruit tree.
    Task('Pick a Pineapple on Karamja', 's', 'Pick a Pineapple on Karamja', 10, 's'),
    Task('Kill a Snake in Karamja', 's', 'Kill a Snake in Karamja', 10, 's'),  # New!
    Task('Enter the Brimhaven Dungeon', 's', 'Enter the Brimhaven Dungeon', 30, 's'),  # -875, around 4.7k
    Task('Enter your Player Owned House', '', 'Enter your Player Owned House', 10),
    Task('Build a Room in Your Player Owned House', '', 'Build a room in your Player Owned House', 30),  # -1000, around 3.7k
    Task('Buy Something From Trader Crewmembers', '', 'Buy something from the Trader Crewmembers', 10),  # Glassblowing pipe + Hammer for later
    # Rake!
    # Task('Receive an Agility Arena Ticket', 's', 'Receive an Agility Arena Ticket from the Brimhaven Agility Arena', 10, 's'),  # Do this later

    # Shilo - get bait/bronze bars/slayer task, calc bronze needed. Fare probably around 60 coins.
    Task('Equip a Spiny Helmet', '', 'Equip a Spiny Helmet', 10),  # -800, around 2.9k
    Task('Check Your Slayer Task', '', 'Use an Enchanted Gem to check your Slayer Task', 10),
    # 300 bait, 200 feathers. -1300, around 1.6k
    # Bronze Bars 12g each, buy 50ish. -600, around 1k. Buy a torch + anything else you forgot
    Task('Light a Torch', '', 'Light a Torch', 10),
    # Bank bronze bars and set up inv for - Restless Ghost skull, magic gear, wool, cooks assistant items
    # Can buy beer in inn too, or the lumby one
    Task('Sleep in Paramaya Inn', 's', 'Pay the barkeep to sleep in Paramaya Inn, in Shilo Village ', 30, 's'),  # New!

    # Lumbridge 2 - RAKE!
    Task('Pickpocket a Citizen', '', 'Pickpocket a Man or a Woman', 10),
    Task('Open 28 Coin Pouches At Once', '', 'Open 28 Coin Pouches at once', 30),
    Task('Obtain 800 Coins From Coin Pouches At Once', '', 'Open a stack of Coin Pouches and obtain at least 800 Coins', 30),  # Guards+
    Task('Talk to Hans', 's', 'Talk to Hans and have him tell you how old you are', 10, 's'),  # New!
    Task('Reach Combat Level 10', '', 'Reach Combat Level 10', 10),
    # Turn in cooks assistant
    Task('Burn Some Food', '', 'Burn any kind of food while trying to cook it', 10),
    Task('Use the Range in Lumbridge Castle', 's', 'Use the Range in Lumbridge Castle to cook some food', 30, 's'),
    Task('Ask for a Quest from Bob', 's', 'Talk to Bob in Lumbridge axe shop and ask for a Quest', 10, 's'),  # New!
    Task('Superhuman Strength and Improved Reflexes', '', 'Use both the Superhuman Strength prayer and the Improved Reflexes prayer at the same time', 10),
    Task('Pray at an Altar in Lumbridge', 's', 'Pray at an Altar in Lumbridge', 10, 's'),  # New!
    Task('Restore 5 Prayer Points at an Altar', '', 'Restore 5 or more Prayer Points at any altar', 10),
    Task('Spin a Ball of Wool', '', 'Use a Spinning Wheel to spin a Ball of Wool', 10),
    Task('Kill a Duck with a fire spell', 's', 'Kill a Duck with a fire spell', 10, 's'),  # New!
    Task('Catch 25 Sardines', '', 'Catch 25 Sardines', 30),  # Lumby / Draynor, Lvl 5 Rod + Bait
    Task('Cook 10 Sardines', '', 'Cook 10 Raw Sardines', 30),  # Lvl 5, Lumbridge / Musa / Draynor, Fishing Rod + Bait
    Task('Catch a Herring', '', 'Catch a Raw Herring whilst Fishing', 10),  # Lvl 10, Lumby or Draynor, Fishing Rod + Bait
    Task('Catch 10 Pike', '', 'Catch 10 Pike', 30),  # Lumbridge / Barbarian / Shilo, Lvl 25, Fishing Rod + Bait
    Task('Cook 20 Pike', '', 'Cook 20 Raw Pike', 30),  # Lumbridge / Barbarian / Shilo, Lvl 25, Fishing Rod + Bait
    Task('Catch 50 Salmon', '', 'Catch 50 Raw Salmon whilst Fishing', 30),  # Lvl 30, Fly Fishing + Feather, Lumby/Shilo/Barb Village
    # Can buy bait from Lumby shop if not 40
    Task('Kill a Frog', 's', 'Kill a Frog', 10, 's'),  # New!
    Task('Buy a candle in Lumbridge', '', 'Buy a candle in Lumbridge', 30),  # Should have gp from thieving if not do HAM first
    # THIEVING TO 38
    Task('Pickpocket a H.A.M. Member', 's', 'Pickpocket any H.A.M. member at their hideout', 30, 's'),  # Iron Dagger, Steel Pickaxe, Steel Axe
    Task('Equip an Iron dagger', 's', 'Equip an Iron dagger', 10, 's'),  # From HAM
    # Task('Chop a log from a potato tree', 's', 'Chop a log from a tree that is curiously in a potato field', 10, 's'),  # !!!FIXME BOTTLENECK

    # Draynor - Start Vampire slayer, buy Chronicle and some wines, get seeds, barley esp. Do req fishing before Musa Point
    # Enough agility for Varrock if 8x. Cook some food.
    Task('Insult Aggie the Witch', 's', 'Insult Aggie the Witch in Draynor Village', 10, 's'),
    Task('Have Ned make you some rope', 's', 'Have Ned make you some rope using a ball of wool in Draynor Village', 10, 's'),
    # THIEVING TO 40
    Task('Pickpocket a Master Farmer', '', 'Successfully pickpocket from a Master farmer', 30),
    # Do enough to get 30 agility
    Task('Complete the Draynor Agility Course', 's', 'Complete a lap of the Draynor Rooftop Agility Course', 10, 's'),
    Task('Complete 10 Laps of the Draynor Agility Course', 's', 'Complete 10 laps of the Draynor Rooftop Agility Course', 30, 's'),
    Task('Obtain a Mark of Grace', '', 'Obtain a Mark of Grace from any Rooftop Agility Course', 30),

    # Frem should be unlocked now - Leagues tele there - claim seal of passage
    # Fill inv with clay, switch to steel pick from HAM once 6 (can't equip)
    Task('Mine some Ore With a Steel Pickaxe', '', 'Mine any ore using a Steel Pickaxe', 10),
    # Lunar Isle
    Task('Switch to the Lunar Spellbook', 'f', 'Switch to the Lunar Spellbook.', 10, 'f'),
    # Switch back after
    Task('Use the Bank on Lunar Isle', 'f', 'Use the Bank on Lunar Isle.', 10, 'f'),
    # Buy a law rune or 5, and some chaos runes from Baba Yaga
    # Get kicked back to Rellekka and mine more clay
    Task('Use the Bank on Jatizso', 'f', 'Use the Bank on Jatizso.', 10, 'f'),
    Task('Mine 5 Tin Ore', '', 'Mine 5 Tin Ore', 10),
    # Neitiznot
    Task('Use the Bank on Neitiznot', 'f', 'Use the Bank on Neitiznot.', 10, 'f'),
    Task('Kill a Yak', 'f', 'Kill a Yak.', 10, 'f'),
    Task('Smelt a Bronze Bar', '', 'Use a Furnace to smelt a Bronze Bar', 10),

    # Varrock - Figure out Kudos, get Trowel / Specimen Brush / Specimen Jar. Progress Vampyre slayer and have beer for barb village
    Task('Teleport Using Law Runes', '', 'Cast any teleport spell that uses Law Runes', 30),
    Task('Smith a Bronze full helm', '', 'Use an Anvil to smith a Bronze full helm', 10),
    Task('Smith a Bronze plateskirt', '', 'Use an Anvil to smith a Bronze plateskirt', 10),
    # Up to 45 or maybe 50, make sure you have enough gp for daddys home, including 100 nails
    Task('Steal From the Varrock Tea Stall', 's', 'Steal from the Tea Stall in Varrock', 10, 's'),
    # IMPORTANT! Need to use Tea on Elsie
    Task('Have Elsie tell you a story', 's', 'Have Elsie tell you a story in Varrock', 10, 's'),
    Task('Slash a web in varrock sewers', 's', 'Slash a web in Varrock sewers', 10, 's'),  # Maybe skip?
    Task('Pickpocket a Varrock Guard', 's', 'Pickpocket any Varrock Guard', 30, 's'),  # New!
    Task('Achieve Your First Level 30', '', 'Reach level 30 in any skill', 30),
    Task('Achieve Your First Level 40', '', 'Reach level 40 in any skill', 30),
    Task('Achieve Your First Level 50', '', 'Reach level 50 in any skill', 30),
    Task('Reach Total Level 100', '', 'Reach a Total Level of 100', 30),

    Task('Complete the Varrock Agility Course', 's', 'Complete a lap of the Varrock Rooftop Agility Course', 10, 's'),
    Task('Complete 10 Laps of the Varrock Agility Course', 's', 'Complete 10 laps of the Varrock Rooftop Agility Course', 30, 's'),
    # Task('Complete 50 Laps of a Rooftop Agility Course', '', 'Complete 50 laps of any Rooftop Agility Course', 30),  # if needed
    # TODO Understand Kudos
    Task('Complete the Natural History Quiz', 's', 'Complete the Natural History Quiz in the Varrock Museum', 10, 's'),

    # Fossil Island / Daddys Home
    Task('Provide Terry a buckle', 's', 'Show Terry Balando in the Digsite a Belt Buckle', 30, 's'),  # Bring Trowel/Specimen Brush+Jar
    Task('Pan for an Uncut Jade', 's', 'Pan for an Uncut Jade', 10, 's'),  # Panning tray is in panning spot
    # Grab certificate for RFD
    Task('Turn any Logs Into a Plank', '', 'Use a Sawmill to turn Logs into a Plank', 10),
    Task('Travel to Fossil Island', 's', 'Take the Museum Barge to Fossil Island', 10, 's'),
    Task('Pet the Museum Camp dog', 's', 'Pet the dog in the Museum Camp on Fossil Island', 10, 's'),
    Task('Build a Bank on Fossil Island', 's', 'Build a Bank at the Museum Camp on Fossil Island', 30, 's'),
    Task('Fully Unlock the Mycelium Transportation System', 's', 'Unlock every destination for the Mycelium Transportation System on Fossil Island', 30, 's'),

    # Chronicle to Champion's Guild. Barley Seeds, gp
    Task('Get your revenge against a Dark Wizard', 's', 'Get your revenge against a Dark Wizard, south of Varrock', 10, 's'),
    Task('Protect Your Crops', '', 'Pay a farmer to protect any of your crops', 10),  # Buy compost, plant barley and prot
    Task('Kill a Cow in one hit', 's', 'Kill a Cow in one hit', 10, 's'),  # New!

    # Minigame Tele, Mining, and Bank at Soul Wars, down to Barbarian Village, or just run idk
    Task('Drink a beer in the Longhall', 's', 'Drink a beer in the Longhall in Barbarian Village', 10, 's'),  # New!
    Task('Kill a Barbarian in the Barbarian Village', 's', 'Kill a Barbarian in Barbarian Village', 10, 's'),  # New!
    # Train crafting to 20 with pottery. How do I do pottery again?. Need 3270 with Sheep Shearer xp to hit 20.

    # Leagues Tele to Rellekka, thieve fremmys if not 50 -> Keldagrim
    Task('Steal a Chocolate Slice', '', 'Steal a Chocolate Slice from a Bakery Stall.', 10, 'f | k | z | v'),
    Task('Achieve Your First Level 60', '', 'Reach level 60 in any skill.', 80),
    Task('Achieve Your First Level 70', '', 'Reach level 70 in any skill.', 80),
    Task('Cut a Sapphire', '', 'Cut a Sapphire', 10),
    Task('Achieve Your First Level 80', '', 'Reach level 80 in any skill.', 80),
    # Silver Stall to 75
    # Gem Stall to 90+?

    # Draynor 2
    Task('Fletch Some Arrow Shafts', '', 'Fletch some Arrow Shafts', 10),
    Task('Burn Some Oak Logs', '', 'Burn some Oak Logs', 10),
    Task('Fletch an Oak Shortbow', '', 'Fletch an Oak Shortbow', 10),
    Task('Get a chair to follow you', 's', 'Get a chair to follow you', 10, 's'),  # if ringing next do later
    Task('Complete Vampyre Slayer', 's', 'Complete the  Vampyre Slayer  quest', 30, 's'),  # bring stuff! know safespot. Need a hammer

    # Lumbridge 3 - You should buy wool from Frem for Sheep Shearer
    Task('Complete Sheep Shearer', 's', 'Complete the  Sheep Shearer  quest', 30, 's'),
    Task('Churn some butter', 's', 'Use a churn to make some butter', 30, 's'),  # Need 38 cooking and milk (or at least a bucket),
    Task('Take a Canoe to Champions Guild', 's', 'Take a Canoe from Lumbridge to the Champions Guild', 10, 's'),  # 12 WC

    # Over to Musa Point by leagues tele or tzhaar ring BLP - Fishing here
    Task('Defeat a TzHaar', 's', 'Defeat any TzHaar in Mor Ul Rek', 30, 's'),
    Task('Eat a Banana', '', 'Eat a Banana', 10),  # New!
    Task('Fill a Crate With Bananas', 's', 'Fill a crate with Bananas for Luthas at Musa Point', 10, 's'),  # !!!FIXME BOTTLENECK
    Task('Catch 100 Lobsters', '', 'Catch 100 Raw Lobsters whilst Fishing', 30),  # Musa Point / IoS by fairy ring, Lvl 40, Cage or regions
    Task('Cook 100 Lobsters', '', 'Cook 100 Raw Lobsters', 30),  # Musa Point / IoS by fairy ring, Lvl 40, Cage or regions
    Task('Catch 50 Swordfish', '', 'Catch 50 Raw Swordfish whilst Fishing', 30),  # Lvl 50, Harpoon, Musa Point

    # Shilo
    Task('Take a Shortcut Across the Shilo Village River', 's', 'Use the Stepping Stones Agility Shortcut in Shilo Village ', 30, 's'),
    Task('Catch a Salmon on Karamja', 's', 'Catch a Salmon on Karamja', 30, 's'),  # Lvl 30, Fly Fishing + Feather, Shilo

    # Beneath Lumbridge
    # Do RFD another cooks quest
    Task('Eat Eel sushi', 's', 'Eat the Dorgeshuun delicacy, Eel sushi', 30, 's'),  # New!
    Task('Drink From the Tears of Guthix', 's', 'Drink from the Tears of Guthix  in the Lumbridge Swamp Caves', 30, 's'),

    # From gem stall
    Task('Craft a Ruby Amulet', '', 'Craft a Ruby Amulet', 30),
    Task('Craft an Emerald Ring', '', 'Craft an Emerald Ring', 30),

    # OK GO START either Farming/BH or PVMing NOW - Figure out how to get a Agility Potion(4)
    # At 12x consider woodcutting or mining while farming

    # In Fremmy land
    Task('Mine 15 coal', '', 'Mine 15 coal', 30),
    Task('Mine 50 Iron Ore', '', 'Mine 50 Iron Ore', 30),
    Task('Smelt an Iron Bar', '', 'Use a Furnace to smelt an Iron Bar', 10),
    Task('Obtain a Clue Geode While Mining', '', 'Obtain any kind of clue geode whilst Mining a rock', 30),
    Task('Obtain a Gem While Mining', '', 'Obtain any kind of gem whilst Mining a rock', 30),
    Task('Fletch 150 Iron Arrows', '', 'Fletch 150 Iron Arrows', 30),

    # Honk mimimimimimi we live in Draynor
    Task('Equip a Wizard Robe and Hat', '', 'Equip any wizard robe along with any wizard hat', 30),
    Task('Chop some Rising Roots', '', 'Chop some Rising Roots spawned via Forestry', 30),
    Task('Fletch 25 Oak Stocks', '', 'Fletch 25 Oak Stocks', 30),
    Task('Fletch 1000 arrow shafts', '', 'Fletch 1000 arrow shafts', 30),
    Task('Burn 100 Willow Logs', '', 'Burn 100 Willow Logs', 30),
    Task('Chop 100 Willow Logs', '', 'Chop 100 Willow Logs from Willow Trees', 30),
    Task('Fletch a Willow Shortbow (u)', '', 'Fletch a Willow Shortbow (u)', 30),  # New!
    Task('Equip a Willow Shield', '', 'Equip a Willow Shield', 30),
    Task('Mine 25 Pure Essence', 's', 'Mine 25 Pure Essence', 30, 's'),  # New!
    Task('Obtain a Bird Nest', '', 'Obtain a Bird Nest whilst cutting down trees', 10),
    # Isle of souls?
    Task('Cut 50 Maple Logs', '', 'Cut 50 Maple Logs', 30),  # New!
    Task('Burn 25 Maple Logs', '', 'Burn 25 Maple Logs', 30),  # New!
    Task('Build a Waka Canoe', '', 'Build a Waka Canoe', 30),
    Task('Bury Some Wyvern or Dragon Bones', '', 'Bury either some Wyvern Bones or some Dragon Bones', 30),

    # Start PVM?
    Task('Complete 1 Slayer Task', '', 'Complete 1 Slayer Task', 30),
    Task('Complete Demon Slayer', 's', 'Complete the  Demon Slayer  quest', 30, 's'),
    Task('Defeat a Greater Demon on Karamja', 's', 'Defeat a Greater Demon on Karamja', 30, 's'),

    # Some Kourend stuff
    Task('Kill a Necromancer', '', 'Kill a Necromancer', 10, 'k | z'),
    Task('Steal Some Silk', '', 'Steal some silk from a silk stall', 10, 'k | z | t | v'),
    Task('Drink a LizardKicker', 'z', 'Drink a LizardKicker.', 10, 'z'),
    Task('Equip a Protest Banner', 'z', 'Equip a Protest Banner.', 10, 'z'),
    Task('Steal 1 Artefact', 'z', 'Steal an artefact for Captain Khaled in Piscarilius.', 10, 'z'),
    Task('Turn in 1 Library Book', 'z', 'Find and turn in a book in the Arceuus Library.', 10, 'z'),
    Task('Turn in 25 Library Books', 'z', 'Find and turn in 25 books in the Arceuus Library.', 30, 'z'),
    Task('Turn in 50 Library Books', 'z', 'Find and turn in 50 books in the Arceuus Library.', 30, 'z'),
    Task('Headbang with KetSal Kuk', 'z', 'Headbang with KetSal Kuk.', 30, 'z'),
    Task('Complete Getting Ahead', 'z', 'Complete  Getting Ahead  quest.', 30, 'z'),  # 26 Construction
    Task('Inferior Demonbane Demon Kill', 'z', 'Kill a demon using the Inferior Demonbane spell.', 30, 'z'),
    Task('Enter the Cooks Guild', 's', 'Enter the Cooks Guild west of Varrock', 30, 's'),  # Buy chefs hat in Shayzien
    Task('Cast a Blast Spell', '', 'Cast any blast spell', 30),
    Task('Cast High Level Alchemy', '', 'Cast the High Level Alchemy spell', 30),

    # "At this point I probably have done these:"
    Task('1 Easy Clue Scroll', '', 'Open a Reward casket for completing an easy clue scroll', 30),
    Task('Gain a Unique Item From an Easy Clue', '', 'Gain a unique item from an Easy Clue Scroll Reward Casket', 30),
    Task('Equip a Mithril Weapon', '', 'Equip any Mithril weapon', 30),  # Vampyre slayer gets you there
    Task('Clean a Grimy Guam', '', 'Clean a Grimy Guam', 30),
    Task('Gain a Unique Item From an Easy Clue', '', 'Gain a unique item from an Easy Clue Scroll Reward Casket', 30),
    Task('Build an Oak Larder', '', 'Build an Oak Larder in a Kitchen in your Player Owned House', 30),

    # Can shopscape these
    Task('Smelt a Steel Bar', '', 'Use a Furnace to smelt a Steel Bar', 30),
    Task('Smith 10 Steel bolts (unf)', '', 'Use an Anvil to smith 10 Steel bolts (unf)', 30),
    Task('Smith a Steel Platebody', '', 'Use an Anvil to smith a Steel Platebody', 30),

    # Maybe defensive cast post books
    Task('Equip some Black armour', '', 'Equip either a Black Platebody, some Black Platelegs or a Black Full Helm', 30),
    Task('Equip some Steel armour', '', 'Equip either a Steel Platebody, some Steel Platelegs or a Steel Full Helm', 30),

    # At 12x with likely bankers note, if not there do at 8x
    # Task('Achieve Your First Level 90', '', 'Reach level 90 in any skill.', 200),
    # Task('Achieve Your First Level 95', '', 'Reach level 95 in any skill.', 200),
    # Task('Reach Level 99 Thieving', '', 'Reach level 99 in your Thieving skill.', 200),
]

points_so_far = sum(task.points for task in routed_tasks)
print(f'Tasks: {len(routed_tasks)}, Points: {points_so_far}')

wont_route = [
    Task('Catch a Baby Impling', '', 'Catch a Baby Impling', 10),
    Task('Craft a Leather Body', '', 'Craft a Leather Body', 10, 'a | k | z | d | m | f'),
    Task('Clean 15 Grimy Tarromin', '', 'Clean 15 Grimy Tarromin', 10),  # New!
    Task('Clean 25 Grimy Guam Leafs', '', 'Clean 25 Grimy Guam Leafs', 10),  # New!
    Task('Create a Compost Potion', '', 'Create a Compost Potion', 10),
    Task('Create an Antipoison', '', 'Create an Antipoison', 10),
    Task('Enter Puro Puro from Gielinor', '', 'Enter Puro Puro from a crop circle in mainland Gielinor', 10),
    Task('Equip a Studded Body and Chaps', '', 'Equip a Studded Body along with some Studded Chaps', 10),  # 20 ranged/def
    Task('Equip an Elemental Battlestaff or Mystic Staff', '', 'Equip either an elemental battlestaff or an elemental mystic staff', 30),
    Task('1 Elite Clue Scroll', '', 'Open a Reward casket for completing an elite clue scroll', 30),
    Task('1 Hard Clue Scroll', '', 'Open a Reward casket for completing a hard clue scroll', 30),
    Task('1 Medium Clue Scroll', '', 'Open a Reward casket for completing a medium clue scroll', 30),
    Task('15 Collection log slots', '', 'Obtain 15 unique Collection Log slots', 30),
    Task('5 Collection log slots', '', 'Obtain 5 unique Collection Log slots', 30),
    Task('Make 20 Stamina Potions', '', 'Make 20 Stamina Potions', 30),
    Task('Make a 4 dose potion', '', 'Make any 4 dose potion using an Amulet of Chemistry', 30),
    Task('Clean 50 Grimy Cadantine', '', 'Clean 50 Grimy Cadantine', 30),  # New!
    Task('Clean 50 Grimy Ranarr Weed', '', 'Clean 50 Grimy Ranarr Weed', 30),  # New!
    Task('Clean a Grimy Avantoe', '', 'Clean a Grimy Avantoe', 30),
    Task('Fill 5 Beginner Clue Collection Log Slots', '', 'Fill 5 slots in the Beginner Clue section of the Collection Log', 30),
    Task('Fill 5 Easy Clue Collection Log Slots', '', 'Fill 5 slots in the Easy Clue section of the Collection Log', 30),
    Task('Fill 5 Medium Clue Collection Log Slots', '', 'Fill 5 slots in the Medium Clue section of the Collection Log', 30),
    Task('Fill a Medium S.T.A.S.H. Unit', '', 'Build a Medium S.T.A.S.H. unit and fill it with the relevant items', 30),
    Task('Gain a Unique Item From a Beginner Clue', '', 'Gain a unique item from a Beginner Clue Scroll Reward Casket', 30),
    Task('Gain a Unique Item From a Hard Clue', '', 'Gain a unique item from a Hard Clue Scroll Reward Casket', 30),
    Task('Gain a Unique Item From a Master Clue', '', 'Gain a unique item from a Master Clue Scroll Reward Casket', 30),
    Task('Gain a Unique Item From a Medium Clue', '', 'Gain a unique item from a Medium Clue Scroll Reward Casket', 30),
    Task('Reach Base Level 10', '', 'Reach level 10 in every skill', 30),
    Task('Reach Base Level 20', '', 'Reach level 20 in every skill', 30),
    Task('Reach Base Level 30', '', 'Reach level 30 in every skill', 30),
    Task('Reach Base Level 5', '', 'Reach level 5 in every skill', 30),
    Task('Read a prayer book near a lectern', '', 'Read a Prayer book near a lectern', 30, 'm | f'),
    Task('Equip a Yew Shortbow', '', 'Equip a Yew Shortbow', 30),
    Task('Use a Digsite Pendant to Teleport to Fossil Island', 's', 'Use a Digsite Pendant to teleport to Fossil Island', 30, 's'),
    Task('Catch a Grey Chinchompa', '', 'Catch a Grey Chinchompa', 30),  # New!
    Task('Check a grown Fruit Tree', '', 'Check the health of any Fruit Tree youve grown', 30),
    Task('Chop Some Logs With a Rune Axe', '', 'Chop any kind of logs using a Rune Axe', 30),
    Task('Equip a Maple Shortbow', '', 'Equip a Maple Shortbow', 30),
    Task('Trade a herb with Jekyll', '', 'Trade a herb with Jekyll for a potion', 30),  # New!
    Task('Make an Attack Potion', '', 'Make an Attack Potion', 10),
    Task('Drink a Strength Potion', '', 'Drink a Strength Potion', 10),
    Task('Equip an Adamant Weapon', '', 'Equip any Adamant weapon', 30),
    Task('Equip a Rune Weapon', '', 'Equip any Rune weapon', 30),
    Task('Defeat a Steel Dragon on Karamja', 's', 'Defeat a Steel Dragon on Karamja', 30, 's'),
    Task('Enter the Tai Bwo Wannai Hardwood Grove', 's', 'Enter the Hardwood Grove in Tai Bwo Wannai', 30, 's'),
    Task('Equip a Toktz-Ket-Xil', 's', 'Equip a Toktz-Ket-Xil', 30, 's'),
    Task('Equip a Toktz-Xil-Ak', 's', 'Equip a Toktz-Xil-Ak', 30, 's'),
    Task('Equip a Toktz-Xil-Ek', 's', 'Equip a Toktz-Xil-Ek', 30, 's'),
    Task('Equip an Obsidian Cape', 's', 'Equip an Obsidian Cape', 30, 's'),
    Task('Use the Protect from Melee Prayer', '', 'Use the Protect from Melee Prayer', 30),
    Task('Mine some Ore With a Rune Pickaxe', '', 'Mine any ore using a Rune Pickaxe', 30),
]

fishing_cooking = [
    Task('Catch 50 Karambwan', 's', 'Catch 50 Karambwan on Karamja', 30, 's'),
]

starter_tasks = [
    Task('Dye a cape orange', '', 'Dye a cape orange', 10),
    Task('Obtain a Casket from Fishing', '', 'Obtain a Casket from Fishing', 10),
    Task('Perform a Special Attack', '', 'Perform any special attack', 10),
    Task('Reach Combat Level 25', '', 'Reach Combat Level 25', 10),
    Task('Snare a Bird', '', 'Catch any bird with a Bird Snare', 10),
    Task('Successfully Cut a Red Topaz', '', 'Successfully Cut a Red Topaz', 10),
    Task('Eat an Onion', 's', 'Eat an Onion, raw', 10, 's'),  # New!
    Task('Craft Any Combination Rune', '', 'Use a Runecrafting Altar to craft any type of combination rune', 30),
    Task('Kill three chickens in 6 seconds', '', 'Kill three chickens in 6 seconds', 30),
    Task('Land a hoop on a stick', '', 'Successfully land a hoop on a stick in the PoH minigame', 30),  # New!
    Task('Make a Pineapple Pizza', '', 'Make a Pineapple Pizza', 30),
    Task('Reach a Prayer Bonus of 15', '', 'Equip enough item to reach a Prayer bonus of 15 or more', 30),
    Task('Reach Combat Level 50', '', 'Reach Combat Level 50', 30),
    Task('Reach Combat Level 75', '', 'Reach Combat Level 75', 30),
    Task('Reach Total Level 250', '', 'Reach a Total Level of 250', 30),
    Task('Reach Total Level 500', '', 'Reach a Total Level of 500', 30),
    Task('Reach Total Level 750', '', 'Reach a Total Level of 750', 30),
    Task('Scrape some blue dragonhide', '', 'Scrape some blue dragonhide', 30),
    Task('Buy a Snapdragon From Pirate Jackie the Fruit', 's', 'Buy a Snapdragon From Pirate Jackie the Fruit in Brimhaven', 30, 's'),
    Task('Complete the Easy Karamja Diary', 's', 'Complete all of the easy tasks in the  Karamja Achievement Diary', 30, 's'),
    Task('Complete the Medium Karamja Diary', 's', 'Complete all of the medium tasks in the  Karamja Achievement Diary', 30, 's'),
    Task('Catch 50 Implings in Puro-Puro', 's', 'Catch 50 Implings in Puro-Puro', 30, 's'),
    Task('Chop a Sulliuscep Cap', 's', 'Chop a Sulliuscep Cap on Fossil Island', 30, 's'),
    Task('Complete a Volcanic Mine Game', 's', 'Complete a Volcanic Mine game on Fossil Island', 30, 's'),
    Task('Complete the Easy Lumbridge & Draynor Diary', 's', 'Complete all of the easy tasks in the  Lumbridge & Draynor Achievement Diary', 30, 's'),
    Task('Complete the Easy Varrock Diary', 's', 'Complete all of the easy tasks in the  Varrock Achievement Diary', 30, 's'),
    Task('Complete the Medium Lumbridge & Draynor Diary', 's', 'Complete all of the medium tasks in the  Lumbridge & Draynor Achievement Diary', 30, 's'),
    Task('Complete the Medium Varrock Diary', 's', 'Complete all of the medium tasks in the  Varrock Achievement Diary', 30, 's'),
    Task('Craft 50 Cosmic Runes', 's', 'Craft 50 Cosmic Runes from Essence at the Cosmic Altar from Essence', 30, 's'),
    Task('Craft 50 Water Runes', 's', 'Craft 50 Water Runes from Essence at the Water Altar', 30, 's'),
    Task('Defeat Bryophyta', 's', 'Defeat Bryophyta in Varrock Sewers', 30, 's'),
    Task('Defeat Obor', 's', 'Defeat Obor in Edgeville Dungeon', 30, 's'),
    Task('Defeat Scurrius', 's', 'Defeat Scurrius', 30, 's'),
    Task('Equip a Dorgeshuun Crossbow', 's', 'Equip a Dorgeshuun Crossbow', 30, 's'),
    Task('Equip a Rat Bone Weapon', 's', 'Obtain and equip any Rat Bone weaponry', 30, 's'),
    Task('Make a pie for Romily', 's', 'Make a pie for Romily, north west of Varrock', 30, 's'),  # New!
    Task('Open the Dark Chest', 's', 'Open the Dark Chest', 30, 's'),
    Task('Pickpocket a Bullseye Lantern From a Cave Goblin', 's', 'Pickpocket a Bullseye Lantern from a Cave Goblin', 30, 's'),
]

unassigned_task_names = [t.name for t in starter_tasks]
routed_task_names = [t.name for t in routed_tasks]
# print([t for t in unassigned_task_names if t in routed_task_names])

task_map = {}
for name in routed_task_names:
    if name in task_map.keys():
        print(f'DUPLICATE TASK: {name}')
    task_map[name] = True

current_points = 0

r1_tasks_needed = 60
r2_tasks_needed = 140
t2_points_needed = 500
t3_points_needed = 1200
t4_points_needed = 2000

t2_points_reached = False
t3_points_reached = False
t4_points_reached = False

for idx, task in enumerate(routed_tasks):
    if idx == r1_tasks_needed:
        print(f"~~{r1_tasks_needed} TASKS COMPLETED~~")
    if idx == r2_tasks_needed:
        print(f"~~{r2_tasks_needed} TASKS COMPLETED~~")
    if not t2_points_reached and current_points >= t2_points_needed:
        t2_points_reached = True
        print(f"~~{current_points} PTS ACQUIRED - T2 MET~~")
    if not t3_points_reached and current_points >= t3_points_needed:
        t3_points_reached = True
        print(f"~~{current_points} PTS ACQUIRED - T3 MET~~")
    if not t4_points_reached and current_points >= t4_points_needed:
        t4_points_reached = True
        print(f"~~{current_points} PTS ACQUIRED - T4 MET~~")
    print(f'{task.points}: {task.name}')
    current_points += task.points