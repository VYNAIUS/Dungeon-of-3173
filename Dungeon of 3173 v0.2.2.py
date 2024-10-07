from random import *
import os
import sys
import subprocess
import time
import math
from turtle import speed

# Gets the current user's LocalLow directory
save_directory_path = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'DungeonOf3173')
# This path is user-specific and will automatically adapt to whoever is running the script
#THANKS CHAT GPT!!!!!11
os.makedirs(save_directory_path, exist_ok=True)
file_path = os.path.join(save_directory_path, 'save.txt')
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
else:
    with open(file_path, 'w') as file:
        file.write('''TD_unlocks=[1100000]
TD_high_scores=[0000000]''')
    print("New save file has been created!")
with open(file_path, 'r') as file:
    content = file.read()

TD_area_unlocks = []
TD_max_raids = []
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
                    TD_area_unlocks.append(True)
                    area_counter += 1
                elif content[i] == "0":
                    TD_area_unlocks.append(False)
                    area_counter += 1
        if key_word == "TD_high_scores":
            print("Scanning Raid Mode high scores")
            area_counter = 0
            for i in range(symbol, len(content)):
                if content[i] == "]" or area_counter == 7:
                    break
                elif content[i].isdigit():
                    TD_max_raids.append(int(content[i]))
                    area_counter += 1
#print(TD_area_unlocks)
fancy_percentage_save_file_thing = 0
while len(TD_area_unlocks) < 7:
    fancy_percentage_save_file_thing += 1
    if len(TD_area_unlocks) < 2:
        TD_area_unlocks.append(True)
    else:
        TD_area_unlocks.append(False)
    print("Restoring a corrupt save file - ", round(fancy_percentage_save_file_thing / 14 * 100), "%", sep = "")
while len(TD_max_raids) < 7:
    fancy_percentage_save_file_thing += 1
    TD_max_raids.append(0)
    print("Restoring a corrupt save file - ", round(fancy_percentage_save_file_thing / 14 * 100), "%", sep = "")
print("\n\n\n")
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
#print('''Please notify the developer if any of these symbols don't work:
#Pb•○×†$B⌂~ΛADE

#''')

def enemy_name_color(enemy_id = 0):
    string = "\033[38;2"
    for i in range(3):
        try:
            string = string + ";" + str(enemys_name_colors[enemy_id][i])
        except:
            string = string + ";255"
    string = string + "m"
    return string

def area_color(height = 5, affected_by_weather = False):
    global area_id
    global current_weather
    string = "\033[38;2"
    weather_colors = []
    weather_color_effect = 0
    for i in range(3):
        #try:
            if affected_by_weather and (1 in current_weather or 6 in current_weather or 7 in current_weather or 8 in current_weather):
                weather_colors.append(water_colors_0[area_id][i])
            if affected_by_weather and 5 in current_weather:
                weather_colors.append(50)
            if affected_by_weather and (2 in current_weather or 4 in current_weather):
                weather_colors.append(200)
            if affected_by_weather and 9 in current_weather:
                weather_colors.append(140)
            if len(weather_colors) > 0:
                counter = 0
                for r in weather_colors:
                    counter += 1
                    weather_color_effect += r
                weather_color_effect = weather_color_effect // counter
            else:
                weather_color_effect = areas_colors[area_id][i]
            color = (areas_colors[area_id][i] + weather_color_effect) // 2
            if area_id != 6:
                color = color + (12 * height) - 60
            else:
                color = color + (7 * height) - 35
            if color > 255:
                color = 255
            elif color < 0:
                color = 0
            string = string + ";" + str(color)
        #except:
            #string = string + ";255"
    string = string + "m"
    return string

def represented_area_color(area=0):
    string = "\033[38;2"
    for i in range(3):
        color = areas_colors[area][i]
        string = string + ";" + str(color)
    string = string + "m"
    return string

def water_color(water_type = 0):
    global area_id
    string = "\033[38;2"
    for i in range(3):
        try:
            if water_type == 0:
                string = string + ";" + str(water_colors_0[area_id][i])
            elif water_type == 1:
                string = string + ";" + str(water_colors_1[area_id][i])
        except:
            string = string + ";50"
    string = string + "m"
    return string

# I NEED TO SET THESE BEFORE THE enemy_actions LIST!!!
def enemy_hit(attacker = 0):
    global player_current_hp
    global player_base_def
    global player_extra_def
    global player_poisoned
    global player_spikes
    global player_spikes_armor_break
    global player_shield
    global player_dodge_chance
    global player_dodge_count
    global player_dodged
    global enemys
    global allys

    if player_dodge_chance > 0:
        dodges_needed = 100 // player_dodge_chance
        if player_dodge_count < dodges_needed:
            if chance(player_dodge_chance / 100) and player_dodged == False:
                will_dodge = True
                player_dodged = True
                player_dodge_count += 1
            else:
                will_dodge = False
                player_dodge_count += 1
        else:
            if player_dodged == True:
                will_dodge = False
                player_dodge_count += 1
            else:
                will_dodge = True
            player_dodge_count = 0
            player_dodged = False
    else:
        will_dodge = False

    print(enemy_name_color(enemys[attacker].en_id), end = "")

    dealt_damage = round(enemys[attacker].dmg * (randint(90, 110) / 100))
    cur_crit_chance = enemys[attacker].crit
    crit_count = 0
    while cur_crit_chance > 0:
        if chance(cur_crit_chance):
            dealt_damage *= 2
            crit_count += 1
        cur_crit_chance -= 1
    if len(allys) > 0:
        alive_allies = 0
        for i in allys:
            if i.hp > 0:
                alive_allies += 1
        dealt_damage //= 1 + alive_allies
        if alive_allies > 0:
            print(enemys[attacker].name, "dealt ", end = "")
        k = 0
        for i in allys:
            if i.hp <= 0:
                continue
            k += 1
            ally_dealt_damage = dealt_damage
            ally_dealt_damage -= i.defense
            if ally_dealt_damage < 1:
                ally_dealt_damage = 1
            ally_dealt_damage += enemys[attacker].psn
            if i.imm > 0:
                ally_dealt_damage = 0
            i.hp -= ally_dealt_damage
            if k > 1:
                print(", ", end = "")
            print(ally_dealt_damage, "DMG to", enemy_name_color(i.en_id) + i.name + enemy_name_color(enemys[attacker].en_id), end = "")
        print("!")
    player_dealt_damage = round(dealt_damage * (1 - (player_shield / 100)))
    if player_dealt_damage > player_base_def + player_extra_def:
        player_dealt_damage -= player_base_def + player_extra_def
    else:
        player_dealt_damage = 1
    if immortality_compute() > 0:
        player_dealt_damage = round(dealt_damage * (1 - immortality_compute()))
    if will_dodge == True:
        player_dealt_damage = 0
    player_current_hp -= player_dealt_damage
    if player_current_hp < 0:
        player_current_hp = 0
    if player_spikes > 0:
        enemys[attacker].hp -= player_spikes
        if enemys[attacker].hp < 0:
            enemys[attacker].hp = 0
    if player_dealt_damage > 0:
        print(enemys[attacker].name, "dealt", player_dealt_damage, "DMG! You have", player_current_hp, "HP left!")
        if enemys[attacker].psn > 0:
            player_poisoned += enemys[attacker].psn
            print(enemys[attacker].name, "inflicted", enemys[attacker].psn, "PSN! Your total poison is", player_poisoned, "PSN'd!")
    elif will_dodge == True:
        print(enemys[attacker].name, "dealt no damage to you because you managed to dodge!")
    else:
        print(enemys[attacker].name, "dealt no damage to you because of your immortality!")
    if crit_count == 1:
        print("It was a critical hit!")
    elif crit_count > 1:
        print("They rolled a critical hit", crit_count, "times!")
    if player_spikes > 0:
        print(enemys[attacker].name, "suffered", player_spikes, "DMG from your spikes! They have", enemys[attacker].hp, "HP left!")
        if player_spikes_armor_break > 0:
            enemys[attacker].defense -= player_spikes_armor_break
            print(enemys[attacker].name, "lost", player_spikes_armor_break, "DEF!")

    print("\033[0m", end = "")

def enemy_defend(defender = 0):
    global enemys

    print(enemy_name_color(enemys[defender].en_id), end = "")

    if enemys[defender].original_defense < 3:
        enemys[defender].defense += 1
    else:
        enemys[defender].defense += enemys[defender].original_defense // 3
    print(enemys[defender].name, "defended! Their defense is now", enemys[defender].defense, "DEF!")

    print("\033[0m", end = "")
    
def enemy_magic_hit(attacker = 0):
    global player_current_hp
    global player_base_magic_def
    global player_extra_magic_def
    global player_magic_shield
    global enemys

    print(enemy_name_color(enemys[attacker].en_id), end = "")

    dealt_damage = round(enemys[attacker].dmg * (randint(85, 105) / 100))
    cur_crit_chance = enemys[attacker].crit
    crit_count = 0
    while cur_crit_chance > 0:
        if chance(cur_crit_chance):
            dealt_damage *= 2
            crit_count += 1
        cur_crit_chance -= 1
    dealt_damage = round(dealt_damage * (1 - (player_magic_shield / 100)))
    if dealt_damage > player_base_magic_def + player_extra_magic_def:
        dealt_damage -= player_base_magic_def + player_extra_magic_def
    else:
        dealt_damage = 1
    if immortality_compute() > 0:
        dealt_damage = round(dealt_damage * (1 - immortality_compute()))
    player_current_hp -= dealt_damage
    if player_current_hp < 0:
        player_current_hp = 0
    if dealt_damage > 0:
        print(enemys[attacker].name, "dealt", dealt_damage, "magic DMG! You have", player_current_hp, "HP left!")
    else:
        print(enemys[attacker].name, "dealt no damage to you because of your immortality!")
    if crit_count == 1:
        print("It was a critical hit!")
    elif crit_count > 1:
        print("They rolled a critical hit", crit_count, "times!")

    print("\033[0m", end = "")

def enemy_summon(summoner = 0):
    global enemys

    print(enemy_name_color(enemys[summoner].en_id), end = "")

    spawn = 0
    print(enemys[summoner].name, "summoned ", end = "")
    for k in enemys[summoner].spawner:
        spawn += 1
        if spawn > 1:
            enemys.append(Enemies(k, summoned = True, summoner_id = summoner))
            if spawn == 2:
                print(enemys_name[k], end = "")
            else:
                print(",", enemys_name[k], end = "")
    print(" to their aid.")

    print("\033[0m", end = "")

def enemy_stall(quitter = 0):
    global enemys

    print(enemy_name_color(enemys[quitter].en_id), end = "")

    print(enemys[quitter].name, "did absolutely nothing.")

    print("\033[0m", end = "")

def enemy_heal(healer = 0):
    global enemys

    print(enemy_name_color(enemys[healer].en_id), end = "")

    healed = 0
    print(enemys[healer].name, "attempted to heal ", end = "")
    for i in range(len(enemys)):
        if i == healer:
            continue
        else:
            heal = 0
            for k in range(len(enemys[healer].spawner)):
                heal += 1
                if enemys[i].en_id == enemys[healer].spawner[k] and heal > 1:
                    enemys[i].hp += round(enemys[i].max_hp * 0.1)
                    if enemys[i].hp > enemys[i].max_hp:
                        enemys[i].hp = enemys[i].max_hp
                    healed += 1
                    if healed > 1:
                        print(", ", end = "")
                    print(enemys[i].name, "for", round(enemys[i].max_hp * 0.1), "HP", end = "")
    if healed == 0:
        print("and didn't succed.")
    else:
        print(".")

    print("\033[0m", end = "")

def enemy_stun(stunner = 0):
    global player_stunned
    
    print(enemy_name_color(enemys[stunner].en_id), end = "")

    player_stunned += 2

    print(enemys[stunner].name, "stunned you for 2 turns! You are totally stunned for", player_stunned, "turns!", end = "")
    
    print("\033[0m")

def enemy_berserk(berserk = 0):
    global enemys

    print(enemy_name_color(enemys[berserk].en_id), end = "")

    enemys[berserk].dmg = round(enemys[berserk].dmg * 1.3)
    enemys[berserk].crit = round(enemys[berserk].crit * 2, 2)
    
    print(enemys[berserk].name, "increased their damage up to", enemys[berserk].dmg, "DMG!")
    print(enemys[berserk].name, " increased their crit chance up to ", round(enemys[berserk].crit * 100), "%!", sep = "", end = "")
    
    print("\033[0m")

def ally_hit(attacker = 0):
    global enemys
    global allys

    if len(enemys) > 0:

        print(enemy_name_color(allys[attacker].en_id), end = "")

        dealt_damage = round(allys[attacker].dmg * (randint(90, 110) / 100))
        dealt_damage //= len(enemys)
        print(allys[attacker].name, "dealt ", end = "")
        k = 0
        for i in enemys:
            k += 1
            target_dealt_damage = dealt_damage
            target_dealt_damage -= i.defense
            if target_dealt_damage < 1:
                target_dealt_damage = 1
            if i.imm > 0:
                target_dealt_damage = 0
                target_dealt_poison = 0
            else:
                target_dealt_poison = allys[attacker].psn
            i.hp -= target_dealt_damage
            i.psnd += target_dealt_poison
            if i.spk > 0:
                allys[attacker][1] -= i.spk
            if k > 1:
                print(", ", end = "")
            print(target_dealt_damage, "DMG to", enemy_name_color(i.en_id) + i.name + enemy_name_color(allys[attacker].en_id), end = "")
        print("!")

        print("\033[0m", end = "")

