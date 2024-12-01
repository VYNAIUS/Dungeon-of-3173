
from random import seed, choice, randint, uniform
from coloring import enemy_name_color
from extra_functions import chance
from upgrades_functions import xp_to_lvl_up

def default_enemies(V):
    seed(V.global_seed)
    V.bounty_hunter_name_0 = ["Axel", "Blaze", "Dagger", "Echo", "Flint", "Gage", "Hawk", "Jax", "Kane", "Lex", "Mace", "Nash", "Orin", "Pax", "Quinn", "Raze", "Slade", "Thorn", "Vex", "Wolf"]
    V.bounty_hunter_name_1 = ["Black", "Blade", "Cage", "Fang", "Grim", "Hunt", "Iron", "Jade", "Knight", "Locke", "Raven", "Shadow", "Stone", "Strike", "Thorne", "Viper", "Ward", "Whisper", "Wolf", "Wylde"]
    V.evolution_name_suffix = [" Evolved", " Prime", "-Adapter", " Plus", " Mutant"]
    V.enemys = []
    V.enemy_areas = [[0, 1], [0], [0], [0, 1], [], [0], [1], [1], [1, 5], [1], [2], [2], [2, 4, 6], [6], [2], [3], [3], [3], [3], [3], [4], [2, 4], [4], [4], [4], [5], [5],
               [5], [5], [2, 6], [6], [6], [6], [], [], [0, 1, 3, 5], [1, 2, 3, 6], [1, 4, 5, 6], [], [], [], [], [], [0], [1, 2], [2], [3], [4], [5], [5],
               [6], [], [], [], [], [6], [], [6], [0], [2], [3], [4], [6], ["drought", 5], [], [], [5], [5], [5], [0], [0], [1], [5], [5]]
    V.enemy_is_boss = [False, False, False, False, False, True, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False,
                 False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, True, True, True, True, False, False, False, True, True, True, True, True, False,
                 True, False, False, False, False, False, False, True, True, True]
    V.enemys_power_level = [1, 0.9, 0.75, 1.35, 1.7, 1, 1.02, 0.95, 1.05, 1, 1.07, 0.95, 1.45, 0.55, 1, 1, 1.05, 0.6, 1.12, 1, 0.85, 1.15, 1, 1.4, 1, 1, 1.1, 1.07,
                      1, 1.15, 1.1, 1.45, 1, 2, 1.65, 1.75, 1.75, 1.75, 1.9, 1.9, 2, 2, 2, 1.1, 1.07, 0.5, 1.45, 1.3, 0.7, 0.8, 1.3, 1.5, 2.3, 1.3, 1.6, 1.02, 0.5,
                      1.2, 1.1, 1, 1.05, 0.6, 0.9, 0.35, 1.5, 1.5, 0.2, 0.9, 2, 1.13, 1.14, 1.03, 1, 1.5]
    V.enemys_name = ["Bush Man", "Weird Plant", "Arachno-flower", "Ent", "Spirit of Fear", "Treant", "Thug", "Bandit", "Dark Mage", "Bandit Chieftain", "Skeleton Warrior",
               "Undead Miner", "Bone Serpent", "Skeleton", "Soul Catcher", "Snowman Knifer", "Ice Elemental", "Snowman", "Snow Mage", "Yeti", "Spiderling",
               "Cave Spider", "Gargoyle", "Matriarch", "Spider Queen", "Cactus", "Desert Spider", "Sandwitch", "Cactus Golem", "Necromancer", "Poison Spider",
               "Rotten Ent", "Undead Paladin", "Shopkeeper", "Spirit of Kindness", choice(V.bounty_hunter_name_0) + " " + choice(V.bounty_hunter_name_1),
               choice(V.bounty_hunter_name_0) + " " + choice(V.bounty_hunter_name_1), choice(V.bounty_hunter_name_0) + " " + choice(V.bounty_hunter_name_1),
               "Spirit of Vitality", "Spirit of Strength", "Spirit of Might", "Spirit of Protection", "Yourself", "Venomous Roser", "Crystal Assassin",
               "Crystal Shard", "Snowman Shotgunner", "Arachno Mage", "Jerboa", "Tumbleweeder", "Dark Knight", "Death", "The 3173rd", "Change", "Cycle",
               "Amphibian Heretic", "Spectral Frog", "Amphibromancer", "Rose Knight", "Crystal Wizard", "Buff Polar Bear", "Spider King", "False Idol", "Wrom",
               "Insane Alchemist", "Antlion Parasite", "Antlion Larva", "Antlion Larva", "Antlion", "Vine Bookster", "Plant Mage", "Shield Thug", "Jerboa",
               "Mature Antlion Parasite"]
    V.enemys_name_colors = [[0, 170, 0], [0, 230, 0], [180, 200, 0], [180, 100, 0], [140, 0, 155], [190, 90, 0], [200, 185, 105], [200, 175, 120], [70, 70, 70],
                      [200, 185, 125], [210, 210, 170], [170, 165, 140], [170, 200, 170], [210, 210, 210], [75, 220, 220], [240, 240, 240], [40, 220, 220],
                      [240, 240, 240], [135, 220, 220], [190, 190, 190], [50, 65, 90], [90, 95, 110], [130, 140, 130], [50, 160, 90], [70, 200, 140],
                      [90, 240, 90], [120, 80, 70], [200, 175, 20], [110, 200, 110], [140, 180, 170], [50, 220, 50], [90, 90, 30], [100, 100, 100],
                      [100, 220, 100], [240, 240, 0], [40, 210, 210], [210, 40, 40], [40, 210, 40], [0, 255, 0], [255, 0, 0], [255, 128, 0], [0, 200, 255],
                      [249, 241, 165], [200, 0, 50], [255, 100, 255], [255, 100, 255], [255, 230, 230], [40, 100, 100], [150, 150, 100], [150, 150, 50],
                      [60, 70, 60], [100, 100, 100], [249, 241, 165], [100, 100, 175], [100, 200, 250], [20, 200, 20], [0, 250, 250], [0, 250, 100], [200, 0, 35],
                      [255, 50, 255], [255, 200, 200], [100, 210, 100], [75, 250, 75], [250, 220, 100], [200, 0, 150], [210, 200, 160], [190, 200, 160],
                      [190, 200, 160], [170, 180, 140], [0, 200, 50], [100, 255, 0], [150, 150, 150], [150, 150, 100], [210, 200, 160]]
    V.enemys_elements = [[6], [6], [6], [2, 6], [4, 5], [2, 6], [2], [2], [5], [1, 2], [0], [0], [0, 6], [0], [5, 6], [1], [5], [], [1, 5], [1], [3], [5], [3], [0], [3],
                       [4], [4], [4, 5], [4], [0, 5], [0], [0, 2], [0, 2], [], [5], [2], [1], [], [0, 5], [1, 5], [3, 5], [2, 6, 5], [6], [6], [], [0], [1], [3], [4],
                       [4], [0, 2], [3], [6, 4, 0, 3, 2, 1], [5], [6], [], [], [], [6], [5], [1], [3], [], [4], [1], [4], [4], [4], [4], [5, 6], [5, 6], [2], [4], [4]] # 0 - Vitality, 1 - Strength, 2 - Protection, 3 - Might, 4 - Innocence, 5 - Mana, 6 - Magic Protection
    V.enemys_base_hp = [30, 25, 23, 50, 50, 78, 35, 30, 27, 78, 31, 27, 40, 10, 66, 20, 27, 10, 25, 84, 10, 30, 25, 45, 72, 26, 32, 27, 72, 25, 30, 55, 78, 60, 72,
                  60, 42, 56, 150, 50, 30, 60, 1, 30, 30, 10, 19, 40, 2, 30, 40, 100, 350, 75, 125, 30, 7, 35, 72, 60, 78, 36, 60, 20, 60, 40, 5, 5, 60, 34, 30, 72,
                  2, 84]
    V.enemys_base_dmg = [10, 7, 8, 12, 14, 14, 10, 9, 7, 13, 10, 9, 12, 4, 10, 15, 7, 5, 4, 13, 7, 11, 9, 12, 12, 10, 11, 4, 12, 5, 12, 14, 12, 10, 10, 10, 25, 12,
                   20, 60, 30, 17, 1, 10, 14, 4, 40, 9, 0, 7, 15, 1, 50, 20, 30, 10, 0, 9, 10, 12, 20, 15, 10, 7, 12, 19, 1, 1, 22, 10, 9, 7, 0, 20]
    V.enemys_base_def = [0, 0, 0, 0.4, 2, 1, 0, 0, 0, 2, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 7, 2, 15, 2, 5, 7, 3, 0, 40, 1, 1, 1, 0, 0, 0,
                       0.2, 0, 2.5, 4, 150, 3, 15, 0, 0, 0, 1, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 5, 0, 3]
    V.enemys_base_crit = [0.02, 0.01, 0.02, 0.04, 0.12, 0.06, 0.05, 0.05, 0.03, 0.09, 0.07, 0.04, 0.1, 0.01, 0.06, 0.05, 0.04, 0.01, 0.03, 0.11, 0.1, 0.05, 0.15, 0.1, 0.1,
                        0.06, 0.05, 0.03, 0.07, 0.03, 0.06, 0.06, 0.1, 0.35, 0.13, 0.05, 0.4, 0.1, 0.03, 0.2, 0.8, 0.05, 1, 0.04, 0.07, 0.01, 0, 0.03, 0, 0.02, 0.1, 1,
                        0.4, 0.1, 0.1, 0.04, 0, 0.03, 0.1, 0.06, 0.1, 0.1, 0.07, 0.01, 0.05, 0.02, 0, 0, 0.04, 0.02, 0.02, 0.05, 0, 0.05]
    V.enemys_base_spk = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 7, 0, 0, 0, 10, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0,
                       0, 0.25, 0, 5, 15, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0.25, 0.125, 0.125, 0.5, 0, 0, 0, 0, 0.25]
    V.enemys_base_psn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 2, 3, 0, 2, 0, 0, 0, 4, 0, 0, 7, 0, 0, 0, 10, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                       0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    V.enemys_base_immortality = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0,
                               0, 0, 0, 0, 0.3, 2.5, 1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0.45, 0, 0.7, 0, 0, 0, 0, 0.07, 0, 0.1, 0, 0]
    V.enemys_descriptions = ["That's a weird looking bush", "Boring plant, uses roots as its legs", "This plant usually accompanies its other siblings",
                       "This tree moves surprisingly quickly for its size", "This spirit punishes those, who abuse altars' magic of innocence",
                       "It is ent but stronger", "This bandit is capable of killing dangerous foes", "This person is for some reason aggressive",
                       "This mage is able to pierce through regular armor", "This bandit is capable of killing really powerful foes",
                       "Was a warrior before death and still is after death", "A qualified gravedigger", "This serpent seems to have consumed several humans",
                       "A dead traveller", "Ancient contraption used for fighting ghosts and evil spirits",
                       "This snowman appears to be possessed... and has a knife", "Floating icicles that are orbiting some magical light blue sphere",
                       "This snowman appears to be possessed", "This mage is able to summon snowmen to their aid", "This snow gorilla is a formidable threat",
                       "Agile and venomous little spider", "This spider is pretty rare to see in well lit areas", "Stone statue turned into a living creature",
                       "Lazy spider capable of reproducing quickly", "Past matriarch mutated into Spidernach's form",
                       "Thorny moving cactus attacks any intruder of their territory", "This spider has evolved to burry itself underground and come out to catch prey",
                       "Uses powers of Suffering Sands to heal allies and attack intruders", "Infestacious cactus has grown over an ancient stone golem",
                       "Dark mage who is able to summon the dead to their aid", "Extremely poisonous spider capable of killing large prey",
                       "Corrupted by eternal life, this ent will fight to protect the Holy Forest",
                       "Once great paladin and now a force mindlessly protecting the Holy Forest", "One of the only humans, that you have made angry",
                       "This spirit avenges those who act justly in life", "A bounty hunter who seems to use defense a lot",
                       "A bounty hunter who seems to specify in damage", "A bounty hunter who seems to be proficient in poison and spikes",
                       "This spirit punishes those, who abuse altars' magic of vitality", "This spirit punishes those, who abuse altars' magic of strength",
                       "This spirit punishes those, who abuse altars' magic of might", "This spirit punishes those, who abuse altars' magic of protection and magic protection",
                       "...", "Thorny, venomous predator, that leaves its prey slowly dying", "Empowered by corrupt crystals of the Stale Cave, they seek out powerful foes",
                       "Crystals infused with life force of corrupt crystals", "This snowman appears to be possessed... and has a freaking shotgun",
                       "This mage is adept at healing arachnids", "Unassuming rodent. What can go wrong?", "A big bug that uses tumbleweed as a nest",
                       "Corrupted by eternal life, this knight mindlessly protects the Holy Forest",
                       "'Death comes for all of us. And those who cheat her, have to fight her'", "Greatest Cycle's creation yet, it is ready to consume you",
                       "'Once one cycle ends, something changes, allowing for a new cycle to be born'", "'Once one cycle ends, something changes, allowing for a new cycle to be born'",
                       "These heretics worship false idols of Great J", "These vengeful spirits, that resemble frogs, are the last resort of many amphibian heretics",
                       "Elite amphibian heretic, who learned how manipulate and create frogs", "The great knight that protects the Garden's grounds",
                       "A great wizard that infused himself with corrupted crystals of the Stale Cave", "There is little explanation of how this bear has visible abs",
                       "Male Spidernachs are considerably smaller than their counterparts", "This frog has been empowered by magic of amphibian heretics",
                       "This worm like creature is quite common during dry weather", "A somewhat immortal alchemist that robs his customers when the buy nothing for too long",
                       "This incredibly large parasite can make others transform", "This larva may mature when provoked", "This larva may mature when provoked",
                       "Mature antlion, ready to fight, hunt and kill for its colony", "This mage uses powers of Vine's Book to protect the Garden's grounds",
                       "This mage is obsessed with preserving plant life of the Garden's grounds", "This thug stole the armour from one of the legendary shield men",
                       "Unassuming rodent. What can go wrong?", "This incredibly large parasite forces its own offsprings to grow"]
    V.enemys_patterns = [[0], [0], [0], [0, 0, 0, 0, 0, 0, 1], [2, 2, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0], [0], [2], [0, 0, 0, 1, 0, 0, 0], [0], [0],
                   [0, 0, 0, 0, 0, 0, 0, 1], [0], [2, 2, 2, 0], [0], [2], [0], [3, 2, 2], [0, 0, 0, 1, 0, 0, 0], [0], [0], [0], [0, 4, 3, 4, 0, 4],
                   [0, 0, 0, 4, 4, 3], [0], [0], [2, 2, 2, 2, 2, 5], [0, 0, 0, 0, 1], [2, 3, 2], [0, 0, 4, 0], [0, 1, 0, 0, 1, 0, 0, 0, 0], [2, 2, 1, 2, 2, 0],
                   [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1], [2, 1, 2, 1, 0, 0], [1, 1, 0], [0], [1, 0, 0, 0, 0, 0, 1, 1], [2, 2, 5, 5, 2], [0, 2], [0],
                   [2, 1, 2, 2, 1, 1, 2, 2], [0], [0, 0, 0, 1], [0], [0], [0, 4], [2, 2, 5], [4], [1, 0], [0, 1, 0], [2], [0], [2], [0, 0, 5],
                   [0, 0, 0, 1], [0], [3, 0, 0, 0], [0], [2], [0, 0, 1, 0], [0, 4], [0, 2, 1], [0], [0, 6, 0, 0, 7, 0], [0, 8, 0, 0, 0], [4, 4, 0], [4, 4, 0],
                   [0], [2], [2, 6, 2, 2], [1, 1, 0, 0, 1, 1], [4], [0, 3, 8, 0, 0]]
    V.enemys_spawners = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1, 13, 13], [0], [0], [0], [0], [0], [0, 17], [0], [0], [0], [0],
                       [0, 20, 20], [0, 20, 20], [0], [0], [0, 25, 26, 27, 28, 48, 49, 65, 66, 67, 68], [0], [0, 13], [0], [0], [0], [1, 34], [0], [0], [0], [0],
                       [0, 0, 1, 2, 3, 5, 6, 7, 8, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 33, 43, 44, 45, 46, 47, 48, 49, 50,
                       52, 58, 59, 60, 61, 65, 66, 67, 68, 69, 70, 71],
                       [0], [0], [0], [0], [0], [1, 45], [0], [0], [0, 20, 21, 23, 24, 26, 30, 61], [1, 65], [0], [1, 13], [0], [0], [0], [0, 52], [1, 56],
                       [0], [1, 56, 56], [0], [0], [0], [0], [1, 56, 56, 56, 56], [0], [0], [0], [0], [1, 68], [0], [0], [0, 0, 1, 2, 4, 43, 58], [0], [1, 73], [0, 66, 67]]
    V.enemy_actions = [enemy_hit, enemy_defend, enemy_magic_hit, enemy_summon, enemy_stall, enemy_heal, enemy_stun, enemy_berserk, enemy_transform_others]
    V.ally_actions = [ally_hit, ally_hit, ally_hit, ally_hit, ally_hit, ally_hit, ally_hit, ally_hit, ally_hit]
    V.enemy_unconsumable = [4, 34, 38, 39, 40, 41, 42, 51, 52, 53, 54, 64, 67]
    V.enemy_unelite = [4, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 51, 52, 53, 54, 64]
    V.bosses_for_areas = [[5, 58], [9, 71], [14, 59], [19, 60], [24, 61], [28, 72, 73], [32, 62]]
    V.hunters_appeared = [False, False, False]

