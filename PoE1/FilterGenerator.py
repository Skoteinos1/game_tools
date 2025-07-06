
show_rgb_tf = True
# show_rgb_tf = False

show_rgb = ""
if show_rgb_tf:
	show_rgb = """Show
	SocketGroup "RGB"
	Width 1
	SetFontSize 40

Show
	SocketGroup "RGB"
	Height = 2
	Width 2
	SetFontSize 40"""

header = """# https://www.pathofexile.com/item-filter/about
#============================================================================================================
#	   All Classes
#============================================================================================================
# Class == "Amulets" "Belts" "Body Armour" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Dagger" "Rune Daggers" "Sceptre" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wand" "Wands" "Warstaves"
# "Abyss Jewels" "Jewel" "Jewels"
# "Blueprints" "Contracts"
# "Breachstones"
# "Corpses"
# "Delve Stackable Socketable Currency" "Divination Cards"
# "Fishing Rods"
# "Heist Brooches" "Heist Cloaks" "Heist Gear" "Heist Targets" "Heist Tools"
# "Flask" "Hybrid Flasks" "Life Flasks" "Mana Flasks" "Tinctures" "Utility Flasks"
# "Map Fragments" "Maps" "Memories" "Misc Map Items"
# "Idols"
# "Incubators"
# "Trinkets"
# "Incursion Items"
# "Labyrinth Items" "Labyrinth Trinkets"
# "Skill Gems" "Support Gems"
# "Stackable Currency"
# "Pantheon Souls" "Pieces" "Relics" "Sanctum Research" "Vault Keys"
# "Quest Items"

# ----------- Colors -------------
# Red Green Blue Brown White Yellow Cyan Grey Orange Pink Purple

# ----------- Icons --------------
# Shapes: Circle Cross Diamond Hexagon Kite Moon Pentagon Raindrop Square Star Triangle UpsideDownHouse


#============================================================================================================
#	   Commands
#============================================================================================================

# Drop Sound -----
# PlayAlertSound
# PlayAlertSoundPositional
# CustomAlertSound
# CustomAlertSoundOptional
# DisableDropSound
# EnableDropSound
# DisableDropSoundIfAlertSound
# EnableDropSoundIfAlertSound

# OTHER ----------

# SetTextColor R G B A  0-255
# SetFontSize 1-45
# SetBackgroundColor R G B A  0-255
# SetBorderColor  R G B A  0-255
# PlayEffect Color Temp  # C:(Red, Green, Blue...)  T(Temp) #   PlayEffect Red Temp
# MinimapIcon 2 Cyan Diamond
#   0-2; Color;  Shapes (Circle, Cross...)


#  'Class', 'Show', 'Hide', 'SetBorderColor', 'BaseType', 'Quality', 'StackSize'
# AnyEnchantment True"
# ArchnemesisMod "Toxic"
# BaseDefencePercentile >= 99"
# BaseEnergyShield
# BaseArmour
# BaseEvasion
# BaseWard
# BlightedMap True"
# UberBlightedMap True"
# Continue"
# Corrupted False True
# CorruptedMods 0  >= 2
# DisableDropSound True
# DropLevel < 40  >= 64
# FracturedItem True"
# GemLevel 1 >= 6
# HasCruciblePassiveTree True
# HasEnchantment "Enchantment Bane Damage 2"
# HasEaterOfWorldsImplicit >= 1	(1:Lesser, 2:Greater, 3:Grand, 4:Exceptional, 5:Exquisite, 6:Perfect)
# HasInfluence Crusader Elder Hunter Redeemer Shaper Warlord
# HasSearingExarchImplicit >= 1	(1:Lesser, 2:Greater, 3:Grand, 4:Exceptional, 5:Exquisite, 6:Perfect)
# Identified False True
# ItemLevel <= 15
# LinkedSockets >= 5
# MapTier 1 >= 9
# Mirrored False True
# PlayAlertSound 1-6 100"
# Rarity Normal Magic Rare Unique
# Replica True
# SynthesisedItem True

# SocketGroup A RGB W  D
# Sockets < 1  >= 3  >= 3WWW  >= 4WWWW  >= 6 >= 6WWWWWW >= AA >= AAA >= AAAA"
# TransfiguredGem True"
# Height 1  <= 4
# Width 1  >= 2
# HasImplicitMod True
# HasExplicitMod >=1 "8 a" "Abating" "Abbot's" "Acuminate" "Adaptable" "Adept's" "Adroit" "Alpine" "Apparition's" "Apprentice's" "Archmage's" "Arctic" "Athlete's" "Battlemage's" "Beatified" "Beclouded" "Behemoth's" "Betrayer's" "Bishop's" "Biting" "Bitter" "Blasting" "Blazing" "Blistering" "Blue" "Bolting" "Brinerot" "Burning" "Burnished" "Buzzing" "Carapaced" "Carbonising" "Catarina's Veiled" "Chaotic" "Charged" "Cheetah's" "Cherub's" "Chilled" "Chilling" "Citaqualotl" "Citaqualotl's" "Condensing" "Consecrated" "Corrosive" "Countess's" "Crackling" "Cremating" "Crocodile's" "Cruel" "Cryomancer's" "Crystalising" "Crystalline" "Dazzling" "Deceiver's" "Decrepifying" "Devastating" "Dictator's" "Discharging" "Dissolving" "Djinn's" "Duchess's" "Durable" "Eidolon's" "Electrocuting" "Elevated" "Elreon's Veiled" "Elusory" "Emperor's" "Empress's" "Encased" "Enduring" "Enlightened" "Entombing" "Enveloped" "Esh's" "Essences" "Exalter's" "Exarch's" "Excruciating" "Expediting" "Fawn's" "Fearless" "Fecund" "Festering" "Flame Shaper's" "Flaming" "Flaring" "Fleet" "Foul-tongued" "Frigid" "Frost Singer's" "Frosted" "Fugitive" "Girded" "Glaciated" "Glimmering" "Glinting" "Glittering" "Glowing" "Glyphic" "Godly" "Gravicius' Veiled" "Guatelitzi" "Guatelitzi's" "Guff's Veiled" "Haku's" "Hale" "Hallowed" "Harrowing" "Haunted" "Healthy" "Heated" "Heavy" "Hellion's" "Hero's" "Hissing" "Honed" "Humming" "Ibex's" "Icy" "Illusion's" "Illusory" "Impaling" "Impenetrable" "Impervious" "Impregnable" "Incandescent" "Incanter's" "Incinerating" "Incisive" "Incorporeal" "Indomitable" "Infernal" "Inspired" "Interpermeated" "Interpolated" "Ionising" "It That Fled's Veiled" "Korell's Veiled" "Lacerating" "Lancing" "Lava Conjurer's" "Leadership" "Legend's" "Leo's Veiled" "Lich's" "Lissome" "Lithomancer's" "Mad Lord's" "Mage's" "Magister's" "Magmatic" "Magnifying" "Marchioness's" "Martinet's" "Master's" "Matatl" "Matatl's" "Mazarine" "Merciless" "Mirage's" "Mortifying" "Motivating" "Mutewind" "Nautilus's" "Nightmare's" "Overpowering" "Overseer's" "Paragon's" "Perandus'" "Phantasm's" "Piercing" "Polar" "Polished" "Priest's" "Prime" "Prior's" "Protective" "Provocateur's" "Puhuarte" "Pulsing" "Puncturing" "Pyroclastic" "Queen's" "Quintessential" "Ram's" "Rapturous" "Redblade" "Resilient" "Resolute" "Resonating" "Resplendent" "Riker" "Rimedweller's" "Rin's Veiled" "Robust" "Rotund" "Runic" "Runner's" "Rupturing" "Saintly" "Sanguine" "Sapphire" "Scholar's" "Scintillating" "Searing" "Seething" "Seraphim's" "Serrated" "Sharpened" "Sharpshooter's" "Shimmering" "Shining" "Shocking" "Sizzling" "Smiting" "Smoking" "Smouldering" "Snapping" "Sorcerer's" "Spirit's" "Splintermind's" "Sprinter's" "Stallion's" "Stalwart" "Stormbrewer's" "Stout" "Strong-Willed" "Sturdy" "Subterranean" "Surging" "Tacati" "Tacati's" "Taskmaster's" "Tecton's" "Tempered" "Tempest Master's" "Thaumaturgist's" "Thunderhand's" "Thwarting" "Topotante" "Topotante's" "Tora's Veiled" "Trapping" "Tul's" "Turncoat's" "Tyrannical" "Ultramarine" "Unassailable" "Unfaltering" "Unleashed" "Unmoving" "Unreal" "Unwavering" "Unyielding" "Urchin's" "Vagan's Veiled" "Vaporous" "Vapourising" "Veil" "Veiled" "Versatile" "Vicious" "Victor's" "Vigorous" "Vile" "Virile" "Vivid" "Vorici's Veiled" "Vulcanist's" "Warding" "Wicked" "Winter Beckoner's" "Wizard's" "Xopec" "Xoph's" "Zaffre" "e" "i" "o" "of Abjuration" "of Abuse" "of Acclimatisation" "of Acrimony" "of Adaptation" "of Adaption" "of Agitation" "of Aisling's Veil" "of Archery" "of Arcing" "of Ashes" "of Athletics" "of Atrophy" "of Atrophying" "of Authority" "of Bameth" "of Berserking" "of Blasting" "of Blinding" "of Calamity" "of Cameria's Veil" "of Celebration" "of Chilling" "of Coercion" "of Collision" "of Combusting" "of Command" "of Conflagrating" "of Convalescence" "of Crafting" "of Craiceann" "of Cunning" "of Delaying" "of Demolishing" "of Destruction" "of Deteriorating" "of Discharge" "of Disintegrating" "of Dissolution" "of Distraction" "of Ease" "of Efficiency" "of Enchanting" "of Entropy" "of Ephij" "of Euphoria" "of Everlasting" "of Eviction" "of Exile" "of Expertise" "of Expulsion" "of Exsanguinating" "of Fame" "of Farrul" "of Fenumus" "of Ferocity" "of Finesse" "of Fireproofing" "of Flames" "of Fleshbinding" "of Floe" "of Fortitude" "of Fury" "of Gelidity" "of Glaciation" "of Grandmastery" "of Grounding" "of Haast" "of Harmony" "of Harvest Beasts" "of Haunting" "of Heartstopping" "of Heating" "of Hemorrhaging" "of Hillock's Veil" "of Hindering" "of Immolation" "of Incision" "of Incitation" "of Infamy" "of Insulation" "of Janus' Veil" "of Jorgin's Veil" "of Legerdemain" "of Lioneye" "of Liquefaction" "of Many" "of Mastery" "of Melting" "of Menace" "of Metamorphosis" "of Mysticism" "of Needling" "of Nimbleness" "of Nirvana" "of Nullification" "of Obstruction" "of Opportunity" "of Orchestration" "of Order" "of Penetrating" "of Phasing" "of Phlebotomising" "of Poise" "of Potency" "of Prestidigitation" "of Puhuarte" "of Puncturing" "of Rage" "of Recuperation" "of Relishing" "of Rending" "of Resilience" "of Resistance" "of Reveling" "of Revitalization" "of Revoking" "of Rime" "of Ruin" "of Saqawal" "of Shelter" "of Shocking" "of Skill" "of Snuffing" "of Sortilege" "of Spellcraft" "of Spirit" "of Splintering" "of Stifling" "of Suturing" "of Tacati" "of Talent" "of Taunting" "of Training" "of Tzteosh" "of Unholy Might" "of Unmaking" "of Vampirism" "of Variegation" "of Vivification" "of Voltage" "of Weaponcraft" "of Will" "of Wounding" "of Youth" "of Zeal" "of Zealousness" "of the Assassin" "of the Bastion" "of the Blur" "of the Comet" "of the Conservator" "of the Deadeye" "of the Deathless" "of the Elements" "of the Essence" "of the Fanatical" "of the Furnace" "of the Gale" "of the Gelid" "of the Genius" "of the Gods" "of the Godslayer" "of the Hearth" "of the Ice" "of the Inferno" "of the Infinite" "of the Inquisitor" "of the Jaguar" "of the Kraken" "of the Leviathan" "of the Lightning Rod" "of the Lightning" "of the Maelstrom" "of the Magma" "of the Mammoth" "of the Marksman" "of the Multiverse" "of the Phantom" "of the Phoenix" "of the Polar Bear" "of the Polymath" "of the Protector" "of the Rainbow" "of the Ranger" "of the Sacred Grove" "of the Savant" "of the Solar Storm" "of the Span" "of the Taskmaster" "of the Tempest" "of the Titan" "of the Tourniquet" "of the Underground" "of the Universe" "of the Veil" "of the Virtuoso" "of the Volcano" "of the Walrus" "of the Wind" "of the Zealous" "u" "y"
#  - Cluster Jewels -
# EnchantmentPassiveNode "Area Damage" "Armour" "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield" "Attack Damage" "Axe and Sword Damage" "Bow Damage" "Brand Damage" "Chance to Block Attack Damage" "Channelling Skill Damage" "Chaos Damage" "Chaos Resistance" "Cold Damage" "Critical Chance" "Dagger and Claw Damage" "Damage over Time" "Damage with Two Handed Weapons" "Effect of Non-Damaging Ailments" "Elemental Damage" "Exerted Attack Damage" "Fire Damage over Time" "Fire Damage" "Flask Duration" "Life" "Lightning Damage" "Mace and Staff Damage" "Minion Damage" "Minion Life" "Physical Damage" "Projectile Damage" "Reservation Efficiency" "Spell Damage" "Suppres" "Totem Damage" "Trap and Mine Damage" "Wand Damage"
# EnchantmentPassiveNum <= 2"


# FILTER UPDATE INFO   https://www.pathofexile.com/forum/view-thread/3788869
# NEW GEMS
# "Heavy Strike of Trarthus" "Spectral Shield Throw of Trarthus" "Spectral Throw of Trarthus" "Storm Call of Trarthus" "Blast Rain of Trarthus" "Siege Ballista of Trarthus" "Sunder of Trarthus" "Wave of Conviction of Trarthus" "Chain Hook of Trarthus" "Spectral Helix of Trarthus" "Bladefall of Trarthus"

"""

