
from random import seed, randint, choice, choices
from extra_functions import chance, meta_save
from circular_avoidance import max_x, max_y, min_x, min_y, map_tile_move, npc_talk
from coloring import represented_area_color
from upgrades_functions import level_up, xp_to_lvl_up, boss_upgrade
from shops import shop_items_define
from enemies_and_fighting import item_use

def final_statistics(V):
    print("Stats:")
    print("Max health: ", V.player_max_hp, " HP", sep = "")
    print("Base damage: ", V.player_base_dmg, " DMG", sep = "")
    if V.player_damage_range_boost > 0:
        print("Damage boost: ", V.player_damage_range_boost, "%", sep = "")
    print("Base defense: ", V.player_base_def, " DEF", sep = "")
    if V.player_shield > 0:
        print("Shield: ", V.player_shield, "%", sep = "")
    print("Base magic defense: ", V.player_base_magic_def, " MGCDEF", sep = "")
    if V.player_magic_shield > 0:
        print("Magic shield: ", V.player_magic_shield, "%", sep = "")
    print("Crit. chance: ", V.player_crit_chance, "%", sep = "")
    print("Crit. chance reduction: ", V.player_crit_chance_reduction, "%", sep = "")
    if V.player_spikes > 0:
        print("Spikes: ", V.player_spikes, " SPK", sep = "")
    if V.player_spikes_armor_break > 0:
        print("Defense broken by spikes: ", V.player_spikes_armor_break, " DEFRED", sep = "")
    if V.player_poison > 0:
        print("Poison: ", V.player_poison, " PSN", sep = "")
    if V.player_poison_def > 0:
        print("Poison defense: ", V.player_poison_def, " PSNDEF", sep = "")
    if V.player_lifesteal > 0:
        print("Lifesteal: ", V.player_lifesteal, "%", sep = "")
    if V.player_weapon_wrath > 0:
        print("Wrath: ", V.player_weapon_wrath, "% WRT", sep = "", end = "")
    if V.player_enemy_explotano > 0:
        print("Enemy Explotano: ", V.player_enemy_explotano, "%", sep = "", end = "")
    if V.player_immortality > 0:
        print("Immortal for ", V.player_immortality, " turns", sep = "")
    if V.player_regen > 0:
        print("Regeneration: +", V.player_regen, "%", sep = "")
    if V.player_dodge_chance > 0:
        print("Dodge chance: ", V.player_dodge_chance, "% DCH", sep = "")
    if V.player_consume > 0:
        print("Consume: ", V.player_consume, "%", sep = "")
    if V.player_travel > 0:
        print("Travel skill: ", V.player_travel, "%", sep = "")
    print("Money: ", V.player_money, " coins", sep = "")
    if V.player_gold_boost > 0:
        print("Money boost: ", V.player_gold_boost, "%", sep = "")
    print("Experience: ", V.player_xp, "/", xp_to_lvl_up(V), " XP", sep = "")
    print("Level: ", V.player_level, sep = "")
    print("Score: ", V.score, sep = "")
    if V.game_mode == "raid":
        print("Raids survived: ", V.raid_counter, sep = "")
    print("Max power level: ", V.max_power_level, sep = "")
    if V.saved == False:
        print("Seed: ", V.global_seed, sep = "")
        if V.shopkeeper_deaths + V.shopkeeper_sus + V.alchemist_anger + V.alchemist_defeated + V.death_defeated > 0:
            print("\nReputation:")
        if V.shopkeeper_sus > 0:
            print("Shopkeeper's sus meter: ", V.shopkeeper_sus, sep = "")
        if V.shopkeeper_deaths > 0:
            print("Shopkeepers' death count: ", V.shopkeeper_deaths, sep = "")
        if V.alchemist_anger > 0:
            print("Alchemist's anger meter: ", V.alchemist_anger, sep = "")
        if V.alchemist_defeated > 0:
            print("Alchemist's anger meter: ", V.alchemist_defeated, sep = "")
        if V.death_defeated == True:
            print("You have defeated Death")

