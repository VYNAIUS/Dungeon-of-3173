
from random import choice, choices, randint, uniform, seed, shuffle
from time import localtime

import variables
from coloring import *
from reset_functions import *
from extra_functions import *
from enemies_and_fighting import *
from areas import *
from circular_avoidance import *
from misc_functions import *
from shops import *
from upgrades_functions import *

print("V0.3.4")
V = variables.V()
V.enemy_AIs = [fight_AI_basic_0, fight_AI_basic_1, fight_AI_basic_2, fight_AI_magic_1, fight_AI_magic_2, fight_AI_magic_basic_2,
               fight_AI_summoner_magic_1, fight_AI_summoner_basic_lazy_1, fight_AI_basic_lazy_1, fight_AI_healer_magic_1,
               fight_AI_healer_magic_basic_1, fight_AI_transform_basic_1, fight_AI_transform_summoner_basic_2, fight_AI_basic_defend,
               fight_AI_basic_shotgunner, fight_AI_stalker, fight_AI_alchemist, fight_AI_3173, fight_AI_cycle]

def infinite_mode():
    if V.continue_run == False:
        print('''\033[38;2;100;200;250m"My child, defeat your enemies, consume power, and acquire strength."
"Survive for as long as you can..."\033[0m
Type anything to continue...''')
        action = input()
        V.game_mode = "infinite"
        V.area_id = 0
        V.areas_visited = 0
    while True:
        if V.continue_run == False:
            V.default_water_levels[6] = 0.75
            V.earth_cannot_generate_tiles = False
            V.vision_range = V.base_vision_ranges[V.area_id]
            if V.areas_visited > 7:
                V.difficulty += 10
            for k in range(len(V.hunters_appeared)):
                V.hunters_appeared[k] = False
            V.areas_visited += 1
            V.score += int(V.score_increase)
            V.score_increase = 0
            shop_items_define(V)
            V.current_weather = []
            V.current_weather_duration = []
            for i in range(V.weather_amount):
                V.current_weather.append(0)
                V.current_weather_duration.append(3)
            V.area = V.areas[V.area_id]
            print(area_color(V) + "You have entered the", V.area + "\033[0m\nType anything to continue...")
            action = input()
            V.game_time = 0
            if V.player_travel > 0:
                V.player_xp += round(xp_to_lvl_up(V) * V.player_travel / 100)
                print("You gained\033[38;2;100;0;200m", round(xp_to_lvl_up(V) * V.player_travel / 100), "XP\033[0m for entering a new area!")
            level_up(V)
            V.mimic_got_item = False
            V.mimic_given_items = 0
            V.bank_first_time = True
            V.bank_money += round(V.bank_money * 0.5)
            V.forest_enemy_spawn = 0
            V.enough_destroyed = False
            V.water_level = V.default_water_levels[V.area_id]
            map_generation(V)
            V.escape_amount = 0
        V.delete_run()
        V.continue_run = False
        map_movement(V)
        if V.lost == 1:
            break
        V.area_id += V.escape_amount
        if V.area_id >= len(V.areas):
            V.area_id -= len(V.areas)
        V.map_complexity += 2
    final_statistics(V)
    if V.saved == False:
        print("\033[31;3mYou lost it all...\033[0m\n")
    else:
        print("\033[34;3mYou have saved yourself...\033[0m\nType anything to close the game...")
        action = input()