color_text = """

#============================================================================================================
#	   Color
#============================================================================================================

# -------------- Text Color ----------------------------
Show
	Rarity Normal
	SetTextColor 200 200 200 255
	MinimapIcon 2 Grey Circle
	Continue

Show
	Rarity Magic
	SetTextColor 131 131 247 255
	MinimapIcon 2 Blue Circle
	Continue

Show
	Rarity Rare
	ItemLevel > 90
	SetTextColor 255 127 0 255
	MinimapIcon 2 Orange Circle
	Continue

Show
	Rarity Rare
	ItemLevel > 83
	ItemLevel <= 89
	SetTextColor 245 190 0 255
	MinimapIcon 2 Yellow Circle
	Continue

Show
	Rarity Rare
	ItemLevel <= 83
	SetTextColor 254 254 118 255
	MinimapIcon 2 Yellow Circle
	Continue

Show
	Rarity Unique
	SetFontSize 45
	SetTextColor 175 95 28 255
	SetBorderColor 175 95 28 255
	PlayAlertSound 3 300
	PlayEffect Brown
	MinimapIcon 2 Brown Star

Show
	Class == "Skill Gems" "Support Gems"
	SetTextColor 30 190 190 255
	Continue
"""

color_border = """
# ------------------- Borders -----------------------------------
Show
	Mirrored True
	Class == "Amulets" "Belts" "Body Armour" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wand" "Wands" "Warstaves"
	SetBorderColor 180 0 0 255
	Continue

Show
	Corrupted True
	Class == "Amulets" "Belts" "Body Armour" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wand" "Wands" "Warstaves"
	SetBorderColor 180 0 0 255
	Continue

Show
	FracturedItem True
	Class == "Amulets" "Belts" "Body Armour" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wand" "Wands" "Warstaves"
	SetBorderColor 0 0 255 255
	Continue

Show
	SynthesisedItem True
	Class == "Amulets" "Belts" "Body Armour" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wand" "Wands" "Warstaves"
	SetBorderColor 175 67 219 255
	Continue

Show
	HasExplicitMod >=1 "Catarina's Veiled" "Elreon's Veiled" "Gravicius' Veiled" "Guff's Veiled" "It That Fled's Veiled" "Korell's Veiled" "Leo's Veiled" "Rin's Veiled" "Tora's Veiled" "Vagan's Veiled" "Veil" "Veiled" "Vorici's Veiled" "of Aisling's Veil" "of Cameria's Veil" "of Hillock's Veil" "of Janus' Veil" "of Jorgin's Veil" "of the Veil"
	SetBorderColor 20 190 20 255
	Continue

"""

color_background = """
# ------------------- Backgrounds --------------------------
Show
	Class == "Flask" "Hybrid Flasks" "Life Flasks" "Mana Flasks" "Tinctures" "Utility Flasks"
	SetBackgroundColor 20 90 0 180
	Continue

Show
	Class == "Wand" "Wands"
	SetBackgroundColor 86 88 29 255
	MinimapIcon 2 Blue Circle
	Continue

Show
	Class == "Abyss Jewels" "Jewels"
	SetBackgroundColor 138 50 50 255
	MinimapIcon 2 Red Hexagon
	Continue

Show
	SocketGroup "RGB"
	SetBackgroundColor 130 110 110 255
	Continue

Show
	Sockets >= 6
	SetBackgroundColor 155 138 138 255
	Continue

Show
	SocketGroup "W"
	SetBackgroundColor 255 255 255 255
	Continue

Show
	SocketGroup "A"
	SetBackgroundColor 0 180 0 255
	Continue

Show
	SocketGroup "D"
	SetBackgroundColor 0 180 0 255
	Continue

Show
	# Class == "Body Armours" "Boots" "Gloves" "Helmets" "Shields"
	BaseType == "Royal Plate" "Syndicate's Garb" "Twilight Regalia" "Conquest Lamellar" "Sacred Chainmail" "Necrotic Armour" "Leviathan Greaves" "Velour Boots" "Warlock Boots" "Wyvernscale Boots" "Paladin Boots" "Phantom Boots" "Leviathan Gauntlets" "Velour Gloves" "Warlock Gloves" "Wyvernscale Gauntlets" "Paladin Gloves" "Phantom Mitts" "Giantslayer Helmet" "Majestic Pelt" "Lich's Circlet" "Haunted Bascinet" "Divine Crown" "Torturer's Mask" "Ezomyte Tower Shield" "Colossal Tower Shield" "Pinnacle Tower Shield" "Lacquered Buckler" "Crusader Buckler" "Imperial Buckler" "Fossilised Spirit Shield" "Titanium Spirit Shield" "Harmonic Spirit Shield" "Cardinal Round Shield" "Elegant Round Shield" "Archon Kite Shield" "Champion Kite Shield" "Supreme Spiked Shield"
	BaseDefencePercentile >= 90
	SetBackgroundColor 0 92 0 255 # Dark Green BG
	MinimapIcon 2 Green Circle
	Continue

Show	# Atlas base
	BaseType == "Apothecary's Gloves" "Fingerless Silk Gloves" "Fugitive Boots" "Gripped Gloves" "Spiked Gloves" "Two-Toned Boots"  "Two-Toned Boots"  "Two-Toned Boots" "Convoking Wand" "Bone Helmet" "Artillery Quiver" "Marble Amulet" "Seaglass Amulet" "Blue Pearl Amulet" "Vanguard Belt" "Crystal Belt" "Cerulean Ring" "Iolite Ring" "Opal Ring" "Steel Ring" "Vermillion Ring"
	SetBackgroundColor 0 188 155 255
	Continue

Show	# Talismans
	AnyEnchantment True
	SetBackgroundColor 255 0 0 255 # Red BG
	MinimapIcon 0 Red Circle
	Continue
""" 

custom1 = """
Show
	EnchantmentPassiveNum <= 1
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 133 20 46 255 # Wine Red BG	133 20 46
	MinimapIcon 0 Red Circle

Show
	EnchantmentPassiveNum >= 1
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 133 20 46 255 # Wine Red BG	133 20 46
	MinimapIcon 0 Red Circle


# ----------------- Deprecated -----------------------------

# Show
#	Class == "Idols"
#	SetFontSize 45
#	SetBorderColor 0 240 190 255
#	SetBackgroundColor 20 20 0 255
#	PlayAlertSound 3 300
#	PlayEffect Blue
#	MinimapIcon 1 Blue Diamond
"""

currency = """

#============================================================================================================
#	   Currency
#============================================================================================================

Show
	BaseType == "Gold"
	SetFontSize 35
	SetTextColor 161 157 99 255
	SetBorderColor 161 157 99 255
	SetBackgroundColor 20 20 0 180
	MinimapIcon 2 Yellow Cross

Show
	BaseType == "Rogue's Marker"
	SetFontSize 40
	SetTextColor 175 67 219 255
	SetBorderColor 175 67 219 255
	SetBackgroundColor 20 20 0 255
	MinimapIcon 1 Yellow Cross

Show
	Class "Stackable Currency"
	BaseType == "Ancient Orb" "Ancient Shard" "Blessed Orb" "Divine Orb" "Engineer's Orb" "Engineer's Shard" "Enkindling Orb" "Exalted Orb" "Exalted Shard" "Fracturing Shard" "Gemcutter's Prism" "Glassblower's Bauble" "Harbinger's Orb" "Harbinger's Shard" "Orb of Horizons" "Horizon Shard" "Chaos Orb" "Chaos Shard" "Instilling Orb" "Mirror of Kalandra" "Mirror Shard" "Orb of Annulment" "Annulment Shard" "Regal Orb" "Regal Shard" "Sacred Orb" "Hinekora's Lock" "Blighted Scouting Report" "Comprehensive Scouting Report" "Delirious Scouting Report" "Operative's Scouting Report" "Singular Scouting Report" "Vaal Scouting Report" "Influenced Scouting Report" "Otherworldly Scouting Report" "Awakener's Orb" "Crescent Splinter" "Crusader's Exalted Orb" "Eldritch Chaos Orb" "Eldritch Exalted Orb" "Eldritch Orb of Annulment" "Exceptional Eldritch Ember" "Exceptional Eldritch Ichor" "Grand Eldritch Ember" "Grand Eldritch Ichor" "Greater Eldritch Ember" "Greater Eldritch Ichor" "Hunter's Exalted Orb" "Maven's Chisel of Avarice" "Maven's Chisel of Divination" "Maven's Chisel of Procurement" "Maven's Chisel of Scarabs" "Orb of Conflict" "Orb of Dominance" "Redeemer's Exalted Orb" "Warlord's Exalted Orb" "Crimson Oil" "Black Oil" "Opalescent Oil" "Silver Oil" "Golden Oil" "Reflective Oil" "Tainted Oil" "Prismatic Oil"
	SetFontSize 40
	SetTextColor 175 67 219 255
	SetBorderColor 175 67 219 255  # 134 33 176
	SetBackgroundColor 20 20 0 255
	PlayEffect Purple
	MinimapIcon 0 Orange Cross

Show
	Class "Stackable Currency"
	SetFontSize 40
	SetTextColor 175 67 219 255
	SetBorderColor 175 67 219 255  # 134 33 176
	SetBackgroundColor 20 20 0 255
	MinimapIcon 1 Yellow Cross

Show
	Class == "Divination Cards"
	SetFontSize 45
	SetTextColor 39 141 192 255
	SetBorderColor 39 141 192 255
	SetBackgroundColor 20 20 0 255
	MinimapIcon 2 Grey Triangle

Show
	Class == "Breachstones"
	SetFontSize 45
	SetTextColor 255 255 255 255
	SetBorderColor 255 255 255 255
	SetBackgroundColor 180 0 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Hexagon

Show
	Class == "Map Fragments"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 175 120 230 240
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Hexagon

Show
	Class == "Incubators"
	SetFontSize 45
	SetTextColor 0 0 0 255
	SetBorderColor 0 0 0 255
	SetBackgroundColor 249 150 25 255
	PlayAlertSound 2 300
	PlayEffect White
	MinimapIcon 2 White Circle
"""

gems_jewels = """

#============================================================================================================
#	   Gems + Jewels
#============================================================================================================

Show
	Rarity Rare
	Class == "Abyss Jewels" "Jewel" "Jewels"
	SetFontSize 40

Show
	Rarity Magic
	Class == "Abyss Jewels"
	SetFontSize 40

Show
	Class == "Skill Gems" "Support Gems"
	BaseType == "Empower Support" "Enhance Support" "Enlighten Support" "Item Quantity Support" "Vaal Breach" "Portal"
	SetFontSize 45
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show
	Class == "Skill Gems" "Support Gems"
	BaseType "Awakened"
	SetFontSize 45
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show
	GemLevel >= 15
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show
	Quality >= 20
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show
	TransfiguredGem True
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetBorderColor 240 0 0 255
	SetBackgroundColor 70 0 20 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Triangle

Show
	Class == "Skill Gems" "Support Gems"
	BaseType "Vaal"
	SetFontSize 45
	SetBorderColor 40 130 130 255
	PlayEffect Grey Temp
	MinimapIcon 1 Grey Triangle

Show
	Quality >= 1
	Class == "Skill Gems" "Support Gems"
	SetFontSize 45
	SetBorderColor 40 130 130 255
	PlayEffect Grey Temp
	MinimapIcon 1 Grey Triangle

Show
	Class == "Skill Gems" "Support Gems"
	GemLevel >= 15
	SetFontSize 45
	SetBorderColor 40 130 130 255
	PlayEffect Grey Temp
	MinimapIcon 1 Grey Triangle
"""

