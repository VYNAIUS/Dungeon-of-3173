
from random import seed, shuffle, randint, choice, choices
from extra_functions import chance
from upgrades_functions import level_up, stats_altar, player_remnants
from coloring import area_color, water_color
from misc_functions import lost_check, time_events, inventory_statistics, escape, change_interaction
from enemies_and_fighting import fight, fight_choose, bossfight_choose, ally_choose
from shops import shop, alchemist_shop, mimic_gamble, mimic_bank, death_boat
from circular_avoidance import max_x, max_y, min_x, min_y, stalker_AI

def default_areas(V):
    V.areas = ["Garden", "Deep Forest", "Cave", "Tundra", "Canyon", "Desert", "Rotten Forest"]
    V.areas_colors = [[0, 255, 100], [32, 150, 32], [140, 140, 140], [200, 200, 230], [150, 180, 150], [190, 210, 0], [125, 125, 125]]
    V.water_colors_0 = [[0, 200, 255], [0, 100, 150], [0, 150, 150], [0, 150, 150], [0, 170, 100], [0, 255, 255], [0, 255, 100]]
    V.water_colors_1 = [[0, 100, 128], [0, 50, 75], [0, 75, 75], [0, 75, 75], [0, 85, 50], [0, 128, 128], [0, 128, 50]]
    V.path_lengths = [[3, 3], [0, 3], [0, 2], [2, 3], [1, 3], [3, 4], [0, 3]] # [min, max]
    V.height_variaty = [[0, 0], [-1, 1], [-2, 2], [-1, 3], [-1, 2], [-1, 1], [-2, 1]]
    V.wall_min_thickness = [1, 3, 2, 1, 1, 1, 2]
    V.turn_right_prob = [1, 1, 1, 1, 1, 1, 1]
    V.turn_down_prob = [1, 1, 1, 0.95, 1, 1, 1]
    V.turn_left_prob = [1, 1, 1, 1, 1, 1, 1]
    V.turn_up_prob = [1, 1, 1, 0.5, 0.5, 1, 1]
    V.area_max_x = [83, 41, 23, 41, 54, 54, 47]
    V.area_max_y = [15, 10, 8, 10, 5, 12, 12]
    V.start_positions = [["ul", "ml", "dl"], ["ul", "um", "ur", "dl", "dm", "dr"], ["mm"], ["um", "dm", "ml"], ["ul", "ur"],
                       ["ul", "ur", "dl", "dr"], ["ul", "um", "ur", "ml", "mr", "dl", "dm", "dr"]]
    V.area_patterns = [[[["small boxes"], [1], [0]], [["basic", "basic water"], [1, 1], [0, 0]], [["small boxes", "basic"], [0.65, 1], [0, 0]]],
                     
                     [[["basic", "basic water"], [1, 1], [0, 0]], [["basic", "basic water", "isolated remnants"], [1, 1, 1], [0, 0, 0]]],
                     
                     [[["basic", "basic water", "isolated remnants", "isolated remnants", "change's crystal"], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]],
                      [["basic", "basic water", "isolated remnants", "change's crystal"], [1, 1, 1, 1], [0, 0, 0, 0, 0]]],

                     [[["basic", "basic water"], [1, 1], [0, 0]]],
                     
                     [[["basic only horizontal", "basic", "basic water"], [0.3, 1, 1], [0, 0, 0]]],
                     
                     [[["basic", "holes down", "basic", "holes up", "basic", "basic water", "basic water"], [0.3, 0.1, 0.5, 0.3, 1, 1, 1], [0, 0, -1, -1, 0, 0, -1]],
                      [["basic", "holes down", "basic", "holes down", "basic", "holes up", "basic", "holes up", "basic", "basic water"], [0.15, 0.5, 0.1, 0.5, 0.3, 0.5, 0.1, 0.5, 1, 1], [0, 0, -1, -1, -2, -2, -1, -1, 0, 0]]],
                     
                     [[["basic", "basic water"], [1, 1], [0, 0]]]]
    V.area_pattern_chances = [[3, 1, 2], [3, 1], [1, 2], [1], [1], [3, 2], [1]]
    V.remnants_spawns = [[0, 4, 3], [0, 2, 0], [0, 0, 0], [0, 1, 1], [0, 4, 0], [0, 6, 1], [0, 3, 0]] # first value - min, second value - max, third value - average
    V.snow_pile_spawns = [0, 0, 0.05, 0.1, 0, 0, 0]
    V.water_level = 0
    V.default_water_levels = [3, 2, 1, 2, 1, -2.5, 0.75]
    V.river_prob = [0, 0.75, 0.15, 0.75, 0, 1, 2]
    V.river_thickness = [1, 1, 1, 1, 1, 1, 1]
    V.escape_river_prob = [0, 0.45, 0.25, 0.65, 0, 0.25, 0.55]
    V.pond_prob = [1, 0.1, 0.5, 0, 0, 0, 0]
    V.pond_radius = [4, 4, 4, 0, 0, 1, 0]
    V.weathers = [[0], [0, 1, 2, 7, 8, 9], [0, 3, 8], [0, 2, 4, 7, 8], [0, 1, 2, 3, 7, 9], [0, 1, 5, 8, 9], [0, 2, 6, 8, 9]] # 0 - nothing, 1 - rain, 2 - thick fog, 3 - earth quake, 4 - blizzard, 5 - sandstorm, 6 - acid rain, 7 - hail, 8 - flood, 9 - drought
    V.weather_chances = [[1], [7, 4, 3, 3, 1, 1], [10, 4, 6], [7, 3, 4, 4, 1], [7, 4, 2, 1, 3, 1], [12, 2, 7, 1, 6], [5, 1, 4, 4, 1]]
    V.weathers_durations = [[0, 5], [10, 30], [6, 12], [5, 7], [8, 16], [6, 24], [4, 12], [6, 18], [4, 8], [7, 14]]
    V.base_vision_ranges = [-1, 12, 6, 16, 14, 18, 8]
    V.current_weather = [0]
    V.current_weather_duration = [0]
    V.events = []
    V.benefitial_events = [2, 3, 5, 11, 12, 13, 14, 16, 18, 19, 24]
    V.hurtful_events = [1, 4, 7, 8, 17, 20]
    V.neutral_events = [0, 6, 9, 10, 15, 21, 22, 25, 26, 27, 28]
    V.events_coordinates = []
    V.events_heights = []
    V.player_coordinates = [0, 0, 0]
    V.map_complexity = 0
    V.game_time = 0
    V.vision_range = 0 # -1 - entire map is visible
    V.escape_amount = 0
    V.earth_cannot_generate_tiles = False

    V.player_hp_penalty = 0
    V.player_def_penalty = 0
    V.stalker_stealth = 100
    V.player_oxygen_danger = False
# AREA STATS END