class Enemies:
    def __init__(self, V, enemy_id = 0, summoned = False, summoner_id = 0, elite = 0):
        if enemy_id == 4 and V.fear_anger - V.spirit_anger_reduction > 1:
            multiplier = round(V.fear_anger) - V.spirit_anger_reduction
        elif enemy_id == 34 and V.shopkeeper_deaths - V.spirit_anger_reduction > 1:
            multiplier = round(V.shopkeeper_deaths) - V.spirit_anger_reduction
        elif enemy_id == 38 and V.vitality_anger - V.spirit_anger_reduction > 1:
            multiplier = round(V.vitality_anger) - V.spirit_anger_reduction
        elif enemy_id == 39 and V.strength_anger - V.spirit_anger_reduction > 1:
            multiplier = round(V.strength_anger) - V.spirit_anger_reduction
        elif enemy_id == 40 and V.might_anger - V.spirit_anger_reduction > 1:
            multiplier = round(V.might_anger) - V.spirit_anger_reduction
        elif enemy_id == 41 and V.protection_anger - V.spirit_anger_reduction > 1:
            multiplier = round(V.protection_anger) - V.spirit_anger_reduction
        else:
            multiplier = 1
            
        elite_prefixes = []
        if not enemy_id in V.enemy_unelite:
            possible_elite_prefixes = ["Toxic ", "Impenetrable ", "Critical ", "Thorny ", "Tanky "]
            for i in range(elite):
                item = choice(possible_elite_prefixes)
                possible_elite_prefixes.remove(item)
                elite_prefixes.append(item)

        name_prefix = ""
        for i in elite_prefixes:
            name_prefix = name_prefix + i

        self.en_id = enemy_id
        self.name = name_prefix + V.enemys_name[enemy_id]
        self.description = V.enemys_descriptions[enemy_id]
        if "Tanky " in elite_prefixes:
            self.hp = round(V.enemys_base_hp[enemy_id] * health_multiplier(V, enemy_id) * multiplier * 2.3)
        else:
            self.hp = round(V.enemys_base_hp[enemy_id] * health_multiplier(V, enemy_id) * multiplier)
        self.max_hp = self.hp
        self.dmg = round(V.enemys_base_dmg[enemy_id] * damage_multiplier(V, enemy_id) * multiplier)
        self.defense = round((V.enemys_base_def[enemy_id] + defense_addition(V, enemy_id)) * defense_multiplier(V, enemy_id) * multiplier)
        if "Critical " in elite_prefixes:
            self.crit = round(V.enemys_base_crit[enemy_id] * 2, 2) * crit_multiplier(V, enemy_id)
        else:
            self.crit = round(V.enemys_base_crit[enemy_id], 2) * crit_multiplier(V, enemy_id)
        self.original_defense = self.defense
        if "Thorny " in elite_prefixes:
            self.spk = round((V.enemys_base_spk[enemy_id] + 2) * spike_multiplier(V, enemy_id) * multiplier * 2.3)
        else:
            self.spk = round(V.enemys_base_spk[enemy_id] * spike_multiplier(V, enemy_id) * multiplier)
        if "Toxic " in elite_prefixes:
            self.psn = round((V.enemys_base_psn[enemy_id] + 2) * poison_multiplier(V, enemy_id) * multiplier * 1.5)
        else:
            self.psn = round(V.enemys_base_psn[enemy_id] * poison_multiplier(V, enemy_id) * multiplier)
        if summoned:
            self.psnd = V.enemys[summoner_id].psnd // 2
        else:
            self.psnd = 0
        self.stnd = 0
        if "Impenetrable " in elite_prefixes:
            self.imm = round((V.enemys_base_immortality[enemy_id] + 2) * immortality_multiplier(V, enemy_id) * multiplier)
        else:
            self.imm = round(V.enemys_base_immortality[enemy_id] * immortality_multiplier(V, enemy_id) * multiplier)
        self.pattern = V.enemys_patterns[enemy_id].copy()
        self.pattern_action = 0
        self.spawner = V.enemys_spawners[enemy_id].copy()
        if not enemy_id in [4, 34, 38, 39, 40, 41, 42] and not summoned:
            self.money = round((self.hp + (self.dmg * 2) + (self.defense * 3) + (self.spk * 1.5) + (self.psn * 2.5) + (self.imm * 10)) * 55 / (13 * V.difficulty))
            self.xp = round((self.hp + (self.dmg * 2) + (self.defense * 3) + (self.spk * 1.5) + (self.psn * 2.5) + (self.imm * 10)) * 55 / (10 * V.difficulty))
        elif enemy_id == 42 and not summoned:
            self.money = V.player_money
            self.xp = V.player_xp
        else:
            self.money = 0
            self.xp = 0