weapon_armour = f"""
#============================================================================================================
#	   Weapons+Armour
#============================================================================================================


#===============================================================================================================
# [[0500]] Exotic Bases
#===============================================================================================================
# !! Waypoint c1.exotic.all : "Exotic - Expedition, exotic Talismans, Sacrificial garbs"
# These bases don't usually drop during normal gameplay and are usually only acquired form certain sources
# These are bases such as heist and ritual bases.

Show # $type->exoticbases $tier->exoticheistbases
	Rarity Normal Magic Rare
	BaseType == "Accumulator Wand" "Alternating Sceptre" "Anarchic Spiritblade" "Apex Cleaver" "Astrolabe Amulet" "Banishing Blade" "Battery Staff" "Blasting Blade" "Boom Mace" "Capricious Spiritblade" "Cogwork Ring" "Cold-attuned Buckler" "Composite Ring" "Congregator Wand" "Crack Mace" "Crushing Force Magnifier" "Disapprobation Axe" "Eventuality Rod" "Flashfire Blade" "Focused Amulet" "Foundry Bow" "Geodesic Ring" "Heat-attuned Tower Shield" "Helical Ring" "Honed Cleaver" "Impact Force Propagator" "Infernal Blade" "Magmatic Tower Shield" "Malign Fangs" "Manifold Ring" "Mechalarm Belt" "Mechanical Belt" "Micro-Distillery Belt" "Oscillating Sceptre" "Pneumatic Dagger" "Polar Buckler" "Potentiality Rod" "Pressurised Dagger" "Psychotic Axe" "Ratcheting Ring" "Reciprocation Staff" "Simplex Amulet" "Solarine Bow" "Stabilising Sceptre" "Subsuming Spirit Shield" "Transfer-attuned Spirit Shield" "Void Fangs"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # $type->exoticbases $tier->exoticritualbases
	Rarity Normal Magic Rare
	BaseType == "Aetherwind Gloves" "Apprentice Gloves" "Archdemon Crown" "Atonement Mask" "Basemetal Treads" "Blizzard Crown" "Brimstone Treads" "Cloudwhisper Boots" "Darksteel Treads" "Demon Crown" "Dreamquest Slippers" "Duskwalk Slippers" "Gale Crown" "Guarding Gauntlets" "Imp Crown" "Leyline Gloves" "Nexus Gloves" "Nightwind Slippers" "Penitent Mask" "Preserving Gauntlets" "Sorrow Mask" "Stormrider Boots" "Thwarting Gauntlets" "Tinker Gloves" "Trapsetter Gloves" "Windbreak Boots" "Winter Crown"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # $type->exoticbases $tier->exoticlakekala
	Rarity Normal Magic Rare
	BaseType == "Dusk Ring" "Gloam Ring" "Penumbra Ring" "Shadowed Ring" "Tenebrous Ring"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D5 $type->exoticbases $tier->exoticexpeditionbases
	Rarity Normal Magic Rare
	BaseType == "Iron Flask" "Runic Crest" "Runic Crown" "Runic Gages" "Runic Gauntlets" "Runic Gloves" "Runic Greaves" "Runic Helm" "Runic Sabatons" "Runic Sollerets"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # $type->exoticbases $tier->exotictalismanbases $artefactex
	Rarity Normal Magic Rare
	BaseType == "Greatwolf Talisman" "Rot Head Talisman"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # $type->exoticbases $tier->exoticbasesmisc
	Rarity Normal Magic Rare
	BaseType == "Grasping Mail"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # $type->exoticbases $tier->exoticuniquebases
	Rarity Normal Magic Rare
	BaseType == "Nameless Ring" "Ornate Quiver" "Prismatic Jewel" "Ring" "Ruby Amulet" "Unset Amulet"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D6 $type->exoticbaseslower $tier->stygian86
	Mirrored False
	Corrupted False
	ItemLevel >= 86
	Rarity Normal Magic Rare
	BaseType == "Stygian Vise"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show # %D5 $type->exoticbaseslower $tier->stygian
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	BaseType == "Stygian Vise"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show # %D6 $type->exoticbaseslower $tier->exoticsacrificial
	Mirrored False
	Corrupted False
	Rarity Normal Magic Rare
	BaseType == "Sacrificial Garb"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

Show
	BaseType == "Sacrificial Garb" "Stygian Vise"
	SetFontSize 45
	SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 20 20 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 1 Blue Diamond

# ----------------------------------------------------

Show	# Atlas base
	BaseType == "Apothecary's Gloves" "Fingerless Silk Gloves" "Fugitive Boots" "Gripped Gloves" "Spiked Gloves" "Two-Toned Boots"  "Two-Toned Boots"  "Two-Toned Boots" "Convoking Wand" "Bone Helmet" "Artillery Quiver" "Marble Amulet" "Seaglass Amulet" "Blue Pearl Amulet" "Vanguard Belt" "Crystal Belt" "Cerulean Ring" "Iolite Ring" "Opal Ring" "Steel Ring" "Vermillion Ring"
	# BaseType == "Atlas"
	# Rarity Normal Magic Rare
	SetFontSize 40
	# SetTextColor 0 240 190 255
	# SetBorderColor 0 240 190 255
	# SetBackgroundColor 20 20 0 255
	# PlayAlertSound 12 100
	# PlayEffect Cyan
	MinimapIcon 1 Cyan Diamond

Show
	HasExplicitMod >=1 "Catarina's Veiled" "Elreon's Veiled" "Gravicius' Veiled" "Guff's Veiled" "It That Fled's Veiled" "Korell's Veiled" "Leo's Veiled" "Rin's Veiled" "Tora's Veiled" "Vagan's Veiled" "Veil" "Veiled" "Vorici's Veiled" "of Aisling's Veil" "of Cameria's Veil" "of Hillock's Veil" "of Janus' Veil" "of Jorgin's Veil" "of the Veil"
	SetFontSize 45

Show # $type->influenced->common $tier->t1_exo
	# HasInfluence Crusader Elder Hunter Redeemer Shaper Warlord
	Rarity Rare
	BaseType == "Accumulator Wand" "Aetherwind Gloves" "Alternating Sceptre" "Anarchic Spiritblade" "Apex Cleaver" "Apprentice Gloves" "Archdemon Crown" "Astrolabe Amulet" "Atonement Mask" "Banishing Blade" "Basemetal Treads" "Battery Staff" "Blasting Blade" "Blizzard Crown" "Boom Mace" "Brimstone Treads" "Capricious Spiritblade" "Cloudwhisper Boots" "Cogwork Ring" "Cold-attuned Buckler" "Composite Ring" "Congregator Wand" "Crack Mace" "Crushing Force Magnifier" "Darksteel Treads" "Demon Crown" "Disapprobation Axe" "Dreamquest Slippers" "Duskwalk Slippers" "Eventuality Rod" "Flashfire Blade" "Focused Amulet" "Foundry Bow" "Gale Crown" "Geodesic Ring" "Guarding Gauntlets" "Heat-attuned Tower Shield" "Helical Ring" "Honed Cleaver" "Imp Crown" "Impact Force Propagator" "Infernal Blade" "Leyline Gloves" "Magmatic Tower Shield" "Malign Fangs" "Manifold Ring" "Mechanical Belt" "Micro-Distillery Belt" "Nexus Gloves" "Nightwind Slippers" "Ornate Quiver" "Oscillating Sceptre" "Penitent Mask" "Pneumatic Dagger" "Polar Buckler" "Potentiality Rod" "Preserving Gauntlets" "Pressurised Dagger" "Psychotic Axe" "Ratcheting Ring" "Reciprocation Staff" "Runic Crest" "Runic Crown" "Runic Gages" "Runic Gauntlets" "Runic Gloves" "Runic Greaves" "Runic Helm" "Runic Sabatons" "Runic Sollerets" "Simplex Amulet" "Solarine Bow" "Sorrow Mask" "Stabilising Sceptre" "Stormrider Boots" "Subsuming Spirit Shield" "Thwarting Gauntlets" "Tinker Gloves" "Transfer-attuned Spirit Shield" "Trapsetter Gloves" "Void Fangs" "Windbreak Boots" "Winter Crown"
	SetFontSize 45
	SetTextColor 50 130 165 255
	SetBorderColor 50 130 165 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Diamond

Show
	HasInfluence Crusader Elder Hunter Redeemer Shaper Warlord
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 45
	SetBorderColor 50 130 165 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Diamond

Show
	Rarity Rare
	Class == "Wands"
	ItemLevel > 75
	SetFontSize 30

Show
	Rarity Normal Magic Rare
	BaseType == "Prophecy Wand" "Omen Wand" "Accumulator Wand"
	ItemLevel > 64
	SetFontSize 35

Show
	LinkedSockets >= 6
	# Rarity Normal Magic Rare
	SetFontSize 45
	SetBorderColor 255 255 255 255
	SetBackgroundColor 200 0 0 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Diamond

Show
	LinkedSockets 5
	# Rarity Normal Magic Rare
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

Show
	Sockets >= 6
	# Rarity Normal Magic Rare
	SetFontSize 45
	PlayAlertSound 2 300
	PlayEffect Grey
	MinimapIcon 2 Grey Hexagon

Show
	# Sockets >= A
	SocketGroup "A"
	SetFontSize 45
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show
	Rarity Rare
	SocketGroup "W"
	LinkedSockets >= 3
	SetFontSize 45
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

Show
	SocketGroup "D"
	SetFontSize 45
	PlayAlertSound 6 300
	PlayEffect Red
	MinimapIcon 0 Red Star

{show_rgb}

Show
	Quality >= 20
	# ItemLevel >= 84
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 45
	# SetTextColor 0 240 190 255
	SetBorderColor 0 240 190 255
	# SetBackgroundColor 0 75 30 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 0 Blue Diamond

Show
	BaseType ==  "Breach Ring"
	SetFontSize 45
	SetBorderColor 0 240 190 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

Show
	Rarity Rare
	Class == "Amulets" "Rings"
	SetFontSize 45
	SetBorderColor 245 190 0 255
	# SetBackgroundColor 20 20 0 255

Show
	HasCruciblePassiveTree True
	# Rarity Normal Magic Rare
	SetFontSize 45
	SetBorderColor 0 240 190 255
	SetBackgroundColor 210 0 0 255
	PlayAlertSound 3 300
	PlayEffect Blue
	MinimapIcon 2 Blue Diamond

Show
	Rarity Rare
	Corrupted True
	ItemLevel >= 70

Show
	Rarity Rare
	Mirrored True
	ItemLevel >= 70

Show
	# Rarity Magic Rare
	FracturedItem True
	# ItemLevel >= 70
	SetFontSize 45

Show
	# Rarity Magic Rare
	SynthesisedItem True
	# ItemLevel >= 70
	SetFontSize 45

Show
	# Rarity Magic Rare
	Identified True
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	SetFontSize 30

Show
	Rarity Rare
	Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
	ItemLevel >= 86
	SetFontSize 30




# ------- Crafting Quality Perfection -----------

Show
	Mirrored False
	Corrupted False
	ItemLevel >= 75
 	BaseDefencePercentile >= 93
	BaseType == "Royal Plate" "Syndicate's Garb" "Twilight Regalia" "Conquest Lamellar" "Sacred Chainmail" "Necrotic Armour" "Leviathan Greaves" "Velour Boots" "Warlock Boots" "Wyvernscale Boots" "Paladin Boots" "Phantom Boots" "Leviathan Gauntlets" "Velour Gloves" "Warlock Gloves" "Wyvernscale Gauntlets" "Paladin Gloves" "Phantom Mitts" "Giantslayer Helmet" "Majestic Pelt" "Lich's Circlet" "Haunted Bascinet" "Divine Crown" "Torturer's Mask" "Ezomyte Tower Shield" "Colossal Tower Shield" "Pinnacle Tower Shield" "Lacquered Buckler" "Crusader Buckler" "Imperial Buckler" "Fossilised Spirit Shield" "Titanium Spirit Shield" "Harmonic Spirit Shield" "Cardinal Round Shield" "Elegant Round Shield" "Archon Kite Shield" "Champion Kite Shield" "Supreme Spiked Shield"
	SetFontSize 35
	PlayAlertSound 3 300
	PlayEffect Green
	MinimapIcon 1 Green Diamond

Show
	Mirrored False
	Corrupted False
	BaseDefencePercentile >= 66
	Rarity Rare Magic
	BaseType == "Royal Plate" "Syndicate's Garb" "Twilight Regalia" "Conquest Lamellar" "Sacred Chainmail" "Necrotic Armour" "Leviathan Greaves" "Velour Boots" "Warlock Boots" "Wyvernscale Boots" "Paladin Boots" "Phantom Boots" "Leviathan Gauntlets" "Velour Gloves" "Warlock Gloves" "Wyvernscale Gauntlets" "Paladin Gloves" "Phantom Mitts" "Giantslayer Helmet" "Majestic Pelt" "Lich's Circlet" "Haunted Bascinet" "Divine Crown" "Torturer's Mask" "Ezomyte Tower Shield" "Colossal Tower Shield" "Pinnacle Tower Shield" "Lacquered Buckler" "Crusader Buckler" "Imperial Buckler" "Fossilised Spirit Shield" "Titanium Spirit Shield" "Harmonic Spirit Shield" "Cardinal Round Shield" "Elegant Round Shield" "Archon Kite Shield" "Champion Kite Shield" "Supreme Spiked Shield"

Hide
	Rarity Rare Magic Normal
	AnyEnchantment False
	FracturedItem False
	HasCruciblePassiveTree False
	SynthesisedItem False
	BaseType == "Royal Plate" "Syndicate's Garb" "Twilight Regalia" "Conquest Lamellar" "Sacred Chainmail" "Necrotic Armour" "Leviathan Greaves" "Velour Boots" "Warlock Boots" "Wyvernscale Boots" "Paladin Boots" "Phantom Boots" "Leviathan Gauntlets" "Velour Gloves" "Warlock Gloves" "Wyvernscale Gauntlets" "Paladin Gloves" "Phantom Mitts" "Giantslayer Helmet" "Majestic Pelt" "Lich's Circlet" "Haunted Bascinet" "Divine Crown" "Torturer's Mask" "Ezomyte Tower Shield" "Colossal Tower Shield" "Pinnacle Tower Shield" "Lacquered Buckler" "Crusader Buckler" "Imperial Buckler" "Fossilised Spirit Shield" "Titanium Spirit Shield" "Harmonic Spirit Shield" "Cardinal Round Shield" "Elegant Round Shield" "Archon Kite Shield" "Champion Kite Shield" "Supreme Spiked Shield"


# ------- High tier wepons ------------

Show
	Rarity Rare
	BaseType == "Maraketh Bow" "Imperial Bow" "Harbinger Bow" "Ranger Bow" "Assassin Bow" "Steelwood Bow" "Vaal Claw" "Eye Gouger" "Imperial Claw" "Gemini Claw" "Ambusher" "Sai" "Royal Axe" "Runic Hatchet" "Gavel" "Behemoth Mace" "Vaal Blade" "Midnight Blade" "Tiger Hook" "Legion Sword" "Primal Arrow Quiver" "Demon Dagger" "Platinum Kris" "Void Sceptre" "Sambar Sceptre" "Opal Sceptre" "Imperial Staff" "Eclipse Staff" "Harpy Rapier" "Dragoon Sword" "Void Axe" "Fleshripper" "Karui Chopper" "Vaal Axe" "Sundering Axe" "Imperial Maul" "Terror Maul" "Coronal Maul" "Vaal Greatsword" "Lion Sword" "Infernal Sword" "Reaver Sword" "Ezomyte Blade" "Exquisite Blade" "Prophecy Wand" "Profane Wand" "Omen Wand" "Maelström Staff" "Judgement Staff"
	# ItemLevel >= 86
	SetFontSize 40

# Show
#	 Rarity Rare
#	 BaseType == "Maraketh Bow" "Imperial Bow" "Harbinger Bow" "Ranger Bow" "Assassin Bow" "Steelwood Bow" "Vaal Claw" "Eye Gouger" "Imperial Claw" "Gemini Claw" "Ambusher" "Sai" "Royal Axe" "Runic Hatchet" "Gavel" "Behemoth Mace" "Vaal Blade" "Midnight Blade" "Tiger Hook" "Legion Sword" "Primal Arrow Quiver" "Demon Dagger" "Platinum Kris" "Void Sceptre" "Sambar Sceptre" "Opal Sceptre" "Imperial Staff" "Eclipse Staff" "Harpy Rapier" "Dragoon Sword" "Void Axe" "Fleshripper" "Karui Chopper" "Vaal Axe" "Sundering Axe" "Imperial Maul" "Terror Maul" "Coronal Maul" "Vaal Greatsword" "Lion Sword" "Infernal Sword" "Reaver Sword" "Ezomyte Blade" "Exquisite Blade" "Prophecy Wand" "Profane Wand" "Omen Wand" "Maelström Staff" "Judgement Staff"
#	 ItemLevel <= 85
#	 SetFontSize 30

Hide
	Rarity Magic
	AnyEnchantment False
	# Corrupted False
	FracturedItem False
	HasCruciblePassiveTree False
	Identified False
	# Mirrored False
	SynthesisedItem False
	Quality < 20
	BaseType == "Maraketh Bow" "Imperial Bow" "Harbinger Bow" "Ranger Bow" "Assassin Bow" "Steelwood Bow" "Vaal Claw" "Eye Gouger" "Imperial Claw" "Gemini Claw" "Ambusher" "Sai" "Royal Axe" "Runic Hatchet" "Gavel" "Behemoth Mace" "Vaal Blade" "Midnight Blade" "Tiger Hook" "Legion Sword" "Primal Arrow Quiver" "Demon Dagger" "Platinum Kris" "Void Sceptre" "Sambar Sceptre" "Opal Sceptre" "Imperial Staff" "Eclipse Staff" "Harpy Rapier" "Dragoon Sword" "Void Axe" "Fleshripper" "Karui Chopper" "Vaal Axe" "Sundering Axe" "Imperial Maul" "Terror Maul" "Coronal Maul" "Vaal Greatsword" "Lion Sword" "Infernal Sword" "Reaver Sword" "Ezomyte Blade" "Exquisite Blade" "Prophecy Wand" "Profane Wand" "Omen Wand" "Maelström Staff" "Judgement Staff"

Hide
	Rarity Normal
	Quality < 20
	BaseType == "Maraketh Bow" "Imperial Bow" "Harbinger Bow" "Ranger Bow" "Assassin Bow" "Steelwood Bow" "Vaal Claw" "Eye Gouger" "Imperial Claw" "Gemini Claw" "Ambusher" "Sai" "Royal Axe" "Runic Hatchet" "Gavel" "Behemoth Mace" "Vaal Blade" "Midnight Blade" "Tiger Hook" "Legion Sword" "Primal Arrow Quiver" "Demon Dagger" "Platinum Kris" "Void Sceptre" "Sambar Sceptre" "Opal Sceptre" "Imperial Staff" "Eclipse Staff" "Harpy Rapier" "Dragoon Sword" "Void Axe" "Fleshripper" "Karui Chopper" "Vaal Axe" "Sundering Axe" "Imperial Maul" "Terror Maul" "Coronal Maul" "Vaal Greatsword" "Lion Sword" "Infernal Sword" "Reaver Sword" "Ezomyte Blade" "Exquisite Blade" "Prophecy Wand" "Profane Wand" "Omen Wand" "Maelström Staff" "Judgement Staff"

"""

