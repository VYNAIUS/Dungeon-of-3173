from reset_functions import true_reset

class V:
    def __init__(self):
        
        # META STATS START
        self.TD_area_unlocks = []
        self.TD_max_raids = []
        self.SM_completed = False
        self.consume_discovered = False
        self.continue_run = False
        self.saved = False
        self.SM_skip = False
        self.RM_areas_cheat = False
        self.V_gamma = 1
        self.bestiary_entries = []
        self.enemies_killed = [0] * 74
        self.reaper_enemy_description_unlocks = [False] * 17
        self.version = "blank"
        self.warning = False

        self.dont_save = ["dont_save", "consume_discovered", "SM_completed", "TD_area_unlocks", "TD_max_raids", "SM_skip", "RM_areas_cheat", "V_gamma",
"bestiary_entries", "enemies_killed", "reaper_enemy_description_unlocks", "warning", "enemy_AIs", "ally_actions", "map_show_UI", "bounty_hunter_name_0",
"bounty_hunter_name_1", "enemys", "enemy_areas", "enemy_is_boss", "enemys_power_level", "enemys_name", "nemys_name_colors", "enemys_elements",
"enemys_charm_immunity", "enemys_base_hp", "enemys_base_dmg", "enemys_base_def", "enemys_base_crit", "enemys_base_spk", "enemys_base_psn",
"enemys_base_immortality", "enemys_descriptions", "enemys_patterns", "enemys_spawners", "enemy_unconsumable", "enemy_unelite", "bosses_for_areas",
"reaper_included_enemys", "reaper_enemy_descriptions", "areas", "areas_colors", "water_colors_0", "water_colors_1", "path_lengths", "height_variaty",
"wall_min_thickness", "turn_right_prob", "turn_down_prob", "turn_left_prob", "turn_up_prob", "area_max_x", "area_max_y", "start_positions",
"area_patterns", "area_pattern_chances", "remnants_spawns", "snow_pile_spawns", "river_prob", "river_thickness", "escape_river_prob", "pond_prob",
"pond_radius", "weathers", "weather_chances", "weathers_durations", "base_vision_ranges", "benefitial_events", "hurtful_events", "neutral_events",
"item_names", "item_base_costs", "item_descriptions", "item_descriptions_mimic", "consumable_item_names", "consumable_item_desc", "weapon_names",
"weapon_damage_ranges", "weapon_descriptions", "weapon_poison_factor", "weapon_crowd_factor"]

        self.show_map_UI = True
        self.game_mode = "story"
        self.difficulty = 55 # suggested 0 - 100
        self.original_difficulty = 55
        self.weather_amount = 1
        self.scaling_style = "blank"
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

        from random import randint
        self.global_seed = randint(0, 10000)
        self.daily_seed = 0

        self.map_seed = 0
        self.enemy_encouter_seed = 0
        self.altar_seed = 0
        self.shop_seed = 0
        self.gamble_seed = 0
        self.remnant_seed = 0
        self.weather_seed = 0
        self.weather_effects_seed = 0
        self.reaper_seed = 0
        self.reaper_reward_seed = 0

        self.area = "None"
        self.area_id = 0
        self.story_mode_area_number = 0
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
        self.player_weapon_wrath = 0

        self.player_boat = False
        self.player_has_boat = False
        self.player_boat_hp = 0
        self.player_items = [0] # 1 - cookie, 2 - antidote, 3 - gambler's drink, 4 - cooked meat, 5 - winter tea, 6 - heal potion, 7 - berserk's potion,
        #8 - stun potion, 9 - regeneration potion, 10 - poison flask, 11 - lifesteal flask, 12 - flask of enemy explotano
        self.player_inventory_weapons = []
        self.player_inventory_weapons_psn = []
        self.player_inventory_weapons_explotano = []
        self.player_inventory_weapons_lifesteal = []
        self.player_inventory_weapons_wrath = []

        self.mimic_got_item = False
        self.mimic_gamble_encounters = 0
        self.debt = 0
        self.shopkeeper_sus = 0 # in decimals
        self.shopkeeper_deaths = 0
        self.alchemist_anger = 0 # in decimals
        self.alchemist_defeated = 0
        self.alchemist_visited = False
        self.bought_from_alchemist = False
        self.cur_shopkeeper_dead = False
        self.death_encounters = 0
        self.death_defeated = False
        self.change_encounters = 0
        self.change_recruited = False
        self.brewery_encounters = 0
        self.bank_locked = False
        self.bank_first_time = True
        self.mimic_bank_encounters = 0
        self.bank_money = 0
        self.locking_tutorial = False
        self.reaper_trust = 0
        self.reaper_encounters = 0
        self.bounty_target = []
        self.bounty_target_tracking = []
        self.bounty_target_goal = []

        self.said_dialogue_shopkeeper = []
        self.said_dialogue_gamble_mimic = []
        self.said_dialogue_bank_mimic = []
        self.said_dialogue_boat_person = []
        self.said_dialogue_alchemist = []
        self.said_dialogue_change = []
        self.said_dialogue_reaper = []

        self.vitality_anger = 0 # in decimals
        self.strength_anger = 0 # in decimals
        self.might_anger = 0 # in decimals
        self.protection_anger = 0 # in decimals
        self.fear_anger = 0 # in decimals
        self.spirit_anger_reduction = 0
        # PLAYER STATS END

        # SHOP ITEMS START
        self.item_names = ["Nothing", "Poison Flask", "Armor Spikes", "Flask of Lifesteal", "Bottle of Midas' power", "Bottle of Impenetrability", "Mark of the Undead", "Consume",
                      "Traveller's Hallow", "Flask of Enemy Explotano", "Life's Gift", "Cookie", "Antidote", "Gambler's Drink", "Cooked Meat", "Winter Tea", "Band of Agility",
                      "Heal Potion", "Berserk's Potion", "Stun Potion", "Regeneration Potion", "Trusty Sword", "Magic Wand", "Double Daggers", "Great Hammer", "Syringe",
                      "Flask of Wrath", "Charming Potion", "Reaper's Scythe", "Shield"]
        self.item_base_costs = [0, 20, 20, 40, 30, 70, 60, 100, 25, 40, 100, 23, 27, 30, 30, 25, 40, 50, 42, 52, 58, 45, 20, 60, 55, 75, 30, 50, 75, 40]
        self.item_bought = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.item_descriptions = ["It is literally nothing", "Allows sharp weapons to inflict poison onto your enemies (weapon upgrade)", "Enemies will get damaged when hit you",
                             "Dealing damage will heal you (weapon upgrade)", "More coins will be dropped", "You will be immortal for a turn", "You will regenerate health every turn",
                             "Kill to grow", "You will get experience for entering a new area", "Enemies explode on death, dealing damage to other enemies (weapon upgrade)",
                             "If you die, you will be revived with no money or experience", "Heals 20% HP and adds 20% of base DEF on use (consumable)",
                             "Clears any poison applied to you on use (consumable)", "Shapeshifts into a random consumable object on use (consumable)",
                             "Heals 50% HP on use (consumable)", "Increases damage by 50% if snow-related enemies are present (consumable)", "Grants chance to dodge physical attacks",
                             "Heals 100% HP on use (consumable)", "Increases damage by 30% and doubles crit chance (consumable)", "Stuns enemies for 3 turns (consumable)",
                             "Adds 5% REG on use (consumable)", "Your favourite weapon of all time. Damage ranges between 80%~120%. Crowd factor is 1; poison factor is 1.",
                             "Extremely weak weapon, but provides 150% MGCDEF and deals 500% more DMG to magic enemies. Damage ranges between 50%~80%. Crowd factor is 1; poison factor is 0.2",
                             "Very sharp weapon, which can be used to strike enemies twice. Damage ranges between 45%~75%. Crowd factor is 0.5; poison factor is 1",
                             "Decent crowd control weapon. Damage ranges between 70%~150%. Crowd factor is 3; poison factor is 0.2",
                             "Infinitely weak weapon on its own, but very good at injecting poison. Damage ranges between 5%~10%. Crowd factor is 0.1; posion factor is 4",
                             "Increases the damage and critical chance with the amount of enemies (weapon upgrade)", "Makes an enemy fight for you for a battle (consumable)",
                             "Sharp weapon, that forces killed enemies' souls to fight for you. Damage ranges between 100%~120%. Crowd factor is 0.6; poison factor is 0.95",
                             "Shield men's weapon that uses DEF as a counter attack. Damage ranges betwen 10%~30%. Crowd factor is 0.9; poison factor is 0.1"]
        self.item_descriptions_mimic = ["It's literally nothing, pal", "This thing kills stuff over time", "Guys that attack you, will get damaged for doing so", "Turn damage into heal!",
                                   "Not sure why I don't use this one myself, but you will gain more money", "You will become untouchable, but that will fade away after a turn",
                                   "How do you think undead people live? They use this to regenerate",
                                   "Oh, I don't know about this one, pal. When you kill something, you take part of their powers", "Do a world tour and become more experienced!",
                                   "Enemies go boom and make other enemies go 'ouch'. Does that sound convincing?", "Another life, pal. But you will be revived broke and unexperienced",
                                   "They say that if you eat this, you will regenerate and stuff. But I can't test it myself, pal",
                                   "Don't you hate being poisoned? Well, this will help with getting rid of it, pal!", "This one is like me! Try to drink it and it turns into something random!",
                                   "Ever-warriors, like you, enjoy eating flesh. I believe it heals half of your health, pal",
                                   "After drinking this tea, you will become stronger if snow enemies are there to witness it", "You will be so quick, that you have a chance to dodge stuff, pal",
                                   "This potion heals all of your wounds, pal", "You become stronger and mightier when you drink this", "Bad guys will do nothing 3 times in a row",
                                   "This potion gives a regen boost! It's quite strong, pal", "The weapon that ever-warriors get in the beginning of their life, pal",
                                   "This wand seems to give you a lot of magic protection and is extremely good against mana guys, pal", "These daggers can be used seperately, pal!",
                                   "This thing can smash multiple bad guys at once, pal!", "I think, this thing poisons enemies very efficiently, but it seems to be very weak on its own",
                                   "This thing makes your weapon deal more, the more enemies you have! Isn't that cool, pal?",
                                   "This thing makes some bad guys like you, and forces them to help you. Neat",
                                   "Pal, I'll be honest. I have no idea how this weapon, that can reap souls got in my possesion",
                                   "This legendary weapon is able to use your defense as offense! Ain't that cool?"]
        self.consumable_item_names = ["Nothing", "Cookie", "Antidote", "Gambler's Drink", "Cooked Meat", "Winter Tea", "Heal Potion", "Berserk's Potion", "Stun Potion",
                                 "Regeneration Potion", "Poison Flask", "FLask of Lifesteal", "Flask of Enemy Explotano", "Flask of Wrath", "Charming Potion"]
        self.consumable_item_desc = ["How in the world do you have a Nothing in your inventory?", "Heals 20% HP and adds 20% of base DEF on use (consumable)",
                                "Clears any poison applied to you on use (consumable)", "Shapeshifts into a random consumable object on use (consumable)",
                                "Heals 50% HP on use (consumable)", "Increases damage if snow-related enemies are present", "Heals 100% HP (consumable)",
                                "Increases damge by 30% and doubles crit chance (consumable)", "Stuns enemies for 3 turns (consumable)",
                                "Adds 5% REG on use (consumable)", "Allows sharp weapons to inflict poison onto your enemies (weapon upgrade)",
                                "Dealing damage will heal you (weapon upgrade)", "Enemies explode on death, dealing damage to other enemies (weapon upgrade)",
                                "Increases the damage and critical chance with the amount of enemies (weapon upgrade)",
                                "Makes an enemy fight for you for a battle (consumable)"]
        # SHOP ITEMS END

        # WEAPONS START
        self.weapon_names = ["Trusty Sword", "Magic Wand", "Double Daggers", "Great Hammer", "Syringe", "Reaper's Scythe", "Shield"]
        self.weapon_damage_ranges = [[80, 120], [50, 80], [45, 75], [90, 120], [5, 10], [100, 120], [10, 30]]
        self.weapon_descriptions = ["Your favourite weapon of all time. Damage ranges between 80%~120%. Crowd factor is 1; poison factor is 1.",
                               "Extremely weak weapon, but provides 150% MGCDEF and deals 500% more DMG to magic enemies. Damage ranges between 50%~80%. Crowd factor is 1; poison factor is 0.2",
                               "Very sharp weapon, which can be used to strike enemies twice. Damage ranges between 45%~75%. Crowd factor is 0.5; poison factor is 1",
                               "Decent crowd control weapon. Damage ranges between 70%~150%. Crowd factor is 3; poison factor is 0.2",
                               "Infinitely weak weapon on its own, but very good at injecting poison. Damage ranges between 5%~10%. Crowd factor is 0.1; posion factor is 4"
                               "Sharp weapon, that forces killed enemies' souls to fight for you. Damage ranges between 100%~120%. Crowd factor is 0.6; poison factor is 0.95",
                               "Shield men's weapon that uses DEF as a counter attack. Damage ranges betwen 10%~30%. Crowd factor is 0.9; poison factor is 0.2"]
        self.weapon_poison_factor = [1, 0.2, 1, 0.2, 4, 0.95, 0.2]
        self.weapon_crowd_factor = [1, 1, 0.5, 3, 0.1, 0.6, 0.9]
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
        self.events = [] # 0 - path, 1 - fight, 2 - altar, 3 - shop, 4 - bossfight, 5 - mimic gamble, 6 - muddy path, 7 - small snow pile, 8 - big snow pile,
        # 9 - non-existent snow pile, 10 - deep water, 11 - boat person, 12 - extra exit, 13 - weird story mode man, 14 - remnants, 15 - crystal path,
        # 16 - main exit, 17 - crystal fight, 18 - crystal altar, 19 - mimic bank, 20 - stalker, 21 - hole down, 22 - hole up, 23 - bounty hunting guy, 
        # 24 - alchemist's brewery, 25 - raid deactivated fight, 26 - raid deactivated altar, 27 - raid deactivated crystal fight, 
        # 28 - raid deactivated crystal altar
        self.benefitial_events = []
        self.hurtful_events = []
        self.neutral_events = []
        self.events_coordinates = []
        self.events_heights = []
        self.player_coordinates = [0, 0, 0] # [x, y, l]
        self.map_complexity = 0
        self.game_time = 0
        self.vision_range = 0 # -1 - entire map is visible
        self.escape_amount = False
        self.earth_cannot_generate_tiles = False

        self.player_hp_penalty = 0
        self.player_def_penalty = 0
        self.stalker_stealth = 100
        self.no_update_coordinates = []
        self.player_oxygen_danger = False
        # AREA STATS END

        # ENEMYS STATS START
        self.enemys = []
        self.fight_turn = 0
        self.original_enemy_count = 0

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
        
        self.ally_actions = []
        self.enemy_unconsumable = []
        self.enemy_unelite = []
        self.bosses_for_areas = []
        self.hunters_appeared = []
        self.reaper_included_enemys = []
        self.bestiary_order = []
        # ENEMYS STATS END
        true_reset(self)

        import os
        import sys
        def turn_text_into_list(text, deletion_needed = True):
            if deletion_needed:
                text = text[1:]
            the_list = []
            value = ''''''
            string_type = ""
            is_string = False
            is_list = 0
            for char in text:
                if is_list == 0:
                    if char == "'":
                        if is_string == False:
                            is_string = True
                            string_type = "'"
                            continue
                        else:
                            if string_type == "'":
                                is_string = False
                                string_type = ""
                                continue
                    elif char == '"':
                        if is_string == False:
                            is_string = True
                            string_type = '"'
                            continue
                        else:
                            if string_type == '"':
                                is_string = False
                                string_type = ""
                                continue
                    elif char == " ":
                        if is_string == False:
                            continue
                    elif char == "[":
                        if is_string == False:
                            is_list += 1
                            continue
                    elif char in [",", "]"]:
                        if is_string == False:
                            if isinstance(value, list):
                                pass
                            elif value.replace("-", "").isdigit():
                                value = int(value)
                            elif value.replace("-", "").replace(".", "").isdigit():
                                value = float(value)
                            elif value == "False":
                                value = False
                            elif value == "True":
                                value = True
                            if value != "":
                                the_list.append(value)
                            value = ''''''
                            string_type = ""
                            is_string = False
                            is_list = 0
                            continue
                    value = value + char
                elif char == "[":
                    is_list += 1
                    value = value + char
                elif char == "]":
                    is_list -= 1
                    value = value + char
                    if is_list == 0:
                        value = turn_text_into_list(value, False)
                else:
                    value = value + char
            return the_list

        def turn_text_into_stuff(text):
            if "[" in text:
                value = turn_text_into_list(text)
            elif text.replace("-", "").isdigit():
                value = int(text)
            elif text.replace(".", "").replace("-", "").isdigit():
                value = float(text)
            elif text == "False":
                value = False
            elif text == "True":
                value = True
            else:
                value = text
            return value

        # Gets the current user's LocalLow directory
        save_directory_path = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'DungeonOf3173')
        # This path is user-specific and will automatically adapt to whoever is running the script
        #THANKS CHAT GPT!!!!!11
        os.makedirs(save_directory_path, exist_ok=True)
        self.meta_save_file_path = os.path.join(save_directory_path, 'save.txt')
        self.run_save_file_path = os.path.join(save_directory_path, 'run_save.txt')
        if os.path.exists(self.meta_save_file_path):
            pass
        else:
            with open(self.meta_save_file_path, 'w') as file:
                file.write('''consume_discovered: False
SM_completed: False
TD_unlocks: [True, True, False, False, False, False, False]
TD_high_scores: [0, 0, 0, 0, 0, 0, 0]
SM_skip: False
RM_areas_cheat: False
V_gamma: 1
bestiary_entires: []''')
            print("New save file has been created!")
        data = {}
        with open(self.meta_save_file_path, 'r') as file:
            for line in file:
                try:
                    key, value = line.strip().split(': ', 1)
                    data[key] = value
                except:
                    break
        for key, value in data.items():
            value = turn_text_into_stuff(value)
            setattr(self, key, value)
        for var in self.TD_area_unlocks:
            if not var in [True, False]:
                self.TD_area_unlocks = []
                break
        for var in self.TD_max_raids:
            if not var in [True, False]:
                self.TD_max_raids = []
                break
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

        if os.path.exists(self.run_save_file_path):
            print("A saved run has been detected!")
            data = {}
            with open(self.run_save_file_path, 'r') as file:
                for line in file:
                    key, value = line.strip().split(': ', 1)
                    data[key] = value
            for key, value in data.items():
                value = turn_text_into_stuff(value)
                setattr(self, key, value)
            self.continue_run = True
            while len(self.item_bought) < len(self.item_names):
                self.item_bought.append(0)

            if self.version != "V0.3.7":
                if not self.version in ["blank", "V0.3.6", "V0.3.6.1", "V0.3.7"]:
                    self.warning = True
                if self.version in ["blank", "V0.3.6", "V0.3.6.1"]:
                    self.scaling_style = "legacy"
                    print("Set scaling style to legacy")
                with open(self.run_save_file_path, 'w') as file:
                    for key, value in self.__dict__.items():
                        if key in self.dont_save:
                            continue
                        file.write(f"{key}: {value}\n")

                true_reset(self)
                        
                if os.path.exists(self.run_save_file_path):
                    print("Opening a new format of saved run!")
                    data = {}
                    with open(self.run_save_file_path, 'r') as file:
                        for line in file:
                            key, value = line.strip().split(': ', 1)
                            data[key] = value
                    for key, value in data.items():
                        value = turn_text_into_stuff(value)
                        setattr(self, key, value)
                    self.continue_run = True
                    while len(self.item_bought) < len(self.item_names):
                        self.item_bought.append(0)

        self.saved = False
        self.version = "V0.3.7"

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

    def save_run(self):
        with open(self.run_save_file_path, 'w') as file:
            for key, value in self.__dict__.items():
                if key in self.dont_save:
                    continue
                file.write(f"{key}: {value}\n")
        self.saved = True

    def delete_run(self):
        import os
        if os.path.exists(self.run_save_file_path):
            os.remove(self.run_save_file_path)