from classes import Task, Notice, Header, Banking

routed_tasks = [
    Header('Lumbridge - Remember to RAKE!'),
    Task('Complete the Leagues Tutorial', '', 'Complete the Leagues Tutorial and begin your adventure', 10),
    Task('Open the Leagues Menu', '', 'Open the Leagues Menu found within the Journal Panel', 10),
    Task('Achieve Your First Level Up', '', 'Level up any of your skills for the first time', 10),
    Task('Achieve Your First Level 5', '', 'Reach level 5 in any skill (not including Agility, Hitpoints and Runecraft)', 10),
    Task('Achieve Your First Level 10', '', 'Reach level 10 in any skill (not including Agility and Hitpoints)', 10),
    Task('Use the Northern Staircase in Lumbridge', 's', 'Use the Northern Staircase in Lumbridge Castle to go upstairs from the bottom floor', 10, 's'),
    Notice('Claim Anti-Dragon Shield'),
    Notice('Claim free runes and ironman armor'),
    Notice('Bank / Prepare Inv - FIGURE OUT WHAT TO BUY FROM GENERAL STORE, Bucket, Shears, Pot, sell starting weps/shield'),
    Task('Kill a Spider by kicking it', 's', 'Kill a Spider in Lumbridge by kicking it', 10, 's'),  # New!
    Task('Rake a Farming Patch', '', 'Rake any Farming patch', 10),  # Store rake on leprechaun
    Task('Dance in a graveyard', '', 'Dance in a graveyard', 10),
    Banking('@Castle top floor, need shears/harpoon/dramen equipped, axe, pot, 2 buckets, pickaxe for copper maybe'),
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
    Task('Use a Fairy Ring', 's', 'Use any Fairy Ring', 10, 's'),  # Edgeville - DKR
    Notice('Can kill a rat in 2nd room of floor 2'),
    Task('Equip Some Fancy Boots or Fighting Boots', 's', 'Equip either a pair of Fancy Boots or a pair of Fighting Boots', 30, 's'),  # New!
    Task('Cast Home Teleport', '', 'Cast the Home Teleport spell', 10),

    Header('North to Varrock - shear sheep on the way?? RAKE!'),
    Task('Milk a cow', 's', 'Milk a cow in Lumbridge', 10, 's'),
    Task('Find the Needle', '', 'Dig in a hay stack for a needle', 30),  # New, can do with potato tree if you cba
    Notice('NEED to pick up an egg for cook\'s assistant here'),
    Task('Kill a Chicken with your fists', 's', 'Kill a Chicken with your fists', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    Notice('Rake Hops Patch'),
    Notice('If spear goblin is up, do that now by safespotting on fence'),
    Task('Kill a Ram', 's', 'Kill a Ram', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    Notice('Grab Redberries'),

    Header('Varrock - RAKE!'),
    Banking('Can bank if you need to here, tbd. Bank redberries, wool, flour, milk, needle'),
    Notice('BUY RUNES - 200 Air, 200 Mind, 30 earth, 30 water = like 2k'),
    Notice('Go to southeast Biohazard area, buy hat from fancy clothes store'),
    Notice('Talk to Minas upstairs in the museum to get kudos'),
    Task('Get a haircut', 's', 'Go and get a haircut', 10, 's'),  # New!
    Task('Purchase a Player Owned House', '', 'Purchase a Player Owned House', 10),
    Task('Kill a Rat', 's', 'Kill a Rat', 10, 's'),  # New!
    Task('Use a Hat Stand', '', 'Put a hat on a hat stand, or try at least', 10),  # New!
    Task('Pet a Stray Dog in Varrock', 's', 'Pet a Stray Dog in Varrock', 10, 's'),  # TODO is he not always in range
    Task('Defeat a Guard', '', 'Defeat a Guard', 10),  # Use ones by tea stall  # !!!FIXME BOTTLENECK
    Task('Bury Some Bones', '', 'Bury any kind of Bones', 10),
    Task('Upset the homeless', 's', 'Anger the Tramp, in south east Varrock', 10, 's'),  # 2 option
    Notice('Kill him from inside Yarlo\'s house, he won\'t enter'),
    Task('Kill a Mugger', 's', 'Kill a Mugger', 10, 's'),  # New!
    Task('Pick a Cabbage in Varrock', 's', 'Pick a Cabbage in Varrock', 10, 's'),  # New!
    Notice('Can buy iron dagger from sword shop for task (would do later) and slash web if going to sewers'),
    Notice('Buy a Red Cape from Thessalia'),
    Notice('Buy Fire, should have about 5.5k left'),
    Task('Equip an Elemental Staff', '', 'Equip a basic elemental staff', 10),
    Notice('You should try to do moss giant in sewers if it isnt crowded yet'),
    Task('Stroke your cat', 's', 'Get a cat and stroke it!', 10, 's'),  # New, -100 for Gertrude

    Header('Minigame to Soul Wars, Combat Mastery 1, Edgeville'),
    Task('Defeat a Moss Giant', '', 'Defeat a Moss Giant', 10),  # Or just do on isle of souls?
    Task('Mine some Copper Ore', '', 'Mine some Copper Ore', 10), # Tin ore on jatizso just get the copper
    Notice('Don\'t do clay if you\'re worried about demon?'),
    Task('Kill an Imp with an earth spell', 's', 'Kill an Imp with an earth spell', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    Task('Scatter some Ashes', '', 'Scatter some Ashes', 10),  # New!
    Task('Visit Deaths Domain', '', 'Visit Deaths Domain', 10),
    Banking('Can bank if needed - need pickaxe for essence, axe for tree spirits, harpoon for karams'),
    Task('Kill a Goblin holding a spear', 's', 'Kill a Goblin holding a spear', 10, 's'),  # New!  # !!!FIXME BOTTLENECK
    Task('Defeat a Goblin', '', 'Defeat a Goblin', 10),

    Header('Wizards Tower - DIS'),
    Task('Defeat a Lesser Demon', '', 'Defeat a Lesser Demon', 30),  # !!!FIXME BOTTLENECK
    Task('Defeat the Lesser Demon in the Wizards Tower', 's', 'Defeat the Lesser Demon at the top of the Wizards Tower', 10, 's'),  # !!!FIXME BOTTLENECK
    Task('Visit the Rune Essence Mine', '', 'Visit the Rune Essence Mine', 10),
    Task('Mine some essence', '', 'Mine some essence', 10),  # New!

    Header('Enchanted Valley - BKQ, Nature Spirits for a while maybe get lucky'),
    Task('Kill 5 Bunnies', '', 'Kill 5 Bunnies', 30),  # New!  # !!!FIXME BOTTLENECK
    Task('Achieve Your First Level 20', '', 'Reach level 20 in any skill', 10),

    Header('Abyssal Area - ALR, get an air/earth/water? (or any) talisman'),
    Task('Locate a Runecrafting Altar With a Talisman', '', 'Use any talisman to check the location of a Runecrafting Altar', 10),  # !!!FIXME BOTTLENECK

    Header('CKR for Karams, need harpoon'),
    Task('Catch a Karambwanji', 's', 'Catch a Karambwanji on Karamja', 10, 's'),
    Notice('Pick up a seaweed'),

    Header('Leagues Tele to Karamja / Brimhaven - RAKE Hardwood / Fruit tree.'),
    Notice('Complete Seaweed diary step and keep the seaweed'),
    Task('Pick a Pineapple on Karamja', 's', 'Pick a Pineapple on Karamja', 10, 's'),
    Task('Kill a Snake in Karamja', 's', 'Kill a Snake in Karamja', 10, 's'),  # New!
    Task('Enter the Brimhaven Dungeon', 's', 'Enter the Brimhaven Dungeon', 30, 's'),  # -875, around 4.7k
    Task('Enter your Player Owned House', '', 'Enter your Player Owned House', 10),
    Task('Build a Room in Your Player Owned House', '', 'Build a room in your Player Owned House', 30),  # -1000, around 3.7k
    Notice('Rake!'),  # TODO add more rakes
    Notice('Buy 11 bananas, glassblowing pipe, hammer, bucket of sand, seaweed if none already'),
    Task('Buy Something From Trader Crewmembers', '', 'Buy something from the Trader Crewmembers', 10),  # Glassblowing pipe + Hammer for later


    Header('Shilo - get bait/bronze bars/slayer task, calc bronze needed. Fare probably around 60 coins.'),
    Task('Equip a Spiny Helmet', '', 'Equip a Spiny Helmet', 10),  # -800, around 2.9k
    Task('Check Your Slayer Task', '', 'Use an Enchanted Gem to check your Slayer Task', 10),
    Notice('300 bait, 200 feathers. -1300, around 1.6k'),
    Notice('Bronze Bars 12g each, buy 50ish. -600, around 1k. Buy a torch + anything else you forgot'),
    Task('Light a Torch', '', 'Light a Torch', 10),
    Notice('Bank bronze bars and set up inv for - magic gear, wool, cooks assistant items'),
    Notice('Can buy beer in inn too, or the lumby one'),
    Task('Sleep in Paramaya Inn', 's', 'Pay the barkeep to sleep in Paramaya Inn, in Shilo Village ', 30, 's'),  # New!

    Header('Lumbridge 2 - RAKE!'),
    Notice('Rake!'),  # TODO add more rakes
    Task('Pickpocket a Citizen', '', 'Pickpocket a Man or a Woman', 10),
    Task('Open 28 Coin Pouches At Once', '', 'Open 28 Coin Pouches at once', 30),
    Task('Obtain 800 Coins From Coin Pouches At Once', '', 'Open a stack of Coin Pouches and obtain at least 800 Coins', 30),  # Guards+
    Task('Reach Combat Level 10', '', 'Reach Combat Level 10', 10),
    Task('Pray at an Altar in Lumbridge', 's', 'Pray at an Altar in Lumbridge', 10, 's'),  # New!
    Task('Ask for a Quest from Bob', 's', 'Talk to Bob in Lumbridge axe shop and ask for a Quest', 10, 's'),  # New!
    Task('Kill a Duck with a fire spell', 's', 'Kill a Duck with a fire spell', 10, 's'),  # New!
    Task('Talk to Hans', 's', 'Talk to Hans and have him tell you how old you are', 10, 's'),  # New!
    Notice('Turn in cooks assistant'),
    Task('Burn Some Food', '', 'Burn any kind of food while trying to cook it', 10),
    Task('Use the Range in Lumbridge Castle', 's', 'Use the Range in Lumbridge Castle to cook some food', 30, 's'),
    Banking('Wool, Harpoon, Magic Equip, Money, Axe'),
    Task('Spin a Ball of Wool', '', 'Use a Spinning Wheel to spin a Ball of Wool', 10),
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
    Notice('Skip below if it is croweded'),
    Task('Chop a log from a potato tree', 's', 'Chop a log from a tree that is curiously in a potato field', 10, 's'),  # !!!FIXME BOTTLENECK

    Header('Draynor - Start Vampire slayer, buy Chronicle and some wines, get seeds, barley esp. Do req fishing before Musa Point'),
    Notice('Enough agility for Varrock if 8x. Cook some food.'),
    Task('Insult Aggie the Witch', 's', 'Insult Aggie the Witch in Draynor Village', 10, 's'),
    Task('Have Ned make you some rope', 's', 'Have Ned make you some rope using a ball of wool in Draynor Village', 10, 's'),
    Notice('THIEVING TO 40'),
    Notice('Buy chronicle and a couple of charges'),
    Task('Pickpocket a Master Farmer', '', 'Successfully pickpocket from a Master farmer', 30),
    Notice('Do enough to get 30 agility'),
    Task('Complete the Draynor Agility Course', 's', 'Complete a lap of the Draynor Rooftop Agility Course', 10, 's'),
    Task('Complete 10 Laps of the Draynor Agility Course', 's', 'Complete 10 laps of the Draynor Rooftop Agility Course', 30, 's'),
    Task('Obtain a Mark of Grace', '', 'Obtain a Mark of Grace from any Rooftop Agility Course', 30),
    Notice('Buy some seeds for birdhouses/barley'),
    Notice('Cook some food if you don\'t have any'),

    Header('Frem should be unlocked now - Leagues tele there. Bring 3-4 food. - claim seal of passage'),
    Notice('Fill inv with clay, switch to steel pick from HAM once 6 (can\'t equip)'),
    Notice('Grab 2-3 onions from field in SE Rellekka'),
    Task('Eat an Onion', 's', 'Eat an Onion, raw', 10, 's'),  # New!
    Task('Mine some Ore With a Steel Pickaxe', '', 'Mine any ore using a Steel Pickaxe', 10),
    Header('Lunar Isle'),
    Task('Switch to the Lunar Spellbook', 'f', 'Switch to the Lunar Spellbook.', 10, 'f'),
    Notice('Switch back after'),
    Task('Use the Bank on Lunar Isle', 'f', 'Use the Bank on Lunar Isle.', 10, 'f'),
    Notice('Buy a law rune or 5, and some chaos runes from Baba Yaga'),
    Notice('Get kicked back to Rellekka and mine more clay'),
    Task('Use the Bank on Jatizso', 'f', 'Use the Bank on Jatizso.', 10, 'f'),
    Task('Mine 5 Tin Ore', '', 'Mine 5 Tin Ore', 10),
    Header('Neitiznot'),
    Task('Use the Bank on Neitiznot', 'f', 'Use the Bank on Neitiznot.', 10, 'f'),
    Task('Kill a Yak', 'f', 'Kill a Yak.', 10, 'f'),
    Notice('Buy Wool for Sheep Shearer here'),
    Task('Smelt a Bronze Bar', '', 'Use a Furnace to smelt a Bronze Bar', 10),

    Header('Varrock - Figure out Kudos, get Trowel / Specimen Brush / Specimen Jar. Progress Vampyre slayer and have beer for barb village'),
    Task('Teleport Using Law Runes', '', 'Cast any teleport spell that uses Law Runes', 30),
    Task('Smith a Bronze full helm', '', 'Use an Anvil to smith a Bronze full helm', 10),
    Task('Smith a Bronze plateskirt', '', 'Use an Anvil to smith a Bronze plateskirt', 10),
    Notice('Rake!'),  # TODO add more rakes
    Task('Pickpocket a Varrock Guard', 's', 'Pickpocket any Varrock Guard', 30, 's'),  # New!
    Notice('Thieving up to 45 or maybe 50, make sure you have enough gp for daddys home, including 100 nails'),
    Task('Steal From the Varrock Tea Stall', 's', 'Steal from the Tea Stall in Varrock', 10, 's'),
    Notice('IMPORTANT! Need to use Tea on Elsie'),
    Task('Have Elsie tell you a story', 's', 'Have Elsie tell you a story in Varrock', 10, 's'),
    Task('Slash a web in varrock sewers', 's', 'Slash a web in Varrock sewers', 10, 's'),  # Maybe skip?
    Task('Achieve Your First Level 30', '', 'Reach level 30 in any skill', 30),
    Task('Achieve Your First Level 40', '', 'Reach level 40 in any skill', 30),
    Task('Achieve Your First Level 50', '', 'Reach level 50 in any skill', 30),
    Task('Reach Total Level 100', '', 'Reach a Total Level of 100', 30),

    Task('Complete the Varrock Agility Course', 's', 'Complete a lap of the Varrock Rooftop Agility Course', 10, 's'),
    Task('Complete 10 Laps of the Varrock Agility Course', 's', 'Complete 10 laps of the Varrock Rooftop Agility Course', 30, 's'),
    Notice('Below if needed, skip otherwise'),
    Task('Complete 50 Laps of a Rooftop Agility Course', '', 'Complete 50 laps of any Rooftop Agility Course', 30),  # if needed
    Notice('Clean til you find digsite pendant for kudos. Claim rewards once you have all 5.'),
    Notice('Definitely do quiz so you can start birdhouses'),
    Task('Complete the Natural History Quiz', 's', 'Complete the Natural History Quiz in the Varrock Museum', 10, 's'),

    Header('Fossil Island / Daddys Home'),
    Notice('Clue Compass to Digsite Q'),
    Notice('Bring Trowel/Specimen Brush'),
    Notice('Search Sacks for a Jar'),
    Notice('Clue Compass to Exam Centre R'),
    Task('Provide Terry a buckle', 's', 'Show Terry Balando in the Digsite a Belt Buckle', 30, 's'),  # Bring Trowel/Specimen Brush+Jar
    Notice('Grab lvl 3 certificate for RFD'),
    Notice('Panning tray is in panning spot'),
    Task('Pan for an Uncut Jade', 's', 'Pan for an Uncut Jade', 10, 's'),  # Panning tray is in panning spot
    Notice('Complete Daddys Home'),
    Notice('Use Varrock Gypsy compass and Lumberyard compass'),
    Task('Turn any Logs Into a Plank', '', 'Use a Sawmill to turn Logs into a Plank', 10),
    Task('Travel to Fossil Island', 's', 'Take the Museum Barge to Fossil Island', 10, 's'),
    Task('Pet the Museum Camp dog', 's', 'Pet the dog in the Museum Camp on Fossil Island', 10, 's'),
    Task('Build a Bank on Fossil Island', 's', 'Build a Bank at the Museum Camp on Fossil Island', 30, 's'),
    Task('Fully Unlock the Mycelium Transportation System', 's', 'Unlock every destination for the Mycelium Transportation System on Fossil Island', 30, 's'),

    Header('Leagues Tele to Brimhaven with money, saw, hammer, steel bars, oak planks, molten glass (seaweed + bucket of sand)'),
    Notice('Make workshop / clockwork bench and make 5 clockworks'),

    Header('Chronicle to Champion\'s Guild. Bring Barley Seeds, gp, runes/staff'),
    Task('Get your revenge against a Dark Wizard', 's', 'Get your revenge against a Dark Wizard, south of Varrock', 10, 's'),
    Notice('Buy compost, plant barley and protect'),
    Task('Protect Your Crops', '', 'Pay a farmer to protect any of your crops', 10),  # Buy compost, plant barley and prot
    Task('Kill a Cow in one hit', 's', 'Kill a Cow in one hit', 10, 's'),  # New!

    Header('Clue compass to edgeville, or just run idk'),
    Notice('Make Soft Clay at Doris\'s house'),
    Task('Drink a beer in the Longhall', 's', 'Drink a beer in the Longhall in Barbarian Village', 10, 's'),  # New!
    Task('Kill a Barbarian in the Barbarian Village', 's', 'Kill a Barbarian in Barbarian Village', 10, 's'),  # New!
    Notice('Train crafting to 20 with pottery. How do I do pottery again?. Need 3270 with Sheep Shearer xp to hit 20.'),

    Header('Leagues Tele to Rellekka, thieve fremmys if not 50 -> Keldagrim'),
    Notice('Enter Blast Furnace to unlock minigame tele'),
    Task('Steal a Chocolate Slice', '', 'Steal a Chocolate Slice from a Bakery Stall.', 10, 'f | k | z | v'),
    Task('Achieve Your First Level 60', '', 'Reach level 60 in any skill.', 80),
    Task('Achieve Your First Level 70', '', 'Reach level 70 in any skill.', 80),
    Task('Cut a Sapphire', '', 'Cut a Sapphire', 10),
    Task('Achieve Your First Level 80', '', 'Reach level 80 in any skill.', 80),
    Notice('Silver Stall to 75'),
    Notice('Gem Stall to 80?'),

    Header('Draynor 2'),
    Notice('Have Aggie Make Red and Yellow dyes using Redberries/Onions'),
    Task('Dye a cape orange', '', 'Dye a cape orange', 10),
    Task('Fletch Some Arrow Shafts', '', 'Fletch some Arrow Shafts', 10),
    Task('Burn Some Oak Logs', '', 'Burn some Oak Logs', 10),
    Task('Fletch an Oak Shortbow', '', 'Fletch an Oak Shortbow', 10),
    Notice('Head to draynor manor with a hammer, clue compass S'),
    Task('Get a chair to follow you', 's', 'Get a chair to follow you', 10, 's'),
    Task('Complete Vampyre Slayer', 's', 'Complete the  Vampyre Slayer  quest', 30, 's'),  # bring stuff! know safespot. Need a hammer

    Header('Lumbridge 3 - You should buy wool from Frem for Sheep Shearer'),
    Task('Complete Sheep Shearer', 's', 'Complete the  Sheep Shearer  quest', 30, 's'),
    Notice('Need 38 cooking and milk (or at least a bucket)'),
    Task('Churn some butter', 's', 'Use a churn to make some butter', 30, 's'),
    Task('Take a Canoe to Champions Guild', 's', 'Take a Canoe from Lumbridge to the Champions Guild', 10, 's'),  # 12 WC

    Header('Over to Musa Point by tzhaar ring BLP - Fishing here'),
    Notice('Walk into fight caves and leave for diary'),
    Task('Defeat a TzHaar', 's', 'Defeat any TzHaar in Mor Ul Rek', 30, 's'),
    Notice('Pick 5 bananas for diary'),
    Task('Eat a Banana', '', 'Eat a Banana', 10),  # New!
    Task('Fill a Crate With Bananas', 's', 'Fill a crate with Bananas for Luthas at Musa Point', 10, 's'),  # !!!FIXME BOTTLENECK
    Task('Catch 100 Lobsters', '', 'Catch 100 Raw Lobsters whilst Fishing', 30),  # Musa Point / IoS by fairy ring, Lvl 40, Cage or regions
    Task('Cook 100 Lobsters', '', 'Cook 100 Raw Lobsters', 30),  # Musa Point / IoS by fairy ring, Lvl 40, Cage or regions
    Task('Catch 50 Swordfish', '', 'Catch 50 Raw Swordfish whilst Fishing', 30),  # Lvl 50, Harpoon, Musa Point

    Header('Brimhaven / Shilo'),
    Task('Receive an Agility Arena Ticket', 's', 'Receive an Agility Arena Ticket from the Brimhaven Agility Arena', 10, 's'),
    Task('Buy a Snapdragon From Pirate Jackie the Fruit', 's', 'Buy a Snapdragon From Pirate Jackie the Fruit in Brimhaven', 30, 's'),
    Task('Take a Shortcut Across the Shilo Village River', 's', 'Use the Stepping Stones Agility Shortcut in Shilo Village ', 30, 's'),
    Task('Catch a Salmon on Karamja', 's', 'Catch a Salmon on Karamja', 30, 's'),  # Lvl 30, Fly Fishing + Feather, Shilo

    Header('Beneath Lumbridge'),
    Notice('Rake'),
    Notice('Do RFD another cooks quest'),
    Task('Eat Eel sushi', 's', 'Eat the Dorgeshuun delicacy, Eel sushi', 30, 's'),  # New!
    Task('Drink From the Tears of Guthix', 's', 'Drink from the Tears of Guthix  in the Lumbridge Swamp Caves', 30, 's'),
    Task('Pickpocket a Bullseye Lantern From a Cave Goblin', 's', 'Pickpocket a Bullseye Lantern from a Cave Goblin', 30, 's'),

    Header('From gem stall'),
    Task('Craft a Ruby Amulet', '', 'Craft a Ruby Amulet', 30),
    Task('Craft an Emerald Ring', '', 'Craft an Emerald Ring', 30),

    Header('End of story path, figure out which of below are applicable'),

    Header('In Fremmy land'),
    Task('Mine 15 coal', '', 'Mine 15 coal', 30),
    Task('Mine 50 Iron Ore', '', 'Mine 50 Iron Ore', 30),
    Task('Smelt an Iron Bar', '', 'Use a Furnace to smelt an Iron Bar', 10),
    Task('Obtain a Clue Geode While Mining', '', 'Obtain any kind of clue geode whilst Mining a rock', 30),
    Task('Obtain a Gem While Mining', '', 'Obtain any kind of gem whilst Mining a rock', 30),
    Task('Fletch 150 Iron Arrows', '', 'Fletch 150 Iron Arrows', 30),

    Header('Honk mimimimimimi we live in Draynor'),
    Notice('Clue compass to wizards tower, fight wizards for robes'),
    Task('Equip a Wizard Robe and Hat', '', 'Equip any wizard robe along with any wizard hat', 30),
    Task('Chop some Rising Roots', '', 'Chop some Rising Roots spawned via Forestry', 30),
    Task('Chop Some Logs With a Steel Axe', '', 'Chop any kind of logs using a Steel Axe', 10),
    Task('Fletch 25 Oak Stocks', '', 'Fletch 25 Oak Stocks', 30),
    Task('Fletch 1000 arrow shafts', '', 'Fletch 1000 arrow shafts', 30),
    Task('Burn 100 Willow Logs', '', 'Burn 100 Willow Logs', 30),
    Task('Chop 100 Willow Logs', '', 'Chop 100 Willow Logs from Willow Trees', 30),
    Task('Fletch a Willow Shortbow (u)', '', 'Fletch a Willow Shortbow (u)', 30),  # New!
    Task('Equip a Willow Shield', '', 'Equip a Willow Shield', 30),
    Task('Mine 25 Pure Essence', 's', 'Mine 25 Pure Essence', 30, 's'),  # New!
    Task('Obtain a Bird Nest', '', 'Obtain a Bird Nest whilst cutting down trees', 10),

    Header('Isle of souls?'),
    Task('Cut 50 Maple Logs', '', 'Cut 50 Maple Logs', 30),  # New!
    Task('Burn 25 Maple Logs', '', 'Burn 25 Maple Logs', 30),  # New!
    Task('Build a Waka Canoe', '', 'Build a Waka Canoe', 30),
    Task('Bury Some Wyvern or Dragon Bones', '', 'Bury either some Wyvern Bones or some Dragon Bones', 30),

    Header('Start PVM?'),
    Task('Complete 1 Slayer Task', '', 'Complete 1 Slayer Task', 30),
    Task('Complete Demon Slayer', 's', 'Complete the  Demon Slayer  quest', 30, 's'),
    Task('Defeat a Greater Demon on Karamja', 's', 'Defeat a Greater Demon on Karamja', 30, 's'),

    Header('Some Kourend stuff'),
    Notice('Rake'),
    Task('Kill a Necromancer', '', 'Kill a Necromancer', 10, 'k | z'),
    Task('Steal Some Silk', '', 'Steal some silk from a silk stall', 10, 'k | z | t | v'),
    Task('Plant Seeds in an Allotment Patch', '', 'Plant some seeds in an Allotment patch', 10, 'a | m | k | z | t | v'),
    Task('Drink a LizardKicker', 'z', 'Drink a LizardKicker.', 10, 'z'),
    Notice('Buy chefs hat in Shayzien'),
    Task('Equip a Protest Banner', 'z', 'Equip a Protest Banner.', 10, 'z'),
    Task('Steal 1 Artefact', 'z', 'Steal an artefact for Captain Khaled in Piscarilius.', 10, 'z'),
    Task('Turn in 1 Library Book', 'z', 'Find and turn in a book in the Arceuus Library.', 10, 'z'),
    Task('Turn in 25 Library Books', 'z', 'Find and turn in 25 books in the Arceuus Library.', 30, 'z'),
    Task('Turn in 50 Library Books', 'z', 'Find and turn in 50 books in the Arceuus Library.', 30, 'z'),
    Task('Headbang with KetSal Kuk', 'z', 'Headbang with KetSal Kuk.', 30, 'z'),
    Task('Complete Getting Ahead', 'z', 'Complete  Getting Ahead  quest.', 30, 'z'),  # 26 Construction but you should have it from setting up BH runs
    Task('Inferior Demonbane Demon Kill', 'z', 'Kill a demon using the Inferior Demonbane spell.', 30, 'z'),
    Task('Enter the Cooks Guild', 's', 'Enter the Cooks Guild west of Varrock', 30, 's'),  # Buy chefs hat in Shayzien
    Task('Cast a Blast Spell', '', 'Cast any blast spell', 30),
    Task('Cast High Level Alchemy', '', 'Cast the High Level Alchemy spell', 30),
    Notice('Telegrab gold bar in varrock bank if needed'),
    Task('Use a Digsite Pendant to Teleport to Fossil Island', 's', 'Use a Digsite Pendant to teleport to Fossil Island', 30, 's'),

    Header("At this point I probably have done/could do these:"),
    Task('1 Easy Clue Scroll', '', 'Open a Reward casket for completing an easy clue scroll', 30),
    Task('Gain a Unique Item From an Easy Clue', '', 'Gain a unique item from an Easy Clue Scroll Reward Casket', 30),
    Task('Equip a Mithril Weapon', '', 'Equip any Mithril weapon', 30),  # Vampyre slayer gets you there
    Task('Equip an Adamant Weapon', '', 'Equip any Adamant weapon', 30),  # if done with combat xp multiplier should be there
    Task('Build an Oak Larder', '', 'Build an Oak Larder in a Kitchen in your Player Owned House', 30),
    Task('Reach Total Level 250', '', 'Reach a Total Level of 250', 30),

    Header('Can shopscape smithing'),
    Task('Smelt a Steel Bar', '', 'Use a Furnace to smelt a Steel Bar', 30),
    Task('Smith 10 Steel bolts (unf)', '', 'Use an Anvil to smith 10 Steel bolts (unf)', 30),
    Task('Smith a Steel Platebody', '', 'Use an Anvil to smith a Steel Platebody', 30),

    Header('Maybe defensive cast post books'),
    Task('Equip some Black armour', '', 'Equip either a Black Platebody, some Black Platelegs or a Black Full Helm', 30),
    Task('Equip some Steel armour', '', 'Equip either a Steel Platebody, some Steel Platelegs or a Steel Full Helm', 30),

    # At 12x with likely bankers note, if not there do at 8x
    Header('Assuming you have Bankers Note now, finish thieving stalls'),
    Task('Achieve Your First Level 90', '', 'Reach level 90 in any skill.', 200),
    Task('Achieve Your First Level 95', '', 'Reach level 95 in any skill.', 200),
    Task('Reach Level 99 Thieving', '', 'Reach level 99 in your Thieving skill.', 200),

    Header('Complete Karamja Easy / Kudos for prayer xp'),
    Notice('We may be gated by 40 mining so finish that at Rellekka if we need'),
    Notice('Claim Minas lamps now'),
    Task('Use the Protect from Melee Prayer', '', 'Use the Protect from Melee Prayer', 30),
    Task('Restore 5 Prayer Points at an Altar', '', 'Restore 5 or more Prayer Points at any altar', 10),
    Task('Superhuman Strength and Improved Reflexes', '', 'Use both the Superhuman Strength prayer and the Improved Reflexes prayer at the same time', 10),

    Header('Okay, time to PVM!'),
]

tasks_only = [task for task in routed_tasks if isinstance(task, Task)]
points_so_far = sum(task.points for task in tasks_only)
print(f'Tasks: {len(tasks_only)}, Points: {points_so_far}')

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
    Task('Catch a Grey Chinchompa', '', 'Catch a Grey Chinchompa', 30),  # New!
    Task('Check a grown Fruit Tree', '', 'Check the health of any Fruit Tree youve grown', 30),
    Task('Chop Some Logs With a Rune Axe', '', 'Chop any kind of logs using a Rune Axe', 30),
    Task('Equip a Maple Shortbow', '', 'Equip a Maple Shortbow', 30),
    Task('Trade a herb with Jekyll', '', 'Trade a herb with Jekyll for a potion', 30),  # New!
    Task('Make an Attack Potion', '', 'Make an Attack Potion', 10),
    Task('Drink a Strength Potion', '', 'Drink a Strength Potion', 10),
    Task('Equip a Rune Weapon', '', 'Equip any Rune weapon', 30),
    Task('Defeat a Steel Dragon on Karamja', 's', 'Defeat a Steel Dragon on Karamja', 30, 's'),
    Task('Enter the Tai Bwo Wannai Hardwood Grove', 's', 'Enter the Hardwood Grove in Tai Bwo Wannai', 30, 's'),
    Task('Equip a Toktz-Ket-Xil', 's', 'Equip a Toktz-Ket-Xil', 30, 's'),
    Task('Equip a Toktz-Xil-Ak', 's', 'Equip a Toktz-Xil-Ak', 30, 's'),
    Task('Equip a Toktz-Xil-Ek', 's', 'Equip a Toktz-Xil-Ek', 30, 's'),
    Task('Equip an Obsidian Cape', 's', 'Equip an Obsidian Cape', 30, 's'),
    Task('Mine some Ore With a Rune Pickaxe', '', 'Mine any ore using a Rune Pickaxe', 30),
    Task('Catch 50 Karambwan', 's', 'Catch 50 Karambwan on Karamja', 30, 's'),
]

starter_tasks = [
    Task('Obtain a Casket from Fishing', '', 'Obtain a Casket from Fishing', 10),
    Task('Perform a Special Attack', '', 'Perform any special attack', 10),
    Task('Reach Combat Level 25', '', 'Reach Combat Level 25', 10),
    Task('Successfully Cut a Red Topaz', '', 'Successfully Cut a Red Topaz', 10),
    Task('Craft Any Combination Rune', '', 'Use a Runecrafting Altar to craft any type of combination rune', 30),
    Task('Kill three chickens in 6 seconds', '', 'Kill three chickens in 6 seconds', 30),
    Task('Land a hoop on a stick', '', 'Successfully land a hoop on a stick in the PoH minigame', 30),  # New!
    Task('Make a Pineapple Pizza', '', 'Make a Pineapple Pizza', 30),
    Task('Reach a Prayer Bonus of 15', '', 'Equip enough item to reach a Prayer bonus of 15 or more', 30),
    Task('Reach Combat Level 50', '', 'Reach Combat Level 50', 30),
    Task('Reach Combat Level 75', '', 'Reach Combat Level 75', 30),
    Task('Reach Total Level 500', '', 'Reach a Total Level of 500', 30),
    Task('Reach Total Level 750', '', 'Reach a Total Level of 750', 30),
    Task('Scrape some blue dragonhide', '', 'Scrape some blue dragonhide', 30),
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
]

difficult_tasks = [
    Task('Locate a Runecrafting Altar With a Talisman', '', 'Use any talisman to check the location of a Runecrafting Altar', 10),
    Task('Chop a log from a potato tree', 's', 'Chop a log from a tree that is curiously in a potato field', 10, 's'),
    Task('25 Easy Clue Scrolls', '', 'Open 25 Reward caskets for completing easy clue scrolls', 30),
    Task('25 Elite Clue Scrolls', '', 'Open 25 Reward caskets for completing elite clue scrolls', 30),
    Task('25 Hard Clue Scrolls', '', 'Open 25 Reward caskets for completing hard clue scrolls', 30),
    Task('25 Medium Clue Scrolls', '', 'Open 25 Reward caskets for completing medium clue scrolls', 30),
    Task('25 Superior Slayer Encounters', '', 'Defeat 25 superior foes while on a Slayer Task', 30),
    Task('30 Collection log slots', '', 'Obtain 30 unique Collection Log slots', 30),
    Task('50 Collection log slots', '', 'Obtain 50 unique Collection Log slots', 30),
    Task('75 Easy Clue Scrolls', '', 'Open 75 Reward caskets for completing easy clue scrolls', 30),
    Task('75 Medium Clue Scrolls', '', 'Open 75 Reward caskets for completing medium clue scrolls', 30),
    Task('75 Superior Slayer Encounters', '', 'Defeat 75 superior foes while on a Slayer Task', 30),
    Task('Build a Mahogany Portal', '', 'Build a Mahogany Portal in a Portal Chamber in your Player Owned House', 30),
    Task('Burn Some Coloured Logs', '', 'Burn some logs that have been coloured with a firelighter', 30),
    Task('Catch a Swamp Lizard or Salamander', '', 'Catch either a Swamp Lizard or any kind of Salamander', 30, 'm | d | k | w | v'),
    Task('Complete 10 Mahogany homes contracts', '', 'Complete 10 Mahogany homes contracts', 30),
    Task('Complete 25 Mahogany homes contracts', '', 'Complete 25 Mahogany homes contracts', 30),
    Task('Complete 50 Laps of a Rooftop Agility Course', '', 'Complete 50 laps of any Rooftop Agility Course', 30),
    Task('Complete a Mahogany homes adept contract', '', 'Complete a  Mahogany Homes adept contract', 30, ''),
    Task('Complete a Mahogany homes beginner contract', '', 'Complete a  Mahogany Homes beginner contract', 30, ''),
    Task('Complete a Mahogany homes novice contract', '', 'Complete a  Mahogany Homes novice contract', 30, ''),
    Task('Complete the Easy Western Provinces Diary', '', 'Complete all of the easy tasks in the  Western Provinces Achievement Diary', 30, 'k'),
    Task('Complete the Evil Bob random event', '', 'Complete the Evil Bob random event', 30),
    Task('Complete the Flowering Bush event', '', 'Complete the Flowering Bush event spawned via Forestry', 30),
    Task('Complete the Maze random event', '', 'Complete the Maze random event', 30),
    Task('Complete the Medium Western Provinces Diary', '', 'Complete all of the medium tasks in the  Western Provinces Achievement Diary', 30, 'k'),
    Task('Complete the Pheasant Forestry Event', '', 'Complete the Pheasant event spawned via Forestry', 30),
    Task('Complete the Pillory random event', '', 'Complete the Pillory random event', 30),
    Task('Complete the Pinball random event', '', 'Complete the Pinball random event', 30),
    Task('Complete the Postie Pete random event', '', 'Complete the Postie Pete random event', 30),
    Task('Complete the Prison Pete random event', '', 'Complete the Prison Pete random event', 30),
    Task('Complete the Ritual Forestry Event', '', 'Complete the Ritual event spawned via Forestry', 30),
    Task('Complete the Struggling Sapling event', '', 'Complete the Struggling Sapling event spawned via Forestry', 30),
    Task('Complete the Surprise Exam random event', '', 'Complete the Surprise Exam random event', 30),
    Task('Craft 200 Essence Into Runes', '', 'Use Runecrafting Altars to craft 200 essence into runes of any type', 30),
    Task('Craft 4 Runes With 1 Essence', '', 'Use a Runecrafting Altar to craft 4 of any type of rune using a single essence', 30),
    Task('Create a green dhide shield', '', 'Create a green dhide shield', 30),
    Task('Create a Guthix Rest Tea', '', 'Create a Guthix Rest Tea', 30, 'f | d | k'),
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
    Task('Equip a Piece of a Mystic Set', '', 'Equip any piece of any Mystic robe set', 30),
    Task('Equip a piece of Beekeepers Outfit', '', 'Equip a piece of Beekeepers Outfit', 30),
    Task('Equip a piece of Camouflage outfit', '', 'Equip a piece of Camouflage outfit', 30),
    Task('Equip a piece of Mime Outfit', '', 'Equip a piece of Mime Outfit', 30),
    Task('Equip a piece of Zombie Outfit', '', 'Equip a piece of Zombie Outfit', 30),
    Task('Equip a Trimmed Amulet', '', 'Equip a Trimmed Amulet', 30),
    Task('Equip full Graahk, Larupia or Kyatt', '', 'Equip a full set of Graahk, Larupia or Kyatt attire', 30),
    Task('Fill 15 Hard Clue Collection Log Slots', '', 'Fill 15 slots in the Hard Clue section of the Collection Log', 30),
    Task('Fill 20 Easy Clue Collection Log Slots', '', 'Fill 20 slots in the Easy Clue section of the Collection Log', 30),
    Task('Fill 20 Medium Clue Collection Log Slots', '', 'Fill 20 slots in the Medium Clue section of the Collection Log', 30),
    Task('Fill 3 Elite Clue Collection Log Slots', '', 'Fill 3 slots in the Elite Clue section of the Collection Log', 30),
    Task('Fill 3 Hard Clue Collection Log Slots', '', 'Fill 3 slots in the Hard Clue section of the Collection Log', 30),
    Task('Fill a Bucket With Supercompost', '', 'Fill a Bucket with Supercompost from a Compost Bin', 30, 'a | m | k | z | t | v'),
    Task('Fill a Large Pouch', '', 'Fill a Large Pouch with Essence', 30),
    Task('Fletch some Broad Arrows or Bolts', '', 'Fletch either some Broad Arrows or some Broad Bolts', 30),
    Task('Gain 10 Unique Items From Beginner Clues', '', 'Gain 10 unique items from Beginner Clue Scroll Reward Caskets', 30),
    Task('Gain 10 Unique Items From Easy Clues', '', 'Gain 10 unique items from Easy Clue Scroll Reward Caskets', 30),
    Task('Gain 10 Unique Items From Medium Clues', '', 'Gain 10 unique items from Medium Clue Scroll Reward Caskets', 30),
    Task('Gain 20 Unique Items From Hard Clues', '', 'Gain 20 unique items from Hard Clue Scroll Reward Caskets', 30),
    Task('Gain 35 Unique Items From Easy Clues', '', 'Gain 35 unique items from Easy Clue Scroll Reward Caskets', 30),
    Task('Gain 5 Unique Items From Hard Clues', '', 'Gain 5 unique items from Hard Clue Scroll Reward Caskets', 30),
    Task('Harvest an Irit Leaf', '', 'Harvest an Irit Leaf from any Herb patch', 30, 'a | m | k | f | z | v'),
    Task('Light a Bullseye Lantern', '', 'Light a Bullseye Lantern', 30),
    Task('Make 30 Prayer Potions', '', 'Make 30 Prayer Potions', 30),
    Task('Mine 50 Mithril Ore', '', 'Mine 50 Mithril Ore', 30),
    Task('Open the Mystery Box', '', 'A boat is a boat, but the mystery box could be anything, even a boat!', 30),
    Task('Slay 250 Creatures', '', 'Slay 250 creatures whilst on a Slayer Task', 30),
    Task('Smith 150 Iron Arrowtips', '', 'Use an Anvil to smith 150 Iron Arrowtips', 30),
    Task('Smith 250 Mithril bolts (unf)', '', 'Use an Anvil to smith 250 Mithril bolts (unf)', 30),
    Task('Craft 50 Nature Runes', 's', 'Craft 50 Nature Runes from Essence at the Nature Altar', 30, 's'),
    Task('Defeat 50 Tormented Demons', 's', 'Defeat 50 Tormented Demons', 30, 's'),
    Task('Defeat a Fossil Island Wyvern', 's', 'Defeat any type of Wyvern on Fossil Island', 30, 's'),
    Task('Defeat a Tormented Demon', 's', 'Defeat a Tormented Demon', 30, 's'),
    Task('Defeat Scurrius 10 times', 's', 'Defeat Scurrius 10 times', 30, 's'),
    Task('Defeat Scurrius 25 times', 's', 'Defeat Scurrius 25 times', 30, 's'),
    Task('Dismantle 20 Filled Bird Houses', 's', 'Dismantle 20 filled Bird Houses on Fossil Island', 30, 's'),
    Task('Equip the Forestry Basket', 's', 'Obtain and Equip the Forestry Basket', 30, 's'),
    Task('Get a Gem from a Gorak', 's', 'Obtain a gem drop from a Gorak', 30, 's'),
    Task('Win a Game of Soul Wars', 's', 'Win a game of Soul Wars', 30, 's')
]


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

r1_tasks_needed = 60
r2_tasks_needed = 140
t2_points_needed = 500
t3_points_needed = 1200
t4_points_needed = 2000
t5_points_needed = 4000

t2_points_reached = False
t3_points_reached = False
t4_points_reached = False
t5_points_reached = False

for idx, task in enumerate(routed_tasks):
    if isinstance(task, Task):
        if idx == r1_tasks_needed:
            print(f"~~{r1_tasks_needed} TASKS COMPLETED, BUT CLAIM KUDOS FROM MINAS BEFORE PICKING REGION~~")
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
        if not t5_points_reached and current_points >= t5_points_needed:
            t5_points_reached = True
            print(f"~~{current_points} PTS ACQUIRED - T5 MET~~")
        current_points += task.points

    print(task.display)

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