flasks = """
#============================================================================================================
#	   Flasks
#============================================================================================================

Show
	Rarity Normal Magic
	Class == "Flask" "Hybrid Flasks" "Life Flasks" "Mana Flasks" "Tinctures" "Utility Flasks"
	Quality >= 1
	SetFontSize 40

Show
	Rarity Normal Magic
	Class == "Utility Flasks"
	ItemLevel >= 84
	SetFontSize 40

Hide
	Rarity Normal Magic
	Class == "Tinctures"
	BaseType == "Ironwood Tincture" "Prismatic Tincture" "Rosethorn Tincture" "Ashbark Tincture" "Borealwood Tincture" "Fulgurite Tincture" "Blood Sap Tincture" "Poisonberry Tincture" "Sporebloom Tincture" "Oakbranch Tincture"
	Quality = 0
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Normal Magic
	Class == "Mana Flasks"
	BaseType == "Small Mana Flask" "Medium Mana Flask" "Large Mana Flask" "Greater Mana Flask" "Grand Mana Flask" "Giant Mana Flask" "Colossal Mana Flask" "Sacred Mana Flask" "Hallowed Mana Flask" "Sanctified Mana Flask" "Divine Mana Flask" "Eternal Mana Flask"
	Quality = 0
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Normal Magic
	Class == "Life Flasks"
	BaseType == "Small Life Flask" "Medium Life Flask" "Large Life Flask" "Greater Life Flask" "Grand Life Flask" "Giant Life Flask" "Colossal Life Flask" "Sacred Life Flask" "Hallowed Life Flask" "Sanctified Life Flask" "Divine Life Flask" "Eternal Life Flask"
	Quality = 0
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Normal Magic
	Class == "Hybrid Flasks"
	BaseType == "Small Hybrid Flask" "Medium Hybrid Flask" "Large Hybrid Flask" "Colossal Hybrid Flask" "Sacred Hybrid Flask" "Hallowed Hybrid Flask"
	Quality = 0
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Normal Magic
	Class == "Utility Flasks"
	BaseType == "Amethyst Flask" "Aquamarine Flask" "Basalt Flask" "Bismuth Flask" "Corundum Flask" "Diamond Flask" "Granite Flask" "Jade Flask" "Quartz Flask" "Quicksilver Flask" "Ruby Flask" "Sapphire Flask" "Silver Flask" "Stibnite Flask" "Sulphur Flask" "Topaz Flask" # "Gold Flask" "Iron Flask"
	Quality = 0
	ItemLevel <= 83
	SetFontSize 30
	DisableDropSound True
"""

maps = """
#============================================================================================================
#	   Maps
#============================================================================================================

# ------ Borders -------
Show
	MapTier >= 16
	Class == "Maps"
	SetFontSize 45
	SetBorderColor 9 29 230 255
	PlayAlertSound 7 200
	PlayEffect Blue
	MinimapIcon 2 Blue Square
	Continue

Show
	MapTier <= 15
	MapTier >= 11
	Class == "Maps"
	SetFontSize 40
	SetBorderColor 230 29 9 255
	PlayAlertSound 8 100
	PlayEffect Red
	MinimapIcon 2 Red Square
	Continue

Show
	MapTier >= 6
	MapTier <= 10
	Class == "Maps"
	SetFontSize 40
	SetBorderColor 251 204 65 255
	PlayAlertSound 9 100
	PlayEffect Yellow
	MinimapIcon 2 Yellow Square
	Continue

Show
	MapTier <= 5
	Class == "Maps"
	SetFontSize 35
	SetBorderColor 255 255 255 255
	PlayAlertSound 9 100
	PlayEffect White
	MinimapIcon 2 White Square
	Continue

# ------ Backgrounds -------

Show
	Class == "Maps"
	Quality >= 1
	SetBackgroundColor 0 100 0 255
	Continue

Show
	Class == "Maps"
	Quality 0
	SetBackgroundColor 20 20 0 255
	Continue

Show
	Class == "Maps"
	MapTier = 17
	SetBackgroundColor 135 135 254 255
	Continue

Show	# Favored
	Class == "Maps"
	BaseType "Defiled" "Shore"
	SetBackgroundColor 20 46 133 255
	Continue

# ----------------------------

Show
	HasInfluence Shaper Elder Crusader Hunter Redeemer Warlord
	Class == "Maps"
	SetBackgroundColor 100 0 122 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Square

Show
	UberBlightedMap True
	Class == "Maps"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 145 30 220 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 0 Purple Square

Show
	BlightedMap True
	Class == "Maps"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 235 220 245 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 0 Purple Square

Show
	ElderMap True
	Class == "Maps"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 235 220 245 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 0 Purple Square

Show
	ShapedMap True
	Class == "Maps"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 235 220 245 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 0 Purple Square


Show
	Class == "Maps"
	BaseType == "Vaal Temple Map"
	SetFontSize 45
	SetTextColor 100 0 122 255
	SetBorderColor 100 0 122 255
	SetBackgroundColor 255 255 255 255
	PlayAlertSound 1 300
	PlayEffect Red
	MinimapIcon 0 Red Square

Show
	Corrupted True
	Identified True
	Class == "Maps"
	HasExplicitMod >=2 "a" "e" "i" "o" "u" "y"
	SetFontSize 45
	SetTextColor 145 30 220 255
	SetBorderColor 145 30 220 255
	SetBackgroundColor 235 220 245 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 0 Purple Square

Show
	AnyEnchantment True
	Class == "Maps"
	SetBackgroundColor 145 30 220 255
	PlayAlertSound 5 300
	PlayEffect Purple
	MinimapIcon 2 Purple Square

Show
	Class == "Maps"

Show
	Class == "Blueprints" "Contracts"
	SetFontSize 45
	SetTextColor 255 85 85 255
	SetBorderColor 255 85 85 255
	SetBackgroundColor 40 0 30 255
	PlayAlertSound 5 100
	PlayEffect Yellow
	MinimapIcon 2 Yellow UpsideDownHouse
"""

don_now_jet = """
#============================================================================================================
# Don nov jet
#============================================================================================================

Show	# OLD GEM SYSTEM. Deprecated in v3.23 , replaced by Transfigured Gem Sys
	AlternateQuality True
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 255 0 0 255 # Red BG
	MinimapIcon 0 Red Circle

Show
	HasEaterOfWorldsImplicit >= 1
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 0 0 255 255 # Blue BG
	MinimapIcon 0 Blue Circle

Show
	ElderItem True
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 0 0 255 255 # Blue BG
	MinimapIcon 0 Blue Circle

Show
	HasInfluence Crusader Elder Hunter Redeemer Shaper Warlord
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 255 255 0 255 # Yellow BG
	MinimapIcon 0 Yellow Circle

Show
	Scourged True
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 255 255 0 255 # Yellow BG
	MinimapIcon 0 Yellow Circle

Show
	HasSearingExarchImplicit >= 1
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 255 0 255 255 # Purple BG
	MinimapIcon 0 Purple Circle

Show
	ShaperItem True
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 255 0 255 255 # Purple BG
	MinimapIcon 0 Purple Circle

Show
	EnchantmentPassiveNode "Area Damage" "Armour" "Attack Damage while Dual Wielding" "Attack Damage while holding a Shield" "Attack Damage" "Axe and Sword Damage" "Bow Damage" "Brand Damage" "Chance to Block Attack Damage" "Channelling Skill Damage" "Chaos Damage" "Chaos Resistance" "Cold Damage" "Critical Chance" "Dagger and Claw Damage" "Damage over Time" "Damage with Two Handed Weapons" "Effect of Non-Damaging Ailments" "Elemental Damage" "Exerted Attack Damage" "Fire Damage over Time" "Fire Damage" "Flask Duration" "Life" "Lightning Damage" "Mace and Staff Damage" "Minion Damage" "Minion Life" "Physical Damage" "Projectile Damage" "Reservation Efficiency" "Spell Damage" "Suppres" "Totem Damage" "Trap and Mine Damage" "Wand Damage"
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 0 255 255 255 # Cyan BG
	MinimapIcon 0 Cyan Circle

Show	# For cluster jewels, check number of passives
	EnchantmentPassiveNum <= 1
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 133 20 46 255 # Wine Red BG
	MinimapIcon 0 Red Circle

Show
	EnchantmentPassiveNum >= 1
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 133 20 46 255 # Wine Red BG
	MinimapIcon 0 Red Circle

Show
	HasExplicitMod >=1 "Abating" "Abbot's" "Acuminate" "Adaptable" "Adept's" "Adroit" "Alpine" "Apparition's" "Apprentice's" "Archmage's" "Arctic" "Athlete's" "Battlemage's" "Beatified" "Beclouded" "Behemoth's" "Betrayer's" "Bishop's" "Biting" "Bitter" "Blasting" "Blazing" "Blistering" "Blue" "Bolting" "Brinerot" "Burning" "Burnished" "Buzzing" "Carapaced" "Carbonising" "Chaotic" "Charged" "Cheetah's" "Cherub's" "Chilled" "Chilling" "Citaqualotl" "Citaqualotl's" "Condensing" "Consecrated" "Corrosive" "Countess's" "Crackling" "Cremating" "Crocodile's" "Cruel" "Cryomancer's" "Crystalising" "Crystalline" "Dazzling" "Deceiver's" "Decrepifying" "Devastating" "Dictator's" "Discharging" "Dissolving" "Djinn's" "Duchess's" "Durable" "Eidolon's" "Electrocuting" "Elevated" "Elusory" "Emperor's" "Empress's" "Encased" "Enduring" "Enlightened" "Entombing" "Enveloped" "Esh's" "Essences" "Exalter's" "Exarch's" "Excruciating" "Expediting" "Fawn's" "Fearless" "Fecund" "Festering" "Flame Shaper's" "Flaming" "Flaring" "Fleet" "Foul-tongued" "Frigid" "Frost Singer's" "Frosted" "Fugitive" "Girded" "Glaciated" "Glimmering" "Glinting" "Glittering" "Glowing" "Glyphic" "Godly" "Guatelitzi" "Guatelitzi's" "Haku's" "Hale" "Hallowed" "Harrowing" "Haunted" "Healthy" "Heated" "Heavy" "Hellion's" "Hero's" "Hissing" "Honed" "Humming" "Ibex's" "Icy" "Illusion's" "Illusory" "Impaling" "Impenetrable" "Impervious" "Impregnable" "Incandescent" "Incanter's" "Incinerating" "Incisive" "Incorporeal" "Indomitable" "Infernal" "Inspired" "Interpermeated" "Interpolated" "Ionising" "Lacerating" "Lancing" "Lava Conjurer's" "Leadership" "Legend's" "Lich's" "Lissome" "Lithomancer's" "Mad Lord's" "Mage's" "Magister's" "Magmatic" "Magnifying" "Marchioness's" "Martinet's" "Master's" "Matatl" "Matatl's" "Mazarine" "Merciless" "Mirage's" "Mortifying" "Motivating" "Mutewind" "Nautilus's" "Nightmare's" "Overpowering" "Overseer's" "Paragon's" "Perandus'" "Phantasm's" "Piercing" "Polar" "Polished" "Priest's" "Prime" "Prior's" "Protective" "Provocateur's" "Puhuarte" "Pulsing" "Puncturing" "Pyroclastic" "Queen's" "Quintessential" "Ram's" "Rapturous" "Redblade" "Resilient" "Resolute" "Resonating" "Resplendent" "Riker" "Rimedweller's" "Robust" "Rotund" "Runic" "Runner's" "Rupturing" "Saintly" "Sanguine" "Sapphire" "Scholar's" "Scintillating" "Searing" "Seething" "Seraphim's" "Serrated" "Sharpened" "Sharpshooter's" "Shimmering" "Shining" "Shocking" "Sizzling" "Smiting" "Smoking" "Smouldering" "Snapping" "Sorcerer's" "Spirit's" "Splintermind's" "Sprinter's" "Stallion's" "Stalwart" "Stormbrewer's" "Stout" "Strong-Willed" "Sturdy" "Subterranean" "Surging" "Tacati" "Tacati's" "Taskmaster's" "Tecton's" "Tempered" "Tempest Master's" "Thaumaturgist's" "Thunderhand's" "Thwarting" "Topotante" "Topotante's" "Trapping" "Tul's" "Turncoat's" "Tyrannical" "Ultramarine" "Unassailable" "Unfaltering" "Unleashed" "Unmoving" "Unreal" "Unwavering" "Unyielding" "Urchin's" "Vaporous" "Vapourising" "Versatile" "Vicious" "Victor's" "Vigorous" "Vile" "Virile" "Vivid" "Vulcanist's" "Warding" "Wicked" "Winter Beckoner's" "Wizard's" "Xopec" "Xoph's" "Zaffre" "of Abjuration" "of Abuse" "of Acclimatisation" "of Acrimony" "of Adaptation" "of Adaption" "of Agitation" "of Archery" "of Arcing" "of Ashes" "of Athletics" "of Atrophy" "of Atrophying" "of Authority" "of Bameth" "of Berserking" "of Blasting" "of Blinding" "of Calamity" "of Celebration" "of Chilling" "of Coercion" "of Collision" "of Combusting" "of Command" "of Conflagrating" "of Convalescence" "of Crafting" "of Craiceann" "of Cunning" "of Delaying" "of Demolishing" "of Destruction" "of Deteriorating" "of Discharge" "of Disintegrating" "of Dissolution" "of Distraction" "of Ease" "of Efficiency" "of Enchanting" "of Entropy" "of Ephij" "of Euphoria" "of Everlasting" "of Eviction" "of Exile" "of Expertise" "of Expulsion" "of Exsanguinating" "of Fame" "of Farrul" "of Fenumus" "of Ferocity" "of Finesse" "of Fireproofing" "of Flames" "of Fleshbinding" "of Floe" "of Fortitude" "of Fury" "of Gelidity" "of Glaciation" "of Grandmastery" "of Grounding" "of Haast" "of Harmony" "of Harvest Beasts" "of Haunting" "of Heartstopping" "of Heating" "of Hemorrhaging" "of Hindering" "of Immolation" "of Incision" "of Incitation" "of Infamy" "of Insulation" "of Legerdemain" "of Lioneye" "of Liquefaction" "of Many" "of Mastery" "of Melting" "of Menace" "of Metamorphosis" "of Mysticism" "of Needling" "of Nimbleness" "of Nirvana" "of Nullification" "of Obstruction" "of Opportunity" "of Orchestration" "of Order" "of Penetrating" "of Phasing" "of Phlebotomising" "of Poise" "of Potency" "of Prestidigitation" "of Puhuarte" "of Puncturing" "of Rage" "of Recuperation" "of Relishing" "of Rending" "of Resilience" "of Resistance" "of Reveling" "of Revitalization" "of Revoking" "of Rime" "of Ruin" "of Saqawal" "of Shelter" "of Shocking" "of Skill" "of Snuffing" "of Sortilege" "of Spellcraft" "of Spirit" "of Splintering" "of Stifling" "of Suturing" "of Tacati" "of Talent" "of Taunting" "of Training" "of Tzteosh" "of Unholy Might" "of Unmaking" "of Vampirism" "of Variegation" "of Vivification" "of Voltage" "of Weaponcraft" "of Will" "of Wounding" "of Youth" "of Zeal" "of Zealousness" "of the Assassin" "of the Bastion" "of the Blur" "of the Comet" "of the Conservator" "of the Deadeye" "of the Deathless" "of the Elements" "of the Essence" "of the Fanatical" "of the Furnace" "of the Gale" "of the Gelid" "of the Genius" "of the Gods" "of the Godslayer" "of the Hearth" "of the Ice" "of the Inferno" "of the Infinite" "of the Inquisitor" "of the Jaguar" "of the Kraken" "of the Leviathan" "of the Lightning Rod" "of the Lightning" "of the Maelstrom" "of the Magma" "of the Mammoth" "of the Marksman" "of the Multiverse" "of the Phantom" "of the Phoenix" "of the Polar Bear" "of the Polymath" "of the Protector" "of the Rainbow" "of the Ranger" "of the Sacred Grove" "of the Savant" "of the Solar Storm" "of the Span" "of the Taskmaster" "of the Tempest" "of the Titan" "of the Tourniquet" "of the Underground" "of the Universe" "of the Virtuoso" "of the Volcano" "of the Walrus" "of the Wind" "of the Zealous"
	SetFontSize 45
	SetTextColor 61 217 15 255
	SetBorderColor 61 217 15 255
	SetBackgroundColor 255 255 255 255 # White BG
	MinimapIcon 0 White Circle

"""