def story_mode():
    if V.continue_run == False:
        print('''\033[38;2;100;200;250m"My child, defeat your enemies, consume power, and acquire strength."
"And once you are strong enough, come back here for the final test..."\033[0m
Type anything to continue...''')
        action = input()
        V.game_mode = "story"
        V.area_id = 0
        V.story_mode_area_number = 0
    while V.story_mode_area_number in range(8):
        if V.continue_run == False:
            V.default_water_levels[6] = 0.75
            V.earth_cannot_generate_tiles = False
            V.vision_range = V.base_vision_ranges[V.area_id]
            for k in range(len(V.hunters_appeared)):
                V.hunters_appeared[k] = False
            V.score += int(V.score_increase)
            V.score_increase = 0
            shop_items_define(V)
            V.current_weather = []
            V.current_weather_duration = []
            for r in range(V.weather_amount):
                V.current_weather.append(0)
                V.current_weather_duration.append(3)
            V.area = V.areas[V.area_id]
            print(area_color(V) + "You have entered the", V.area + "\033[0m\nType anything to continue...")
            action = input()
            V.game_time = 0
            if V.player_travel > 0:
                V.player_xp += round(xp_to_lvl_up(V) * V.player_travel / 100)
                print("You gained\033[38;2;100;0;200m", round(xp_to_lvl_up(V) * V.player_travel / 100), "XP\033[0m for entering a new area!")
            level_up(V)
            V.mimic_got_item = False
            V.mimic_given_items = 0
            V.bank_first_time = True
            V.bank_money += round(V.bank_money * 0.5)
            V.forest_enemy_spawn = 0
            V.enough_destroyed = False
            V.water_level = V.default_water_levels[V.area_id]
            map_generation(V)
            V.escape_amount = 0
        V.delete_run()
        V.continue_run = False
        map_movement(V)
        if V.lost == 1:
            break
        V.area_id += V.escape_amount
        V.story_mode_area_number += V.escape_amount
        if V.story_mode_area_number > 7 and V.escape_amount > 1:
            V.story_mode_area_number = 7
        if V.area_id >= len(V.areas):
            V.area_id = 0
            V.final_area = True
            print('''\033[38;2;100;200;250m"My child, you have come back. Prepare yourself for the final battle."\033[0m
Type anything to continue...''')
            action = input()
        V.map_complexity += 1
    final_statistics(V)
    if V.saved == False:
        if V.lost == 1:
            print("\033[31;3mYou lost it all...\033[0m\n")
        else:
            V.SM_completed = True
            print("\033[33;3mYou have won...\033[0m\n")
            meta_save(V)
    else:
        print("\033[34;3mYou have saved yourself...\033[0m\nType anything to close the game...")
        action = input()

def raid_mode_area_choose():
    if V.continue_run == False:
        print('''Choose an area.''')
        for k in range(7):
            print( end = "")
            if V.TD_area_unlocks[k] == False and V.RM_areas_cheat == False:
                print("\033[0m" + str(k+1) + ". Locked")
            else:
                print(represented_area_color(V, k) + str(k+1) + ". " + V.areas[k], "\033[0m- Survived", V.TD_max_raids[k], "raids.")
        print("\033[0m8. Unlocks")
        print("9. Cancel")
        while True:
            print('''\033[0mType in the action...''')
            action = input()
            if action.isdigit():
                action = int(action) - 1
                if action < 7:
                    if V.TD_area_unlocks[action] or V.RM_areas_cheat:
                        raid_mode(action)
                        break
                    else:
                        print("You don't have this area unlocked!")
                elif action == 7:
                    if False in V.TD_area_unlocks:
                        print("In order to unlock some of the next areas you can:")
                        if V.TD_area_unlocks[2] == False:
                            print("Survive 2 raids in " + represented_area_color(V, 1) + "the Deep Forest\033[0m.")
                            print("Survive 3 raids in " + represented_area_color(V, 0) + "the Garden\033[0m.")
                        if V.TD_area_unlocks[3] == False:
                            if V.TD_area_unlocks[2]:
                                print("Survive 3 raids in " + represented_area_color(V, 2) + "the Cave\033[0m.")
                        if V.TD_area_unlocks[4] == False:
                            if V.TD_area_unlocks[3]:
                                print("Survive 4 raids in " + represented_area_color(V, 3) + "the Tundra\033[0m.")
                            if V.TD_area_unlocks[2]:
                                print("Survive 5 raids in " + represented_area_color(V, 2) + "the Cave\033[0m.")
                        if V.TD_area_unlocks[5] == False:
                            if V.TD_area_unlocks[4]:
                                print("Survive 4 raids in " + represented_area_color(V, 4) + "the Canyon\033[0m.")
                            if V.TD_area_unlocks[3]:
                                print("Survive 6 raids in " + represented_area_color(V, 3) + "the Tundra\033[0m.")
                        if V.TD_area_unlocks[6] == False:
                            if V.TD_area_unlocks[5]:
                                print("Survive 7 raids in " + represented_area_color(V, 5) + "the Desert\033[0m.")
                    else:
                        print("You have unlocked every single area for raids!")
                elif action == 8:
                    break
    else:
        raid_mode(V.area_id)