def enemy_hit(V, attacker = 0):

    if V.player_dodge_chance > 0:
        dodges_needed = 100 // V.player_dodge_chance
        if V.player_dodge_count < dodges_needed:
            if chance(V.player_dodge_chance / 100) and V.player_dodged == False:
                will_dodge = True
                V.player_dodged = True
                V.player_dodge_count += 1
            else:
                will_dodge = False
                V.player_dodge_count += 1
        else:
            if V.player_dodged == True:
                will_dodge = False
                V.player_dodge_count += 1
            else:
                will_dodge = True
            V.player_dodge_count = 0
            V.player_dodged = False
    else:
        will_dodge = False

    print(enemy_name_color(V, V.enemys[attacker].en_id), end = "")

    dealt_damage = round(V.enemys[attacker].dmg * (randint(90, 110) / 100))
    cur_crit_chance = V.enemys[attacker].crit
    crit_count = 0
    while cur_crit_chance > 0:
        if chance(cur_crit_chance):
            dealt_damage *= 2
            crit_count += 1
        cur_crit_chance -= 1
    if len(V.allys) > 0:
        alive_allies = 0
        for i in V.allys:
            if i.hp > 0:
                alive_allies += 1
        dealt_damage //= 1 + alive_allies
        if alive_allies > 0:
            print(V.enemys[attacker].name, "dealt ", end = "")
        k = 0
        for i in V.allys:
            if i.hp <= 0:
                continue
            k += 1
            ally_dealt_damage = dealt_damage
            ally_dealt_damage -= i.defense
            if ally_dealt_damage < 1:
                ally_dealt_damage = 1
            ally_dealt_damage += V.enemys[attacker].psn
            if i.imm > 0:
                ally_dealt_damage = 0
            i.hp -= ally_dealt_damage
            if k > 1:
                print(", ", end = "")
            print(ally_dealt_damage, "DMG to", enemy_name_color(V, i.en_id) + i.name + enemy_name_color(V, V.enemys[attacker].en_id), end = "")
        print("!")
    V.player_dealt_damage = round(dealt_damage * (1 - (V.player_shield / 100)))
    if V.player_dealt_damage > V.player_base_def + V.player_extra_def:
        V.player_dealt_damage -= V.player_base_def + V.player_extra_def
    else:
        V.player_dealt_damage = 1
    if immortality_compute(V) > 0:
        V.player_dealt_damage = round(dealt_damage * (1 - immortality_compute(V)))
    if will_dodge == True:
        V.player_dealt_damage = 0
    V.player_current_hp -= V.player_dealt_damage
    if V.player_current_hp < 0:
        V.player_current_hp = 0
    if V.player_spikes > 0:
        V.enemys[attacker].hp -= V.player_spikes
        if V.enemys[attacker].hp < 0:
            V.enemys[attacker].hp = 0
    if V.player_dealt_damage > 0:
        print(V.enemys[attacker].name, "dealt", V.player_dealt_damage, "DMG! You have", V.player_current_hp, "HP left!")
        if V.enemys[attacker].psn > 0:
            V.player_poisoned += V.enemys[attacker].psn
            print(V.enemys[attacker].name, "inflicted", V.enemys[attacker].psn, "PSN! Your total poison is", V.player_poisoned, "PSN'd!")
    elif will_dodge == True:
        print(V.enemys[attacker].name, "dealt no damage to you because you managed to dodge!")
    else:
        print(V.enemys[attacker].name, "dealt no damage to you because of your immortality!")
    if crit_count == 1:
        print("It was a critical hit!")
    elif crit_count > 1:
        print("They rolled a critical hit", crit_count, "times!")
    if V.player_spikes > 0:
        print(V.enemys[attacker].name, "suffered", V.player_spikes, "DMG from your spikes! They have", V.enemys[attacker].hp, "HP left!")
        if V.player_spikes_armor_break > 0:
            V.enemys[attacker].defense -= V.player_spikes_armor_break
            print(V.enemys[attacker].name, "lost", V.player_spikes_armor_break, "DEF!")

    print("\033[0m", end = "")

def enemy_defend(V, defender = 0):

    print(enemy_name_color(V, V.enemys[defender].en_id), end = "")

    if V.enemys[defender].original_defense < 3:
        V.enemys[defender].defense += 1
    else:
        V.enemys[defender].defense += V.enemys[defender].original_defense // 10
    print(V.enemys[defender].name, "defended! Their defense is now", V.enemys[defender].defense, "DEF!")

    print("\033[0m", end = "")
    
def enemy_magic_hit(V, attacker = 0):

    print(enemy_name_color(V, V.enemys[attacker].en_id), end = "")

    dealt_damage = round(V.enemys[attacker].dmg * (randint(85, 105) / 100))
    cur_crit_chance = V.enemys[attacker].crit
    crit_count = 0
    while cur_crit_chance > 0:
        if chance(cur_crit_chance):
            dealt_damage *= 2
            crit_count += 1
        cur_crit_chance -= 1
    dealt_damage = round(dealt_damage * (1 - (V.player_magic_shield / 100)))
    if dealt_damage > V.player_base_magic_def + V.player_extra_magic_def:
        dealt_damage -= V.player_base_magic_def + V.player_extra_magic_def
    else:
        dealt_damage = 1
    if immortality_compute(V) > 0:
        dealt_damage = round(dealt_damage * (1 - immortality_compute(V)))
    V.player_current_hp -= dealt_damage
    if V.player_current_hp < 0:
        V.player_current_hp = 0
    if dealt_damage > 0:
        print(V.enemys[attacker].name, "dealt", dealt_damage, "magic DMG! You have", V.player_current_hp, "HP left!")
    else:
        print(V.enemys[attacker].name, "dealt no damage to you because of your immortality!")
    if crit_count == 1:
        print("It was a critical hit!")
    elif crit_count > 1:
        print("They rolled a critical hit", crit_count, "times!")

    print("\033[0m", end = "")

def enemy_summon(V, summoner = 0):

    print(enemy_name_color(V, V.enemys[summoner].en_id), end = "")

    spawn = 0
    print(V.enemys[summoner].name, "summoned ", end = "")
    for k in V.enemys[summoner].spawner:
        spawn += 1
        if spawn > 1:
            V.enemys.append(Enemies(V, k, summoned = True, summoner_id = summoner))
            if spawn == 2:
                print(V.enemys_name[k], end = "")
            else:
                print(",", V.enemys_name[k], end = "")
    print(" to their aid.")

    print("\033[0m", end = "")
    V.queue_amount = 0

def enemy_stall(V, quitter = 0):

    print(enemy_name_color(V, V.enemys[quitter].en_id), end = "")

    print(V.enemys[quitter].name, "did absolutely nothing.")

    print("\033[0m", end = "")

def enemy_heal(V, healer = 0):

    print(enemy_name_color(V, V.enemys[healer].en_id), end = "")

    healed = 0
    print(V.enemys[healer].name, "attempted to heal ", end = "")
    for i in range(len(V.enemys)):
        if i == healer:
            continue
        else:
            heal = 0
            for k in range(len(V.enemys[healer].spawner)):
                heal += 1
                if V.enemys[i].en_id == V.enemys[healer].spawner[k] and heal > 1:
                    V.enemys[i].hp += round(V.enemys[i].max_hp * 0.1)
                    if V.enemys[i].hp > V.enemys[i].max_hp:
                        V.enemys[i].hp = V.enemys[i].max_hp
                    healed += 1
                    if healed > 1:
                        print(", ", end = "")
                    print(V.enemys[i].name, "for", round(V.enemys[i].max_hp * 0.1), "HP", end = "")
    if healed == 0:
        print("and didn't succed.")
    else:
        print(".")

    print("\033[0m", end = "")