hide_jew_gem_amul_belt_ring = """
#============================================================================================================
# Hide unwanted
#============================================================================================================

# Filtered items by base type instead of class.
# It makes easier to spot new items, and filter out low qual bases while keeping good ones.

Hide
	Rarity Magic
	Class == "Jewel"
	Quality = 0
	SetFontSize 30
	# SetBackgroundColor 20 90 0 180
	DisableDropSound True

Hide
	Class == "Skill Gems" "Support Gems"
	TransfiguredGem False
	Quality = 0
	GemLevel < 15
	SetFontSize 30
	DisableDropSound True

#
# # Class == "Amulets" "Belts" "Body Armours" "Boots" "Bows" "Claws" "Daggers" "Gloves" "Helmets" "One Hand Axes" "One Hand Maces" "One Hand Swords" "Quivers" "Rings" "Rune Daggers" "Sceptres" "Shields" "Staves" "Thrusting One Hand Swords" "Two Hand Axes" "Two Hand Maces" "Two Hand Swords" "Wands" "Warstaves"
#

# ------ Amulets ------  Class == "Amulets"

# UNFILTERED: "Unset Amulet" " "Focused Amulet" "Simplex Amulet" "Astrolabe Amulet" "Marble Amulet" "Seaglass Amulet" "Blue Pearl Amulet"

Hide
	Rarity Normal
	Class == "Amulets"
	BaseType == "Coral Amulet" "Paua Amulet" "Amber Amulet" "Jade Amulet" "Lapis Amulet" "Gold Amulet" "Agate Amulet" "Citrine Amulet" "Turquoise Amulet" "Onyx Amulet"
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Magic
	AnyEnchantment False
	FracturedItem False
	HasCruciblePassiveTree False
	Identified False
	SynthesisedItem False
	Class == "Amulets"
	BaseType == "Coral Amulet" "Paua Amulet" "Amber Amulet" "Jade Amulet" "Lapis Amulet" "Gold Amulet" "Agate Amulet" "Citrine Amulet" "Turquoise Amulet" "Onyx Amulet"
	SetFontSize 30
	DisableDropSound True

# ------ Belts ------  Class == "Belts"

# UNFILTERED: "Stygian Vise" "Micro-Distillery Belt" "Mechanical Belt" "Vanguard Belt" "Crystal Belt

Hide
	Rarity Rare
	AnyEnchantment False
	Corrupted False
	FracturedItem False
	HasCruciblePassiveTree False
	Identified False
	Mirrored False
	SynthesisedItem False
	Class == "Belts"
	BaseType == "Chain Belt" "Rustic Sash" "Heavy Belt" "Leather Belt" "Cloth Belt" "Studded Belt"
	ItemLevel <= 85
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Rare
	Corrupted True
	AnyEnchantment False
	FracturedItem False
	HasCruciblePassiveTree False
	Identified False
	Mirrored False
	SynthesisedItem False
	Class == "Belts"
	BaseType == "Chain Belt" "Rustic Sash" "Heavy Belt" "Leather Belt" "Cloth Belt" "Studded Belt"
	ItemLevel < 70

Hide
	Rarity Magic
	AnyEnchantment False
	FracturedItem False
	HasCruciblePassiveTree False
	SynthesisedItem False
	Class == "Belts"
	BaseType == "Chain Belt" "Rustic Sash" "Heavy Belt" "Leather Belt" "Cloth Belt" "Studded Belt"
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Normal
	Class == "Belts"
	BaseType == "Chain Belt" "Rustic Sash" "Heavy Belt" "Leather Belt" "Cloth Belt" "Studded Belt"
	SetFontSize 30
	DisableDropSound True

# ------ Rings ------  Class == "Rings"

# ALL
# "Breach Ring" "Coral Ring" "Iron Ring" "Paua Ring" "Unset Ring" "Sapphire Ring" "Topaz Ring" "Ruby Ring" "Diamond Ring" "Gold Ring" "Moonstone Ring" "Two-Stone Ring" "Cogwork Ring" "Composite Ring" "Dusk Ring" "Geodesic Ring" "Gloam Ring" "Helical Ring" "Manifold Ring" "Nameless Ring" "Penumbra Ring" "Ratcheting Ring" "Shadowed Ring" "Tenebrous Ring" "Bone Ring" "Amethyst Ring" "Prismatic Ring" "Cerulean Ring" "Iolite Ring" "Opal Ring" "Steel Ring" "Vermillion Ring"


Hide
	Rarity Normal
	Class == "Rings"
	BaseType == "Coral Ring" "Iron Ring" "Paua Ring" "Unset Ring" "Sapphire Ring" "Topaz Ring" "Ruby Ring" "Diamond Ring" "Gold Ring" "Moonstone Ring" "Two-Stone Ring" "Bone Ring" "Amethyst Ring" "Prismatic Ring"
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Magic
	AnyEnchantment False
	FracturedItem False
	HasCruciblePassiveTree False
	Identified False
	SynthesisedItem False
	Class == "Rings"
	BaseType == "Coral Ring" "Iron Ring" "Paua Ring" "Unset Ring" "Sapphire Ring" "Topaz Ring" "Ruby Ring" "Diamond Ring" "Gold Ring" "Moonstone Ring" "Two-Stone Ring" "Bone Ring" "Amethyst Ring" "Prismatic Ring"
	SetFontSize 30
	DisableDropSound True
	
"""