def raid_mode(starting_area = 0):
    if V.continue_run == False:
        print('''\033[38;2;100;200;250m"My child, defeat your enemies, consume power, and acquire strength."
"Survive here for as long as you can..."\033[0m
Type anything to continue...''')
        action = input()
        V.game_mode = "raid"
        V.default_water_levels[6] = 0.75
        V.area_id = starting_area
        V.vision_range = V.base_vision_ranges[V.area_id]
        V.area = V.areas[V.area_id]
        V.game_time = 0
        V.mimic_got_item = False
        V.mimic_given_items = 0
        V.bank_first_time = True
        V.current_weather = []
        V.current_weather_duration = []
        shop_items_define(V)
        for r in range(V.weather_amount):
            V.current_weather.append(0)
            V.current_weather_duration.append(3)
        V.map_complexity = 3
        map_generation(V)
    V.delete_run()
    V.continue_run = False
    map_movement(V)
    final_statistics(V)
    if V.saved == False:
        print("\033[31;3mYou lost it all...\033[0m\n")
    else:
        print("\033[34;3mYou have saved yourself...\033[0m\nType anything to close the game...")
        action = input()

def daily_run():
    seed(V.daily_seed)
    V.difficulty = randint(70, 100)
    V.original_difficulty = V.difficulty
    mutator_factor = V.difficulty * (-0.05) + 5.5
    V.weather_amount = randint(1, 6)
    mutator_factor = mutator_factor + (V.weather_amount * (-0.1) + 0.6)
    V.global_seed = randint(0, 10000)
    V.map_seed, V.weather_seed, V.weather_effects_seed, V.altar_seed, V.shop_seed, V.gamble_seed, V.remnant_seed, V.enemy_encouter_seed = V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed
    mode = choice(["story", "infinite", "raid"])
    print("\nDaily Run Seed -", V.daily_seed, "\nGame Mode -", mode, "\nSeed -", V.global_seed, "\nDifficulty -", V.difficulty, "\nWeather amount -", V.weather_amount)
    print('''
Are you sure you want to play this daily run?
1. Yes
2. No''')
    while True:
        action = input()
        if action == "1" or action.lower() == "yes":
            if mode == "infinite":
                V.game_mode = "infinite"
                infinite_mode()
            elif mode == "story":
                V.game_mode = "story"
                story_mode()
            elif mode == "raid":
                V.game_mode = "raid"
                raid_mode(randint(0, 6))
            else:
                print("There was an error initializing game modes for the daily run! Report this to the developer!")
            break
        elif action == "2" or action.lower() == "no":
            break

def daily_run_retry():
    seed(V.daily_seed)
    V.difficulty = randint(70, 100)
    V.original_difficulty = V.difficulty
    mutator_factor = V.difficulty * (-0.05) + 5.5
    V.weather_amount = randint(1, 6)
    mutator_factor = mutator_factor + (V.weather_amount * (-0.1) + 0.6)
    V.global_seed = randint(0, 10000)
    V.map_seed, V.weather_seed, V.weather_effects_seed, V.altar_seed, V.shop_seed, V.gamble_seed, V.remnant_seed, V.enemy_encouter_seed = V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed
    mode = choice(["story", "infinite", "raid"])
    if mode == "infinite":
        V.game_mode = "infinite"
        infinite_mode()
    elif mode == "story":
        V.game_mode = "story"
        story_mode()
    elif mode == "raid":
        V.game_mode = "raid"
        raid_mode(randint(0, 6))
    else:
        print("There was an error initializing game modes for the daily run! Report this to the developer!")

def credits_mode():
    V.game_mode = "credits"
    default_enemies_credits(V)
    print('''Main Credits:
(Type anything to continue...)''')
    action = input()
    print("\n\n\n")
    fight(V, [0])
    print('''Special Thanks to
(Type anything to continue...)''')
    action = input()
    print("\n\n\n")
    fight(V, [1])
    fight(V, [2])
    level_up(V)
    fight(V, [3])


