
from random import seed, randint, choice, uniform, choices

def stats_altar(V):
    print("You came across an altar.")
    random_dialogue = randint(1, 3)
    if random_dialogue == 1:
        print("You heard voices promising powerful gifts.")
    elif random_dialogue == 2:
        print("You see three stones, with glyphs on them, lying here.")
    elif random_dialogue == 3:
        print("You feel essence of power coursing through you.")
    print("Choose one gift:")

    seed(V.altar_seed)
    V.altar_seed = randint(0, 10000)

    while True:
        possible_upgrades = ["V", "S", "M", "P", "I", "MP"]
        new_upgrades = []
        for i in range(3):
            if possible_upgrades == []:
                break
            item = choice(possible_upgrades)
            possible_upgrades.remove(item)
            new_upgrades.append(item)
        if sorted(new_upgrades) != sorted(V.last_altar):
            break
    V.last_altar = new_upgrades.copy()
    counter = 0
    for i in new_upgrades:
        counter += 1
        print(str(counter) + ". ", end = "")
        if i == "V":
            print("\033[38;2;0;255;0mVitality", end = "")
        elif i == "S":
            print("\033[38;2;255;0;0mStrength", end = "")
        elif i == "M":
            print("\033[38;2;255;128;0mMight", end = "")
        elif i == "P":
            print("\033[38;2;0;200;255mProtection", end = "")
        elif i == "I":
            print("\033[38;2;190;0;205mInnocence", end = "")
        elif i == "MP":
            print("\033[38;2;0;255;255mMagic Protection", end = "")
        print("\033[0m")
    print(str(counter + 1) + ". Self Inspect")
    while True:
        print("Type in the number of upgrade")
        action = input()
        if action.isdigit():
            action = int(action) - 1
            if action >= 0 and action < len(new_upgrades):
                altar_grant(V, new_upgrades[action])
                break
            elif action == len(new_upgrades):
                print("\033[38;2;0;255;0mMax HP -", V.player_max_hp, "\033[38;2;255;0;0m\nBase DMG -", V.player_base_dmg, "\033[38;2;0;200;255m\nBase DEF -", V.player_base_def, "\033[38;2;0;255;255m\nBase MGCDEF -", V.player_base_magic_def, "\033[38;2;255;128;0m\nCrit chance -", V.player_crit_chance, "\033[38;2;190;0;205m\nPower level -", V.max_power_level, "\033[0m")
        elif "inspect" in action.lower() or "self" in action.lower():
            print("\033[38;2;0;255;0mMax HP -", V.player_max_hp, "\033[38;2;255;0;0m\nBase DMG -", V.player_base_dmg, "\033[38;2;0;200;255m\nBase DEF -", V.player_base_def, "\033[38;2;0;255;255m\nBase MGCDEF -", V.player_base_magic_def, "\033[38;2;255;128;0m\nCrit chance -", V.player_crit_chance, "\033[38;2;190;0;205m\nPower level -", V.max_power_level, "\033[0m")
        elif (action.lower() == "vitality" or action.lower() == "life") and "V" in new_upgrades:
            altar_grant(V, "V")
            break
        elif action.lower() == "strength" and "S" in new_upgrades:
            altar_grant(V, "S")
            break
        elif action.lower() == "might" and "M" in new_upgrades:
            altar_grant(V, "M")
            break
        elif action.lower() == "protection" and "P" in new_upgrades:
            altar_grant(V, "P")
            break
        elif (action.lower() == "innocence" or action.lower() == "fear") and "I" in new_upgrades:
            altar_grant(V, "I")
            break
        elif action.lower() == "magic protection" and "MP" in new_upgrades:
            altar_grant(V, "MP")
            break
    print("Type anything to continue...")
    action = input()
    print("\n\n\n")