def enemy_stun(V, stunner = 0):
    
    print(enemy_name_color(V, V.enemys[stunner].en_id), end = "")

    V.player_stunned += 2

    print(V.enemys[stunner].name, "stunned you for 2 turns! You are totally stunned for", V.player_stunned, "turns!", end = "")
    
    print("\033[0m")

def enemy_berserk(V, berserk = 0):

    print(enemy_name_color(V, V.enemys[berserk].en_id), end = "")

    V.enemys[berserk].dmg = round(V.enemys[berserk].dmg * 1.3)
    V.enemys[berserk].crit = round(V.enemys[berserk].crit * 2, 2)
    
    print(V.enemys[berserk].name, "increased their damage up to", V.enemys[berserk].dmg, "DMG!")
    print(V.enemys[berserk].name, " increased their crit chance up to ", round(V.enemys[berserk].crit * 100), "%!", sep = "", end = "")
    
    print("\033[0m")

def enemy_transform_others(V, transformer = 0):

    print(enemy_name_color(V, V.enemys[transformer].en_id), end = "")
    
    print(V.enemys[transformer].name, "made ", end = "")
    transformed = 0
    for i in range(len(V.enemys)):
        if i == transformer:
            continue
        else:
            if V.enemys[i].spawner[0] == 1:
                transformed += 1
                if transformed == 1:
                    print(V.enemys[i].name, end = "")
                else:
                    print(",", V.enemys[i].name, end = "")
                V.enemys[i].hp = 0

    if transformed == 0:
        print("no one transform.")
    else:
        print(" transform.")

    print("\033[0m", end = "")


def ally_hit(V, attacker = 0):

    if len(V.enemys) > 0:

        print(enemy_name_color(V, V.allys[attacker].en_id), end = "")

        dealt_damage = round(V.allys[attacker].dmg * (randint(90, 110) / 100))
        dealt_damage //= len(V.enemys)
        print(V.allys[attacker].name, "dealt ", end = "")
        k = 0
        for i in V.enemys:
            k += 1
            target_dealt_damage = dealt_damage
            target_dealt_damage -= i.defense
            if target_dealt_damage < 1:
                target_dealt_damage = 1
            if i.imm > 0:
                target_dealt_damage = 0
                target_dealt_poison = 0
            else:
                target_dealt_poison = V.allys[attacker].psn
            i.hp -= target_dealt_damage
            i.psnd += target_dealt_poison
            if i.spk > 0:
                V.allys[attacker].hp -= i.spk
            if k > 1:
                print(", ", end = "")
            print(target_dealt_damage, "DMG to", enemy_name_color(V, i.en_id) + i.name + enemy_name_color(V, V.allys[attacker].en_id), end = "")
        print("!")

        print("\033[0m", end = "")