def mutators_init():
    print('''Would you like to turn on \033[38;2;255;40;100;5mmutators\033[0m/change difficulty?
1. No
2. Yes
3. What is a \033[38;2;255;40;100;5mmutator?\033[0m''')
    while True:
        print("Type in the action")
        action = input()
        if action == '1' or action.lower() == 'no':
            break
        elif action == '2' or action.lower() == 'yes':
            mutators_choose()
            break
        elif action == '3' or 'what' in action.lower():
            print('''\033[38;2;255;40;100;5mMutator\033[0m is a modifier for this game, which makes the game harder (or sometimes easier) in a unique way.''')
            
def mutators_choose():
    leave = 0
    while leave == 0:
        print("0. Seed -", V.global_seed)
        if V.difficulty == 40:
            print("1. Difficulty - Easy")
        elif V.difficulty == 55:
            print("1. Difficulty - Medium")
        elif V.difficulty == 70:
            print("1. Difficulty - Hard")
        elif V.difficulty == 100:
            print("1. Difficulty - Absurd")
        else:
            print("1. Difficulty - Unknown (", V.difficulty, ")", sep = "")
        if V.SM_completed or V.SM_skip:
            print("2. Weather Amount -", V.weather_amount)
            print("3. More...")
        else:
            print("2. Locked")
        print("9. Play the game")
        while True:
            action = input()
            if action == "0" or action.lower() == "seed":
                print("Type in an integer for it to be a seed. Type anything else to randomize it")
                action = input()
                if action.isdigit():
                    V.global_seed = int(action)
                    break
                else:
                    V.global_seed = randint(0, 10000)
                    break
            elif action == "1" or action.lower() == "difficulty":
                if V.difficulty < 70:
                    V.difficulty += 15
                else:
                    V.difficulty += 30
                if V.difficulty > 100:
                    V.difficulty = 40
                break
            elif action.lower() == "easy":
                V.difficulty = 40
                break
            elif action.lower() == "medium" or action.lower() == "normal":
                V.difficulty = 55
                break
            elif action.lower() == "hard":
                V.difficulty = 70
                break
            elif action.lower() == "absurd":
                V.difficulty = 100
                break
            elif (action == "2" or "weather" in action.lower()) and (V.SM_completed or V.SM_skip):
                print("Type in an integer for it to be the amount of weathers active at the same time. Type anything else to randomize it")
                action = input()
                if action.isdigit():
                    if int(action) < 15:
                        V.weather_amount = int(action)
                    else:
                        V.weather_amount = 15
                else:
                    V.weather_amount = randint(1, 5)
                break
            elif (action == "3" or "more" in action.lower()) and (V.SM_completed or V.SM_skip):
                print("I really wasn't happy with the mutators that did exist. I will make better ones later!\nType anything to continue...")
                action = input()
                break
            elif action == "9" or "play" in action.lower() or "game" in action.lower():
                leave = 1
                V.original_difficulty = V.difficulty
                break

def meta_options():
    while True:
        print('''1. Gameplay
2. Quit to title
Type in the number or the action itself...''')
        action = input()
        if action.lower() in ["1", "gameplay"]:
            while True:
                print("1. Skip Story Mode requirements -", V.SM_skip)
                if V.SM_completed or V.SM_skip:
                    print("2. Unlock all Raid Mode areas -", V.RM_areas_cheat)
                else:
                    print("2. Locked")
                print("9. Back")
                print("Type in the number or the action itself...")
                action = input()
                if action.lower() in ["1", "skip story mode requirements"] or "skip" in action.lower() or "story mode" in action.lower():
                    if V.SM_skip:
                        V.SM_skip = False
                        if V.SM_completed == False:
                            V.RM_areas_cheat = False
                    else:
                        V.SM_skip = True
                elif (action.lower() in ["2", "unlock all raid mode areas"] or "raid" in action.lower()) and (V.SM_completed or V.SM_skip):
                    if V.RM_areas_cheat:
                        V.RM_areas_cheat = False
                    else:
                        V.RM_areas_cheat = True
                elif action.lower() in ["9", "back"]:
                    break
        elif action == "2" or "quit" in action.lower() or "title" in action.lower():
            break
    meta_save(V)