def map_print(V):
    print("AREA:" + area_color(V) + " The", V.area + "\033[0m")
    print("TIME: ", end = "")
    if V.area_id == 2 or V.area_id == 6 or V.player_coordinates[2] < 0:
        print("Unknown", end = "")
    elif V.game_time < 6:
        print("Morning", end = "")
    elif V.game_time < 12:
        print("Day", end = "")
    elif V.game_time < 18:
        print("Evening", end = "")
    else:
        print("Night", end = "")
    print()
    if V.weather_amount > 0:
        print("WEATHER: ", end = "")
        counter = 0
        for i in V.current_weather:
            if counter > 0:
                print(", ", end = "")
            if i == 0:
                print("None", end = "")
            elif i == 1:
                print("Rain", end = "")
            elif i == 2:
                print("Thick Fog", end = "")
            elif i == 3:
                print("Earthquake", end = "")
            elif i == 4:
                print("Blizzard", end = "")
            elif i == 5:
                print("Sandstorm", end = "")
            elif i == 6:
                print("Acid Rain", end = "")
            elif i == 7:
                print("Hail", end = "")
            elif i == 8:
                print("Flood", end = "")
            elif i == 9:
                print("Drought", end = "")
            counter += 1
        print()
    if V.player_boat == False:
        print("OXYGEN:" + water_color(V), end = "")
        if V.player_oxygen > 0:
            for i in range(int(V.player_oxygen)):
                print("•", end = "")
        else:
            for i in range(int(abs(V.player_oxygen))):
                print("\033[38;2;255;0;0m○", end = "")
        if V.player_oxygen_danger:
            print("\033[38;2;255;0;0m!")
    else:
        print("BOAT DURABILITY: " + water_color(V), V.player_boat_hp, "%", sep = "", end = "")
        if V.player_boat_hp <= 0:
            print("\n\033[38;2;255;0;0mThe boat will break when you step on land!", end = "")
    print("\033[0m")
    print("MAP:" + area_color(V))
    for x in range(min_x(V), max_x(V) + 1):
        print("-", end = "")
    print()
    l = V.player_coordinates[2]
    for y in range(min_y(V), max_y(V) + 1):
        for x in range(min_x(V), max_x(V) + 1):
            if [x, y, l] == V.player_coordinates and V.player_boat == False:
                print("\033[33;1mP" + area_color(V), end = "")
            elif [x, y, l] == V.player_coordinates and V.player_boat == True:
                print("\033[33;1mb" + area_color(V), end = "")
            elif not [x, y, l] in V.events_coordinates or (V.vision_range != -1 and (((V.player_coordinates[0] - x) ** 2 + (V.player_coordinates[1] - y) ** 2) ** 0.5) > V.vision_range + 0.25 + l * 1.5):
                print(" ", end = "")
            else:
                event = V.events[V.events_coordinates.index([x, y, l])]
                event_height = V.events_heights[V.events_coordinates.index([x, y, l])] + l * 2.5
                if event in [0, 9, 25, 26]:
                    if V.water_level > event_height:
                        print(water_color(V) + "~", end = "")
                    elif V.area_id == 2 or V.area_id == 6:
                        print(area_color(V, event_height, True) + "○", end = "")
                    elif V.game_time < 18:
                        print(area_color(V, event_height, True) + "•", end = "")
                    else:
                        print(area_color(V, event_height, True) + "○", end = "")
                elif event == 1:
                    if V.water_level > event_height:
                        print(water_color(V) + "×", end = "")
                    else:
                        print(area_color(V, event_height, True) + "×", end = "")
                elif event == 2:
                    if V.water_level > event_height:
                        print(water_color(V) + "†", end = "")
                    else:
                        print(area_color(V, event_height, True) + "†", end = "")
                elif event == 3:
                    if V.water_level > event_height:
                        print(water_color(V) + "$", end = "")
                    else:
                        print(area_color(V, event_height, True) + "$", end = "")
                elif event == 4:
                    if V.water_level > event_height:
                        print(water_color(V) + "B", end = "")
                    else:
                        print(area_color(V, event_height, True) + "B", end = "")
                elif event == 5:
                    if V.water_level > event_height:
                        print(water_color(V) + "⌂", end = "")
                    else:
                        print(area_color(V, event_height, True) + "⌂", end = "")
                elif event == 6:
                    if V.water_level > event_height:
                        print(water_color(V) + "~", end = "")
                    else:
                        print(area_color(V, event_height, True) + "~", end = "")
                elif event == 7:
                    if V.water_level > event_height:
                        print(water_color(V) + "Λ", end = "")
                    else:
                        print(area_color(V, event_height, True) + "Λ", end = "")
                elif event == 8:
                    if V.water_level > event_height:
                        print(water_color(V) + "A", end = "")
                    else:
                        print(area_color(V, event_height, True) + "A", end = "")
                elif event == 10:
                    if V.water_level > event_height:
                        print(water_color(V, 1) + "~", end = "")
                    else:
                        print(" ", end = "")
                elif event == 11:
                    if V.water_level > event_height:
                        print(water_color(V) + "D", end = "")
                    else:
                        print(area_color(V, event_height, True) + "D", end = "")
                elif event in [12, 16]:
                    if V.water_level > event_height:
                        print(water_color(V) + "E", end = "")
                    else:
                        print(area_color(V, event_height, True) + "E", end = "")
                elif event == 13:
                    if V.water_level > event_height:
                        print(water_color(V) + "C", end = "")
                    else:
                        print(area_color(V, event_height, True) + "C", end = "")
                elif event == 14:
                    if V.water_level > event_height:
                        print(water_color(V) + "P", end = "")
                    else:
                        print(area_color(V, event_height, True) + "P", end = "")
                elif event in [15, 27, 28]:
                    if V.water_level > event_height:
                        print("\033[38;2;255;50;255m~", end = "")
                    else:
                        print("\033[38;2;255;50;255m•", end = "")
                elif event == 17:
                    print("\033[38;2;255;50;255mΛ", end = "")
                elif event == 18:
                    print("\033[38;2;255;50;255m†", end = "")
                elif event == 19:
                    if V.water_level > event_height:
                        print(water_color(V) + "#", end = "")
                    else:
                        print(area_color(V, event_height, True) + "#", end = "")
                elif event == 20:
                    print("\033[33;1m?", end = "")
                    stalker_coords = V.events_coordinates[V.events.index(20)]
                    distance = ((V.player_coordinates[0] - stalker_coords[0]) ** 2 + (V.player_coordinates[1] - stalker_coords[1]) ** 2) ** 0.5
                    if distance > 0:
                        V.stalker_stealth -= round(12 / distance) + 1
                    else:
                        V.stalker_stealth -= 13
                    if V.stalker_stealth <= 0:
                        V.events[V.events.index(20)] = 0
                elif event == 21:
                    if V.water_level > event_height:
                        print(water_color(V) + "L", end = "")
                    else:
                        print(area_color(V, event_height, True) + "L", end = "")
                elif event == 22:
                    if V.water_level > event_height:
                        print(water_color(V) + "H", end = "")
                    else:
                        print(area_color(V, event_height, True) + "H", end = "")
                elif event == 24:
                    if V.water_level > event_height:
                        print(water_color(V) + "a", end = "")
                    else:
                        print(area_color(V, event_height, True) + "a", end = "")
                else:
                    print(event)

        print("\n" + water_color(V), end = "")
    for x in range(min_x(V), max_x(V) + 1):
        print("-", end = "")
    print("\033[0m")

