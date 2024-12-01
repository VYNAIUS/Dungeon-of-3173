
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

V = variables.V()

print("V0.3.2")
def infinite_mode():
    V.game_mode = "infinite"
    V.area_id = 0
    V.areas_visited = 0
    if V.area_rando:
        area_randomize(V)
    while True:
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
            V.current_weather_duration.append(0)
        V.area = V.areas[V.area_id]
        print(area_color(V) + "You have entered the", V.area + "\033[0m")
        V.game_time = 0
        if V.player_travel > 0:
            V.player_xp += round(xp_to_lvl_up(V) * V.player_travel / 100)
            print("You gained\033[38;2;100;0;200m", round(xp_to_lvl_up(V) * V.player_travel / 100), "XP\033[0m for entering a new area!")
        level_up(V)
        V.mimic_got_item = False
        V.mimic_given_items = 0
        V.bank_first_time = True
        V.forest_enemy_spawn = 0
        V.enough_destroyed = False
        V.water_level = V.default_water_levels[V.area_id]
        V.player_boat = False
        map_generation(V)
        V.escaped = False
        map_movement(V)
        if V.lost == 1:
            break
        if V.escaped == False:
            V.area_id += 1
        else:
            V.area_id += 3
        if V.area_id >= len(V.areas):
            V.area_id -= len(V.areas)
        V.map_complexity += 2
    print("\033[31;3mYou lost it all...\033[0m\n")
    final_statistics(V)

def story_mode():
    V.game_mode = "story"
    V.area_id = 0
    i = 0
    if V.area_rando:
        area_randomize(V)
    while i in range(8):
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
            V.current_weather_duration.append(0)
        V.area = V.areas[V.area_id]
        print(area_color(V) + "You have entered the", V.area + "\033[0m")
        V.game_time = 0
        if V.player_travel > 0:
            V.player_xp += round(xp_to_lvl_up(V) * V.player_travel / 100)
            print("You gained\033[38;2;100;0;200m", round(xp_to_lvl_up(V) * V.player_travel / 100), "XP\033[0m for entering a new area!")
        level_up(V)
        V.mimic_got_item = False
        V.mimic_given_items = 0
        V.bank_first_time = True
        V.forest_enemy_spawn = 0
        V.enough_destroyed = False
        V.water_level = V.default_water_levels[V.area_id]
        V.player_boat = False
        map_generation(V)
        V.escaped = False
        map_movement(V)
        i += 1
        if V.lost == 1:
            break
        if V.escaped == False:
            V.area_id += 1
        else:
            V.area_id += 3
            i += 2
            if i > 7:
                i = 7
        if V.area_id >= len(V.areas):
            V.area_id = 0
            V.final_area = True
        V.map_complexity += 1
    if V.lost == 1:
        print("\033[31;3mYou lost it all...\033[0m\n")
    else:
        print("\033[33;3mYou have won...\033[0m\n")
    final_statistics(V)

def raid_mode_area_choose():
    print('''Choose an area.''')
    for k in range(7):
        print( end = "")
        if V.TD_area_unlocks[k] == False:
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
                raid_mode(action)
                break
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

def raid_mode(starting_area = 0):
    V.default_water_levels[6] = 0.75
    V.game_mode = "raid"
    if V.area_rando:
        area_randomize(V)
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
        V.current_weather_duration.append(0)
    V.map_complexity = 3
    map_generation(V)
    map_movement(V)
    final_statistics(V)
    print("\033[31;3mYou lost it all...\033[0m\n")

def daily_run():
    seed(V.daily_seed)
    V.difficulty = randint(50, 70)
    V.original_difficulty = V.difficulty
    mutator_factor = V.difficulty * (-0.05) + 4.5
    V.weather_amount = randint(1, 6)
    mutator_factor = mutator_factor + (V.weather_amount * (-0.1) + 0.6)
    V.evolution = chance(0.4 * mutator_factor)
    V.overkill = chance(0.2 * mutator_factor)
    V.speedrunner = chance(0.4 * mutator_factor)
    V.item_rando = chance(0.3 * mutator_factor)
    V.eclipse = chance(0.3 * mutator_factor)
    V.area_rando = chance(0.1 * mutator_factor)
    V.global_seed = randint(0, 10000)
    V.map_seed, V.weather_seed, V.weather_effects_seed, V.altar_seed, V.shop_seed, V.gamble_seed, V.remnant_seed, V.enemy_encouter_seed, V.evolution_seed = V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed
    mode = choice(["story", "infinite"])
    print("\nDaily Run Seed -", V.daily_seed, "\nGame Mode -", mode, "\nSeed -", V.global_seed, "\nDifficulty -", V.difficulty, "\nWeather amount -", V.weather_amount)
    if V.evolution:
        print("Evolution is enabled")
    if V.overkill:
        print("Overkill is enabled")
    if V.speedrunner:
        print("Speedrunner is enabled")
    if V.item_rando:
        print("Item Randomizer is enabled")
    if V.eclipse:
        print("Eclipse is enabled")
    if V.area_rando:
        print("Area Randomizer is enabled")
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
            else:
                print("There was an error initializing game modes for the daily run! Report this to the developer!")
            break
        elif action == "2" or action.lower() == "no":
            break