def game():
    retry = 0
    option_moment = 0
    while True:
        if V.continue_run:
            print('''

Do you want to continue your saved run?(Your run will be deleted if you won't continue it!)
1. Yes
2. No
Type in the action...''')
            while True:
                action = input()
                if action.lower() in ["1", "yes"]:
                    break
                elif action.lower() in ["2", "no"]:
                    V.continue_run = False
                    V.delete_run()
                    break
        if V.continue_run == False:
            V.global_seed = randint(0, 10000)
            true_reset(V)
        V.daily_seed = (localtime().tm_year * 365 + localtime().tm_mon * 30 + localtime().tm_mday)
        if retry == 0 and V.continue_run == False:
            settings_reset(V)
            if V.SM_completed or V.SM_skip:
                print('''Which gamemode do you want to play?
1. Story Mode
2. Infinite Mode
3. Raid Mode
4. Daily Run
5. Credits
9. Options

Type in the gamemode you want to play...''')
            else:
                print('''Which gamemode do you want to play?
1. Story Mode
2. Locked
3. Locked
4. Locked
5. Locked
9. Options

Beat the Story Mode to unlock other game modes.
Type in the gamemode you want to play...''')
            while V.continue_run == False:
                action = input()
                if action == "1" or "story" in action.lower():
                    V.meta_game_mode = "story"
                    V.game_mode = "story"
                    break
                elif (action == "2" or "inf" in action.lower()) and (V.SM_completed or V.SM_skip):
                    V.meta_game_mode = "infinite"
                    V.game_mode = "infinite"
                    break
                elif (action == "3" or "raid" in action.lower()) and (V.SM_completed or V.SM_skip):
                    V.meta_game_mode = "raid"
                    V.game_mode = "raid"
                    break
                elif (action == "4" or "day" in action.lower() or "daily" in action.lower()) and (V.SM_completed or V.SM_skip):
                    V.meta_game_mode = "daily"
                    V.game_mode = "daily"
                    break
                elif (action == "5" or "credits" in action.lower()) and (V.SM_completed or V.SM_skip):
                    V.meta_game_mode = "credits"
                    V.game_mode = "credits"
                    break
                elif (action == "9" or "options" in action.lower()):
                    meta_options()
                    option_moment = 1
                    break
            if option_moment == 1:
                option_moment = 0
                continue
            if V.game_mode not in ["daily", "credits"] and V.continue_run == False:
                mutators_init()
                V.map_seed, V.weather_seed, V.weather_effects_seed, V.altar_seed, V.shop_seed, V.gamble_seed, V.remnant_seed, V.enemy_encouter_seed = V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed
            if V.game_mode == "story":
                story_mode()
            elif V.game_mode == "infinite":
                infinite_mode()
            elif V.game_mode == "raid":
                raid_mode_area_choose()
            elif V.game_mode == "daily":
                daily_run()
            elif V.game_mode == "credits":
                credits_mode()
            else:
                print("There was an error initiating gamemodes...")
        else:
            V.map_seed, V.weather_seed, V.weather_effects_seed, V.altar_seed, V.shop_seed, V.gamble_seed, V.remnant_seed, V.enemy_encouter_seed = V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed
            if V.meta_game_mode == "story":
                story_mode()
            elif V.meta_game_mode == "infinite":
                infinite_mode()
            elif V.meta_game_mode == "raid":
                raid_mode_area_choose()
            elif V.meta_game_mode == "daily":
                daily_run_retry()
            elif V.meta_game_mode == "credits":
                credits_mode()
            else:
                print("There was an error initiating gamemodes...")
        if V.saved == False:
            print('''\n\n\nDo you want to retry same settings?
1. Yes
2. No
Type in the action...''')
            while True:
                action = input()
                if action == '1' or action.lower() == 'yes':
                    retry = 1
                    break
                elif action == '2' or action.lower() == 'no':
                    retry = 0
                    break
        else:
            break

meta_save(V)
game()