def health_multiplier(enemy_id = 0):
    global score
    global player_max_hp
    global difficulty
    hp_multi = 1
    if score > 177500:
        print("Started to calculate health")
    if enemy_id == 42:
        hp_multi = player_max_hp
    else:
        for i in range(score):
            if hp_multi > 10000000000000000000000:
                hp_multi = int(hp_multi)
                hp_multi += round(hp_multi // 100000000) + ((difficulty - 50) * 1000)
            else:
                hp_multi *= 1.05 + uniform(0.0008 * difficulty + 0.01, 0.0008 * difficulty + 0.06)
                #hp_multi *= 1.05 + (randint(-50 + difficulty, -40 + difficulty) / 100)
                hp_multi = round(hp_multi, 10)
    return hp_multi

def damage_multiplier(enemy_id = 0):
    global score
    global difficulty
    global player_base_dmg
    global player_crit_chance
    global player_crit_chance_reduction
    global player_weapon
    global player_max_hp
    global player_base_magic_def
    global player_min_extra_magic_def
    global player_magic_shield
    dmg_multi = 1
    if score > 177500:
        print("Started to calculate damage")
    if enemy_id == 42:
        dmg_multi = round(player_base_dmg * (weapon_damage_ranges[player_weapon][0] + player_damage_range_boost + weapon_damage_ranges[player_weapon][1] + player_damage_range_boost) / 200)
    elif enemy_id == 51:
        if player_magic_shield != 100:
            dmg_multi = round(0.042 * player_max_hp / ((100 - player_magic_shield) / 100)) + player_base_magic_def + player_min_extra_magic_def
        else:
            dmg_multi = round(0.042 * player_max_hp) + player_base_magic_def + player_min_extra_magic_def
    else:
        for i in range(score):
            if dmg_multi > 10000000000000000000000:
                dmg_multi = int(dmg_multi)
                dmg_multi += round(dmg_multi // 100000000) + ((difficulty - 50) * 1000) 
            else:
                dmg_multi *= 1 + uniform(difficulty * 0.00075 + 0.01, difficulty * 0.00075 + 0.04)
                #dmg_multi *= 1 + (randint(-460 + difficulty * 10, -430 + difficulty * 10) / 1000)
                dmg_multi = round(dmg_multi, 10)
    return dmg_multi

def defense_multiplier(enemy_id = 0):
    global score
    global player_base_def
    def_multi = 1
    if score > 177500:
        print("Started to calculate defense multiplier")
    if enemy_id == 42:
        def_multi = player_base_def
    else:
        for i in range(score):
            if def_multi > 10000000000000000000000:
                def_multi = int(def_multi)
                def_multi += round(def_multi // 100000000) + ((difficulty - 50) * 1000)
            else:
                def_multi *= 1 + uniform(0.0001 * difficulty + 0.005, 0.0001 * difficulty + 0.065)
                #def_multi *= 1 + (randint(-50 + difficulty, -43 + difficulty) / 100)
                def_multi = round(def_multi, 10)
    return def_multi

def defense_addition(enemy_id = 0):
    global score
    global difficulty
    def_add = 0
    if score > 887500:
        print("Started to calculate defense addition")
    if enemy_id == 42:
        def_add = 0
    else:
        if difficulty != 0:
            if difficulty <= 250:
                for i in range(score // (250 // difficulty)):
                    def_add += 1
            else:
                for i in range(round(score * (difficulty // 250))):
                    def_add += 1
    return def_add

def crit_multiplier(enemy_id = 0):
    global score
    global difficutly
    global player_crit_chance
    crit_multi = 1
    if score > 887500:
        print("Started to calculate crit multiplier")
    if enemy_id == 42:
        crit_multi = player_crit_chance / 100
    else:
        for i in range(score):
            if crit_multi < 10000000:
                crit_multi *= 1 + uniform(0.00008 * difficulty + 0.0001, 0.00008 * difficulty + 0.0002)
            else:
                break
    return crit_multi

def spike_multiplier(enemy_id = 0):
    global score
    global player_spikes
    spk_multi = 1
    if score > 177500:
        print("Started to calculate spike multiplier")
    if enemy_id == 42:
        spk_multi = player_spikes
    else:
        for i in range(score):
            if spk_multi > 10000000000000000000000:
                spk_multi = int(spk_multi)
                spk_multi += round(spk_multi // 100000000)
            else:
                spk_multi *= 1 + uniform(0.00058 * difficulty + 0.001, 0.00058 * difficulty + 0.021)
                #spk_multi *= 1 + (randint(3, 5) / 100)
                spk_multi = round(spk_multi, 10)
    return spk_multi

def poison_multiplier(enemy_id = 0):
    global score
    global player_poison
    psn_multi = 1
    if score > 177500:
        print("Started to calculate poison multiplier")
    if enemy_id == 42:
        psn_multi = player_poison
    else:
        for i in range(score):
            if psn_multi > 10000000000000000000000:
                psn_multi = int(psn_multi)
                psn_multi += round(psn_multi // 100000000)
            else:
                psn_multi *= 1 + uniform(0.00058 * difficulty + 0.001, 0.00058 * difficulty + 0.021)
                #psn_multi *= 1 + (randint(3, 5) / 100)
                psn_multi = round(psn_multi, 10)
    return psn_multi

def immortality_multiplier(enemy_id = 0):
    global score
    global player_immortality
    imm_multi = 1
    if score > 177500:
        print("Started to calculate impenetrability multiplier")
    if enemy_id == 42:
        imm_multi = player_immortality // 2
    else:
        for i in range(score):
            if imm_multi > 10000000000000000000000:
                imm_multi = int(imm_multi)
                imm_multi += round(imm_multi // 100000000)
            else:
                imm_multi *= 1 + uniform(0.00018 * difficulty + 0.001, 0.00018 * difficulty + 0.011)
                #imm_multi *= 1 + (randint(1, 2) / 100)
                imm_multi = round(imm_multi, 10)
    return imm_multi

# ENEMYS STATS START
def default_enemies():
    global evolution_name_suffix
    global areas
    global enemys
    global enemy_areas
    global enemy_is_boss
    global enemys_name
    global enemys_name_colors
    global enemys_base_hp
    global enemys_base_dmg
    global enemys_base_def
    global enemys_base_crit
    global enemys_base_spk
    global enemys_base_psn
    global enemys_base_immortality
    global enemys_power_level
    global enemys_descriptions
    global enemys_patterns
    global enemys_spawners
    global enemys_elements
    global enemy_actions
    global ally_actions
    global enemy_unconsumable
    global enemy_unelite
    global bosses_for_areas
    global hunters_appeared
    global global_seed
    seed(global_seed)
    bounty_hunter_name_0 = ["Axel", "Blaze", "Dagger", "Echo", "Flint", "Gage", "Hawk", "Jax", "Kane", "Lex", "Mace", "Nash", "Orin", "Pax", "Quinn", "Raze", "Slade", "Thorn", "Vex", "Wolf"]
    bounty_hunter_name_1 = ["Black", "Blade", "Cage", "Fang", "Grim", "Hunt", "Iron", "Jade", "Knight", "Locke", "Raven", "Shadow", "Stone", "Strike", "Thorne", "Viper", "Ward", "Whisper", "Wolf", "Wylde"]
    evolution_name_suffix = [" Evolved", " Prime", "-Adapter", " Plus", " Mutant"]
    enemys = []
    enemy_areas = [[0, 1], [0], [0], [0, 1], [], [0], [1], [1], [1, 5], [1], [2], [2], [2, 4, 6], [6], [2], [3], [3], [3], [3], [3], [4], [2, 4], [4], [4], [4], [5], [5],
               [5], [5], [6], [6], [6], [6], [], [], [0, 1, 3, 5], [1, 2, 3, 6], [1, 4, 5, 6], [], [], [], [], [0, 1, 2, 3, 4, 5, 6], [0], [1, 2], [2], [3], [4], [5], [5],
               [6], [], [], [], [], [6], [], [6], [0], [2], [3], [4], [6], ["drought"], []]
    enemy_is_boss = [False, False, False, False, False, True, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False,
                 False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False,
                 False, False, False, False, False, False, False, False, False, True, True, True, True, False, False, False, True, True, True, True, True, False,
                 True]
    enemys_power_level = [1, 0.9, 0.75, 1.35, 1.7, 1, 1.02, 0.95, 1.05, 1, 1.07, 0.95, 1.45, 0.55, 1, 1, 1.05, 0.6, 1.12, 1, 0.85, 1.15, 1, 1.4, 1, 1, 1.1, 1.07,
                      1, 1.15, 1.1, 1.45, 1, 2, 1.65, 1.75, 1.75, 1.75, 1.9, 1.9, 2, 2, 2, 1.1, 1.07, 0.5, 1.45, 1.3, 1.05, 0.8, 1.3, 1.5, 2.3, 1.3, 1.6, 1.02, 0.5,
                      1.2, 1.1, 1, 1.05, 0.6, 0.9, 0.25, 1.5]
    enemys_name = ["Bush Man", "Weird Plant", "Arachno-flower", "Ent", "Spirit of Fear", "Treant", "Thug", "Bandit", "Dark Mage", "Bandit Chieftain", "Skeleton Warrior",
               "Undead Miner", "Bone Serpent", "Skeleton", "Soul Catcher", "Snowman Knifer", "Ice Elemental", "Snowman", "Snow Mage", "Yeti", "Spiderling",
               "Cave Spider", "Gargoyle", "Matriarch", "Spider Queen", "Cactus", "Desert Spider", "Sandwitch", "Cactus Golem", "Necromancer", "Poison Spider",
               "Rotten Ent", "Undead Paladin", "Shopkeeper", "Spirit of Kindness", choice(bounty_hunter_name_0) + " " + choice(bounty_hunter_name_1),
               choice(bounty_hunter_name_0) + " " + choice(bounty_hunter_name_1), choice(bounty_hunter_name_0) + " " + choice(bounty_hunter_name_1),
               "Spirit of Vitality", "Spirit of Strength", "Spirit of Might", "Spirit of Protection", "Yourself", "Venomous Roser", "Crystal Assassin",
               "Crystal Shard", "Snowman Shotgunner", "Arachno Mage", "Big Jerboa", "Tumbleweeder", "Dark Knight", "Death", "The 3173rd", "Change", "Cycle",
               "Amphibian Heretic", "Spectral Frog", "Amphibromancer", "Rose Knight", "Crystal Wizard", "Buff Polar Bear", "Spider King", "False Idol", "Wrom",
               "Insane Alchemist"]
    enemys_name_colors = [[0, 170, 0], [0, 230, 0], [180, 200, 0], [180, 100, 0], [140, 0, 155], [190, 90, 0], [200, 185, 105], [200, 175, 120], [60, 60, 60],
                      [200, 185, 125], [210, 210, 170], [170, 165, 140], [170, 200, 170], [210, 210, 210], [75, 220, 220], [240, 240, 240], [40, 220, 220],
                      [240, 240, 240], [135, 220, 220], [190, 190, 190], [50, 65, 90], [90, 95, 110], [130, 140, 130], [50, 160, 90], [70, 200, 140],
                      [90, 240, 90], [120, 80, 70], [200, 175, 20], [110, 200, 110], [140, 180, 170], [50, 220, 50], [90, 90, 30], [100, 100, 100],
                      [100, 220, 100], [240, 240, 0], [40, 210, 210], [210, 40, 40], [40, 210, 40], [0, 255, 0], [255, 0, 0], [255, 128, 0], [0, 200, 255],
                      [249, 241, 165], [200, 0, 50], [255, 100, 255], [255, 100, 255], [255, 230, 230], [40, 100, 100], [150, 150, 100], [150, 150, 50],
                      [60, 70, 60], [100, 100, 100], [249, 241, 165], [100, 100, 175], [100, 200, 250], [20, 200, 20], [0, 250, 250], [0, 250, 100], [200, 0, 35],
                      [255, 50, 255], [255, 200, 200], [100, 210, 100], [75, 250, 75], [250, 220, 100], [200, 0, 150]]
    enemys_elements = [[6], [6], [6], [2, 6], [4], [2, 6], [2], [2], [5], [1, 2], [0], [0], [0, 6], [0], [5, 6], [1], [5], [], [1, 5], [1], [3], [5], [3], [0], [3], [4],
                       [4], [4, 5], [4], [0, 5], [0], [0, 2], [0, 2], [], [5], [2], [1], [], [0, 5], [1, 5], [3, 5], [2, 6, 5], [6], [6], [], [0], [1], [3], [4], [4],
                       [0, 2], [3], [6, 4, 0, 3, 2, 1], [5], [6], [], [], [], [6], [5], [1], [3], [], [4], [1]] # 0 - Vitality, 1 - Strength, 2 - Protection, 3 - Might, 4 - Innocence, 5 - Mana, 6 - Magic Protection
    enemys_base_hp = [30, 25, 23, 50, 50, 65, 35, 30, 27, 65, 31, 27, 40, 10, 55, 20, 27, 10, 25, 70, 10, 30, 25, 45, 60, 26, 32, 27, 60, 25, 30, 55, 65, 50, 60,
                  60, 42, 56, 150, 50, 30, 60, 1, 30, 30, 10, 19, 40, 35, 30, 40, 100, 350, 75, 125, 30, 7, 35, 60, 50, 65, 30, 50, 20, 50]
    enemys_base_dmg = [10, 7, 8, 12, 14, 14, 10, 9, 7, 13, 10, 9, 12, 4, 10, 15, 7, 5, 4, 13, 7, 11, 9, 12, 12, 10, 11, 4, 12, 5, 12, 14, 12, 10, 10, 10, 25, 15,
                   20, 60, 30, 17, 1, 10, 14, 4, 40, 9, 13, 7, 15, 1, 50, 20, 30, 10, 0, 9, 10, 12, 20, 15, 10, 7, 12]
    enemys_base_def = [0, 0, 0, 0.3, 2, 1, 0, 0, 0, 2, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 7, 2, 15, 2, 5, 7, 3, 0, 40, 1, 1, 1, 0, 0, 0,
                       0.2, 0, 2.5, 4, 150, 3, 15, 0, 0, 0, 1, 1, 0, 0, 2, 0, 2]
    enemys_base_crit = [0.02, 0.01, 0.02, 0.04, 0.12, 0.06, 0.05, 0.05, 0.03, 0.09, 0.07, 0.04, 0.1, 0.01, 0.06, 0.05, 0.04, 0.01, 0.03, 0.11, 0.1, 0.05, 0.15, 0.1, 0.1,
                        0.06, 0.05, 0.03, 0.07, 0.03, 0.06, 0.06, 0.1, 0.35, 0.13, 0.05, 0.4, 0.1, 0.03, 0.2, 0.8, 0.05, 1, 0.04, 0.07, 0.01, 0, 0.03, 0.03, 0.02, 0.1, 1,
                        0.4, 0.1, 0.1, 0.04, 0, 0.03, 0.1, 0.06, 0.1, 0.1, 0.07, 0.01, 0.05]
    enemys_base_spk = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 7, 0, 0, 0, 10, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0,
                       0.25, 0.25, 0, 5, 15, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    enemys_base_psn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 2, 3, 0, 2, 0, 0, 0, 4, 0, 0, 7, 0, 0, 0, 10, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                       0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0]
    enemys_base_immortality = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0,
                               0, 0, 0, 0, 0.3, 2.5, 1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0.45, 0, 0]
    enemys_descriptions = ["That's a weird looking bush", "Boring plant, uses roots as its legs", "This plant usually accompanies its other siblings",
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
                       "Is that who you truly are?", "Thorny, venomous predator, that leaves its prey slowly dying",
                       "Empowered by corrupt crystals of the Stale Cave, they seek out powerful foes", "Crystals infused with life force of corrupt crystals",
                       "This snowman appears to be possessed... and has a freaking shotgun", "This mage is adept at healing arachnids",
                       "This rodent has sharp teeth, and what appears to be spiky fur", "A big bug that uses tumbleweed as a nest",
                       "Corrupted by eternal life, this knight mindlessly protects the Holy Forest",
                       "'Death comes for all of us. And those who cheat her, have to fight her'", "Greatest Cycle's creation yet, it is ready to consume you",
                       "'Once one cycle ends, something changes, allowing for a new cycle to be born'", "'Once one cycle ends, something changes, allowing for a new cycle to be born'",
                       "These heretics worship false idols of Great J", "These vengeful spirits, that resemble frogs, are the last resort of many amphibian heretics",
                       "Elite amphibian heretic, who learned how manipulate and create frogs", "The great knight that protects the Garden's grounds",
                       "A great wizard that infused himself with corrupted crystals of the Stale Cave", "There is little explanation of how this bear has visible abs",
                       "Male Spidernachs are considerably smaller than their counterparts", "This frog has been empowered by magic of amphibian heretics",
                       "This worm like creature is quite common during dry weather", "Kto, kto, kto, kto, kto"]
    enemys_patterns = [[0], [0], [0], [0, 0, 0, 0, 0, 0, 1], [2, 2, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0], [0], [2], [0, 0, 0, 1, 0, 0, 0], [0], [0],
                   [0, 0, 0, 0, 0, 0, 0, 1], [0], [2, 2, 2, 0], [0], [2], [0], [3, 2, 2], [0, 0, 0, 1, 0, 0, 0], [0], [0], [0], [0, 4, 3, 4, 0, 4],
                   [0, 0, 0, 4, 4, 3], [0], [0], [2, 2, 2, 2, 2, 5], [0, 0, 0, 0, 1], [2, 3, 2], [0, 0, 4, 0], [0, 1, 0, 0, 1, 0, 0, 0, 0], [2, 2, 1, 2, 2, 0],
                   [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1], [2, 1, 2, 1, 0, 0], [1, 1, 0], [0], [1, 0, 0, 0, 0, 0, 1, 1], [2, 2, 5, 5, 2], [0, 2], [0],
                   [2, 1, 2, 2, 1, 1, 2, 2], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1], [0], [0], [0, 4], [2, 2, 5], [0], [1, 0], [0, 1, 0], [2], [0], [2], [0, 0, 5],
                   [0, 0, 0, 1], [0], [3, 0, 0, 0], [0], [2], [0, 0, 1, 0], [0, 4], [0, 2, 1], [0], [0, 6, 0, 0, 7, 0]]
    enemys_spawners = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1, 13, 13], [0], [0], [0], [0], [0], [0, 17], [0], [0], [0], [0],
                       [0, 20, 20], [0, 20, 20], [0], [0], [0, 25, 26, 27, 28, 48, 49], [0], [0, 13], [0], [0], [0], [1, 34], [0], [0], [0], [0],
                       [0, 0, 1, 2, 3, 5, 6, 7, 8, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 33, 43, 44, 45, 46, 47, 48, 49, 50, 52, 58, 59, 60, 61],
                       [0], [0], [0], [0], [0], [1, 45], [0], [0], [0, 20, 21, 23, 24, 26, 30, 61], [0], [0], [1, 13], [0], [0], [0], [0, 52], [1, 56],
                       [0], [1, 56, 56], [0], [0], [0], [0], [1, 56, 56, 56, 56], [0], [0]]
    enemy_actions = [enemy_hit, enemy_defend, enemy_magic_hit, enemy_summon, enemy_stall, enemy_heal, enemy_stun, enemy_berserk]
    ally_actions = [ally_hit, ally_hit, ally_hit, ally_hit, ally_hit, ally_hit, ally_hit]
    enemy_unconsumable = [4, 34, 38, 39, 40, 41, 42, 51, 52, 53, 54, 64]
    enemy_unelite = [4, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 51, 52, 53, 54, 64]
    bosses_for_areas = [[5, 58], [9], [14, 59], [19, 60], [24, 61], [28], [32, 62]]
    hunters_appeared = [False, False, False]

class Enemies:
    def __init__(self, enemy_id = 0, summoned = False, summoner_id = 0, elite = 0):
        global difficulty
        global enemys
        global fear_anger, vitality_anger, protection_anger, strength_anger, might_anger, shopkeeper_deaths, spirit_anger_reduction

        if enemy_id == 4 and fear_anger - spirit_anger_reduction > 1:
            multiplier = round(fear_anger) - spirit_anger_reduction
        elif enemy_id == 34 and shopkeeper_deaths - spirit_anger_reduction > 1:
            multiplier = round(shopkeeper_deaths) - spirit_anger_reduction
        elif enemy_id == 38 and vitality_anger - spirit_anger_reduction > 1:
            multiplier = round(vitality_anger) - spirit_anger_reduction
        elif enemy_id == 39 and strength_anger - spirit_anger_reduction > 1:
            multiplier = round(strength_anger) - spirit_anger_reduction
        elif enemy_id == 40 and might_anger - spirit_anger_reduction > 1:
            multiplier = round(might_anger) - spirit_anger_reduction
        elif enemy_id == 41 and protection_anger - spirit_anger_reduction > 1:
            multiplier = round(protection_anger) - spirit_anger_reduction
        else:
            multiplier = 1
            
        elite_prefixes = []
        if not enemy_id in enemy_unelite:
            possible_elite_prefixes = ["Toxic ", "Impenetrable ", "Critical ", "Thorny ", "Tanky "]
            for i in range(elite):
                item = choice(possible_elite_prefixes)
                possible_elite_prefixes.remove(item)
                elite_prefixes.append(item)

        name_prefix = ""
        for i in elite_prefixes:
            name_prefix = name_prefix + i

        self.en_id = enemy_id
        self.name = name_prefix + enemys_name[enemy_id]
        self.description = enemys_descriptions[enemy_id]
        if "Tanky " in elite_prefixes:
            self.hp = round(enemys_base_hp[enemy_id] * health_multiplier(enemy_id) * multiplier * 2.3)
        else:
            self.hp = round(enemys_base_hp[enemy_id] * health_multiplier(enemy_id) * multiplier)
        self.max_hp = self.hp
        self.dmg = round(enemys_base_dmg[enemy_id] * damage_multiplier(enemy_id) * multiplier)
        self.defense = round((enemys_base_def[enemy_id] + defense_addition(enemy_id)) * defense_multiplier(enemy_id) * multiplier)
        if "Critical " in elite_prefixes:
            self.crit = round(enemys_base_crit[enemy_id] * 2, 2) * crit_multiplier(enemy_id)
        else:
            self.crit = round(enemys_base_crit[enemy_id], 2) * crit_multiplier(enemy_id)
        self.original_defense = self.defense
        if "Thorny " in elite_prefixes:
            self.spk = round((enemys_base_spk[enemy_id] + 2) * spike_multiplier(enemy_id) * multiplier * 2.3)
        else:
            self.spk = round(enemys_base_spk[enemy_id] * spike_multiplier(enemy_id) * multiplier)
        if "Toxic " in elite_prefixes:
            self.psn = round((enemys_base_psn[enemy_id] + 2) * poison_multiplier(enemy_id) * multiplier * 1.5)
        else:
            self.psn = round(enemys_base_psn[enemy_id] * poison_multiplier(enemy_id) * multiplier)
        if summoned:
            self.psnd = enemys[summoner_id].psnd // 2
        else:
            self.psnd = 0
        self.stnd = 0
        if "Impenetrable " in elite_prefixes:
            self.imm = round((enemys_base_immortality[enemy_id] + 2) * immortality_multiplier(enemy_id) * multiplier)
        else:
            self.imm = round(enemys_base_immortality[enemy_id] * immortality_multiplier(enemy_id) * multiplier)
        self.pattern = enemys_patterns[enemy_id].copy()
        self.pattern_action = 0
        self.spawner = enemys_spawners[enemy_id].copy()
        if not enemy_id in [4, 34, 38, 39, 40, 41] and not summoned:
            self.money = round((self.hp + (self.dmg * 2) + (self.defense * 3) + (self.spk * 1.5) + (self.psn * 2.5) + (self.imm * 10)) * 55 / (13 * difficulty))
            self.xp = round((self.hp + (self.dmg * 2) + (self.defense * 3) + (self.spk * 1.5) + (self.psn * 2.5) + (self.imm * 10)) * 55 / (10 * difficulty))
        else:
            self.money = 0
            self.xp = 0
# ENEMYS STATS END

# AREA STATS START
areas = ["Garden", "Deep Forest", "Cave", "Tundra", "Canyon", "Desert", "Rotten Forest"]
areas_colors = [[0, 255, 100], [32, 150, 32], [140, 140, 140], [200, 200, 230], [150, 180, 150], [190, 210, 0], [125, 125, 125]]
water_colors_0 = [[0, 200, 255], [0, 100, 150], [0, 150, 150], [0, 150, 150], [0, 170, 100], [0, 255, 255], [0, 255, 100]]
water_colors_1 = [[0, 100, 128], [0, 50, 75], [0, 75, 75], [0, 75, 75], [0, 85, 50], [0, 128, 128], [0, 128, 50]]
path_lengths = [[3, 3], [0, 3], [0, 2], [2, 3], [1, 3], [3, 4], [0, 3]] # [min, max]
height_variaty = [[0, 0], [-1, 1], [-2, 2], [-1, 3], [-1, 2], [-1, 1], [-2, 1]]
wall_min_thickness = [1, 3, 2, 1, 1, 1, 2]
turn_right_prob = [1, 1, 1, 1, 1, 1, 1]
turn_down_prob = [1, 1, 1, 0.95, 1, 1, 1]
turn_left_prob = [1, 1, 1, 1, 1, 1, 1]
turn_up_prob = [1, 1, 1, 0.5, 0.5, 1, 1]
area_max_x = [83, 41, 23, 41, 54, 54, 47]
area_max_y = [15, 10, 8, 10, 5, 12, 12]
start_positions = [["ul", "ml", "dl"], ["ul", "um", "ur", "dl", "dm", "dr"], ["mm"], ["um", "dm", "ml"], ["ul", "ur"],
                   ["ul", "ur", "dl", "dr"], ["ul", "um", "ur", "ml", "mr", "dl", "dm", "dr"]]
remnants_spawns = [[0, 4, 3], [0, 2, 0], [0, 0, 0], [0, 1, 1], [0, 4, 0], [0, 6, 1], [0, 3, 0]] # first value - min, second value - max, third value - average
snow_pile_spawns = [0, 0, 0.05, 0.1, 0, 0, 0]
water_level = 0
default_water_levels = [3, 2, 1, 2, 1, 0, 1.5]
river_prob = [0, 0.75, 0, 0.75, 0, 1, 2]
river_thickness = [1, 1, 1, 1, 1, 1, 1]
escape_river_prob = [0, 0.45, 0.25, 0.65, 0, 0.25, 0.55]
pond_prob = [1, 0.1, 0.5, 0, 0, 0, 0]
pond_radius = [4, 4, 4, 0, 0, 1, 0]
weathers = [[0], [0, 1, 2, 7, 8, 9], [0, 3, 8], [0, 2, 4, 7, 8], [0, 1, 2, 3, 7, 9], [0, 1, 5, 8, 9], [0, 2, 6, 8, 9]] # 0 - nothing, 1 - rain, 2 - thick fog, 3 - earth quake, 4 - blizzard, 5 - sandstorm, 6 - acid rain, 7 - hail, 8 - flood, 9 - drought
weather_chance = [0, 1, 0.5, 0.4, 0.7, 0.5, 0.9]
weathers_durations = [[0, 5], [10, 30], [6, 12], [5, 7], [5, 15], [6, 24], [4, 12], [6, 18], [4, 8], [7, 14]]
current_weather = [0]
current_weather_duration = [0]
events = [] # 0 - path, 1 - fight, 2 - altar, 3 - shop, 4 - bossfight, 5 - mimic gamble, 6 - muddy path, 7 - small snow pile, 8 - big snow pile, 9 - non-existent snow pile,
# 10 - deep water, 11 - boat person, 12 - extra exit, 13 - weird story mode man, 14 - remnants, 15 - crystal path, 16 - inactive crystal path, 17 - pre crystal path,
# 18 - pre crystal fight, 19 - crystal fight, 20 - inactive crystal fight, 21 - pre crystal altar, 22 - crystal altar, 23 - inactive crystal altar, 24 - alchemist's brewery,
# 25 - raid deactivated fight, 26 - raid deactivated altar, 27 - raid deactivated crystal fight, 28 - raid deactivated crystal altar
benefitial_events = [2, 3, 5, 11, 12, 13, 14, 21, 22, 23, 24]
hurtful_events = [1, 4, 7, 8, 18, 19, 20]
neutral_events = [0, 6, 9, 10, 15, 16, 17, 25, 26, 27, 28]
events_coordinates = [] # [x, y]
events_heights = []
player_coordinates = [0, 0]
map_complexity = 0
game_time = 0
escaped = False

player_hp_penalty = 0
player_def_penalty = 0
player_oxygen_danger = False
# AREA STATS END

# META STATS START
difficulty = 55 # suggested 0 - 100
original_difficulty = 55
evolution = False
overkill = False
speedrunner = False
speed_timer = 0
item_rando = False
eclipse = False
weather_amount = 1
score_increase = 0
score = 0
raid_counter = 0
max_power_level = 1
max_power_level_increase = 0
win = 0
lost = 0
forest_enemy_spawn = 0
enough_destroyed = False
is_boss_battle = False
final_area = False

global_seed = 0
daily_seed = 0

map_seed = 0
enemy_encouter_seed = 0
evolution_seed = 0
altar_seed = 0
shop_seed = 0
gamble_seed = 0
remnant_seed = 0
weather_seed = 0
weather_effects_seed = 0

area = "None"
area_id = 0
# META STATS END

# PLAYER STATS START
allies = []

player_money = 0
player_xp = 0
player_level = 0

player_max_hp = 100
player_current_hp = player_max_hp 
player_base_dmg = 5
player_weapon = 0
player_base_def = 0
player_extra_def = 0
player_base_magic_def = 0
player_extra_magic_def = 0
player_extra_magic_def_buff = 0
player_crit_chance = 5  # in %
player_poison = 0
player_poisoned = 0
player_spikes = 0
player_stunned = 0
last_altar = []

player_shield = 0 # in %
player_magic_shield = 0 # in %
player_gold_boost = 0 # in %
player_damage_range_boost = 0 # in %
player_poison_def = 0
player_spikes_armor_break = 0
player_crit_chance_reduction = 100 # in %
last_boss = []

player_lifesteal = 0 # in %
player_immortality = 0 # in turns
player_current_immortality = player_immortality
player_regen = 0
player_consume = 0
player_travel = 0
player_enemy_explotano = 0
player_extra_life = 0
player_spent_life = 0
player_dodge_chance = 0
player_dodge_count = 0
player_dodged = False

player_boat = False
player_items = [0] # 1 - cookie, 2 - antidote, 3 - gambler's drink, 4 - cooked meat, 5 - winter tea, 6 - heal potion, 7 - berserk's potion, 8 - stun potion

mimic_got_item = False
debt = 0
shopkeeper_sus = 0 # in decimals
shopkeeper_deaths = 0
alchemist_anger = 0
alchemist_defeated = 0
alchemist_visited = False
bought_from_alchemist = False
cur_shopkeeper_dead = False
death_encounters = 0
death_defeated = False
change_encouters = 0
change_recruited = False
brewery_encouters = 0

vitality_anger = 0 # in decimals
strength_anger = 0 # in decimals
might_anger = 0 # in decimals
protection_anger = 0 # in decimals
fear_anger = 0 # in decimals
spirit_anger_reduction = 0

mimic_gamble_encounters = 0
# PLAYER STATS END

# SHOP ITEMS START
item_names = ["Nothing", "Poison Flask", "Armor Spikes", "Bottle of Lifesteal", "Bottle of Midas' power", "Bottle of Impenetrability", "Mark of the Undead", "Consume",
              "Traveller's Hallow", "Enemy Explotano", "Life's Gift", "Cookie", "Antidote", "Gambler's Drink", "Cooked Meat", "Winter Tea", "Band of Agility",
              "Heal Potion", "Berserk's Potion", "Stun Potion"]
item_base_costs = [0, 20, 20, 40, 30, 70, 60, 100, 25, 40, 100, 23, 27, 30, 30, 25, 40, 50, 42, 52]
item_bought = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
item_descriptions = ["It is literally nothing", "Allows sharp weapons to inflict poison onto your enemies", "Enemies will get damaged when hit you",
                     "Dealing damage will heal you", "More coins will be dropped", "You will be immortal for a turn", "You will regenerate health every turn", "Kill to grow",
                     "You will get experience for entering new area", "Enemies explode on death, dealing damage to other enemies",
                     "If you die, you will be revived with no money or experience", "Heals 20% HP and adds 20% of base DEF on use (consumable)",
                     "Clears any poison applied to you on use (consumable)", "Shapeshifts into a random consumable object on use (consumable)",
                     "Heals 50% HP on use (consumable)", "Increases damage by 50% if snow-related enemies are present (consumable)", "Grants chance to dodge physical attacks",
                     "Heals 100% HP on use (consumable)", "Increases damge by 30% and doubles crit chance (consumable)", "Stuns enemies for 3 turns (consumable)"]
item_descriptions_mimic = ["It's literally nothing, pal", "This thing kills stuff over time", "Guys that attack you, will get damaged for doing so", "Turn damage into heal!",
                           "Not sure why I don't use this one myself, but you will gain more money", "You will become untouchable, but that will fade away after a turn",
                           "How do you think undead people live? They use this to regenerate", "Oh, I don't know about this one, pal. Pretty dark stuff", 
                           "Do a world tour and become more experienced!", "Enemies go boom and make other enemies go 'ouch'. Does that sound convincing?",
                           "Another life, pal. But you will be revived broke and unexpirienced", "They say that if you eat this, you will regenerate and stuff. But I can't test it myself, pal",
                           "Don't you hate being poisoned? Well, this will help with getting rid of it, pal!", "This one is like me! Try to drink it and it turns into something random!",
                           "Ever-warriors, like you, enjoy eating flesh. I believe it heals half of your health, pal",
                           "After drinking this tea, you will become stronger if snow enemies are there to witness it", "You will be so quick, that you have a chance to dodge stuff, pal",
                           "This potion heals all of your wounds, pal", "You become stronger and mightier when you drink this", "Bad guys will do nothing 3 times in a row"]
consumable_item_names = ["Nothing", "Cookie", "Antidote", "Gambler's Drink", "Cooked Meat", "Winter Tea", "Heal Potion", "Berserk's Potion", "Stun Potion"]
consumable_item_desc = ["How in the world do you have a Nothing in your inventory?", "Heals 20% HP and adds 20% of base DEF on use (consumable)",
                        "Clears any poison applied to you on use (consumable)", "Shapeshifts into a random consumable object on use (consumable)",
                        "Heals 50% HP on use (consumable)", "Increases damage if snow-related enemies are present", "Heals 100% HP (consumable)",
                        "Increases damge by 30% and doubles crit chance (consumable)", "Stuns enemies for 3 turns (consumable)"]
# SHOP ITEMS END

# WEAPONS START
weapon_names = ["Trusty Sword", "Magic Wand", "Double Daggers", "Great Hammer", "Syringe"]
weapon_damage_ranges = [[80, 120], [50, 80], [95, 135], [90, 120], [5, 10]]
weapon_descriptions = ["Your favourite weapon of all time. Damage ranges between 80%~120%. Crowd factor is 1; poison factor is 1.",
                       "Extremely weak weapon, but provides 15 MGCDEF. Damage ranges between 50%~80%. Crowd factor is 1; poison factor is 0.2",
                       "Very sharp weapon, which makes deep cuts. Damage ranges between 95%~135%. Crowd factor is 0.5; poison factor is 1.7",
                       "Decent crowd control weapon. Damage ranges between 70%~150%. Crowd factor is 3; poison factor is 0.2",
                       "Infinitely weak weapon on its own, but very good at injecting poison. Damage ranges between 5%~10%. Crowd factor is 0.1; posion factor is 4"]
weapon_poison_factor = [1, 0.2, 1.7, 0.2, 4]
weapon_crowd_factor = [1, 1, 0.5, 3, 0.1]
weapon_base_costs = [45, 20, 60, 55, 75]
# WEAPONS END

def fight(enemy_ids = [0], ally_ids = []):
    global score
    global score_increase
    global max_power_level
    global player_money
    global money_gain
    global player_xp
    global xp_gain
    global player_level
    global player_max_hp
    global player_current_hp
    global player_base_dmg
    global player_crit_chance
    global player_crit_chance_reduction
    global player_weapon
    global player_base_def
    global player_extra_def
    global player_base_magic_def
    global player_extra_magic_def
    global player_min_extra_magic_def
    global player_poison
    global player_poisoned
    global player_shield
    global player_magic_shield
    global player_poison_def
    global player_spikes_armor_break
    global player_gold_boost
    global player_lifesteal
    global player_immortality
    global player_current_immortality
    global player_regen
    global player_enemy_explotano
    global player_extra_life
    global player_spent_life
    global player_dodge_chance
    global player_stunned
    global enemys
    global allys
    global is_boss_battle
    global win
    global lost
    global current_weather
    global fear_anger
    global vitality_anger
    global strength_anger
    global might_anger
    global protection_anger
    global shopkeeper_deaths
    global player_hp_penalty
    global player_def_penalty
    global player_damage_buff
    global player_crit_chance_buff
    win = 0
    lost = 0
    money_gain = 0
    xp_gain = 0
    player_current_hp = player_max_hp - round(player_max_hp * player_hp_penalty)
    player_hp_penalty = 0
    player_extra_def = - player_def_penalty
    player_def_penalty = 0
    player_extra_magic_def = round(player_extra_magic_def_buff * player_base_magic_def)
    player_poisoned = 0
    player_current_immortality = player_immortality
    player_damage_buff = 0
    player_crit_chance_buff = 0
    player_stunned = 0
    enemys = []
    allys = []
    enemy_deletions = []
    k = 0
    original_enemy_count = 0
    for i in enemy_ids:
        elite_counter = 0
        while chance(0.1 * (difficulty / 55)):
            elite_counter += 1
            if elite_counter >= 5:
                break
        enemys.append(Enemies(i, elite=elite_counter))
        #[0] name, [1] current hp, [2] max hp, [3] damage, [4] defense, [5] original defense, [6] description, [7] pattern, [8] pattern action, [9] spawner, [10] spikes, [11] enemy id, [12] money, [13] poisoned, [14] xp, [15] poison, [16] immortality
        k += 1
        original_enemy_count += 1
        if k > 1:
            print("\033[0m and ", end = '')
        print(enemy_name_color(i) + enemys_name[i], end = '')
    if k > 5:
        print("\033[0m swarm you!")
    elif k > 1:
        print("\033[0m block your way!")
    else:
        print("\033[0m blocks your way!")
    k = 0
    for i in ally_ids:
        jank_code_variable_for_health = round(enemys_base_hp[i] * health_multiplier(i))
        jank_code_variable_for_defense = round((enemys_base_def[i] + defense_addition(i)) * defense_multiplier(i))
        allys.append([enemys_name[i], jank_code_variable_for_health, jank_code_variable_for_health, round(enemys_base_dmg[i] * damage_multiplier(i)), jank_code_variable_for_defense, jank_code_variable_for_defense, enemys_descriptions[i], enemys_patterns[i].copy(), 0, enemys_spawners[i].copy(), round(enemys_base_spk[i] * spike_multiplier(i)), i])
        allys[k].append(0)
        allys[k].append(0)
        allys[k].append(0)
        allys[k].append(round(enemys_base_psn[i] * poison_multiplier(i)))
        allys[k].append(round(enemys_base_immortality[i] * immortality_multiplier(i)))
        k += 1
    while True:
        while True:
            print("\033[33;1mYour stats: ", player_current_hp, "/", player_max_hp, " HP; ", round(player_base_dmg * ((player_damage_buff / 100) + 1)), " DMG; ", round(player_crit_chance * ((player_crit_chance_buff / 100) + 1)), "% CRT; ", player_base_def, "+", player_extra_def, " DEF", sep = "", end = "")
            if player_base_magic_def + player_extra_magic_def > 0:
                print("; ", player_base_magic_def, "+", player_extra_magic_def, " MGCDEF", sep = "", end = "")
            if player_poison_def > 0:
                print("; ", player_poison_def, " PSNDEF", sep = "", end = "")
            if player_regen > 0:
                print("; ", player_regen, "% REG", sep = "", end = "")
            if player_poison > 0:
                print("; ", player_poison, " PSN", sep = "", end = "")
            if player_spikes > 0:
                print("; ", player_spikes, " SPK", sep = "", end = "")
            if player_spikes_armor_break > 0:
                print("; ", player_spikes_armor_break, " DEFRED", sep = "", end = "")
            if player_shield > 0:
                print("; ", player_shield, "% SHLD", sep = "", end = "")
            if player_magic_shield > 0:
                print("; ", player_magic_shield, "% MGCSHLD", sep = "", end = "")
            if player_lifesteal > 0:
                print("; ", player_lifesteal, "% LFST", sep = "", end = "")
            if player_dodge_chance > 0:
                print("; ", player_dodge_chance, "% DCH", sep = "", end = "")
            if player_poisoned > 0:
                print("; ", player_poisoned, " PSN'd", sep = "", end = "")
            if player_current_immortality > 0:
                print("\nImpenetrability for ", player_current_immortality, " turn(s). Absorbs: ", int(immortality_compute() * 100), "% of dealt DMG.", sep = "")

            if len(allys) > 0:
                print("\033[31;0m\nStats of your allies:")
                for i in range(len(allys)):
                    print(i + 1, ". ", enemy_name_color(allys[i][11]) + allys[i][0], ": ", allys[i][1], "/", allys[i][2], " HP; ", allys[i][3], " DMG; ", allys[i][4], " DEF", sep = "", end = "")
                    if allys[i][10] > 0:
                        print("; ", allys[i][10], " SPK", sep = "", end = "")
                    if allys[i][15] > 0:
                        print("; ", allys[i][15], " PSN", sep = "", end = "")
                    if allys[i][13] > 0:
                        print("; ", allys[i][13], " PSN'd", sep = "", end = "")
                    if allys[i][16] > 0:
                        print("; Impenetrable for ", allys[i][16], " turns", sep = "", end = "")
                    print("\033[31;0m")

            print("\033[31;0m\nStats of your enemies:")
            for i in range(len(enemys)):
                print(i + 1, ". ", enemy_name_color(enemys[i].en_id) + enemys[i].name, ": ", enemys[i].hp, "/", enemys[i].max_hp, " HP; ", enemys[i].dmg, " DMG; ", round(enemys[i].crit * 100), "% CRT; ", enemys[i].defense, " DEF", sep = "", end = "")
                if enemys[i].spk > 0:
                    print("; ", enemys[i].spk, " SPK", sep = "", end = "")
                if enemys[i].psn > 0:
                    print("; ", enemys[i].psn, " PSN", sep = "", end = "")
                if enemys[i].psnd > 0:
                    print("; ", enemys[i].psnd, " PSN'd", sep = "", end = "")
                if enemys[i].stnd > 0:
                    print("; ", enemys[i].stnd, " STN'd", sep = "", end = "")
                if enemys[i].imm > 0:
                    print("; Impenetrable for ", enemys[i].imm, " turns", sep = "", end = "")
                print("\033[31;0m")
            if player_stunned > 0:
                print("You are stunned! You can't do anything!")
                player_stunned -= 1
                break
            else:
                print("What will you do?")
                print("1. Hit")
                print("2. Defend")
                print("3. Inspect")
                print("4. Self Inspect")
                if len(enemys) > 1:
                    print("5. Broad Hit")
                print("8. Items")
                print("9. Do Nothing")
                print("Type in the action")
                action = input()
                if action == '1' or action.lower() == "hit":
                    if len(enemys) > 1:
                        print("Choose enemy")
                        for i in range(len(enemys)):
                            print(i + 1, ". ", enemy_name_color(enemys[i].en_id) + enemys[i].name, "\033[0m", sep='')
                        hit_action = input()
                        if hit_action.isdigit():
                            hit_action = int(hit_action)
                            if hit_action > 0 and hit_action <= len(enemys):
                                player_hit(hit_action - 1)
                                break
                    else:
                        player_hit(0)
                        break
                elif action == '2' or action.lower() == "defend":
                    if player_base_def < 5:
                        player_extra_def += 1
                    else:
                        player_extra_def += player_base_def // 3
                    print("\033[33;1mYou defended! Your defense has increased to", player_base_def + player_extra_def, "DEF!\033[0m")
                    break
                elif action == '3' or action.lower() == "inspect":
                    if len(enemys) > 1:
                        print("Choose enemy")
                        for i in range(len(enemys)):
                            print(i + 1, ". ", enemy_name_color(enemys[i].en_id) + enemys[i].name, "\033[0m", sep='')
                        inspect_action = input()
                        if inspect_action.isdigit():
                            inspect_action = int(inspect_action)
                            if inspect_action > 0 and inspect_action <= len(enemys):
                                print(enemy_name_color(enemys[inspect_action - 1].en_id) + enemys[inspect_action - 1].description)
                    else:
                        inspect_action = 1
                        print(enemy_name_color(enemys[0].en_id) + enemys[0].description)
                    print("Elements: ", end = "")
                    if len(enemys_elements[enemys[inspect_action - 1].en_id]):
                        element_count = 0
                        for i in enemys_elements[enemys[inspect_action - 1].en_id]:
                            if element_count > 0:
                                print(enemy_name_color(enemys[0].en_id)+ ", ", end = "")
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
                    print("\033[33;1mYou concentrate and attempt to remember yourself...\nYour balance is ", player_money, " coins\nYour experience is ", player_xp, "/", xp_to_lvl_up(), " XP\nYour level is ", player_level, sep = "")
                    if player_gold_boost > 0:
                        print("Your coin boost is ", player_gold_boost, "%", sep = "")
                    if player_crit_chance_reduction != 100:
                        print("Your crit. chance reduction is ", player_crit_chance_reduction, "%", sep = "")
                    if player_enemy_explotano > 0:
                        print("Enemies explode on death dealing ", player_enemy_explotano, "% of their HP", sep = "")
                    if player_consume > 0:
                        print("Your consume skill is at ", player_consume, "%", sep = "")
                    if player_extra_life > 0:
                        print("You have", player_extra_life + 1, "lives")
                    print("Your score is ", score, "\nYour power level is ", max_power_level, "\033[0m", sep = "")
                    print("\033[0m\nType anything to continue...")
                    action = input()
                elif (action == '5' or action.lower() == "broad hit"):
                    if len(enemys) > 1:
                        player_hit(-1)
                    elif len(enemys) == 1:
                        player_hit(0)
                    break
                elif action == '8' or "item" in action.lower():
                    if len(player_items) > 0:
                        counter = 0
                        for i in player_items:
                            counter += 1
                            print(str(counter) + ".", consumable_item_names[i])
                        print("\n1. Use\n2. Inspect")
                        while True:
                            action = input()
                            if action == '1' or action.lower() == "use":
                                print("Which item do you want to use?")
                                use_action = input()
                                if use_action.isdigit():
                                    use_action = int(use_action)
                                    if use_action > 0 and use_action <= len(player_items):
                                        item_use(player_items[use_action - 1])
                                break
                            elif action == '2' or action.lower() == "inspect":
                                print("Which one do you want to inspect?")
                                inspect_action = input()
                                if inspect_action.isdigit():
                                    inspect_action = int(inspect_action)
                                    if inspect_action > 0 and inspect_action <= len(player_items):
                                        print(consumable_item_desc[player_items[inspect_action-1]])
                                break
                    else:
                        print("You have no items!")
                    print("\033[0m\nType anything to continue...")
                    action = input()
                elif action == '9' or action.lower() == "do nothing":
                    print("\033[33;1mYou decided to do absolutely nothing for this turn!\033[0m")
                    break

        if player_regen > 0:
            regen = round((player_regen / 100) * player_max_hp)
            if regen + player_current_hp > player_max_hp:
                regen -= regen + player_current_hp - player_max_hp 
            player_current_hp += regen
            if regen > 0:
                print("\033[33;1mYou regenerated", regen, "HP! You have", player_current_hp, "HP left!\033[0m")
        
        if player_poisoned > 0:
            if player_poison_def >= player_poisoned:
                cur_poisoned = 1
            else:
                cur_poisoned = player_poisoned - player_poison_def
            player_current_hp -= cur_poisoned
            if player_current_hp < 0:
                player_current_hp = 0
            print("\033[33;1mPoison dealt", cur_poisoned, "DMG to you! You have", player_current_hp, "HP left!")

        for i in current_weather:
            if i == 6:
                def_decrease = round(player_base_def / 50) + 1
                player_extra_def -= def_decrease
                print("\033[33;1mYour defense has been decreased by ", def_decrease, "! Your current defense is ", player_base_def + player_extra_def, " DEF!\033[0m", sep = "")
            if i == 7:
                hp_decrease = round(player_max_hp / 100) + 1
                player_current_hp -= hp_decrease
                print("\033[33;1mHail dealt", hp_decrease, "DMG! You have", player_current_hp, "HP left!\033[0m")

        for i in range(len(allys)):
            if allys[i].hp <= 0:
                allys[i].hp += allys[i].max_hp // 10
                if allys[i].hp > 0:
                    allys[i].hp = allys[i].max_hp // 2
                else:
                    continue
            while allys[i].pattern[allys[i].pattern_action] == 3 and len(allys) > original_enemy_count * 1.25:
                allys[i].pattern_action += 1
                if allys[i].pattern_action >= len(allys[i].pattern):
                    allys[i].pattern_action = 0
            ally_actions[allys[i].pattern[allys[i].pattern_action]](i)
            allys[i].pattern_action += 1
            if allys[i].defense > (allys[i].original_defense + 1) * 1.25:
                while 1 in allys[i].pattern:
                    allys[i].pattern.remove(1)
            if allys[i].pattern_action >= len(allys[i].pattern):
                allys[i].pattern_action = 0
            if allys[i].psnd > 0:
                allys[i].hp -= allys[i].psnd
            allys[i].imm -= 1

        for i in range(len(enemys)):
            while enemys[i].pattern[enemys[i].pattern_action] == 3 and len(enemys) > original_enemy_count * 1.25:
                enemys[i].pattern_action += 1
                if enemys[i].pattern_action >= len(enemys[i].pattern):
                    enemys[i].pattern_action = 0
            if enemys[i].stnd > 0:
                enemy_actions[4]()
                enemys[i].stnd -= 1
            else:
                enemy_actions[enemys[i].pattern[enemys[i].pattern_action]](i)
            enemys[i].pattern_action += 1
            if enemys[i].defense > (enemys[i].original_defense + 1) * 1.25:
                while 1 in enemys[i].pattern:
                    enemys[i].pattern.remove(1)
            if enemys[i].pattern_action >= len(enemys[i].pattern):
                enemys[i].pattern_action = 0
            if enemys[i].psnd > 0:
                enemys[i].hp -= enemys[i].psnd
                if enemys[i].hp <= 0:
                    enemys[i].hp = 0
                print(enemy_name_color(enemys[i].en_id) + enemys[i].name, "suffered", enemys[i].psnd, "DMG from poison! They have", enemys[i].hp, "HP left!\033[0m")
            if enemys[i].hp <= 0:
                enemy_deletions.append(enemys[i])
            enemys[i].imm -= 1
        for i in enemy_deletions:
            if i.spawner[0] == 1:
                spawn = 0
                for k in i.spawner:
                    spawn += 1
                    if spawn > 1:
                        enemys.append(Enemies(enemy_id = k, summoned = True, summoner_id = enemys.index(i)))
            money_gain += i.money
            xp_gain += i.xp
            if not i.en_id in enemy_unconsumable:
                player_max_hp += round((player_consume / 100) * i.max_hp)
                player_base_dmg += round((player_consume / 100) * i.dmg)
                player_base_def += round((player_consume / 100) * i.original_defense)
                player_crit_chance += round(player_consume * i.crit)
            if player_enemy_explotano > 0:
                exploding_damage = round((player_enemy_explotano / 100) * i.max_hp)
                if len(enemys) - len(enemy_deletions) > 0:
                    exploding_damage //= len(enemys) - len(enemy_deletions)
                else:
                    exploding_damage = 0
                for k in enemys:
                    if not k in enemy_deletions:
                        k.hp -= exploding_damage
                        if k.hp <= 0:
                            enemy_deletions.append(k)
                if exploding_damage > 0:
                    print(i.name, "exploded and dealt", exploding_damage, "to other enemies.")
            enemys.remove(i)
        player_current_immortality -= 1
        enemy_deletions = []
        if player_current_hp == 0:
            if is_boss_battle == False or player_extra_life == 0:
                lost = 1
                break
            else:
                player_current_hp = player_max_hp
                player_extra_life -= 1
                player_spent_life += 1
                print("\033[31;3mYou lost one of your lives. But you refuse to die...\033[0m\n\n\n")
        if len(enemys) == 0:
            win = 1
            break
    if lost == 1:
        print("You have lost!\n\n\n")
    elif win == 1:
        money_gain = round(money_gain * (1 + (player_gold_boost / 100)))
        player_money += money_gain
        player_xp += xp_gain
        is_boss_battle = False
        print("You have won! You have earned \033[38;2;200;200;0m", money_gain, " coins!\033[0m Your balance is \033[38;2;200;200;0m", player_money, " coins!\033[0m You have collected \033[38;2;100;0;200m", xp_gain, " XP!\033[0m Your total experience is \033[38;2;100;0;200m", player_xp, "/", xp_to_lvl_up(), "XP!\033[0m\n\n\n", sep = "")
    else:
        print("You have encountered a bug! Notify developer!")
        print("Type anything to continue...")
        action = input()

def immortality_compute():
    global player_immortality
    global player_current_immortality
    if player_immortality > 0:
        return player_current_immortality / player_immortality
    else:
        return 0

def player_hit(target = 0):
    global player_base_dmg
    global player_crit_chance
    global player_poison
    global player_current_hp
    global player_max_hp
    global player_damage_range_boost
    global player_crit_chance_reduction
    global player_lifesteal
    global player_base_def
    global enemys
    global money_gain
    global xp_gain
    global player_weapon
    global player_damage_buff
    global player_crit_chance_buff

    enemys_deletion = []
    print("\033[33;1m", end = "")
    if target > -1: # Regular Hit
        dealt_damage = round(player_base_dmg * (randint(weapon_damage_ranges[player_weapon][0] + player_damage_range_boost, weapon_damage_ranges[player_weapon][1] + player_damage_range_boost) / 100) * ((player_damage_buff / 100) + 1))
        cur_crit_chance = player_crit_chance * ((player_crit_chance_buff / 100) + 1)
        crit_count = 0
        while cur_crit_chance > 0:
            if chance(cur_crit_chance / 100):
                dealt_damage *= 2
                crit_count += 1
            cur_crit_chance -= player_crit_chance_reduction
        if enemys[target].defense < dealt_damage:
            dealt_damage -= enemys[target].defense
        else:
            dealt_damage = 1
        if enemys[target].imm > 0:
            dealt_damage = 0
        enemys[target].hp -= dealt_damage
        spike_damage = enemys[target].spk
        if player_lifesteal > 0:
            heal = round(dealt_damage * player_lifesteal / 100)
            if heal + player_current_hp > player_max_hp:
                heal -= heal + player_current_hp - player_max_hp
            player_current_hp += heal
            print("You have healed for", heal, "HP! You have", player_current_hp, "HP left!")
        player_current_hp -= spike_damage
        if player_current_hp < 0:
            player_current_hp = 0
        if enemys[target].hp > 0:
            print("You hit", enemys[target].name, "for", dealt_damage, "DMG! They have", enemys[target].hp, "HP left!")
            if spike_damage > 0:
                print(enemys[target].name, "'s spikes dealt ", spike_damage, " DMG to you! You have ", player_current_hp, " HP left!", sep = "")
            if player_poison > 0:
                dealt_poison = round(player_poison * weapon_poison_factor[player_weapon])
            else:
                dealt_poison = 0
            if dealt_poison > 0:
                enemys[target].psnd += dealt_poison
                print("You have inflicted ", dealt_poison, " PSN to ", enemys[target].name, "! Their total poison is ", enemys[target].psnd, " PSN!", sep = "")
        else:
            print("You hit", enemys[target].name, "for", dealt_damage, "DMG! You killed them!")
            if spike_damage > 0:
                print(enemys[target].name, "'s spikes dealt ", spike_damage, " DMG to you! You have ", player_current_hp, " HP left!", sep = "")
            if enemys[target].spawner[0] == 1:
                spawn = 0
                for i in enemys[target].spawner:
                    spawn += 1
                    if spawn > 1:
                        enemys.append(Enemies(enemy_id = i, summoned = True, summoner_id = target))
            money_gain += enemys[target].money
            xp_gain += enemys[target].xp
            if not enemys[target].en_id in enemy_unconsumable:
                player_max_hp += round((player_consume / 100) * enemys[target].max_hp)
                player_base_dmg += round((player_consume / 100) * enemys[target].dmg)
                player_base_def += round((player_consume / 100) * enemys[target].defense)
                player_crit_chance += round(player_consume * enemys[target].crit)
            if player_enemy_explotano > 0:
                exploding_damage = round((player_enemy_explotano / 100) * enemys[target].max_hp)
                if len(enemys) - 1 != 0:
                    exploding_damage //= len(enemys) - 1
                else:
                    exploding_damage = 0
                for k in enemys:
                    if not k == enemys[target]:
                        k.hp -= exploding_damage
                        if k.hp <= 0:
                            enemys_deletion.append(k)
                if exploding_damage > 0:
                    print(enemys[target].name, "exploded and dealt", exploding_damage, "to other enemies.")
            enemys.remove(enemys[target])

    else: # Broad Hit
        dealt_damage = round(player_base_dmg * ((weapon_damage_ranges[player_weapon][1] + player_damage_range_boost)  / 100) * ((player_damage_buff / 100) + 1) * weapon_crowd_factor[player_weapon])
        cur_crit_chance = player_crit_chance * ((player_crit_chance_buff / 100) + 1)
        crit_count = 0
        while cur_crit_chance > 0:
            if chance(cur_crit_chance / 100):
                dealt_damage *= 2
                crit_count += 1
            cur_crit_chance -= player_crit_chance_reduction
        dealt_damage = round(dealt_damage / len(enemys))
        print("You dealt", end = "")
        jank_code_counter = 0
        enemys_deletion = []
        spike_damage = 0
        for i in enemys:
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
        player_current_hp -= spike_damage
        if spike_damage > 0:
            print("Some of the enemies you've hit had spikes and dealt", spike_damage, "DMG to you! You have", player_current_hp, "HP left!")
        if player_poison > 0:
            print("Your hit was too inaccurate to inflict poison!")
    for i in enemys_deletion:
        enemy_id = enemys.index(i)
        if i.spawner[0] == 1:
            spawn = 0
            for k in i.spawner:
                spawn += 1
                if spawn > 1:
                    enemys.append(Enemies(enemy_id = k,summoned = True, summoner_id = enemy_id))
        money_gain += i.money
        xp_gain += i.xp
        if not i.en_id in enemy_unconsumable:
            player_max_hp += round((player_consume / 100) * i.max_hp)
            player_base_dmg += round((player_consume / 100) * i.dmg)
            player_base_def += round((player_consume / 100) * i.original_defense)
            player_crit_chance += round(player_consume * i.crit)
        if player_enemy_explotano > 0:
            exploding_damage = round((player_enemy_explotano / 100) * i.max_hp)
            if len(enemys) - len(enemys_deletion) > 0:
                exploding_damage //= len(enemys) - len(enemys_deletion)
            else:
                exploding_damage = 0
            for k in enemys:
                if not k in enemys_deletion:
                    k.hp -= exploding_damage
                    if k.hp <= 0:
                        enemys_deletion.append(k)
            if exploding_damage > 0:
                print(i.name, "exploded and dealt", exploding_damage, "to other enemies.")
        enemys.remove(i)

    if crit_count == 1:
        print("It was a critical hit!")
    elif crit_count > 1:
        print("You rolled a critical hit", crit_count, "times!")

    print("\033[0m", end = "")

def item_use(item):
    global player_max_hp
    global player_current_hp
    global player_extra_def
    global player_poisoned
    global enemys
    global player_damage_buff
    global player_crit_chance_buff
    print("\033[33;1m", end = "")
    original_item = item
    while item == 3:
        item = randint(0, len(consumable_item_names) - 1)
    if item == 0:
        print("This did absolutely nothing!")
    elif item == 1:
        heal = round(0.2 * player_max_hp)
        if heal + player_current_hp > player_max_hp:
            heal = player_max_hp - player_current_hp
        extra_def = round(0.2 * player_base_def)
        player_extra_def += extra_def
        player_current_hp += heal
        print("You ate a cookie. You regenerated", heal, "HP and gained", extra_def, "defense!")
    elif item == 2:
        player_poisoned = 0
        print("You injected antidote. Your PSN'd decreased to 0!")
    elif item == 4:
        heal = round(0.5 * player_max_hp)
        if heal + player_current_hp > player_max_hp:
            heal = player_max_hp - player_current_hp
        player_current_hp += heal
        print("You ate cooked meat. You regenerated", heal, "HP!")
    elif item == 5:
        heal = round(0.05 * player_max_hp)
        if heal + player_current_hp > player_max_hp:
            heal = player_max_hp - player_current_hp
        for i in enemys:
            if i.en_id in [15, 16, 17, 18, 19, 36, 39, 46, 52, 60]:
                player_damage_buff += 20
        player_current_hp += heal
        print("You drank winter tea. You regenerated ", heal, " HP and your damage is increased by ", player_damage_buff, "%!", sep = "")
    elif item == 6:
        player_current_hp = player_max_hp
        print("You drank a heal potion. You regenerated all of your HP!")
    elif item == 7:
        player_damage_buff += 30
        player_crit_chance_buff += 100
        print("You drank a berserk's potion. Your damage is increased by ", player_damage_buff, "% and your crit chance is increased by ", player_crit_chance_buff, "%!", sep = "")
    elif item == 8:
        for i in range(len(enemys)):
            enemys[i].stnd += 3
        print("You threw stun potion at the enemies, you stunned them for 3 turns!")
    if original_item in player_items:
        player_items.remove(original_item)
    print("\033[0m", end = "")

def chance(num = 0):
    if random() <= num:
        return True
    else:
        return False

def fight_choose(extra_power_level = 0):
    global area_id
    global max_power_level
    global game_time
    global current_weather
    global overkill
    global eclipse
    global enemy_encouter_seed

    seed(enemy_encouter_seed)
    enemy_encouter_seed = randint(0, 10000)
    possible_enemies = []
    enemies = []

    if eclipse:
        game_time_bonus = 0.24
    elif game_time < 12:
        game_time_bonus = 0
    elif game_time < 18:
        game_time_bonus = round(game_time / 100, 2)
    elif game_time < 22:
        game_time_bonus = round(game_time / 90, 2)
    else:
        game_time_bonus = round(0.23 - round(game_time / 100, 2), 2)
    cur_max_power_level = max_power_level + game_time_bonus + extra_power_level

    for i in range(len(enemys_name)):
        if (enemy_is_boss[i] == False and area_id in enemy_areas[i]) or ("drought" in enemy_areas[i] and 9 in current_weather):
            if i in [35, 36, 37]:
                if hunters_appeared[i - 35] == False:
                    possible_enemies.append(i)
            else:
                possible_enemies.append(i)

    if overkill == False:
        while len(possible_enemies) > 0:
            i = choice(possible_enemies)
            if cur_max_power_level - enemys_power_level[i] < 0:
                while i in possible_enemies:
                    possible_enemies.remove(i)
            else:
                if i == 35 or i == 36 or i == 37:
                    while i in possible_enemies:
                        possible_enemies.remove(i)
                    hunters_appeared[i - 35] = True
                enemies.append(i)
                cur_max_power_level -= enemys_power_level[i]
    else:
        while cur_max_power_level > 0:
            i = choice(possible_enemies)
            if i == 35 or i == 36 or i == 37:
                while i in possible_enemies:
                    possible_enemies.remove(i)
                hunters_appeared[i - 35] = True
            enemies.append(i)
            cur_max_power_level -= enemys_power_level[i]
    if len(enemies) == 0:
        enemies.append(4)
    spirits_for_fight_choose(enemies)
    return enemies

def bossfight_choose():
    global area_id
    global max_power_level
    global last_boss
    global game_mode
    global final_area
    global change_recruited
    global death_defeated
    global is_boss_battle
    is_boss_battle = True
    if game_mode == "story" and final_area == True:
        if change_recruited == False and death_defeated == False:
            enemies = [52]
            print('''\033[38;2;100;200;250m"My child, it is time to prove yourself worthy. Prove it to your sibling."\033[0m''')
        elif change_recruited == True and death_defeated == False:
            enemies = [52, 54]
            print('''\033[38;2;100;200;250m"My child, it is time... Who is that person behind you?"\033[0m
The weird man from before approaches you and starts to speak to the glass ceiling of the Garden,
\033[38;2;100;100;175m"You know who I am, Cycle. Your child and I decided to put a stop to this madness. So come out and fight us!"\033[0m
A familiar figure appears in front of you two.
\033[38;2;100;200;250m"I am sorry, my child,"\033[0m it says.''')
        elif change_recruited == False and death_defeated == True:
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
        print('''Type anything to continue...''')
        action = input()
    else:
        cur_max_power_level = max_power_level
        enemies = []
        possible_enemies = []

        for i in range(len(enemys_name)):
            if enemy_is_boss[i] == True and ((area_id in enemy_areas[i]) or ("drought" in enemy_areas[i] and 9 in current_weather)):
                possible_enemies.append(i)
    
        if overkill == False:
            while len(possible_enemies) > 0:
                i = choice(possible_enemies)
                if cur_max_power_level - enemys_power_level[i] < 0:
                    while i in possible_enemies:
                        possible_enemies.remove(i)
                else:
                    enemies.append(i)
                    cur_max_power_level -= enemys_power_level[i]
        else:
            while cur_max_power_level > 0:
                i = choice(possible_enemies)
                enemies.append(i)
                cur_max_power_level -= enemys_power_level[i]
        if len(enemies) == 0:
            enemies.append(4)
        spirits_for_fight_choose(enemies)
    last_boss = enemies.copy()
    return enemies

def ally_choose():
    global game_mode
    global final_area
    global change_recruited
    global death_defeated
    allies = []
    if game_mode == "story":
        if final_area == True:
            if change_recruited == True:
                allies.append(53)
            if death_defeated == True:
                allies.append(51)
    return allies

def spirits_for_fight_choose(enemies = []):
    global vitality_anger
    global strength_anger
    global might_anger
    global protection_anger
    global shopkeeper_deaths
    global fear_anger
    global spirit_anger_reduction
    if vitality_anger - spirit_anger_reduction > 0:
        enemies.append(38)
    if strength_anger - spirit_anger_reduction > 0:
        enemies.append(39)
    if protection_anger - spirit_anger_reduction > 0:
        enemies.append(41)
    if might_anger - spirit_anger_reduction > 0:
        enemies.append(40)
    if fear_anger - spirit_anger_reduction > 0:
        enemies.append(4)
    if chance(shopkeeper_deaths * 0.25 - spirit_anger_reduction):
        enemies.append(34)
    return enemies

def stats_altar():
    global player_max_hp, player_base_dmg, player_base_def, player_base_magic_def, player_crit_chance, max_power_level, last_altar, altar_seed
    print("You came across an altar.")
    random_dialogue = randint(1, 3)
    if random_dialogue == 1:
        print("You heard voices promising powerful gifts.")
    elif random_dialogue == 2:
        print("You see three stones, with glyphs on them, lying here.")
    elif random_dialogue == 3:
        print("You feel essence of power coursing through you.")
    print("Choose one gift:")

    seed(altar_seed)
    altar_seed = randint(0, 10000)

    while True:
        possible_upgrades = ["\033[38;2;0;255;0mVitality", "\033[38;2;255;0;0mStrength", "\033[38;2;255;128;0mMight", "\033[38;2;0;200;255mProtection", "\033[38;2;190;0;205mInnocence", "\033[38;2;0;255;255mMagic Protection"]
        item1 = choice(possible_upgrades)
        possible_upgrades.remove(item1)
        item2 = choice(possible_upgrades)
        possible_upgrades.remove(item2)
        item3 = choice(possible_upgrades)
        possible_upgrades.remove(item3)
        if not (item1 in last_altar and item2 in last_altar and item3 in last_altar):
            break
    current_upgrades = [item1, item2, item3]
    last_altar = current_upgrades.copy()
    print("1.", item1, "\033[0m\n2.", item2, "\033[0m\n3.", item3, "\033[0m\n4. Self Inspect")
    while True:
        print("Type in the number of upgrade")
        action = input()
        if action == "1":
            altar_grant(item1)
            break
        elif action == "2":
            altar_grant(item2)
            break
        elif action == "3":
            altar_grant(item3)
            break
        elif action == "4" or "insepct" in action.lower() or "self" in action.lower():
            print("\033[38;2;0;255;0mMax HP -", player_max_hp, "\033[38;2;255;0;0m\nBase DMG -", player_base_dmg, "\033[38;2;0;200;255m\nBase DEF -", player_base_def, "\033[38;2;0;255;255m\nBase MGCDEF -", player_base_magic_def, "\033[38;2;255;128;0m\nCrit chance -", player_crit_chance, "\033[38;2;190;0;205m\nPower level -", max_power_level, "\033[0m")
        elif (action.lower() == "vitality" or action.lower() == "life") and "\033[38;2;0;255;0mVitality" in current_upgrades:
            altar_grant("\033[38;2;0;255;0mVitality")
            break
        elif action.lower() == "strength" and "\033[38;2;255;0;0mStrength" in current_upgrades:
            altar_grant("\033[38;2;255;0;0mStrength")
            break
        elif action.lower() == "might" and "\033[38;2;255;128;0mMight" in current_upgrades:
            altar_grant("\033[38;2;255;128;0mMight")
            break
        elif action.lower() == "protection" and "\033[38;2;0;200;255mProtection" in current_upgrades:
            altar_grant("\033[38;2;0;200;255mProtection")
            break
        elif (action.lower() == "innocence" or action.lower() == "fear") and "\033[38;2;190;0;205mInnocence" in current_upgrades:
            altar_grant("\033[38;2;190;0;205mInnocence")
            break
        elif action.lower() == "magic protection" and "\033[38;2;0;255;255mMagic Protection" in current_upgrades:
            altar_grant("\033[38;2;0;255;255mMagic Protection")
            break
    print("\n\n\n")

def altar_grant(item):
    global player_max_hp
    global player_base_dmg
    global player_base_def
    global player_crit_chance
    global max_power_level
    global player_base_magic_def

    if item == "\033[38;2;0;255;0mVitality":
        player_max_hp = round(player_max_hp * 1.15)
        print("\033[38;2;0;255;0mYour max health is now", player_max_hp, "HP!")
    elif item == "\033[38;2;255;0;0mStrength":
        if player_base_dmg < 20:
            player_base_dmg = round(player_base_dmg * 1.2)
        else:
            player_base_dmg = round(player_base_dmg * 1.15)
        print("\033[38;2;255;0;0mYour damage is now", player_base_dmg, "DMG!")
    elif item == "\033[38;2;255;128;0mMight":
        if player_crit_chance > 300:
            player_crit_chance += 1
        elif player_crit_chance > 100:
            player_crit_chance += 2
        else:
            player_crit_chance += 5
        print("\033[38;2;255;128;0mYour chance to get critical hit is now ", player_crit_chance, "%!", sep = "")
    elif item == "\033[38;2;0;200;255mProtection":
        def_multiplier = (player_base_def / 60) + 1
        player_base_def = round(player_base_def + def_multiplier * 3)
        print("\033[38;2;0;200;255mYour defense is now", player_base_def, "DEF!")
    elif item == "\033[38;2;190;0;205mInnocence":
        max_power_level -= round(max_power_level * 0.1, 2)
        print("\033[38;2;190;0;205mLess enemies will consider you a threat.")
    elif item == "\033[38;2;0;255;255mMagic Protection":
        def_multiplier = (player_base_magic_def / 50) + 1
        player_base_magic_def = round(player_base_magic_def + def_multiplier * 3)
        print("\033[38;2;0;255;255mYour magic defense is now", player_base_magic_def, "DEF!")
    print("\033[0m", end = "")

    # Spirit anger management
    global vitality_anger
    global strength_anger
    global might_anger
    global protection_anger
    global fear_anger
    global max_power_level_increase
    if estimate_max_hp() < player_max_hp:
        vitality_anger = player_max_hp // estimate_max_hp()
    else:
        vitality_anger = 0
        
    if estimate_dmg() < player_base_dmg:
        strength_anger = player_base_dmg // estimate_max_hp()
    else:
        strength_anger = 0

    if player_crit_chance > 205:
        might_anger = player_crit_chance // 205
    else:
        might_anger = 0

    if estimate_def() < player_base_def + player_base_magic_def:
        protection_anger = (player_base_def + player_base_magic_def) // estimate_def()
    else:
        protection_anger = 0

    estimate_power_level = 1
    for i in range(max_power_level_increase):
        estimate_power_level = round(estimate_power_level * 1.0175, 2)
    if max_power_level < estimate_power_level * 0.1:
        fear_anger = round((estimate_power_level * 0.1) / max_power_level)
    else:
        fear_anger = 0

def estimate_max_hp():
    global score
    global score_increase
    global difficulty
    hp = 100
    for i in range(score + int(score_increase) + 10):
        hp += 300 - difficulty
        hp = hp
    return hp

def estimate_dmg():
    global score
    global score_increase
    global difficulty
    dmg = 5
    for i in range(score + int(score_increase) + 10):
        dmg += 80 - difficulty
        dmg = int(dmg)
    return dmg

def estimate_def():
    global score
    global score_increase
    global difficulty
    defense = 0
    for i in range(score + int(score_increase) + 10):
        defense += 77 - difficulty
        defense = int(defense)
    return defense

def xp_to_lvl_up():
    global player_level
    xp = 10
    for i in range(player_level):
        xp += xp // 2
    return xp

def level_up():
    global player_level
    global player_xp
    global player_max_hp
    global player_base_dmg
    global player_base_def
    global player_base_magic_def
    global player_crit_chance
    i = 0
    while player_xp >= xp_to_lvl_up():
        player_xp -= xp_to_lvl_up()
        player_level += 1
        i += 1
    if i > 0:
        print("You leveled up! Your level is ", player_level, "!", sep = "")
        for k in range(i):
            player_max_hp += player_max_hp // 10 + 1
            player_base_dmg += player_base_dmg // 20 + 1
            player_base_def += player_base_def // 10 + 1
            player_base_magic_def += player_base_magic_def // 10 + 1
            if player_crit_chance < 100:
                player_crit_chance += player_crit_chance // 20 + 1
            else:
                player_crit_chance += 1
        print("A lot of your base stats have been increased!\n\n\n")

def shop_items_define():
    global current_shop_items
    global current_alchemist_items
    global is_weapon_bought
    global shop_weapon
    global leave
    global alchemist_visited
    global alchemist_anger
    global bought_from_alchemist
    global item_rando
    global shop_seed
    seed(shop_seed)
    shop_seed = randint(0, 10000)
    if item_rando:
        possible_shop_items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        possible_alchemist_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    else:
        possible_shop_items = [1, 2, 4, 8, 11, 12, 13, 14, 15, 16]
        possible_alchemist_items = [13, 15, 17, 18, 19]
    current_shop_items = []
    current_alchemist_items = []
    possible_weapons = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    while player_weapon in possible_weapons:
        possible_weapons.remove(player_weapon)
    is_weapon_bought = 0
    for i in range(3):
        item = choice(possible_shop_items)
        possible_shop_items.remove(item)
        current_shop_items.append(item)
        item = choice(possible_alchemist_items)
        possible_alchemist_items.remove(item)
        current_alchemist_items.append(item)
    shop_weapon = choice(possible_weapons)
    leave = 0
    #print(bought_from_alchemist, alchemist_visited)
    if bought_from_alchemist == False and alchemist_visited:
        alchemist_anger += 0.4
    else:
        alchemist_anger -= 0.5
        if alchemist_anger < 0:
            alchemist_anger = 0
    #print(alchemist_anger)

def peaceful_shop():
    global player_money
    global leave
    global current_shop_items
    global shopkeeper_deaths
    global player_weapon
    global is_weapon_bought
    global shop_weapon
    if shopkeeper_deaths == 0:
        print('''You came across a shop. \033[38;2;100;220;100mThe shopkeeper\033[0m warmly welcomes you,
\033[38;2;100;220;100m"Ah. Customer. Welcome. Take a look at these items!"\033[0m''')
    elif shopkeeper_deaths == 1:
        print('''You came across a shop. \033[38;2;100;220;100mThe shopkeeper\033[0m welcomes you,
\033[38;2;100;220;100m"Oh. Customer, welcome! These are items that my cousin gave me as a gift. I wonder what happened to him..."\033[0m''')
    elif shopkeeper_deaths == 2:
        print('''You came across a shop. \033[38;2;100;220;100mThe shopkeeper\033[0m welcomes you,
\033[38;2;100;220;100m"Hello. My name is Zach. My cousins Mach and Lach left some items for me to sell. They were damaged by someone. I mean the items."\033[0m''')
    elif shopkeeper_deaths == 3:
        print('''You came across a shop. \033[38;2;100;220;100mThe shopkeeper\033[0m welcomes you,
\033[38;2;100;220;100m"Hello, there. Here are some items that, I found myself. Zach didn't gift me anything! Err... I meant to say... Do you want anything?"\033[0m''')
    else:
        print('''You came across a shop. Another \033[38;2;100;220;100mshopkeeper\033[0m welcomed you,
\033[38;2;100;220;100m"Ah. Hello. Welcome to my shop. There have been quite a few changes over the last few days. As if someone started genocide. Genocide of Shopkeepers"\033[0m''')
    leave = 0
    while True:
        counter = 0
        print("Your balance is\033[38;2;200;200;0m", player_money, "coins\033[0m")
        for i in current_shop_items:
            counter += 1
            print(counter, ". ", item_names[i], " - \033[38;2;200;200;0m", cost(i), " coins\033[0m", sep = "")
        if is_weapon_bought == 0:
            counter += 1
            print(counter, ". ", weapon_names[shop_weapon], " - \033[38;2;200;200;0m", cost(shop_weapon, 1), " coins\033[0m", sep="")
        counter += 1
        print(counter, ". Inspect", sep = "")
        print(counter + 1, ". Leave", sep = "")
        while True:
            print("Which one do you want to buy?")
            action = input()
            if action.isdigit():
                action = int(action)
                if action > 0 and action <= len(current_shop_items):
                    shop_buy(action - 1, "shop")
                    break
                elif action - 1 == len(current_shop_items) and is_weapon_bought == 0:
                    shop_weapon_buy(shop_weapon)
                    break
                elif (action - 2 == len(current_shop_items) and is_weapon_bought == 0) or (action - 1 == len(current_shop_items) and is_weapon_bought == 1):
                    item_info(shop_weapon, "shop")
                    break
                elif (action - 3 == len(current_shop_items) and is_weapon_bought == 0) or (is_weapon_bought == 1 and action - 2 == len(current_shop_items)):
                    leave = 1
                    break
            else:
                print("Type in the correct action")
        if leave == 1:
            break
    print("You left the shop and continued your journey...\n\n\n")

def cost(item, type = 0):
    global score
    if type == 0:
        cost = item_base_costs[item]
        for i in range(score + (item_bought[item] * 3)):
            if cost < 170000000000000000000000:
                cost *= 1.05
                cost = round(cost)
            else:
                cost += cost // 10000000000000
    elif type == 1:
        cost = weapon_base_costs[item]
        for i in range(score):
            if cost < 170000000000000000000000:
                cost *= 1.05
                cost = round(cost)
            else:
                cost += cost // 10000000000000
    return cost

def item_info(weapon, shop_type = "shop"):
    global item_descriptions
    global is_weapon_bought
    print("Which item is the confusing one?")
    if shop_type == "shop":
        counter = 0
        for i in current_shop_items:
            counter += 1
            print(counter, ". ", item_names[i], sep = "")
        if is_weapon_bought == 0:
            counter += 1
            print(counter, ". ", weapon_names[weapon], sep="")
        action = input()
        if action.isdigit():
            action = int(action)
            if action > 0 and action <= len(current_shop_items):
                print(item_descriptions[current_shop_items[action - 1]])
            elif action - 1 == len(current_shop_items) and is_weapon_bought == 0:
                print(weapon_descriptions[weapon])
    elif shop_type == "alchemist":
        counter = 0
        for i in current_alchemist_items:
            counter += 1
            print(counter, ". ", item_names[i], sep = "")
        action = input()
        if action.isdigit():
            action = int(action)
            if action > 0 and action <= len(current_alchemist_items):
                print(item_descriptions[current_alchemist_items[action - 1]])

def shop_buy(item, shop_type = "shop"):
    global player_money
    global leave
    global items
    global shopkeeper_sus
    global debt
    global bought_from_alchemist
    if shop_type == "shop":
        item_id = current_shop_items[item]
        if player_money >= cost(item_id):
            player_money -= cost(item_id)
            shop_grant(item_id)
            item_bought[item_id] += 1
            current_shop_items[item] = 0
            shopkeeper_sus -= 0.05
            if shopkeeper_sus <= 0:
                shopkeeper_sus = 0
                debt = 0
        else:
            print('''You don't have enough money to buy this item!
But you could try stealing it...
What will you do?
1. Steal
2. Not Steal''')
            action = input()
            if action == "1":
                print("You stole", item_names[item_id])
                debt += cost(item_id)
                shop_grant(item_id)
                current_shop_items[item] = 0
                shopkeeper_sus += 0.125
                leave = 1
            elif action == "2":
                print("You put the item back down and continued shopping...")
    elif shop_type == "alchemist":
        item_id = current_alchemist_items[item]
        if player_money >= cost(item_id):
            bought_from_alchemist = True
            player_money -= cost(item_id)
            shop_grant(item_id)
            item_bought[item_id] += 1
            current_alchemist_items[item] = 0
        else:
            print('''You don't have enough money to buy this item!''')

def shop_weapon_buy(weapon):
    global player_money
    global player_extra_magic_def_buff
    global player_weapon
    global leave
    global debt
    global shopkeeper_sus
    global is_weapon_bought
    if cost(weapon, 1) <= player_money:
        player_money -= cost(weapon, 1)
        player_weapon = weapon
        if weapon == 1:
            player_extra_magic_def_buff = 1.5
        else:
            player_extra_magic_def_buff = 0
        is_weapon_bought = 1
        print("You bought", weapon_names[weapon])
    else:
        print('''You don't have enough money to buy this item!
But you could try stealing it...
What will you do?
1. Steal
2. Not Steal''')
        action = input()
        if action == "1":
            print("You stole", weapon_names[weapon])
            debt += cost(weapon, 1)
            player_weapon = weapon
            if weapon == 1:
                player_extra_magic_def_buff = 1.5
            else:
                player_extra_magic_def_buff = 0
            shopkeeper_sus += 0.5
            leave = 1
            is_weapon_bought = 1
        elif action == "2":
            print("You put the item back down and continued shopping...")

def shop_grant(item):
    global player_poison
    global player_spikes
    global player_lifesteal
    global player_gold_boost
    global shopkeeper_sus
    global player_immortality
    global player_regen
    global player_consume
    global player_travel
    global player_enemy_explotano
    global player_extra_life
    global player_dodge_chance
    global player_items
    if item == 0:
        print("You bought nothing! Good job")
    elif item == 1:
        psn_addition = round(1 * ((player_poison / 5) + 1))
        player_poison += psn_addition
        print("You poured poison onto your weapon, adding", psn_addition, "PSN to it. Total poison that your sword will inflict is now", player_poison, "PSN!")
    elif item == 2:
        spk_addition = round(1 * ((player_spikes / 2) + 1))
        player_spikes += spk_addition
        print("You attached the spikes to your armor, adding", spk_addition, "SPK to it. Enemies will get hit for", player_spikes, "DMG when hit you.")
    elif item == 3:
        if player_lifesteal < 99:
            player_lifesteal += round(25 * (100 - player_lifesteal) / 100)
        else:
            player_lifesteal += 1
        print("You consumed the essence of lifesteal. Your total lifesteal is ", player_lifesteal, "% now.", sep = "")
    elif item == 4:
        player_gold_boost += 10
        shopkeeper_sus -= 0.1
        if shopkeeper_sus < 0:
            shopkeeper_sus = 0
        print("You consumed the part of Midas' power. Your money boost is ", player_gold_boost, "% now.", sep = "")
    elif item == 5:
        player_immortality += 1
        print("You feel impenetrability, coursing through your body. Your total impenetrability is", player_immortality)
    elif item == 6:
        if player_regen < 24:
            player_regen += 4
            print("You feel marked by some curse. Your total regeneration is ", player_regen, "%!", sep = "")
        elif player_regen < 35:
            player_regen += 1
            print("You feel marked by some curse. Your total regeneration is ", player_regen, "%!", sep = "")
        else:
            player_lifesteal += 4
            print("Despite consuming mark of the undead, you feel the essence of lifesteal. Your total lifesteal is ", player_lifesteal, "% now.", sep = "")
    elif item == 7:
        if player_consume < 7:
            player_consume += 1
            print("You consume consume. You will absorb ", player_consume, "% of enemies' stats on kill", sep = "")
        else:
            player_gold_boost += 20
            print("Despite consuimg consume, you feel as if you are becoming richer. Your money boost is ", player_gold_boost, "% now.", sep = "")
    elif item == 8:
        if player_travel < 90:
            player_travel += round(30 * (100 - player_travel) / 100)
        else:
            player_travel += 1
        print("You feel strength in your legs. Total experience gained for entering new area is ", player_travel, "%", sep = "")
    elif item == 9:
        if player_enemy_explotano > 50:
            player_enemy_explotano += 3
        else:
            player_enemy_explotano += 10
        print("Your weapon gets enchanted by exploding magic. Killed enemies will explode dealing ", player_enemy_explotano, "% of their HP to other enemies!", sep = "")
    elif item == 10:
        player_extra_life += 1
        print("You feel some floatyness in your stomach. You have", player_extra_life + 1, "lives!")
    elif item == 11:
        player_items.append(1)
        print("You got a cookie!")
    elif item == 12:
        player_items.append(2)
        print("You got an antidote!")
    elif item == 13:
        player_items.append(3)
        print("You got a gambler's drink!")
    elif item == 14:
        player_items.append(4)
        print("You got cooked meat!")
    elif item == 15:
        player_items.append(5)
        print("You got winter tea!")
    elif item == 16:
        if player_dodge_chance < 25:
            player_dodge_chance += 5
            print("You feel lighter. Your chance to dodge physical attacks is now ", player_dodge_chance, "%!", sep = "")
        else:
            player_immortality += 1
            print("Despite having additional band of agility, you feel impenetrability, coursing through you. Your total impenetrability is", player_immortality)
    elif item == 17:
        player_items.append(6)
        print("You got a heal potion!")
    elif item == 18:
        player_items.append(7)
        print("You got a berserk's potion!")
    elif item == 19:
        player_items.append(8)
        print("You got a stun potion!")

def shop():
    global shopkeeper_sus
    global debt
    global player_money
    global lost
    global shopkeeper_deaths
    global cur_shopkeeper_dead
    global eclipse
    if game_time < 18 and eclipse == False:
        if chance(shopkeeper_sus) == False:
            peaceful_shop()
        else:
            print('''When you came across a shop, \033[38;2;100;220;100mthe familiar shopkeeper\033[0m grabbed you by the wrist and said,
\033[38;2;100;220;100m"You are the thief. I know it. It's time for you to pay."\033[0m
You owe \033[38;2;100;220;100mthe shopkeeper\033[38;2;200;200;0m''', debt, '''coins.\033[0m Will you play it back?
Your balance is\033[38;2;200;200;0m''', player_money,'''coins\033[0m
1. Pay
2. Refuse''')
            while True:
                print("Type in the action")
                action = input()
                if action == "1" and player_money >= debt:
                    player_money -= debt
                    print("You paid \033[38;2;100;220;100mthe shopkeeper\033[38;2;200;200;0m", debt, "coins.\033[0m Your balance is now\033[38;2;200;200;0m", player_money, '''coins.
\033[38;2;100;220;100m"Alright. Come back later. My shop isn't ready yet,"\033[0m he said and let you go.
You continued on your journey...\n\n\n''')
                    break
                elif action == "2" and player_money < debt:
                    print('''\033[38;2;100;220;100m"Oh. So you are poor? I will get products from you, then."''')
                    fight([33])
                    if lost == 1:
                        reset_player()
                        lost = 0
                    else:
                        print("With guilt overwhelming you, you step over \033[38;2;100;220;100mthe shopkeeper\033[0m's body, and continue your journey...\n\n\n")
                        shopkeeper_deaths += 1
                        cur_shopkeeper_dead = True
                    break
                elif action == "2" and player_money >= debt:
                    print('''\033[38;2;100;220;100m"Greedy? I will take it away by force, then."\033[0m''')
                    fight([33])
                    if lost == 1:
                        reset_player()
                        lost = 0
                    else:
                        print("With guilt overwhelming you, you step over \033[38;2;100;220;100mthe shopkeeper\033[0m's body, and continue your journey...\n\n\n")
                        shopkeeper_deaths += 1
                        cur_shopkeeper_dead = True
                    break
            shopkeeper_sus = 0
    elif eclipse:
        print('''When you came across the shop, it was locked. The sign at the entrance said,
\033[38;2;100;220;100m"Please, come back after the eclipse!"\033[0m You decided to continue your jorney...\n\n\n''')
    else:
        print('''When you came across the shop, it was locked. The sign at the entrance said,
\033[38;2;100;220;100m"Please, come back in the morning!"\033[0m You decided to continue your jorney...\n\n\n''')

def alchemist_shop():
    global player_money
    global brewery_encouters
    global game_time
    global current_alchemist_items
    global alchemist_visited
    global alchemist_anger
    global alchemist_defeated
    global lost
    if not chance(alchemist_anger - 1):
        alchemist_visited = True
        if brewery_encouters == 0:
            print('''You came across a brewery. Inside, you were greeted by \033[38;2;200;0;150mthe alchemist\033[0m,
\033[38;2;200;0;150m"'ello, 'ello! Finally one arrifes to buy my kreat potions."\033[0m
He presents you the goods.''')
        else:
            if alchemist_anger <= 0.3:
                if game_time < 6:
                    print('''You came across a brewery. Half-sleeping \033[38;2;200;0;150malchemist\033[0m greets you,
\033[38;2;200;0;150m"Guten morgen. Neet any potionz?"\033[0m
He presents you the goods.''')
                elif game_time < 18:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"The zun is high, and I greet it. I meant, the zun is high, but my prices are low."\033[0m
He presents you the goods.''')
                else:
                    print('''You came across a brewery. Half-sleeping \033[38;2;200;0;150malchemist\033[0m greets you,
\033[38;2;200;0;150m"Quite late. Need a zleep potion?"\033[0m
He presents you the goods.''')
            elif alchemist_anger <= 0.6:
                if alchemist_defeated < 1:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I woult like to see you buy zomethink already."\033[0m''')
                else:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I have impenetrabalality potion. Which iz why I keep living."\033[0m''')
            elif alchemist_anger <= 1:
                if alchemist_defeated < 1:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"Buy zomethink."\033[0m''')
                else:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I have impenetrabalality potion. Which iz why I keep living. Idiot."\033[0m''')
            else:
                if alchemist_defeated < 1:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I giff you last chanze. BUY ZOMETHINK"\033[0m''')
                else:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I have impenetrabalality potion. Which iz why I keep living. NOW BUY ZOMETHINK"\033[0m''')
        leave = 0
        brewery_encouters += 1
        while True:
            counter = 0
            print("Your balance is\033[38;2;200;200;0m", player_money, "coins\033[0m")
            for i in current_alchemist_items:
                counter += 1
                print(counter, ". ", item_names[i], " - \033[38;2;200;200;0m", cost(i), " coins\033[0m", sep = "")
            counter += 1
            print(counter, ". Inspect", sep = "")
            print(counter + 1, ". Leave", sep = "")
            while True:
                print("Which one do you want to buy?")
                action = input()
                if action.isdigit():
                    action = int(action)
                    if action > 0 and action <= len(current_alchemist_items):
                        shop_buy(action - 1, "alchemist")
                        break
                    elif action - 1 == len(current_alchemist_items):
                        item_info(shop_weapon, "alchemist")
                        break
                    elif action - 2 == len(current_alchemist_items):
                        leave = 1
                        break
                else:
                    print("Type in the correct action")
            if leave == 1:
                break
        print('''You left the brewery and continued your journey...''')
    else:
        if alchemist_defeated == 0:
            print('''You came across a brewery. Inside, you were greeted by \033[38;2;200;0;150mthe alchemist\033[0m,
\033[38;2;200;0;150m"I gave you enouff chanzes. Ja are goink to pay."\033[0m
Type anything to continue...''')
        else:
            print('''You came across a brewery. Inside, you were greeted by \033[38;2;200;0;150mthe alchemist\033[0m,
\033[38;2;200;0;150m"Again. Anozer round?"\033[0m
Type anything to continue...''')
        action = input()
        fight([64])
        if lost == 1:
            reset_player()
            lost = 0
            alchemist_anger = 0.4
        else:
            alchemist_anger = 1
            alchemist_defeated += 1

def boss_upgrade():
    global last_boss
    global bosses_for_areas
    global max_power_level
    global player_shield
    global player_gold_boost
    global player_magic_shield
    global player_damage_range_boost
    global player_poison_def
    global player_spikes_armor_break
    global player_crit_chance_reduction
    global player_base_dmg
    global player_spikes
    garden_reward, forest_reward, cave_reward, tundra_reward, canyon_reward, desert_reward, rot_reward = False, False, False, False, False, False, False
    for i in last_boss:
        if i in bosses_for_areas[0]:
            garden_reward = True
        if i in bosses_for_areas[1]:
            forest_reward = True
        if i in bosses_for_areas[2]:
            cave_reward = True
        if i in bosses_for_areas[3]:
            tundra_reward = True
        if i in bosses_for_areas[4]:
            canyon_reward = True
        if i in bosses_for_areas[5]:
            desert_reward = True
        if i in bosses_for_areas[6]:
            rot_reward = True
    if garden_reward:
        player_shield += round(20 * (75 - player_shield) / 75)
        print("You now ignore ", player_shield, "% of physical DMG!", sep = "")
    if forest_reward:
        player_gold_boost += 25
        print("You get ", player_gold_boost, "% more money from enemies.", sep = "")
    if cave_reward:
        player_magic_shield += round(20 * (75 - player_magic_shield) / 75)
        print("You now ignore ", player_magic_shield, "% of magic DMG!", sep = "")
    if tundra_reward:
        player_damage_range_boost += 15
        print("You deal ", player_damage_range_boost, "% more DMG!", sep = "")
    if canyon_reward:
        if game_mode in ["story", "infinite"]:
            player_poison_def += round(15 * ((player_poison_def / 25) + 1))
        elif game_mode in ["raid"]:
            player_poison_def += round(3 * ((player_poison_def / 30) + 1))
        print("Your poison defense is now", player_poison_def, "PSNDEF!")
    if desert_reward:
        if game_mode in ["story", "infinite"]:
            player_spikes_armor_break += round(10 * ((player_spikes_armor_break / 50) + 1))
        elif game_mode in ["raid"]:
            player_spikes_armor_break += round(2 * ((player_spikes_armor_break / 25) + 1))
        player_spikes += round((player_spikes / 20) + 1)
        print("You now have", player_spikes, "SPK, which break", player_spikes_armor_break, "of enemies' DEF.")
    if rot_reward:
        if player_crit_chance > 1:
            player_crit_chance_reduction -= round(player_crit_chance_reduction * 0.25)
            print("Your crit. chance reduction is now ", player_crit_chance_reduction, "%!", sep = "")
        else:
            player_base_dmg += round(player_base_dmg * 1.4)
            print("Your base damage is now", player_base_dmg, "DMG!")
    if 52 in last_boss:
        if change_recruited == False and death_defeated == False:
            print("You have become the 3174th...")
        elif change_recruited == True and death_defeated == False:
            print("You and Change have managed to defeat Cycle and the 3173rd.\nYou have destroyed the balance of elements, leaving only dense forests and some landmarks behind.\nAnd without your creator you cannot exist...")
        elif change_recruited == False and death_defeated == True:
            print("You and Death have managed to defeat Cycle and the 3173rd.\nBut without an opposite force, you destroyed the balance of elements.\nAnd without your creator you cannot exist...")
        elif change_recruited == True and death_defeated == True:
            print("Death and Cycle have managed to extract every poor soul that the 3173rd has consumed.\nCycle and its creations were banished from this realm, and without your creator you cannot exist. You have died as a hero...")
    if 4 in last_boss:
        max_power_level += 1
        print("More enemies consider you a threat.")

    print("Type anything to continue...")
    action = input()
    print("\n\n\n")

def mimic_gamble():
    global mimic_gamble_encounters
    global player_money
    global mimic_got_item
    global mimic_given_items
    global item_rando
    global gamble_seed
    change_cost = round(10 * (mimic_given_items / 2 + 1))
    for i in range(score):
        change_cost += change_cost // 10
    if item_rando:
        common_items = [2, 4, 6, 8, 11, 13, 14, 15]
        uncommon_items = [1, 3, 5, 9, 12, 16]
        rare_items = [0, 7, 10]
    else:
        common_items = [4, 6, 8]
        uncommon_items = [3, 5, 9, 16]
        rare_items = [7, 10]
    if mimic_got_item == False:
        if mimic_gamble_encounters == 0:
            print('''You see a golden chest on your path. You reach to open it, but as if it is alive, it springs back.
It starts talking, \033[38;2;200;240;0m"Hey, pal! It is rude to open a mimic's mouth without permission."\033[0m
It continues, \033[38;2;200;240;0m"However, I think I can play a game with you."\033[0m
It jumps closer to you, \033[38;2;200;240;0m"I will give you a present. If you don't like it, you can pay me to get a different one."\033[0m
Do you like the idea?
1. Yes
2. No''')
            action = input()
            if action == "1" or action == "2":
                print('''\033[38;2;200;240;0m"What? I didn't ask anything. Anyway, let's see what I can gift you."\033[0m''')
        elif mimic_gamble_encounters < 3:
            print('''You approach the golden chest and as usual, it starts to speak, \033[38;2;200;240;0m"Hey, pal. Welcome back. Wanna somethin'?"\033[0m''')
        elif mimic_gamble_encounters == 3:
            print('''You approach the golden chest and as usual, it springs to life, \033[38;2;200;240;0m"Hey. Third time's the charm, right?"\033[0m''')
        else:
            dialogue = randint(1, 100)
            if dialogue < 34:
                print('''You approach golden mimic again. It starts to speak, \033[38;2;200;240;0m"Hey, there. Wanna gift?"\033[0m''')
            elif dialogue < 67:
                print('''You approach a familiar golden chest, which starts talking, \033[38;2;200;240;0m"Hey, pal. Need a gift by any chance?"\033[0m''')
            elif dialogue < 100:
                print('''You walk up to the golden mimic. \033[38;2;200;240;0m"Hey, pal. Welcome back. Let me just get you somethin'."\033[0m''')
            else:
                mimic_gamble_encounters = 0
                print('''You approach the familiar mimic, but its tone is different, \033[38;2;200;240;0m"Hey, pal. Here to torture me again with your needs?"\033[0m
Slightly creeped out you back away a bit.
\033[38;2;200;200;0m"Do you have any idea, what it's like to be a pawn with no free will and no control?"\033[0m
The mimic starts to crack, "\033[38;2;160;160;40mI said too much again. \033[38;2;140;140;80mI will forget this and be reborn. \033[38;2;120;120;120mSay goodbye to this me, pal."\033[0m
The chest shatters into pieces. Then the pieces fly towards each other and form the chest again. It speaks again,
\033[38;2;200;240;0m"Oh hey there, pal. Wanna gift?"\033[0m''')
    elif mimic_given_items <= 5:
        print('''You approach the familiar mimic again. It springs to life and says,
\033[38;2;200;240;0m"Hey, pal. I am a little too tired for your funny business..."\033[0m
It continues, \033[38;2;200;240;0m"However, if you pay me a little, I will give you another item."\033[0m''')
        print("Your balance is", player_money, "coins")
        print("1. Pay", change_cost * 2, "coins\n2. Refuse")
        while True: 
            action = input()
            if action == "1" or action.lower() == "pay":
                if player_money >= change_cost * 2:
                    player_money -= change_cost * 2
                    print('''\033[38;2;200;240;0m"Alright, gimme a second, pal."\033[0m''')
                    mimic_got_item = False
                    break
                else:
                    print('''\033[38;2;200;240;0m"Ay, ay, ay! Don't you scam me like that. I can clearly tell that you don't have enough. Just leave."\033[0m''')
                    break
            elif action == "2" or action.lower() == "refuse":
                print('''\033[38;2;200;240;0m"Your choice, I guess."\033[0m''')
                break
    else:
        print('''You approach the familiar mimic again. It springs to life and say,
\033[38;2;200;240;0m"Hey, pal. I am a little too tired for your funny business... And my stomach hurts..."\033[0m
It continues, \033[38;2;200;240;0m"Can you meet me later? I don't feel like vomiting another gift."\033[0m''')

    while mimic_given_items <= 5:
        if mimic_got_item == True:
            break
        leave = 0
        while mimic_got_item == False:
            seed(gamble_seed)
            remember_seed = gamble_seed
            gamble_seed = randint(0, 10000)
            while gamble_seed == remember_seed:
                gamble_seed = randint(0, 10000)
            if chance(0.6):
                item = choice(common_items)
            elif chance(0.75):
                item = choice(uncommon_items)
            else:
                item = choice(rare_items)
            print('\033[38;2;200;240;0m"How about ', item_names[item], '?"\033[0m', sep ="")
            print("Your balance is", player_money, "coins")
            print("1. Take it\n2. Pay", change_cost, "coins to reroll\n3. Inspect")
            while True:
                print("Type in the action")
                action = input()
                if action == "1":
                    shop_grant(item)
                    mimic_got_item = True
                    mimic_given_items += 1
                    break
                elif action == "2":
                    if player_money >= change_cost:
                       player_money -= change_cost
                       print('''\033[38;2;200;240;0m"Alright, gimme a second, pal."\033[0m''')
                       break
                    else:
                        print('''\033[38;2;200;240;0m"Ay, ay, ay! Don't you scam me like that. I can clearly tell that you don't have enough. Just take the item."\033[0m''')
                elif action == "3":
                    print('\033[38;2;200;240;0m"', item_descriptions_mimic[item], '"\033[0m', sep = "")
        if mimic_given_items <= 5:
            change_cost = round(10 * (mimic_given_items / 2 + 1))
            for i in range(score):
                change_cost += change_cost // 10
            print('''The chest speaks again,\033[38;2;200;240;0m "Hmm... I can give you another item, if you pay me a little."\033[0m
Will you pay''', change_cost * 2, "coins? Your balance is", player_money, "coins.")
            print("1. Pay\n2. Refuse")
            while True: 
                action = input()
                if action == "1" or action.lower() == "pay":
                    if player_money >= change_cost * 2:
                        player_money -= change_cost * 2
                        print('''\033[38;2;200;240;0m"Alright, gimme a second, pal."\033[0m''')
                        mimic_got_item = False
                        break
                    else:
                        print('''\033[38;2;200;240;0m"Ay, ay, ay! Don't you scam me like that. I can clearly tell that you don't have enough. Just leave."\033[0m''')
                        break
                elif action == "2" or action.lower() == "refuse":
                    print('''\033[38;2;200;240;0m"Your choice, I guess."\033[0m''')
                    leave = 1
                    break
        else:
            print('''The chest tiringly says, \033[38;2;200;240;0m"Ooh, pal. I think that is enough for now. Meet me later."\033[0m''')
        if leave == 1:
            break
    print('''\033[38;2;200;240;0m"Alright, good luck there, pal."\033[0m After that you moved forwards.\n\n\n''')
    mimic_gamble_encounters += 1

def death_boat():
    global death_encounters
    global player_boat
    global player_money
    global player_base_dmg
    global spirit_anger_reduction
    sacrificed = 0
    price = 21
    for i in range(score):
        price += round(price / 15)
    if death_encounters == 0:
        print('''You see a weird creature with four heads, each wearing a mask.
You brace yourself, but the creature speaks,
\033[38;2;100;100;100m"Hello, another one. I am no threat to you."\033[0m
You lower your weapon. She continues,
\033[38;2;100;100;100m"I can provide you a boat. But it only functions in this area."\033[0m
Do you accept a gift of a boat from this creature?
1. Yes
2. No''')
        while True:
            action = input()
            if action == "1" or action.lower() == "yes":
                print('''You grab the incredibly light boat. The creature speaks again,
\033[38;2;100;100;100m"I hope it will help you. I shall depart. Meet me later."\033[0m
After that, she crawls away.''')
                player_boat = True
                break
            elif action == "2" or action.lower() == "no":
                print('''You refuse to grab the boat. The creature speaks again,
\033[38;2;100;100;100m"Do not let your cockiness be the death of yours."\033[0m
She then crawls away.''')
                break
        print('''You continue your journey...''')
    elif death_encounters == 1:
        print('''You see the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. The boat prices are growing, which is why I have to sell them now."\033[0m
She continues, \033[38;2;100;100;100m"I can give you a boat for''', price, '''coins."\033[0m
Your balance is''', player_money, '''coins.
1. Pay''', price, '''
2. Continue your journey''')
        while True:
            action = input()
            if action == "1" or action.lower() == "pay":
                if player_boat == True:
                    print('''The creature looks at you with confusion,
\033[38;2;100;100;100m"I do not take gratuity. But thank you?"\033[0m''')
                elif player_money >= price:
                    print('''You offer your coins. The creature grabs them, and hands you the boat,
\033[38;2;100;100;100m"I am surprised, that you actually decided to pay. Thank you?"\033[0m''')
                    player_money -= price
                    player_boat = True
                else:
                    print('''You offer less than she asked. The creature looks at you,
\033[38;2;100;100;100m"I can tell that you are trying trick me."\033[0m
You take your money back.''')
            elif action == "2" or action.lower() == "leave":
                print('''The creature speaks again,
\033[38;2;100;100;100m"Good bye. We will meet again."\033[0m You continue your journey...''')
                break
    elif death_encounters == 2:
        print('''You see the mask creature again. She speaks,
\033[38;2;100;100;100m"Hello, warrior. I thought of the inevitable that will come for you. And I am not talking about myself."\033[0m
Slightly unsettled by this, you continue listening, \033[38;2;100;100;100m"Some spirits may come for you."\033[0m
\033[38;2;100;100;100m"But I can provide some safety for you. It is not easy, which is why I ask for payment."\033[0m
She continues, \033[38;2;100;100;100m"However, I do not need your coins. Instead, I need your strength."\033[0m
Your balance is''', player_money, '''coins.
1. Pay''', price, '''for a boat
2. Sacrifice 10% of your strength
3. Self Inspect
4. Continue your journey''')
        while True:
            action = input()
            if action == "1" or action.lower() == "pay":
                if player_boat == True:
                    print('''The creature looks at you with confusion,
\033[38;2;100;100;100m"I do not take gratuity. But thank you for the offer?"\033[0m''')
                elif player_money >= price:
                    print('''You offer your coins. The creature grabs them, and hands you the boat,
\033[38;2;100;100;100m"I am surprised, that you actually decided to pay. Thank you?"\033[0m''')
                    player_money -= price
                    player_boat = True
                else:
                    print('''You offer less than she asked. The creature looks at you,
\033[38;2;100;100;100m"I can tell that you are trying trick me."\033[0m
You take your money back.''')
            elif action == "2" or action.lower() == "sacrifice":
                if sacrificed == 0:
                    player_base_dmg -= round(player_base_dmg * 0.1)
                    spirit_anger_reduction += 1
                    sacrificed += 1
                    print('''You feel part of your strength leaving your body. Few moments later you feel safety.
\033[38;2;100;100;100m"They should become weaker. Unlike the boat, this is permanent."\033[0m
Your base damage is now''', player_base_dmg, '''DMG!''')
                elif sacrificed == 1:
                    print('''The creature speaks again,
\033[38;2;100;100;100m"No. You are going to be far too weak."\033[0m''')
            elif action == "3" or "self" in action.lower() or "inspect" in action.lower():
                print("\033[38;2;255;0;0mStrength -", player_base_dmg, "DMG\033[0m")
            elif action == "4" or action.lower() == "leave":
                print('''The creature speaks again,
\033[38;2;100;100;100m"Good bye. We will meet again."\033[0m You continue your journey...''')
                break
    else:
        if area_id == 0:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. Do you feel the familiarity of your home?"\033[0m
She quickly changes the topic, \033[38;2;100;100;100m"Do you need a boat here? Or help with spirits?"\033[0m''')
        elif area_id == 2:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. Can you feel the presence of another being like me, penetrating the air?"\033[0m
She quickly changes the topic, \033[38;2;100;100;100m"Do you need a boat here? Or help with spirits?"\033[0m''')
        elif area_id == 4:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. What is this feeling? Pride? Longing? Nostalgia? I do not feel it anywhere else."\033[0m
She quickly changes the topic, \033[38;2;100;100;100m"Do you need a boat here? Or help with spirits?"\033[0m''')
        elif area_id == 5:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. I do not enjoy being in this place. I feel guilt? I hate recalling \033[38;2;100;100;100;3mHim.\033[0m
She quickly changes the topic, \033[38;2;100;100;100m"Do you really need a boat here? Or help with spirits?"\033[0m''')
        elif area_id == 6:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. This place reminds me of... No, not right in anyone's presence."\033[0m
She quickly changes the topic, \033[38;2;100;100;100m"You probably need a boat here. Do you need help with spirits?"\033[0m''')
        else:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Do you need a boat here? Or help with spirits?"\033[0m''')
        print('''Your balance is''', player_money, '''
1. Pay''', price, '''for a boat
2. Sacrifice 10% of your strength
3. Self Inspect
4. Continue your journey''')
        while True:
            action = input()
            if action == "1" or action.lower() == "pay":
                if player_boat == True:
                    print('''The creature looks at you with confusion,
\033[38;2;100;100;100m"I do not take gratuity. But thank you for the offer?"\033[0m''')
                elif player_money >= price:
                    print('''You offer your coins. The creature grabs them, and hands you the boat,
\033[38;2;100;100;100m"I am surprised, that you actually decided to pay. Thank you?"\033[0m''')
                    player_money -= price
                    player_boat = True
                else:
                    print('''You offer less than she asked. The creature looks at you,
\033[38;2;100;100;100m"I can tell that you are trying trick me."\033[0m
You take your money back.''')
            elif action == "2" or action.lower() == "sacrifice":
                if sacrificed == 0:
                    player_base_dmg -= round(player_base_dmg * 0.1)
                    spirit_anger_reduction += 1
                    sacrificed += 1
                    print('''You feel part of your strength leaving your body. Few moments later you feel safety.
\033[38;2;100;100;100m"They should become weaker. Unlike the boat, this is permanent."\033[0m
Your base damage is now''', player_base_dmg, '''DMG!''')
                elif sacrificed == 1:
                    print('''The creature speaks again,
\033[38;2;100;100;100m"No. You are going to be far too weak."\033[0m''')
            elif action == "3" or "self" in action.lower() or "inspect" in action.lower():
                print("\033[38;2;255;0;0mStrength -", player_base_dmg, "DMG\033[0m")
            elif action == "4" or action.lower() == "leave":
                print('''The creature speaks again,
\033[38;2;100;100;100m"Good bye. We will meet again."\033[0m You continue your journey...''')
                break

    death_encounters += 1

def escape():
    global escaped
    print('''You see a secret passage, leading to somewhere.
Do you want to abandon this place or continue exploring it?
1. Escape
2. Stay''')
    while True:
        action = input()
        if action == "1" or action.lower() == "escape":
            escaped = True
            break
        elif action == "2" or action.lower() == "stay":
            break

def change_interaction():
    global area_id
    global change_recruited
    global change_encouters
    if area_id == 2 and change_encouters == 0:
        print('''You come across a man with otherworldly glow surrounding him.
He quickly notices you and starts to speak, \033[38;2;100;100;175m"You. You. Another one. Did you come here to destroy me or to see me suffer?"\033[0m
You attempt to respond but the words aren't coming out of your mouth.
\033[38;2;100;100;175m"Stop mocking me. You don't understand what it is like to hide in the shadows for more than any mortal's lifespan."\033[0m
. . .
1. Continue talking
2. Leave''')
        while True:
            action = input()
            if action == "1" or "continue" in action.lower() or "talking" in action.lower():
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
\033[38;2;100;100;175m"Great. I will assist you in the your last battle, and you will assist me. Meet me again in the land of your creation."\033[0m
You leave the man alone...''')
                        change_recruited = True
                        break
                    elif action == "2" or action.lower() == "no":
                        print('''The man looks surprised, \033[38;2;100;100;175m"You aren't going to help me? Well, don't tell your creator where I am, okay?"\033[0m
You leave the man alone...''')
                        break
                break
            elif action == "2" or action.lower() == "leave":
                print("You turned around and left the mysterious man alone...")
                break
        change_encouters += 1
    elif area_id == 2 and change_encouters != 0:
        if change_recruited == True:
            print('''You approach the weird man again. He speaks again,
\033[38;2;100;100;175m"Okay, I will repeat. I will assist you in the your last battle, and you will assist me. Meet me again in the land of your creation."\033[0m
You leave the man alone...''')
        else:
            print('''You approach the weird man again. He speaks again,
\033[38;2;100;100;175m"Leave. Me. Alone."\033[0m
You leave the man alone...''')
    elif area_id == 0 and change_encouters == 1:
        print('''You come across the mysterious man again. He notices and speaks quietly,
\033[38;2;100;100;175m"Hello, again. I assume we're still going with the plan, right?"\033[0m
\033[38;2;100;100;175m"The next formidable foe you're going to face is your sibling. Please, don't consume 'em; we need to stop Cycle's cycle, not continue it."\033[0m
After a pause he adds, \033[38;2;100;100;175m"Not sure what else to say, that you wouldn't already know."\033[0m
You leave the man and continue your journey...
Type anything to continue...''')
        action = input()
        change_encouters += 1
    elif area_id == 0 and change_encouters == 2:
        print('''You come to the mysterious man again. He speaks quietly again,
\033[38;2;100;100;175m"What? Just go to the boss and I will help you."\033[0m
You walk away and continue your journey...''')
    else:
        print('''You aren't supposed to encouter this event tile in this area! Please notify the developer!
Type anything to continue...''')
        action = input()

def player_remnants():
    global player_money
    global player_spikes
    global player_poison
    global remnant_seed
    seed(remnant_seed)
    remnant_seed = randint(0, 10000)
    money = round(uniform(5, 15) * (score / 2 + 1))
    spike = round(uniform(1, 2) * (score / 3 + 1))
    poison = round(uniform(1, 1.25) * (score / 5 + 1))
    player_money += money
    player_spikes += spike
    player_poison += poison
    print('''You came across a warrior's remnants. You picked up their items...
You got''', money, "coins (your balance is", player_money, "coins),", spike, "SPK(your total is", player_spikes, "SPK), and", poison, "PSN(your total is", player_poison, '''PSN)!
Type anything to continue...''')
    action = input()

def reset_player():
    global player_max_hp
    player_max_hp = 100
    global player_base_def
    player_base_def = 0
    global player_base_dmg
    player_base_dmg = 5
    global player_base_magic_def
    player_base_magic_def = 0
    global player_crit_chance
    player_crit_chance = 5
    global player_poison
    player_poison = 0
    global player_spikes
    player_spikes = 0
    global player_money
    player_money = 0
    print("You lost everything but your life.")

def true_reset():
    global player_max_hp
    player_max_hp = 100
    global player_base_def
    player_base_def = 0
    global player_base_dmg
    player_base_dmg = 5
    global player_base_magic_def
    player_base_magic_def = 0
    global player_extra_magic_def
    player_extra_magic_def = 0
    global player_min_extra_magic_def
    player_min_extra_magic_def = 0
    global player_crit_chance
    player_crit_chance = 5
    global player_weapon
    player_weapon = 0
    global player_poison
    player_poison = 0
    global player_spikes
    player_spikes = 0
    global player_money
    player_money = 0
    global player_xp
    player_xp = 0
    global player_level
    player_level = 0
    global lost
    lost = 0
    global win
    win = 0
    global score
    score = 0
    global raid_counter
    raid_counter = 0
    global original_difficulty
    global difficulty
    difficulty = original_difficulty
    global score_increase
    score_increase = 0
    global map_complexity
    map_complexity = 0
    global max_power_level
    max_power_level = 1
    global max_power_level_increase
    max_power_level_increase = 0
    global player_shield
    player_shield = 0
    global player_magic_shield
    player_magic_shield = 0
    global player_gold_boost
    player_gold_boost = 0
    global player_damage_range_boost
    player_damage_range_boost = 0
    global player_poison_def
    player_poison_def = 0
    global player_spikes_armor_break
    player_spikes_armor_break = 0
    global player_crit_chance_reduction
    player_crit_chance_reduction = 100
    global last_boss
    last_boss = []
    global is_boss_battle
    is_boss_battle = False
    global player_lifesteal
    player_lifesteal = 0
    global player_immortality
    player_immortality = 0
    global player_current_immortality
    player_current_immortality = player_immortality
    global player_regen
    player_regen = 0
    global player_consume
    player_consume = 0
    global player_travel
    player_travel = 0
    global player_enemy_explotano
    player_enemy_explotano = 0
    global player_extra_life
    player_extra_life = 0
    global player_spent_life
    player_spent_life = 0
    global player_items
    player_items = []
    global debt
    debt = 0
    global shopkeeper_sus
    shopkeeper_sus = 0
    global shopkeeper_deaths
    shopkeeper_deaths = 0
    global cur_shopkeeper_dead
    cur_shopkeeper_dead = False
    global vitality_anger
    vitality_anger = 0
    global strength_anger
    strength_anger = 0
    global might_anger
    might_anger = 0
    global protection_anger
    protection_anger = 0
    global fear_anger
    fear_anger = 0
    global mimic_gamble_encounters
    mimic_gamble_encounters = 0
    global death_encounters
    death_encounters = 0
    global speed_timer
    speed_timer = 0
    global player_oxygen
    player_oxygen = 3
    global player_boat
    player_boat = False
    global death_defeated
    death_defeated = False
    global change_encouters
    change_encouters = 0
    global change_recruited
    change_recruited = False
    global final_area
    final_area = False
    default_enemies()

def settings_reset():
    global weather_amount
    weather_amount = 1
    global difficulty
    difficulty = 55
    global evolution
    evolution = False
    global overkill
    overkill = False
    global speedrunner
    speedrunner = False
    global item_rando
    item_rando = False

def final_statistics():
    global player_max_hp
    global player_base_dmg
    global player_base_def
    global player_shield
    global player_base_magic_def
    global player_magic_shield
    global player_crit_chance
    global player_crit_chance_reduction
    global player_money
    global player_gold_boost
    global player_xp
    global player_level
    global player_spikes
    global player_spikes_armor_break
    global player_poison
    global player_poison_def
    global player_damage_range_boost
    global player_lifesteal
    global player_immortality
    global player_regen
    global player_consume
    global player_travel

    global score
    global raid_counter
    global max_power_level
    global vitality_anger
    global strength_anger
    global might_anger
    global protection_anger
    global shopkeeper_sus
    global shopkeeper_deaths
    global alchemist_anger
    global alchemist_defeated
    global death_defeated
    print("Stats:")
    print("Max health: ", player_max_hp, " HP", sep = "")
    print("Base damage: ", player_base_dmg, " DMG", sep = "")
    if player_damage_range_boost > 0:
        print("Damage boost: ", player_damage_range_boost, "%", sep = "")
    print("Base defense: ", player_base_def, " DEF", sep = "")
    if player_shield > 0:
        print("Shield: ", player_shield, "%", sep = "")
    print("Base magic defense: ", player_base_magic_def, " MGCDEF", sep = "")
    if player_magic_shield > 0:
        print("Magic shield: ", player_magic_shield, "%", sep = "")
    print("Crit. chance: ", player_crit_chance, "%", sep = "")
    print("Crit. chance reduction: ", player_crit_chance_reduction, "%", sep = "")
    if player_spikes > 0:
        print("Spikes: ", player_spikes, " SPK", sep = "")
    if player_spikes_armor_break > 0:
        print("Defense broken by spikes: ", player_spikes_armor_break, " DEFRED", sep = "")
    if player_poison > 0:
        print("Poison: ", player_poison, " PSN", sep = "")
    if player_poison_def > 0:
        print("Poison defense: ", player_poison_def, " PSNDEF", sep = "")
    if player_lifesteal > 0:
        print("Lifesteal: ", player_lifesteal, "%", sep = "")
    if player_immortality > 0:
        print("Immortal for ", player_immortality, " turns", sep = "")
    if player_regen > 0:
        print("Regeneration: +", player_regen, "%", sep = "")
    if player_dodge_chance > 0:
        print("Dodge chance: ", player_dodge_chance, "% DCH", sep = "")
    if player_consume > 0:
        print("Consume: ", player_consume, "%", sep = "")
    if player_travel > 0:
        print("Travel skill: ", player_travel, "%", sep = "")
    print("Money: ", player_money, " coins", sep = "")
    if player_gold_boost > 0:
        print("Money boost: ", player_gold_boost, "%", sep = "")
    print("Experience: ", player_xp, "/", xp_to_lvl_up(), " XP", sep = "")
    print("Level: ", player_level, sep = "")
    print("Score: ", score, sep = "")
    if game_mode == "raid":
        print("Raids survived: ", raid_counter, sep = "")
    print("Max power level: ", max_power_level, sep = "")
    if shopkeeper_deaths > 0 or shopkeeper_sus > 0:
        print("\nReputation:")
    if shopkeeper_sus > 0:
        print("Shopkeeper's sus meter: ", shopkeeper_sus, sep = "")
    if shopkeeper_deaths > 0:
        print("Shopkeepers' death count: ", shopkeeper_deaths, sep = "")
    if alchemist_anger > 0:
        print("Alchemist's anger meter: ", alchemist_anger, sep = "")
    if alchemist_defeated > 0:
        print("Alchemist's anger meter: ", alchemist_defeated, sep = "")
    if death_defeated == True:
        print("You have defeated Death")

def inventory_statistics():
    global player_max_hp
    global player_base_dmg
    global player_base_def
    global player_shield
    global player_base_magic_def
    global player_magic_shield
    global player_crit_chance
    global player_crit_chance_reduction
    global player_money
    global player_gold_boost
    global player_xp
    global player_level
    global player_spikes
    global player_spikes_armor_break
    global player_poison
    global player_poison_def
    global player_damage_range_boost
    global player_lifesteal
    global player_immortality
    global player_regen
    global player_dodge_chance
    global player_consume
    global player_travel

    global score
    global max_power_level
    print("Stats:")
    print(player_max_hp, " HP; ", player_base_dmg, " DMG; ", sep = "", end = "")
    if player_damage_range_boost > 0:
        print(player_damage_range_boost, "% DMG Boost; ", sep = "", end = "")
    print(player_base_def, " DEF; ", sep = "", end = "")
    if player_shield > 0:
        print(player_shield, "% SHLD; ", sep = "", end = "")
    if player_base_magic_def > 0:
        print(player_base_magic_def, " MGCDEF; ", sep = "", end = "")
    if player_magic_shield > 0:
        print(player_magic_shield, "% MGCSHLD; ", sep = "", end = "")
    print(player_crit_chance, "% CRT; ", sep = "", end = "")
    print("Crit. chance reduction: ", player_crit_chance_reduction, "%; ", sep = "")
    if player_spikes > 0:
        print(player_spikes, " SPK; ", sep = "", end = "")
    if player_spikes_armor_break > 0:
        print(player_spikes_armor_break, " DEFRED; ", sep = "", end = "")
    if player_poison > 0:
        print(player_poison, " PSN; ", sep = "", end = "")
    if player_poison_def > 0:
        print(player_poison_def, " PSNDEF; ", sep = "", end = "")
    if player_lifesteal > 0:
        print(player_lifesteal, "% LFSTL; ", sep = "", end = "")
    if player_immortality > 0:
        print(player_immortality, " IMM; ", sep = "", end = "")
    if player_regen > 0:
        print("+", player_regen, "% REG", sep = "", end = "")
    if player_dodge_chance > 0:
        print(player_dodge_chance, "% DCH", sep = "", end = "")
    print()
    if player_consume > 0:
        print("Consume: ", player_consume, "%; ", sep = "", end = "")
    if player_travel > 0:
        print("Travel skill: ", player_travel, "%; ", sep = "", end = "")
    print("Money: ", player_money, " coins", sep = "")
    if player_gold_boost > 0:
        print("Money boost: ", player_gold_boost, "%", sep = "")
    print("Experience: ", player_xp, "/", xp_to_lvl_up(), " XP", sep = "")
    print("Level: ", player_level, sep = "")
    print("Score: ", score, sep = "")
    print("Max power level: ", max_power_level, sep = "")

def map_generation():
    global escaped
    global score
    global score_increase
    global map_complexity
    global events
    global events_coordinates
    global player_coordinates
    global events_heights
    global benefitial_events
    global hurtful_events
    global neutral_events
    global game_mode
    global change_recruited
    global speedrunner
    global speed_timer
    global area_id
    global map_seed
    global shop_seed
    global weather_seed
    global weather_effects_seed
    seed(map_seed)
    shop_seed, weather_seed, weather_effects_seed = map_seed, map_seed, map_seed
    map_seed = randint(0, 10000)
    start = choice(start_positions[area_id])
    good_events = []
    bad_events = []
    if game_mode in ["infinite", "story"]:
        if score >= 0:
            good_events.append(3)
        if score >= 3:
            good_events.append(5)
        if score >= 5:
            good_events.append(11)
        if score >= 7:
            good_events.append(24)
    elif game_mode == "raid":
        good_events.append(3)
        if area_id > 0:
            good_events.append(5)
        if area_id > 1:
            good_events.append(24)
    if game_mode == "story" and (area_id == 2 or (area_id == 0 and change_recruited == True)):
        good_events.append(13)
    min_remnant, max_remnant, avg_remnant = remnants_spawns[area_id][0], remnants_spawns[area_id][1], remnants_spawns[area_id][2]
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
    for i in range(map_complexity + 5):
        for i in range(randint(1, round(rate))):
            bad_events.append(1)
        if area_id == 3 and chance(0.2):
            bad_events.append(8)
        elif area_id == 3 and chance(0.125):
            bad_events.append(7)
        rate -= 0.125
        if rate < 1:
            rate = 1
    rate = 2.875
    for i in range(map_complexity + 2):
        for i in range(randint(1, round(rate))):
            good_events.append(2)
        rate -= 0.125
        if rate < 1:
            rate = 1

    #print(len(bad_events))
    score_increase = 0.75 * len(bad_events)

    turns = []
    if start[0] == "u":
        turns.append([0, 0, "d", 1, 5])
    elif start[0] == "d":
        turns.append([0, 0, "u", 1, 5])
    else:
        turns.append([0, 0, "d", 1, 5])
        turns.append([0, 0, "u", 1, 5])
    if start[1] == "l":
        turns.append([0, 0, "r", 1, 5])
    elif start[1] == "r":
        turns.append([0, 0, "l", 1, 5])
    else:
        turns.append([0, 0, "r", 1, 5])
        turns.append([0, 0, "l", 1, 5])
    events = [1]
    events_coordinates = [[0, 0]]
    events_heights = [5]
    player_coordinates = [0, 0]
    x = 0
    y = 0
    iteration = 0
    while len(good_events) + len(bad_events) > 0:
        iteration += 1
        bad_path = False
        if len(turns) == 1:
            break
        if iteration > 1000:
            break
        path = choice(turns)
        x = path[0]
        y = path[1]
        h = path[4]
        if path[2] == "r":
            min_length = round(path_lengths[area_id][0] - (map_complexity * 0.025))
            if min_length < 0:
                min_length = 0
            possible_max_lengths = [path_lengths[area_id][1]]
            for i in range(map_complexity):
                max_length = round(path_lengths[area_id][1] - i * 0.3)
                if max_length < min_length:
                    max_length = min_length
                possible_max_lengths.append(max_length)
            length = randint(min_length, choice(possible_max_lengths))
            for k in range(wall_min_thickness[area_id]):
                for i in range(length + 1):
                    if [x + 1 + i, y] in events_coordinates:
                        continue
                    if [x + 1 + i, y + 1 + k] in events_coordinates or [x + 1 + i, y - 1 + k] in events_coordinates:
                        turns.remove(path)
                        bad_path = True
                        break
                if bad_path == True:
                    break
            if bad_path == True:
                continue
            for i in range(length):
                x += 1
                h += randint(height_variaty[area_id][0], height_variaty[area_id][1])
                if h > 5:
                    h = 5
                elif h < 0:
                    h = 0
                if [x, y] in events_coordinates:
                    continue
                if chance(snow_pile_spawns[area_id]):
                    events.append(9)
                else:
                    events.append(0)
                events_coordinates.append([x, y])
                events_heights.append(h)
            x += 1
            if [x, y] in events_coordinates:
                continue
            if path[3] in hurtful_events:
                if len(good_events) > 0:
                    event = choice(good_events)
                    good_events.remove(event)
                elif len(bad_events) > 0:
                    event = choice(bad_events)
                    bad_events.remove(event)
                else:
                    event = 0
            elif path[3] in benefitial_events:
                if len(bad_events) > 0:
                    event = choice(bad_events)
                    bad_events.remove(event)
                else:
                    event = 0
            elif path[3] in neutral_events:
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
            events.append(event)
            events_coordinates.append([x, y])
            events_heights.append(h)
            if start[0] == "d" or start[0] == "m":
                if y - (path_lengths[area_id][1] + 1) >= - area_max_y[area_id] and chance(turn_up_prob[area_id]):
                    turns.append([x, y, "u", event, h])
            else:
                if y - (path_lengths[area_id][1] + 1) >= 0 and chance(turn_up_prob[area_id]):
                    turns.append([x, y, "u", event, h])
            if start[1] == "l" or start[1] == "m":
                if x + (path_lengths[area_id][1] + 1) <= area_max_x[area_id] and chance(turn_right_prob[area_id]):
                    turns.append([x, y, "r", event, h])
            else:
                if x + (path_lengths[area_id][1] + 1) <= 0 and chance(turn_right_prob[area_id]):
                    turns.append([x, y, "r", event, h])
            if start[0] == "u" or start[0] == "m":
                if y + (path_lengths[area_id][1] + 1) <= area_max_y[area_id] and chance(turn_down_prob[area_id]):
                    turns.append([x, y, "d", event, h])
            else:
                if y + (path_lengths[area_id][1] + 1) <= 0 and chance(turn_down_prob[area_id]):
                    turns.append([x, y, "d", event, h])
        elif path[2] == "d":
            min_length = round(path_lengths[area_id][0] - (map_complexity * 0.05))
            if min_length < 0:
                min_length = 0
            possible_max_lengths = [path_lengths[area_id][1]]
            for i in range(map_complexity):
                max_length = round(path_lengths[area_id][1] - i * 0.3)
                if max_length < min_length:
                    max_length = min_length
                possible_max_lengths.append(max_length)
            length = randint(min_length, choice(possible_max_lengths))
            for k in range(wall_min_thickness[area_id]):
                for i in range(length + 1):
                    if [x, y + 1 + i] in events_coordinates:
                        continue
                    if [x + 1 + k, y + 1 + i] in events_coordinates or [x - 1 - k, y + 1 + i] in events_coordinates:
                        turns.remove(path)
                        bad_path = True
                        break
                if bad_path == True:
                    break
            if bad_path == True:
                continue
            for i in range(length):
                y += 1
                h += randint(height_variaty[area_id][0], height_variaty[area_id][1])
                if h > 5:
                    h = 5
                elif h < 0:
                    h = 0
                if [x, y] in events_coordinates:
                    continue
                if chance(snow_pile_spawns[area_id]):
                    events.append(9)
                else:
                    events.append(0)
                events_coordinates.append([x, y])
                events_heights.append(h)
            y += 1
            if [x, y] in events_coordinates:
                continue
            if path[3] in hurtful_events:
                if len(good_events) > 0:
                    event = choice(good_events)
                    good_events.remove(event)
                elif len(bad_events) > 0:
                    event = choice(bad_events)
                    bad_events.remove(event)
                else:
                    event = 0
            elif path[3] in benefitial_events:
                if len(bad_events) > 0:
                    event = choice(bad_events)
                    bad_events.remove(event)
                else:
                    event = 0
            elif path[3] in neutral_events:
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
            events.append(event)
            events_coordinates.append([x, y])
            events_heights.append(h)
            if (area_id == 4 and chance(turn_down_prob[area_id])) or area_id != 4 or iteration < 3:
                if start[1] == "r" or start[1] == "m":
                    if x - (path_lengths[area_id][1] + 1) >= - area_max_x[area_id] and chance(turn_left_prob[area_id]):
                        turns.append([x, y, "l", event, h])
                else:
                    if x - (path_lengths[area_id][1] + 1) >= 0 and chance(turn_left_prob[area_id]):
                        turns.append([x, y, "l", event, h])
                if start[1] == "l" or start[1] == "m":
                    if x + (path_lengths[area_id][1] + 1) <= area_max_x[area_id] and chance(turn_right_prob[area_id]):
                        turns.append([x, y, "r", event, h])
                else:
                    if x + (path_lengths[area_id][1] + 1) <= 0 and chance(turn_right_prob[area_id]):
                        turns.append([x, y, "r", event, h])
            if start[0] == "u" or start[1] == "m":
                if y + (path_lengths[area_id][1] + 1) <= area_max_y[area_id] and chance(turn_down_prob[area_id]):
                    turns.append([x, y, "d", event, h])
            else:
                if y + (path_lengths[area_id][1] + 1) <= 0 and chance(turn_down_prob[area_id]):
                    turns.append([x, y, "d", event, h])
        elif path[2] == "l":
            min_length = round(path_lengths[area_id][0] - (map_complexity * 0.05))
            if min_length < 0:
                min_length = 0
            possible_max_lengths = [path_lengths[area_id][1]]
            for i in range(map_complexity):
                max_length = round(path_lengths[area_id][1] - i * 0.3)
                if max_length < min_length:
                    max_length = min_length
                possible_max_lengths.append(max_length)
            length = randint(min_length, choice(possible_max_lengths))
            for k in range(wall_min_thickness[area_id]):
                for i in range(length + 1):
                    if [x - 1 - i, y] in events_coordinates:
                        continue
                    if [x - 1 - i, y + 1 + k] in events_coordinates or [x - 1 - i, y - 1 - k] in events_coordinates:
                        turns.remove(path)
                        bad_path = True
                        break
                if bad_path == True:
                    break
            if bad_path == True:
                continue
            for i in range(length):
                x -= 1
                h += randint(height_variaty[area_id][0], height_variaty[area_id][1])
                if h > 5:
                    h = 5
                elif h < 0:
                    h = 0
                if [x, y] in events_coordinates:
                    continue
                if chance(snow_pile_spawns[area_id]):
                    events.append(9)
                else:
                    events.append(0)
                events_coordinates.append([x, y])
                events_heights.append(h)
            x -= 1
            if [x, y] in events_coordinates:
                continue
            if path[3] in hurtful_events:
                if len(good_events) > 0:
                    event = choice(good_events)
                    good_events.remove(event)
                elif len(bad_events) > 0:
                    event = choice(bad_events)
                    bad_events.remove(event)
                else:
                    event = 0
            elif path[3] in benefitial_events:
                if len(bad_events) > 0:
                    event = choice(bad_events)
                    bad_events.remove(event)
                else:
                    event = 0
            elif path[3] in neutral_events:
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
            events.append(event)
            events_coordinates.append([x, y])
            events_heights.append(h)
            if start[0] == "d" or start[0] == "m":
                if y - (path_lengths[area_id][1] + 1) >= - area_max_y[area_id] and chance(turn_up_prob[area_id]):
                    turns.append([x, y, "u", event, h])
            else:
                if y - (path_lengths[area_id][1] + 1) >= 0 and chance(turn_up_prob[area_id]):
                    turns.append([x, y, "u", event, h])
            if start[1] == "r" or start[1] == "m":
                if x - (path_lengths[area_id][1] + 1) >= - area_max_x[area_id] and chance(turn_left_prob[area_id]):
                    turns.append([x, y, "l", event, h])
            else:
                if x - (path_lengths[area_id][1] + 1) >= 0 and chance(turn_left_prob[area_id]):
                    turns.append([x, y, "l", event, h])
            if start[0] == "u" or start[0] == "m":
                if y + (path_lengths[area_id][1] + 1) <= area_max_y[area_id] and chance(turn_down_prob[area_id]):
                    turns.append([x, y, "d", event, h])
            else:
                if y + (path_lengths[area_id][1] + 1) <= 0 and chance(turn_down_prob[area_id]):
                    turns.append([x, y, "d", event, h])
        elif path[2] == "u":
            min_length = round(path_lengths[area_id][0] - (map_complexity * 0.05))
            if min_length < 0:
                min_length = 0
            possible_max_lengths = [path_lengths[area_id][1]]
            for i in range(map_complexity):
                max_length = round(path_lengths[area_id][1] - i * 0.3)
                if max_length < min_length:
                    max_length = min_length
                possible_max_lengths.append(max_length)
            length = randint(min_length, choice(possible_max_lengths))
            for k in range(wall_min_thickness[area_id]):
                for i in range(length + 1):
                    if [x, y - 1 - i] in events_coordinates:
                        continue
                    if [x + 1 + k, y - 1 - i] in events_coordinates or [x - 1 - k, y - 1 - i] in events_coordinates:
                        turns.remove(path)
                        bad_path = True
                        break
                if bad_path == True:
                    break
            if bad_path == True:
                continue
            for i in range(length):
                y -= 1
                h += randint(height_variaty[area_id][0], height_variaty[area_id][1])
                if h > 5:
                    h = 5
                elif h < 0:
                    h = 0
                if [x, y] in events_coordinates:
                    continue
                if chance(snow_pile_spawns[area_id]):
                    events.append(9)
                else:
                    events.append(0)
                events_coordinates.append([x, y])
                events_heights.append(h)
            y -= 1
            if [x, y] in events_coordinates:
                continue
            if path[3] in hurtful_events:
                if len(good_events) > 0:
                    event = choice(good_events)
                    good_events.remove(event)
                elif len(bad_events) > 0:
                    event = choice(bad_events)
                    bad_events.remove(event)
                else:
                    event = 0
            elif path[3] in benefitial_events:
                if len(bad_events) > 0:
                    event = choice(bad_events)
                    bad_events.remove(event)
                else:
                    event = 0
            elif path[3] in neutral_events:
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
            events.append(event)
            events_coordinates.append([x, y])
            events_heights.append(h)
            if start[0] == "d" or start[0] == "m":
                if y - (path_lengths[area_id][1] + 1) >= - area_max_y[area_id] and chance(turn_up_prob[area_id]):
                    turns.append([x, y, "u", event, h])
            else:
                if y - (path_lengths[area_id][1] + 1) >= 0 and chance(turn_up_prob[area_id]):
                    turns.append([x, y, "u", event, h])
            if start[1] == "r" or start[1] == "m":
                if x - (path_lengths[area_id][1] + 1) >= - area_max_x[area_id] and chance(turn_left_prob[area_id]):
                    turns.append([x, y, "l", event, h])
            else:
                if x - (path_lengths[area_id][1] + 1) >= 0 and chance(turn_left_prob[area_id]):
                    turns.append([x, y, "l", event, h])
            if start[1] == "l" or start[1] == "m":
                if x + (path_lengths[area_id][1] + 1) <= area_max_x[area_id] and chance(turn_right_prob[area_id]):
                    turns.append([x, y, "r", event, h])
            else:
                if x + (path_lengths[area_id][1] + 1) <= 0 and chance(turn_right_prob[area_id]):
                    turns.append([x, y, "r", event, h])
        turns.remove(path)
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
                    cur_max_xy = cur_xy
                    furthest_turn_index = turns.index(i)
                elif start[1] == "r" and turns[furthest_turn_index][2] != "l":
                    cur_max_xy = cur_xy
                    furthest_turn_index = turns.index(i)
                elif start[1] == "m":
                    cur_max_xy = cur_xy
                    furthest_turn_index = turns.index(i)
            elif start[0] == "d" and turns[furthest_turn_index][2] != "u":
                if start[1] == "l" and turns[furthest_turn_index][2] != "r":
                    cur_max_xy = cur_xy
                    furthest_turn_index = turns.index(i)
                elif start[1] == "r" and turns[furthest_turn_index][2] != "l":
                    cur_max_xy = cur_xy
                    furthest_turn_index = turns.index(i)
                elif start[1] == "m":
                    cur_max_xy = cur_xy
                    furthest_turn_index = turns.index(i)
            elif start[1] == "l" and turns[furthest_turn_index][2] != "r":
                cur_max_xy = cur_xy
                furthest_turn_index = turns.index(i)
            elif start[1] == "r" and turns[furthest_turn_index][2] != "l":
                cur_max_xy = cur_xy
                furthest_turn_index = turns.index(i)
    path = turns[furthest_turn_index]
    x = path[0]
    y = path[1]
    h = path[4]
    if path[2] == "r":
        for i in range(randint(path_lengths[area_id][1], path_lengths[area_id][1])):
            x += 1
            h += randint(height_variaty[area_id][0], height_variaty[area_id][1])
            if h > 5:
                h = 5
            elif h < 0:
                h = 0
            if [x, y] in events_coordinates:
                continue
            if chance(snow_pile_spawns[area_id]):
                events.append(9)
            else:
                events.append(0)
            events_coordinates.append([x, y])
            events_heights.append(h)
        x += 1
        if [x, y] in events_coordinates:
            events[events_coordinates.index([x, y])] = 4
            try:
                events_heights[events_coordinates.index([x, y])] = h
            except:
                events_heights.append(h)
        else:
            events.append(4)
            events_coordinates.append([x, y])
            events_heights.append(h)
    elif path[2] == "d":
        for i in range(randint(path_lengths[area_id][1], path_lengths[area_id][1])):
            y += 1
            h += randint(height_variaty[area_id][0], height_variaty[area_id][1])
            if h > 5:
                h = 5
            elif h < 0:
                h = 0
            if [x, y] in events_coordinates:
                continue
            if chance(snow_pile_spawns[area_id]):
                events.append(9)
            else:
                events.append(0)
            events_coordinates.append([x, y])
            events_heights.append(h)
        y += 1
        if [x, y] in events_coordinates:
            events[events_coordinates.index([x, y])] = 4
            try:
                events_heights[events_coordinates.index([x, y])] = h
            except:
                events_heights.append(h)
        else:
            events.append(4)
            events_coordinates.append([x, y])
            events_heights.append(h)
    elif path[2] == "l":
        for i in range(randint(path_lengths[area_id][1], path_lengths[area_id][1])):
            x -= 1
            h += randint(height_variaty[area_id][0], height_variaty[area_id][1])
            if h > 5:
                h = 5
            elif h < 0:
                h = 0
            if [x, y] in events_coordinates:
                continue
            if chance(snow_pile_spawns[area_id]):
                events.append(9)
            else:
                events.append(0)
            events_coordinates.append([x, y])
            events_heights.append(h)
        x -= 1
        if [x, y] in events_coordinates:
            events[events_coordinates.index([x, y])] = 4
            try:
                events_heights[events_coordinates.index([x, y])] = h
            except:
                events_heights.append(h)
        else:
            events.append(4)
            events_coordinates.append([x, y])
            events_heights.append(h)
    elif path[2] == "u":
        for i in range(randint(path_lengths[area_id][1], path_lengths[area_id][1])):
            y -= 1
            h += randint(height_variaty[area_id][0], height_variaty[area_id][1])
            if h > 5:
                h = 5
            elif h < 0:
                h = 0
            if [x, y] in events_coordinates:
                continue
            if chance(snow_pile_spawns[area_id]):
                events.append(9)
            else:
                events.append(0)
            events_coordinates.append([x, y])
            events_heights.append(h)
        y -= 1
        if [x, y] in events_coordinates:
            events[events_coordinates.index([x, y])] = 4
            try:
                events_heights[events_coordinates.index([x, y])] = h
            except:
                events_heights.append(h)
        else:
            events.append(4)
            events_coordinates.append([x, y])
            events_heights.append(h)
    # water landmarks
    water_turns = []
    river_chance = river_prob[area_id]
    while river_chance > 0:
        if chance(river_chance):
            if chance(0.5):
                # horizontal start
                if chance(0.5):
                    x = min_x()
                    direction = "r"
                else:
                    x = max_x()
                    direction = "l"
                y = randint(min_y(), max_y() - 1)
            else:
                # vertical start
                if chance(0.5):
                    y = min_y()
                    direction = "d"
                else:
                    y = max_y()
                    direction = "u"
                x = randint(min_x(), max_x() - 1)
            while True:
                for i in range(river_thickness[area_id]):
                    if direction == "r" or direction == "l":
                        if not y + i > max_y():
                            if not [x, y + i] in events_coordinates:
                                events.append(10)
                                events_coordinates.append([x, y + i])
                                events_heights.append(0)
                            else:
                                events_heights[events_coordinates.index([x, y + i])] = 0
                    if direction == "u" or direction == "d":
                        if not x + i > max_x():
                            if not [x + i, y] in events_coordinates:
                                events.append(10)
                                events_coordinates.append([x + i, y])
                                events_heights.append(0)
                            else:
                                events_heights[events_coordinates.index([x + i, y])] = 0
                if direction == "r":
                    x += 1
                    if chance(0.2):
                        if chance(0.5):
                            direction = "u"
                        else:
                            direction = "d"
                        water_turns.append([x, y, "r"])
                elif direction == "d":
                    y += 1
                    if chance(0.2):
                        if chance(0.5):
                            direction = "l"
                        else:
                            direction = "r"
                        water_turns.append([x, y, "d"])
                elif direction == "l":
                    x -= 1
                    if chance(0.2):
                        if chance(0.5):
                            direction = "u"
                        else:
                            direction = "d"
                        water_turns.append([x, y, "l"])
                elif direction == "u":
                    y -= 1
                    if chance(0.2):
                        if chance(0.5):
                            direction = "l"
                        else:
                            direction = "r"
                        water_turns.append([x, y, "u"])
                if x > max_x() or y > max_y() or x < min_x() or y < min_y():
                    break
                river_chance -= 0.01
        river_chance -= 0.25

    pond_chance = pond_prob[area_id]
    if chance(pond_chance):
        x = (min_x() + max_x()) // 2
        y = (min_y() + max_y()) // 2
        pond_radius[area_id] = abs(pond_radius[area_id])
        x1 = x - pond_radius[area_id]
        y1 = y + pond_radius[area_id]
        while [x1, y1] != [x - pond_radius[area_id], y - pond_radius[area_id]]:
            if not [x1, y1] in events_coordinates:
                events.append(10)
                events_coordinates.append([x1, y1])
                events_heights.append(0)
            else:
                events_heights[events_coordinates.index([x1, y1])] = 0
            y1 -= 1
        while [x1, y1] != [x + pond_radius[area_id], y - pond_radius[area_id]]:
            if not [x1, y1] in events_coordinates:
                events.append(10)
                events_coordinates.append([x1, y1])
                events_heights.append(0)
            else:
                events_heights[events_coordinates.index([x1, y1])] = 0
            x1 += 1
        while [x1, y1] != [x + pond_radius[area_id], y + pond_radius[area_id]]:
            if not [x1, y1] in events_coordinates:
                events.append(10)
                events_coordinates.append([x1, y1])
                events_heights.append(0)
            else:
                events_heights[events_coordinates.index([x1, y1])] = 0
            y1 += 1
        while [x1, y1] != [x - pond_radius[area_id], y + pond_radius[area_id]]:
            if not [x1, y1] in events_coordinates:
                events.append(10)
                events_coordinates.append([x1, y1])
                events_heights.append(0)
            else:
                events_heights[events_coordinates.index([x1, y1])] = 0
            x1 -= 1

    if chance(escape_river_prob[area_id]) and escaped == False and game_mode in ["infinite", "story"]:
        if len(water_turns) > 0:
            turn = choice(water_turns)
        else:
            turn = [(min_x() + max_x()) // 2, -1, "d"]
        x, y = turn[0], turn[1]
        if turn[2] == "r":
            while x + 1 < max_x():
                x += 1
                if not [x, y] in events_coordinates:
                    events.append(10)
                    events_coordinates.append([x, y])
                    events_heights.append(0)
                else:
                    events_heights[events_coordinates.index([x, y])] = 0
            x += 1
        elif turn[2] == "d":
            while y + 1 < max_y():
                y += 1
                if not [x, y] in events_coordinates:
                    events.append(10)
                    events_coordinates.append([x, y])
                    events_heights.append(0)
                else:
                    events_heights[events_coordinates.index([x, y])] = 0
            y += 1
        elif turn[2] == "l":
            while x - 1 > 0:
                x -= 1
                if not [x, y] in events_coordinates:
                    events.append(10)
                    events_coordinates.append([x, y])
                    events_heights.append(0)
                else:
                    events_heights[events_coordinates.index([x, y])] = 0
            x -= 1
        elif turn[2] == "u":
            while y - 1 > 0:
                y -= 1
                if not [x, y] in events_coordinates:
                    events.append(10)
                    events_coordinates.append([x, y])
                    events_heights.append(0)
                else:
                    events_heights[events_coordinates.index([x, y])] = 0
            y -= 1
        if not [x, y] in events_coordinates:
            events.append(12)
            events_coordinates.append([x, y])
            events_heights.append(0)
        else:
            if events[events_coordinates.index([x, y])] != 3 and events[events_coordinates.index([x, y])] != 4 and events[events_coordinates.index([x, y])] != 5:
                events[events_coordinates.index([x, y])] = 12
            events_heights[events_coordinates.index([x, y])] = 0

    if area_id == 2:
        counter = 0
        while True:
            counter += 1
            new_tile_coords = choice(events_coordinates)
            if events[events_coordinates.index(new_tile_coords)] == 0 or counter > 1000:
                break
        events[events_coordinates.index(new_tile_coords)] = 15
    
    while events.count(14) > remnants_spawns[area_id][1]:
        events[events.index(14)] = 2
    while events.count(13) > 1:
        events[events.index(13)] = 0
    while events.count(11) > 1:
        events[events.index(11)] = 0
    while events.count(3) > 1:
        events[events.index(3)] = 0
    while events.count(5) > 1:
        events[events.index(5)] = 0

    if speedrunner:
        speed_timer = round((events.count(1) * 2 + events.count(2)) * 0.85)

def map_print():
    global game_time
    global speedrunner
    global speed_timer
    global eclipse
    global weather_amount
    global current_weather
    global player_oxygen
    global player_oxygen_danger
    global area_id
    global water_level
    print("AREA:" + area_color() + " The", areas[area_id] + "\033[0m")
    print("TIME: ", end = "")
    if area_id == 2 or area_id == 6:
        print("Unknown", end = "")
    elif game_time < 6:
        print("Morning", end = "")
    elif game_time < 12:
        print("Day", end = "")
    elif game_time < 18:
        print("Evening", end = "")
    else:
        print("Night", end = "")
    if eclipse:
        print(", \033[38;2;200;150;50mEclipse\033[0m", end = "")
    print()
    if speedrunner:
        if speed_timer > 0:
            print("\033[38;2;255;0;0mTIME LEFT:", speed_timer, "\033[0m")
        else:
            print("\033[38;2;255;0;0mTIME LEFT: too late...\033[0m")
    if weather_amount > 0:
        print("WEATHER: ", end = "")
        counter = 0
        for i in current_weather:
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
    print("OXYGEN:" + water_color(), end = "")
    if player_oxygen > 0:
        for i in range(math.floor(player_oxygen)):
            print("•", end = "")
    else:
        for i in range(math.floor(abs(player_oxygen))):
            print("\033[38;2;255;0;0m○", end = "")
    if player_oxygen_danger:
        print("\033[38;2;255;0;0m!")
    print("\033[0m")
    print("MAP:" + area_color())
    for x in range(min_x(), max_x() + 1):
        print("-", end = "")
    print()
    for y in range(min_y(), max_y()+1):
        for x in range(min_x(), max_x()+1):
            if [x, y] == player_coordinates and player_boat == False:
                print("\033[33;1mP" + area_color(), end = "")
            elif [x, y] == player_coordinates and player_boat == True:
                print("\033[33;1mb" + area_color(), end = "")
            elif not [x, y] in events_coordinates:
                print(" ", end = "")
            else:
                event = events[events_coordinates.index([x, y])]
                event_height = events_heights[events_coordinates.index([x, y])]
                if event in [0, 9, 25, 26]:
                    if water_level > event_height:
                        print(water_color() + "~", end = "")
                    elif area_id == 2 or area_id == 6 or eclipse:
                        print(area_color(event_height, True) + "○", end = "")
                    elif game_time < 18:
                        print(area_color(event_height, True) + "•", end = "")
                    else:
                        print(area_color(event_height, True) + "○", end = "")
                elif event == 1:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "×", end = "")
                        else:
                            print(area_color(event_height, True) + "×", end = "")
                elif event == 2:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "†", end = "")
                        else:
                            print(area_color(event_height, True) + "†", end = "")
                elif event == 3:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "$", end = "")
                        else:
                            print(area_color(event_height, True) + "$", end = "")
                elif event == 4:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "B", end = "")
                        else:
                            print(area_color(event_height, True) + "B", end = "")
                elif event == 5:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "⌂", end = "")
                        else:
                            print(area_color(event_height, True) + "⌂", end = "")
                elif event == 6:
                    if water_level > event_height:
                        print(water_color() + "~", end = "")
                    else:
                        print(area_color(event_height, True) + "~", end = "")
                elif event == 7:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "Λ", end = "")
                        else:
                            print(area_color(event_height, True) + "Λ", end = "")
                elif event == 8:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "A", end = "")
                        else:
                            print(area_color(event_height, True) + "A", end = "")
                elif event == 10:
                    if water_level > event_height:
                        print(water_color(1) + "~", end = "")
                    else:
                        print(" ", end = "")
                elif event == 11:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "D", end = "")
                        else:
                            print(area_color(event_height, True) + "D", end = "")
                elif event == 12:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "E", end = "")
                        else:
                            print(area_color(event_height, True) + "E", end = "")
                elif event == 13:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "C", end = "")
                        else:
                            print(area_color(event_height, True) + "C", end = "")
                elif event == 14:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "P", end = "")
                        else:
                            print(area_color(event_height, True) + "P", end = "")
                elif event == 15:
                    if water_level > event_height:
                        print("\033[38;2;255;50;255m~", end = "")
                    else:
                        print("\033[38;2;255;50;255m•", end = "")
                elif event in [16, 17, 27, 28]:
                    if water_level > event_height:
                        print("\033[38;2;200;0;200m~", end = "")
                    else:
                        print("\033[38;2;200;0;200m•", end = "")
                elif event in [18, 19, 20]:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        print("\033[38;2;255;50;255mΛ", end = "")
                elif event in [21, 22, 23]:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        print("\033[38;2;255;50;255m†", end = "")
                elif event == 24:
                    if 2 in current_weather:
                        if water_level > event_height:
                            print(water_color() + "?", end = "")
                        else:
                            print(area_color(event_height, True) + "?", end = "")
                    else:
                        if water_level > event_height:
                            print(water_color() + "a", end = "")
                        else:
                            print(area_color(event_height, True) + "a", end = "")

        print("\n" + water_color(), end = "")
    for x in range(min_x(), max_x() + 1):
        print("-", end = "")
    print("\033[0m")

def max_x():
    cur_max = 0
    for i in events_coordinates:
        if cur_max < i[0]:
            cur_max = i[0]
    return cur_max

def min_x():
    cur_min = 0
    for i in events_coordinates:
        if cur_min > i[0]:
            cur_min = i[0]
    return cur_min

def max_y():
    cur_max = 0
    for i in events_coordinates:
        if cur_max < i[1]:
            cur_max = i[1]
    return cur_max

def min_y():
    cur_min = 0
    for i in events_coordinates:
        if cur_min > i[1]:
            cur_min = i[1]
    return cur_min

def map_movement():
    global game_time
    global player_xp
    global player_money
    global lost
    global win
    global score
    global score_increase
    global area_id
    global current_weather
    global current_weather_duration
    global max_power_level
    global max_power_level_increase
    global player_extra_life
    global player_spent_life
    global evolution
    global cur_shopkeeper_dead
    global forest_enemy_spawn
    global water_level
    global player_oxygen
    global player_oxygen_danger
    global player_hp_penalty
    global player_def_penalty
    global player_boat
    global player_spent_life
    global death_defeated
    player_oxygen = 3
    player_hp_penalty = 0
    player_def_penalty = 0
    while True:
        if player_coordinates in events_coordinates:
            event = events[events_coordinates.index(player_coordinates)]
            current_height = events_heights[events_coordinates.index(player_coordinates)]
        else:
            print("You are somehow out of bounds!")
            event = 0
        if current_height < water_level and player_boat == False:
            player_oxygen -= 1
            if player_oxygen < 0:
                player_hp_penalty += 0.01
                player_oxygen_danger = True
            if area_id == 6:
                player_def_penalty += 1
                player_hp_penalty += 0.02
                player_oxygen_danger = True
            if player_oxygen < -3:
                player_oxygen = -3
        else:
            player_oxygen += 1.5
            if player_oxygen > 3:
                player_oxygen = 3
            player_oxygen_danger = False
        if cur_shopkeeper_dead == True:
            while 3 in events:
                events[events.index(3)] = 0
        if event in [0, 9, 15, 16, 17, 25, 26, 27, 28]:
            print()
        elif event == 1:
            fight(fight_choose())
            max_power_level = round(max_power_level * 1.0175, 2)
            max_power_level_increase += 1
            #score_increase += 0.9
            if lost == 1 and player_extra_life < 1:
                break
            elif lost == 1 and player_extra_life > 0:
                player_spent_life += 1
                player_extra_life -= 1
                score -= 2
                score_increase += 2
                player_money = 0
                player_xp = 0
                lost = 0
                print("\033[31;3mYou lost one of your lives. But you refuse to die...\033[0m\n\n\n")
            #if evolution == True:
                #evolve()
            level_up()
            if game_mode in ["infinite", "story"]:
                events[events_coordinates.index(player_coordinates)] = 0
            elif game_mode == "raid":
                events[events_coordinates.index(player_coordinates)] = 25
            time_events(2)
        elif event == 2:
            stats_altar()
            if game_mode in ["infinite", "story"]:
                events[events_coordinates.index(player_coordinates)] = 0
            elif game_mode == "raid":
                events[events_coordinates.index(player_coordinates)] = 26
            time_events(1)
        elif event == 3:
            shop()
        elif event == 4:
            fight(bossfight_choose(), ally_choose())
            max_power_level = round(max_power_level * 1.0175, 2)
            max_power_level_increase += 1
            if lost == 1 and player_extra_life < 1:
                break
            elif lost == 1 and player_extra_life > 0:
                player_spent_life += 1
                player_extra_life -= 1
                score -= 2
                score_increase += 2
                player_money = 0
                player_xp = 0
                lost = 0
                print("\033[31;3mYou lost one of your lives. But you refuse to die...\033[0m\n\n\n")
            else:
                boss_upgrade()
            if evolution == True:
                evolve()
            level_up()
            if game_mode == "raid":
                events[events_coordinates.index(player_coordinates)] = 25
                time_events(0)
            elif game_mode in ["infinite", "story"]:
                break
        elif event == 5:
            mimic_gamble()
        elif event == 6:
            print()
            events[events_coordinates.index(player_coordinates)] = 0
            time_events(1)
        elif event == 7:
            fight(fight_choose(0.6))
            max_power_level = round(max_power_level * 1.0175, 2)
            max_power_level_increase += 1
            #score_increase += 0.9
            if lost == 1 and player_extra_life < 1:
                break
            elif lost == 1 and player_extra_life > 0:
                player_spent_life += 1
                player_extra_life -= 1
                score -= 2
                score_increase += 2
                player_money = 0
                player_xp = 0
                lost = 0
                print("\033[31;3mYou lost one of your lives. But you refuse to die...\033[0m\n\n\n")
            #if evolution == True:
                #evolve()
            level_up()
            events[events_coordinates.index(player_coordinates)] = 9
            time_events(2)
        elif event == 8:
            fight(fight_choose(1.2))
            max_power_level = round(max_power_level * 1.0175, 2)
            max_power_level_increase += 1
            #score_increase += 0.9
            if lost == 1 and player_extra_life < 1:
                break
            elif lost == 1 and player_extra_life > 0:
                player_spent_life += 1
                player_extra_life -= 1
                score -= 2
                score_increase += 2
                player_money = 0
                player_xp = 0
                lost = 0
                print("\033[31;3mYou lost one of your lives. But you refuse to die...\033[0m\n\n\n")
            #if evolution == True:
                #evolve()
            level_up()
            events[events_coordinates.index(player_coordinates)] = 9
            time_events(3)
        elif event == 11:
            if death_defeated == False and player_spent_life > 0:
                print('''You approach the masked creature again. She speaks threateningly,
\033[38;2;100;100;100m"Perhaps, you do not appreciate what I do. Everyone that who is killed has to die. And you should be no exception."\033[0m
You ready yourself for the fight...
Type anything to continue''')
                action = input()
                score -= 5
                fight([51])
                if lost == 1:
                    player_spent_life += player_extra_life + 1
                    player_extra_life = 0
                    break
                else:
                    score += 5
                    death_defeated = True
                    print('''The masked creature, stands up again.
\033[38;2;100;100;100m"Your kind is so persistent. They keep continuing the cycle. But I feel that you are attempting to change that."\033[0m
She pauses for a moment, \033[38;2;100;100;100m"Perhaps, we are in the same \033[38;2;100;100;100;3mboat\033[0m\033[38;2;100;100;100m? Meet me later."\033[0m
The creature crawls away. You decide to continue your journey...
Type anything to continue''')
                    action = input()
            else:
                death_boat()
            events[events_coordinates.index(player_coordinates)] = 0
            time_events(2)
        elif event == 12:
            escape()
            if escaped == True:
                if evolution == True:
                    evolve()
                break
        elif event == 13:
            change_interaction()
        elif event == 14:
            player_remnants()
            time_events(1)
            if game_mode in ["infinite", "story"]:
                events[events_coordinates.index(player_coordinates)] = 0
            elif game_mode == "raid":
                events[events_coordinates.index(player_coordinates)] = 26
        elif event in [18, 19, 20]:
            fight(fight_choose(0.9))
            max_power_level = round(max_power_level * 1.0175, 2)
            max_power_level_increase += 1
            #score_increase += 0.9
            if lost == 1 and player_extra_life < 1:
                break
            elif lost == 1 and player_extra_life > 0:
                player_spent_life += 1
                player_extra_life -= 1
                score -= 2
                score_increase += 2
                player_money = 0
                player_xp = 0
                lost = 0
                print("\033[31;3mYou lost one of your lives. But you refuse to die...\033[0m\n\n\n")
            #if evolution == True:
                #evolve()
            level_up()
            if game_mode in ["infinite", "story"]:
                events[events_coordinates.index(player_coordinates)] = 15
            elif game_mode == "raid":
                events[events_coordinates.index(player_coordinates)] = 27
            time_events(2)
        elif event in [21, 22, 23]:
            fight(fight_choose(-0.3))
            if lost == 1 and player_extra_life < 1:
                break
            elif lost == 1 and player_extra_life > 0:
                player_spent_life += 1
                player_extra_life -= 1
                score -= 2
                score_increase += 2
                player_money = 0
                player_xp = 0
                lost = 0
                print("\033[31;3mYou lost one of your lives. But you refuse to die...\033[0m\n\n\n")
                stats_altar()
            else:
                stats_altar()
            if game_mode in ["infinite", "story"]:
                events[events_coordinates.index(player_coordinates)] = 15
            elif game_mode == "raid":
                events[events_coordinates.index(player_coordinates)] = 28
            time_events(1)
        elif event == 24:
            alchemist_shop()
        map_print()
        print('''\nWhere do you want to move?
W. ↑
A. ←
D. →
S. ↓
I. - inventory
H. - Map Help''')
        while True:
            action = input()
            if action.lower() == "w" or action.lower() == "up":
                if [player_coordinates.copy()[0], player_coordinates.copy()[1] - 1] in events_coordinates and (events[events_coordinates.index([player_coordinates.copy()[0], player_coordinates.copy()[1] - 1])] != 10 or (player_boat == True and water_level > 0)):
                    player_coordinates[1] -= 1
                    break
                else:
                    print("You can't move there!")
            if action.lower() == "a" or action.lower() == "left":
                if [player_coordinates.copy()[0] - 1, player_coordinates.copy()[1]] in events_coordinates and (events[events_coordinates.index([player_coordinates.copy()[0] - 1, player_coordinates.copy()[1]])] != 10 or (player_boat == True and water_level > 0)):
                    player_coordinates[0] -= 1
                    break
                else:
                    print("You can't move there!")
            if action.lower() == "d" or action.lower() == "right":
                if [player_coordinates.copy()[0] + 1, player_coordinates.copy()[1]] in events_coordinates and (events[events_coordinates.index([player_coordinates.copy()[0] + 1, player_coordinates.copy()[1]])] != 10 or (player_boat == True and water_level > 0)):
                    player_coordinates[0] += 1
                    break
                else:
                    print("You can't move there!")
            if action.lower() == "s" or action.lower() == "down":
                if [player_coordinates.copy()[0], player_coordinates.copy()[1] + 1] in events_coordinates and (events[events_coordinates.index([player_coordinates.copy()[0], player_coordinates.copy()[1] + 1])] != 10 or (player_boat == True and water_level > 0)):
                    player_coordinates[1] += 1
                    break
                else:
                    print("You can't move there!")
            if action.lower() == "i" or action.lower() == "inventory":
                print("\033[33;1mYour weapon -", weapon_names[player_weapon])
                if len(player_items) > 0:
                    counter = 0
                    print("Consumables:")
                    for i in player_items:
                        counter += 1
                        print(str(counter) + ".", consumable_item_names[i])
                inventory_statistics()
                print("\033[0m", end = "")
            if action.lower() == "h" or "map" in action.lower() or "help" in action.lower():
                if player_boat == False:
                    print('''Yellow \033[33;1mP\033[0m is you. You can move freely on circles.
Other symbols act differently when stepped on. Note that when you leave the area, you cannot come back...''')
                else:
                    print('''Yellow \033[33;1mb\033[0m is you. You can move freely on circles and tildas.
Other symbols act differently when stepped on. Note that when you leave the area, you cannot come back...''')
            if "restart" in action.lower():
                print('''Are you sure you want to restart? You will not be able to continue this run.
Type in the action
1. No
2. Yes''')
                action = input()
                if action == "2" or action.lower() == "yes":
                    lost = 1
                    break
        if lost == 1:
            break

def time_events(num = 0):
    global game_time
    global forest_enemy_spawn
    global enough_destroyed
    global current_weather
    global current_weather_duration
    global water_level
    global area_id
    global eclipse
    global weather_seed
    global weather_effects_seed
    global map_seed
    global speedrunner
    global speed_timer
    global difficulty
    game_time += num
    too_much = False
    if speedrunner:
        speed_timer -= num
        if speed_timer <= 0:
            difficulty += 3 * num
    if (eclipse or game_time > 12) and forest_enemy_spawn < 3 and area_id == 1:
        node = randint(0, len(events) - 1)
        if (events[node] == 0 or events[node] == 6) and events_coordinates[node] != player_coordinates:
            events[node] = 1
            forest_enemy_spawn += 1

    raid_mode_reset()

    if 15 in events or 19 in events or 22 in events or 27 in events or 28 in events:
        for node_coordinates in events_coordinates:
            if events[events_coordinates.index(node_coordinates)] in [15, 19, 22, 27, 28]:
                new_coordinates = [node_coordinates[0], node_coordinates[1] - 1]
                if new_coordinates in events_coordinates:
                    if events[events_coordinates.index(new_coordinates)] in [0, 6]:
                        events[events_coordinates.index(new_coordinates)] = 17
                    elif events[events_coordinates.index(new_coordinates)] in [1, 7, 8, 9]:
                        events[events_coordinates.index(new_coordinates)] = 18
                    elif events[events_coordinates.index(new_coordinates)] in [2]:
                        events[events_coordinates.index(new_coordinates)] = 21
                    elif events[events_coordinates.index(new_coordinates)] in [25]:
                        events[events_coordinates.index(new_coordinates)] = 27
                    elif events[events_coordinates.index(new_coordinates)] in [26]:
                        events[events_coordinates.index(new_coordinates)] = 28
                new_coordinates = [node_coordinates[0] + 1, node_coordinates[1]]
                if new_coordinates in events_coordinates:
                    if events[events_coordinates.index(new_coordinates)] in [0, 6]:
                        events[events_coordinates.index(new_coordinates)] = 17
                    elif events[events_coordinates.index(new_coordinates)] in [1, 7, 8, 9]:
                        events[events_coordinates.index(new_coordinates)] = 18
                    elif events[events_coordinates.index(new_coordinates)] in [2]:
                        events[events_coordinates.index(new_coordinates)] = 21
                    elif events[events_coordinates.index(new_coordinates)] in [25]:
                        events[events_coordinates.index(new_coordinates)] = 27
                    elif events[events_coordinates.index(new_coordinates)] in [26]:
                        events[events_coordinates.index(new_coordinates)] = 28
                new_coordinates = [node_coordinates[0], node_coordinates[1] + 1]
                if new_coordinates in events_coordinates:
                    if events[events_coordinates.index(new_coordinates)] in [0, 6]:
                        events[events_coordinates.index(new_coordinates)] = 17
                    elif events[events_coordinates.index(new_coordinates)] in [1, 7, 8, 9]:
                        events[events_coordinates.index(new_coordinates)] = 18
                    elif events[events_coordinates.index(new_coordinates)] in [2]:
                        events[events_coordinates.index(new_coordinates)] = 21
                    elif events[events_coordinates.index(new_coordinates)] in [25]:
                        events[events_coordinates.index(new_coordinates)] = 27
                    elif events[events_coordinates.index(new_coordinates)] in [26]:
                        events[events_coordinates.index(new_coordinates)] = 28
                new_coordinates = [node_coordinates[0] - 1, node_coordinates[1]]
                if new_coordinates in events_coordinates:
                    if events[events_coordinates.index(new_coordinates)] in [0, 6]:
                        events[events_coordinates.index(new_coordinates)] = 17
                    elif events[events_coordinates.index(new_coordinates)] in [1, 7, 8, 9]:
                        events[events_coordinates.index(new_coordinates)] = 18
                    elif events[events_coordinates.index(new_coordinates)] in [2]:
                        events[events_coordinates.index(new_coordinates)] = 21
                    elif events[events_coordinates.index(new_coordinates)] in [25]:
                        events[events_coordinates.index(new_coordinates)] = 27
                    elif events[events_coordinates.index(new_coordinates)] in [26]:
                        events[events_coordinates.index(new_coordinates)] = 28

                if events[events_coordinates.index(node_coordinates)] == 15:
                    events[events_coordinates.index(node_coordinates)] = 16
                elif events[events_coordinates.index(node_coordinates)] == 19:
                    events[events_coordinates.index(node_coordinates)] = 20
                elif events[events_coordinates.index(node_coordinates)] == 21:
                    events[events_coordinates.index(node_coordinates)] = 22
    if 17 in events or 18 in events:
        for i in range(len(events)):
            if events[i] == 17:
                events[i] = 15
            elif events[i] == 18:
                events[i] = 19
            elif events[i] == 21:
                events[i] = 22

    if game_time > 23:
        game_time -= 24
        forest_enemy_spawn = 0
        shop_items_define()
        if area_id == 4 and enough_destroyed == False:
            shop_coord_y, boss_coord_y, player_coord_y = events_coordinates[events.index(3)][1], events_coordinates[events.index(4)][1], player_coordinates[1]
            if 5 in events:
                mimic_coord_y = events_coordinates[events.index(5)][1]
            else:
                mimic_coord_y = 0
            if 11 in events:
                death_coord_y = events_coordinates[events.index(11)][1]
            else:
                death_coord_y = 0
            if 24 in events:
                alchemist_coord_y = events_coordinates[events.index(24)][1]
            else:
                alchemist_coord_y = 0
            event_deletions = []
            if not max_y() == player_coord_y:
                if not max_y() in [mimic_coord_y, shop_coord_y, death_coord_y, boss_coord_y, alchemist_coord_y] or game_mode == "raid":
                    for i in range(len(events_coordinates)):
                        if events_coordinates[i][1] == max_y():
                            event_deletions.append(i)
                    counter = 0
                    for i in event_deletions:
                        del events[i - counter]
                        del events_coordinates[i - counter]
                        del events_heights[i - counter]
                        counter += 1
                else:
                    enough_destroyed = True
    seed(weather_seed)
    for r in range(len(current_weather)):
        if current_weather[r] == 0:
            if chance(weather_chance[area_id]) and current_weather_duration[r] <= 0:
                if len(weathers[area_id]) > 0:
                    current_weather[r] = choice(weathers[area_id])
                    current_weather_duration[r] = randint(weathers_durations[current_weather[r]][0], weathers_durations[current_weather[r]][1])
                else:
                    current_weather[r] = 0
                    current_weather_duration[r] = randint(weathers_durations[current_weather[r]][0], weathers_durations[current_weather[r]][1])
            else:
                current_weather_duration[r] -= num
            weather_seed = randint(0, 10000)
        elif current_weather[r] == 1:
            if current_weather_duration[r] <= 0:
                current_weather[r] = 0
                current_weather_duration[r] = randint(weathers_durations[current_weather[r]][0], weathers_durations[current_weather[r]][1])
            else:
                seed(weather_effects_seed)
                for i in range(num):
                    node = randint(0, len(events) - 1)
                    if (events[node] == 0) and events_coordinates[node] != player_coordinates:
                        events[node] = 6
                current_weather_duration[r] -= num
                weather_effects_seed = randint(0, 10000)
        elif current_weather[r] == 2:
            if current_weather_duration[r] <= 0:
                current_weather[r] = 0
                current_weather_duration[r] = randint(weathers_durations[current_weather[r]][0], weathers_durations[current_weather[r]][1])
            else:
                seed(weather_effects_seed)
                for i in range(num):
                    if 1 in events:
                        node1 = 0
                        while events[node1] != 1:
                            node1 = randint(0, len(events) - 1)
                        events[node1] = 2
                        swapped = 1
                    else:
                        swapped = 0
                        node1 = 0
                    if events.count(2) > swapped:
                        node2 = 0
                        while events[node2] != 2 or node2 == node1:
                            node2 = randint(0, len(events) - 1)
                        events[node2] = 1
                weather_effects_seed = randint(0, 10000)
                current_weather_duration[r] -= num
        elif current_weather[r] == 3:
            if current_weather_duration[r] <= 0:
                current_weather[r] = 0
                current_weather_duration[r] = randint(weathers_durations[current_weather[r]][0], weathers_durations[current_weather[r]][1])
            else:
                seed(map_seed)
                for i in range(num):
                    iteration = 0
                    while True:
                        iteration += 1
                        if iteration > 999:
                            too_much = True
                        if too_much:
                            break
                        x = randint(min_x(), max_x())
                        y = randint(min_y(), max_y())
                        h_neighbors = 0
                        v_neighbors = 0
                        d_neighbors = 0
                        heights = 0
                        if [x, y] in events_coordinates:
                            continue
                        else:
                            if [x + 1, y + 1] in events_coordinates and events[events_coordinates.index([x + 1, y + 1])] != 10:
                                d_neighbors += 1
                                heights += events_heights[events_coordinates.index([x + 1, y + 1])]
                            if [x, y + 1] in events_coordinates and events[events_coordinates.index([x, y + 1])] != 10:
                                v_neighbors += 1
                                heights += events_heights[events_coordinates.index([x, y + 1])]
                            if [x - 1, y + 1] in events_coordinates and events[events_coordinates.index([x - 1, y + 1])] != 10:
                                d_neighbors += 1
                                heights += events_heights[events_coordinates.index([x - 1, y + 1])]
                            if [x + 1, y] in events_coordinates and events[events_coordinates.index([x + 1, y])] != 10:
                                h_neighbors += 1
                                heights += events_heights[events_coordinates.index([x + 1, y])]
                            if [x - 1, y] in events_coordinates and events[events_coordinates.index([x - 1, y])] != 10:
                                h_neighbors += 1
                                heights += events_heights[events_coordinates.index([x - 1, y])]
                            if [x + 1, y - 1] in events_coordinates and events[events_coordinates.index([x + 1, y - 1])] != 10:
                                d_neighbors += 1
                                heights += events_heights[events_coordinates.index([x + 1, y - 1])]
                            if [x, y - 1] in events_coordinates and events[events_coordinates.index([x, y - 1])] != 10:
                                v_neighbors += 1
                                heights += events_heights[events_coordinates.index([x, y - 1])]
                            if [x - 1, y - 1] in events_coordinates and events[events_coordinates.index([x - 1, y - 1])] != 10:
                                d_neighbors += 1
                                heights += events_heights[events_coordinates.index([x - 1, y - 1])]
                            if v_neighbors + h_neighbors < 1:
                                continue
                            elif v_neighbors > 0 and h_neighbors > 0 and d_neighbors > 0:
                                continue
                            else:
                                break
                    if iteration < 1000:
                        #print(v_neighbors, h_neighbors, d_neighbors)
                        if chance(0.7):
                            events.append(0)
                        elif chance(0.5):
                            events.append(9)
                        elif chance(0.5):
                            events.append(25)
                        else:
                            events.append(26)
                        events_coordinates.append([x, y])
                        if h_neighbors + v_neighbors + d_neighbors > 0:
                            events_heights.append(heights // (h_neighbors + v_neighbors + d_neighbors))
                        else:
                            events_heights.append(heights)
                current_weather_duration[r] -= num
        elif current_weather[r] == 4:
            if current_weather_duration[r] <= 0:
                current_weather[r] = 0
                current_weather_duration[r] = randint(weathers_durations[current_weather[r]][0], weathers_durations[current_weather[r]][1])
            else:
                seed(weather_effects_seed)
                for i in range(num):
                    iteration = 0
                    while True:
                        iteration += 1
                        if iteration > 999:
                            break
                        node = randint(0, len(events) - 1)
                        if events[node] == 9:
                            events[node] = 7
                        elif events[node] == 7:
                            events[node] = 8
                        else:
                            continue
                        break
                weather_effects_seed = randint(0, 10000)
                current_weather_duration[r] -= num
        elif current_weather[r] == 5:
            if current_weather_duration[r] <= 0:
                current_weather[r] = 0
                current_weather_duration[r] = randint(weathers_durations[current_weather[r]][0], weathers_durations[current_weather[r]][1])
            else:
                seed(map_seed)
                for k in range(num * 4):
                    for i in range(len(events)):
                        if events[i] == 1:
                            directions = ["u", "r", "d", "l"]
                            coordinates = events_coordinates[i]
                            while len(directions) > 0:
                                direction = choice(directions)
                                if direction == "u":
                                    directions.remove("u")
                                    new_coordinates = [coordinates[0], coordinates[1] - 1]
                                    if new_coordinates in events_coordinates:
                                        if events[events_coordinates.index(new_coordinates)] == 0 or events[events_coordinates.index(new_coordinates)] == 6:
                                            events[events_coordinates.index(new_coordinates)] = 1
                                            events[i] = 0
                                            break
                                elif direction == "r":
                                    directions.remove("r")
                                    new_coordinates = [coordinates[0] + 1, coordinates[1]]
                                    if new_coordinates in events_coordinates:
                                        if events[events_coordinates.index(new_coordinates)] == 0 or events[events_coordinates.index(new_coordinates)] == 6:
                                            events[events_coordinates.index(new_coordinates)] = 1
                                            events[i] = 0
                                            break
                                elif direction == "l":
                                    directions.remove("l")
                                    new_coordinates = [coordinates[0] - 1, coordinates[1]]
                                    if new_coordinates in events_coordinates:
                                        if events[events_coordinates.index(new_coordinates)] == 0 or events[events_coordinates.index(new_coordinates)] == 6:
                                            events[events_coordinates.index(new_coordinates)] = 1
                                            events[i] = 0
                                            break
                                elif direction == "d":
                                    directions.remove("d")
                                    new_coordinates = [coordinates[0], coordinates[1] + 1]
                                    if new_coordinates in events_coordinates:
                                        if events[events_coordinates.index(new_coordinates)] == 0 or events[events_coordinates.index(new_coordinates)] == 6:
                                            events[events_coordinates.index(new_coordinates)] = 1
                                            events[i] = 0
                                            break
                current_weather_duration[r] -= num
        elif current_weather[r] == 6:
            if current_weather_duration[r] <= 0:
                current_weather[r] = 0
                current_weather_duration[r] = randint(weathers_durations[current_weather[r]][0], weathers_durations[current_weather[r]][1])
            else:
                current_weather_duration[r] -= num
        elif current_weather[r] == 7:
            if current_weather_duration[r] <= 0:
                current_weather[r] = 0
                current_weather_duration[r] = randint(weathers_durations[current_weather[r]][0], weathers_durations[current_weather[r]][1])
            else:
                try:
                    current_weather_duration[r] -= num
                except:
                    num
        elif current_weather[r] == 8:
            if current_weather_duration[r] <= 0:
                current_weather[r] = 0
                current_weather_duration[r] = randint(weathers_durations[current_weather[r]][0], weathers_durations[current_weather[r]][1])
            else:
                water_level += num / 4
                if water_level > 5:
                    water_level = 5
                current_weather_duration[r] -= num
        elif current_weather[r] == 9:
            if current_weather_duration[r] <= 0:
                current_weather[r] = 0
                current_weather_duration[r] = randint(weathers_durations[current_weather[r]][0], weathers_durations[current_weather[r]][1])
            else:
                water_level -= num / 5
                if water_level > 0:
                    water_level = 0
                current_weather_duration[r] -= num

    seed(weather_seed)
    if not 8 in current_weather and not 6 in current_weather and not 1 in current_weather:
        if water_level > default_water_levels[area_id]:
            water_level -= randint(1, num + 1) * 0.5
            if water_level < default_water_levels[area_id]:
                water_level = default_water_levels[area_id]
    if not 9 in current_weather:
        if water_level < default_water_levels[area_id]:
            water_level += randint(1, num + 1) * 0.5
            if water_level > default_water_levels[area_id]:
                water_level = default_water_levels[area_id]

def infinite_mode():
    global area
    global area_id
    global player_travel
    global player_xp
    global player_money
    global lost
    global win
    global score_increase
    global score
    global difficulty
    global water_level
    global map_complexity
    global max_power_level
    global player_extra_life
    global player_spent_life
    global evolution
    global mimic_got_item
    global game_time
    global forest_enemy_spawn
    global enough_destroyed
    global weather_amount
    global current_weather
    global current_weather_duration
    global mimic_given_items
    global player_boat
    global escaped
    global game_mode # very important
    game_mode = "infinite"
    area_id = 0
    areas_visited = 0
    while True:
        if areas_visited > 7:
            difficulty += 10
        for k in range(len(hunters_appeared)):
            hunters_appeared[k] = False
        areas_visited += 1
        score += int(score_increase)
        score_increase = 0
        shop_items_define()
        current_weather = []
        current_weather_duration = []
        for i in range(weather_amount):
            current_weather.append(0)
            current_weather_duration.append(0)
        area = areas[area_id]
        print(area_color() + "You have entered the", area + "\033[0m")
        game_time = 0
        if player_travel > 0:
            player_xp += round(xp_to_lvl_up() * player_travel / 100)
            print("You gained\033[38;2;100;0;200m", round(xp_to_lvl_up() * player_travel / 100), "XP\033[0m for entering a new area!")
        level_up()
        mimic_got_item = False
        mimic_given_items = 0
        forest_enemy_spawn = 0
        enough_destroyed = False
        water_level = default_water_levels[area_id]
        player_boat = False
        map_generation()
        escaped = False
        map_movement()
        if lost == 1:
            break
        if escaped == False:
            area_id += 1
        else:
            area_id += 3
        if area_id >= len(areas):
            area_id -= len(areas)
        map_complexity += 2
    print("\033[31;3mYou lost it all...\033[0m\n")
    final_statistics()

def story_mode():
    global area
    global area_id
    global player_travel
    global player_xp
    global player_money
    global lost
    global win
    global score_increase
    global score
    global difficulty
    global water_level
    global map_complexity
    global max_power_level
    global player_extra_life
    global player_spent_life
    global evolution
    global mimic_got_item
    global game_time
    global forest_enemy_spawn
    global enough_destroyed
    global weather_amount
    global current_weather
    global current_weather_duration
    global mimic_given_items
    global player_boat
    global escaped
    global game_mode # very important
    global final_area
    game_mode = "story"
    area_id = 0
    i = 0
    while i in range(8):
        for k in range(len(hunters_appeared)):
            hunters_appeared[k] = False
        score += int(score_increase)
        score_increase = 0
        shop_items_define()
        current_weather = []
        current_weather_duration = []
        for r in range(weather_amount):
            current_weather.append(0)
            current_weather_duration.append(0)
        area = areas[area_id]
        print(area_color() + "You have entered the", area + "\033[0m")
        game_time = 0
        if player_travel > 0:
            player_xp += round(xp_to_lvl_up() * player_travel / 100)
            print("You gained\033[38;2;100;0;200m", round(xp_to_lvl_up() * player_travel / 100), "XP\033[0m for entering a new area!")
        level_up()
        mimic_got_item = False
        mimic_given_items = 0
        forest_enemy_spawn = 0
        enough_destroyed = False
        water_level = default_water_levels[area_id]
        player_boat = False
        map_generation()
        escaped = False
        map_movement()
        i += 1
        if lost == 1:
            break
        if escaped == False:
            area_id += 1
        else:
            area_id += 3
            i += 2
            if i > 7:
                i = 7
        if area_id >= len(areas):
            area_id = 0
            final_area = True
        map_complexity += 1
    if lost == 1:
        print("\033[31;3mYou lost it all...\033[0m\n")
    else:
        print("\033[33;3mYou have won...\033[0m\n")
    final_statistics()

def raid_mode_area_choose():
    print('''Choose an area.''')
    for k in range(7):
        print( end = "")
        if TD_area_unlocks[k] == False:
            print("\033[0m" + str(k+1) + ". Locked")
        else:
            print(represented_area_color(k) + str(k+1) + ". " + areas[k], "\033[0m- Survived", TD_max_raids[k], "raids.")
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
                if False in TD_area_unlocks:
                    print("In order to unlock some of the next areas you can:")
                    if TD_area_unlocks[2] == False:
                        print("Survive 2 raids in " + represented_area_color(1) + "the Deep Forest\033[0m.")
                        print("Survive 3 raids in " + represented_area_color(0) + "the Garden\033[0m.")
                    if TD_area_unlocks[3] == False:
                        if TD_area_unlocks[2]:
                            print("Survive 3 raids in " + represented_area_color(2) + "the Cave\033[0m.")
                    if TD_area_unlocks[4] == False:
                        if TD_area_unlocks[3]:
                            print("Survive 4 raids in " + represented_area_color(3) + "the Tundra\033[0m.")
                        if TD_area_unlocks[2]:
                            print("Survive 5 raids in " + represented_area_color(2) + "the Cave\033[0m.")
                    if TD_area_unlocks[5] == False:
                        if TD_area_unlocks[4]:
                            print("Survive 4 raids in " + represented_area_color(4) + "the Canyon\033[0m.")
                        if TD_area_unlocks[3]:
                            print("Survive 6 raids in " + represented_area_color(3) + "the Tundra\033[0m.")
                    if TD_area_unlocks[6] == False:
                        if TD_area_unlocks[5]:
                            print("Survive 7 raids in " + represented_area_color(5) + "the Desert\033[0m.")
                else:
                    print("You have unlocked every single area for raids!")
            elif action == 8:
                break

def raid_mode_reset():
    global map_seed, raid_counter, area_id, mimic_got_item, mimic_given_items, player_travel, score, score_increase, player_xp
    if not (1 in events or 4 in events or 7 in events or 8 in events or 19 in events or 20 in events) and game_mode == "raid":
        print("The raid is over. Another one begins!")
        seed(map_seed)
        map_seed = randint(0, 10000)
        raid_counter += 1
        for i in range(len(events)):
            if events[i] in [15, 16, 17]:
                events[i] = 0
            if events[i] in [25, 27]:
                events[i] = 1
            if events[i] in [3, 5, 11, 14, 24, 26, 28]:
                events[i] = 2
        min_remnant, max_remnant, avg_remnant = remnants_spawns[area_id][0], remnants_spawns[area_id][1], remnants_spawns[area_id][2]
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
        while remnant_events_amount > events.count(14):
            event = choice(range(len(events)))
            if events[event] == 2:
                events[event] = 14
        if area_id == 0:
            while not 3 in events:
                event = choice(range(len(events)))
                if events[event] in [2]:
                    events[event] = 3
        elif area_id == 1:
            while not 3 in events or not 5 in events:
                event = choice(range(len(events)))
                if events[event] in [2]:
                    if not 3 in events:
                        events[event] = 3
                    elif not 5 in events:
                        events[event] = 5
        else:
            while not 3 in events or not 5 in events or not 24 in events:
                event = choice(range(len(events)))
                if events[event] in [2]:
                    if not 3 in events:
                        events[event] = 3
                    elif not 5 in events:
                        events[event] = 5
                    elif not 24 in events:
                        events[event] = 24
        while not 4 in events or (area_id == 2 and not 15 in events):
            event = choice(range(len(events)))
            if events[event] in [1] and not 4 in events and chance(0.3):
                events[event] = 4
            elif area_id == 2 and events[event] == 0 and not 15 in events:
                events[event] = 15
        for i in range(len(hunters_appeared)):
            hunters_appeared[i] = False
        if player_travel > 0:
            player_xp += round(xp_to_lvl_up() * player_travel / 100)
            print("You gained\033[38;2;100;0;200m", round(xp_to_lvl_up() * player_travel / 100), "XP\033[0m for finishing a raid!")
        level_up()
        mimic_got_item = False
        mimic_given_items = 0
        score += int(score_increase)
        if speedrunner:
            speed_timer = round((events.count(1) * 2 + events.count(2)) * 0.95)
        if raid_counter > TD_max_raids[area_id]:
            TD_max_raids[area_id] = raid_counter
        if area_id == 0:
            if TD_area_unlocks[2] == False and raid_counter == 3:
                TD_area_unlocks[2] = True
                print("You have unlocked " + represented_area_color(2) + "the Cave!\033[0m")
        elif area_id == 1:
            if TD_area_unlocks[2] == False and raid_counter == 2:
                TD_area_unlocks[2] = True
                print("You have unlocked " + represented_area_color(2) + "the Cave!\033[0m")
        elif area_id == 2:
            if TD_area_unlocks[3] == False and raid_counter == 3:
                TD_area_unlocks[3] = True
                print("You have unlocked " + represented_area_color(3) + "the Tundra!\033[0m")
            if TD_area_unlocks[4] == False and raid_counter == 5:
                TD_area_unlocks[4] = True
                print("You have unlocked " + represented_area_color(4) + "the Canyon!\033[0m")
        elif area_id == 3:
            if TD_area_unlocks[4] == False and raid_counter == 4:
                TD_area_unlocks[4] = True
                print("You have unlocked " + represented_area_color(4) + "the Canyon!\033[0m")
            if TD_area_unlocks[5] == False and raid_counter == 6:
                TD_area_unlocks[5] = True
                print("You have unlocked " + represented_area_color(5) + "the Desert!\033[0m")
        elif area_id == 4:
            if TD_area_unlocks[5] == False and raid_counter == 4:
                TD_area_unlocks[5] = True
                print("You have unlocked " + represented_area_color(5) + "the Desert!\033[0m")
        elif area_id == 5:
            if TD_area_unlocks[6] == False and raid_counter == 7:
                TD_area_unlocks[6] = True
                print("You have unlocked " + represented_area_color(6) + "the Rotten Forest!\033[0m")
        save()
        print('''Type anything to continue...''')
        action = input()

def raid_mode(starting_area = 0):
    global area
    global area_id
    global game_mode
    global map_complexity
    global game_time
    global weather_amount
    global mimic_got_item
    global mimic_given_items
    game_mode = "raid"
    area_id = starting_area
    area = areas[area_id]
    game_time = 0
    mimic_got_item = False
    mimic_given_items = 0
    current_weather = []
    current_weather_duration = []
    shop_items_define()
    for r in range(weather_amount):
        current_weather.append(0)
        current_weather_duration.append(0)
    map_complexity = 3
    map_generation()
    map_movement()
    final_statistics()
    print("\033[31;3mYou lost it all...\033[0m\n")

def evolve():
    global evolution_seed
    evo_counter = 0
    seed(evolution_seed)
    evolution_seed = randint(0, 10000)
    for i in range(len(enemys_name)):
        if len(enemys_name) >= 1000:
            break
        if i in [4, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 51, 52, 53, 54, 64]:
            continue
        if chance(0.25):
            evo_counter += 1
            for k in range(len(bosses_for_areas)):
                if i in bosses_for_areas[k]:
                    bosses_for_areas[k].append(len(enemys_name))
            enemys_name.append(enemys_name[i] + choice(evolution_name_suffix))
            enemys_base_hp.append(enemys_base_hp[i] + round(enemys_base_hp[i] * randint(-5, 15) / 100))
            enemys_base_dmg.append(enemys_base_dmg[i] + round(enemys_base_dmg[i] * randint(-4, 13) / 100))
            enemys_base_def.append(enemys_base_def[i] + round(enemys_base_def[i] * randint(30, 65) / 100))
            enemys_base_crit.append(enemys_base_crit[i] + uniform(-0.05, 0.1))
            if enemys_base_spk[i] > 0:
                spk_add = randint(-1, 2)
            elif chance(0.1):
                spk_add = 1
            else:
                spk_add = 0
            enemys_base_spk.append(enemys_base_spk[i] + spk_add)
            if enemys_base_psn[i] > 0:
                psn_add = randint(-1, 2)
            elif chance(0.1):
                psn_add = 1
            else:
                psn_add = 0
            enemys_base_psn.append(enemys_base_psn[i] + psn_add)
            enemys_base_immortality.append(enemys_base_immortality[i])
            enemys_power_level.append(round(enemys_power_level[i] + (randint(-10, 10) / 100), 2))
            enemys_descriptions.append(enemys_descriptions[i])
            enemys_spawners.append(enemys_spawners[i].copy())
            enemys_patterns.append(enemys_patterns[i].copy())
            enemy_is_boss.append(enemy_is_boss[i])
            enemys_name_colors.append(enemys_name_colors[i].copy())
            enemys_elements.append(enemys_elements[i].copy())
            for k in range(3):
                enemys_name_colors[i][k] += randint(-15, 15)
                if enemys_name_colors[i][k] > 255:
                    enemys_name_colors[i][k] = 255
                elif enemys_name_colors[i][k] < 0:
                    enemys_name_colors[i][k] = 0

            enemy_areas.append(enemy_areas[i].copy())
            if 0 in enemy_areas[-1] and not 1 in enemy_areas[-1]:
                if chance(0.1):
                    enemy_areas[-1].append(1)
            if 1 in enemy_areas[-1] and not 0 in enemy_areas[-1]:
                if chance(0.1):
                    enemy_areas[-1].append(0)
            if 1 in enemy_areas[-1] and not 2 in enemy_areas[-1]:
                if chance(0.1):
                    enemy_areas[-1].append(2)
            if 2 in enemy_areas[-1] and not 4 in enemy_areas[-1]:
                if chance(0.1):
                    enemy_areas[-1].append(4)
            if 2 in enemy_areas[-1] and not 1 in enemy_areas[-1]:
                if chance(0.1):
                    enemy_areas[-1].append(1)
            if 4 in enemy_areas[-1] and not 5 in enemy_areas[-1]:
                if chance(0.1):
                    enemy_areas[-1].append(5)
            if 4 in enemy_areas[-1] and not 6 in enemy_areas[-1]:
                if chance(0.1):
                    enemy_areas[-1].append(6)
            if 4 in enemy_areas[-1] and not 3 in enemy_areas[-1]:
                if chance(0.1):
                    enemy_areas[-1].append(3)

    print(evo_counter, "enemies have \033[38;2;255;150;0;3mevolved...\033[0m\n\n\n")

def daily_run():
    global difficulty
    global original_difficulty
    global weather_amount
    global evolution
    global overkill
    global speedrunner
    global item_rando
    global eclipse
    global global_seed
    global daily_seed
    global map_seed
    global weather_seed
    global weather_effects_seed
    global altar_seed
    global shop_seed
    global gamble_seed
    global remnant_seed
    global enemy_encouter_seed
    global evolution_seed
    global game_mode
    seed(daily_seed)
    difficulty = randint(50, 70)
    original_difficulty = difficulty
    weather_amount = randint(1, 6)
    evolution = chance(0.4)
    overkill = chance(0.2)
    speedrunner = chance(0.4)
    item_rando = chance(0.3)
    eclipse = chance(0.3)
    global_seed = randint(0, 10000)
    map_seed, weather_seed, weather_effects_seed, altar_seed, shop_seed, gamble_seed, remnant_seed, enemy_encouter_seed, evolution_seed = global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed
    mode = choice(["story", "infinite"])
    print("\nDaily Run Seed -", daily_seed, "\nGame Mode -", mode, "\nSeed -", global_seed, "\nDifficulty -", difficulty, "\nWeather amount -", weather_amount)
    if evolution:
        print("Evolution is enabled")
    if overkill:
        print("Overkill is enabled")
    if speedrunner:
        print("Speedrunner is enabled")
    if item_rando:
        print("Item Randomizer is enabled")
    if eclipse:
        print("Eclipse is enabled")
    print('''
Are you sure you want to play this daily run?
1. Yes
2. No''')
    while True:
        action = input()
        if action == "1" or action.lower() == "yes":
            if mode == "infinite":
                game_mode = "infinite"
                infinite_mode()
            elif mode == "story":
                game_mode = "story"
                story_mode()
            else:
                print("There was an error initializing game modes for the daily run! Report this to the developer!")
            break
        elif action == "2" or action.lower() == "no":
            break

def daily_run_retry():
    global difficulty
    global original_difficulty
    global weather_amount
    global evolution
    global overkill
    global speedrunner
    global item_rando
    global eclipse
    global global_seed
    global daily_seed
    global map_seed
    global weather_seed
    global weather_effects_seed
    global altar_seed
    global shop_seed
    global gamble_seed
    global remnant_seed
    global enemy_encouter_seed
    global evolution_seed
    global game_mode
    seed(daily_seed)
    difficulty = randint(50, 70)
    original_difficulty = difficulty
    weather_amount = randint(1, 6)
    evolution = chance(0.4)
    overkill = chance(0.2)
    speedrunner = chance(0.4)
    item_rando = chance(0.3)
    eclipse = chance(0.3)
    global_seed = randint(0, 10000)
    map_seed, weather_seed, weather_effects_seed, altar_seed, shop_seed, gamble_seed, remnant_seed, enemy_encouter_seed, evolution_seed = global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed
    mode = choice(["story", "infinite"])
    if mode == "infinite":
        game_mode = "infinite"
        infinite_mode()
    elif mode == "story":
        game_mode = "story"
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
    global difficulty
    global original_difficulty
    global weather_amount
    global evolution
    global overkill
    global speedrunner
    global item_rando
    global eclipse
    global global_seed
    leave = 0
    while leave == 0:
        print("0. Seed -", global_seed)
        if difficulty == 40:
            print("1. Difficulty - Easy")
        elif difficulty == 55:
            print("1. Difficulty - Medium")
        elif difficulty == 70:
            print("1. Difficulty - Hard")
        elif difficulty == 100:
            print("1. Difficulty - Absurd")
        else:
            print("1. Difficulty - Unknown (", difficulty, ")", sep = "")
        print("2. Weather Amount -", weather_amount)
        print("3. Evolution -", evolution)
        print("4. Overkill -", overkill)
        print("5. Speedrunner -", speedrunner)
        print("6. Item Randomizer -", item_rando)
        print("7. Eclipse -", eclipse)
        print("9. Play the game")
        while True:
            action = input()
            if action == "0" or action.lower() == "seed":
                print("Type in an integer for it to be a seed. Type anything else to randomize it")
                action = input()
                if action.isdigit():
                    global_seed = int(action)
                    break
                else:
                    global_seed = randint(0, 10000)
                    break
            elif action == "1" or action.lower() == "difficulty":
                if difficulty < 70:
                    difficulty += 15
                else:
                    difficulty += 30
                if difficulty > 100:
                    difficulty = 40
                break
            elif action.lower() == "easy":
                difficulty = 40
                break
            elif action.lower() == "medium" or action.lower() == "normal":
                difficulty = 55
                break
            elif action.lower() == "hard":
                difficulty = 70
                break
            elif action.lower() == "absurd":
                difficulty = 100
                break
            elif action == "2" or "weather" in action.lower():
                print("Type in an integer for it to be the amount of weathers active at the same time. Type anything else to randomize it")
                action = input()
                if action.isdigit():
                    if int(action) < 15:
                        weather_amount = int(action)
                    else:
                        weather_amount = 15
                else:
                    weather_amount = randint(1, 5)
                break
            elif action == "3" or action.lower() == "evolution" or action.lower() == "evolve":
                if evolution == False:
                    evolution = True
                else:
                    evolution = False
                break
            elif action == "4" or action.lower() == "overkill":
                if overkill == False:
                    overkill = True
                else:
                    overkill = False
                break
            elif action == "5" or "speed" in action.lower():
                if speedrunner == False:
                    speedrunner = True
                else:
                    speedrunner = False
                break
            elif action == "6" or "item" in action.lower():
                if item_rando == False:
                    item_rando = True
                else:
                    item_rando = False
                break
            elif action == "7" or action.lower() == "eclipse":
                if eclipse == False:
                    eclipse = True
                else:
                    eclipse = False
                break
            elif action == "9" or "play" in action.lower() or "game" in action.lower():
                leave = 1
                original_difficulty = difficulty
                break

def save():
    text = "TD_unlocks=["
    for i in TD_area_unlocks:
        if i:
            text = text + "1"
        else:
            text = text + "0"
    text = text + "]"
    text = text + '''
TD_high_scores=['''
    for i in TD_max_raids:
        text = text + str(i)
    text = text + "]"
    with open(file_path, 'w') as file:
        file.write(text)
    print("The game was saved.")

def game():
    global global_seed
    global daily_seed
    global map_seed
    global weather_seed
    global weather_effects_seed
    global altar_seed
    global shop_seed
    global gamble_seed
    global remnant_seed
    global enemy_encouter_seed
    global evolution_seed
    
    retry = 0
    while True:
        global_seed = randint(0, 10000)
        daily_seed = (time.localtime().tm_year * 365 + time.localtime().tm_mon * 30 + time.localtime().tm_mday)
        true_reset()
        if retry == 0:
            settings_reset()
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
                    meta_game_mode = "story"
                    game_mode = "story"
                    break
                elif action == "2" or "inf" in action.lower():
                    meta_game_mode = "infinite"
                    game_mode = "infinite"
                    break
                elif action == "3" or "raid" in action.lower():
                    meta_game_mode = "raid"
                    game_mode = "raid"
                    break
                elif action == "4" or "day" in action.lower() or "daily" in action.lower():
                    meta_game_mode = "daily"
                    game_mode = "daily"
                    break
            if game_mode != "daily":
                mutators_init()
                map_seed, weather_seed, weather_effects_seed, altar_seed, shop_seed, gamble_seed, remnant_seed, enemy_encouter_seed, evolution_seed = global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed
            if game_mode == "story":
                story_mode()
            elif game_mode == "infinite":
                infinite_mode()
            elif game_mode == "raid":
                raid_mode_area_choose()
            elif game_mode == "daily":
                daily_run()
            else:
                print("There was an error initiating gamemodes...")
        else:
            map_seed, weather_seed, weather_effects_seed, altar_seed, shop_seed, gamble_seed, remnant_seed, enemy_encouter_seed, evolution_seed = global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed, global_seed
            if meta_game_mode == "story":
                story_mode()
            elif meta_game_mode == "infinite":
                infinite_mode()
            elif meta_game_mode == "raid":
                raid_mode_area_choose()
            elif meta_game_mode == "daily":
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

save()
game()