def inventory_statistics(V):
    print("Stats:")
    print(V.player_max_hp, " HP; ", V.player_base_dmg, " DMG; ", sep = "", end = "")
    if V.player_damage_range_boost > 0:
        print(V.player_damage_range_boost, "% DMG Boost; ", sep = "", end = "")
    print(V.player_base_def, " DEF; ", sep = "", end = "")
    if V.player_shield > 0:
        print(V.player_shield, "% SHLD; ", sep = "", end = "")
    if V.player_base_magic_def > 0:
        print(V.player_base_magic_def, " MGCDEF; ", sep = "", end = "")
    if V.player_magic_shield > 0:
        print(V.player_magic_shield, "% MGCSHLD; ", sep = "", end = "")
    print(V.player_crit_chance, "% CRT; ", sep = "", end = "")
    print("Crit. chance reduction: ", V.player_crit_chance_reduction, "%; ", sep = "")
    if V.player_spikes > 0:
        print(V.player_spikes, " SPK; ", sep = "", end = "")
    if V.player_spikes_armor_break > 0:
        print(V.player_spikes_armor_break, " DEFRED; ", sep = "", end = "")
    if V.player_poison > 0:
        print(V.player_poison, " PSN; ", sep = "", end = "")
    if V.player_poison_def > 0:
        print(V.player_poison_def, " PSNDEF; ", sep = "", end = "")
    if V.player_lifesteal > 0:
        print(V.player_lifesteal, "% LFSTL; ", sep = "", end = "")
    if V.player_enemy_explotano > 0:
        print(V.player_enemy_explotano, "% - enemy explotano", sep = "", end = "")
    if V.player_weapon_wrath > 0:
        print(V.player_weapon_wrath, "% WRT", sep = "", end = "")
    if V.player_immortality > 0:
        print(V.player_immortality, " IMM; ", sep = "", end = "")
    if V.player_regen > 0:
        print("+", V.player_regen, "% REG", sep = "", end = "")
    if V.player_dodge_chance > 0:
        print(V.player_dodge_chance, "% DCH", sep = "", end = "")
    print()
    if V.player_consume > 0:
        print("Consume: ", V.player_consume, "%; ", sep = "", end = "")
    if V.player_travel > 0:
        print("Travel skill: ", V.player_travel, "%; ", sep = "", end = "")
    print("Money: ", V.player_money, " coins", sep = "")
    if V.player_gold_boost > 0:
        print("Money boost: ", V.player_gold_boost, "%", sep = "")
    print("Experience: ", V.player_xp, "/", xp_to_lvl_up(V), " XP", sep = "")
    print("Level: ", V.player_level, sep = "")
    print("Score: ", V.score, sep = "")
    print("Max power level: ", V.max_power_level, sep = "")




def lost_check(V, boss = False, death = False):
    if V.lost == 1 and (V.player_extra_life == False or death):
        return True
    elif V.lost == 1 and V.player_extra_life:
        V.player_spent_life = True
        V.player_extra_life = False
        V.score -= 2
        V.score_increase += 2
        V.player_money = 0
        V.player_xp = 0
        V.lost = 0
        print("\033[31;3mYou lost one of your lives. But you refuse to die...\033[0m\n\n\n")
        return False
    else:
        if boss:
            boss_upgrade(V)
        return False