# Body Armours 
hide_barm = '''"Plate Vest" "Chestplate" "Copper Plate" "War Plate" "Full Plate" "Arena Plate" "Lordly Plate" "Bronze Plate" "Battle Plate" "Sun Plate" "Colosseum Plate" "Majestic Plate" "Golden Plate" "Crusader Plate" "Astral Plate" "Gladiator Plate" "Glorious Plate" "Titan Plate" "Legion Plate" "Shabby Jerkin" "Strapped Leather" "Buckskin Tunic" "Wild Leather" "Full Leather" "Sun Leather" "Thief's Garb" "Eelskin Tunic" "Frontier Leather" "Glorious Leather" "Coronal Leather" "Cutthroat's Garb" "Sharkskin Tunic" "Destiny Leather" "Exquisite Leather" "Zodiac Leather" "Assassin's Garb" "Supreme Leather" "Astral Leather" "Simple Robe" "Silken Vest" "Scholar's Robe" "Silken Garb" "Mage's Vestment" "Silk Robe" "Cabalist Regalia" "Sage's Robe" "Silken Wrap" "Conjurer's Vestment" "Spidersilk Robe" "Destroyer Regalia" "Savant's Robe" "Necromancer Silks" "Occultist's Vestment" "Widowsilk Robe" "Vaal Regalia" "Arcane Vestment" "Nightweave Robe" "Scale Vest" "Light Brigandine" "Scale Doublet" "Infantry Brigandine" "Full Scale Armour" "Soldier's Brigandine" "Field Lamellar" "Wyrmscale Doublet" "Hussar Brigandine" "Full Wyrmscale" "Commander's Brigandine" "Battle Lamellar" "Dragonscale Doublet" "Desert Brigandine" "Full Dragonscale" "General's Brigandine" "Triumphant Lamellar" "Full Wyvernscale" "Marshall's Brigandine" "Chainmail Vest" "Chainmail Tunic" "Ringmail Coat" "Chainmail Doublet" "Full Ringmail" "Full Chainmail" "Holy Chainmail" "Latticed Ringmail" "Crusader Chainmail" "Ornate Ringmail" "Chain Hauberk" "Devout Chainmail" "Loricated Ringmail" "Conquest Chainmail" "Elegant Ringmail" "Saint's Hauberk" "Saintly Chainmail" "Grand Ringmail" "Paladin's Hauberk" "Padded Vest" "Oiled Vest" "Padded Jacket" "Oiled Coat" "Scarlet Raiment" "Waxed Garb" "Bone Armour" "Quilted Jacket" "Sleek Coat" "Crimson Raiment" "Lacquered Garb" "Crypt Armour" "Sentinel Jacket" "Varnished Coat" "Blood Raiment" "Sadist Garb" "Carnal Armour" "Sanguine Raiment" "Torturer Garb"'''
# Boots
hide_boots = ''' "Iron Greaves" "Steel Greaves" "Plated Greaves" "Reinforced Greaves" "Antique Greaves" "Ancient Greaves" "Goliath Greaves" "Vaal Greaves" "Titan Greaves" "Precursor Greaves" "Rawhide Boots" "Goathide Boots" "Deerskin Boots" "Nubuck Boots" "Eelskin Boots" "Sharkskin Boots" "Shagreen Boots" "Stealth Boots" "Slink Boots" "Harpyskin Boots" "Wool Shoes" "Velvet Slippers" "Silk Slippers" "Scholar Boots" "Satin Slippers" "Samite Slippers" "Conjurer Boots" "Arcanist Slippers" "Sorcerer Boots" "Sage Slippers" "Leatherscale Boots" "Ironscale Boots" "Bronzescale Boots" "Steelscale Boots" "Serpentscale Boots" "Wyrmscale Boots" "Hydrascale Boots" "Dragonscale Boots" "Chimerascale Boots" "Chain Boots" "Ringmail Boots" "Mesh Boots" "Riveted Boots" "Zealot Boots" "Soldier Boots" "Legion Boots" "Crusader Boots" "Martyr Boots" "Wrapped Boots" "Strapped Boots" "Clasped Boots" "Shackled Boots" "Trapper Boots" "Ambush Boots" "Carnal Boots" "Assassin's Boots" "Murder Boots" "Infiltrator Boots"'''
# Gloves
hide_gloves = ''' "Iron Gauntlets" "Plated Gauntlets" "Bronze Gauntlets" "Steel Gauntlets" "Antique Gauntlets" "Ancient Gauntlets" "Goliath Gauntlets" "Vaal Gauntlets" "Titan Gauntlets" "Precursor Gauntlets" "Rawhide Gloves" "Goathide Gloves" "Deerskin Gloves" "Nubuck Gloves" "Eelskin Gloves" "Sharkskin Gloves" "Shagreen Gloves" "Stealth Gloves" "Slink Gloves" "Harpyskin Gloves" "Wool Gloves" "Velvet Gloves" "Silk Gloves" "Embroidered Gloves" "Satin Gloves" "Samite Gloves" "Conjurer Gloves" "Arcanist Gloves" "Sorcerer Gloves" "Sage Gloves" "Fishscale Gauntlets" "Ironscale Gauntlets" "Bronzescale Gauntlets" "Steelscale Gauntlets" "Serpentscale Gauntlets" "Wyrmscale Gauntlets" "Hydrascale Gauntlets" "Dragonscale Gauntlets" "Chimerascale Gauntlets" "Chain Gloves" "Ringmail Gloves" "Mesh Gloves" "Riveted Gloves" "Zealot Gloves" "Soldier Gloves" "Legion Gloves" "Crusader Gloves" "Martyr Gloves" "Wrapped Mitts" "Strapped Mitts" "Clasped Mitts" "Trapper Mitts" "Ambush Mitts" "Carnal Mitts" "Assassin's Mitts" "Murder Mitts" "Infiltrator Mitts"'''
# Helmets
hide_helmets = ''' "Iron Hat" "Cone Helmet" "Barbute Helmet" "Close Helmet" "Gladiator Helmet" "Reaver Helmet" "Siege Helmet" "Samnite Helmet" "Ezomyte Burgonet" "Royal Burgonet" "Eternal Burgonet" "General's Helmet" "Conqueror's Helmet" "Leather Cap" "Tricorne" "Leather Hood" "Wolf Pelt" "Hunter Hood" "Noble Tricorne" "Ursine Pelt" "Silken Hood" "Sinner Tricorne" "Lion Pelt" "Dire Pelt" "Grizzly Pelt" "Vine Circlet" "Iron Circlet" "Torture Cage" "Tribal Circlet" "Bone Circlet" "Lunaris Circlet" "Steel Circlet" "Necromancer Circlet" "Solaris Circlet" "Mind Cage" "Hubris Circlet" "Moonlit Circlet" "Sunfire Circlet" "Battered Helm" "Sallet" "Visored Sallet" "Gilded Sallet" "Secutor Helm" "Fencer Helm" "Lacquered Helmet" "Fluted Bascinet" "Pig-Faced Bascinet" "Nightmare Bascinet" "Knight Helm" "Conquest Helmet" "Rusted Coif" "Soldier Helmet" "Great Helmet" "Crusader Helmet" "Aventail Helmet" "Zealot Helmet" "Great Crown" "Magistrate Crown" "Prophet Crown" "Praetor Crown" "Faithful Helmet" "Paladin Crown" "Scare Mask" "Plague Mask" "Iron Mask" "Festival Mask" "Golden Mask" "Raven Mask" "Callous Mask" "Regicide Mask" "Harlequin Mask" "Vaal Mask" "Deicide Mask" "Jester Mask" "Ancient Mask"'''
# Shieldds
hide_shields = ''' "Splintered Tower Shield" "Corroded Tower Shield" "Rawhide Tower Shield" "Cedar Tower Shield" "Copper Tower Shield" "Reinforced Tower Shield" "Painted Tower Shield" "Buckskin Tower Shield" "Mahogany Tower Shield" "Bronze Tower Shield" "Girded Tower Shield" "Crested Tower Shield" "Shagreen Tower Shield" "Ebony Tower Shield" "Goathide Buckler" "Pine Buckler" "Painted Buckler" "Hammered Buckler" "War Buckler" "Gilded Buckler" "Oak Buckler" "Enameled Buckler" "Corrugated Buckler" "Battle Buckler" "Golden Buckler" "Ironwood Buckler" "Vaal Buckler" "Twig Spirit Shield" "Yew Spirit Shield" "Bone Spirit Shield" "Tarnished Spirit Shield" "Jingling Spirit Shield" "Brass Spirit Shield" "Walnut Spirit Shield" "Ivory Spirit Shield" "Ancient Spirit Shield" "Chiming Spirit Shield" "Thorium Spirit Shield" "Lacewood Spirit Shield" "Vaal Spirit Shield" "Rotted Round Shield" "Fir Round Shield" "Studded Round Shield" "Scarlet Round Shield" "Splendid Round Shield" "Maple Round Shield" "Spiked Round Shield" "Crimson Round Shield" "Baroque Round Shield" "Teak Round Shield" "Spiny Round Shield" "Plank Kite Shield" "Linden Kite Shield" "Reinforced Kite Shield" "Layered Kite Shield" "Ceremonial Kite Shield" "Etched Kite Shield" "Steel Kite Shield" "Laminated Kite Shield" "Angelic Kite Shield" "Branded Kite Shield" "Mosaic Kite Shield" "Spiked Bundle" "Driftwood Spiked Shield" "Alloyed Spiked Shield" "Burnished Spiked Shield" "Ornate Spiked Shield" "Redwood Spiked Shield" "Compound Spiked Shield" "Polished Spiked Shield" "Sovereign Spiked Shield" "Alder Spiked Shield" "Ezomyte Spiked Shield" "Mirrored Spiked Shield"'''

hide_armour = f"""
# ------ Body Armours ------  Class == "Body Armours"

# ALL
# "Plate Vest" "Chestplate" "Copper Plate" "War Plate" "Full Plate" "Arena Plate" "Lordly Plate" "Bronze Plate" "Battle Plate" "Sun Plate" "Colosseum Plate" "Majestic Plate" "Golden Plate" "Crusader Plate" "Astral Plate" "Gladiator Plate" "Glorious Plate" "Titan Plate" "Legion Plate" "Royal Plate"
# "Shabby Jerkin" "Strapped Leather" "Buckskin Tunic" "Wild Leather" "Full Leather" "Sun Leather" "Thief's Garb" "Eelskin Tunic" "Frontier Leather" "Glorious Leather" "Coronal Leather" "Cutthroat's Garb" "Sharkskin Tunic" "Destiny Leather" "Exquisite Leather" "Zodiac Leather" "Assassin's Garb" "Supreme Leather" "Astral Leather" "Syndicate's Garb"
# "Simple Robe" "Silken Vest" "Scholar's Robe" "Silken Garb" "Mage's Vestment" "Silk Robe" "Cabalist Regalia" "Sage's Robe" "Silken Wrap" "Conjurer's Vestment" "Spidersilk Robe" "Destroyer Regalia" "Savant's Robe" "Necromancer Silks" "Occultist's Vestment" "Widowsilk Robe" "Vaal Regalia" "Arcane Vestment" "Nightweave Robe" "Twilight Regalia"
# "Scale Vest" "Light Brigandine" "Scale Doublet" "Infantry Brigandine" "Full Scale Armour" "Soldier's Brigandine" "Field Lamellar" "Wyrmscale Doublet" "Hussar Brigandine" "Full Wyrmscale" "Commander's Brigandine" "Battle Lamellar" "Dragonscale Doublet" "Desert Brigandine" "Full Dragonscale" "General's Brigandine" "Triumphant Lamellar" "Full Wyvernscale" "Marshall's Brigandine" "Conquest Lamellar"
# "Chainmail Vest" "Chainmail Tunic" "Ringmail Coat" "Chainmail Doublet" "Full Ringmail" "Full Chainmail" "Holy Chainmail" "Latticed Ringmail" "Crusader Chainmail" "Ornate Ringmail" "Chain Hauberk" "Devout Chainmail" "Loricated Ringmail" "Conquest Chainmail" "Elegant Ringmail" "Saint's Hauberk" "Saintly Chainmail" "Grand Ringmail" "Paladin's Hauberk" "Sacred Chainmail"
# "Padded Vest" "Oiled Vest" "Padded Jacket" "Oiled Coat" "Scarlet Raiment" "Waxed Garb" "Bone Armour" "Quilted Jacket" "Sleek Coat" "Crimson Raiment" "Lacquered Garb" "Crypt Armour" "Sentinel Jacket" "Varnished Coat" "Blood Raiment" "Sadist Garb" "Carnal Armour" "Sanguine Raiment" "Torturer Garb" "Necrotic Armour"
# "Grasping Mail" "Sacrificial Garb"

# ------ Boots ------  Class == "Boots"

# ALL
# "Basemetal Treads" "Darksteel Treads" "Brimstone Treads" "Cloudwhisper Boots" "Windbreak Boots" "Stormrider Boots" "Duskwalk Slippers" "Nightwind Slippers" "Dreamquest Slippers" "Two-Toned Boots" "Fugitive Boots" "Runic Greaves" "Runic Sollerets" "Runic Sabatons"
# "Iron Greaves" "Steel Greaves" "Plated Greaves" "Reinforced Greaves" "Antique Greaves" "Ancient Greaves" "Goliath Greaves" "Vaal Greaves" "Titan Greaves" "Precursor Greaves" "Leviathan Greaves"
# "Rawhide Boots" "Goathide Boots" "Deerskin Boots" "Nubuck Boots" "Eelskin Boots" "Sharkskin Boots" "Shagreen Boots" "Stealth Boots" "Slink Boots" "Harpyskin Boots" "Velour Boots"
# "Wool Shoes" "Velvet Slippers" "Silk Slippers" "Scholar Boots" "Satin Slippers" "Samite Slippers" "Conjurer Boots" "Arcanist Slippers" "Sorcerer Boots" "Sage Slippers" "Warlock Boots"
# "Leatherscale Boots" "Ironscale Boots" "Bronzescale Boots" "Steelscale Boots" "Serpentscale Boots" "Wyrmscale Boots" "Hydrascale Boots" "Dragonscale Boots" "Chimerascale Boots" "Wyvernscale Boots"
# "Chain Boots" "Ringmail Boots" "Mesh Boots" "Riveted Boots" "Zealot Boots" "Soldier Boots" "Legion Boots" "Crusader Boots" "Martyr Boots" "Paladin Boots"
# "Wrapped Boots" "Strapped Boots" "Clasped Boots" "Shackled Boots" "Trapper Boots" "Ambush Boots" "Carnal Boots" "Assassin's Boots" "Murder Boots" "Infiltrator Boots" "Phantom Boots"

# ------ Gloves ------  Class == "Gloves"

# ALL
# "Iron Gauntlets" "Plated Gauntlets" "Preserving Gauntlets" "Bronze Gauntlets" "Steel Gauntlets" "Antique Gauntlets" "Guarding Gauntlets" "Ancient Gauntlets" "Goliath Gauntlets" "Vaal Gauntlets" "Titan Gauntlets" "Spiked Gloves" "Thwarting Gauntlets" "Precursor Gauntlets" "Leviathan Gauntlets"
# "Rawhide Gloves" "Goathide Gloves" "Tinker Gloves" "Deerskin Gloves" "Nubuck Gloves" "Eelskin Gloves" "Apprentice Gloves" "Sharkskin Gloves" "Shagreen Gloves" "Stealth Gloves" "Gripped Gloves" "Slink Gloves" "Trapsetter Gloves" "Harpyskin Gloves" "Velour Gloves"
# "Wool Gloves" "Leyline Gloves" "Velvet Gloves" "Silk Gloves" "Embroidered Gloves" "Aetherwind Gloves" "Satin Gloves" "Samite Gloves" "Conjurer Gloves" "Arcanist Gloves" "Sorcerer Gloves" "Fingerless Silk Gloves" "Nexus Gloves" "Sage Gloves" "Warlock Gloves"
# "Fishscale Gauntlets" "Ironscale Gauntlets" "Bronzescale Gauntlets" "Steelscale Gauntlets" "Serpentscale Gauntlets" "Wyrmscale Gauntlets" "Hydrascale Gauntlets" "Dragonscale Gauntlets" "Chimerascale Gauntlets" "Wyvernscale Gauntlets"
# "Chain Gloves" "Ringmail Gloves" "Mesh Gloves" "Riveted Gloves" "Zealot Gloves" "Soldier Gloves" "Legion Gloves" "Crusader Gloves" "Apothecary's Gloves" "Martyr Gloves" "Paladin Gloves"
# "Wrapped Mitts" "Strapped Mitts" "Clasped Mitts" "Trapper Mitts" "Ambush Mitts" "Carnal Mitts" "Assassin's Mitts" "Murder Mitts" "Infiltrator Mitts" "Phantom Mitts"
# "Runic Gloves" "Runic Gages" "Runic Gauntlets" "

# ------ Helmets ------  Class == "Helmets"

# ALL
# "Iron Hat" "Cone Helmet" "Barbute Helmet" "Close Helmet" "Gladiator Helmet" "Reaver Helmet" "Siege Helmet" "Samnite Helmet" "Ezomyte Burgonet" "Royal Burgonet" "Eternal Burgonet" "General's Helmet" "Conqueror's Helmet" "Giantslayer Helmet"
# "Leather Cap" "Tricorne" "Leather Hood" "Wolf Pelt" "Hunter Hood" "Noble Tricorne" "Ursine Pelt" "Silken Hood" "Sinner Tricorne" "Lion Pelt" "Dire Pelt" "Grizzly Pelt" "Majestic Pelt"
# "Vine Circlet" "Iron Circlet" "Torture Cage" "Tribal Circlet" "Bone Circlet" "Lunaris Circlet" "Steel Circlet" "Necromancer Circlet" "Solaris Circlet" "Mind Cage" "Hubris Circlet" "Moonlit Circlet" "Sunfire Circlet" "Lich's Circlet"
# "Battered Helm" "Sallet" "Sorrow Mask" "Visored Sallet" "Gilded Sallet" "Secutor Helm" "Fencer Helm" "Atonement Mask" "Lacquered Helmet" "Fluted Bascinet" "Pig-Faced Bascinet" "Nightmare Bascinet" "Knight Helm" "Penitent Mask" "Conquest Helmet" "Haunted Bascinet"
# "Rusted Coif" "Soldier Helmet" "Imp Crown" "Great Helmet" "Crusader Helmet" "Aventail Helmet" "Zealot Helmet" "Demon Crown" "Great Crown" "Magistrate Crown" "Prophet Crown" "Praetor Crown" "Bone Helmet" "Faithful Helmet" "Archdemon Crown" "Paladin Crown" "Divine Crown"
# "Scare Mask" "Plague Mask" "Gale Crown" "Iron Mask" "Festival Mask" "Golden Mask" "Raven Mask" "Callous Mask" "Winter Crown" "Regicide Mask" "Harlequin Mask" "Vaal Mask" "Deicide Mask" "Jester Mask" "Blizzard Crown" "Ancient Mask" "Torturer's Mask"
# "Runic Helm" "Runic Crest" "Runic Crown"

# ------ Shields ------  Class == "Shields"

# ALL
# "Splintered Tower Shield" "Corroded Tower Shield" "Rawhide Tower Shield" "Cedar Tower Shield" "Copper Tower Shield" "Reinforced Tower Shield" "Painted Tower Shield" "Buckskin Tower Shield" "Mahogany Tower Shield" "Bronze Tower Shield" "Magmatic Tower Shield" "Girded Tower Shield" "Crested Tower Shield" "Shagreen Tower Shield" "Ebony Tower Shield" "Ezomyte Tower Shield" "Colossal Tower Shield" "Heat-attuned Tower Shield" "Pinnacle Tower Shield"
# Goathide Buckler" "Pine Buckler" "Painted Buckler" "Hammered Buckler" "War Buckler" "Gilded Buckler" "Oak Buckler" "Enameled Buckler" "Corrugated Buckler" "Battle Buckler" "Polar Buckler" "Golden Buckler" "Ironwood Buckler" "Lacquered Buckler" "Vaal Buckler" "Crusader Buckler" "Imperial Buckler" "Cold-attuned Buckler"
# "Twig Spirit Shield" "Yew Spirit Shield" "Bone Spirit Shield" "Tarnished Spirit Shield" "Jingling Spirit Shield" "Brass Spirit Shield" "Walnut Spirit Shield" "Ivory Spirit Shield" "Ancient Spirit Shield" "Chiming Spirit Shield" "Subsuming Spirit Shield" "Thorium Spirit Shield" "Lacewood Spirit Shield" "Fossilised Spirit Shield" "Vaal Spirit Shield" "Harmonic Spirit Shield" "Titanium Spirit Shield" "Transfer-attuned Spirit Shield"
# "Rotted Round Shield" "Fir Round Shield" "Studded Round Shield" "Scarlet Round Shield" "Splendid Round Shield" "Maple Round Shield" "Spiked Round Shield" "Crimson Round Shield" "Baroque Round Shield" "Teak Round Shield" "Spiny Round Shield" "Cardinal Round Shield" "Elegant Round Shield"
# "Plank Kite Shield" "Linden Kite Shield" "Reinforced Kite Shield" "Layered Kite Shield" "Ceremonial Kite Shield" "Etched Kite Shield" "Steel Kite Shield" "Laminated Kite Shield" "Angelic Kite Shield" "Branded Kite Shield" "Champion Kite Shield" "Mosaic Kite Shield" "Archon Kite Shield"
# "Spiked Bundle" "Driftwood Spiked Shield" "Alloyed Spiked Shield" "Burnished Spiked Shield" "Ornate Spiked Shield" "Redwood Spiked Shield" "Compound Spiked Shield" "Polished Spiked Shield" "Sovereign Spiked Shield" "Alder Spiked Shield" "Ezomyte Spiked Shield" "Mirrored Spiked Shield" "Supreme Spiked Shield"

Hide
	Rarity Rare
	AnyEnchantment False
	Corrupted False
	FracturedItem False
	HasCruciblePassiveTree False
	Identified False
	Mirrored False
	SynthesisedItem False
	BaseType == {hide_barm + hide_boots + hide_gloves + hide_helmets + hide_shields}
	ItemLevel <= 85
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Rare
	Corrupted True
	AnyEnchantment False
	FracturedItem False
	HasCruciblePassiveTree False
	Identified False
	Mirrored False
	SynthesisedItem False
	BaseType == {hide_barm + hide_boots + hide_gloves + hide_helmets + hide_shields}
	ItemLevel < 70

 Hide
	Rarity Magic
	AnyEnchantment False
	FracturedItem False
	HasCruciblePassiveTree False
	SynthesisedItem False
	Identified False
	Class == "Gloves"
	BaseType == {hide_gloves}
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Magic
	AnyEnchantment False
	FracturedItem False
	HasCruciblePassiveTree False
	SynthesisedItem False
	BaseType == {hide_barm + hide_boots + hide_helmets + hide_shields}
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Normal
	BaseType == {hide_barm + hide_boots + hide_gloves + hide_helmets + hide_shields}
	SetFontSize 30
	DisableDropSound True

"""