def health_multiplier(V, enemy_id = 0):

    hp_multi = 1
    if V.score > 177500:
        print("Started to calculate health")
    if enemy_id == 42:
        hp_multi = V.player_max_hp
    else:
        for i in range(V.score):
            if hp_multi > 10000000000000000000000:
                hp_multi = int(hp_multi)
                hp_multi += round(hp_multi // 100000000) + ((V.difficulty - 50) * 1000)
            else:
                hp_multi *= 1.05 + uniform(0.0006 * V.difficulty + 0.01, 0.0006 * V.difficulty + 0.06)
                #hp_multi *= 1.05 + (randint(-50 + V.difficulty, -40 + V.difficulty) / 100)
                hp_multi = round(hp_multi, 10)
    return hp_multi

def damage_multiplier(V, enemy_id = 0):

    dmg_multi = 1
    if V.score > 177500:
        print("Started to calculate damage")
    if enemy_id == 42:
        dmg_multi = round(V.player_base_dmg * (V.weapon_damage_ranges[V.player_weapon][0] + V.player_damage_range_boost + V.weapon_damage_ranges[V.player_weapon][1] + V.player_damage_range_boost) / 200)
    elif enemy_id == 51:
        if V.player_magic_shield != 100:
            dmg_multi = round(0.042 * V.player_max_hp / ((100 - V.player_magic_shield) / 100)) + V.player_base_magic_def + V.player_min_extra_magic_def
        else:
            dmg_multi = round(0.042 * V.player_max_hp) + V.player_base_magic_def + V.player_min_extra_magic_def
    else:
        for i in range(V.score):
            if dmg_multi > 10000000000000000000000:
                dmg_multi = int(dmg_multi)
                dmg_multi += round(dmg_multi // 100000000) + ((V.difficulty - 50) * 1000) 
            else:
                dmg_multi *= 1 + uniform(V.difficulty * 0.00075 + 0.01, V.difficulty * 0.00075 + 0.04)
                #dmg_multi *= 1 + (randint(-460 + V.difficulty * 10, -430 + V.difficulty * 10) / 1000)
                dmg_multi = round(dmg_multi, 10)
    return dmg_multi

def defense_multiplier(V, enemy_id = 0):
    def_multi = 1
    if V.score > 177500:
        print("Started to calculate defense multiplier")
    if enemy_id == 42:
        def_multi = V.player_base_def
    else:
        for i in range(V.score):
            if def_multi > 10000000000000000000000:
                def_multi = int(def_multi)
                def_multi += round(def_multi // 100000000) + ((V.difficulty - 50) * 1000)
            else:
                def_multi *= 1 + uniform(0.0001 * V.difficulty + 0.005, 0.0001 * V.difficulty + 0.065)
                #def_multi *= 1 + (randint(-50 + V.difficulty, -43 + V.difficulty) / 100)
                def_multi = round(def_multi, 10)
    return def_multi

def defense_addition(V, enemy_id = 0):

    def_add = 0
    if V.score > 887500:
        print("Started to calculate defense addition")
    if enemy_id == 42:
        def_add = 0
    else:
        if V.difficulty != 0:
            if V.difficulty <= 250:
                for i in range(V.score // (250 // V.difficulty)):
                    def_add += 1
            else:
                for i in range(round(V.score * (V.difficulty // 250))):
                    def_add += 1
    return def_add

def crit_multiplier(V, enemy_id = 0):

    crit_multi = 1
    if V.score > 887500:
        print("Started to calculate crit multiplier")
    if enemy_id == 42:
        crit_multi = V.player_crit_chance / 100
    else:
        for i in range(V.score):
            if crit_multi < 10000000:
                crit_multi *= 1 + uniform(0.00008 * V.difficulty + 0.0001, 0.00008 * V.difficulty + 0.0002)
            else:
                break
    return crit_multi

def spike_multiplier(V, enemy_id = 0):

    spk_multi = 1
    if V.score > 177500:
        print("Started to calculate spike multiplier")
    if enemy_id == 42:
        spk_multi = V.player_spikes
    else:
        for i in range(V.score):
            if spk_multi > 10000000000000000000000:
                spk_multi = int(spk_multi)
                spk_multi += round(spk_multi // 100000000)
            else:
                spk_multi *= 1 + uniform(0.00058 * V.difficulty + 0.001, 0.00058 * V.difficulty + 0.021)
                #spk_multi *= 1 + (randint(3, 5) / 100)
                spk_multi = round(spk_multi, 10)
    return spk_multi

def poison_multiplier(V, enemy_id = 0):

    psn_multi = 1
    if V.score > 177500:
        print("Started to calculate poison multiplier")
    if enemy_id == 42:
        psn_multi = V.player_poison
    else:
        for i in range(V.score):
            if psn_multi > 10000000000000000000000:
                psn_multi = int(psn_multi)
                psn_multi += round(psn_multi // 100000000)
            else:
                psn_multi *= 1 + uniform(0.00058 * V.difficulty + 0.001, 0.00058 * V.difficulty + 0.021)
                #psn_multi *= 1 + (randint(3, 5) / 100)
                psn_multi = round(psn_multi, 10)
    return psn_multi

def immortality_multiplier(V, enemy_id = 0):

    imm_multi = 1
    if V.score > 177500:
        print("Started to calculate impenetrability multiplier")
    if enemy_id == 42:
        imm_multi = V.player_immortality // 2
    else:
        for i in range(V.score):
            if imm_multi > 10000000000000000000000:
                imm_multi = int(imm_multi)
                imm_multi += round(imm_multi // 100000000)
            else:
                imm_multi *= 1 + uniform(0.00018 * V.difficulty + 0.001, 0.00018 * V.difficulty + 0.011)
                #imm_multi *= 1 + (randint(1, 2) / 100)
                imm_multi = round(imm_multi, 10)
    return imm_multi

def immortality_compute(V):
    if V.player_immortality > 0:
        return V.player_current_immortality / V.player_immortality
    else:
        return 0

def fight_choose(V, extra_power_level = 0):
    seed(V.enemy_encouter_seed)
    V.enemy_encouter_seed = randint(0, 10000)
    possible_enemies = []
    enemies = []

    if V.eclipse:
        game_time_bonus = 0.24
    elif V.game_time < 12:
        game_time_bonus = 0
    elif V.game_time < 18:
        game_time_bonus = round(V.game_time / 100, 2)
    elif V.game_time < 22:
        game_time_bonus = round(V.game_time / 90, 2)
    else:
        game_time_bonus = round(0.23 - round(V.game_time / 100, 2), 2)
    cur_max_power_level = V.max_power_level + game_time_bonus + extra_power_level

    for i in range(len(V.enemys_name)):
        if (V.enemy_is_boss[i] == False and V.area_id in V.enemy_areas[i]) or ("drought" in V.enemy_areas[i] and 9 in V.current_weather):
            if i in [35, 36, 37]:
                if V.hunters_appeared[i - 35] == False:
                    possible_enemies.append(i)
            else:
                possible_enemies.append(i)

    if V.overkill == False:
        while len(possible_enemies) > 0:
            i = choice(possible_enemies)
            if cur_max_power_level - V.enemys_power_level[i] < 0:
                while i in possible_enemies:
                    possible_enemies.remove(i)
            else:
                if i == 35 or i == 36 or i == 37:
                    while i in possible_enemies:
                        possible_enemies.remove(i)
                    V.hunters_appeared[i - 35] = True
                enemies.append(i)
                cur_max_power_level -= V.enemys_power_level[i]
    else:
        while cur_max_power_level > 0:
            i = choice(possible_enemies)
            if i == 35 or i == 36 or i == 37:
                while i in possible_enemies:
                    possible_enemies.remove(i)
                V.hunters_appeared[i - 35] = True
            enemies.append(i)
            cur_max_power_level -= V.enemys_power_level[i]
    if len(enemies) == 0:
        enemies.append(4)
    spirits_for_fight_choose(V, enemies)
    return enemies

def bossfight_choose(V):
    V.is_boss_battle = True
    if V.game_mode == "story" and V.final_area == True:
        if V.change_recruited == False and V.death_defeated == False:
            enemies = [52]
            print('''\033[38;2;100;200;250m"My child, it is time to prove yourself worthy. Prove it to your sibling."\033[0m''')
        elif V.change_recruited == True and V.death_defeated == False:
            enemies = [52, 54]
            print('''\033[38;2;100;200;250m"My child, it is time... Who is that person behind you?"\033[0m
The weird man from before approaches you and starts to speak to the glass ceiling of the Garden,
\033[38;2;100;100;175m"You know who I am, Cycle. Your child and I decided to put a stop to this madness. So come out and fight us!"\033[0m
A familiar figure appears in front of you two.
\033[38;2;100;200;250m"I am sorry, my child,"\033[0m it says.''')
        elif V.change_recruited == False and V.death_defeated == True:
            enemies = [52, 54]
            print('''\033[38;2;100;200;250m"My child, it is time... What is that thing behind you?"\033[0m
The masked creature crawls up behind you and starts to speak to something,
\033[38;2;100;100;100m"Hello, Cycle. I am glad I refused your plea for help, when you tried to execute Change."\033[0m
The voice responds, \033[38;2;100;200;250m"I recognise your voice, Death. Why did you come here?"\033[0m
\033[38;2;100;100;100m"To stop this madness. Your creation and I are here to do so."\033[0m
A familiar figure appears in front of you two.
\033[38;2;100;200;250m"I am sorry, my child,"\033[0m it says.''')
        else:
            print('''\033[38;2;100;200;250m"My child, it is time... Who are those?"\033[0m
The weird man from before approaches you and starts to speak to the glass ceiling of the Garden,
\033[38;2;100;100;175m"You know who I am, Cycle. Your child and I decided to put a stop to this madness."\033[0m
The man looks startled as he notices the masked creature. She starts to speak,
\033[38;2;100;100;100m"Hello, Change. Hello, Cycle. Do I really have to introduce myself again?"\033[0m
A familiar figure appears in front of you three.
\033[38;2;100;200;250m"I am sorry, my child, I have to do this,"\033[0m it says.''')
            enemies = [52, 54]
        enemies = spirits_for_fight_choose(V, enemies)
        print('''Type anything to continue...''')
        action = input()
    else:
        cur_max_power_level = V.max_power_level
        enemies = []
        possible_enemies = []

        for i in range(len(V.enemys_name)):
            if V.enemy_is_boss[i] == True and ((V.area_id in V.enemy_areas[i]) or ("drought" in V.enemy_areas[i] and 9 in V.current_weather)):
                possible_enemies.append(i)
    
        if V.overkill == False:
            while len(possible_enemies) > 0:
                i = choice(possible_enemies)
                if cur_max_power_level - V.enemys_power_level[i] < 0:
                    while i in possible_enemies:
                        possible_enemies.remove(i)
                else:
                    enemies.append(i)
                    cur_max_power_level -= V.enemys_power_level[i]
        else:
            while cur_max_power_level > 0:
                i = choice(possible_enemies)
                enemies.append(i)
                cur_max_power_level -= V.enemys_power_level[i]
        if len(enemies) == 0:
            enemies.append(4)
        spirits_for_fight_choose(V, enemies)
    V.last_boss = enemies.copy()
    return enemies

def ally_choose(V):
    allies = []
    if V.game_mode == "story":
        if V.final_area == True:
            if V.change_recruited == True:
                allies.append(53)
            if V.death_defeated == True:
                allies.append(51)
    return allies

def spirits_for_fight_choose(V, enemies = []):
    if chance(V.vitality_anger - V.spirit_anger_reduction):
        enemies.append(38)
    if chance(V.strength_anger - V.spirit_anger_reduction):
        enemies.append(39)
    if chance(V.protection_anger - V.spirit_anger_reduction):
        enemies.append(41)
    if chance(V.might_anger - V.spirit_anger_reduction):
        enemies.append(40)
    if chance(V.fear_anger - V.spirit_anger_reduction):
        enemies.append(4)
    if chance(V.shopkeeper_deaths * 0.25 - V.spirit_anger_reduction):
        enemies.append(34)
    return enemies



def fight(V, enemy_ids = [0], ally_ids = []):
    V.queue_amount = 0
    V.queue_action = 0
    V.queue_action_enemy = 0
    V.win = 0
    V.lost = 0
    V.money_gain = 0
    V.xp_gain = 0
    V.player_current_hp = V.player_max_hp - round(V.player_max_hp * V.player_hp_penalty)
    V.player_hp_penalty = 0
    V.player_extra_def = - V.player_def_penalty
    V.player_def_penalty = 0
    V.player_extra_magic_def = round(V.player_extra_magic_def_buff * V.player_base_magic_def)
    V.player_current_regen = V.player_regen
    V.player_poisoned = 0
    V.player_current_immortality = V.player_immortality
    V.player_damage_buff = 0
    V.player_crit_chance_buff = 0
    V.player_stunned = 0
    V.enemys = []
    V.allys = []
    enemy_deletions = []
    k = 0
    original_enemy_count = 0

    max_elite_counter = (V.score / 15)
    if max_elite_counter < 1:
        max_elite_counter = 1
    elif max_elite_counter > 5:
        max_elite_counter = 5
    for i in enemy_ids:
        elite_counter = 0
        while chance(0.05 * (V.difficulty / 40)):
            elite_counter += 1
            if elite_counter >= max_elite_counter:
                break
        V.enemys.append(Enemies(V, i, elite=elite_counter))
        k += 1
        original_enemy_count += 1
        if k > 1:
            print("\033[0m and ", end = '')
        print(enemy_name_color(V, i) + V.enemys_name[i], end = '')
    if k > 5:
        print("\033[0m swarm you!")
    elif k > 1:
        print("\033[0m block your way!")
    else:
        print("\033[0m blocks your way!")
    k = 0
    for i in ally_ids:
        V.allys.append(Enemies(V, i))
    while True:
        while True:
            print("\033[33;1mYour stats: ", V.player_current_hp, "/", V.player_max_hp, " HP; ", round(V.player_base_dmg * ((V.player_damage_buff / 100) + 1)), " DMG; ", round(V.player_crit_chance * ((V.player_crit_chance_buff / 100) + 1)), "% CRT; ", V.player_base_def, "+", V.player_extra_def, " DEF", sep = "", end = "")
            if V.player_base_magic_def + V.player_extra_magic_def > 0:
                print("; ", V.player_base_magic_def, "+", V.player_extra_magic_def, " MGCDEF", sep = "", end = "")
            if V.player_poison_def > 0:
                print("; ", V.player_poison_def, " PSNDEF", sep = "", end = "")
            if V.player_regen + V.player_current_regen > 0:
                print("; ", V.player_current_regen, "% REG", sep = "", end = "")
            if V.player_poison > 0:
                print("; ", V.player_poison, " PSN", sep = "", end = "")
            if V.player_spikes > 0:
                print("; ", V.player_spikes, " SPK", sep = "", end = "")
            if V.player_spikes_armor_break > 0:
                print("; ", V.player_spikes_armor_break, " DEFRED", sep = "", end = "")
            if V.player_shield > 0:
                print("; ", V.player_shield, "% SHLD", sep = "", end = "")
            if V.player_magic_shield > 0:
                print("; ", V.player_magic_shield, "% MGCSHLD", sep = "", end = "")
            if V.player_lifesteal > 0:
                print("; ", V.player_lifesteal, "% LFST", sep = "", end = "")
            if V.player_dodge_chance > 0:
                print("; ", V.player_dodge_chance, "% DCH", sep = "", end = "")
            if V.player_poisoned > 0:
                print("; ", V.player_poisoned, " PSN'd", sep = "", end = "")
            if V.player_current_immortality > 0:
                print("\nImpenetrability for ", V.player_current_immortality, " turn(s). Absorbs: ", int(immortality_compute(V) * 100), "% of dealt DMG.", sep = "")

            if len(V.allys) > 0:
                print("\033[31;0m\nStats of your allies:")
                for i in range(len(V.allys)):
                    print(i + 1, ". ", enemy_name_color(V, V.allys[i].en_id) + V.allys[i].name, ": ", V.allys[i].hp, "/", V.allys[i].max_hp, " HP; ", V.allys[i].dmg, " DMG; ", round(V.enemys[i].crit * 100), "% CRT; ", V.allys[i].defense, " DEF", sep = "", end = "")
                    if V.allys[i].spk > 0:
                        print("; ", V.allys[i].spk, " SPK", sep = "", end = "")
                    if V.allys[i].psn > 0:
                        print("; ", V.allys[i].psn, " PSN", sep = "", end = "")
                    if V.allys[i].psnd > 0:
                        print("; ", V.allys[i].psnd, " PSN'd", sep = "", end = "")
                    if V.allys[i].imm > 0:
                        print("; Impenetrable for ", V.allys[i].imm, " turns", sep = "", end = "")
                    print("\033[31;0m")

            print("\033[31;0m\nStats of your enemies:")
            for i in range(len(V.enemys)):
                print(i + 1, ". ", enemy_name_color(V, V.enemys[i].en_id) + V.enemys[i].name, ": ", V.enemys[i].hp, "/", V.enemys[i].max_hp, " HP; ", V.enemys[i].dmg, " DMG; ", round(V.enemys[i].crit * 100), "% CRT; ", V.enemys[i].defense, " DEF", sep = "", end = "")
                if V.enemys[i].spk > 0:
                    print("; ", V.enemys[i].spk, " SPK", sep = "", end = "")
                if V.enemys[i].psn > 0:
                    print("; ", V.enemys[i].psn, " PSN", sep = "", end = "")
                if V.enemys[i].psnd > 0:
                    print("; ", V.enemys[i].psnd, " PSN'd", sep = "", end = "")
                if V.enemys[i].stnd > 0:
                    print("; ", V.enemys[i].stnd, " STN'd", sep = "", end = "")
                if V.enemys[i].imm > 0:
                    print("; Impenetrable for ", V.enemys[i].imm, " turns", sep = "", end = "")
                print("\033[31;0m")
            print()
            if V.player_stunned > 0:
                print("You are stunned! You can't do anything!")
                V.player_stunned -= 1
                break
            elif V.queue_amount > 0:
                V.queue_amount -= 1
                if V.queue_action == 1:
                    player_hit(V, V.queue_action_enemy)
                    break
                elif V.queue_action == 2:
                    if V.player_base_def < 10:
                        V.player_extra_def += 1
                    else:
                        V.player_extra_def += V.player_base_def // 10
                    print("\033[33;1mYou defended! Your defense has increased to", V.player_base_def + V.player_extra_def, "DEF!\033[0m")
                    break
                elif V.queue_action == 5:
                    player_hit(V, -1)
                    break
                elif V.queue_action == 7:
                    print("\033[33;1mYou decided to do absolutely nothing for this turn!\033[0m")
                    break
            else:
                print("What will you do?")
                print("1. Hit")
                print("2. Defend")
                print("3. Inspect")
                print("4. Self Inspect")
                if len(V.enemys) > 1:
                    print("5. Broad Hit")
                print("7. Do Nothing")
                print("8. Items")
                print("9. Queue actions")
                print("10. End It All")
                print("Type in the action")
                action = input()
                if action == '1' or action.lower() == "hit":
                    if len(V.enemys) > 1:
                        print("Choose enemy")
                        for i in range(len(V.enemys)):
                            print(i + 1, ". ", enemy_name_color(V, V.enemys[i].en_id) + V.enemys[i].name, "\033[0m", sep='')
                        hit_action = input()
                        if hit_action.isdigit():
                            hit_action = int(hit_action)
                            if hit_action > 0 and hit_action <= len(V.enemys):
                                player_hit(V, hit_action - 1)
                                break
                    else:
                        player_hit(V, 0)
                        break
                elif action == '2' or action.lower() == "defend":
                    if V.player_base_def < 10:
                        V.player_extra_def += 1
                    else:
                        V.player_extra_def += V.player_base_def // 10
                    print("\033[33;1mYou defended! Your defense has increased to", V.player_base_def + V.player_extra_def, "DEF!\033[0m")
                    break
                elif action == '3' or action.lower() == "inspect":
                    if len(V.enemys) > 1:
                        print("Choose enemy")
                        for i in range(len(V.enemys)):
                            print(i + 1, ". ", enemy_name_color(V, V.enemys[i].en_id) + V.enemys[i].name, "\033[0m", sep='')
                        inspect_action = input()
                        if inspect_action.isdigit():
                            inspect_action = int(inspect_action)
                            if inspect_action > 0 and inspect_action <= len(V.enemys):
                                print(enemy_name_color(V, V.enemys[inspect_action - 1].en_id) + V.enemys[inspect_action - 1].description)
                    else:
                        inspect_action = 1
                        print(enemy_name_color(V, V.enemys[0].en_id) + V.enemys[0].description)
                    print("Elements: ", end = "")
                    if len(V.enemys_elements[V.enemys[inspect_action - 1].en_id]):
                        element_count = 0
                        for i in V.enemys_elements[V.enemys[inspect_action - 1].en_id]:
                            if element_count > 0:
                                print(enemy_name_color(V, V.enemys[0].en_id)+ ", ", end = "")
                            if i == 0:
                                print("\033[38;2;0;255;0mVitality", end = "")
                            elif i == 1:
                                print("\033[38;2;255;0;0mStrength", end = "")
                            elif i == 2:
                                print("\033[38;2;0;200;255mProtection", end = "")
                            elif i == 3:
                                print("\033[38;2;255;128;0mMight", end = "")
                            elif i == 4:
                                print("\033[38;2;190;0;205mInnocence", end = "")
                            elif i == 5:
                                print("\033[38;2;250;250;0mMana", end = "")
                            elif i == 6:
                                print("\033[38;2;0;255;255mMagic Protection", end = "")
                            element_count += 1
                    else:
                        print("\033[0mNone", end = "")
                    print("\033[0m\nType anything to continue...")
                    action = input()
                elif action == '4' or action.lower() == "self inspect":
                    print("\033[33;1mYou concentrate and attempt to remember yourself...\nYour balance is ", V.player_money, " coins\nYour experience is ", V.player_xp, "/", xp_to_lvl_up(V), " XP\nYour level is ", V.player_level, sep = "")
                    if V.player_gold_boost > 0:
                        print("Your coin boost is ", V.player_gold_boost, "%", sep = "")
                    if V.player_crit_chance_reduction != 100:
                        print("Your crit. chance reduction is ", V.player_crit_chance_reduction, "%", sep = "")
                    if V.player_enemy_explotano > 0:
                        print("Enemies explode on death dealing ", V.player_enemy_explotano, "% of their HP", sep = "")
                    if V.player_consume > 0:
                        print("Your consume skill is at ", V.player_consume, "%", sep = "")
                    if V.player_extra_life:
                        print("You have 2 lives")
                    print("Your score is ", V.score, "\nYour power level is ", V.max_power_level, "\033[0m", sep = "")
                    print("\033[0m\nType anything to continue...")
                    action = input()
                elif (action == '5' or action.lower() == "broad hit"):
                    if len(V.enemys) > 1:
                        player_hit(V, -1)
                    elif len(V.enemys) == 1:
                        player_hit(V, 0)
                    break
                elif action == '7' or action.lower() == "do nothing":
                    print("\033[33;1mYou decided to do absolutely nothing for this turn!\033[0m")
                    break
                elif action == '8' or "item" in action.lower():
                    if len(V.player_items) > 0:
                        counter = 0
                        for i in V.player_items:
                            counter += 1
                            print(str(counter) + ".", V.consumable_item_names[i])
                        print("\n1. Use\n2. Inspect")
                        while True:
                            action = input()
                            if action == '1' or action.lower() == "use":
                                print("Which item do you want to use?")
                                use_action = input()
                                if use_action.isdigit():
                                    use_action = int(use_action)
                                    if use_action > 0 and use_action <= len(V.player_items):
                                        item_use(V, V.player_items[use_action - 1])
                                break
                            elif action == '2' or action.lower() == "inspect":
                                print("Which one do you want to inspect?")
                                inspect_action = input()
                                if inspect_action.isdigit():
                                    inspect_action = int(inspect_action)
                                    if inspect_action > 0 and inspect_action <= len(V.player_items):
                                        print(V.consumable_item_desc[V.player_items[inspect_action-1]])
                                break
                    else:
                        print("You have no items!")
                    print("\033[0m\nType anything to continue...")
                    action = input()
                elif action == '9' or "queue" in action.lower() or "action" in action.lower():
                    print("You will repeat the same action a certain amount of times.")
                    print("Choose which action do you want to queue:")
                    print("1. Hit")
                    print("2. Defend")
                    if len(V.enemys) > 1:
                        print("5. Broad Hit")
                    print("7. Do Nothing")
                    action = input()
                    if action == '1' or action.lower() == "hit":
                        V.queue_action = 1
                        if len(V.enemys) > 1:
                            print("Choose enemy")
                            for i in range(len(V.enemys)):
                                print(i + 1, ". ", enemy_name_color(V, V.enemys[i].en_id) + V.enemys[i].name, "\033[0m", sep='')
                            hit_action = input()
                            if hit_action.isdigit():
                                hit_action = int(hit_action)
                                if hit_action > 0 and hit_action <= len(V.enemys):
                                    V.queue_action_enemy = hit_action - 1
                                else:
                                    continue
                            else:
                                continue
                        else:
                            V.queue_action_enemy = 0
                    elif action == '2' or action.lower() == "defend":
                        V.queue_action = 2
                    elif action == '5' or "broad" in action.lower():
                        if len(V.enemys) > 1:
                            V.queue_action = 5
                        else:
                            V.queue_action = 1
                            V.queue_action_enemy = 0
                    elif action == '7' or "nothing" in action.lower():
                        V.queue_action = 7
                    else:
                        continue
                    print("How many times do you want to repeat it?")
                    action = input()
                    if action.isdigit():
                        action = int(action)
                        if action > 0:
                            V.queue_amount = action

                elif action == '10' or "end" in action.lower():
                    print("ARE YOU SURE YOU WANT TO END THE RUN?")
                    print("> No")
                    print("> Yes")
                    action = input()
                    if action.lower() == "yes":
                        V.lost = 1
                        V.player_spent_life = True
                        V.player_extra_life = False
                        V.player_current_hp = 0
                        break

        if V.lost == 1:
            break

        if V.player_current_regen > 0:
            regen = round((V.player_current_regen / 100) * V.player_max_hp)
            if regen + V.player_current_hp > V.player_max_hp:
                regen -= regen + V.player_current_hp - V.player_max_hp 
            V.player_current_hp += regen
            if regen > 0:
                print("\033[33;1mYou regenerated", regen, "HP! You have", V.player_current_hp, "HP left!\033[0m")
                print("\033[33;1mYour REG has been decreased by 1% for this battle!\033[0m")
                V.player_current_regen -= 1
        
        if V.player_poisoned > 0:
            if V.player_poison_def >= V.player_poisoned:
                cur_poisoned = 1
            else:
                cur_poisoned = V.player_poisoned - V.player_poison_def
            V.player_current_hp -= cur_poisoned
            if V.player_current_hp < 0:
                V.player_current_hp = 0
            print("\033[33;1mPoison dealt", cur_poisoned, "DMG to you! You have", V.player_current_hp, "HP left!")

        for i in V.current_weather:
            if i == 6:
                def_decrease = round(V.player_base_def / 50) + 1
                V.player_extra_def -= def_decrease
                print("\033[33;1mYour defense has been decreased by ", def_decrease, "! Your current defense is ", V.player_base_def + V.player_extra_def, " DEF!\033[0m", sep = "")
            if i == 7:
                hp_decrease = round(V.player_max_hp / 100) + 1
                V.player_current_hp -= hp_decrease
                print("\033[33;1mHail dealt", hp_decrease, "DMG! You have", V.player_current_hp, "HP left!\033[0m")

        for i in range(len(V.allys)):
            if V.allys[i].hp <= 0:
                V.allys[i].hp += V.allys[i].max_hp // 10
                if V.allys[i].hp > 0:
                    V.allys[i].hp = V.allys[i].max_hp // 2
                else:
                    continue
            while V.allys[i].pattern[V.allys[i].pattern_action] == 3 and len(V.allys) > original_enemy_count * 1.25:
                V.allys[i].pattern_action += 1
                if V.allys[i].pattern_action >= len(V.allys[i].pattern):
                    V.allys[i].pattern_action = 0
            V.ally_actions[V.allys[i].pattern[V.allys[i].pattern_action]](V, i)
            V.allys[i].pattern_action += 1
            if V.allys[i].defense > (V.allys[i].original_defense + 1) * 1.25:
                while 1 in V.allys[i].pattern:
                    V.allys[i].pattern.remove(1)
            if V.allys[i].pattern_action >= len(V.allys[i].pattern):
                V.allys[i].pattern_action = 0
            if V.allys[i].psnd > 0:
                V.allys[i].hp -= V.allys[i].psnd
            V.allys[i].imm -= 1

        for i in range(len(V.enemys)):
            while V.enemys[i].pattern[V.enemys[i].pattern_action] == 3 and len(V.enemys) > original_enemy_count * 1.25:
                V.enemys[i].pattern_action += 1
                if V.enemys[i].pattern_action >= len(V.enemys[i].pattern):
                    V.enemys[i].pattern_action = 0
            if V.enemys[i].stnd > 0:
                V.enemy_actions[4]()
                V.enemys[i].stnd -= 1
            else:
                V.enemy_actions[V.enemys[i].pattern[V.enemys[i].pattern_action]](V, i)
            V.enemys[i].pattern_action += 1
            if V.enemys[i].defense > (V.enemys[i].original_defense + 1) * 1.25:
                while 1 in V.enemys[i].pattern:
                    V.enemys[i].pattern.remove(1)
            if V.enemys[i].pattern_action >= len(V.enemys[i].pattern):
                V.enemys[i].pattern_action = 0
            if V.enemys[i].psnd > 0:
                V.enemys[i].hp -= V.enemys[i].psnd
                if V.enemys[i].hp <= 0:
                    V.enemys[i].hp = 0
                print(enemy_name_color(V, V.enemys[i].en_id) + V.enemys[i].name, "suffered", V.enemys[i].psnd, "DMG from poison! They have", V.enemys[i].hp, "HP left!\033[0m")
            if V.enemys[i].hp <= 0:
                V.queue_amount = 0
                enemy_deletions.append(V.enemys[i])
            V.enemys[i].imm -= 1
        for i in enemy_deletions:
            if i.spawner[0] == 1:
                spawn = 0
                for k in i.spawner:
                    spawn += 1
                    if spawn > 1:
                        V.enemys.append(Enemies(V, enemy_id = k, summoned = True, summoner_id = V.enemys.index(i)))
            V.money_gain += i.money
            V.xp_gain += i.xp
            if not i.en_id in V.enemy_unconsumable:
                V.player_max_hp += round((V.player_consume / 100) * i.max_hp)
                V.player_base_dmg += round((V.player_consume / 100) * i.dmg)
                V.player_base_def += round((V.player_consume / 100) * i.original_defense)
                V.player_crit_chance += round(V.player_consume * i.crit)
            if V.player_enemy_explotano > 0:
                exploding_damage = round((V.player_enemy_explotano / 100) * i.max_hp)
                if len(V.enemys) - len(enemy_deletions) > 0:
                    exploding_damage //= len(V.enemys) - len(enemy_deletions)
                else:
                    exploding_damage = 0
                for k in V.enemys:
                    if not k in enemy_deletions:
                        k.hp -= exploding_damage
                        if k.hp <= 0:
                            enemy_deletions.append(k)
                if exploding_damage > 0:
                    print(i.name, "exploded and dealt", exploding_damage, "to other enemies.")
            V.enemys.remove(i)
        V.player_current_immortality -= 1
        enemy_deletions = []
        if V.player_current_hp == 0:
            if V.is_boss_battle == False or V.player_extra_life == False:
                V.lost = 1
                break
            else:
                V.player_current_hp = V.player_max_hp
                V.player_extra_life = False
                V.player_spent_life = True
                print("\033[31;3mYou lost one of your lives. But you refuse to die...\033[0m\n\n\n")
        if len(V.enemys) == 0:
            V.win = 1
            break
    if V.lost == 1:
        print("\033[0mYou have lost!\n\n\n")
    elif V.win == 1:
        V.money_gain = round(V.money_gain * (1 + (V.player_gold_boost / 100)))
        V.player_money += V.money_gain
        V.player_xp += V.xp_gain
        V.is_boss_battle = False
        print("\033[0mYou have won! You have earned \033[38;2;200;200;0m", V.money_gain, " coins!\033[0m Your balance is \033[38;2;200;200;0m", V.player_money, " coins!\033[0m You have collected \033[38;2;100;0;200m", V.xp_gain, " XP!\033[0m Your total experience is \033[38;2;100;0;200m", V.player_xp, "/", xp_to_lvl_up(V), "XP!\033[0m\n\n\n", sep = "")
    else:
        print("You have encountered a bug! Notify developer!")
        print("Type anything to continue...")
        action = input()

def player_hit(V, target = 0):

    enemys_deletion = []
    print("\033[33;1m", end = "")
    if target > -1: # Regular Hit
        dealt_damage = round(V.player_base_dmg * (randint(V.weapon_damage_ranges[V.player_weapon][0] + V.player_damage_range_boost, V.weapon_damage_ranges[V.player_weapon][1] + V.player_damage_range_boost) / 100) * ((V.player_damage_buff / 100) + 1))
        cur_crit_chance = V.player_crit_chance * ((V.player_crit_chance_buff / 100) + 1)
        crit_count = 0
        while cur_crit_chance > 0:
            if chance(cur_crit_chance / 100):
                dealt_damage *= 2
                crit_count += 1
            cur_crit_chance -= V.player_crit_chance_reduction
        if V.enemys[target].defense < dealt_damage:
            dealt_damage -= V.enemys[target].defense
        else:
            dealt_damage = 1
        if V.enemys[target].imm > 0:
            dealt_damage = 0
        V.enemys[target].hp -= dealt_damage
        spike_damage = V.enemys[target].spk
        if V.player_lifesteal > 0:
            heal = round(dealt_damage * V.player_lifesteal / 100)
            if heal + V.player_current_hp > V.player_max_hp:
                heal -= heal + V.player_current_hp - V.player_max_hp
            V.player_current_hp += heal
            print("You have healed for", heal, "HP! You have", V.player_current_hp, "HP left!")
        V.player_current_hp -= spike_damage
        if V.player_current_hp < 0:
            V.player_current_hp = 0
        if V.enemys[target].hp > 0:
            print("You hit", V.enemys[target].name, "for", dealt_damage, "DMG! They have", V.enemys[target].hp, "HP left!")
            if spike_damage > 0:
                print(V.enemys[target].name, "'s spikes dealt ", spike_damage, " DMG to you! You have ", V.player_current_hp, " HP left!", sep = "")
            if V.player_poison > 0:
                dealt_poison = round(V.player_poison * V.weapon_poison_factor[V.player_weapon])
            else:
                dealt_poison = 0
            if dealt_poison > 0:
                V.enemys[target].psnd += dealt_poison
                print("You have inflicted ", dealt_poison, " PSN to ", V.enemys[target].name, "! Their total poison is ", V.enemys[target].psnd, " PSN!", sep = "")
        else:
            V.queue_amount = 0
            print("You hit", V.enemys[target].name, "for", dealt_damage, "DMG! You killed them!")
            if spike_damage > 0:
                print(V.enemys[target].name, "'s spikes dealt ", spike_damage, " DMG to you! You have ", V.player_current_hp, " HP left!", sep = "")
            if V.enemys[target].spawner[0] == 1:
                spawn = 0
                for i in V.enemys[target].spawner:
                    spawn += 1
                    if spawn > 1:
                        V.enemys.append(Enemies(V, enemy_id = i, summoned = True, summoner_id = target))
            V.money_gain += V.enemys[target].money
            V.xp_gain += V.enemys[target].xp
            if not V.enemys[target].en_id in V.enemy_unconsumable:
                V.player_max_hp += round((V.player_consume / 100) * V.enemys[target].max_hp)
                V.player_base_dmg += round((V.player_consume / 100) * V.enemys[target].dmg)
                V.player_base_def += round((V.player_consume / 100) * V.enemys[target].defense)
                V.player_crit_chance += round(V.player_consume * V.enemys[target].crit)
            if V.player_enemy_explotano > 0:
                exploding_damage = round((V.player_enemy_explotano / 100) * V.enemys[target].max_hp)
                if len(V.enemys) - 1 != 0:
                    exploding_damage //= len(V.enemys) - 1
                else:
                    exploding_damage = 0
                for k in V.enemys:
                    if not k == V.enemys[target]:
                        k.hp -= exploding_damage
                        if k.hp <= 0:
                            V.enemys_deletion.append(k)
                if exploding_damage > 0:
                    print(V.enemys[target].name, "exploded and dealt", exploding_damage, "to other enemies.")
            V.enemys.remove(V.enemys[target])

    else: # Broad Hit
        dealt_damage = round(V.player_base_dmg * ((V.weapon_damage_ranges[V.player_weapon][1] + V.player_damage_range_boost)  / 100) * ((V.player_damage_buff / 100) + 1) * V.weapon_crowd_factor[V.player_weapon])
        cur_crit_chance = V.player_crit_chance * ((V.player_crit_chance_buff / 100) + 1)
        crit_count = 0
        while cur_crit_chance > 0:
            if chance(cur_crit_chance / 100):
                dealt_damage *= 2
                crit_count += 1
            cur_crit_chance -= V.player_crit_chance_reduction
        dealt_damage = round(dealt_damage / len(V.enemys))
        print("You dealt", end = "")
        jank_code_counter = 0
        enemys_deletion = []
        spike_damage = 0
        for i in V.enemys:
            if jank_code_counter > 0:
                print(",", end = "")
            if i.imm > 0:
                print(" 0 DMG to", i.name, end = "")
            elif i.defense < dealt_damage:
                i.hp -= dealt_damage - i.defense
                print("", dealt_damage - i.defense, "DMG to", i.name, end = "")
            else:
                i.hp -= 1
                print(" 1 DMG to", i.name, end = "")
            if i.hp <= 0:
                enemys_deletion.append(i)
            jank_code_counter += 1
            spike_damage += i.spk
        print("!")
        V.player_current_hp -= spike_damage
        if V.player_current_hp < 0:
            V.player_current_hp = 0
        if spike_damage > 0:
            print("Some of the enemies you've hit had spikes and dealt", spike_damage, "DMG to you! You have", V.player_current_hp, "HP left!")
        if V.player_poison > 0:
            print("Your hit was too inaccurate to inflict poison!")
    for i in enemys_deletion:
        V.queue_amount = 0
        enemy_id = V.enemys.index(i)
        if i.spawner[0] == 1:
            spawn = 0
            for k in i.spawner:
                spawn += 1
                if spawn > 1:
                    V.enemys.append(Enemies(V, enemy_id = k,summoned = True, summoner_id = enemy_id))
        V.money_gain += i.money
        V.xp_gain += i.xp
        if not i.en_id in V.enemy_unconsumable:
            V.player_max_hp += round((V.player_consume / 100) * i.max_hp)
            V.player_base_dmg += round((V.player_consume / 100) * i.dmg)
            V.player_base_def += round((V.player_consume / 100) * i.original_defense)
            V.player_crit_chance += round(V.player_consume * i.crit)
        if V.player_enemy_explotano > 0:
            exploding_damage = round((V.player_enemy_explotano / 100) * i.max_hp)
            if len(V.enemys) - len(enemys_deletion) > 0:
                exploding_damage //= len(V.enemys) - len(enemys_deletion)
            else:
                exploding_damage = 0
            for k in V.enemys:
                if not k in enemys_deletion:
                    k.hp -= exploding_damage
                    if k.hp <= 0:
                        enemys_deletion.append(k)
            if exploding_damage > 0:
                print(i.name, "exploded and dealt", exploding_damage, "to other enemies.")
        V.enemys.remove(i)

    if crit_count == 1:
        print("It was a critical hit!")
    elif crit_count > 1:
        print("You rolled a critical hit", crit_count, "times!")

    print("\033[0m", end = "")

def item_use(V, item):
    print("\033[33;1m", end = "")
    original_item = item
    while item == 3:
        item = randint(0, len(V.consumable_item_names) - 1)
    if item == 0:
        print("This did absolutely nothing!")
    elif item == 1:
        heal = round(0.2 * V.player_max_hp)
        if heal + V.player_current_hp > V.player_max_hp:
            heal = V.player_max_hp - V.player_current_hp
        extra_def = round(0.2 * V.player_base_def)
        V.player_extra_def += extra_def
        V.player_current_hp += heal
        print("You ate a cookie. You regenerated", heal, "HP and gained", extra_def, "defense!")
    elif item == 2:
        V.player_poisoned = 0
        print("You injected antidote. Your PSN'd decreased to 0!")
    elif item == 4:
        heal = round(0.5 * V.player_max_hp)
        if heal + V.player_current_hp > V.player_max_hp:
            heal = V.player_max_hp - V.player_current_hp
        V.player_current_hp += heal
        print("You ate cooked meat. You regenerated", heal, "HP!")
    elif item == 5:
        heal = round(0.05 * V.player_max_hp)
        if heal + V.player_current_hp > V.player_max_hp:
            heal = V.player_max_hp - V.player_current_hp
        for i in V.enemys:
            if i.en_id in [15, 16, 17, 18, 19, 36, 39, 46, 52, 60]:
                V.player_damage_buff += 20
        V.player_current_hp += heal
        print("You drank winter tea. You regenerated ", heal, " HP and your damage is increased by ", V.player_damage_buff, "%!", sep = "")
    elif item == 6:
        V.player_current_hp = V.player_max_hp
        print("You drank a heal potion. You regenerated all of your HP!")
    elif item == 7:
        V.player_damage_buff += 30
        V.player_crit_chance_buff += 100
        print("You drank a berserk's potion. Your damage is increased by ", V.player_damage_buff, "% and your crit chance is increased by ", V.player_crit_chance_buff, "%!", sep = "")
    elif item == 8:
        for i in range(len(V.enemys)):
            V.enemys[i].stnd += 3
        print("You threw stun potion at the enemies, you stunned them for 3 turns!")
    elif item == 9:
        V.player_current_regen += 5
        regen_limit = round(V.player_regen * 1.67)
        if regen_limit < 7:
            regen_limit = 7
        if V.player_current_regen > regen_limit:
            V.player_current_regen = regen_limit
        print("You drank regeneration potion. Your regeneration is increased by 5%! You have ", V.player_current_regen, "% REG!", sep = "")
    if original_item in V.player_items:
        V.player_items.remove(original_item)
    print("\033[0m", end = "")

def evolve(V):
    evo_counter = 0
    seed(V.evolution_seed)
    V.evolution_seed = randint(0, 10000)
    for i in range(len(V.enemys_name)):
        if len(V.enemys_name) >= 1000:
            break
        if i in [4, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 51, 52, 53, 54, 64]:
            continue
        if chance(0.25):
            evo_counter += 1
            for k in range(len(V.bosses_for_areas)):
                if i in V.bosses_for_areas[k]:
                    V.bosses_for_areas[k].append(len(V.enemys_name))
            V.enemys_name.append(V.enemys_name[i] + choice(V.evolution_name_suffix))
            V.enemys_base_hp.append(V.enemys_base_hp[i] + round(V.enemys_base_hp[i] * randint(-5, 15) / 100))
            V.enemys_base_dmg.append(V.enemys_base_dmg[i] + round(V.enemys_base_dmg[i] * randint(-4, 13) / 100))
            V.enemys_base_def.append(V.enemys_base_def[i] + round(V.enemys_base_def[i] * randint(30, 65) / 100))
            V.enemys_base_crit.append(V.enemys_base_crit[i] + uniform(-0.05, 0.1))
            if V.enemys_base_spk[i] > 0:
                spk_add = randint(-1, 2)
            elif chance(0.1):
                spk_add = 1
            else:
                spk_add = 0
            V.enemys_base_spk.append(V.enemys_base_spk[i] + spk_add)
            if V.enemys_base_psn[i] > 0:
                psn_add = randint(-1, 2)
            elif chance(0.1):
                psn_add = 1
            else:
                psn_add = 0
            V.enemys_base_psn.append(V.enemys_base_psn[i] + psn_add)
            V.enemys_base_immortality.append(V.enemys_base_immortality[i])
            V.enemys_power_level.append(round(V.enemys_power_level[i] + (randint(-10, 10) / 100), 2))
            V.enemys_descriptions.append(V.enemys_descriptions[i])
            V.enemys_spawners.append(V.enemys_spawners[i].copy())
            V.enemys_patterns.append(V.enemys_patterns[i].copy())
            V.enemy_is_boss.append(V.enemy_is_boss[i])
            V.enemys_name_colors.append(V.enemys_name_colors[i].copy())
            V.enemys_elements.append(V.enemys_elements[i].copy())
            for k in range(3):
                V.enemys_name_colors[i][k] += randint(-15, 15)
                if V.enemys_name_colors[i][k] > 255:
                    V.enemys_name_colors[i][k] = 255
                elif V.enemys_name_colors[i][k] < 0:
                    V.enemys_name_colors[i][k] = 0

            V.enemy_areas.append(V.enemy_areas[i].copy())
            if 0 in V.enemy_areas[-1] and not 1 in V.enemy_areas[-1]:
                if chance(0.1):
                    V.enemy_areas[-1].append(1)
            if 1 in V.enemy_areas[-1] and not 0 in V.enemy_areas[-1]:
                if chance(0.1):
                    V.enemy_areas[-1].append(0)
            if 1 in V.enemy_areas[-1] and not 2 in V.enemy_areas[-1]:
                if chance(0.1):
                    V.enemy_areas[-1].append(2)
            if 2 in V.enemy_areas[-1] and not 4 in V.enemy_areas[-1]:
                if chance(0.1):
                    V.enemy_areas[-1].append(4)
            if 2 in V.enemy_areas[-1] and not 1 in V.enemy_areas[-1]:
                if chance(0.1):
                    V.enemy_areas[-1].append(1)
            if 4 in V.enemy_areas[-1] and not 5 in V.enemy_areas[-1]:
                if chance(0.1):
                    V.enemy_areas[-1].append(5)
            if 4 in V.enemy_areas[-1] and not 6 in V.enemy_areas[-1]:
                if chance(0.1):
                    V.enemy_areas[-1].append(6)
            if 4 in V.enemy_areas[-1] and not 3 in V.enemy_areas[-1]:
                if chance(0.1):
                    V.enemy_areas[-1].append(3)

    print(evo_counter, "enemies have \033[38;2;255;150;0;3mevolved...\033[0m\n\n\n")