def daily_run_retry():
    seed(V.daily_seed)
    V.difficulty = randint(50, 70)
    V.original_difficulty = V.difficulty
    mutator_factor = V.difficulty * (-0.05) + 4.5
    V.weather_amount = randint(1, 6)
    mutator_factor = mutator_factor + (V.weather_amount * (-0.1) + 0.6)
    V.evolution = chance(0.4 * mutator_factor)
    V.overkill = chance(0.2 * mutator_factor)
    V.speedrunner = chance(0.4 * mutator_factor)
    V.item_rando = chance(0.3 * mutator_factor)
    V.eclipse = chance(0.3 * mutator_factor)
    V.area_rando = chance(0.1 * mutator_factor)
    V.global_seed = randint(0, 10000)
    V.map_seed, V.weather_seed, V.weather_effects_seed, V.altar_seed, V.shop_seed, V.gamble_seed, V.remnant_seed, V.enemy_encouter_seed, V.evolution_seed = V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed
    mode = choice(["story", "infinite"])
    if mode == "infinite":
        V.game_mode = "infinite"
        infinite_mode()
    elif mode == "story":
        V.game_mode = "story"
        story_mode()
    else:
        print("There was an error initializing game modes for the daily run! Report this to the developer!")

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
        print("2. Weather Amount -", V.weather_amount)
        print("3. Evolution -", V.evolution)
        print("4. Overkill -", V.overkill)
        print("5. Speedrunner -", V.speedrunner)
        print("6. Item Randomizer -", V.item_rando)
        print("7. Eclipse -", V.eclipse)
        print("8. Area Randomizer -", V.area_rando)
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
            elif action == "2" or "weather" in action.lower():
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
            elif action == "3" or action.lower() == "evolution" or action.lower() == "evolve":
                if V.evolution == False:
                    V.evolution = True
                else:
                    V.evolution = False
                break
            elif action == "4" or action.lower() == "overkill":
                if V.overkill == False:
                    V.overkill = True
                else:
                    V.overkill = False
                break
            elif action == "5" or "speed" in action.lower():
                if V.speedrunner == False:
                    V.speedrunner = True
                else:
                    V.speedrunner = False
                break
            elif action == "6" or "item" in action.lower():
                if V.item_rando == False:
                    V.item_rando = True
                else:
                    V.item_rando = False
                break
            elif action == "7" or action.lower() == "eclipse":
                if V.eclipse == False:
                    V.eclipse = True
                else:
                    V.eclipse = False
                break
            elif action == "8" or "area" in action.lower():
                if V.area_rando == False:
                    V.area_rando = True
                else:
                    V.area_rando = False
                break
            elif action == "9" or "play" in action.lower() or "game" in action.lower():
                leave = 1
                V.original_difficulty = V.difficulty
                break

def game():
    retry = 0
    while True:
        V.global_seed = randint(0, 10000)
        V.daily_seed = (localtime().tm_year * 365 + localtime().tm_mon * 30 + localtime().tm_mday)
        true_reset(V)
        if retry == 0:
            settings_reset(V)
            print('''Which gamemode do you want to play?
1. Story Mode
2. Infinite Mode
3. Raid Mode
4. Daily Run

Story Mode is recommended for first playthrough
Type in the gamemode you want to play...''')
            while True:
                action = input()
                if action == "1" or "story" in action.lower():
                    V.meta_game_mode = "story"
                    V.game_mode = "story"
                    break
                elif action == "2" or "inf" in action.lower():
                    V.meta_game_mode = "infinite"
                    V.game_mode = "infinite"
                    break
                elif action == "3" or "raid" in action.lower():
                    V.meta_game_mode = "raid"
                    V.game_mode = "raid"
                    break
                elif action == "4" or "day" in action.lower() or "daily" in action.lower():
                    V.meta_game_mode = "daily"
                    V.game_mode = "daily"
                    break
            if V.game_mode != "daily":
                mutators_init()
                V.map_seed, V.weather_seed, V.weather_effects_seed, V.altar_seed, V.shop_seed, V.gamble_seed, V.remnant_seed, V.enemy_encouter_seed, V.evolution_seed = V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed
            if V.game_mode == "story":
                story_mode()
            elif V.game_mode == "infinite":
                infinite_mode()
            elif V.game_mode == "raid":
                raid_mode_area_choose()
            elif V.game_mode == "daily":
                daily_run()
            else:
                print("There was an error initiating gamemodes...")
        else:
            V.map_seed, V.weather_seed, V.weather_effects_seed, V.altar_seed, V.shop_seed, V.gamble_seed, V.remnant_seed, V.enemy_encouter_seed, V.evolution_seed = V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed, V.global_seed
            if V.meta_game_mode == "story":
                story_mode()
            elif V.meta_game_mode == "infinite":
                infinite_mode()
            elif V.meta_game_mode == "raid":
                raid_mode_area_choose()
            elif V.meta_game_mode == "daily":
                daily_run_retry()
            else:
                print("There was an error initiating gamemodes...")
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

save(V)
game()