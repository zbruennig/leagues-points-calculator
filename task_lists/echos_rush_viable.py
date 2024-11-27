from classes import Task, Notice, Header, Banking

routed_tasks = [
    Header('Lumbridge - Remember to RAKE! I will be reminding you often because idk how to do early farming'),
    Task('Complete the Leagues Tutorial', '', 'Complete the Leagues Tutorial and begin your adventure', 10),
    Task('Open the Leagues Menu', '', 'Open the Leagues Menu found within the Journal Panel', 10),
    Task('Achieve Your First Level Up', '', 'Level up any of your skills for the first time', 10),
    Task('Achieve Your First Level 5', '', 'Reach level 5 in any skill (not including Agility, Hitpoints and Runecraft)', 10),
    Task('Achieve Your First Level 10', '', 'Reach level 10 in any skill (not including Agility and Hitpoints)', 10),
    Task('Use the Northern Staircase in Lumbridge', 's', 'Use the Northern Staircase in Lumbridge Castle to go upstairs from the bottom floor', 10, 's'),
    Notice('Claim Dramen Staff'),
    Notice('Claim Echo Harpoon'),
    Notice('Claim Anti-Dragon Shield'),
    Notice('Claim free runes and ironman armor'),
    Notice('Bank / Prepare Inv - Buy 2 Buckets, Shears, Pot, from general store, sell starting weps/shield'),
    Task('Kill a Spider by kicking it', 's', 'Kill a Spider in Lumbridge by kicking it', 10, 's'),  # New!
    Task('Rake a Farming Patch', '', 'Rake any Farming patch', 10),  # Store rake on leprechaun
    Task('Dance in a graveyard', '', 'Dance in a graveyard', 10),
    Banking('@Castle top floor, need shears/harpoon/dramen equipped, axe, pot, pickaxe for copper maybe'),
    Notice('Really try to mine a copper here so you don\'t have to run all the way thru Isle of Souls later'),
    Task('Catch a Shrimp', '', 'Catch Raw Shrimp while Fishing', 10),
    Task('Cook Shrimp', '', 'Cook Raw Shrimp', 10),
    Task('Successfully Cook 5 Pieces of Food', '', 'Cook 5 pieces of food in a row without burning them', 30),

    Header('Zanaris'),
    Notice('Pick up egg if available by Evil Chicken Lair'),
    Task('Enter Zanaris', 's', 'Enter the lost city of Zanaris', 10, 's'),
    Task('Chop Some Logs', '', 'Chop any kind of logs', 10),
    Task('Burn Some Normal Logs', '', 'Burn some Normal Logs', 10),
    Notice('SHEAR SHEEP! Need 4 for Ned to make rope'),  # !!!FIXME BOTTLENECK
    Task('Cry in a wheat field', '', 'Cry in a wheat field', 10),
    Notice('Grab a grain in the wheat field to make flour with'),
    Task('Make some Flour', '', 'Make some Flour in a windmill', 30),
    Banking('Prepare Inv, Food, Bucket, Runes, Shears for possible wool KC. Dramen/ADS/Ironman armor equipped. Also Buckets + Runes'),

    Header('Stronghold Rush'),
    Notice('Fairy Ring to Edgeville - DKR'),
    Task('Use a Fairy Ring', 's', 'Use any Fairy Ring', 10, 's'),
    Notice('Can kill a rat in 2nd room of floor 2'),
    Task('Equip Some Fancy Boots or Fighting Boots', 's', 'Equip either a pair of Fancy Boots or a pair of Fighting Boots', 30, 's'),  # New!
    Task('Cast Home Teleport', '', 'Cast the Home Teleport spell', 10),

    Header('North to Varrock - shear sheep on the way if its available and you dont have any wool, RAKE!'),
    Task('Milk a cow', 's', 'Milk a cow in Lumbridge', 10, 's'),
    Task('Find the Needle', '', 'Dig in a hay stack for a needle', 30),  # New, can do with potato tree if you cba
    Notice('NEED to pick up an egg for cook\'s assistant here if you didn\'t grab the Zanaris one'),
    Task('Kill a Chicken with your fists', 's', 'Kill a Chicken with your fists', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    Notice('Rake Hops Patch'),
    Notice('If spear goblin is up, do that now by safespotting on fence'),
    Task('Kill a Ram', 's', 'Kill a Ram', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    Notice('Grab 3x Redberries'),

    Header('Varrock - RAKE!'),
    Banking('Can bank if you need to. Bank redberries, wool, flour, milk, needle'),
    Notice('BUY RUNES - 250 Air, 150 Mind, 30 earth, 30 water = like 2k'),
    Notice('Talk to Minas upstairs in the museum to get kudos'),
    Task('Get a haircut', 's', 'Go and get a haircut', 10, 's'),  # New!
    Notice('Go to southeast Biohazard area, buy hat from fancy clothes store'),
    Task('Purchase a Player Owned House', '', 'Purchase a Player Owned House', 10),
    Task('Kill a Rat', 's', 'Kill a Rat', 10, 's'),  # New!
    Task('Use a Hat Stand', '', 'Put a hat on a hat stand, or try at least', 10),  # New!
    Task('Pet a Stray Dog in Varrock', 's', 'Pet a Stray Dog in Varrock', 10, 's'),  # TODO is he not always in range
    Task('Defeat a Guard', '', 'Defeat a Guard', 10),  # Use ones by tea stall  # !!!FIXME BOTTLENECK
    Task('Bury Some Bones', '', 'Bury any kind of Bones', 10),
    Task('Upset the homeless', 's', 'Anger the Tramp, in south east Varrock', 10, 's'),  # 2 option
    Notice('Kill Mugger from inside Yarlo\'s house, he won\'t enter'),
    Task('Kill a Mugger', 's', 'Kill a Mugger', 10, 's'),  # New!
    Task('Pick a Cabbage in Varrock', 's', 'Pick a Cabbage in Varrock', 10, 's'),  # New!
    Notice('Can buy iron dagger from sword shop for task (would do later) and slash web if going to sewers'),
    Notice('Buy a Red Cape from Thessalia'),
    Notice('Buy Fire Staff, should have about 5.5k left'),
    Task('Equip an Elemental Staff', '', 'Equip a basic elemental staff', 10),
    Notice('You should try to do moss giant in sewers if it isnt crowded yet'),
    Notice('If going to sewers you can buy a cat later'),
    Task('Stroke your cat', 's', 'Get a cat and stroke it!', 10, 's'),  # New, -100 for Gertrude

    Header('Minigame to Soul Wars, Combat Mastery 1, Edgeville'),
    Notice('If you mined copper in Lumbridge and killed the Moss Giant already, just go to Edgeville'),
    Task('Defeat a Moss Giant', '', 'Defeat a Moss Giant', 10),  # Or just do on isle of souls?
    Notice('Want to do most of our mining in Frem because those spots will be quieter, copper is just annoying there'),
    Task('Mine some Copper Ore', '', 'Mine some Copper Ore', 10), # Tin ore on jatizso just get the copper
    Task('Kill an Imp with an earth spell', 's', 'Kill an Imp with an earth spell', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    Task('Scatter some Ashes', '', 'Scatter some Ashes', 10),  # New!
    Task('Visit Deaths Domain', '', 'Visit Deaths Domain', 10),
    Banking('Can bank if needed - need pickaxe for essence, axe for tree spirits, harpoon for karams'),
    Task('Kill a Goblin holding a spear', 's', 'Kill a Goblin holding a spear', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    Notice('There\'s a spear goblin south of the edgeville fairy ring'),
    Task('Defeat a Goblin', '', 'Defeat a Goblin', 10),

    Header('Wizards Tower - DIS'),
    Task('Defeat a Lesser Demon', '', 'Defeat a Lesser Demon', 30),  # !!!FIXME BOTTLENECK
    Task('Defeat the Lesser Demon in the Wizards Tower', 's', 'Defeat the Lesser Demon at the top of the Wizards Tower', 10, 's'),  # !!!FIXME BOTTLENECK
    Task('Visit the Rune Essence Mine', '', 'Visit the Rune Essence Mine', 10),
    Task('Mine some essence', '', 'Mine some essence', 10),  # New!

    Header('Enchanted Valley - BKQ, Nature Spirits for a while maybe get lucky on a rune axe.'),
    Notice('You\'re mostly here for the bunnies though just fight tree spirits if they need to respawn'),
    Task('Kill 5 Bunnies', '', 'Kill 5 Bunnies', 30),  # New!  # !!!FIXME BOTTLENECK
    Task('Achieve Your First Level 20', '', 'Reach level 20 in any skill', 10),

    Header('Abyssal Area - ALR, get an air/earth/water? (or any) talisman'),
    Notice('This can take a while if you are frustrated just move on'),
    Task('Locate a Runecrafting Altar With a Talisman', '', 'Use any talisman to check the location of a Runecrafting Altar', 10),  # !!!FIXME BOTTLENECK

    Header('CKR for Karams, need harpoon'),
    Task('Catch a Karambwanji', 's', 'Catch a Karambwanji on Karamja', 10, 's'),
    Notice('Pick up a seaweed, drop and pick it up til diary step is completed. Keep it.'),

    Header('Leagues Tele to Karamja / Brimhaven - RAKE Hardwood / Fruit tree.'),
    Task('Pick a Pineapple on Karamja', 's', 'Pick a Pineapple on Karamja', 10, 's'),
    Task('Kill a Snake in Karamja', 's', 'Kill a Snake in Karamja', 10, 's'),  # New!
    Task('Enter the Brimhaven Dungeon', 's', 'Enter the Brimhaven Dungeon', 30, 's'),  # -875, around 4.7k
    Task('Enter your Player Owned House', '', 'Enter your Player Owned House', 10),
    Task('Build a Room in Your Player Owned House', '', 'Build a room in your Player Owned House', 30),  # -1000, around 3.7k
    Notice('Rake!'),  # TODO add more rakes
    Notice('Buy 11 bananas, glassblowing pipe, hammer, bucket of sand, seaweed if you don\'t have'),
    Task('Buy Something From Trader Crewmembers', '', 'Buy something from the Trader Crewmembers', 10),  # Glassblowing pipe + Hammer for later
    Notice('Cart to Shilo'),

    Header('Shilo - get bait/bronze bars/slayer task, calc bronze needed. Fare probably around 60 coins.'),
    Task('Equip a Spiny Helmet', '', 'Equip a Spiny Helmet', 10),  # -800, around 2.9k
    Task('Check Your Slayer Task', '', 'Use an Enchanted Gem to check your Slayer Task', 10),
    Notice('300 bait, 200 feathers. -1300, around 1.6k left'),
    Notice('Bronze Bars 12g each, buy 50ish. -600, around 1k. Buy a torch + anything else you forgot'),
    Task('Light a Torch', '', 'Light a Torch', 10),
    Notice('Bank bronze bars and set up inv for - magic gear, wool, cooks assistant items'),
    Notice('Can buy beer in inn too, or the lumby one'),
    Task('Sleep in Paramaya Inn', 's', 'Pay the barkeep to sleep in Paramaya Inn, in Shilo Village ', 30, 's'),  # New!

    Header('Lumbridge 2 - RAKE!'),
    Notice('Rake!'),  # TODO add more rakes
    Task('Ask for a Quest from Bob', 's', 'Talk to Bob in Lumbridge axe shop and ask for a Quest', 10, 's'),  # New!
    Task('Kill a Duck with a fire spell', 's', 'Kill a Duck with a fire spell', 10, 's'),  # New!
    Task('Talk to Hans', 's', 'Talk to Hans and have him tell you how old you are', 10, 's'),  # New!
    Task('Pray at an Altar in Lumbridge', 's', 'Pray at an Altar in Lumbridge', 10, 's'),  # New!
    Task('Pickpocket a Citizen', '', 'Pickpocket a Man or a Woman', 10),
    Task('Open 28 Coin Pouches At Once', '', 'Open 28 Coin Pouches at once', 30),
    Notice('You get 800 here because DD triples your pouch cap, else you get this at Varrock guards later'),
    Task('Obtain 800 Coins From Coin Pouches At Once', '', 'Open a stack of Coin Pouches and obtain at least 800 Coins', 30),  # Guards+
    Task('Reach Combat Level 10', '', 'Reach Combat Level 10', 10),
    Notice('Turn in cooks assistant'),
    Task('Burn Some Food', '', 'Burn any kind of food while trying to cook it', 10),
    Notice('Use a cooked food on a range to burn it for Animal Wrangler-ers'),
    Task('Use the Range in Lumbridge Castle', 's', 'Use the Range in Lumbridge Castle to cook some food', 30, 's'),
    Banking('Wool, Harpoon, Magic Equip, Money, Axe'),
    Task('Spin a Ball of Wool', '', 'Use a Spinning Wheel to spin a Ball of Wool', 10),
    Notice('Do all this fishing at the lumbridge spot, stay til it\'s all done and you have level 40.'),
    Task('Catch an Anchovy', '', 'Catch a Raw Anchovy whilst Fishing', 10),
    Task('Catch 25 Sardines', '', 'Catch 25 Sardines', 30),  # Lumby / Draynor, Lvl 5 Rod + Bait
    Task('Cook 10 Sardines', '', 'Cook 10 Raw Sardines', 30),  # Lvl 5, Lumbridge / Musa / Draynor, Fishing Rod + Bait
    Task('Catch a Herring', '', 'Catch a Raw Herring whilst Fishing', 10),  # Lvl 10, Lumby or Draynor, Fishing Rod + Bait
    Task('Catch 10 Pike', '', 'Catch 10 Pike', 30),  # Lumbridge / Barbarian / Shilo, Lvl 25, Fishing Rod + Bait
    Task('Cook 20 Pike', '', 'Cook 20 Raw Pike', 30),  # Lumbridge / Barbarian / Shilo, Lvl 25, Fishing Rod + Bait
    Task('Catch 50 Salmon', '', 'Catch 50 Raw Salmon whilst Fishing', 30),  # Lvl 30, Fly Fishing + Feather, Lumby/Shilo/Barb Village
    Notice('Can buy bait from Lumby shop if not 40'),
    Task('Kill a Frog', 's', 'Kill a Frog', 10, 's'),  # New!
    Task('Buy a candle in Lumbridge', '', 'Buy a candle in Lumbridge', 30),  # Should have gp from thieving if not do HAM first
    Notice('Clean out your inventory for HAM thieving'),
    Notice('Rake!'),  # TODO add more rakes
    Notice('THIEVING TO 38, also get steel tools, iron dagger, grimy guam.'),
    Task('Clean a Grimy Guam', '', 'Clean a Grimy Guam', 30),
    Notice('Hold on to the Guam'),
    Task('Pickpocket a H.A.M. Member', 's', 'Pickpocket any H.A.M. member at their hideout', 30, 's'),  # Iron Dagger, Steel Pickaxe, Steel Axe
    Task('Equip an Iron dagger', 's', 'Equip an Iron dagger', 10, 's'),  # From HAM
    Notice('Skip below if it is crowded'),
    Task('Chop a log from a potato tree', 's', 'Chop a log from a tree that is curiously in a potato field', 10, 's'),  # !!!FIXME BOTTLENECK

    Header('Draynor - Start Vampire slayer, buy Chronicle and some wines, get seeds, barley esp. Prep fishing for Musa Point.'),
    Notice('Cook your food at 1 of the 1000 fires inevitably in Draynor.'),
    Notice('Aggie will take 20 coins from you'),
    Task('Insult Aggie the Witch', 's', 'Insult Aggie the Witch in Draynor Village', 10, 's'),
    Task('Have Ned make you some rope', 's', 'Have Ned make you some rope using a ball of wool in Draynor Village', 10, 's'),
    Notice('Buy chronicle and a couple of charges'),
    Notice('THIEVING TO 40'),
    Task('Pickpocket a Master Farmer', '', 'Successfully pickpocket from a Master farmer', 30),
    Notice('Do enough laps to get 30 agility'),
    Task('Complete the Draynor Agility Course', 's', 'Complete a lap of the Draynor Rooftop Agility Course', 10, 's'),
    Task('Complete 10 Laps of the Draynor Agility Course', 's', 'Complete 10 laps of the Draynor Rooftop Agility Course', 30, 's'),
    Task('Obtain a Mark of Grace', '', 'Obtain a Mark of Grace from any Rooftop Agility Course', 30),
    Notice('Buy some seeds for birdhouses/barley'),
    Notice('Cook some food if you don\'t have any you will run by some hostile mobs next'),

    Header('Frem should be unlocked now - Leagues tele there. Bring 3-4 food, bronze pick, steel pick. - claim seal of passage'),
    Notice('Grab 2-3 onions from field in SE Rellekka'),
    Task('Steal a Cow bell in Rellekka', 'f', 'Steal a Cow bell in Rellekka', 30, 'f'),  # New!
    Task('Eat an Onion', 's', 'Eat an Onion, raw', 10, 's'),  # New!
    Notice('Fill inv with clay from Relekka mining spot, switch to steel pick from HAM once 6 (can\'t equip yet)'),
    Notice('Drop the bronze pick once you reach level 6'),
    Task('Mine some Ore With a Steel Pickaxe', '', 'Mine any ore using a Steel Pickaxe', 10),
    Task('Pick up Snapegrass', 'f', 'Pick up Snapegrass from Lunar Isle', 10, 'f'),  # New!
    Header('Lunar Isle'),
    Task('Switch to the Lunar Spellbook', 'f', 'Switch to the Lunar Spellbook.', 10, 'f'),
    Notice('Switch back after'),
    Task('Use the Bank on Lunar Isle', 'f', 'Use the Bank on Lunar Isle.', 10, 'f'),
    Notice('Buy a law rune or 5, 1/2 cosmic for enchanting, and some chaos and death runes from Baba Yaga.'),
    Notice('If you have gp, buy some natures too, to start alching as you run. Otherwise come back when you do.'),
    Banking('Clear your inv of everything except for the steel pick, bank your seal of passage'),
    Notice('Get kicked back to Rellekka and mine more clay'),
    Task('Use the Bank on Jatizso', 'f', 'Use the Bank on Jatizso.', 10, 'f'),
    Notice('Enter the Jatizso mine'),
    Task('Mine 5 Tin Ore', '', 'Mine 5 Tin Ore', 10),
    Header('Neitiznot'),
    Banking('Buy all your wool from the guy in the bank house, 20 for Fred, 4 for Ned = 24 needed'),
    Task('Use the Bank on Neitiznot', 'f', 'Use the Bank on Neitiznot.', 10, 'f'),
    Task('Kill a Yak', 'f', 'Kill a Yak.', 10, 'f'),
    Task('Smelt a Bronze Bar', '', 'Use a Furnace to smelt a Bronze Bar', 10),

    Header('Varrock - Figure out your Kudos situation, get Trowel / Specimen Brush / Specimen Jar. Progress Vampyre slayer and have beer for barb village'),
    Task('Teleport Using Law Runes', '', 'Cast any teleport spell that uses Law Runes', 30),
    Notice('Consider making knives to begin range training'),
    Task('Smith a Bronze full helm', '', 'Use an Anvil to smith a Bronze full helm', 10),
    Task('Smith a Bronze plateskirt', '', 'Use an Anvil to smith a Bronze plateskirt', 10),
    Notice('Rake!'),  # TODO add more rakes
    Task('Pickpocket a Varrock Guard', 's', 'Pickpocket any Varrock Guard', 30, 's'),  # New!
    Notice('Best Dirty Deeds spot I could find is on the roof of Varrock Castle'),
    Notice('Thieving up to 45 or maybe 50, make sure you have enough gp for daddys home, including 100 nails'),
    Task('Steal From the Varrock Tea Stall', 's', 'Steal from the Tea Stall in Varrock', 10, 's'),
    Notice('IMPORTANT! Need to use Tea on Elsie'),
    Task('Have Elsie tell you a story', 's', 'Have Elsie tell you a story in Varrock', 10, 's'),
    Task('Slash a web in varrock sewers', 's', 'Slash a web in Varrock sewers', 10, 's'),  # Maybe skip?
    Task('Achieve Your First Level 30', '', 'Reach level 30 in any skill', 30),
    Task('Achieve Your First Level 40', '', 'Reach level 40 in any skill', 30),
    Task('Achieve Your First Level 50', '', 'Reach level 50 in any skill', 30),
    Task('Reach Total Level 100', '', 'Reach a Total Level of 100', 30),
    Notice('Consider going back to Baba Yaga for nature runes to 0-time alch. Remember your seal of passage. You can Compass back'),

    Task('Complete the Varrock Agility Course', 's', 'Complete a lap of the Varrock Rooftop Agility Course', 10, 's'),
    Task('Complete 10 Laps of the Varrock Agility Course', 's', 'Complete 10 laps of the Varrock Rooftop Agility Course', 30, 's'),
    Notice('Below if needed, skip otherwise'),
    Task('Complete 50 Laps of a Rooftop Agility Course', '', 'Complete 50 laps of any Rooftop Agility Course', 30),  # if needed
    Notice('Clean til you find digsite pendant for kudos. Claim rewards from info clerk once you have 3, or 2 if you talked to Minas before Frem. Don\'t talk to Minas yet!'),
    Notice('Definitely do quiz so you can start birdhouses'),
    Task('Complete the Natural History Quiz', 's', 'Complete the Natural History Quiz in the Varrock Museum', 10, 's'),

    Header('Fossil Island / Daddys Home'),
    Notice('Clue Compass to Digsite Q'),
    Notice('Bring Trowel/Specimen Brush'),
    Notice('Search Sacks for a Jar'),
    Notice('Use trowel on the level 3 area (big one in the middle) til you find a belt buckle.'),
    Notice('Clue Compass to Exam Centre R'),
    Task('Provide Terry a buckle', 's', 'Show Terry Balando in the Digsite a Belt Buckle', 30, 's'),  # Bring Trowel/Specimen Brush+Jar
    Notice('Grab lvl 3 certificate for RFD'),
    Notice('Panning tray is in a tent near the panning spot'),
    Task('Pan for an Uncut Jade', 's', 'Pan for an Uncut Jade', 10, 's'),  # Panning tray is in panning spot
    Notice('Complete Daddys Home'),
    Task('Complete a Mahogany homes beginner contract', '', 'Complete a  Mahogany Homes beginner contract', 30, ''),
    Task('Complete a Mahogany homes novice contract', '', 'Complete a  Mahogany Homes novice contract', 30, ''),
    Notice('Use Varrock Gypsy compass and Lumberyard compass'),
    Notice('Turn in your digsite cert for a fruit blast, do RFD on your own time'),
    Task('Turn any Logs Into a Plank', '', 'Use a Sawmill to turn Logs into a Plank', 10),
    Task('Travel to Fossil Island', 's', 'Take the Museum Barge to Fossil Island', 10, 's'),
    Task('Pet the Museum Camp dog', 's', 'Pet the dog in the Museum Camp on Fossil Island', 10, 's'),
    Task('Build a Bank on Fossil Island', 's', 'Build a Bank at the Museum Camp on Fossil Island', 30, 's'),
    Task('Fully Unlock the Mycelium Transportation System', 's', 'Unlock every destination for the Mycelium Transportation System on Fossil Island', 30, 's'),

    Header('Leagues Tele to Brimhaven with money, saw, hammer, steel bars, oak planks, molten glass (seaweed + bucket of sand)'),
    Notice('Can sell the silk you get from Daddys Home reward to lumberyard'),
    Notice('Make workshop / clockwork bench and make 5 clockworks'),
    Notice('Try to be kinda diligent about your birdhouse runs'),

    Header('Chronicle to Champion\'s Guild. Bring Barley Seeds, gp, runes/staff'),
    Task('Get your revenge against a Dark Wizard', 's', 'Get your revenge against a Dark Wizard, south of Varrock', 10, 's'),
    Notice('Buy compost, plant barley and protect'),
    Task('Protect Your Crops', '', 'Pay a farmer to protect any of your crops', 10),  # Buy compost, plant barley and prot
    Task('Kill a Cow in one hit', 's', 'Kill a Cow in one hit', 10, 's'),  # New!

    Header('Clue compass X to Edgeville, or just run idk'),
    Notice('Make Soft Clay at Doris\'s house'),
    Task('Drink a beer in the Longhall', 's', 'Drink a beer in the Longhall in Barbarian Village', 10, 's'),  # New!
    Task('Kill a Barbarian in the Barbarian Village', 's', 'Kill a Barbarian in Barbarian Village', 10, 's'),  # New!
    Notice('Train crafting to 20 with pottery. Need 3270 (lvl 17 + progress) with Sheep Shearer xp to hit 20.'),
    Notice('You probably have enough clay to make the highest level item always, but if you are short cups are most xp per clay but annoying.'),

    Header('Leagues Tele to Rellekka, thieve fremmys if not 50 -> Keldagrim'),
    Notice('Bring some empty buckets'),
    Task('Fill up 20 buckets of sand in Rellekka', 'f', 'Fill up 20 buckets of sand in Rellekka', 30, 'f'),  # New!
    Task('Steal a Fish', 'f', 'Steal some fish from a Fish stall', 30, 'f'),  # New!
    Task('Loot a Lyre', 'f', 'Kill someone and obtain their Lyre', 30, 'f'),  # New!
    Task('Defeat a Troll in the Fremennik Province', 'f', 'Defeat a Troll in the Fremennik Province', 30, 'f'),
    Notice('Enter Blast Furnace to unlock minigame tele'),
    Task('Steal a Chocolate Slice', '', 'Steal a Chocolate Slice from a Bakery Stall.', 10, 'f | k | z | v'),
    Task('Steal a Wooden Stock', 'f', 'Steal a Wooden Stock from a Crossbow Stall', 30, 'f'),  # New!
    Task('Steal a Chisel', 'f', 'Steal a Chisel from a crafting stall in Keldagrim', 30, 'f'),  # New!
    Task('Achieve Your First Level 60', '', 'Reach level 60 in any skill.', 80),
    Task('Achieve Your First Level 70', '', 'Reach level 70 in any skill.', 80),
    Task('Cut a Sapphire', '', 'Cut a Sapphire', 10),
    Task('Steal From a Gem Stall', '', 'Steal from a Gem Stall', 80),
    Task('Achieve Your First Level 80', '', 'Reach level 80 in any skill.', 80),
    Notice('Keep one of each mould from the crafting stall'),
    Notice('Silver Stall to 75'),
    Notice('Gem Stall to 80, we stop here to finish off 99 at 12x.'),
    Notice('Cut and drop gems here, keep a couple of each for tasks'),
    Notice('The main reason we want 75 now is the longer we wait on thieving the higher chance a non Dodgy Dealer can grief you.'),

    Header('Lighthouse'),
    Task('Equip a Damaged God book', 'f', 'Equip a Damaged God book', 30, 'f'),  # New!
    Task('Defeat a Dagannoth in the Fremennik Province', 'f', 'Defeat a Dagannoth in the Fremennik Province', 30, 'f'),

    Header('Draynor 2'),
    Notice('Compass to W (Miss Schism), this is your best keybound banking tele'),
    Notice('Have Aggie Make Red and Yellow dyes using Redberries/Onions'),
    Task('Dye a cape orange', '', 'Dye a cape orange', 10),
    Task('Fletch Some Arrow Shafts', '', 'Fletch some Arrow Shafts', 10),
    Task('Burn Some Oak Logs', '', 'Burn some Oak Logs', 10),
    Task('Fletch an Oak Shortbow', '', 'Fletch an Oak Shortbow', 10),
    Notice('Head to draynor manor with a hammer, clue compass S. Bring some food.'),
    Task('Get a chair to follow you', 's', 'Get a chair to follow you', 10, 's'),
    Notice('You can setup a corner trap by running to southwest of room (on south wall) and running on top of Count til he moves south. Then move West.'),
    Task('Complete Vampyre Slayer', 's', 'Complete the  Vampyre Slayer  quest', 30, 's'),  # bring stuff! know safespot. Need a hammer

    Banking('Compass to W, grab 20 wool, bucket of milk (or just a bucket), and axe'),

    Header('Lumbridge 3 - You should have from Frem for Sheep Shearer'),
    Task('Complete Sheep Shearer', 's', 'Complete the  Sheep Shearer  quest', 30, 's'),
    Notice('Need 38 cooking and milk (or at least a bucket)'),
    Task('Churn some butter', 's', 'Use a churn to make some butter', 30, 's'),
    Task('Take a Canoe to Champions Guild', 's', 'Take a Canoe from Lumbridge to the Champions Guild', 10, 's'),  # 12 WC

    Banking('W on Compass and grab your bananas (eat one if you haven\'t yet), harpoon, and runes'),

    Header('Clue Compass to TzHaar area'),
    Notice('Walk into fight caves and leave for diary'),
    Task('Defeat a TzHaar', 's', 'Defeat any TzHaar in Mor Ul Rek', 30, 's'),
    Notice('Pick 5 bananas for diary'),
    Task('Eat a Banana', '', 'Eat a Banana', 10),  # New!
    Task('Fill a Crate With Bananas', 's', 'Fill a crate with Bananas for Luthas at Musa Point', 10, 's'),  # !!!FIXME BOTTLENECK
    Task('Catch 100 Lobsters', '', 'Catch 100 Raw Lobsters whilst Fishing', 30),  # Musa Point / IoS by fairy ring, Lvl 40, Cage or regions
    Task('Cook 100 Lobsters', '', 'Cook 100 Raw Lobsters', 30),  # Musa Point / IoS by fairy ring, Lvl 40, Cage or regions
    Task('Catch 50 Swordfish', '', 'Catch 50 Raw Swordfish whilst Fishing', 30),  # Lvl 50, Harpoon, Musa Point
    Notice('Remember your birdhouses and rakes'),

    Header('Brimhaven / Shilo'),
    Task('Receive an Agility Arena Ticket', 's', 'Receive an Agility Arena Ticket from the Brimhaven Agility Arena', 10, 's'),
    Task('Buy a Snapdragon From Pirate Jackie the Fruit', 's', 'Buy a Snapdragon From Pirate Jackie the Fruit in Brimhaven', 30, 's'),
    Task('Take a Shortcut Across the Shilo Village River', 's', 'Use the Stepping Stones Agility Shortcut in Shilo Village ', 30, 's'),
    Task('Catch a Salmon on Karamja', 's', 'Catch a Salmon on Karamja', 30, 's'),  # Lvl 30, Fly Fishing + Feather, Shilo

    Banking('W and grab torch/tinderbox, some cooked low hp food. Buy bananas if you need a cheap source'),

    Header('Beneath Lumbridge'),
    Notice('Rake'),
    Notice('Do RFD another cooks quest if you want '),
    Task('Drink From the Tears of Guthix', 's', 'Drink from the Tears of Guthix  in the Lumbridge Swamp Caves', 30, 's'),
    Notice('Use the Bone dagger spec'),
    Task('Perform a Special Attack', '', 'Perform any special attack', 10),
    Notice('Consult this table - https://oldschool.runescape.wiki/w/Dorgesh-Kaan_market_trading#Types_of_food and I think selling at half price works most of the time'),
    Notice('Try to hop worlds if you are constantly losing'),
    Task('Eat Eel sushi', 's', 'Eat the Dorgeshuun delicacy, Eel sushi', 30, 's'),  # New!
    Task('Pickpocket a Bullseye Lantern From a Cave Goblin', 's', 'Pickpocket a Bullseye Lantern from a Cave Goblin', 30, 's'),
    Notice('Requires 49 Firemaking plus swamp tar for lamp oil. Tar available in Lumby Swamp, and FM levels get put to use for Wintertodt'),
    Task('Light a Bullseye Lantern', '', 'Light a Bullseye Lantern', 30),

    Header('From gem stall - Telegrabs some gold bars from Varrock bank if you need'),
    Notice('Edgeville tele is X'),
    Task('Craft a Ruby Amulet', '', 'Craft a Ruby Amulet', 30),
    Task('Craft an Emerald Ring', '', 'Craft an Emerald Ring', 30),

    Header('Mining Fremmy area preferably, we will want 40 mining anyways'),
    Notice('Remember your birdhouses and rakes'),
    Notice('You can buy Mith up to Rune pickaxe in shop north of Blast Furnace'),
    Task('Mine 15 coal', '', 'Mine 15 coal', 30),
    Task('Mine 50 Iron Ore', '', 'Mine 50 Iron Ore', 30),
    Task('Smelt an Iron Bar', '', 'Use a Furnace to smelt an Iron Bar', 10),
    Task('Obtain a Clue Geode While Mining', '', 'Obtain any kind of clue geode whilst Mining a rock', 30),
    Task('Obtain a Gem While Mining', '', 'Obtain any kind of gem whilst Mining a rock', 30),
    Task('Fletch 150 Iron Arrows', '', 'Fletch 150 Iron Arrows', 30),

    Header('All of below are _kind of_ in order but are more flexible since we can tele everywhere.'),
    Notice('You could be fine to skip the grindier ones, but I wanted to add as much as I could route to have options.'),
    Notice('If I can get away with it, I will try to do a bit of each skill and stop once the fast tasks dry up.'),

    Header('Honk mimimimimimi we have to woodcut in Draynor'),
    Notice('Before starting WC training consider farming the Gout Tubers for Karamja diary and likely gem machete task. You should have max rate at this point'),
    Notice('Clue compass to wizards tower, fight wizards for robes'),
    Task('Equip a Wizard Robe and Hat', '', 'Equip any wizard robe along with any wizard hat', 30),
    Notice('Use this time to figure out what you want to do next'),
    Notice('Remember your birdhouses and rakes'),
    Task('Chop some Rising Roots', '', 'Chop some Rising Roots spawned via Forestry', 30),
    Task('Complete the Flowering Bush event', '', 'Complete the Flowering Bush event spawned via Forestry', 30),
    Task('Complete the Pheasant Forestry Event', '', 'Complete the Pheasant event spawned via Forestry', 30),
    Task('Complete the Ritual Forestry Event', '', 'Complete the Ritual event spawned via Forestry', 30),
    Task('Complete the Struggling Sapling event', '', 'Complete the Struggling Sapling event spawned via Forestry', 30),
    Task('Chop Some Logs With a Steel Axe', '', 'Chop any kind of logs using a Steel Axe', 10),
    Task('Fletch 25 Oak Stocks', '', 'Fletch 25 Oak Stocks', 30),
    Task('Fletch 1000 arrow shafts', '', 'Fletch 1000 arrow shafts', 30),
    Task('Burn 100 Willow Logs', '', 'Burn 100 Willow Logs', 30),
    Task('Chop 100 Willow Logs', '', 'Chop 100 Willow Logs from Willow Trees', 30),
    Task('Fletch a Willow Shortbow (u)', '', 'Fletch a Willow Shortbow (u)', 30),  # New!
    Task('Equip a Willow Shield', '', 'Equip a Willow Shield', 30),
    Task('Cut the Swaying Tree', 'f', 'Cut the Swaying Tree', 10, 'f'),  # New!
    Task('Obtain a Bird Nest', '', 'Obtain a Bird Nest whilst cutting down trees', 10),

    Header('Isle of Souls'),
    Banking('Harpoon, Axe (if woodcutting), Runes for Blue Dragon, food'),
    Notice('Remember your birdhouses and rakes'),
    Task('Open the Dark Chest', 's', 'Open the Dark Chest', 30, 's'),
    Notice('Can get a bird snare on the isle next to the spinning wheel icon'),
    Task('Snare a Bird', '', 'Catch any bird with a Bird Snare', 10),
    Task('Obtain a Casket from Fishing', '', 'Obtain a Casket from Fishing', 10),
    Task('Cut 50 Maple Logs', '', 'Cut 50 Maple Logs', 30),  # New!
    Task('Burn 25 Maple Logs', '', 'Burn 25 Maple Logs', 30),  # New!
    Task('Build a Waka Canoe', '', 'Build a Waka Canoe', 30),
    Task('Bury Some Wyvern or Dragon Bones', '', 'Bury either some Wyvern Bones or some Dragon Bones', 30),

    Header('Do your diaries'),
    Notice('Especially for Karamja, try to wait on collecting rewards til 12x'),
    Task('Complete the Easy Fremennik Diary', 'f', 'Complete all of the easy tasks in the  Fremennik Achievement Diary.', 40, 'f'),
    Task('Deposit an Item Using Peer the Seer', 'f', 'Deposit an item into your Bank using Peer the Seer', 30, 'f'),
    Task('Complete the Easy Lumbridge & Draynor Diary', 's', 'Complete all of the easy tasks in the  Lumbridge & Draynor Achievement Diary', 30, 's'),
    Task('Complete the Easy Varrock Diary', 's', 'Complete all of the easy tasks in the  Varrock Achievement Diary', 30, 's'),
    Task('Complete the Easy Karamja Diary', 's', 'Complete all of the easy tasks in the  Karamja Achievement Diary', 30, 's'),

    Header('Puro Puro'),
    Task('Enter Puro Puro from Gielinor', '', 'Enter Puro Puro from a crop circle in mainland Gielinor', 10),
    Task('Catch a Baby Impling', '', 'Catch a Baby Impling', 10),

    Header('Shopscape smithing'),
    Notice('Coal and Iron is available at Jatizso, pickpocket if you need money. I think Varrock guards are our best gp.'),
    Notice('Use Blast Furnace. Alternatively, Rings of Forging.'),
    Notice('Consider making knives to begin range training'),
    Task('Smelt a Steel Bar', '', 'Use a Furnace to smelt a Steel Bar', 30),
    Task('Smith 10 Steel bolts (unf)', '', 'Use an Anvil to smith 10 Steel bolts (unf)', 30),
    Task('Smith a Steel Platebody', '', 'Use an Anvil to smith a Steel Platebody', 30),

    Header('Start PVM a bit'),
    Task('Complete 1 Slayer Task', '', 'Complete 1 Slayer Task', 30),
    Task('Kill a Rooster', 'f', 'Kill a Rooster in the Fremennik Province', 10, 'f'),  # New!
    Notice('Keep some bones from slayer monsters for Demon Slayer, we will train prayer later'),
    Task('Complete Demon Slayer', 's', 'Complete the  Demon Slayer  quest', 30, 's'),
    Task('Defeat a Greater Demon on Karamja', 's', 'Defeat a Greater Demon on Karamja', 30, 's'),
    Task('Slay 250 Creatures', '', 'Slay 250 creatures whilst on a Slayer Task', 30),
    Task('Defeat a Pyrefiend in the Fremennik Province', 'f', 'Defeat a Pyrefiendin the Fremennik Province.', 10, 'f'),
    Task('Defeat a Cockatrice in the Fremennik Province', 'f', 'Defeat a Cockatricein the Fremennik Province.', 10, 'f'),
    Task('Defeat a Rock Crab in the Fremennik Province', 'f', 'Defeat a Rock Crabin the Fremennik Province.', 10, 'f'),
    Task('Talk to the Voice of Yama', 'z', 'Talk to the Voice of Yama', 30, 'z'),  # New!
    Notice('Requires 500 TL and 40 Cmb to join'),
    Task('Win a Game of Soul Wars', 's', 'Win a game of Soul Wars', 30, 's'),

    Header('Some Kourend stuff, if you take another region you can probably swap out the tasks easily enough'),
    Notice('Good chance Kourend will need a few more tasks to unlock, knock these out once you can'),
    Notice('Remember your birdhouses and rakes'),

    Header('Port Piscarilius Area'),
    Task('Steal 1 Artefact', 'z', 'Steal an artefact for Captain Khaled in Piscarilius.', 10, 'z'),
    Task('Capture 10 sandworms', 'z', 'Capture 10 sandworms', 30, 'z'),  # New!
    Notice('Take boat to Lands End'),

    Header('Lands End Area'),
    Task('Bank at Lands End', 'z', 'Open your Bank using the Bank at Lands End', 10, 'z'),  # New!
    Task('Kill a Barbarian in Kourend', 'z', 'Kill a Barbarian in Kourend', 10, 'z'),  # New!
    Task('Kill a Necromancer', '', 'Kill a Necromancer', 10, 'k | z'),

    Header('Shayzien Area'),
    Task('Drink a LizardKicker', 'z', 'Drink a LizardKicker.', 10, 'z'),
    Task('Travel to Molch Island', 'z', 'Take one of the boats around Lake Molch to Molch Island', 10, 'z'),  # New!
    Task('Eat a Field Ration', 'z', 'Eat a Field Ration', 10, 'z'),  # New!
    Task('Complete the Shayzien Basic Agility Course', 'z', 'Complete a lap of the Shayzien Basic Agility Course', 30, 'z'),  # New!
    Notice('Buy chefs hat in Shayzien'),

    Header('Hosidius Area'),
    Task('Plant Seeds in an Allotment Patch', '', 'Plant some seeds in an Allotment patch', 10, 'a | m | k | z | t | v'),
    Task('Fill a Bucket With Supercompost', '', 'Fill a Bucket with Supercompost from a Compost Bin', 30, 'a | m | k | z | t | v'),
    Task('Dig 25 Saltpetre', 'z', 'Dig 25 Saltpetre', 30, 'z'),  # New!
    Task('Restore 14 Prayer points in Hosidius', 'z', 'Restore exactly 14 Prayer Points when praying at an Altar in Hosidius', 30, 'z'),  # New!

    Header('Arceuus Area'),
    Task('Use the Mine cart transportation System', 'z', 'Use the Mine cart transportation System', 10, 'z'),  # New!
    Task('Turn in 1 Library Book', 'z', 'Find and turn in a book in the Arceuus Library.', 10, 'z'),
    Task('Turn in 10 Library Books', 'z', 'Find and turn in 25 books in the Arceuus Library.', 30, 'z'),
    Task('Cast a Wave Spell', '', 'Cast any wave spell', 80),
    Notice('Buy eye of newt in Arceuus'),
    Task('Make an Attack Potion', '', 'Make an Attack Potion', 10),
    Task('1 Wintertodt Kill', 'z', 'Help the Pyromancers subdue the Wintertodt', 10, 'z'),

    Header('Kebos'),
    Notice('Hope you were raking, make compost if you are not 20 farming'),
    Task('Complete the Garden of Death', 'z', 'Complete the Garden of Death', 30, 'z'),  # New!
    Task('Complete 1 Farming Contract', 'z', 'Complete a Farming Contract for Guildmaster Jane in the Farming Guild', 10, 'z'),
    Task('Bank at Mount Quidamortem', 'z', 'Open your Bank using the Bank at Mount Quidamortem', 10, 'z'),  # New!

    Header('Kourend Castle'),
    Task('Cast Kourend Castle Teleport', 'z', 'Cast the spell Kourend Castle Teleport after unlocking it by reading transportation incantations', 30, 'z'),
    Task('Steal Some Silk', '', 'Steal some silk from a silk stall', 10, 'k | z | t | v'),
    Task('Equip a Protest Banner', 'z', 'Equip a Protest Banner.', 10, 'z'),
    Task('Smith Steel in Kourend Castle', 'z', 'Smith Steel in Kourend Castle', 30, 'z'),  # New!
    Task('Inferior Demonbane Demon Kill', 'z', 'Kill a demon using the Inferior Demonbane spell.', 30, 'z'),
    Notice('If you\'re in catacombs now consider safespotting Fire Giants for Combat Mastery (100% weakness to water spells)'),
    Notice('From entrance, run south then west through the other giants, safespot on the ramp to them'),
    Task('Kill a King Sand Crab', 'z', 'Kill a King Sand Crab', 30, 'z'),  # New!
    Task('Kourend and Kebos Easy Diary Tasks', 'z', 'Complete all tasks in the easy tier of the   Kourend and Kebos achievement diary', 30, 'z'),
    Task('Cast a Blast Spell', '', 'Cast any blast spell', 30),
    Task('Cast High Level Alchemy', '', 'Cast the High Level Alchemy spell', 30),
    Notice('Telegrab gold bar in varrock bank if needed'),
    Task('Use a Digsite Pendant to Teleport to Fossil Island', 's', 'Use a Digsite Pendant to teleport to Fossil Island', 30, 's'),

    Header('Defensive casting post Arceuus Library'),
    Task('Equip some Black armour', '', 'Equip either a Black Platebody, some Black Platelegs or a Black Full Helm', 30),
    Task('Equip some Steel armour', '', 'Equip either a Steel Platebody, some Steel Platelegs or a Steel Full Helm', 30),
    Task('Equip a Full Mithril Set', '', 'Equip a Mithril Platebody, a Mithril Full Helm and either some Mithril Platelegs or a Mithril Plateskirt', 30),

    Header('Use your clues from skilling'),
    Task('1 Easy Clue Scroll', '', 'Open a Reward casket for completing an easy clue scroll', 30),
    Task('Gain a Unique Item From an Easy Clue', '', 'Gain a unique item from an Easy Clue Scroll Reward Casket', 30),
    Task('1 Medium Clue Scroll', '', 'Open a Reward casket for completing a medium clue scroll', 30),
    Task('5 Collection log slots', '', 'Obtain 5 unique Collection Log slots', 30),
    Task('Eat some Purple Sweets', '', 'Eat some Purple Sweets', 30),
    Task('Burn Some Coloured Logs', '', 'Burn some logs that have been coloured with a firelighter', 30),

    Header('Pre-Bankers Note Runecrafting'),
    Notice('Since you need this for Lumby diary anyways, probably should just knock out up to 50 Water Runes. 200 Essence and others, wait for BN'),
    Task('Mine 25 Pure Essence', 's', 'Mine 25 Pure Essence', 30, 's'),  # New!
    Task('Craft 50 Water Runes', 's', 'Craft 50 Water Runes from Essence at the Water Altar', 30, 's'),
    Task('Craft 200 Essence Into Runes', '', 'Use Runecrafting Altars to craft 200 essence into runes of any type', 30),

    Header('Milestones'),
    Task('Reach Total Level 250', '', 'Reach a Total Level of 250', 30),
    Task('Reach Total Level 500', '', 'Reach a Total Level of 500', 30),
    Task('Reach Total Level 750', '', 'Reach a Total Level of 750', 30),
    Task('Reach Base Level 5', '', 'Reach level 5 in every skill', 30),
    Task('Reach Base Level 10', '', 'Reach level 10 in every skill', 30),

    Header("Miscellaneous things you could get but didn\'t know how to group:"),
    Notice('You should have the attack level after finishing Vampyre Slayer'),
    Task('Equip an Adamant Weapon', '', 'Equip any Adamant weapon', 30),  # if done with combat xp multiplier should be there
    Task('Equip a Mithril Weapon', '', 'Equip any Mithril weapon', 30),  # Vampyre slayer gets you there
    Task('Build an Oak Larder', '', 'Build an Oak Larder in a Kitchen in your Player Owned House', 30),
    Task('Enter the Tai Bwo Wannai Hardwood Grove', 's', 'Enter the Hardwood Grove in Tai Bwo Wannai', 30, 's'),
    Task('Create an Antipoison', '', 'Create an Antipoison', 10),
    Task('Dismantle 20 Filled Bird Houses', 's', 'Dismantle 20 filled Bird Houses on Fossil Island', 30, 's'),
    Task('Enter the Cooks Guild', 's', 'Enter the Cooks Guild west of Varrock', 30, 's'),  # Buy chefs hat in Shayzien

    Header('End of branching paths, final bit expects you to be 12x at T5'),

    # At 12x with likely bankers note, if not there do at 8x
    Header('With 12x or maybe just 8x, finish thieving stalls. If we\'re still 8x at this point I\'ve got nothing left sorry'),
    Task('Achieve Your First Level 90', '', 'Reach level 90 in any skill.', 200),
    Task('Achieve Your First Level 95', '', 'Reach level 95 in any skill.', 200),
    Task('Reach Level 99 Thieving', '', 'Reach level 99 in your Thieving skill.', 200),

    Header('Complete Karamja Easy / Kudos for prayer xp'),
    Notice('We may be gated by 40 mining so finish that at Rellekka if we need'),
    Notice('Claim Minas lamps now, use them to boost prayer up to overheads (if you have Frem)'),
    Task('Use the Protect from Melee Prayer', '', 'Use the Protect from Melee Prayer', 30),
    Task('Restore 5 Prayer Points at an Altar', '', 'Restore 5 or more Prayer Points at any altar', 10),
    Task('Superhuman Strength and Improved Reflexes', '', 'Use both the Superhuman Strength prayer and the Improved Reflexes prayer at the same time', 10),
    Task('Defeat Scurrius', 's', 'Defeat Scurrius', 30, 's'),
    Task('Reach Combat Level 25', '', 'Reach Combat Level 25', 10),
    Notice('With 1 solo Scurrius you can add a second combat mastery point. I recommend putting it in the same tier as the first for the all-style accuracy boost at t3.'),
    Notice('Once you have the accuracy boost, train ranged with all the knives you made.'),
    Task('Equip a Dorgeshuun Crossbow', 's', 'Equip a Dorgeshuun Crossbow', 30, 's'),
    Task('Equip a Rat Bone Weapon', 's', 'Obtain and equip any Rat Bone weaponry', 30, 's'),
    Task('Defeat Scurrius 10 times', 's', 'Defeat Scurrius 10 times', 30, 's'),
    Task('Reach Combat Level 50', '', 'Reach Combat Level 50', 30),
    Task('Defeat Scurrius 25 times', 's', 'Defeat Scurrius 25 times', 30, 's'),
    Notice('Try on the chickens in Rellekka because Misthalin ones are probably crowded'),
    Task('Kill three chickens in 6 seconds', '', 'Kill three chickens in 6 seconds', 30),
    Header('Okay, time to PVM!'),

    Header('Clues'),
    Task('Fill 5 Beginner Clue Collection Log Slots', '', 'Fill 5 slots in the Beginner Clue section of the Collection Log', 30),
    Task('Fill 5 Easy Clue Collection Log Slots', '', 'Fill 5 slots in the Easy Clue section of the Collection Log', 30),
    Task('Fill 5 Medium Clue Collection Log Slots', '', 'Fill 5 slots in the Medium Clue section of the Collection Log', 30),
    Task('Fill a Medium S.T.A.S.H. Unit', '', 'Build a Medium S.T.A.S.H. unit and fill it with the relevant items', 30),
    Task('Gain a Unique Item From a Beginner Clue', '', 'Gain a unique item from a Beginner Clue Scroll Reward Casket', 30),
    Task('Gain a Unique Item From a Hard Clue', '', 'Gain a unique item from a Hard Clue Scroll Reward Casket', 30),
    Task('Gain a Unique Item From a Master Clue', '', 'Gain a unique item from a Master Clue Scroll Reward Casket', 30),
    Task('Gain a Unique Item From a Medium Clue', '', 'Gain a unique item from a Medium Clue Scroll Reward Casket', 30),

    # Header('Mory Tasks'),
    # Notice('Tan something for diary'),
    # Notice('Get a slayer task from Mazchna'),
    # Task('Defeat a Werewolf in Morytania', 'm', 'Defeat a Werewolf in Morytania', 10, 'm'),
    # Task('Complete the Canifis Agility Course', 'm', 'Complete a lap of the Canifis Rooftop Agility Course', 30, 'm'),
    # Task('Worship the Ectofuntus', 'm', 'Worship the Ectofuntus', 30, 'm'),  # New!
    # Task('Telegrab a Bloody bracer', 'm', 'Telegrab a Bloody bracer in Slepe', 30, 'm'),
    # Task('Unlock permanent boat travel with Andras', 'm', 'Unlock permanent boat travel with Andras in Morytania', 80, 'm'),
    # Task('Visit Port Phasmatys', 'm', 'Visit Port Phasmatys.', 10, 'm'),
    # Task('Visit Mos LeHarmless', 'm', 'Visit Mos LeHarmless', 10, 'm'),
    # Task('Visit Harmony Island', 'm', 'Visit Harmony Island', 10, 'm'),
    #
    # Header('Swampletics'),
    # Task('Feed a ghast some sweets', 'm', 'Feed a ghast some sweets', 30, 'm'),
    # Task('Craft a Snelm', 'm', 'Craft any Snelm', 10, 'm'),
    # Notice('Cook the thin snail you get'),
    # Task('Complete Haunted Mine', 'm', 'Complete the   Haunted Mine quest', 80, 'm'),
    # Task('Equip a Salve Amulet (e)', 'm', 'Equip a Salve Amulet (e)', 30, 'm'),
    #
    # Header('Pvming'),
    # Task('Assemble a Slayer Helm', 'm', 'Assemble a Slayer Helm', 30, 'm'),
    # Notice('Defeat a banshee for Mory diary'),
]

tasks_only = [task for task in routed_tasks if isinstance(task, Task)]
points_so_far = sum(task.points for task in tasks_only)
print(f'Tasks: {len(tasks_only)}, Points: {points_so_far}')

unassigned_task_names = [t.name for t in starter_tasks]
routed_task_names = [t.name for t in tasks_only]
wont_route_task_names = [t.name for t in wont_route]
difficult_tasks_names = [t.name for t in difficult_tasks]
# print([t for t in unassigned_task_names if t in routed_task_names])

task_map = {}
for name in tasks_only:
    if name in task_map.keys():
        print(f'DUPLICATE TASK: {name}')
    task_map[name] = True

current_points = 0

r1_tasks_needed = 90
r2_tasks_needed = 200
t2_points_needed = 750
t3_points_needed = 1500
t4_points_needed = 2500
t5_points_needed = 5000

t2_points_reached = False
t3_points_reached = False
t4_points_reached = False
t5_points_reached = False

task_count = 0
for task in routed_tasks:
    print(task.display)
    if isinstance(task, Task):
        task_count += 1
        if task_count == r1_tasks_needed:
            print(f"~~{r1_tasks_needed} TASKS COMPLETED, BUT CLAIM KUDOS FROM MINAS BEFORE PICKING REGION~~")
            print('Alternatively don\'t claim the kudos, clean 3 finds + museum quiz will get you to the level you need later')
        if task_count == r2_tasks_needed:
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
        if not t5_points_reached and current_points >= t5_points_needed:
            t5_points_reached = True
            print(f"~~{current_points} PTS ACQUIRED - T5 MET~~")
        current_points += task.points


from task_lists.echoes_starter import starter_tasks
all_echoes_tasks = [t.name for t in starter_tasks]
missing_tasks = [t for t in all_echoes_tasks if (
        t not in unassigned_task_names
        and t not in routed_task_names
        and t not in wont_route_task_names
        and t not in difficult_tasks_names
)]
tasks_to_add = [t for t in starter_tasks if t.name in missing_tasks]
# print(tasks_to_add)