def altar_grant(V, item):
    if item == "V":
        if V.scaling_style == "legacy":
            V.player_max_hp = round(V.player_max_hp * 1.15)
        elif V.scaling_style == "V0.3.7":
            V.player_max_hp = round(V.player_max_hp * 1.075)
        print("\033[38;2;0;255;0mYour max health is now", V.player_max_hp, "HP!")
    elif item == "S":
        if V.scaling_style == "legacy":
            if V.player_base_dmg < 20:
                V.player_base_dmg = round(V.player_base_dmg * 1.2)
            else:
                V.player_base_dmg = round(V.player_base_dmg * 1.15)
        elif V.scaling_style == "V0.3.7":
            if V.player_base_dmg < 20:
                V.player_base_dmg = round(V.player_base_dmg * 1.1)
            else:
                V.player_base_dmg = round(V.player_base_dmg * 1.075)
        print("\033[38;2;255;0;0mYour damage is now", V.player_base_dmg, "DMG!")
    elif item == "M":
        if V.player_crit_chance > 300:
            V.player_crit_chance += 1
        elif V.player_crit_chance > 100:
            V.player_crit_chance += 2
        else:
            V.player_crit_chance += 5
        print("\033[38;2;255;128;0mYour chance to get critical hit is now ", V.player_crit_chance, "%!", sep = "")
    elif item == "P":
        if V.scaling_style == "legacy":
            def_multiplier = (V.player_base_def / 60) + 1
        elif V.scaling_style == "V0.3.7":
            def_multiplier = (V.player_base_def / 120) + 1
        V.player_base_def = round(V.player_base_def + def_multiplier * 3)
        print("\033[38;2;0;200;255mYour defense is now", V.player_base_def, "DEF!")
    elif item == "I":
        V.max_power_level -= round(V.max_power_level * 0.1, 2)
        print("\033[38;2;190;0;205mLess enemies will consider you a threat. Your power level is", str(V.max_power_level) + "!")
    elif item == "MP":
        if V.scaling_style == "legacy":
            def_multiplier = (V.player_base_magic_def / 50) + 1
        elif V.scaling_style == "V0.3.7":
            def_multiplier = (V.player_base_magic_def / 100) + 1
        V.player_base_magic_def = round(V.player_base_magic_def + def_multiplier * 3)
        print("\033[38;2;0;255;255mYour magic defense is now", V.player_base_magic_def, "DEF!")
    print("\033[0m", end = "")

    # Spirit anger management
    if estimate_max_hp(V) < V.player_max_hp:
        V.vitality_anger = V.player_max_hp / estimate_max_hp(V)
    else:
        V.vitality_anger = V.player_max_hp / estimate_max_hp(V) - 0.5
        
    if estimate_dmg(V) < V.player_base_dmg:
        V.strength_anger = V.player_base_dmg / estimate_dmg(V)
    else:
        V.strength_anger = V.player_base_dmg / estimate_dmg(V) - 0.5

    if V.player_crit_chance > 205:
        V.might_anger = V.player_crit_chance / 205
    else:
        V.might_anger = V.player_crit_chance / 205 - 0.5

    if estimate_def(V) < V.player_base_def + V.player_base_magic_def:
        V.protection_anger = (V.player_base_def) / estimate_def(V)
    else:
        V.protection_anger = (V.player_base_def) / estimate_def(V) - 0.5

    estimate_power_level = 1
    for i in range(V.max_power_level_increase):
        estimate_power_level = round(estimate_power_level * 1.0175, 2)
    if V.max_power_level < estimate_power_level * 0.25:
        V.fear_anger = round((estimate_power_level * 0.25) / V.max_power_level)
    else:
        V.fear_anger = 0

def estimate_max_hp(V):
    hp = 100
    for i in range(V.score + int(V.score_increase) + 10):
        if V.scaling_style == "legacy":
            hp += 300 - V.difficulty
        elif V.scaling_style == "V0.3.7":
            hp += 150 - V.difficulty
        hp = hp
    return hp

def estimate_dmg(V):
    dmg = 5
    for i in range(V.score + int(V.score_increase) + 10):
        if V.scaling_style == "legacy":
            dmg += 120 - V.difficulty
        elif V.scaling_style == "V0.3.7":
            dmg += 110 - V.difficulty
        dmg = int(dmg)
    return dmg

def estimate_def(V):
    defense = 0
    for i in range(V.score + int(V.score_increase) + 10):
        if V.scaling_style == "legacy":
            defense += 120 - V.difficulty
        elif V.scaling_style == "V0.3.7":
            defense += 105 - V.difficulty
        defense = int(defense)
    return defense