# Bows
hide_bows = '''"Crude Bow" "Short Bow" "Long Bow" "Composite Bow" "Recurve Bow" "Bone Bow" "Royal Bow" "Death Bow" "Grove Bow" "Reflex Bow" "Decurve Bow" "Compound Bow" "Sniper Bow" "Ivory Bow" "Highborn Bow" "Decimation Bow" "Thicket Bow" "Citadel Bow" "Spine Bow"'''
# Claws
hide_claws = ''' "Nailed Fist" "Sharktooth Claw" "Awl" "Cat's Paw" "Blinder" "Timeworn Claw" "Sparkling Claw" "Fright Claw" "Double Claw" "Thresher Claw" "Gouger" "Tiger's Paw" "Gut Ripper" "Prehistoric Claw" "Noble Claw" "Eagle Claw" "Twin Claw" "Great White Claw" "Throat Stabber" "Hellion's Paw" "Terror Claw"'''
# Daggers
hide_daggers = ''' "Glass Shank" "Skinning Knife" "Stiletto" "Flaying Knife" "Prong Dagger" "Poignard" "Trisula" "Gutting Knife"'''
# One Hand Axes
hide_ohaxes = ''' "Rusted Hatchet" "Jade Hatchet" "Boarding Axe" "Cleaver" "Broad Axe" "Arming Axe" "Decorative Axe" "Spectral Axe" "Etched Hatchet" "Jasper Axe" "Tomahawk" "Wrist Chopper" "War Axe" "Chest Splitter" "Ceremonial Axe" "Wraith Axe" "Engraved Hatchet" "Karui Axe" "Siege Axe" "Reaver Axe" "Butcher Axe" "Vaal Hatchet" "Infernal Axe"'''
# One Hand Maces
hide_ohmaces = ''' "Driftwood Club" "Tribal Club" "Spiked Club" "Stone Hammer" "War Hammer" "Bladed Mace" "Ceremonial Mace" "Dream Mace" "Wyrm Mace" "Petrified Club" "Barbed Club" "Rock Breaker" "Battle Hammer" "Flanged Mace" "Ornate Mace" "Phantom Mace" "Dragon Mace" "Ancestral Club" "Tenderizer" "Legion Hammer" "Pernach" "Auric Mace" "Nightmare Mace"'''
# One Hand Swords
hide_ohswords = ''' "Rusted Sword" "Charan's Sword" "Copper Sword" "Sabre" "Broad Sword" "War Sword" "Ancient Sword" "Elegant Sword" "Dusk Blade" "Hook Sword" "Variscite Blade" "Cutlass" "Baselard" "Battle Sword" "Elder Sword" "Graceful Sword" "Twilight Blade" "Corsair Sword" "Gemstone Sword" "Grappler" "Eternal Sword" "Gladius"'''
# Quivers
hide_quivers = ''' "Serrated Arrow Quiver" "Fire Arrow Quiver" "Sharktooth Arrow Quiver" "Feathered Arrow Quiver" "Penetrating Arrow Quiver" "Spike-Point Arrow Quiver" "Blunt Arrow Quiver" "Two-Point Arrow Quiver" "Blazing Arrow Quiver" "Ornate Quiver" "Broadhead Arrow Quiver" "Vile Arrow Quiver" "Heavy Arrow Quiver"'''
# Rune Daggers
hide_rdaggers = ''' "Carving Knife" "Boot Knife" "Copper Kris" "Skean" "Imp Dagger" "Butcher Knife" "Boot Blade" "Golden Kris" "Royal Skean" "Fiend Dagger" "Slaughter Knife" "Ezomyte Dagger" "Imperial Skean"'''
# Sceptres
hide_scepters = ''' "Driftwood Sceptre" "Darkwood Sceptre" "Bronze Sceptre" "Quartz Sceptre" "Iron Sceptre" "Ochre Sceptre" "Ritual Sceptre" "Shadow Sceptre" "Grinning Fetish" "Horned Sceptre" "Sekhem" "Crystal Sceptre" "Lead Sceptre" "Blood Sceptre" "Royal Sceptre" "Abyssal Sceptre" "Stag Sceptre" "Karui Sceptre" "Tyrant's Sekhem" "Platinum Sceptre" "Vaal Sceptre" "Carnal Sceptre"'''
#  Staves
hide_staves = ''' "Gnarled Branch" "Primitive Staff" "Long Staff" "Royal Staff" "Crescent Staff" "Woodful Staff" "Quarterstaff" "Highborn Staff" "Moon Staff" "Primordial Staff" "Lathi"'''
# Thrusting One Hand Swords
hide_tohswords = ''' "Rusted Spike" "Whalebone Rapier" "Battered Foil" "Basket Rapier" "Jagged Foil" "Antique Rapier" "Elegant Foil" "Thorn Rapier" "Smallsword" "Wyrmbone Rapier" "Burnished Foil" "Estoc" "Serrated Foil" "Primeval Rapier" "Fancy Foil" "Apex Rapier" "Courtesan Sword" "Dragonbone Rapier" "Tempered Foil" "Pecoraro" "Spiraled Foil" "Vaal Rapier" "Jewelled Foil"'''
# Two Hand Axes
hide_thaxes = ''' "Stone Axe" "Jade Chopper" "Woodsplitter" "Poleaxe" "Double Axe" "Gilded Axe" "Shadow Axe" "Dagger Axe" "Jasper Chopper" "Timber Axe" "Headsman Axe" "Labrys" "Noble Axe" "Abyssal Axe" "Talon Axe" "Ezomyte Axe" "Despot Axe"'''
# Two Hand Maces
hide_thmaces = ''' "Driftwood Maul" "Tribal Maul" "Mallet" "Sledgehammer" "Jagged Maul" "Brass Maul" "Fright Maul" "Morning Star" "Totemic Maul" "Great Mallet" "Steelhead" "Spiny Maul" "Plated Maul" "Dread Maul" "Solar Maul" "Karui Maul" "Colossus Mallet" "Piledriver" "Meatgrinder"'''
# Two Hand Swords
hide_thswords = ''' "Corroded Blade" "Longsword" "Bastard Sword" "Two-Handed Sword" "Etched Greatsword" "Ornate Sword" "Spectral Sword" "Curved Blade" "Butcher Sword" "Footman Sword" "Highland Blade" "Engraved Greatsword" "Tiger Sword" "Wraith Sword" "Lithe Blade" "Headman's Sword"'''
# Wands
hide_wands = ''' "Driftwood Wand" "Goat's Horn" "Carved Wand" "Quartz Wand" "Calling Wand" "Spiraled Wand" "Sage Wand" "Pagan Wand" "Faun's Horn" "Engraved Wand" "Crystal Wand" "Coiled Wand" "Convening Wand" "Heathen Wand" "Demon's Horn" "Imbued Wand" "Opal Wand" "Tornado Wand"'''
# Warstaves
hide_warstaves = ''' "Iron Staff" "Coiled Staff" "Vile Staff" "Military Staff" "Serpentine Staff" "Foul Staff" "Ezomyte Staff"'''
	