def time_events(V, num = 0):
    V.game_time += num
    for k in range(num):
        if V.game_time > 12 and V.forest_enemy_spawn < 3 and V.area_id == 1:
            node = randint(0, len(V.events) - 1)
            if (V.events[node] == 0 or V.events[node] == 6) and V.events_coordinates[node] != V.player_coordinates:
                V.events[node] = 1
                V.forest_enemy_spawn += 1
        else:
            break

    V.no_update_coordinates = []
    if 15 in V.events or 17 in V.events or 18 in V.events or 27 in V.events or 28 in V.events:
        for node_coordinates in V.events_coordinates:
            if V.events[V.events_coordinates.index(node_coordinates)] in [15, 17, 18, 27, 28] and not node_coordinates in V.no_update_coordinates:
                new_coordinates = [node_coordinates[0], node_coordinates[1] - 1, node_coordinates[2]]
                if new_coordinates in V.events_coordinates:
                    if V.events[V.events_coordinates.index(new_coordinates)] in [0, 6]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 15
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [1, 7, 8, 9]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 17
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [2]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 18
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [25]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 27
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [26]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 28
                        V.no_update_coordinates.append(new_coordinates)
                new_coordinates = [node_coordinates[0] + 1, node_coordinates[1], node_coordinates[2]]
                if new_coordinates in V.events_coordinates:
                    if V.events[V.events_coordinates.index(new_coordinates)] in [0, 6]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 15
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [1, 7, 8, 9]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 17
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [2]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 18
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [25]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 27
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [26]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 28
                        V.no_update_coordinates.append(new_coordinates)
                new_coordinates = [node_coordinates[0], node_coordinates[1] + 1, node_coordinates[2]]
                if new_coordinates in V.events_coordinates:
                    if V.events[V.events_coordinates.index(new_coordinates)] in [0, 6]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 15
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [1, 7, 8, 9]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 17
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [2]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 18
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [25]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 27
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [26]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 28
                        V.no_update_coordinates.append(new_coordinates)
                new_coordinates = [node_coordinates[0] - 1, node_coordinates[1], node_coordinates[2]]
                if new_coordinates in V.events_coordinates:
                    if V.events[V.events_coordinates.index(new_coordinates)] in [0, 6]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 15
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [1, 7, 8, 9]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 17
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [2]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 18
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [25]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 27
                        V.no_update_coordinates.append(new_coordinates)
                    elif V.events[V.events_coordinates.index(new_coordinates)] in [26]:
                        V.events[V.events_coordinates.index(new_coordinates)] = 28
                        V.no_update_coordinates.append(new_coordinates)

    V.no_update_coordinates = []

    if V.game_time > 23:
        seed(V.weather_seed)
        V.game_time -= 24
        if V.vision_range != -1 and chance(1.4) and not 20 in V.events:
            V.stalker_stealth = 100
            epic_nodes = list(range(len(V.events)))
            while len(epic_nodes) > 10:
                stalker_node = choice(epic_nodes)
                stalker_coords = V.events_coordinates[stalker_node]
                if V.events[stalker_node] in [0, 6, 15] and (stalker_coords[2] != V.player_coordinates[2] or ((stalker_coords[0] - V.player_coordinates[0]) ** 2 + (stalker_coords[0] - V.player_coordinates[0]) ** 2) ** 0.5 > V.vision_range):
                    V.events[stalker_node] = 20
                    break
                epic_nodes.remove(stalker_node)
        V.bank_money += round(V.bank_money * 0.5)
        V.forest_enemy_spawn = 0
        shop_items_define(V)
        if V.area_id == 4 and V.enough_destroyed == False:
            V.player_coord_y = V.player_coordinates[1]
            if 3 in V.events:
                shop_coord_y = V.events_coordinates[V.events.index(3)][1]
            else:
                shop_coord_y = 0
            if 4 in V.events:
                boss_coord_y = V.events_coordinates[V.events.index(4)][1]
            elif 16 in V.events:
                boss_coord_y = V.events_coordinates[V.events.index(16)][1]
            else:
                boss_coord_y = 0
            if 5 in V.events:
                mimic_coord_y = V.events_coordinates[V.events.index(5)][1]
            else:
                mimic_coord_y = 0
            if 11 in V.events:
                death_coord_y = V.events_coordinates[V.events.index(11)][1]
            else:
                death_coord_y = 0
            if 24 in V.events:
                alchemist_coord_y = V.events_coordinates[V.events.index(24)][1]
            else:
                alchemist_coord_y = 0
            if 19 in V.events:
                steel_mimic_coord_y = V.events_coordinates[V.events.index(19)][1]
            else:
                steel_mimic_coord_y = 0
            event_deletions = []
            if not max_y(V) == V.player_coord_y:
                if max_y(V) != boss_coord_y and (not max_y(V) in [mimic_coord_y, shop_coord_y, death_coord_y, alchemist_coord_y, steel_mimic_coord_y] or V.game_mode == "raid"):
                    for i in range(len(V.events_coordinates)):
                        if V.events_coordinates[i][1] == max_y(V):
                            event_deletions.append(i)
                    counter = 0
                    for i in event_deletions:
                        del V.events[i - counter]
                        del V.events_coordinates[i - counter]
                        del V.events_heights[i - counter]
                        counter += 1
                else:
                    V.enough_destroyed = True
        V.default_water_levels[6] += 0.25

    seed(V.weather_seed)
    for r in range(len(V.current_weather)):
        if V.current_weather[r] == 0:
            if V.current_weather_duration[r] <= 0:
                if len(V.weathers[V.area_id]) > 0:
                    V.current_weather[r] = choices(V.weathers[V.area_id], weights = V.weather_chances[V.area_id])[0]
                    V.current_weather_duration[r] = randint(V.weathers_durations[V.current_weather[r]][0], V.weathers_durations[V.current_weather[r]][1])
                else:
                    V.current_weather[r] = 0
                    V.current_weather_duration[r] = randint(V.weathers_durations[V.current_weather[r]][0], V.weathers_durations[V.current_weather[r]][1])
            else:
                V.current_weather_duration[r] -= num
            V.weather_seed = randint(0, 10000)
        elif V.current_weather[r] == 1:
            if V.current_weather_duration[r] <= 0:
                V.current_weather[r] = 0
                V.current_weather_duration[r] = randint(V.weathers_durations[V.current_weather[r]][0], V.weathers_durations[V.current_weather[r]][1])
            else:
                seed(V.weather_effects_seed)
                for i in range(num):
                    node = randint(0, len(V.events) - 1)
                    if (V.events[node] == 0) and V.events_coordinates[node] != V.player_coordinates and V.events_coordinates[node][2] == 0:
                        V.events[node] = 6
                V.current_weather_duration[r] -= num
                V.weather_effects_seed = randint(0, 10000)
        elif V.current_weather[r] == 2:
            if V.current_weather_duration[r] <= 0:
                V.current_weather[r] = 0
                V.current_weather_duration[r] = randint(V.weathers_durations[V.current_weather[r]][0], V.weathers_durations[V.current_weather[r]][1])
            else:
                if V.vision_range == -1:
                    V.vision_range = 20 - ((num - 1) * 0.5)
                else:
                    V.vision_range -= (num * 0.5)
                if V.vision_range != -1 and V.vision_range < 1.5:
                    V.vision_range = 1.5
                V.current_weather_duration[r] -= num
        elif V.current_weather[r] == 3:
            if V.current_weather_duration[r] <= 0:
                V.current_weather[r] = 0
                V.current_weather_duration[r] = randint(V.weathers_durations[V.current_weather[r]][0], V.weathers_durations[V.current_weather[r]][1])
            else:
                seed(V.map_seed)
                for i in range(num):
                    iteration = 0
                    while True:
                        iteration += 1
                        if iteration > 999:
                            V.earth_cannot_generate_tiles = True
                        if V.earth_cannot_generate_tiles:
                            break
                        x = randint(min_x(V), max_x(V))
                        y = randint(min_y(V), max_y(V))
                        l = 0
                        h_neighbors = 0
                        v_neighbors = 0
                        d_neighbors = 0
                        heights = 0
                        if [x, y] in V.events_coordinates:
                            continue
                        else:
                            if [x + 1, y + 1, l] in V.events_coordinates and V.events[V.events_coordinates.index([x + 1, y + 1, l])] != 10:
                                d_neighbors += 1
                                heights += V.events_heights[V.events_coordinates.index([x + 1, y + 1, l])]
                            if [x, y + 1, l] in V.events_coordinates and V.events[V.events_coordinates.index([x, y + 1, l])] != 10:
                                v_neighbors += 1
                                heights += V.events_heights[V.events_coordinates.index([x, y + 1, l])]
                            if [x - 1, y + 1, l] in V.events_coordinates and V.events[V.events_coordinates.index([x - 1, y + 1, l])] != 10:
                                d_neighbors += 1
                                heights += V.events_heights[V.events_coordinates.index([x - 1, y + 1, l])]
                            if [x + 1, y, l] in V.events_coordinates and V.events[V.events_coordinates.index([x + 1, y, l])] != 10:
                                h_neighbors += 1
                                heights += V.events_heights[V.events_coordinates.index([x + 1, y, l])]
                            if [x - 1, y, l] in V.events_coordinates and V.events[V.events_coordinates.index([x - 1, y, l])] != 10:
                                h_neighbors += 1
                                heights += V.events_heights[V.events_coordinates.index([x - 1, y, l])]
                            if [x + 1, y - 1, l] in V.events_coordinates and V.events[V.events_coordinates.index([x + 1, y - 1, l])] != 10:
                                d_neighbors += 1
                                heights += V.events_heights[V.events_coordinates.index([x + 1, y - 1, l])]
                            if [x, y - 1, l] in V.events_coordinates and V.events[V.events_coordinates.index([x, y - 1, l])] != 10:
                                v_neighbors += 1
                                heights += V.events_heights[V.events_coordinates.index([x, y - 1, l])]
                            if [x - 1, y - 1, l] in V.events_coordinates and V.events[V.events_coordinates.index([x - 1, y - 1, l])] != 10:
                                d_neighbors += 1
                                heights += V.events_heights[V.events_coordinates.index([x - 1, y - 1, l])]
                            if v_neighbors + h_neighbors < 1:
                                continue
                            elif v_neighbors > 0 and h_neighbors > 0 and d_neighbors > 0:
                                continue
                            else:
                                break
                    if iteration < 1000:
                        #print(v_neighbors, h_neighbors, d_neighbors)
                        if chance(0.7):
                            V.events.append(0)
                        elif chance(0.5):
                            V.events.append(9)
                        elif chance(0.5):
                            V.events.append(25)
                        else:
                            V.events.append(26)
                        V.events_coordinates.append([x, y, l])
                        if h_neighbors + v_neighbors + d_neighbors > 0:
                            V.events_heights.append(heights // (h_neighbors + v_neighbors + d_neighbors))
                        else:
                            V.events_heights.append(heights)
                V.current_weather_duration[r] -= num
        elif V.current_weather[r] == 4:
            if V.current_weather_duration[r] <= 0:
                V.current_weather[r] = 0
                V.current_weather_duration[r] = randint(V.weathers_durations[V.current_weather[r]][0], V.weathers_durations[V.current_weather[r]][1])
            else:
                seed(V.weather_effects_seed)
                if V.vision_range == -1:
                    V.vision_range = 18 - ((num - 1) * 0.75)
                else:
                    V.vision_range -= (num * 0.75)
                if V.vision_range != -1 and V.vision_range < 1.5:
                    V.vision_range = 1.5
                for i in range(num):
                    iteration = 0
                    while True:
                        iteration += 1
                        if iteration > 999:
                            break
                        node = randint(0, len(V.events) - 1)
                        if V.events[node] == 9:
                            V.events[node] = 7
                        elif V.events[node] == 7:
                            V.events[node] = 8
                        else:
                            continue
                        break
                V.weather_effects_seed = randint(0, 10000)
                V.current_weather_duration[r] -= num
        elif V.current_weather[r] == 5:
            if V.current_weather_duration[r] <= 0:
                V.current_weather[r] = 0
                V.current_weather_duration[r] = randint(V.weathers_durations[V.current_weather[r]][0], V.weathers_durations[V.current_weather[r]][1])
            else:
                seed(V.map_seed)
                if V.vision_range == -1:
                    V.vision_range = 18 - ((num - 1) * 0.75)
                else:
                    V.vision_range -= (num * 0.75)
                if V.vision_range != -1 and V.vision_range < 1.5:
                    V.vision_range = 1.5
                for k in range(num * 4):
                    for i in range(len(V.events)):
                        if V.events[i] == 1:
                            coordinates = V.events_coordinates[i]
                            if not coordinates in V.no_update_coordinates:
                                directions = ["u", "r", "d", "l"]
                                while len(directions) > 0:
                                    direction = choice(directions)
                                    if direction == "u":
                                        directions.remove("u")
                                        map_tile_move(V, coordinates, "u", 1)
                                    if direction == "l":
                                        directions.remove("l")
                                        map_tile_move(V, coordinates, "l", 1)
                                    if direction == "d":
                                        directions.remove("d")
                                        map_tile_move(V, coordinates, "d", 1)
                                    if direction == "r":
                                        directions.remove("r")
                                        map_tile_move(V, coordinates, "r", 1)
                V.no_update_coordinates = []
                V.current_weather_duration[r] -= num
        elif V.current_weather[r] == 6:
            if V.current_weather_duration[r] <= 0:
                V.current_weather[r] = 0
                V.current_weather_duration[r] = randint(V.weathers_durations[V.current_weather[r]][0], V.weathers_durations[V.current_weather[r]][1])
            else:
                V.current_weather_duration[r] -= num
        elif V.current_weather[r] == 7:
            if V.current_weather_duration[r] <= 0:
                V.current_weather[r] = 0
                V.current_weather_duration[r] = randint(V.weathers_durations[V.current_weather[r]][0], V.weathers_durations[V.current_weather[r]][1])
            else:
                try:
                    V.current_weather_duration[r] -= num
                except:
                    num
        elif V.current_weather[r] == 8:
            if V.current_weather_duration[r] <= 0:
                V.current_weather[r] = 0
                V.current_weather_duration[r] = randint(V.weathers_durations[V.current_weather[r]][0], V.weathers_durations[V.current_weather[r]][1])
            else:
                V.water_level += num / 4
                if V.water_level > 5:
                    V.water_level = 5
                V.current_weather_duration[r] -= num
        elif V.current_weather[r] == 9:
            if V.current_weather_duration[r] <= 0:
                V.current_weather[r] = 0
                V.current_weather_duration[r] = randint(V.weathers_durations[V.current_weather[r]][0], V.weathers_durations[V.current_weather[r]][1])
            else:
                V.water_level -= num / 5
                if V.water_level > 0:
                    V.water_level = 0
                V.current_weather_duration[r] -= num

    seed(V.weather_seed)
    if not 8 in V.current_weather and not 6 in V.current_weather and not 1 in V.current_weather:
        if V.water_level > V.default_water_levels[V.area_id]:
            V.water_level -= randint(1, num + 1) * 0.5
            if V.water_level < V.default_water_levels[V.area_id]:
                V.water_level = V.default_water_levels[V.area_id]
    if not 9 in V.current_weather:
        if V.water_level < V.default_water_levels[V.area_id]:
            V.water_level += randint(1, num + 1) * 0.5
            if V.water_level > V.default_water_levels[V.area_id]:
                V.water_level = V.default_water_levels[V.area_id]
    if not 2 in V.current_weather and not 5 in V.current_weather:
        if V.vision_range != V.base_vision_ranges[V.area_id]:
            if V.base_vision_ranges[V.area_id] == -1:
                if V.vision_range < 20:
                    V.vision_range += num * 0.75
                if V.vision_range >= 20:
                    V.vision_range = -1
            else:
                if V.vision_range < V.base_vision_ranges[V.area_id]:
                    V.vision_range += num * 0.75
                    if V.vision_range > V.base_vision_ranges[V.area_id]:
                        V.vision_range = V.base_vision_ranges[V.area_id]
                elif V.vision_range > V.base_vision_ranges[V.area_id]:
                    V.vision_range -= num * 0.75
                    if V.vision_range < V.base_vision_ranges[V.area_id]:
                        V.vision_range = V.base_vision_ranges[V.area_id]


def raid_mode_reset(V):
    print("The raid is over. Another one begins!")
    seed(V.map_seed)
    V.map_seed = randint(0, 10000)
    V.raid_counter += 1
    for i in range(len(V.events)):
        if V.events[i] in [15]:
            V.events[i] = 0
        if V.events[i] in [17, 25, 27]:
            V.events[i] = 1
        if V.events[i] in [3, 5, 11, 14, 18, 23, 24, 26, 28]:
            V.events[i] = 2
        if V.events[i] in [16]:
            V.events[i] = 25
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
    if remnant_events_amount > V.events.count(2):
        remnant_events_amount = V.events.count(2)
    while remnant_events_amount > V.events.count(14):
        event = choice(range(len(V.events)))
        if V.events[event] == 2:
            V.events[event] = 14
    if V.area_id == 0:
        if V.events.count(2) + V.events.count(14) > 2:
            while not 3 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    V.events[event] = 3
    elif V.area_id == 1:
        if V.events.count(2) + V.events.count(14) > 6:
            while not 3 in V.events or not 5 in V.events or not 11 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    if not 3 in V.events:
                        V.events[event] = 3
                    elif not 5 in V.events:
                        V.events[event] = 5
                    elif not 11 in V.events:
                        V.events[event] = 11
        elif V.events.count(2) + V.events.count(14) > 4:
            while not 3 in V.events or not 5 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    if not 3 in V.events:
                        V.events[event] = 3
                    elif not 5 in V.events:
                        V.events[event] = 5
        elif V.events.count(2) + V.events.count(14) > 2:
            while not 3 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    V.events[event] = 3
    elif V.area_id == 2:
        if V.events.count(2) + V.events.count(14) > 7:
            while not 3 in V.events or not 5 in V.events or not 11 in V.events or not 24 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    if not 3 in V.events:
                        V.events[event] = 3
                    elif not 5 in V.events:
                        V.events[event] = 5
                    elif not 11 in V.events:
                        V.events[event] = 11
                    elif not 24 in V.events:
                        V.events[event] = 24
        elif V.events.count(2) + V.events.count(14) > 6:
            while not 3 in V.events or not 5 in V.events or not 11 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    if not 3 in V.events:
                        V.events[event] = 3
                    elif not 5 in V.events:
                        V.events[event] = 5
                    elif not 11 in V.events:
                        V.events[event] = 11
        elif V.events.count(2) + V.events.count(14) > 4:
            while not 3 in V.events or not 5 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    if not 3 in V.events:
                        V.events[event] = 3
                    elif not 5 in V.events:
                        V.events[event] = 5
        elif V.events.count(2) + V.events.count(14) > 2:
            while not 3 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    V.events[event] = 3
    else:
        if V.events.count(2) + V.events.count(14) > 8:
            while not 3 in V.events or not 5 in V.events or not 11 in V.events or not 24 in V.events or not 19 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    if not 3 in V.events:
                        V.events[event] = 3
                    elif not 5 in V.events:
                        V.events[event] = 5
                    elif not 11 in V.events:
                        V.events[event] = 11
                    elif not 24 in V.events:
                        V.events[event] = 24
                    elif not 19 in V.events:
                        V.events[event] = 19
        if V.events.count(2) + V.events.count(14) > 7:
            while not 3 in V.events or not 5 in V.events or not 11 in V.events or not 24 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    if not 3 in V.events:
                        V.events[event] = 3
                    elif not 5 in V.events:
                        V.events[event] = 5
                    elif not 11 in V.events:
                        V.events[event] = 11
                    elif not 24 in V.events:
                        V.events[event] = 24
        elif V.events.count(2) + V.events.count(14) > 6:
            while not 3 in V.events or not 5 in V.events or not 19 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    if not 3 in V.events:
                        V.events[event] = 3
                    elif not 5 in V.events:
                        V.events[event] = 5
                    elif not 19 in V.events:
                        V.events[event] = 19
        elif V.events.count(2) + V.events.count(14) > 4:
            while not 3 in V.events or not 5 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    if not 3 in V.events:
                        V.events[event] = 3
                    elif not 5 in V.events:
                        V.events[event] = 5
        elif V.events.count(2) + V.events.count(14) > 2:
            while not 3 in V.events:
                event = choice(range(len(V.events)))
                if V.events[event] in [2, 14]:
                    V.events[event] = 3
    while not 4 in V.events or (V.area_id == 2 and not 15 in V.events):
        event = choice(range(len(V.events)))
        if V.events[event] in [1] and not 4 in V.events and chance(0.3):
            V.events[event] = 4
        elif V.events.count(1) < 2 and V.events[event] == [0] and not 4 in V.events:
            V.events[event] = 4
        elif V.area_id == 2 and V.events[event] == 0 and not 15 in V.events:
            V.events[event] = 15
    for i in range(len(V.hunters_appeared)):
        V.hunters_appeared[i] = False
    if V.player_travel > 0:
        V.player_xp += round(xp_to_lvl_up(V) * V.player_travel / 100)
        print("You gained\033[38;2;100;0;200m", round(xp_to_lvl_up(V) * V.player_travel / 100), "XP\033[0m for finishing a raid!")
    level_up(V)
    V.mimic_got_item = False
    V.mimic_given_items = 0
    V.bank_first_time = True
    V.bank_money += round(V.bank_money * 0.5)
    V.score += int(V.score_increase)
    if V.raid_counter > V.TD_max_raids[V.area_id]:
        V.TD_max_raids[V.area_id] = V.raid_counter
    if V.area_id == 0:
        if V.TD_area_unlocks[2] == False and V.raid_counter == 3:
            V.TD_area_unlocks[2] = True
            print("You have unlocked " + represented_area_color(V, 2) + "the Cave!\033[0m")
    elif V.area_id == 1:
        if V.TD_area_unlocks[2] == False and V.raid_counter == 2:
            V.TD_area_unlocks[2] = True
            print("You have unlocked " + represented_area_color(V, 2) + "the Cave!\033[0m")
    elif V.area_id == 2:
        if V.TD_area_unlocks[3] == False and V.raid_counter == 3:
            V.TD_area_unlocks[3] = True
            print("You have unlocked " + represented_area_color(V, 3) + "the Tundra!\033[0m")
        if V.TD_area_unlocks[4] == False and V.raid_counter == 5:
            V.TD_area_unlocks[4] = True
            print("You have unlocked " + represented_area_color(V, 4) + "the Canyon!\033[0m")
    elif V.area_id == 3:
        if V.TD_area_unlocks[4] == False and V.raid_counter == 4:
            V.TD_area_unlocks[4] = True
            print("You have unlocked " + represented_area_color(V, 4) + "the Canyon!\033[0m")
        if V.TD_area_unlocks[5] == False and V.raid_counter == 6:
            V.TD_area_unlocks[5] = True
            print("You have unlocked " + represented_area_color(V, 5) + "the Desert!\033[0m")
    elif V.area_id == 4:
        if V.TD_area_unlocks[5] == False and V.raid_counter == 4:
            V.TD_area_unlocks[5] = True
            print("You have unlocked " + represented_area_color(V, 5) + "the Desert!\033[0m")
    elif V.area_id == 5:
        if V.TD_area_unlocks[6] == False and V.raid_counter == 7:
            V.TD_area_unlocks[6] = True
            print("You have unlocked " + represented_area_color(V, 6) + "the Rotten Forest!\033[0m")
    meta_save(V)
    print('''Type anything to continue...''')
    action = input()

def escape(V, escape_amount = 1):
    if V.game_mode in ["story", "infinite"]:
        if escape_amount > 1:
            print("You see a secret passage, leading somewhere. It seems to skip a lot of your intended path.")
        else:
            print("The road ahead seems to lead you to the next area.")
        print('''Do you want to escape this place or stay to continue exploring it?
1. Escape
2. Stay''')
        while True:
            action = input()
            if action == "1" or action.lower() == "escape":
                V.escape_amount = escape_amount
                print("\n\n\n")
                break
            elif action == "2" or action.lower() == "stay":
                break
    elif V.game_mode in ["raid"]:
        print('''Do you want start the next raid already?
1. Start
2. Stay''')
        while True:
            action = input()
            if action == "1" or action.lower() == "start":
                print("\n\n\n")
                raid_mode_reset(V)
                break
            elif action == "2" or action.lower() == "stay":
                break

def change_interaction(V):
    V.leave = 0
    if V.area_id == 2 and V.change_encounters == 0:
        print('''You come across a man with otherworldly glow surrounding him.
He quickly notices you and starts to speak, \033[38;2;100;100;175m"You. You. Another one. Did you come here to destroy me or to see me suffer?"\033[0m
You attempt to respond but the words aren't coming out of your mouth.
\033[38;2;100;100;175m"Stop mocking me. You don't understand what it is like to hide in the shadows for more than any mortal's lifespan."\033[0m
. . .
1. Continue talking
2. Leave''')
        while True:
            action = input()
            if action == "1" or "continue" in action.lower() or "talk" in action.lower():
                print('''You stand still and wait until the man continues,
\033[38;2;100;100;175m"You're... you're still here?"\033[0m
After a long pause he continues, \033[38;2;100;100;175m"It was their fault... They ignored my warnings. They didn't take any action against your creator."
"And now I'm here. Just a small reminder of the previous world... But I think, there is a way to stop this now."
"But I need your help. I am not strong enough on my own. Are you going to help me?"\033[0m
1. Yes
2. No''')
                while True:
                    action = input()
                    if action == "1" or action.lower() == "yes":
                        print('''The man stands up and continues to speak,
\033[38;2;100;100;175m"Great. I will assist you in your last battle, and you will assist me. Meet me again in the land of your creation."\033[0m''')
                        V.change_recruited = True
                        break
                    elif action == "2" or action.lower() == "no":
                        print('''The man looks surprised, \033[38;2;100;100;175m"You aren't going to help me? Well, don't tell your creator where I am, okay?"\033[0m''')
                        break
                break
            elif action == "2" or action.lower() == "leave":
                print("You turned around and left the mysterious man alone...")
                V.leave = 1
                break
        V.change_encounters += 1
        while V.leave == 0:
            print('''After a pause, he asks you,
\033[38;2;100;100;175m"Do you want to listen to me talk nonsense? Or are you going onwards with your journey?"\033[0m
1. Talk
2. Leave''')
            while True:
                action = input()
                if action == "1" or action.lower() == "talk":
                    npc_talk(V, "change")
                    break
                elif action == "2" or action.lower() == "leave":
                    V.leave = 1
                    break
        print('''You leave the man alone...
Type anything to continue...''')
        action = input()
    elif V.area_id == 2 and V.change_encounters != 0:
        if V.change_recruited == True:
            print('''You approach the weird man again. He speaks again,
\033[38;2;100;100;175m"Okay, I will repeat. I will assist you in your last battle, and you will assist me. Meet me again in the land of your creation."\033[0m''')
            while V.leave == 0:
                print('''After a pause, he asks you,
\033[38;2;100;100;175m"Do you want to listen to me talk nonsense? Or are you going onwards with your journey?"\033[0m
1. Talk
2. Leave''')
                while True:
                    action = input()
                    if action == "1" or action.lower() == "talk":
                        npc_talk(V, "change")
                        break
                    elif action == "2" or action.lower() == "leave":
                        V.leave = 1
                        break
            print('''You leave the man alone...''')
        else:
            print('''You approach the weird man again. He speaks again,
\033[38;2;100;100;175m"Leave. Me. Alone."\033[0m
You leave the man alone...''')
    elif V.area_id == 0 and V.change_encounters == 1:
        print('''You come across the mysterious man again. He notices you and speaks quietly,
\033[38;2;100;100;175m"Hello, again. I assume we're still going with the plan, right?"\033[0m
\033[38;2;100;100;175m"The next formidable foe you're going to face is your sibling. Please, don't consume 'em; we need to stop Cycle's Great Cycle, not continue it."\033[0m''')
        while V.leave == 0:
            print('''After a pause, he asks you,
\033[38;2;100;100;175m"Do you want to listen to me talk nonsense? Or are you going onwards with your journey?"\033[0m
1. Talk
2. Leave''')
            while True:
                action = input()
                if action == "1" or action.lower() == "talk":
                    npc_talk(V, "change")
                    break
                elif action == "2" or action.lower() == "leave":
                    V.leave = 1
                    break
        print('''You leave the man and continue your journey...''')
        print('''Type anything to continue...''')
        action = input()
        V.change_encounters += 1
    elif V.area_id == 0 and V.change_encounters == 2:
        print('''You come to the mysterious man again. He speaks quietly again,
\033[38;2;100;100;175m"What? Just go to the boss and I will help you."\033[0m''')
        while V.leave == 0:
            print('''After a pause, he asks you,
\033[38;2;100;100;175m"Do you want to listen to me talk nonsense? Or are you going onwards with your journey?"\033[0m
1. Talk
2. Leave''')
            while True:
                action = input()
                if action == "1" or action.lower() == "talk":
                    npc_talk(V, "change")
                    break
                elif action == "2" or action.lower() == "leave":
                    V.leave = 1
                    break
        print('''You walk away and continue your journey...''')
        print('''Type anything to continue...''')
        action = input()
    else:
        print('''You aren't supposed to encouter this event tile in this area! Please notify the developer!
Type anything to continue...''')
        action = input()

def map_inventory(V):
    while True:
        print("\033[33;1mYour weapon -", V.weapon_names[V.player_weapon])
        if len(V.player_items) > 0:
            counter = 0
            print("Consumables:")
            for i in V.player_items:
                counter += 1
                print(str(counter) + ".", V.consumable_item_names[i])
        inventory_statistics(V)
        print("\033[0m", end = "")

        print('''\n\nDo you want to use consumables and/or switch weapons?
1. Yes
2. No''')
        action = input()
        if action == "1" or action.lower() == "yes":
            while True:
                print('''What do you want to do exactly?
1. Change weapons
2. Consumables
0. Cancel''')
                action = input()
                if action == "1" or "change" in action.lower() or "weapons" in action.lower():
                    if len(V.player_inventory_weapons) <= 0:
                        print("You have no other weapons!\nType anything to continue...")
                        action = input()
                    else:
                        while True:
                            counter = 0
                            for i in V.player_inventory_weapons:
                                counter += 1
                                print(str(counter) + ".", V.weapon_names[i])
                            print("0. Cancel")
                            action = input()
                            if action.isdigit():
                                action = int(action) - 1
                                if action > -1 and action < len(V.player_inventory_weapons):
                                    V.player_weapon, V.player_inventory_weapons[action] = V.player_inventory_weapons[action], V.player_weapon
                                    V.player_poison, V.player_inventory_weapons_psn[action] = V.player_inventory_weapons_psn[action], V.player_poison
                                    V.player_enemy_explotano, V.player_inventory_weapons_explotano[action] = V.player_inventory_weapons_explotano[action], V.player_enemy_explotano
                                    V.player_lifesteal, V.player_inventory_weapons_lifesteal[action] = V.player_inventory_weapons_lifesteal[action], V.player_lifesteal
                                    V.player_weapon_wrath, V.player_inventory_weapons_wrath[action] = V.player_inventory_weapons_wrath[action], V.player_weapon_wrath
                                    if V.player_weapon == 1:
                                        V.player_extra_magic_def_buff = 1.5
                                    else:
                                        V.player_extra_magic_def_buff = 0
                                    print("You changed your weapon to", V.weapon_names[V.player_weapon], end = "")
                                    if V.player_poison + V.player_enemy_explotano + V.player_lifesteal + V.player_weapon_wrath > 0:
                                        print(" with", end = "")
                                    if V.player_poison > 0:
                                        print(" ", V.player_poison, " PSN", sep = "", end = "")
                                    if V.player_lifesteal > 0:
                                        if V.player_poison > 0:
                                            print(",", end = "")
                                        print(" ", V.player_lifesteal, "% LFSTL", sep = "", end = "")
                                    if V.player_enemy_explotano > 0:
                                        if V.player_poison + V.player_lifesteal > 0:
                                            print(",", end = "")
                                        print(" ",V.player_enemy_explotano, "% enemy explotano", sep = "", end = "")
                                    if V.player_weapon_wrath > 0:
                                        if V.player_poison + V.player_lifesteal + V.player_enemy_explotano > 0:
                                            print(",", end = "")
                                        print(" ",V.player_weapon_wrath, "% wrath", sep = "", end = "")
                                    print(".")
                                elif action == -1:
                                    break
                            elif action.lower() == "cancel":
                                break
                elif action == "2" or "consumable" in action.lower():
                    if len(V.player_items) > 0:
                        while True:
                            counter = 0
                            for i in V.player_items:
                                counter += 1
                                print(str(counter) + ".", V.consumable_item_names[i])
                            if counter == 0:
                                break
                            print("0. Cancel")
                            print("Choose an item")
                            item_action = input()
                            if item_action.isdigit():
                                item_action = int(item_action)
                                if item_action > 0 and item_action <= len(V.player_items):
                                    print("1. Use\n2. Inspect\n0. Cancel")
                                    while True:
                                        action = input()
                                        if action == '1' or action.lower() == "use":
                                            item_use(V, V.player_items[item_action - 1], "map")
                                            print("\033[0m\nType anything to continue...")
                                            action = input()
                                            break
                                        elif action == '2' or action.lower() == "inspect":
                                            print(V.consumable_item_desc[V.player_items[item_action-1]])
                                            print("\033[0m\nType anything to continue...")
                                            action = input()
                                            break
                                        elif action == '0' or action.lower() == "cancel":
                                            break
                                if item_action == 0:
                                    break
                    else:
                        print("You have no consumable items!\nType anything to continue...")
                        action = input()
                elif action == "0" or "cancel" in action.lower():
                    break
        elif action == "2" or action.lower() == "no":
            break
