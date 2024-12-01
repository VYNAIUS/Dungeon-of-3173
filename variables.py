class V:
    def __init__(self):
        
        # META STATS START
        self.TD_area_unlocks = []
        self.TD_max_raids = []

        self.game_mode = "story"
        self.difficulty = 55 # suggested 0 - 100
        self.original_difficulty = 55
        self.evolution = False
        self.overkill = False
        self.speedrunner = False
        self.speed_timer = 0
        self.item_rando = False
        self.eclipse = False
        self.area_rando = False
        self.weather_amount = 1
        self.score_increase = 0
        self.score = 0
        self.raid_counter = 0
        self.max_power_level = 1
        self.max_power_level_increase = 0
        self.win = 0
        self.lost = 0
        self.forest_enemy_spawn = 0
        self.enough_destroyed = False
        self.is_boss_battle = False
        self.final_area = False

        self.queue_amount = 0
        self.queue_action = 0
        self.queue_action_enemy = 0

        self.global_seed = 0
        self.daily_seed = 0

        self.map_seed = 0
        self.enemy_encouter_seed = 0
        self.evolution_seed = 0
        self.altar_seed = 0
        self.shop_seed = 0
        self.gamble_seed = 0
        self.remnant_seed = 0
        self.weather_seed = 0
        self.weather_effects_seed = 0

        self.area = "None"
        self.area_id = 0
        # META STATS END

        # PLAYER STATS START
        self.allys = []

        self.player_money = 0 # <
        self.player_xp = 0
        self.player_level = 0

        self.player_max_hp = 100
        self.player_current_hp = self.player_max_hp 
        self.player_base_dmg = 5
        self.player_weapon = 0
        self.player_base_def = 0
        self.player_extra_def = 0
        self.player_base_magic_def = 0
        self.player_extra_magic_def = 0
        self.player_extra_magic_def_buff = 0
        self.player_crit_chance = 5  # in %
        self.player_poison = 0
        self.player_poisoned = 0
        self.player_spikes = 0
        self.player_stunned = 0
        self.last_altar = []

        self.player_shield = 0 # in %
        self.player_magic_shield = 0 # in %
        self.player_gold_boost = 0 # in %
        self.player_damage_range_boost = 0 # in %
        self.player_poison_def = 0
        self.player_spikes_armor_break = 0
        self.player_crit_chance_reduction = 100 # in %
        self.last_boss = []

        self.player_lifesteal = 0 # in %
        self.player_immortality = 0 # in turns
        self.player_current_immortality = self.player_immortality
        self.player_regen = 0
        self.player_current_regen = 0
        self.player_consume = 0
        self.player_travel = 0
        self.player_enemy_explotano = 0
        self.player_extra_life = False
        self.player_spent_life = 0
        self.player_dodge_chance = 0
        self.player_dodge_count = 0
        self.player_dodged = False

        self.player_boat = False
        self.player_items = [0] # 1 - cookie, 2 - antidote, 3 - gambler's drink, 4 - cooked meat, 5 - winter tea, 6 - heal potion, 7 - berserk's potion, 8 - stun potion

        self.mimic_got_item = False
        self.mimic_gamble_encounters = 0
        self.debt = 0
        self.shopkeeper_sus = 0 # in decimals
        self.shopkeeper_deaths = 0
        self.alchemist_anger = 0
        self.alchemist_defeated = 0
        self.alchemist_visited = False
        self.bought_from_alchemist = False
        self.cur_shopkeeper_dead = False
        self.death_encounters = 0
        self.death_defeated = False
        self.change_encouters = 0
        self.change_recruited = False
        self.brewery_encouters = 0
        self.bank_locked = False
        self.bank_first_time = True
        self.mimic_bank_encouters = 0
        self.bank_money = 0
        self.locking_tutorial = False

        self.vitality_anger = 0 # in decimals
        self.strength_anger = 0 # in decimals
        self.might_anger = 0 # in decimals
        self.protection_anger = 0 # in decimals
        self.fear_anger = 0 # in decimals
        self.spirit_anger_reduction = 0
        # PLAYER STATS END

        # SHOP ITEMS START
        self.item_names = ["Nothing", "Poison Flask", "Armor Spikes", "Bottle of Lifesteal", "Bottle of Midas' power", "Bottle of Impenetrability", "Mark of the Undead", "Consume",
                      "Traveller's Hallow", "Enemy Explotano", "Life's Gift", "Cookie", "Antidote", "Gambler's Drink", "Cooked Meat", "Winter Tea", "Band of Agility",
                      "Heal Potion", "Berserk's Potion", "Stun Potion", "Regeneration Potion"]
        self.item_base_costs = [0, 20, 20, 40, 30, 70, 60, 100, 25, 40, 100, 23, 27, 30, 30, 25, 40, 50, 42, 52, 58]
        self.item_bought = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.item_descriptions = ["It is literally nothing", "Allows sharp weapons to inflict poison onto your enemies", "Enemies will get damaged when hit you",
                             "Dealing damage will heal you", "More coins will be dropped", "You will be immortal for a turn", "You will regenerate health every turn", "Kill to grow",
                             "You will get experience for entering a new area", "Enemies explode on death, dealing damage to other enemies",
                             "If you die, you will be revived with no money or experience", "Heals 20% HP and adds 20% of base DEF on use (consumable)",
                             "Clears any poison applied to you on use (consumable)", "Shapeshifts into a random consumable object on use (consumable)",
                             "Heals 50% HP on use (consumable)", "Increases damage by 50% if snow-related enemies are present (consumable)", "Grants chance to dodge physical attacks",
                             "Heals 100% HP on use (consumable)", "Increases damage by 30% and doubles crit chance (consumable)", "Stuns enemies for 3 turns (consumable)",
                             "Adds 5% REG on use (consumable)"]
        self.item_descriptions_mimic = ["It's literally nothing, pal", "This thing kills stuff over time", "Guys that attack you, will get damaged for doing so", "Turn damage into heal!",
                                   "Not sure why I don't use this one myself, but you will gain more money", "You will become untouchable, but that will fade away after a turn",
                                   "How do you think undead people live? They use this to regenerate",
                                   "Oh, I don't know about this one, pal. When you kill something, you take part of their powers", "Do a world tour and become more experienced!",
                                   "Enemies go boom and make other enemies go 'ouch'. Does that sound convincing?", "Another life, pal. But you will be revived broke and unexpirienced",
                                   "They say that if you eat this, you will regenerate and stuff. But I can't test it myself, pal",
                                   "Don't you hate being poisoned? Well, this will help with getting rid of it, pal!", "This one is like me! Try to drink it and it turns into something random!",
                                   "Ever-warriors, like you, enjoy eating flesh. I believe it heals half of your health, pal",
                                   "After drinking this tea, you will become stronger if snow enemies are there to witness it", "You will be so quick, that you have a chance to dodge stuff, pal",
                                   "This potion heals all of your wounds, pal", "You become stronger and mightier when you drink this", "Bad guys will do nothing 3 times in a row",
                                   "This potion gives a regen boost! It's quite strong, pal"]
        self.consumable_item_names = ["Nothing", "Cookie", "Antidote", "Gambler's Drink", "Cooked Meat", "Winter Tea", "Heal Potion", "Berserk's Potion", "Stun Potion",
                                 "Regeneration Potion"]
        self.consumable_item_desc = ["How in the world do you have a Nothing in your inventory?", "Heals 20% HP and adds 20% of base DEF on use (consumable)",
                                "Clears any poison applied to you on use (consumable)", "Shapeshifts into a random consumable object on use (consumable)",
                                "Heals 50% HP on use (consumable)", "Increases damage if snow-related enemies are present", "Heals 100% HP (consumable)",
                                "Increases damge by 30% and doubles crit chance (consumable)", "Stuns enemies for 3 turns (consumable)",
                                "Adds 5% REG on use (consumable)"]
        # SHOP ITEMS END

        # WEAPONS START
        self.weapon_names = ["Trusty Sword", "Magic Wand", "Double Daggers", "Great Hammer", "Syringe"]
        self.weapon_damage_ranges = [[80, 120], [50, 80], [95, 135], [90, 120], [5, 10]]
        self.weapon_descriptions = ["Your favourite weapon of all time. Damage ranges between 80%~120%. Crowd factor is 1; poison factor is 1.",
                               "Extremely weak weapon, but provides 150% MGCDEF. Damage ranges between 50%~80%. Crowd factor is 1; poison factor is 0.2",
                               "Very sharp weapon, which makes deep cuts. Damage ranges between 95%~135%. Crowd factor is 0.5; poison factor is 1.7",
                               "Decent crowd control weapon. Damage ranges between 70%~150%. Crowd factor is 3; poison factor is 0.2",
                               "Infinitely weak weapon on its own, but very good at injecting poison. Damage ranges between 5%~10%. Crowd factor is 0.1; posion factor is 4"]
        self.weapon_poison_factor = [1, 0.2, 1.7, 0.2, 4]
        self.weapon_crowd_factor = [1, 1, 0.5, 3, 0.1]
        self.weapon_base_costs = [45, 20, 60, 55, 75]
        # WEAPONS END

        # AREA STATS START
        self.areas = []
        self.areas_colors = []
        self.water_colors_0 = []
        self.water_colors_1 = []
        self.path_lengths = []
        self.height_variaty = []
        self.wall_min_thickness = []
        self.turn_right_prob = []
        self.turn_down_prob = []
        self.turn_left_prob = []
        self.turn_up_prob = []
        self.area_max_x = []
        self.area_max_y = []
        self.start_positions = []
        self.area_patterns = []
        self.area_pattern_chances = []
        self.remnants_spawns = []
        self.snow_pile_spawns = []
        self.water_level = 0
        self.default_water_levels = []
        self.river_prob = []
        self.river_thickness = []
        self.escape_river_prob = []
        self.pond_prob = []
        self.pond_radius = []
        self.weathers = []
        self.weather_chances = []
        self.weathers_durations = []
        self.base_vision_ranges = []
        self.current_weather = []
        self.current_weather_duration = []
        self.events = [] # 0 - path, 1 - fight, 2 - altar, 3 - shop, 4 - bossfight, 5 - mim[escapedic gamble, 6 - muddy path, 7 - small snow pile, 8 - big snow pile, 9 - non-existent snow pile,
        # 10 - deep water, 11 - boat person, 12 - extra exit, 13 - weird story mode man, 14 - remnants, 15 - crystal path, 16 - inactive crystal path, 17 - pre crystal path,
        # 18 - pre crystal fight, 19 - crystal fight, 20 - inactive crystal fight, 21 - pre crystal altar, 22 - crystal altar, 23 - inactive crystal altar, 24 - alchemist's brewery,
        # 25 - raid deactivated fight, 26 - raid deactivated altar, 27 - raid deactivated crystal fight, 28 - raid deactivated crystal altar 29 - hole (down), 30 - hole (up)
        # 31 - mimic bank, 32 - stalker
        self.benefitial_events = []
        self.hurtful_events = []
        self.neutral_events = []
        self.events_coordinates = []
        self.events_heights = []
        self.player_coordinates = [0, 0, 0] # [x, y, l]
        self.map_complexity = 0
        self.game_time = 0
        self.vision_range = 0 # -1 - entire map is visible
        self.escaped = False
        self.earth_cannot_generate_tiles = False

        self.player_hp_penalty = 0
        self.player_def_penalty = 0
        self.stalker_stealth = 100
        self.player_oxygen_danger = False
        # AREA STATS END

        # ENEMYS STATS START
        self.bounty_hunter_name_0 = []
        self.bounty_hunter_name_1 = []
        self.evolution_name_suffix = []
        self.enemys = []

        self.enemy_areas = []
        self.enemy_is_boss = []
        self.enemys_power_level = []
        self.enemys_name = []
        self.enemys_name_colors = []
        self.enemys_elements = []
        self.enemys_base_hp = []
        self.enemys_base_dmg = []
        self.enemys_base_def = []
        self.enemys_base_crit = []
        self.enemys_base_spk = []
        self.enemys_base_psn = []
        self.enemys_base_immortality = []
        self.enemys_descriptions = []
        self.enemys_patterns = []
        self.enemys_spawners = []

        self.enemy_actions = []
        self.ally_actions = []
        self.enemy_unconsumable = []
        self.enemy_unelite = []
        self.bosses_for_areas = []
        self.hunters_appeared = []
        # ENEMYS STATS END


        import os
        import sys
        # Gets the current user's LocalLow directory
        save_directory_path = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'DungeonOf3173')
        # This path is user-specific and will automatically adapt to whoever is running the script
        #THANKS CHAT GPT!!!!!11
        os.makedirs(save_directory_path, exist_ok=True)
        self.file_path = os.path.join(save_directory_path, 'save.txt')
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                content = file.read()
        else:
            with open(self.file_path, 'w') as file:
                file.write('''TD_unlocks=[1100000]
        TD_high_scores=[0000000]''')
            print("New save file has been created!")
        with open(self.file_path, 'r') as file:
            content = file.read()

        starting_symbol = 0
        for starting_symbol in range(len(content)):
            for symbol in range(len(content)):
                key_word = content[starting_symbol:symbol]
                if key_word == "TD_unlocks":
                    print("Scanning Raid Mode areas unlocks")
                    area_counter = 0
                    for i in range(symbol, len(content)):
                        if content[i] == "]" or area_counter == 7:
                            break
                        elif content[i] == "1":
                            self.TD_area_unlocks.append(True)
                            area_counter += 1
                        elif content[i] == "0":
                            self.TD_area_unlocks.append(False)
                            area_counter += 1
                if key_word == "TD_high_scores":
                    print("Scanning Raid Mode high scores")
                    area_counter = 0
                    for i in range(symbol, len(content)):
                        if content[i] == "]" or area_counter == 7:
                            break
                        elif content[i].isdigit():
                            self.TD_max_raids.append(int(content[i]))
                            area_counter += 1
        #print(TD_area_unlocks)
        fancy_percentage_save_file_thing = 0
        while len(self.TD_area_unlocks) < 7:
            fancy_percentage_save_file_thing += 1
            if len(self.TD_area_unlocks) < 2:
                self.TD_area_unlocks.append(True)
            else:
                self.TD_area_unlocks.append(False)
            print("Restoring a corrupt save file - ", round(fancy_percentage_save_file_thing / 14 * 100), "%", sep = "")
        while len(self.TD_max_raids) < 7:
            fancy_percentage_save_file_thing += 1
            self.TD_max_raids.append(0)
            print("Restoring a corrupt save file - ", round(fancy_percentage_save_file_thing / 14 * 100), "%", sep = "")
        print("\n\n\n")
        import subprocess
        def enable_ansi_escape_codes():
            try:
                # Run the PowerShell command to enable ANSI escape codes
                subprocess.run(
                    ["powershell", "-Command", "Set-ItemProperty -Path 'HKCU:\\Console' -Name 'VirtualTerminalLevel' -Value 1"],
                    check=True
                )
                #print("ANSI escape codes enabled successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to enable ANSI escape codes: {e}")

        if __name__ == "__main__":
            enable_ansi_escape_codes()
        sys.set_int_max_str_digits(6969)