def map_generation(V):
    seed(V.map_seed)
    V.shop_seed, V.weather_seed, V.weather_effects_seed = V.map_seed, V.map_seed, V.map_seed
    V.map_seed = randint(0, 10000)
    start = choice(V.start_positions[V.area_id])
    V.generation_area_pattern = choices(V.area_patterns[V.area_id], weights=V.area_pattern_chances[V.area_id])[0]
    #print(V.generation_area_pattern)
    good_events = []
    bad_events = []
    if V.game_mode in ["infinite", "story"]:
        if V.score >= 0:
            good_events.append(3)
        if V.score >= 3:
            good_events.append(5)
        if V.score >= 5:
            good_events.append(11)
        if V.score >= 7:
            good_events.append(19)
        if V.score >= 9:
            good_events.append(24)
    elif V.game_mode == "raid":
        good_events.append(3)
        if V.area_id > 0:
            good_events.append(5)
            good_events.append(11)
        if V.area_id > 1:
            good_events.append(24)
        if V.area_id > 2:
            good_events.append(19)
    if V.game_mode == "story" and (V.area_id == 2 or (V.area_id == 0 and V.change_recruited == True)):
        good_events.append(13)
    min_remnant, max_remnant, avg_remnant = V.remnants_spawns[V.area_id][0], V.remnants_spawns[V.area_id][1], V.remnants_spawns[V.area_id][2]
    remnant_events, remnant_weights = [], []
    for i in range(min_remnant, max_remnant + 1):
        if i == avg_remnant:
            remnant_weights.append(3)
        elif i == min_remnant or i == max_remnant:
            remnant_weights.append(1)
        else:
            if i < avg_remnant:
                addition, amount = 2 / (avg_remnant - min_remnant), i - min_remnant
                remnant_weights.append(1 + (addition * amount))
            else:
                addition, amount = 2 / (max_remnant - avg_remnant), max_remnant - i
                remnant_weights.append(1 + (addition * amount))
        remnant_events.append(i)
    remnant_events_amount = choices(remnant_events, remnant_weights)[0]
    for i in range(remnant_events_amount):
        good_events.append(14)
    rate = 2.5
    for i in range(V.map_complexity + 5):
        for i in range(randint(1, round(rate))):
            bad_events.append(1)
        if V.area_id == 3 and chance(0.2):
            bad_events.append(8)
        elif V.area_id == 3 and chance(0.125):
            bad_events.append(7)
        rate -= 0.25
        if rate < 1:
            rate = 1
    rate = 2.875
    for i in range(V.map_complexity + 3):
        for i in range(randint(1, round(rate))):
            good_events.append(2)
        rate -= 0.125
        if rate < 1:
            rate = 1

    #print(len(bad_events))
    V.score_increase = 0.75 * len(bad_events)

    turns = [] # [x, y, rotation ("r"/"d"/"l"/"u"), event/tile id, height, layer]
    if V.generation_area_pattern[0][0] in ["basic", "small boxes", "basic only horizontal", "basic only vertical"]:
        if start[0] == "u":
            turns.append([0, 0, "d", 0, 5, 0])
        elif start[0] == "d":
            turns.append([0, 0, "u", 0, 5, 0])
        else:
            turns.append([0, 0, "d", 0, 5, 0])
            turns.append([0, 0, "u", 0, 5, 0])
        if start[1] == "l":
            turns.append([0, 0, "r", 0, 5, 0])
        elif start[1] == "r":
            turns.append([0, 0, "l", 0, 5, 0])
        else:
            turns.append([0, 0, "r", 0, 5, 0])
            turns.append([0, 0, "l", 0, 5, 0])
        if V.game_mode in ["infinite", "story"]:
            V.events = [0]
        elif V.game_mode in ["raid"]:
            V.events = [25]
        V.events_coordinates = [[0, 0, 0]]
        V.events_heights = [5]
        V.player_coordinates = [0, 0, 0]

    event_amount = len(bad_events) + len(good_events)
    placed_event_amount = 0

    for pattern_index in range(len(V.generation_area_pattern[0])):
        generation_percentage = V.generation_area_pattern[1][pattern_index]
        generation_layer = V.generation_area_pattern[2][pattern_index]
        if V.generation_area_pattern[0][pattern_index] == "basic":
            x = 0
            y = 0
            iteration = 0
            l = 0

            min_length = round(V.path_lengths[V.area_id][0] - (V.map_complexity * 0.05))
            if min_length < 0:
                min_length = 0
            possible_max_lengths = [V.path_lengths[V.area_id][1]]
            for i in range(V.map_complexity):
                max_length = round(V.path_lengths[V.area_id][1] - i * 0.3)
                if max_length < min_length:
                    max_length = min_length
                possible_max_lengths.append(max_length)

            overleft_event_amount = event_amount - event_amount * generation_percentage - placed_event_amount
            if overleft_event_amount < 0:
                overleft_event_amount = 0

            while len(good_events) + len(bad_events) > overleft_event_amount:
                iteration += 1
                bad_path = False
                if iteration > 10000:
                    break
                path = choice(turns)
                x = path[0]
                y = path[1]
                h = path[4]
                l = path[5]
                if l != generation_layer:
                    iteration -= 0.75
                    continue
                if path[2] == "r":
                    length = randint(min_length, choice(possible_max_lengths))
                    for k in range(V.wall_min_thickness[V.area_id]):
                        for i in range(length + 1):
                            if [x + 1 + i, y, l] in V.events_coordinates:
                                continue
                            if [x + 1 + i, y + 1 + k, l] in V.events_coordinates or [x + 1 + i, y - 1 + k, l] in V.events_coordinates:
                                turns.remove(path)
                                bad_path = True
                                break
                        if bad_path == True:
                            break
                    if bad_path == True:
                        continue
                    for i in range(length):
                        x += 1
                        h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
                        if h > 5:
                            h = 5
                        elif h < 0:
                            h = 0
                        if [x, y, l] in V.events_coordinates:
                            continue
                        if chance(V.snow_pile_spawns[V.area_id]):
                            V.events.append(9)
                        else:
                            V.events.append(0)
                        V.events_coordinates.append([x, y, l])
                        V.events_heights.append(h)
                    x += 1
                    if [x, y, l] in V.events_coordinates:
                        continue
                    if path[3] in V.hurtful_events:
                        if len(good_events) > 0:
                            event = choice(good_events)
                            good_events.remove(event)
                        elif len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.benefitial_events:
                        if len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.neutral_events:
                        if randint(1, 2) == 1:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        else:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            elif len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            else:
                                event = 0
                    else:
                        event = 0
                    V.events.append(event)
                    V.events_coordinates.append([x, y, l])
                    V.events_heights.append(h)
                    if start[0] == "d" or start[0] == "m":
                        if y - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    else:
                        if y - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    if start[1] == "l" or start[1] == "m":
                        if x + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l])
                    else:
                        if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l])
                    if start[0] == "u" or start[0] == "m":
                        if y + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                    else:
                        if y + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                elif path[2] == "d":
                    length = randint(min_length, choice(possible_max_lengths))
                    for k in range(V.wall_min_thickness[V.area_id]):
                        for i in range(length + 1):
                            if [x, y + 1 + i, l] in V.events_coordinates:
                                continue
                            if [x + 1 + k, y + 1 + i, l] in V.events_coordinates or [x - 1 - k, y + 1 + i, l] in V.events_coordinates:
                                turns.remove(path)
                                bad_path = True
                                break
                        if bad_path == True:
                            break
                    if bad_path == True:
                        continue
                    for i in range(length):
                        y += 1
                        h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
                        if h > 5:
                            h = 5
                        elif h < 0:
                            h = 0
                        if [x, y, l] in V.events_coordinates:
                            continue
                        if chance(V.snow_pile_spawns[V.area_id]):
                            V.events.append(9)
                        else:
                            V.events.append(0)
                        V.events_coordinates.append([x, y, l])
                        V.events_heights.append(h)
                    y += 1
                    if [x, y, l] in V.events_coordinates:
                        continue
                    if path[3] in V.hurtful_events:
                        if len(good_events) > 0:
                            event = choice(good_events)
                            good_events.remove(event)
                        elif len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.benefitial_events:
                        if len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.neutral_events:
                        if randint(1, 2) == 1:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        else:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            elif len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            else:
                                event = 0
                    else:
                        event = 0
                    V.events.append(event)
                    V.events_coordinates.append([x, y, l])
                    V.events_heights.append(h)
                    if (V.area_id == 4 and chance(V.turn_down_prob[V.area_id])) or V.area_id != 4 or iteration < 3:
                        if start[1] == "r" or start[1] == "m":
                            if x - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_x[V.area_id] and chance(V.turn_left_prob[V.area_id]):
                                turns.append([x, y, "l", event, h, l])
                        else:
                            if x - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_left_prob[V.area_id]):
                                turns.append([x, y, "l", event, h, l])
                        if start[1] == "l" or start[1] == "m":
                            if x + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                                turns.append([x, y, "r", event, h, l])
                        else:
                            if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                                turns.append([x, y, "r", event, h, l])
                    if start[0] == "u" or start[1] == "m":
                        if y + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                    else:
                        if y + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                elif path[2] == "l":
                    length = randint(min_length, choice(possible_max_lengths))
                    for k in range(V.wall_min_thickness[V.area_id]):
                        for i in range(length + 1):
                            if [x - 1 - i, y, l] in V.events_coordinates:
                                continue
                            if [x - 1 - i, y + 1 + k, l] in V.events_coordinates or [x - 1 - i, y - 1 - k, l] in V.events_coordinates:
                                turns.remove(path)
                                bad_path = True
                                break
                        if bad_path == True:
                            break
                    if bad_path == True:
                        continue
                    for i in range(length):
                        x -= 1
                        h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
                        if h > 5:
                            h = 5
                        elif h < 0:
                            h = 0
                        if [x, y, l] in V.events_coordinates:
                            continue
                        if chance(V.snow_pile_spawns[V.area_id]):
                            V.events.append(9)
                        else:
                            V.events.append(0)
                        V.events_coordinates.append([x, y, l])
                        V.events_heights.append(h)
                    x -= 1
                    if [x, y, l] in V.events_coordinates:
                        continue
                    if path[3] in V.hurtful_events:
                        if len(good_events) > 0:
                            event = choice(good_events)
                            good_events.remove(event)
                        elif len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.benefitial_events:
                        if len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.neutral_events:
                        if randint(1, 2) == 1:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        else:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            elif len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            else:
                                event = 0
                    else:
                        event = 0
                    V.events.append(event)
                    V.events_coordinates.append([x, y, l])
                    V.events_heights.append(h)
                    if start[0] == "d" or start[0] == "m":
                        if y - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    else:
                        if y - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    if start[1] == "r" or start[1] == "m":
                        if x - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_x[V.area_id] and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l])
                    else:
                        if x - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l])
                    if start[0] == "u" or start[0] == "m":
                        if y + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                    else:
                        if y + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                elif path[2] == "u":
                    length = randint(min_length, choice(possible_max_lengths))
                    for k in range(V.wall_min_thickness[V.area_id]):
                        for i in range(length + 1):
                            if [x, y - 1 - i, l] in V.events_coordinates:
                                continue
                            if [x + 1 + k, y - 1 - i, l] in V.events_coordinates or [x - 1 - k, y - 1 - i, l] in V.events_coordinates:
                                turns.remove(path)
                                bad_path = True
                                break
                        if bad_path == True:
                            break
                    if bad_path == True:
                        continue
                    for i in range(length):
                        y -= 1
                        h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
                        if h > 5:
                            h = 5
                        elif h < 0:
                            h = 0
                        if [x, y, l] in V.events_coordinates:
                            continue
                        if chance(V.snow_pile_spawns[V.area_id]):
                            V.events.append(9)
                        else:
                            V.events.append(0)
                        V.events_coordinates.append([x, y, l])
                        V.events_heights.append(h)
                    y -= 1
                    if [x, y, l] in V.events_coordinates:
                        continue
                    if path[3] in V.hurtful_events:
                        if len(good_events) > 0:
                            event = choice(good_events)
                            good_events.remove(event)
                        elif len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.benefitial_events:
                        if len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.neutral_events:
                        if randint(1, 2) == 1:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        else:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            elif len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            else:
                                event = 0
                    else:
                        event = 0
                    V.events.append(event)
                    V.events_coordinates.append([x, y, l])
                    V.events_heights.append(h)
                    if start[0] == "d" or start[0] == "m":
                        if y - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    else:
                        if y - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    if start[1] == "r" or start[1] == "m":
                        if x - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_x[V.area_id] and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l])
                    else:
                        if x - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l])
                    if start[1] == "l" or start[1] == "m":
                        if x + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l])
                    else:
                        if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l])
                turns.remove(path)


        elif V.generation_area_pattern[0][pattern_index] == "basic water":
            # water landmarks
            water_turns = []
            river_chance = V.river_prob[V.area_id]
            l = generation_layer
            while river_chance > 0:
                if chance(river_chance):
                    if chance(0.5):
                        # horizontal start
                        if chance(0.5):
                            x = min_x(V)
                            direction = "r"
                        else:
                            x = max_x(V)
                            direction = "l"
                        y = randint(min_y(V), max_y(V) - 1)
                    else:
                        # vertical start
                        if chance(0.5):
                            y = min_y(V)
                            direction = "d"
                        else:
                            y = max_y(V)
                            direction = "u"
                        x = randint(min_x(V), max_x(V) - 1)
                    while True:
                        for i in range(V.river_thickness[V.area_id]):
                            if direction == "r" or direction == "l":
                                if not y + i > max_y(V):
                                    if not [x, y + i, l] in V.events_coordinates:
                                        V.events.append(10)
                                        V.events_coordinates.append([x, y + i, l])
                                        V.events_heights.append(0)
                                    else:
                                        V.events_heights[V.events_coordinates.index([x, y + i, l])] = 0
                            if direction == "u" or direction == "d":
                                if not x + i > max_x(V):
                                    if not [x + i, y, l] in V.events_coordinates:
                                        V.events.append(10)
                                        V.events_coordinates.append([x + i, y, l])
                                        V.events_heights.append(0)
                                    else:
                                        V.events_heights[V.events_coordinates.index([x + i, y, l])] = 0
                        if direction == "r":
                            x += 1
                            if chance(0.2):
                                if chance(0.5):
                                    direction = "u"
                                else:
                                    direction = "d"
                                water_turns.append([x, y, "r", l])
                        elif direction == "d":
                            y += 1
                            if chance(0.2):
                                if chance(0.5):
                                    direction = "l"
                                else:
                                    direction = "r"
                                water_turns.append([x, y, "d", l])
                        elif direction == "l":
                            x -= 1
                            if chance(0.2):
                                if chance(0.5):
                                    direction = "u"
                                else:
                                    direction = "d"
                                water_turns.append([x, y, "l", l])
                        elif direction == "u":
                            y -= 1
                            if chance(0.2):
                                if chance(0.5):
                                    direction = "l"
                                else:
                                    direction = "r"
                                water_turns.append([x, y, "u", l])
                        if x > max_x(V) or y > max_y(V) or x < min_x(V) or y < min_y(V):
                            break
                        river_chance -= 0.01
                river_chance -= 0.25

            pond_chance = V.pond_prob[V.area_id]
            if chance(pond_chance):
                x = (min_x(V) + max_x(V)) // 2
                y = (min_y(V) + max_y(V)) // 2
                V.pond_radius[V.area_id] = abs(V.pond_radius[V.area_id])
                x1 = x - V.pond_radius[V.area_id]
                y1 = y + V.pond_radius[V.area_id]
                while [x1, y1, l] != [x - V.pond_radius[V.area_id], y - V.pond_radius[V.area_id], l]:
                    if not [x1, y1, l] in V.events_coordinates:
                        V.events.append(10)
                        V.events_coordinates.append([x1, y1, l])
                        V.events_heights.append(0)
                    else:
                        V.events_heights[V.events_coordinates.index([x1, y1, l])] = 0
                    y1 -= 1
                while [x1, y1, l] != [x + V.pond_radius[V.area_id], y - V.pond_radius[V.area_id], l]:
                    if not [x1, y1, l] in V.events_coordinates:
                        V.events.append(10)
                        V.events_coordinates.append([x1, y1, l])
                        V.events_heights.append(0)
                    else:
                        V.events_heights[V.events_coordinates.index([x1, y1, l])] = 0
                    x1 += 1
                while [x1, y1, l] != [x + V.pond_radius[V.area_id], y + V.pond_radius[V.area_id], l]:
                    if not [x1, y1, l] in V.events_coordinates:
                        V.events.append(10)
                        V.events_coordinates.append([x1, y1, l])
                        V.events_heights.append(0)
                    else:
                        V.events_heights[V.events_coordinates.index([x1, y1, l])] = 0
                    y1 += 1
                while [x1, y1, l] != [x - V.pond_radius[V.area_id], y + V.pond_radius[V.area_id], l]:
                    if not [x1, y1, l] in V.events_coordinates:
                        V.events.append(10)
                        V.events_coordinates.append([x1, y1, l])
                        V.events_heights.append(0)
                    else:
                        V.events_heights[V.events_coordinates.index([x1, y1, l])] = 0
                    x1 -= 1

            if chance(V.escape_river_prob[V.area_id]) and V.escape_amount <= 1 and V.game_mode in ["infinite", "story"]:
                if len(water_turns) > 0:
                    turn = choice(water_turns)
                else:
                    turn = [(min_x(V) + max_x(V)) // 2, -1, "d", l]
                x, y = turn[0], turn[1]
                if turn[2] == "r":
                    while x + 1 < max_x(V):
                        x += 1
                        if not [x, y, l] in V.events_coordinates:
                            V.events.append(10)
                            V.events_coordinates.append([x, y, l])
                            V.events_heights.append(0)
                        else:
                            V.events_heights[V.events_coordinates.index([x, y, l])] = 0
                    x += 1
                elif turn[2] == "d":
                    while y + 1 < max_y(V):
                        y += 1
                        if not [x, y, l] in V.events_coordinates:
                            V.events.append(10)
                            V.events_coordinates.append([x, y, l])
                            V.events_heights.append(0)
                        else:
                            V.events_heights[V.events_coordinates.index([x, y, l])] = 0
                    y += 1
                elif turn[2] == "l":
                    while x - 1 > 0:
                        x -= 1
                        if not [x, y, l] in V.events_coordinates:
                            V.events.append(10)
                            V.events_coordinates.append([x, y, l])
                            V.events_heights.append(0)
                        else:
                            V.events_heights[V.events_coordinates.index([x, y, l])] = 0
                    x -= 1
                elif turn[2] == "u":
                    while y - 1 > 0:
                        y -= 1
                        if not [x, y, l] in V.events_coordinates:
                            V.events.append(10)
                            V.events_coordinates.append([x, y, l])
                            V.events_heights.append(0)
                        else:
                            V.events_heights[V.events_coordinates.index([x, y, l])] = 0
                    y -= 1
                if not [x, y, l] in V.events_coordinates:
                    V.events.append(12)
                    V.events_coordinates.append([x, y, l])
                    V.events_heights.append(0)
                else:
                    if not V.events[V.events_coordinates.index([x, y, l])] in [3, 4, 5, 11, 13, 19, 24, 21, 22] and [x, y, l] != V.player_coordinates:
                        V.events[V.events_coordinates.index([x, y, l])] = 12
                    V.events_heights[V.events_coordinates.index([x, y, l])] = 0


        elif V.generation_area_pattern[0][pattern_index] == "isolated remnants":
            l = generation_layer
            for event in range(0, len(V.events), 3):
                if V.events[event] == 10:
                    x, y = V.events_coordinates[event][0], V.events_coordinates[event][1]
                    if [x + 1, y, l] in V.events_coordinates:
                        if V.events[V.events_coordinates.index([x + 1, y, l])] != 10:
                            continue
                    if [x - 1, y, l] in V.events_coordinates:
                        if V.events[V.events_coordinates.index([x - 1, y, l])] != 10:
                            continue
                    if [x, y + 1, l] in V.events_coordinates:
                        if V.events[V.events_coordinates.index([x, y + 1, l])] != 10:
                            continue
                    if [x, y - 1, l] in V.events_coordinates:
                        if V.events[V.events_coordinates.index([x, y - 1, l])] != 10:
                            continue
                    V.events[event] = 14
                    break


        elif V.generation_area_pattern[0][pattern_index] == "small boxes":
            x = 0
            y = 0
            iteration = 0

            overleft_event_amount = event_amount - event_amount * generation_percentage - placed_event_amount
            if overleft_event_amount < 0:
                overleft_event_amount = 0

            while len(good_events) + len(bad_events) > overleft_event_amount:
                iteration += 1
                bad_path = False
                if iteration > 1000:
                    break
                path = choice(turns)
                x = path[0]
                y = path[1]
                h = path[4] + randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
                l = path[5]
                if l != generation_layer:
                    iteration -= 0.75
                    continue
                if path[2] == "r":
                    for x1 in range(5):
                        for y1 in range(5):
                            if [x + x1, y - 2 + y1, l] in V.events_coordinates and not [x + x1, y - 2 + y1, l] in [[x, y, l], [x + 2, y - 2, l], [x + 4, y, l], [x + 2, y + 2, l]]:
                                bad_path = True
                                break
                        if bad_path:
                            break
                    if bad_path:
                        continue
                    V.events_heights = V.events_heights + [0, h, h, h, h, h, h, h, h]
                    V.events_coordinates = V.events_coordinates + [[x + 2, y, l], [x + 1, y, l], [x + 1, y - 1, l], [x + 1, y + 1, l]]
                    V.events = V.events + [10, 0, 0, 0]
                    if not [x + 2, y - 2, l] in V.events_coordinates:
                        V.events_coordinates.append([x + 2, y - 2, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    V.events_coordinates = V.events_coordinates + [[x + 2, y - 1, l], [x + 2, y + 1, l]]
                    V.events = V.events + [0, 0]
                    if not [x + 2, y + 2, l] in V.events_coordinates:
                        V.events_coordinates.append([x + 2, y + 2, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    V.events_coordinates = V.events_coordinates + [[x + 3, y - 1, l], [x + 3, y, l], [x + 3, y + 1, l]]
                    V.events = V.events + [0, 0, 0]
                    if not [x + 4, y, l] in V.events_coordinates:
                        V.events_coordinates.append([x + 4, y, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    if start[0] == "d" or start[0] == "m":
                        if y - 2 - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x + 2, y - 2, "u", event, h, l])
                    else:
                        if y - 2 - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x + 2, y - 2, "u", event, h, l])
                    if start[1] == "l" or start[1] == "m":
                        if x + 4 + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x + 4, y, "r", event, h, l])
                    else:
                        if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x + 4, y, "r", event, h, l])
                    if start[0] == "u" or start[0] == "m":
                        if y + 2 + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x + 2, y + 2, "d", event, h, l])
                    else:
                        if y + 2 + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x + 2, y + 2, "d", event, h, l])
                elif path[2] == "d":
                    for x1 in range(5):
                        for y1 in range(5):
                            if [x + x1 - 2, y + y1, l] in V.events_coordinates and not [x + x1 - 2, y + y1, l] in [[x, y, l], [x - 2, y + 2, l], [x + 2, y + 2, l], [x, y + 4, l]]:
                                bad_path = True
                                break
                        if bad_path:
                            break
                    if bad_path:
                        continue
                    V.events_heights = V.events_heights + [0, h, h, h, h, h, h, h, h]
                    V.events_coordinates = V.events_coordinates + [[x, y + 2, l], [x - 1, y + 1, l], [x, y + 1, l], [x + 1, y + 1, l]]
                    V.events = V.events + [10, 0, 0, 0]
                    if not [x - 2, y + 2, l] in V.events_coordinates:
                        V.events_coordinates.append([x - 2, y + 2, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    V.events_coordinates = V.events_coordinates + [[x - 1, y + 2, l], [x + 1, y + 2, l]]
                    V.events = V.events + [0, 0]
                    if not [x + 2, y + 2, l] in V.events_coordinates:
                        V.events_coordinates.append([x + 2, y + 2, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    V.events_coordinates = V.events_coordinates + [[x - 1, y + 3, l], [x, y + 3, l], [x + 1, y + 3, l]]
                    V.events = V.events + [0, 0, 0]
                    if not [x, y + 4, l] in V.events_coordinates:
                        V.events_coordinates.append([x, y + 4, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    if start[0] == "r" or start[0] == "m":
                        if y - 2 - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x - 2, y + 2, "l", event, h, l])
                    else:
                        if y - 2 - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x - 2, y + 2, "l", event, h, l])
                    if start[1] == "l" or start[1] == "m":
                        if x + 4 + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x + 2, y + 2, "r", event, h, l])
                    else:
                        if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x + 2, y + 2, "r", event, h, l])
                    if start[0] == "u" or start[0] == "m":
                        if y + 2 + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y + 4, "d", event, h, l])
                    else:
                        if y + 2 + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y + 4, "d", event, h, l])
                elif path[2] == "l":
                    for x1 in range(5):
                        for y1 in range(5):
                            if [x + x1 - 4, y - 2 + y1, l] in V.events_coordinates and not [x + x1 - 4, y - 2 + y1, l] in [[x, y, l], [x - 2, y - 2, l], [x - 2, y + 2, l], [x - 4, y, l]]:
                                bad_path = True
                                break
                        if bad_path:
                            break
                    if bad_path:
                        continue
                    V.events_heights = V.events_heights + [0, h, h, h, h, h, h, h, h]
                    V.events_coordinates = V.events_coordinates + [[x - 2, y, l], [x - 1, y, l], [x - 1, y - 1, l], [x - 1, y + 1, l]]
                    V.events = V.events + [10, 0, 0, 0]
                    if not [x - 2, y - 2, l] in V.events_coordinates:
                        V.events_coordinates.append([x - 2, y - 2, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    V.events_coordinates = V.events_coordinates + [[x - 2, y - 1, l], [x - 2, y + 1, l]]
                    V.events = V.events + [0, 0]
                    if not [x - 2, y + 2, l] in V.events_coordinates:
                        V.events_coordinates.append([x - 2, y + 2, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    V.events_coordinates = V.events_coordinates + [[x - 3, y - 1, l], [x - 3, y, l], [x - 3, y + 1, l]]
                    V.events = V.events + [0, 0, 0]
                    if not [x - 4, y, l] in V.events_coordinates:
                        V.events_coordinates.append([x - 4, y, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    if start[0] == "d" or start[0] == "m":
                        if y - 2 - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x - 2, y - 2, "u", event, h, l])
                    else:
                        if y - 2 - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x - 2, y - 2, "u", event, h, l])
                    if start[1] == "r" or start[1] == "m":
                        if x + 4 + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x - 4, y, "l", event, h, l])
                    else:
                        if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x - 4, y, "r", event, h, l])
                    if start[0] == "u" or start[0] == "m":
                        if y + 2 + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x - 2, y + 2, "d", event, h, l])
                    else:
                        if y + 2 + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x - 2, y + 2, "d", event, h, l])
                elif path[2] == "u":
                    for x1 in range(5):
                        for y1 in range(5):
                            if [x + x1 - 2, y + y1 - 4, l] in V.events_coordinates and not [x + x1 - 2, y + y1 - 4, l] in [[x, y, l], [x - 2, y - 2, l], [x + 2, y - 2, l], [x, y - 4, l]]:
                                bad_path = True
                                break
                        if bad_path:
                            break
                    if bad_path:
                        continue
                    V.events_heights = V.events_heights + [0, h, h, h, h, h, h, h, h]
                    V.events_coordinates = V.events_coordinates + [[x, y - 2, l], [x - 1, y - 1, l], [x, y - 1, l], [x + 1, y - 1, l]]
                    V.events = V.events + [10, 0, 0, 0]
                    if not [x - 2, y - 2, l] in V.events_coordinates:
                        V.events_coordinates.append([x - 2, y - 2, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    V.events_coordinates = V.events_coordinates + [[x - 1, y - 2, l], [x + 1, y - 2, l]]
                    V.events = V.events + [0, 0]
                    if not [x + 2, y - 2, l] in V.events_coordinates:
                        V.events_coordinates.append([x + 2, y - 2, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    V.events_coordinates = V.events_coordinates + [[x - 1, y - 3, l], [x, y - 3, l], [x + 1, y - 3, l]]
                    V.events = V.events + [0, 0, 0]
                    if not [x, y - 4, l] in V.events_coordinates:
                        V.events_coordinates.append([x, y - 4, l])
                        V.events_heights.append(h)
                        if path[3] in V.hurtful_events:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.benefitial_events:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        elif path[3] in V.neutral_events:
                            if randint(1, 2) == 1:
                                if len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                elif len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                else:
                                    event = 0
                            else:
                                if len(bad_events) > 0:
                                    event = choice(bad_events)
                                    bad_events.remove(event)
                                elif len(good_events) > 0:
                                    event = choice(good_events)
                                    good_events.remove(event)
                                else:
                                    event = 0
                        V.events.append(event)
                    if start[0] == "r" or start[0] == "m":
                        if y - 2 - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x - 2, y - 2, "l", event, h, l])
                    else:
                        if y - 2 - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x - 2, y - 2, "l", event, h, l])
                    if start[1] == "l" or start[1] == "m":
                        if x + 4 + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x + 2, y - 2, "r", event, h, l])
                    else:
                        if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x + 2, y - 2, "r", event, h, l])
                    if start[0] == "d" or start[0] == "m":
                        if y + 2 + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y - 4, "u", event, h, l])
                    else:
                        if y + 2 + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y - 4, "u", event, h, l])
                turns.remove(path)

                
        elif V.generation_area_pattern[0][pattern_index] == "change's crystal":
            epic_tiles = []
            for i in range(len(V.events)):
                epic_tiles.append(i)
            while len(epic_tiles) > 0:
                tile_index = choice(epic_tiles)
                if V.events[tile_index] == 0:
                    V.events[tile_index] = 15
                    break
                else:
                    epic_tiles.remove(tile_index)

                    
        elif V.generation_area_pattern[0][pattern_index] == "basic only horizontal":
            x = 0
            y = 0
            iteration = 0

            min_length = round(V.path_lengths[V.area_id][0] - (V.map_complexity * 0.05))
            if min_length < 0:
                min_length = 0
            possible_max_lengths = [V.path_lengths[V.area_id][1]]
            for i in range(V.map_complexity):
                max_length = round(V.path_lengths[V.area_id][1] - i * 0.3)
                if max_length < min_length:
                    max_length = min_length
                possible_max_lengths.append(max_length)

            overleft_event_amount = event_amount - event_amount * generation_percentage - placed_event_amount
            if overleft_event_amount < 0:
                overleft_event_amount = 0

            while len(good_events) + len(bad_events) > overleft_event_amount:
                iteration += 1
                bad_path = False
                if iteration > 1000:
                    break
                path = choice(turns)
                x = path[0]
                y = path[1]
                h = path[4]
                l = path[5]
                if l != generation_layer:
                    iteration -= 0.75
                    continue
                if path[2] == "r":
                    length = randint(min_length, choice(possible_max_lengths))
                    for k in range(V.wall_min_thickness[V.area_id]):
                        for i in range(length + 1):
                            if [x + 1 + i, y, l] in V.events_coordinates:
                                continue
                            if [x + 1 + i, y + 1 + k, l] in V.events_coordinates or [x + 1 + i, y - 1 + k, l] in V.events_coordinates:
                                turns.remove(path)
                                bad_path = True
                                break
                        if bad_path == True:
                            break
                    if bad_path == True:
                        continue
                    for i in range(length):
                        x += 1
                        h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
                        if h > 5:
                            h = 5
                        elif h < 0:
                            h = 0
                        if [x, y, l] in V.events_coordinates:
                            continue
                        if chance(V.snow_pile_spawns[V.area_id]):
                            V.events.append(9)
                        else:
                            V.events.append(0)
                        V.events_coordinates.append([x, y, l])
                        V.events_heights.append(h)
                    x += 1
                    if [x, y, l] in V.events_coordinates:
                        continue
                    if path[3] in V.hurtful_events:
                        if len(good_events) > 0:
                            event = choice(good_events)
                            good_events.remove(event)
                        elif len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.benefitial_events:
                        if len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.neutral_events:
                        if randint(1, 2) == 1:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        else:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            elif len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            else:
                                event = 0
                    else:
                        event = 0
                    V.events.append(event)
                    V.events_coordinates.append([x, y, l])
                    V.events_heights.append(h)
                    if start[0] == "d" or start[0] == "m":
                        if y - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    else:
                        if y - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    if start[1] == "l" or start[1] == "m":
                        if x + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l])
                    else:
                        if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l])
                    if start[0] == "u" or start[0] == "m":
                        if y + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                    else:
                        if y + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                elif path[2] == "l":
                    length = randint(min_length, choice(possible_max_lengths))
                    for k in range(V.wall_min_thickness[V.area_id]):
                        for i in range(length + 1):
                            if [x - 1 - i, y, l] in V.events_coordinates:
                                continue
                            if [x - 1 - i, y + 1 + k, l] in V.events_coordinates or [x - 1 - i, y - 1 - k, l] in V.events_coordinates:
                                turns.remove(path)
                                bad_path = True
                                break
                        if bad_path == True:
                            break
                    if bad_path == True:
                        continue
                    for i in range(length):
                        x -= 1
                        h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
                        if h > 5:
                            h = 5
                        elif h < 0:
                            h = 0
                        if [x, y, l] in V.events_coordinates:
                            continue
                        if chance(V.snow_pile_spawns[V.area_id]):
                            V.events.append(9)
                        else:
                            V.events.append(0)
                        V.events_coordinates.append([x, y, l])
                        V.events_heights.append(h)
                    x -= 1
                    if [x, y, l] in V.events_coordinates:
                        continue
                    if path[3] in V.hurtful_events:
                        if len(good_events) > 0:
                            event = choice(good_events)
                            good_events.remove(event)
                        elif len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.benefitial_events:
                        if len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.neutral_events:
                        if randint(1, 2) == 1:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        else:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            elif len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            else:
                                event = 0
                    else:
                        event = 0
                    V.events.append(event)
                    V.events_coordinates.append([x, y, l])
                    V.events_heights.append(h)
                    if start[0] == "d" or start[0] == "m":
                        if y - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    else:
                        if y - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    if start[1] == "r" or start[1] == "m":
                        if x - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_x[V.area_id] and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l])
                    else:
                        if x - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l])
                    if start[0] == "u" or start[0] == "m":
                        if y + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                    else:
                        if y + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                turns.remove(path)

                    
        elif V.generation_area_pattern[0][pattern_index] == "basic only vertical":
            x = 0
            y = 0
            iteration = 0

            min_length = round(V.path_lengths[V.area_id][0] - (V.map_complexity * 0.05))
            if min_length < 0:
                min_length = 0
            possible_max_lengths = [V.path_lengths[V.area_id][1]]
            for i in range(V.map_complexity):
                max_length = round(V.path_lengths[V.area_id][1] - i * 0.3)
                if max_length < min_length:
                    max_length = min_length
                possible_max_lengths.append(max_length)

            overleft_event_amount = event_amount - event_amount * generation_percentage - placed_event_amount
            if overleft_event_amount < 0:
                overleft_event_amount = 0

            while len(good_events) + len(bad_events) > overleft_event_amount:
                iteration += 1
                bad_path = False
                if iteration > 1000:
                    break
                path = choice(turns)
                x = path[0]
                y = path[1]
                h = path[4]
                l = path[5]
                if l != generation_layer:
                    iteration -= 0.75
                    continue
                if path[2] == "d":
                    length = randint(min_length, choice(possible_max_lengths))
                    for k in range(V.wall_min_thickness[V.area_id]):
                        for i in range(length + 1):
                            if [x, y + 1 + i, l] in V.events_coordinates:
                                continue
                            if [x + 1 + k, y + 1 + i, l] in V.events_coordinates or [x - 1 - k, y + 1 + i, l] in V.events_coordinates:
                                turns.remove(path)
                                bad_path = True
                                break
                        if bad_path == True:
                            break
                    if bad_path == True:
                        continue
                    for i in range(length):
                        y += 1
                        h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
                        if h > 5:
                            h = 5
                        elif h < 0:
                            h = 0
                        if [x, y, l] in V.events_coordinates:
                            continue
                        if chance(V.snow_pile_spawns[V.area_id]):
                            V.events.append(9)
                        else:
                            V.events.append(0)
                        V.events_coordinates.append([x, y, l])
                        V.events_heights.append(h)
                    y += 1
                    if [x, y, l] in V.events_coordinates:
                        continue
                    if path[3] in V.hurtful_events:
                        if len(good_events) > 0:
                            event = choice(good_events)
                            good_events.remove(event)
                        elif len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.benefitial_events:
                        if len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.neutral_events:
                        if randint(1, 2) == 1:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        else:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            elif len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            else:
                                event = 0
                    else:
                        event = 0
                    V.events.append(event)
                    V.events_coordinates.append([x, y, l])
                    V.events_heights.append(h)
                    if (V.area_id == 4 and chance(V.turn_down_prob[V.area_id])) or V.area_id != 4 or iteration < 3:
                        if start[1] == "r" or start[1] == "m":
                            if x - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_x[V.area_id] and chance(V.turn_left_prob[V.area_id]):
                                turns.append([x, y, "l", event, h, l])
                        else:
                            if x - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_left_prob[V.area_id]):
                                turns.append([x, y, "l", event, h, l])
                        if start[1] == "l" or start[1] == "m":
                            if x + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                                turns.append([x, y, "r", event, h, l])
                        else:
                            if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                                turns.append([x, y, "r", event, h, l])
                    if start[0] == "u" or start[1] == "m":
                        if y + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                    else:
                        if y + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l])
                elif path[2] == "u":
                    length = randint(min_length, choice(possible_max_lengths))
                    for k in range(V.wall_min_thickness[V.area_id]):
                        for i in range(length + 1):
                            if [x, y - 1 - i, l] in V.events_coordinates:
                                continue
                            if [x + 1 + k, y - 1 - i, l] in V.events_coordinates or [x - 1 - k, y - 1 - i, l] in V.events_coordinates:
                                turns.remove(path)
                                bad_path = True
                                break
                        if bad_path == True:
                            break
                    if bad_path == True:
                        continue
                    for i in range(length):
                        y -= 1
                        h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
                        if h > 5:
                            h = 5
                        elif h < 0:
                            h = 0
                        if [x, y, l] in V.events_coordinates:
                            continue
                        if chance(V.snow_pile_spawns[V.area_id]):
                            V.events.append(9)
                        else:
                            V.events.append(0)
                        V.events_coordinates.append([x, y, l])
                        V.events_heights.append(h)
                    y -= 1
                    if [x, y, l] in V.events_coordinates:
                        continue
                    if path[3] in V.hurtful_events:
                        if len(good_events) > 0:
                            event = choice(good_events)
                            good_events.remove(event)
                        elif len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.benefitial_events:
                        if len(bad_events) > 0:
                            event = choice(bad_events)
                            bad_events.remove(event)
                        else:
                            event = 0
                    elif path[3] in V.neutral_events:
                        if randint(1, 2) == 1:
                            if len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            elif len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            else:
                                event = 0
                        else:
                            if len(bad_events) > 0:
                                event = choice(bad_events)
                                bad_events.remove(event)
                            elif len(good_events) > 0:
                                event = choice(good_events)
                                good_events.remove(event)
                            else:
                                event = 0
                    else:
                        event = 0
                    V.events.append(event)
                    V.events_coordinates.append([x, y, l])
                    V.events_heights.append(h)
                    if start[0] == "d" or start[0] == "m":
                        if y - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    else:
                        if y - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l])
                    if start[1] == "r" or start[1] == "m":
                        if x - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_x[V.area_id] and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l])
                    else:
                        if x - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l])
                    if start[1] == "l" or start[1] == "m":
                        if x + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l])
                    else:
                        if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l])
                turns.remove(path)


        elif V.generation_area_pattern[0][pattern_index] == "holes down":
            for i in range(int(len(turns) * generation_percentage) + 1):
                if len(turns) == 0:
                    break
                path = choice(turns)
                x = path[0]
                y = path[1]
                l = path[5]
                if l != generation_layer:
                    can_generate = False
                    for test_path in turns:
                        if test_path[5] == generation_layer:
                            can_generate = True
                    if can_generate == False:
                        break
                    while l != generation_layer:
                        path = choice(turns)
                        x = path[0]
                        y = path[1]
                        l = path[5]
                event = 21
                if not [x, y, l - 1] in V.events_coordinates:
                    if [x, y, l + 1] in V.events_coordinates:
                        if V.events[V.events_coordinates.index([x, y, l + 1])] == 21:
                            continue
                    turns.remove(path)
                    if [x, y, l] in V.events_coordinates:
                        V.events[V.events_coordinates.index([x, y, l])] = 21
                        V.events_heights[V.events_coordinates.index([x, y, l])] = 0
                    else:
                        V.events.append(21)
                        V.events_coordinates.append(x, y, l)
                        V.events_heights.append(0)
                    V.events_coordinates.append([x, y, l - 1])
                    V.events_heights.append(5)
                    V.events.append(22)
                    if start[0] == "d" or start[0] == "m":
                        if y - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l - 1])
                    else:
                        if y - (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l - 1])
                    if start[1] == "l" or start[1] == "m":
                        if x + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l - 1])
                    else:
                        if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l - 1])
                    if start[0] == "u" or start[0] == "m":
                        if y + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l - 1])
                    else:
                        if y + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l - 1])
                    if start[1] == "r" or start[1] == "m":
                        if x - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_x[V.area_id] and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l - 1])
                    else:
                        if x - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l - 1])


        elif V.generation_area_pattern[0][pattern_index] == "holes up":
            for i in range(int(len(turns) * generation_percentage) + 1):
                if len(turns) == 0:
                    break
                path = choice(turns)
                x = path[0]
                y = path[1]
                l = path[5]
                if l != generation_layer:
                    continue
                event = 22
                if not [x, y, l + 1] in V.events_coordinates:
                    if [x, y, l - 1] in V.events_coordinates:
                        if V.events[V.events_coordinates.index([x, y, l - 1])] == 22:
                            continue
                    turns.remove(path)
                    if [x, y, l] in V.events_coordinates:
                        V.events[V.events_coordinates.index([x, y, l])] = 22
                        V.events_heights[V.events_coordinates.index([x, y, l])] = 5
                    else:
                        V.events.append(22)
                        V.events_coordinates.append(x, y, l)
                        V.events_heights.append(5)
                    V.events_coordinates.append([x, y, l + 1])
                    V.events_heights.append(5)
                    V.events.append(21)
                    if start[0] == "d" or start[0] == "m":
                        if y - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_y[V.area_id] and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l + 1])
                    else:
                        if y - (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_up_prob[V.area_id]):
                            turns.append([x, y, "u", event, h, l + 1])
                    if start[1] == "l" or start[1] == "m":
                        if x + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_x[V.area_id] and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l + 1])
                    else:
                        if x + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_right_prob[V.area_id]):
                            turns.append([x, y, "r", event, h, l + 1])
                    if start[0] == "u" or start[0] == "m":
                        if y + (V.path_lengths[V.area_id][1] + 1) <= V.area_max_y[V.area_id] and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l + 1])
                    else:
                        if y + (V.path_lengths[V.area_id][1] + 1) <= 0 and chance(V.turn_down_prob[V.area_id]):
                            turns.append([x, y, "d", event, h, l + 1])
                    if start[1] == "r" or start[1] == "m":
                        if x - (V.path_lengths[V.area_id][1] + 1) >= - V.area_max_x[V.area_id] and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l + 1])
                    else:
                        if x - (V.path_lengths[V.area_id][1] + 1) >= 0 and chance(V.turn_left_prob[V.area_id]):
                            turns.append([x, y, "l", event, h, l + 1])


        placed_event_amount = event_amount - len(bad_events) - len(good_events)


    cur_max_xy = 0
    furthest_turn_index = 0
    for i in turns:
        cur_xy = 0
        if start[0] == "u":
            cur_xy += i[1]
        elif start[0] == "d":
            cur_xy += - i[1]
        else:
            cur_xy += abs(i[1])
        if start[1] == "l":
            cur_xy += i[0]
        elif start[1] == "r":
            cur_xy += - i[0]
        else:
            cur_xy += abs(i[0])
        if cur_xy > cur_max_xy:
            cur_max_xy = cur_xy
            furthest_turn_index = turns.index(i)
        elif cur_xy == cur_max_xy:
            if start[0] == "u" and turns[furthest_turn_index][2] != "d":
                if start[1] == "l" and turns[furthest_turn_index][2] != "r":
                    furthest_turn_index = turns.index(i)
                elif start[1] == "r" and turns[furthest_turn_index][2] != "l":
                    furthest_turn_index = turns.index(i)
                elif start[1] == "m" and i[2] == "l" and i[0] < 0:
                    furthest_turn_index = turns.index(i)
                elif start[1] == "m" and i[2] == "r" and i[0] > 0:
                    furthest_turn_index = turns.index(i)
            elif start[0] == "d" and turns[furthest_turn_index][2] != "u":
                if start[1] == "l" and turns[furthest_turn_index][2] != "r":
                    furthest_turn_index = turns.index(i)
                elif start[1] == "r" and turns[furthest_turn_index][2] != "l":
                    furthest_turn_index = turns.index(i)
                elif start[1] == "m" and i[2] == "l" and i[0] < 0:
                    furthest_turn_index = turns.index(i)
                elif start[1] == "m" and i[2] == "r" and i[0] > 0:
                    furthest_turn_index = turns.index(i)
            elif start[1] == "l" and turns[furthest_turn_index][2] != "r":
                furthest_turn_index = turns.index(i)
            elif start[1] == "r" and turns[furthest_turn_index][2] != "l":
                furthest_turn_index = turns.index(i)
    path = turns[furthest_turn_index]
    if start == "mm":
        if path[0] < 0 and abs(path[0]) > abs(path[1]):
            path = [path[0], path[1], "l", path[3], path[4], path[5]]
        elif path[0] > 0 and abs(path[0]) > abs(path[1]):
            path = [path[0], path[1], "r", path[3], path[4], path[5]]
        elif path[1] < 0 and abs(path[0]) < abs(path[1]):
            path = [path[0], path[1], "u", path[3], path[4], path[5]]
        elif path[1] > 0 and abs(path[0]) < abs(path[1]):
            path = [path[0], path[1], "d", path[3], path[4], path[5]]
    x = path[0]
    y = path[1]
    h = path[4]
    l = path[5]
    if path[2] == "r":
        for i in range(randint(V.path_lengths[V.area_id][1], V.path_lengths[V.area_id][1])):
            x += 1
            h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
            if h > 5:
                h = 5
            elif h < 0:
                h = 0
            if [x, y, l] in V.events_coordinates:
                if V.events[V.events_coordinates.index([x, y, l])] != 10:
                    continue
                else:
                    if chance(V.snow_pile_spawns[V.area_id]):
                        V.events[V.events_coordinates.index([x, y, l])] = 9
                    else:
                        V.events[V.events_coordinates.index([x, y, l])] = 0
            if chance(V.snow_pile_spawns[V.area_id]):
                V.events.append(9)
            else:
                V.events.append(0)
            V.events_coordinates.append([x, y, l])
            V.events_heights.append(h)
        x += 1
        if [x, y, l] in V.events_coordinates:
            V.events[V.events_coordinates.index([x, y, l])] = 4
            try:
                V.events_heights[V.events_coordinates.index([x, y, l])] = h
            except:
                V.events_heights.append(h)
        else:
            V.events.append(4)
            V.events_coordinates.append([x, y, l])
            V.events_heights.append(h)
    elif path[2] == "d":
        for i in range(randint(V.path_lengths[V.area_id][1], V.path_lengths[V.area_id][1])):
            y += 1
            h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
            if h > 5:
                h = 5
            elif h < 0:
                h = 0
            if [x, y, l] in V.events_coordinates:
                if V.events[V.events_coordinates.index([x, y, l])] != 10:
                    continue
                else:
                    if chance(V.snow_pile_spawns[V.area_id]):
                        V.events[V.events_coordinates.index([x, y, l])] = 9
                    else:
                        V.events[V.events_coordinates.index([x, y, l])] = 0
            if chance(V.snow_pile_spawns[V.area_id]):
                V.events.append(9)
            else:
                V.events.append(0)
            V.events_coordinates.append([x, y, l])
            V.events_heights.append(h)
        y += 1
        if [x, y, l] in V.events_coordinates:
            V.events[V.events_coordinates.index([x, y, l])] = 4
            try:
                V.events_heights[V.events_coordinates.index([x, y, l])] = h
            except:
                V.events_heights.append(h)
        else:
            V.events.append(4)
            V.events_coordinates.append([x, y, l])
            V.events_heights.append(h)
    elif path[2] == "l":
        for i in range(randint(V.path_lengths[V.area_id][1], V.path_lengths[V.area_id][1])):
            x -= 1
            h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
            if h > 5:
                h = 5
            elif h < 0:
                h = 0
            if [x, y, l] in V.events_coordinates:
                if V.events[V.events_coordinates.index([x, y, l])] != 10:
                    continue
                else:
                    if chance(V.snow_pile_spawns[V.area_id]):
                        V.events[V.events_coordinates.index([x, y, l])] = 9
                    else:
                        V.events[V.events_coordinates.index([x, y, l])] = 0
            if chance(V.snow_pile_spawns[V.area_id]):
                V.events.append(9)
            else:
                V.events.append(0)
            V.events_coordinates.append([x, y, l])
            V.events_heights.append(h)
        x -= 1
        if [x, y, l] in V.events_coordinates:
            V.events[V.events_coordinates.index([x, y, l])] = 4
            try:
                V.events_heights[V.events_coordinates.index([x, y, l])] = h
            except:
                V.events_heights.append(h)
        else:
            V.events.append(4)
            V.events_coordinates.append([x, y, l])
            V.events_heights.append(h)
    elif path[2] == "u":
        for i in range(randint(V.path_lengths[V.area_id][1], V.path_lengths[V.area_id][1])):
            y -= 1
            h += randint(V.height_variaty[V.area_id][0], V.height_variaty[V.area_id][1])
            if h > 5:
                h = 5
            elif h < 0:
                h = 0
            if [x, y, l] in V.events_coordinates:
                if V.events[V.events_coordinates.index([x, y, l])] != 10:
                    continue
                else:
                    if chance(V.snow_pile_spawns[V.area_id]):
                        V.events[V.events_coordinates.index([x, y, l])] = 9
                    else:
                        V.events[V.events_coordinates.index([x, y, l])] = 0
            if chance(V.snow_pile_spawns[V.area_id]):
                V.events.append(9)
            else:
                V.events.append(0)
            V.events_coordinates.append([x, y, l])
            V.events_heights.append(h)
        y -= 1
        if [x, y, l] in V.events_coordinates:
            V.events[V.events_coordinates.index([x, y, l])] = 4
            try:
                V.events_heights[V.events_coordinates.index([x, y, l])] = h
            except:
                V.events_heights.append(h)
        else:
            V.events.append(4)
            V.events_coordinates.append([x, y, l])
            V.events_heights.append(h)
    
    while V.events.count(14) > V.remnants_spawns[V.area_id][1]:
        V.events[V.events.index(14)] = 2
    while V.events.count(13) > 1:
        V.events[V.events.index(13)] = 0
    while V.events.count(11) > 1:
        V.events[V.events.index(11)] = 0
    while V.events.count(3) > 1:
        V.events[V.events.index(3)] = 0
    while V.events.count(5) > 1:
        V.events[V.events.index(5)] = 0