def player_remnants(V):
    seed(V.remnant_seed)
    V.remnant_seed = randint(0, 10000)
    money = round(uniform(5, 14) * (V.score / 2 + 1))
    items = [1, 2, 4, 6, 11, 15]
    item_chances = [10, 10, 5, 5, 7, 7]
    if V.player_weapon == 4:
        item_chances[1] += 5
    upgrades = choices(population=items, weights=item_chances, k=randint(2,3))
    V.player_money += money
    print('''You came across a warrior's remnants. You picked up their items...
You got''', money, "coins (your balance is", V.player_money, "coins).")
    for i in upgrades:
        shop_grant(V, i)
    print('''Type anything to continue...''')
    action = input()

def xp_to_lvl_up(V):
    xp = 10
    for i in range(V.player_level):
        xp += xp // 2
    return xp

def level_up(V):
    i = 0
    while V.player_xp >= xp_to_lvl_up(V):
        V.player_xp -= xp_to_lvl_up(V)
        V.player_level += 1
        i += 1
    if i > 0:
        print("You leveled up! Your level is ", V.player_level, "!", sep = "")
        for k in range(i):
            if V.scaling_style == "legacy":
                V.player_max_hp += V.player_max_hp // 10 + 1
                V.player_base_dmg += V.player_base_dmg // 20 + 1
                V.player_base_def += V.player_base_def // 10 + 1
                V.player_base_magic_def += V.player_base_magic_def // 10 + 1
                if V.player_crit_chance < 100:
                    V.player_crit_chance += V.player_crit_chance // 20 + 1
                else:
                    V.player_crit_chance += 1
            elif V.scaling_style == "V0.3.7":
                V.player_max_hp += round(V.player_max_hp * 0.05) + 1
                V.player_base_dmg += round(V.player_base_dmg * 0.05) + 1
                V.player_base_def += round(V.player_base_def * 0.05) + 1
                V.player_base_magic_def += round(V.player_base_magic_def * 0.05) + 1
                if V.player_crit_chance < 100:
                    V.player_crit_chance += round(V.player_crit_chance * 0.05) + 1
                else:
                    V.player_crit_chance += 7
        print("A lot of your base stats have been increased!\n\n\n")

def boss_upgrade(V):
    garden_reward, forest_reward, cave_reward, tundra_reward, canyon_reward, desert_reward, rot_reward = False, False, False, False, False, False, False
    for i in V.last_boss:
        if i in V.bosses_for_areas[0]:
            garden_reward = True
        if i in V.bosses_for_areas[1]:
            forest_reward = True
        if i in V.bosses_for_areas[2]:
            cave_reward = True
        if i in V.bosses_for_areas[3]:
            tundra_reward = True
        if i in V.bosses_for_areas[4]:
            canyon_reward = True
        if i in V.bosses_for_areas[5]:
            desert_reward = True
        if i in V.bosses_for_areas[6]:
            rot_reward = True
    if garden_reward:
        V.player_shield += round(20 * (75 - V.player_shield) / 75)
        print("You now ignore ", V.player_shield, "% of physical DMG!", sep = "")
    if forest_reward:
        V.player_gold_boost += 25
        print("You get ", V.player_gold_boost, "% more money from enemies.", sep = "")
    if cave_reward:
        V.player_magic_shield += round(20 * (75 - V.player_magic_shield) / 75)
        print("You now ignore ", V.player_magic_shield, "% of magic DMG!", sep = "")
    if tundra_reward:
        V.player_damage_range_boost += 15
        print("You deal ", V.player_damage_range_boost, "% more DMG!", sep = "")
    if canyon_reward:
        if V.game_mode in ["story", "infinite"]:
            V.player_poison_def += round(15 * ((V.player_poison_def / 25) + 1))
        elif V.game_mode in ["raid"]:
            V.player_poison_def += round(3 * ((V.player_poison_def / 30) + 1))
        print("Your poison defense is now", V.player_poison_def, "PSNDEF!")
    if desert_reward:
        if V.game_mode in ["story", "infinite"]:
            V.player_spikes_armor_break += round(10 * ((V.player_spikes_armor_break / 50) + 1))
        elif V.game_mode in ["raid"]:
            V.player_spikes_armor_break += round(2 * ((V.player_spikes_armor_break / 25) + 1))
        V.player_spikes += round((V.player_spikes / 20) + 1)
        print("You now have", V.player_spikes, "SPK, which break", V.player_spikes_armor_break, "of enemies' DEF.")
    if rot_reward:
        if V.player_crit_chance > 1:
            V.player_crit_chance_reduction -= round(V.player_crit_chance_reduction * 0.25)
            print("Your crit. chance reduction is now ", V.player_crit_chance_reduction, "%!", sep = "")
        else:
            V.player_base_dmg += round(V.player_base_dmg * 1.4)
            print("Your base damage is now", V.player_base_dmg, "DMG!")
    if 52 in V.last_boss:
        if V.change_recruited == False and V.death_defeated == False:
            print("You have become the 3174th...")
        elif V.change_recruited == True and V.death_defeated == False:
            print("You and Change have managed to defeat Cycle and the 3173rd.\nYou have destroyed the balance of elements, leaving only dense forests and some landmarks behind.\nAnd without your creator you cannot exist...")
        elif V.change_recruited == False and V.death_defeated == True:
            print("You and Death have managed to defeat Cycle and the 3173rd.\nBut without an opposite force, you destroyed the balance of elements.\nAnd without your creator you cannot exist...")
        elif V.change_recruited == True and V.death_defeated == True:
            print("Death and Cycle have managed to extract every poor soul that the 3173rd has consumed.\nCycle and its creations were banished from this realm, and without your creator you cannot exist. You have died as a hero...")
    if 4 in V.last_boss:
        V.max_power_level += 1
        print("More enemies consider you a threat.")

    print("Type anything to continue...")
    action = input()