hide_weapons = f"""
# ------ Bows ------  Class == "Bows"

# ALL
# "Crude Bow" "Short Bow" "Long Bow" "Composite Bow" "Recurve Bow" "Bone Bow" "Royal Bow" "Death Bow" "Grove Bow" "Reflex Bow" "Decurve Bow" "Compound Bow" "Sniper Bow" "Ivory Bow" "Foundry Bow" "Highborn Bow" "Decimation Bow" "Thicket Bow" "Steelwood Bow" "Citadel Bow" "Ranger Bow" "Assassin Bow" "Spine Bow" "Imperial Bow" "Harbinger Bow" "Solarine Bow" "Maraketh Bow"

# ------ Claws ------  Class == "Claws"

# ALL
# "Nailed Fist" "Sharktooth Claw" "Awl" "Cat's Paw" "Blinder" "Timeworn Claw" "Sparkling Claw" "Fright Claw" "Double Claw" "Thresher Claw" "Gouger" "Tiger's Paw" "Gut Ripper" "Prehistoric Claw" "Malign Fangs" "Noble Claw" "Eagle Claw" "Twin Claw" "Great White Claw" "Throat Stabber" "Hellion's Paw" "Eye Gouger" "Vaal Claw" "Imperial Claw" "Terror Claw" "Void Fangs" "Gemini Claw"

# ------ Daggers ------  Class == "Daggers"

# ALL
# "Glass Shank" "Skinning Knife" "Stiletto" "Flaying Knife" "Prong Dagger" "Poignard" "Pressurised Dagger" "Trisula" "Gutting Knife" "Ambusher" "Pneumatic Dagger" "Sai"

# ------ One Hand Axes ------  Class == "One Hand Axes"

# ALL
# "Rusted Hatchet" "Jade Hatchet" "Boarding Axe" "Cleaver" "Broad Axe" "Arming Axe" "Decorative Axe" "Spectral Axe" "Etched Hatchet" "Jasper Axe" "Tomahawk" "Wrist Chopper" "War Axe" "Chest Splitter" "Disapprobation Axe" "Ceremonial Axe" "Wraith Axe" "Engraved Hatchet" "Karui Axe" "Siege Axe" "Reaver Axe" "Butcher Axe" "Vaal Hatchet" "Royal Axe" "Infernal Axe" "Psychotic Axe" "Runic Hatchet"
# "Jade Hatchet" "Boarding Axe" "Cleaver" "Broad Axe" "Arming Axe" "Decorative Axe" "Spectral Axe" "Etched Hatchet" "Jasper Axe" "Tomahawk" "Wrist Chopper" "War Axe" "Chest Splitter" "Disapprobation Axe" "Ceremonial Axe" "Engraved Hatchet" "Karui Axe" "Royal Axe" "Infernal Axe" "Psychotic Axe" "Runic Hatchet"

# ------ One Hand Maces ------  Class == "One Hand Maces"

# ALL
# "Driftwood Club" "Tribal Club" "Spiked Club" "Stone Hammer" "War Hammer" "Bladed Mace" "Ceremonial Mace" "Dream Mace" "Wyrm Mace" "Petrified Club" "Barbed Club" "Rock Breaker" "Battle Hammer" "Flanged Mace" "Crack Mace" "Ornate Mace" "Phantom Mace" "Dragon Mace" "Ancestral Club" "Tenderizer" "Gavel" "Legion Hammer" "Pernach" "Auric Mace" "Nightmare Mace" "Behemoth Mace" "Boom Mace"
#  "Spiked Club" "Stone Hammer" "War Hammer" "Bladed Mace" "Ceremonial Mace" "Dream Mace" "Wyrm Mace" "Petrified Club" "Barbed Club" "Rock Breaker" "Battle Hammer" "Flanged Mace" "Crack Mace" "Ornate Mace" "Dragon Mace" "Ancestral Club" "Tenderizer" "Gavel" "Legion Hammer"  "Auric Mace" "Nightmare Mace" "Behemoth Mace" "Boom Mace"

# ------ One Hand Swords ------  Class == "One Hand Swords"

# ALL
# "Rusted Sword" "Charan's Sword" "Copper Sword" "Sabre" "Broad Sword" "War Sword" "Ancient Sword" "Elegant Sword" "Dusk Blade" "Hook Sword" "Variscite Blade" "Cutlass" "Baselard" "Capricious Spiritblade" "Battle Sword" "Elder Sword" "Graceful Sword" "Twilight Blade" "Corsair Sword" "Anarchic Spiritblade" "Gemstone Sword" "Grappler" "Eternal Sword" "Tiger Hook" "Gladius" "Vaal Blade" "Midnight Blade" "Legion Sword"
# "Charan's Sword" "Sabre" "Broad Sword" "War Sword" "Ancient Sword" "Elegant Sword" "Dusk Blade" "Hook Sword" "Variscite Blade" "Cutlass" "Baselard" "Capricious Spiritblade" "Battle Sword" "Twilight Blade"  "Anarchic Spiritblade" "Grappler" "Vaal Blade" "Midnight Blade" "Legion Sword"

# ------ Quivers ------  Class == "Quivers"

# ALL
# "Serrated Arrow Quiver" "Fire Arrow Quiver" "Sharktooth Arrow Quiver" "Feathered Arrow Quiver" "Penetrating Arrow Quiver" "Blunt Arrow Quiver" "Two-Point Arrow Quiver" "Spike-Point Arrow Quiver" "Blazing Arrow Quiver" "Ornate Quiver" "Broadhead Arrow Quiver" "Vile Arrow Quiver" "Heavy Arrow Quiver" "Primal Arrow Quiver" "Artillery Quiver"

# ------ Rune Daggers ------  Class == "Rune Daggers"

# ALL
#  "Carving Knife" "Boot Knife" "Copper Kris" "Skean" "Imp Dagger" "Butcher Knife" "Boot Blade" "Golden Kris" "Flashfire Blade" "Royal Skean" "Fiend Dagger" "Slaughter Knife" "Ezomyte Dagger" "Platinum Kris" "Imperial Skean" "Demon Dagger" "Infernal Blade"
#  "Boot Knife" "Copper Kris" "Imp Dagger" "Butcher Knife" "Boot Blade" "Golden Kris" "Flashfire Blade" "Royal Skean" "Fiend Dagger"  "Platinum Kris" "Imperial Skean" "Demon Dagger" "Infernal Blade"

# ------ Sceptres ------  Class == "Sceptres"

# ALL
# "Driftwood Sceptre" "Darkwood Sceptre" "Bronze Sceptre" "Quartz Sceptre" "Iron Sceptre" "Ochre Sceptre" "Ritual Sceptre" "Oscillating Sceptre" "Shadow Sceptre" "Grinning Fetish" "Horned Sceptre" "Sekhem" "Crystal Sceptre" "Lead Sceptre" "Blood Sceptre" "Royal Sceptre" "Stabilising Sceptre" "Abyssal Sceptre" "Stag Sceptre" "Karui Sceptre" "Tyrant's Sekhem" "Opal Sceptre" "Platinum Sceptre" "Vaal Sceptre" "Carnal Sceptre" "Void Sceptre" "Alternating Sceptre" "Sambar Sceptre"
# "Darkwood Sceptre" "Bronze Sceptre" "Quartz Sceptre" "Iron Sceptre" "Ochre Sceptre" "Ritual Sceptre" "Oscillating Sceptre" "Shadow Sceptre" "Grinning Fetish" "Horned Sceptre" "Sekhem" "Crystal Sceptre" "Lead Sceptre" "Blood Sceptre" "Stabilising Sceptre" "Abyssal Sceptre" "Stag Sceptre"  "Tyrant's Sekhem" "Platinum Sceptre" "Vaal Sceptre" "Carnal Sceptre" "Void Sceptre" "Alternating Sceptre" "Sambar Sceptre"

# ------ Staves ------  Class == "Staves"

# ALL
# "Gnarled Branch" "Primitive Staff" "Long Staff" "Royal Staff" "Crescent Staff" "Woodful Staff" "Quarterstaff" "Reciprocation Staff" "Highborn Staff" "Moon Staff" "Primordial Staff" "Lathi" "Imperial Staff" "Battery Staff" "Eclipse Staff"
#	"Reciprocation Staff" "Battery Staff" "Eclipse Staff" "Imperial Staff"

# ------ Thrusting One Hand Swords ------  Class == "Thrusting One Hand Swords"

# ALL
# "Rusted Spike" "Whalebone Rapier" "Battered Foil" "Basket Rapier" "Jagged Foil" "Antique Rapier" "Elegant Foil" "Thorn Rapier" "Smallsword" "Wyrmbone Rapier" "Burnished Foil" "Estoc" "Serrated Foil" "Primeval Rapier" "Fancy Foil" "Apex Rapier" "Courtesan Sword" "Dragonbone Rapier" "Tempered Foil" "Pecoraro" "Spiraled Foil" "Vaal Rapier" "Jewelled Foil" "Harpy Rapier" "Dragoon Sword"
# "Battered Foil" "Basket Rapier" "Jagged Foil" "Antique Rapier" "Elegant Foil" "Thorn Rapier" "Smallsword" "Wyrmbone Rapier" "Burnished Foil" "Estoc"  "Primeval Rapier" "Apex Rapier" "Courtesan Sword" "Dragonbone Rapier" "Tempered Foil" "Pecoraro" "Spiraled Foil" "Jewelled Foil" "Harpy Rapier" "Dragoon Sword"

# ------ Two Hand Axes ------  Class == "Two Hand Axes"

# ALL
# "Stone Axe" "Jade Chopper" "Woodsplitter" "Poleaxe" "Double Axe" "Gilded Axe" "Shadow Axe" "Dagger Axe" "Jasper Chopper" "Timber Axe" "Headsman Axe" "Labrys" "Honed Cleaver" "Noble Axe" "Abyssal Axe" "Karui Chopper" "Talon Axe" "Sundering Axe" "Ezomyte Axe" "Vaal Axe" "Despot Axe" "Void Axe" "Apex Cleaver" "Fleshripper"
# "Jade Chopper" "Woodsplitter" "Poleaxe" "Double Axe" "Gilded Axe" "Shadow Axe" "Dagger Axe" "Jasper Chopper" "Timber Axe" "Headsman Axe" "Honed Cleaver" "Noble Axe" "Abyssal Axe"  "Talon Axe" "Sundering Axe" "Ezomyte Axe" "Void Axe" "Apex Cleaver" "Fleshripper"

# ------ Two Hand Maces ------  Class == "Two Hand Maces"

# ALL
# "Driftwood Maul" "Tribal Maul" "Mallet" "Sledgehammer" "Jagged Maul" "Brass Maul" "Fright Maul" "Morning Star" "Totemic Maul" "Great Mallet" "Steelhead" "Spiny Maul" "Crushing Force Magnifier" "Plated Maul" "Dread Maul" "Solar Maul" "Karui Maul" "Colossus Mallet" "Piledriver" "Meatgrinder" "Imperial Maul" "Terror Maul" "Coronal Maul" "Impact Force Propagator"
# "Tribal Maul" "Mallet" "Sledgehammer" "Jagged Maul" "Brass Maul" "Fright Maul" "Morning Star" "Totemic Maul" "Great Mallet"  "Crushing Force Magnifier" "Plated Maul"  "Solar Maul" "Karui Maul" "Imperial Maul" "Terror Maul" "Coronal Maul" "Impact Force Propagator"

# ------ Two Hand Swords ------  Class == "Two Hand Swords"

# ALL
# "Corroded Blade" "Longsword" "Bastard Sword" "Two-Handed Sword" "Etched Greatsword" "Ornate Sword" "Spectral Sword" "Curved Blade" "Butcher Sword" "Footman Sword" "Highland Blade" "Engraved Greatsword" "Blasting Blade" "Tiger Sword" "Wraith Sword" "Lithe Blade" "Headman's Sword" "Reaver Sword" "Ezomyte Blade" "Vaal Greatsword" "Lion Sword" "Infernal Sword" "Banishing Blade" "Exquisite Blade"
# "Longsword" "Bastard Sword" "Two-Handed Sword" "Etched Greatsword" "Ornate Sword" "Spectral Sword" "Curved Blade" "Butcher Sword" "Footman Sword" "Highland Blade" "Engraved Greatsword" "Blasting Blade" "Tiger Sword" "Wraith Sword" "Lithe Blade" "Headman's Sword" "Reaver Sword" "Ezomyte Blade" "Infernal Sword" "Banishing Blade" "Exquisite Blade"

# ------ Wands ------  Class == "Wands"

# ALL
# "Driftwood Wand" "Goat's Horn" "Carved Wand" "Quartz Wand" "Calling Wand" "Spiraled Wand" "Sage Wand" "Pagan Wand" "Faun's Horn" "Engraved Wand" "Crystal Wand" "Coiled Wand" "Congregator Wand" "Convening Wand" "Omen Wand" "Heathen Wand" "Demon's Horn" "Imbued Wand" "Opal Wand" "Tornado Wand" "Prophecy Wand" "Accumulator Wand" "Profane Wand" "Convoking Wand"

# ------ Warstaves ------  Class == "Warstaves"

# ALL
# "Iron Staff" "Coiled Staff" "Vile Staff" "Military Staff" "Serpentine Staff" "Potentiality Rod" "Foul Staff" "Ezomyte Staff" "Maelström Staff" "Judgement Staff" "Eventuality Rod"
#  "Potentiality Rod" "Maelström Staff" "Judgement Staff" "Eventuality Rod"



Hide
	Rarity Rare
	AnyEnchantment False
	Corrupted False
	FracturedItem False
	HasCruciblePassiveTree False
	Identified False
	Mirrored False
	SynthesisedItem False
	BaseType == {hide_bows + hide_claws + hide_daggers + hide_ohaxes + hide_ohmaces + hide_ohswords + hide_quivers + hide_rdaggers + hide_scepters + hide_staves + hide_tohswords + hide_thaxes + hide_thmaces + hide_thswords + hide_wands + hide_warstaves}
	ItemLevel <= 85
	SetFontSize 30
	DisableDropSound True
	
Hide
	Rarity Rare
	Corrupted True
	AnyEnchantment False
	FracturedItem False
	HasCruciblePassiveTree False
	Identified False
	Mirrored False
	SynthesisedItem False
	BaseType == {hide_bows + hide_claws + hide_daggers + hide_ohaxes + hide_ohmaces + hide_ohswords + hide_rdaggers + hide_scepters + hide_staves + hide_tohswords + hide_thaxes + hide_thmaces + hide_thswords + hide_wands + hide_warstaves}
	ItemLevel < 70

Hide
	Rarity Magic
	AnyEnchantment False
	FracturedItem False
	HasCruciblePassiveTree False
	SynthesisedItem False
	BaseType == {hide_bows + hide_claws + hide_daggers + hide_ohaxes + hide_ohmaces + hide_ohswords + hide_quivers + hide_rdaggers + hide_scepters + hide_staves + hide_tohswords + hide_thaxes + hide_thmaces + hide_thswords + hide_warstaves}
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Magic
	AnyEnchantment False
	FracturedItem False
	HasCruciblePassiveTree False
	SynthesisedItem False
	Identified False
	BaseType == {hide_wands}
	SetFontSize 30
	DisableDropSound True

Hide
	Rarity Normal
	BaseType == {hide_bows + hide_claws + hide_daggers + hide_ohaxes + hide_ohmaces + hide_ohswords + hide_quivers + hide_rdaggers + hide_scepters + hide_staves + hide_tohswords + hide_thaxes + hide_thmaces + hide_thswords + hide_wands + hide_warstaves}
	SetFontSize 30
	DisableDropSound True
	
"""



hide = hide_jew_gem_amul_belt_ring + hide_armour + hide_weapons

ee = """
#============================================================================================================
#	   Show EE
#============================================================================================================

Show
	Rarity Rare
	ItemLevel >= 86

Show
	SetFontSize 45
	SetTextColor 255 0 255 255
	SetBorderColor 255 0 255 255
	SetBackgroundColor 100 0 100 255
	PlayAlertSound 3 300
	PlayEffect Pink
	MinimapIcon 0 Pink Circle
"""


s = header + color_text + color_border + color_background + custom1 + currency + gems_jewels + weapon_armour + flasks + maps + don_now_jet + hide + ee

with open("Strict Code.filter", "w") as f:
	f.write(s)