def map_movement(V):
    V.player_oxygen = 3
    V.player_hp_penalty = 0
    V.player_def_penalty = 0
    while True:
        for event in range(len(V.events)):
            if V.events[event] == 20:
                stalker_coords = V.events_coordinates[event]
                if stalker_coords[2] == V.player_coordinates[2] and not stalker_coords in V.no_update_coordinates:
                    distance = ((V.player_coordinates[0] - stalker_coords[0]) ** 2 + (V.player_coordinates[1] - stalker_coords[1]) ** 2) ** 0.5
                    if distance < V.vision_range - 0.25 + V.player_coordinates[2] * 1.5:
                        stalker_AI(V, event)
        V.no_update_coordinates = []
        if V.player_coordinates in V.events_coordinates:
            event = V.events[V.events_coordinates.index(V.player_coordinates)]
            current_height = V.events_heights[V.events_coordinates.index(V.player_coordinates)] + V.player_coordinates[2] * 2.5
        else:
            print("You are somehow out of bounds!")
            event = 0
        if current_height < V.water_level:
            if V.player_boat == False:
                V.player_oxygen -= 1
                if V.player_oxygen < 0:
                    V.player_hp_penalty += 0.01
                    V.player_oxygen_danger = True
                if V.area_id == 6:
                    V.player_def_penalty += 1
                    V.player_hp_penalty += 0.02
                    V.player_oxygen_danger = True
                if V.player_oxygen < -3:
                    V.player_oxygen = -3
            else:
                V.player_boat_hp -= 3
                if V.area_id == 6:
                    V.player_boat_hp -= 1
                elif V.area_id == 4:
                    V.player_boat_hp += 10
                if V.player_boat_hp < 0:
                    V.player_boat_hp = 0
                if V.player_boat_hp > 120:
                    V.player_boat_hp = 120
                V.player_oxygen += 1.5
                if V.player_oxygen > 3:
                    V.player_oxygen = 3
                V.player_oxygen_danger = False
        else:
            V.player_oxygen += 1.5
            if V.player_oxygen > 3:
                V.player_oxygen = 3
            V.player_oxygen_danger = False
        if V.cur_shopkeeper_dead == True:
            while 3 in V.events:
                V.events[V.events.index(3)] = 0
            V.cur_shopkeeper_dead = False
        if event in [0, 9, 15, 25, 26, 27, 28]:
            print()
            if V.player_boat and V.player_boat_hp <= 0:
                boat_break = False
                if V.player_coordinates in V.events_coordinates:
                    land_test_coordinates = [V.player_coordinates[0] - 1, V.player_coordinates[1], V.player_coordinates[2]]
                    if land_test_coordinates in V.events_coordinates:
                        if V.events[V.events_coordinates.index(land_test_coordinates)] != 10:
                            boat_break = True
                    land_test_coordinates = [V.player_coordinates[0] + 1, V.player_coordinates[1], V.player_coordinates[2]]
                    if land_test_coordinates in V.events_coordinates:
                        if V.events[V.events_coordinates.index(land_test_coordinates)] != 10:
                            boat_break = True
                    land_test_coordinates = [V.player_coordinates[0], V.player_coordinates[1] - 1, V.player_coordinates[2]]
                    if land_test_coordinates in V.events_coordinates:
                        if V.events[V.events_coordinates.index(land_test_coordinates)] != 10:
                            boat_break = True
                    land_test_coordinates = [V.player_coordinates[0], V.player_coordinates[1] + 1, V.player_coordinates[2]]
                    if land_test_coordinates in V.events_coordinates:
                        if V.events[V.events_coordinates.index(land_test_coordinates)] != 10:
                            boat_break = True
                if boat_break:
                    V.player_boat = False
                    V.player_has_boat = False
        elif event == 1:
            fight(V, fight_choose(V))
            V.max_power_level = round(V.max_power_level * 1.0175, 2)
            V.max_power_level_increase += 1
            if lost_check(V):
                break
            level_up(V)
            if V.game_mode in ["infinite", "story"]:
                V.events[V.events_coordinates.index(V.player_coordinates)] = 0
            elif V.game_mode == "raid":
                V.events[V.events_coordinates.index(V.player_coordinates)] = 25
            time_events(V, 2)
        elif event == 2:
            stats_altar(V)
            if V.game_mode in ["infinite", "story"]:
                V.events[V.events_coordinates.index(V.player_coordinates)] = 0
            elif V.game_mode == "raid":
                V.events[V.events_coordinates.index(V.player_coordinates)] = 26
            time_events(V, 1)
        elif event == 3:
            shop(V)
        elif event == 4:
            fight(V, bossfight_choose(V), ally_choose(V))
            V.max_power_level = round(V.max_power_level * 1.0175, 2)
            V.max_power_level_increase += 1
            if lost_check(V, boss=True):
                break
            level_up(V)
            if V.game_mode in ["infinite", "story", "raid"]:
                if V.final_area == False:
                    V.events[V.events_coordinates.index(V.player_coordinates)] = 16
                    time_events(V, 2)
                    continue
                else:
                    V.escape_amount = 1
                    break
        elif event == 5:
            mimic_gamble(V)
        elif event == 6:
            print()
            V.events[V.events_coordinates.index(V.player_coordinates)] = 0
            time_events(V, 1)
        elif event == 7:
            fight(V, fight_choose(V, 0.6))
            V.max_power_level = round(V.max_power_level * 1.0175, 2)
            V.max_power_level_increase += 1
            if lost_check(V):
                break
            level_up(V)
            V.events[V.events_coordinates.index(V.player_coordinates)] = 9
            time_events(V, 2)
        elif event == 8:
            fight(V, fight_choose(V, 1.2))
            V.max_power_level = round(V.max_power_level * 1.0175, 2)
            V.max_power_level_increase += 1
            if lost_check(V):
                break
            level_up(V)
            V.events[V.events_coordinates.index(V.player_coordinates)] = 9
            time_events(V, 3)
        elif event == 10:
            V.player_boat_hp -= 2
            if V.player_boat_hp < 0:
                V.player_boat_hp = 0
        elif event == 11:
            if V.death_defeated == False and V.player_spent_life > 0:
                print('''You approach the masked creature again. She speaks threateningly,
\033[38;2;100;100;100m"Perhaps, you do not appreciate what I do. Everyone that who is killed has to die. And you should be no exception."\033[0m
You ready yourself for the fight...
Type anything to continue''')
                action = input()
                V.score -= 5
                fight(V, [51])
                V.score += 5
                if lost_check(V, death=True):
                    break
                else:
                    V.death_defeated = True
                    print('''The masked creature, stands up again.
\033[38;2;100;100;100m"Your kind is so persistent. They keep continuing the cycle. But I feel that you are attempting to change that."\033[0m
She pauses for a moment, \033[38;2;100;100;100m"Perhaps, we are in the same \033[38;2;100;100;100;3mboat\033[0m\033[38;2;100;100;100m? Meet me later."\033[0m
The creature crawls away. You decide to continue your journey...
Type anything to continue''')
                    action = input()
            else:
                death_boat(V)
            if V.game_mode in ["infinite", "story"]:
                V.events[V.events_coordinates.index(V.player_coordinates)] = 0
            elif V.game_mode == "raid":
                V.events[V.events_coordinates.index(V.player_coordinates)] = 26
            time_events(V, 2)
        elif event in [12, 16]:
            if event == 12:
                escape(V, 3)
            elif event == 16:
                escape(V)
            else:
                escape(V)
            if V.escape_amount > 0:
                break
        elif event == 13:
            change_interaction(V)
        elif event == 14:
            player_remnants(V)
            time_events(V, 0)
            if V.game_mode in ["infinite", "story"]:
                V.events[V.events_coordinates.index(V.player_coordinates)] = 0
            elif V.game_mode == "raid":
                V.events[V.events_coordinates.index(V.player_coordinates)] = 26
        elif event == 17:
            fight(V, fight_choose(V, 0.9))
            V.max_power_level = round(V.max_power_level * 1.0175, 2)
            V.max_power_level_increase += 1
            if lost_check(V):
                break
            level_up(V)
            if V.game_mode in ["infinite", "story"]:
                V.events[V.events_coordinates.index(V.player_coordinates)] = 15
            elif V.game_mode == "raid":
                V.events[V.events_coordinates.index(V.player_coordinates)] = 27
            time_events(V, 2)
        elif event == 18:
            fight(V, fight_choose(V, -0.3))
            if lost_check(V):
                break
            stats_altar(V)
            if V.game_mode in ["infinite", "story"]:
                V.events[V.events_coordinates.index(V.player_coordinates)] = 15
            elif V.game_mode == "raid":
                V.events[V.events_coordinates.index(V.player_coordinates)] = 28
            time_events(V, 1)
        elif event == 19:
            mimic_bank(V)
        elif event == 20:
            fight(V, [42])
            if lost_check(V):
                break
            V.events[V.events_coordinates.index(V.player_coordinates)] = 0
        elif event == 21:
            V.player_coordinates[2] -= 1
        elif event == 22:
            V.player_coordinates[2] += 1
        elif event == 24:
            alchemist_shop(V)
        map_print(V)
        if V.player_has_boat == False:
            print('''\nWhere do you want to move?
W. ↑
A. ←
D. →
S. ↓
Y. O
I. - Inventory
H. - Map Help''')
        else:
            print('''\nWhere do you want to move?
W. ↑
A. ←
D. →
S. ↓
Y. O
B. - Switch boat mode
I. - Inventory
H. - Map Help''')
        while True:
            action = input()
            if action.lower() == "w" or action.lower() == "up":
                if [V.player_coordinates.copy()[0], V.player_coordinates.copy()[1] - 1, V.player_coordinates.copy()[2]] in V.events_coordinates and (V.events[V.events_coordinates.index([V.player_coordinates.copy()[0], V.player_coordinates.copy()[1] - 1, V.player_coordinates.copy()[2]])] != 10 or (V.player_boat == True and V.water_level > 0)):
                    V.player_coordinates[1] -= 1
                    break
                else:
                    print("You can't move there!")
            if action.lower() == "a" or action.lower() == "left":
                if [V.player_coordinates.copy()[0] - 1, V.player_coordinates.copy()[1], V.player_coordinates.copy()[2]] in V.events_coordinates and (V.events[V.events_coordinates.index([V.player_coordinates.copy()[0] - 1, V.player_coordinates.copy()[1], V.player_coordinates.copy()[2]])] != 10 or (V.player_boat == True and V.water_level > 0)):
                    V.player_coordinates[0] -= 1
                    break
                else:
                    print("You can't move there!")
            if action.lower() == "d" or action.lower() == "right":
                if [V.player_coordinates.copy()[0] + 1, V.player_coordinates.copy()[1], V.player_coordinates.copy()[2]] in V.events_coordinates and (V.events[V.events_coordinates.index([V.player_coordinates.copy()[0] + 1, V.player_coordinates.copy()[1], V.player_coordinates.copy()[2]])] != 10 or (V.player_boat == True and V.water_level > 0)):
                    V.player_coordinates[0] += 1
                    break
                else:
                    print("You can't move there!")
            if action.lower() == "s" or action.lower() == "down":
                if [V.player_coordinates.copy()[0], V.player_coordinates.copy()[1] + 1, V.player_coordinates.copy()[2]] in V.events_coordinates and (V.events[V.events_coordinates.index([V.player_coordinates.copy()[0], V.player_coordinates.copy()[1] + 1, V.player_coordinates.copy()[2]])] != 10 or (V.player_boat == True and V.water_level > 0)):
                    V.player_coordinates[1] += 1
                    break
                else:
                    print("You can't move there!")
            if action.lower() == "y" or "stay" in action.lower() or "still" in action.lower():
                break
            if action.lower() == "b" or "boat" in action.lower():
                if V.player_has_boat:
                    if V.player_boat:
                        if event != 10:
                            V.player_boat = False
                            break
                        else:
                            print("You can't stop using the boat here!")
                    else:
                        V.player_boat = True
                        break
            if action.lower() == "i" or action.lower() == "inventory":
                print("\033[33;1mYour weapon -", V.weapon_names[V.player_weapon])
                if len(V.player_items) > 0:
                    counter = 0
                    print("Consumables:")
                    for i in V.player_items:
                        counter += 1
                        print(str(counter) + ".", V.consumable_item_names[i])
                inventory_statistics(V)
                print("\033[0m", end = "")
            if action.lower() == "h" or "map" in action.lower() or "help" in action.lower():
                if V.player_boat == False and V.player_has_boat == False:
                    print('''Yellow \033[33;1mP\033[0m is you. You can move freely on circles.
Other symbols act differently when stepped on. Note that when you leave the area, you cannot come back...
Type in "save" to save the run''')
                else:
                    print('''Yellow \033[33;1mb\033[0m is you. You can move freely on circles and tildas.
Other symbols act differently when stepped on. Note that when you leave the area, you cannot come back...
Type in "save" to save the run''')
            if "restart" in action.lower():
                print('''Are you sure you want to restart? You will not be able to continue this run.
Type in the action
1. No
2. Yes''')
                action = input()
                if action == "2" or action.lower() == "yes":
                    V.lost = 1
                    break
            if action.lower() == "save":
                if V.meta_game_mode != "daily":
                    print('''Are you sure you want to save this run and continue later? The game will be closed.
Type in the action
1. No
2. Yes''')
                    action = input()
                    if action == "2" or action.lower() == "yes":
                        V.save_run()
                        V.lost = 1
                        break
                else:
                    print('''You cannot save in daily run...
Type anything to continue...''')
                    action = input()
        if V.lost == 1:
            break