def shop_grant(V, item):
    if item == 0:
        print("You bought nothing! Good job")
    elif item == 1:
        V.player_items.append(10)
        if not 10 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(10)
        print("You got a poison flask! You can apply it to your weapon at any time!")
    elif item == 2:
        if V.scaling_style == "legacy":
            spk_addition = round(1 * ((V.player_spikes / 2) + 1))
        elif V.scaling_style == "V0.3.7":
            spk_addition = round(1 * ((V.player_spikes / 4) + 1))
        V.player_spikes += spk_addition
        print("You attached the spikes to your armor, adding", spk_addition, "SPK to it. Enemies will get hit for", V.player_spikes, "DMG when hit you.")
    elif item == 3:
        V.player_items.append(11)
        if not 11 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(11)
        print("You got a flask of lifesteal! You can apply it to your weapon at any time!")
    elif item == 4:
        V.player_items.append(15)
        if not 15 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(15)
        print("You got a bottle of Midas' power! You can apply it at any time!")
    elif item == 5:
        V.player_items.append(16)
        if not 16 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(16)
        print("You got a bottle of impenetrability! You can apply it at any time!")
    elif item == 6:
        if V.player_regen < 10:
            V.player_regen += 2
            print("You feel marked by some curse. Your total regeneration is ", V.player_regen, "%!", sep = "")
        elif V.player_regen < 15:
            V.player_regen += 1
            print("You feel marked by some curse. Your total regeneration is ", V.player_regen, "%!", sep = "")
        else:
            V.player_items.append(11)
            V.player_items.append(11)
            if not 11 in V.encyclopedia_consumable_items_entries:
                V.encyclopedia_consumable_items_entries.append(11)
            print("Despite consuming mark of the undead, you feel the essence of lifesteal. You notice that you for some reason got 2 new lifesteal flasks.")
    elif item == 7:
        V.player_items.append(17)
        if not 17 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(17)
        print("You got a bottle of consume! You can apply it at any time!")
    elif item == 8:
        if V.player_travel < 100:
            V.player_travel += round(15 * (200 - V.player_travel) / 100)
        else:
            V.player_travel += 10
        print("You feel strength in your legs. Total experience gained for entering new area is ", V.player_travel, "%", sep = "")
    elif item == 9:
        V.player_items.append(12)
        if not 12 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(12)
        print("You got a flask of enemy explotano! You can apply it to your weapon at any time!")
    elif item == 10:
        if V.player_extra_life == False:
            V.player_extra_life = True
            print("You feel some floatyness in your stomach. You have 2 lives!")
        else:
            V.player_items.append(11)
            V.player_items.append(11)
            if not 11 in V.encyclopedia_consumable_items_entries:
                V.encyclopedia_consumable_items_entries.append(11)
            print("Despite consuming Life's gift, you feel the essence of lifesteal. You notice that you for some reason got 2 new lifesteal flasks.")
    elif item == 11:
        V.player_items.append(1)
        if not 1 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(1)
        print("You got a cookie!")
    elif item == 12:
        V.player_items.append(2)
        if not 2 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(2)
        print("You got an antidote!")
    elif item == 13:
        V.player_items.append(3)
        if not 3 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(3)
        print("You got a gambler's drink!")
    elif item == 14:
        V.player_items.append(4)
        if not 4 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(4)
        print("You got cooked meat!")
    elif item == 15:
        V.player_items.append(5)
        if not 5 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(5)
        print("You got winter tea!")
    elif item == 16:
        if V.player_dodge_chance < 25:
            V.player_dodge_chance += 5
            print("You feel lighter. Your chance to dodge physical attacks is now ", V.player_dodge_chance, "%!", sep = "")
        else:
            V.player_immortality += 1
            print("Despite having additional band of agility, you feel impenetrability, coursing through you. Your total impenetrability is", V.player_immortality)
    elif item == 17:
        V.player_items.append(6)
        if not 6 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(6)
        print("You got a heal potion!")
    elif item == 18:
        V.player_items.append(7)
        if not 7 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(7)
        print("You got a berserk's potion!")
    elif item == 19:
        V.player_items.append(8)
        if not 8 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(8)
        print("You got a stun potion!")
    elif item == 20:
        V.player_items.append(9)
        if not 9 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(9)
        print("You got a regeneration potion!")
    elif item == 21:
        V.player_inventory_weapons.append(0)
        V.player_inventory_weapons_psn.append(0)
        V.player_inventory_weapons_explotano.append(0)
        V.player_inventory_weapons_lifesteal.append(0)
        V.player_inventory_weapons_wrath.append(0)
        print("You got a trusty sword! You can equip it outside of combat!")
    elif item == 22:
        V.player_inventory_weapons.append(1)
        V.player_inventory_weapons_psn.append(0)
        V.player_inventory_weapons_explotano.append(0)
        V.player_inventory_weapons_lifesteal.append(0)
        V.player_inventory_weapons_wrath.append(0)
        print("You got a magic wand! You can equip it outside of combat!")
    elif item == 23:
        V.player_inventory_weapons.append(2)
        V.player_inventory_weapons_psn.append(0)
        V.player_inventory_weapons_explotano.append(0)
        V.player_inventory_weapons_lifesteal.append(0)
        V.player_inventory_weapons_wrath.append(0)
        print("You got double daggers! You can equip them outside of combat!")
    elif item == 24:
        V.player_inventory_weapons.append(3)
        V.player_inventory_weapons_psn.append(0)
        V.player_inventory_weapons_explotano.append(0)
        V.player_inventory_weapons_lifesteal.append(0)
        V.player_inventory_weapons_wrath.append(0)
        print("You got a great hammer! You can equip it outside of combat!")
    elif item == 25:
        V.player_inventory_weapons.append(4)
        V.player_inventory_weapons_psn.append(1)
        V.player_inventory_weapons_explotano.append(0)
        V.player_inventory_weapons_lifesteal.append(0)
        V.player_inventory_weapons_wrath.append(0)
        print("You got a syringe! You can equip it outside of combat!")
    elif item == 26:
        V.player_items.append(13)
        if not 13 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(13)
        print("You got a flask of wrath! You can apply it to your weapon at any time!")
    elif item == 27:
        V.player_items.append(14)
        if not 14 in V.encyclopedia_consumable_items_entries:
            V.encyclopedia_consumable_items_entries.append(14)
        print("You got a charming potion!")
    elif item == 28:
        V.player_inventory_weapons.append(5)
        V.player_inventory_weapons_psn.append(0)
        V.player_inventory_weapons_explotano.append(0)
        V.player_inventory_weapons_lifesteal.append(0)
        V.player_inventory_weapons_wrath.append(0)
        print("You got a reaper's scythe! You can equip it outside of combat!")
    elif item == 29:
        V.player_inventory_weapons.append(6)
        V.player_inventory_weapons_psn.append(0)
        V.player_inventory_weapons_explotano.append(0)
        V.player_inventory_weapons_lifesteal.append(0)
        V.player_inventory_weapons_wrath.append(0)
        print("You got a shield! You can equip it outside of combat!")