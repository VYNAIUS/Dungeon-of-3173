
from random import seed, randint, choice
from extra_functions import chance
from reset_functions import reset_player
from enemies_and_fighting import fight
from upgrades_functions import shop_grant

def shop_items_define(V):
    seed(V.shop_seed)
    V.shop_seed = randint(0, 10000)
    if V.item_rando:
        possible_shop_items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        possible_alchemist_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    else:
        possible_shop_items = [1, 2, 4, 8, 11, 12, 13, 14, 15, 16]
        possible_alchemist_items = [13, 15, 17, 18, 19, 20]
    V.current_shop_items = []
    V.current_alchemist_items = []
    possible_weapons = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    while V.player_weapon in possible_weapons:
        possible_weapons.remove(V.player_weapon)
    V.is_weapon_bought = 0
    for i in range(3):
        item = choice(possible_shop_items)
        possible_shop_items.remove(item)
        V.current_shop_items.append(item)
        item = choice(possible_alchemist_items)
        possible_alchemist_items.remove(item)
        V.current_alchemist_items.append(item)
    V.shop_weapon = choice(possible_weapons)
    V.leave = 0
    if V.bought_from_alchemist == False and V.alchemist_visited:
        V.alchemist_anger += 0.4
    else:
        V.alchemist_anger -= 0.5
        if V.alchemist_anger < 0:
            V.alchemist_anger = 0
    V.alchemist_visited = False
    V.bought_from_alchemist = False

def peaceful_shop(V):
    if V.shopkeeper_deaths == 0:
        print('''You came across a shop. \033[38;2;100;220;100mThe shopkeeper\033[0m warmly welcomes you,
\033[38;2;100;220;100m"Ah. Customer. Welcome. Take a look at these items!"\033[0m''')
    elif V.shopkeeper_deaths == 1:
        print('''You came across a shop. \033[38;2;100;220;100mThe shopkeeper\033[0m welcomes you,
\033[38;2;100;220;100m"Oh. Customer, welcome! These are items that my cousin gave me as a gift. I wonder what happened to him..."\033[0m''')
    elif V.shopkeeper_deaths == 2:
        print('''You came across a shop. \033[38;2;100;220;100mThe shopkeeper\033[0m welcomes you,
\033[38;2;100;220;100m"Hello. My cousins Mach and Lach left some items for me to sell. They were damaged by someone. I mean the items."\033[0m''')
    elif V.shopkeeper_deaths == 3:
        print('''You came across a shop. \033[38;2;100;220;100mThe shopkeeper\033[0m welcomes you,
\033[38;2;100;220;100m"Hello, there. Here are some items that, I found myself. Zach hasn't gift me anything! Err... I meant to say... Do you want anything?"\033[0m''')
    else:
        print('''You came across a shop. Another \033[38;2;100;220;100mshopkeeper\033[0m welcomed you,
\033[38;2;100;220;100m"Ah. Hello. Welcome to my shop. There have been quite a few changes over the last few days. As if someone started genocide. Genocide of Shopkeepers"\033[0m''')
    V.leave = 0
    while True:
        counter = 0
        print("Your balance is\033[38;2;200;200;0m", V.player_money, "coins\033[0m")
        for i in V.current_shop_items:
            counter += 1
            print(counter, ". ", V.item_names[i], " - \033[38;2;200;200;0m", cost(V, i), " coins\033[0m", sep = "")
        if V.is_weapon_bought == 0:
            counter += 1
            print(counter, ". ", V.weapon_names[V.shop_weapon], " - \033[38;2;200;200;0m", cost(V, V.shop_weapon, 1), " coins\033[0m", sep="")
        counter += 1
        print(counter, ". Inspect", sep = "")
        print(counter + 1, ". Leave", sep = "")
        while True:
            print("Which one do you want to buy?")
            action = input()
            if action.isdigit():
                action = int(action)
                if action > 0 and action <= len(V.current_shop_items):
                    shop_buy(V, action - 1, "shop")
                    break
                elif action - 1 == len(V.current_shop_items) and V.is_weapon_bought == 0:
                    shop_weapon_buy(V, V.shop_weapon)
                    break
                elif (action - 2 == len(V.current_shop_items) and V.is_weapon_bought == 0) or (action - 1 == len(V.current_shop_items) and V.is_weapon_bought == 1):
                    item_info(V, V.shop_weapon, "shop")
                    break
                elif (action - 3 >= len(V.current_shop_items) and V.is_weapon_bought == 0) or (V.is_weapon_bought == 1 and action - 2 >= len(V.current_shop_items)):
                    V.leave = 1
                    break
            else:
                print("Type in the correct action")
        if V.leave == 1:
            break
    print("You left the shop and continued your journey...\n\n\n")

def cost(V, item, type = 0):
    if type == 0:
        cost = V.item_base_costs[item]
        for i in range(V.score + (V.item_bought[item] * 3)):
            if cost < 170000000000000000000000:
                cost *= 1.1
                cost = round(cost)
            else:
                cost += cost // 10000000000000
    elif type == 1:
        cost = V.weapon_base_costs[item]
        for i in range(V.score):
            if cost < 170000000000000000000000:
                cost *= 1.1
                cost = round(cost)
            else:
                cost += cost // 10000000000000
    return cost

def item_info(V, weapon, shop_type = "shop"):
    print("Which item is the confusing one?")
    if shop_type == "shop":
        counter = 0
        for i in V.current_shop_items:
            counter += 1
            print(counter, ". ", V.item_names[i], sep = "")
        if V.is_weapon_bought == 0:
            counter += 1
            print(counter, ". ", V.weapon_names[weapon], sep="")
        action = input()
        if action.isdigit():
            action = int(action)
            if action > 0 and action <= len(V.current_shop_items):
                print()
                print(V.item_descriptions[V.current_shop_items[action - 1]])
                print("\nType anything to continue...")
                action = input()
            elif action - 1 == len(V.current_shop_items) and V.is_weapon_bought == 0:
                print()
                print(V.weapon_descriptions[weapon])
                print("\nType anything to continue...")
                action = input()
    elif shop_type == "alchemist":
        counter = 0
        for i in V.current_alchemist_items:
            counter += 1
            print(counter, ". ", V.item_names[i], sep = "")
        action = input()
        if action.isdigit():
            action = int(action)
            if action > 0 and action <= len(V.current_alchemist_items):
                print()
                print(V.item_descriptions[V.current_alchemist_items[action - 1]])
                print("\nType anything to continue...")
                action = input()

def shop_buy(V, item, shop_type = "shop"):
    if shop_type == "shop":
        item_id = V.current_shop_items[item]
        if V.player_money >= cost(V, item_id):
            V.player_money -= cost(V, item_id)
            shop_grant(V, item_id)
            V.item_bought[item_id] += 1
            V.current_shop_items[item] = 0
            V.shopkeeper_sus -= 0.05
            if V.shopkeeper_sus <= 0:
                V.shopkeeper_sus = 0
                V.debt = 0
        else:
            print('''You don't have enough money to buy this item!
But you could try stealing it...
What will you do?
1. Steal
2. Not Steal''')
            action = input()
            if action == "1":
                print("You stole", V.item_names[item_id])
                V.debt += cost(V, item_id)
                shop_grant(V, item_id)
                V.current_shop_items[item] = 0
                V.shopkeeper_sus += 0.125
                V.leave = 1
            elif action == "2":
                print("You put the item back down and continued shopping...")
    elif shop_type == "alchemist":
        item_id = V.current_alchemist_items[item]
        if V.player_money >= cost(V, item_id):
            V.bought_from_alchemist = True
            V.player_money -= cost(V, item_id)
            shop_grant(V, item_id)
            V.item_bought[item_id] += 1
            V.current_alchemist_items[item] = 0
        else:
            print('''You don't have enough money to buy this item!''')

def shop_weapon_buy(V, weapon):
    if cost(V, weapon, 1) <= V.player_money:
        V.player_money -= cost(V, weapon, 1)
        V.player_weapon = weapon
        if weapon == 1:
            V.player_extra_magic_def_buff = 1.5
        else:
            V.player_extra_magic_def_buff = 0
        V.is_weapon_bought = 1
        print("You bought", V.weapon_names[weapon])
    else:
        print('''You don't have enough money to buy this item!
But you could try stealing it...
What will you do?
1. Steal
2. Not Steal''')
        action = input()
        if action == "1":
            print("You stole", V.weapon_names[weapon])
            V.debt += cost(V, weapon, 1)
            V.player_weapon = weapon
            if weapon == 1:
                V.player_extra_magic_def_buff = 1.5
            else:
                V.player_extra_magic_def_buff = 0
            V.shopkeeper_sus += 0.5
            V.leave = 1
            V.is_weapon_bought = 1
        elif action == "2":
            print("You put the item back down and continued shopping...")

def shop(V):
    if V.game_time < 18 and V.eclipse == False:
        if chance(V.shopkeeper_sus) == False:
            peaceful_shop(V)
        else:
            print('''When you came across a shop, \033[38;2;100;220;100mthe familiar shopkeeper\033[0m grabbed you by the wrist and said,
\033[38;2;100;220;100m"You are the thief. I know it. It's time for you to pay."\033[0m
You owe \033[38;2;100;220;100mthe shopkeeper\033[38;2;200;200;0m''', V.debt, '''coins.\033[0m Will you play it back?
Your balance is\033[38;2;200;200;0m''', V.player_money,'''coins\033[0m
1. Pay
2. Refuse''')
            while True:
                print("Type in the action")
                action = input()
                if action == "1" and V.player_money >= V.debt:
                    player_money -= V.debt
                    print("You paid \033[38;2;100;220;100mthe shopkeeper\033[38;2;200;200;0m", V.debt, "coins.\033[0m Your balance is now\033[38;2;200;200;0m", V.player_money, '''coins.
\033[38;2;100;220;100m"Alright. Come back later. My shop isn't ready yet,"\033[0m he said and let you go.
You continued on your journey...\n\n\n''')
                    break
                elif action == "2" and V.player_money < V.debt:
                    print('''\033[38;2;100;220;100m"Oh. So you are poor? I will get products from you, then."''')
                    fight(V, [33])
                    if V.lost == 1:
                        reset_player(V)
                        V.lost = 0
                    else:
                        print("With guilt overwhelming you, you step over \033[38;2;100;220;100mthe shopkeeper\033[0m's body, and continue your journey...\n\n\n")
                        V.shopkeeper_deaths += 1
                        V.cur_shopkeeper_dead = True
                    break
                elif action == "2" and player_money >= V.debt:
                    print('''\033[38;2;100;220;100m"Greedy? I will take it away by force, then."\033[0m''')
                    fight(V, [33])
                    if V.lost == 1:
                        reset_player(V)
                        V.lost = 0
                    else:
                        print("With guilt overwhelming you, you step over \033[38;2;100;220;100mthe shopkeeper\033[0m's body, and continue your journey...\n\n\n")
                        V.shopkeeper_deaths += 1
                        V.cur_shopkeeper_dead = True
                    break
            V.shopkeeper_sus = 0
    elif V.eclipse:
        print('''When you came across the shop, it was locked. The sign at the entrance said,
\033[38;2;100;220;100m"Please, come back after the eclipse!"\033[0m You decided to continue your journey...\n\n\n''')
    else:
        print('''When you came across the shop, it was locked. The sign at the entrance said,
\033[38;2;100;220;100m"Please, come back in the morning!"\033[0m You decided to continue your journey...\n\n\n''')

def alchemist_shop(V):
    if not chance(V.alchemist_anger - 1):
        V.alchemist_visited = True
        if V.brewery_encouters == 0:
            print('''You came across a brewery. Inside, you were greeted by \033[38;2;200;0;150mthe alchemist\033[0m,
\033[38;2;200;0;150m"'ello, 'ello! Finally one arrifes to buy my kreat potions."\033[0m
He presents you the goods.''')
        else:
            if V.alchemist_anger <= 0.3:
                if V.game_time < 6:
                    print('''You came across a brewery. Half-sleeping \033[38;2;200;0;150malchemist\033[0m greets you,
\033[38;2;200;0;150m"Guten morgen. Neet any potionz?"\033[0m
He presents you the goods.''')
                elif V.game_time < 18:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"The zun is high, and I greet it. I meant, the zun is high, but my prices are low."\033[0m
He presents you the goods.''')
                else:
                    print('''You came across a brewery. Half-sleeping \033[38;2;200;0;150malchemist\033[0m greets you,
\033[38;2;200;0;150m"Quite late. Need a zleep potion?"\033[0m
He presents you the goods.''')
            elif V.alchemist_anger <= 0.6:
                if V.alchemist_defeated < 1:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I woult like to see you buy zomethink already."\033[0m''')
                else:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I have impenetrabalality potion. Which iz why I keep living."\033[0m''')
            elif V.alchemist_anger <= 1:
                if V.alchemist_defeated < 1:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"Buy zomethink."\033[0m''')
                else:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I have impenetrabalality potion. Which iz why I keep living. Idiot."\033[0m''')
            else:
                if V.alchemist_defeated < 1:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I giff you last chanze. BUY ZOMETHINK"\033[0m''')
                else:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I have impenetrabalality potion. Which iz why I keep living. NOW BUY ZOMETHINK"\033[0m''')
        V.leave = 0
        V.brewery_encouters += 1
        while True:
            counter = 0
            print("Your balance is\033[38;2;200;200;0m", V.player_money, "coins\033[0m")
            for i in V.current_alchemist_items:
                counter += 1
                print(counter, ". ", V.item_names[i], " - \033[38;2;200;200;0m", cost(V, i), " coins\033[0m", sep = "")
            counter += 1
            print(counter, ". Inspect", sep = "")
            print(counter + 1, ". Leave", sep = "")
            while True:
                print("Which one do you want to buy?")
                action = input()
                if action.isdigit():
                    action = int(action)
                    if action > 0 and action <= len(V.current_alchemist_items):
                        shop_buy(V, action - 1, "alchemist")
                        break
                    elif action - 1 == len(V.current_alchemist_items):
                        item_info(V, V.shop_weapon, "alchemist")
                        break
                    elif action - 2 >= len(V.current_alchemist_items):
                        V.leave = 1
                        break
                else:
                    print("Type in the correct action")
            if V.leave == 1:
                break
        print('''You left the brewery and continued your journey...''')
    else:
        if V.alchemist_defeated == 0:
            print('''You came across a brewery. Inside, you were greeted by \033[38;2;200;0;150mthe alchemist\033[0m,
\033[38;2;200;0;150m"I gave you enouff chanzes. Ja are goink to pay."\033[0m
Type anything to continue...''')
        else:
            print('''You came across a brewery. Inside, you were greeted by \033[38;2;200;0;150mthe alchemist\033[0m,
\033[38;2;200;0;150m"Again. Anozer round?"\033[0m
Type anything to continue...''')
        action = input()
        fight(V, [64])
        if V.lost == 1:
            reset_player(V)
            V.lost = 0
            V.alchemist_anger = 0.4
        else:
            V.alchemist_anger = 1
            V.alchemist_defeated += 1
            
def mimic_gamble(V):
    change_cost = round(10 * (V.mimic_given_items / 1.8 + 1))
    for i in range(V.score):
        change_cost += change_cost // 10
    if V.item_rando:
        common_items = [2, 4, 6, 8, 11, 13, 14, 15]
        uncommon_items = [1, 3, 5, 9, 12, 16, 20]
        rare_items = [0, 7, 10]
    else:
        common_items = [4, 6, 8]
        uncommon_items = [3, 5, 9, 16]
        rare_items = [7, 10]
    if V.mimic_got_item == False:
        if V.mimic_gamble_encounters == 0:
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
        elif V.mimic_gamble_encounters < 3:
            print('''You approach the golden chest and as usual, it starts to speak, \033[38;2;200;240;0m"Hey, pal. Welcome back. Wanna somethin'?"\033[0m''')
        elif V.mimic_gamble_encounters == 3:
            print('''You approach the golden chest and as usual, it springs to life, \033[38;2;200;240;0m"Hey. Third time's the charm, right?"\033[0m''')
        else:
            dialogue = randint(1, 3)
            if dialogue == 1:
                print('''You approach golden mimic again. It starts to speak, \033[38;2;200;240;0m"Hey, there. Wanna gift?"\033[0m''')
            elif dialogue == 2:
                print('''You approach a familiar golden chest, which starts talking, \033[38;2;200;240;0m"Hey, pal. Need a gift by any chance?"\033[0m''')
            elif dialogue == 3:
                print('''You walk up to the golden mimic. \033[38;2;200;240;0m"Hey, pal. Welcome back. Let me just get you somethin'."\033[0m''')
    elif V.mimic_given_items <= 5:
        print('''You approach the familiar mimic again. It springs to life and says,
\033[38;2;200;240;0m"Hey, pal. I am a little too tired for your funny business..."\033[0m
It continues, \033[38;2;200;240;0m"However, if you pay me a little, I will give you another item."\033[0m''')
        print("Your balance is", V.player_money, "coins")
        print("1. Pay", change_cost * 2, "coins\n2. Refuse")
        while True: 
            action = input()
            if action == "1" or action.lower() == "pay":
                if V.player_money >= change_cost * 2:
                    V.player_money -= change_cost * 2
                    print('''\033[38;2;200;240;0m"Alright, gimme a second, pal."\033[0m''')
                    V.mimic_got_item = False
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

    while V.mimic_given_items <= 5:
        if V.mimic_got_item == True:
            break
        V.leave = 0
        while V.mimic_got_item == False:
            seed(V.gamble_seed)
            remember_seed = V.gamble_seed
            V.gamble_seed = randint(0, 10000)
            while V.gamble_seed == remember_seed:
                V.gamble_seed = randint(0, 10000)
            if chance(0.6):
                item = choice(common_items)
            elif chance(0.75):
                item = choice(uncommon_items)
            else:
                item = choice(rare_items)
            print('\033[38;2;200;240;0m"How about ', V.item_names[item], '?"\033[0m', sep ="")
            print("Your balance is", V.player_money, "coins")
            print("1. Take it\n2. Pay", change_cost, "coins to reroll\n3. Inspect")
            while True:
                print("Type in the action")
                action = input()
                if action == "1":
                    shop_grant(V, item)
                    V.mimic_got_item = True
                    V.mimic_given_items += 1
                    break
                elif action == "2":
                    if V.player_money >= change_cost:
                       V.player_money -= change_cost
                       print('''\033[38;2;200;240;0m"Alright, gimme a second, pal."\033[0m''')
                       break
                    else:
                        print('''\033[38;2;200;240;0m"Ay, ay, ay! Don't you scam me like that. I can clearly tell that you don't have enough. Just take the item."\033[0m''')
                elif action == "3":
                    print('\033[38;2;200;240;0m"', V.item_descriptions_mimic[item], '"\033[0m', sep = "")
        if V.mimic_given_items <= 5:
            change_cost = round(10 * (V.mimic_given_items / 1.8 + 1))
            for i in range(V.score):
                change_cost += change_cost // 10
            print('''The chest speaks again,\033[38;2;200;240;0m "Hmm... I can give you another item, if you pay me a little."\033[0m
Will you pay''', change_cost * 2, "coins? Your balance is", V.player_money, "coins.")
            print("1. Pay\n2. Refuse")
            while True: 
                action = input()
                if action == "1" or action.lower() == "pay":
                    if V.player_money >= change_cost * 2:
                        V.player_money -= change_cost * 2
                        print('''\033[38;2;200;240;0m"Alright, gimme a second, pal."\033[0m''')
                        V.mimic_got_item = False
                        break
                    else:
                        print('''\033[38;2;200;240;0m"Ay, ay, ay! Don't you scam me like that. I can clearly tell that you don't have enough. Just leave."\033[0m''')
                        break
                elif action == "2" or action.lower() == "refuse":
                    print('''\033[38;2;200;240;0m"Your choice, I guess."\033[0m''')
                    V.leave = 1
                    break
        else:
            print('''The chest tiringly says, \033[38;2;200;240;0m"Ooh, pal. I think that is enough for now. Meet me later."\033[0m''')
        if V.leave == 1:
            break
    print('''\033[38;2;200;240;0m"Alright, good luck there, pal."\033[0m After that you moved forwards.\n\n\n''')
    V.mimic_gamble_encounters += 1

def mimic_bank(V):
    if V.bank_first_time:
        V.bank_locked = False
    epic_money = 0
    if V.mimic_bank_encouters == 0 and V.bank_locked == False:
        V.mimic_bank_encouters += 1
        print('''You see a locked steel chest with extremely sharp edges. You see a key lying right next to it.
You unlock the chest and reach to open it, but it springs back as if it is alive. It starts talking,
\033[38;2;150;150;150m"Ah, my friend! Thank you for setting me free from this prison. I will never be able to repay you!"\033[0m
After an awkwardly long pause, it continues,
\033[38;2;150;150;150m"I think I can actually. If you invest a little of your earnings, I can get you even more!"\033[0m''')
    elif V.mimic_bank_encouters <= 0 and V.bank_locked:
        V.mimic_bank_encouters += 1
        print("How did you manage to trigger these conditions?")
    elif V.mimic_bank_encouters > 0 and V.bank_first_time:
        V.mimic_bank_encouters += 1
        print('''You come across the familiar steel chest. You see the key lying right next to it.
You unlock the chest and let it speak.''')
    elif V.mimic_bank_encouters > 0 and V.bank_locked == False:
        V.mimic_bank_encouters += 1
        print('''You come across the familiar steel chest. It springs to life.''')
    V.bank_first_time = False
    if V.bank_locked == False:
        if V.mimic_bank_encouters > 1:
            dialogue = randint(1, 4)
            if dialogue == 1:
                print('''\033[38;2;150;150;150m"My friend! Hello again! I am glad to see you again! Let's cut to business?"\033[0m''')
            elif dialogue == 2:
                print('''\033[38;2;150;150;150m"Hello! I am glad to see you again! Have I mentioned that before? Anyway, my services..."\033[0m''')
            elif dialogue == 3:
                print('''\033[38;2;150;150;150m"Hello, my friend! The fresh air that you bring with your arrival is amazing! Let's do business?"\033[0m''')
            elif dialogue == 4 and V.stalker_stealth < 100:
                print('''\033[38;2;150;150;150m"My friend! It is you, right? I keep seeing a person that looks like you. As if it stalks you. Anyway, business?"\033[0m''')
            else:
                print('''\033[38;2;150;150;150m"My dear friend! Are you hurt? Are you hurt financially? I can help you with that, I think!"\033[0m''')
        while True:
            print('''\033[38;2;150;150;150m"I have''', V.bank_money, '''coins inside me. Do you want to deposit or take some?"\033[0m''')
            print("Your balance is", V.player_money, "coins")
            print('''1. Deposit
2. Take
3. Leave''')
            action = input()
            if action == "1" or action.lower() == "deposit":
                if V.player_money > 0:
                    print("How much do you want to deposit?")
                    action = input()
                    if action.isdigit():
                        if int(action) == 0:
                            print("Stop wasting this guy's time!")
                            continue
                        epic_money = int(action)
                        if epic_money > V.player_money:
                            print("You don't have that much money!")
                        else:
                            V.bank_money += epic_money
                            V.player_money -= epic_money
                else:
                    print("You don't have any money to deposit!")
            elif action == "2" or action.lower() == "take":
                if V.bank_money > 0:
                    V.player_money += V.bank_money
                    V.bank_money = 0
                else:
                    print("There is no money to take!")
            elif action == "3" or action.lower() == "leave":
                break
    else:
        print("You come across a locked steel chest. Its excitement is barely contained by the lock on it.")
    if epic_money > 0 and V.locking_tutorial == False:
        V.locking_tutorial = True
        print('''You decide to continue your journey, but the chest speaks again,
\033[38;2;150;150;150m"Friend, there is one more thing. You need to lock me, so that my magic of duplication works."\033[0m
You grab the key that you used to open the chest, and lock it. As you do so, the key disappears.

Type anything to continue...''')
        V.bank_locked = True
        action = input()
    elif epic_money > 0:
        print('''\033[38;2;150;150;150m"Don't forget to lock me."\033[0m
You grab the key and lock it.''')
        V.bank_locked = True
    print("You continue your journey...\n\n\n")

def death_boat(V):
    sacrificed = 0
    price = 21
    for i in range(V.score):
        price += round(price / 11)
    if V.death_encounters == 0:
        print('''You see a weird creature with four heads, each wearing a mask.
You brace yourself, but the creature speaks,
\033[38;2;100;100;100m"Hello, another one. I am no threat to you."\033[0m
You lower your weapon. She continues,
\033[38;2;100;100;100m"I can provide you a boat. But it only functions in this area."\033[0m''')
        while True:
            print('''
Do you accept a gift of a boat from this creature?
1. Yes
2. No''')
            action = input()
            if action == "1" or action.lower() == "yes":
                print('''You grab the incredibly light boat. The creature speaks again,
\033[38;2;100;100;100m"I hope it will help you. I shall depart. Meet me later."\033[0m
After that, she crawls away.''')
                V.player_boat = True
                break
            elif action == "2" or action.lower() == "no":
                print('''You refuse to grab the boat. The creature speaks again,
\033[38;2;100;100;100m"Do not let your cockiness be the death of yours."\033[0m
She then crawls away.''')
                break
        print('''You continue your journey...''')
    elif V.death_encounters == 1:
        print('''You see the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. The boat prices are growing, which is why I have to sell them now."\033[0m
She continues, \033[38;2;100;100;100m"I can give you a boat for''', price, '''coins."\033[0m''')
        while True:
            print('''Your balance is''', V.player_money, '''coins.
1. Pay''', price, '''coins
2. Continue your journey''')
            action = input()
            if action == "1" or action.lower() == "pay":
                if V.player_boat == True:
                    print('''The creature looks at you with confusion,
\033[38;2;100;100;100m"I do not take gratuity. But thank you?"\033[0m''')
                elif V.player_money >= price:
                    print('''You offer your coins. The creature grabs them, and hands you the boat,
\033[38;2;100;100;100m"I am surprised, that you have actually decided to pay. Thank you?"\033[0m''')
                    V.player_money -= price
                    V.player_boat = True
                else:
                    print('''You offer less than she asked. The creature looks at you,
\033[38;2;100;100;100m"I can tell that you are trying trick me."\033[0m
You take your money back.''')
            elif action == "2" or action.lower() == "leave":
                print('''The creature speaks again,
\033[38;2;100;100;100m"Good bye. We will meet again."\033[0m You continue your journey...''')
                break
    elif V.death_encounters == 2:
        print('''You see the mask creature again. She speaks,
\033[38;2;100;100;100m"Hello, warrior. I thought of the inevitable that will come for you. And I am not talking about myself."\033[0m
Slightly unsettled by this, you continue listening, \033[38;2;100;100;100m"Some spirits may come for you."\033[0m
\033[38;2;100;100;100m"But I can provide some safety for you. It is not easy, which is why I ask for payment."\033[0m
She continues, \033[38;2;100;100;100m"However, I do not need your coins. Instead, I need your strength."\033[0m''')
        while True:
            print('''Your balance is''', V.player_money, '''coins.
1. Pay''', price, '''coins for a boat
2. Sacrifice 10% of your strength
3. Self Inspect
4. Continue your journey''')
            action = input()
            if action == "1" or action.lower() == "pay":
                if V.player_boat == True:
                    print('''The creature looks at you with confusion,
\033[38;2;100;100;100m"I do not take gratuity. But thank you for the offer?"\033[0m''')
                elif V.player_money >= price:
                    print('''You offer your coins. The creature grabs them, and hands you the boat,
\033[38;2;100;100;100m"I am surprised, that you have actually decided to pay. Thank you?"\033[0m''')
                    V.player_money -= price
                    V.player_boat = True
                else:
                    print('''You offer less than she asked. The creature looks at you,
\033[38;2;100;100;100m"I can tell that you are trying trick me."\033[0m
You take your money back.''')
            elif action == "2" or action.lower() == "sacrifice":
                if sacrificed == 0:
                    V.player_base_dmg -= round(V.player_base_dmg * 0.1)
                    V.spirit_anger_reduction += 1
                    sacrificed += 1
                    print('''You feel part of your strength leaving your body. Few moments later you feel safety.
\033[38;2;100;100;100m"They should become weaker. Unlike the boat, this is permanent."\033[0m
Your base damage is now''', V.player_base_dmg, '''DMG!''')
                elif sacrificed == 1:
                    print('''The creature speaks again,
\033[38;2;100;100;100m"No. You are going to be far too weak."\033[0m''')
            elif action == "3" or "self" in action.lower() or "inspect" in action.lower():
                print("\033[38;2;255;0;0mStrength -", V.player_base_dmg, "DMG\033[0m")
            elif action == "4" or action.lower() == "leave":
                print('''The creature speaks again,
\033[38;2;100;100;100m"Good bye. We will meet again."\033[0m You continue your journey...''')
                break
    else:
        if V.area_id == 0:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. Do you feel the familiarity of your home?"\033[0m
She quickly changes the topic, \033[38;2;100;100;100m"Do you need a boat here? Or help with spirits?"\033[0m''')
        elif V.area_id == 2:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. Can you feel the presence of another being like me, penetrating the air?"\033[0m
She quickly changes the topic, \033[38;2;100;100;100m"Do you need a boat here? Or help with spirits?"\033[0m''')
        elif V.area_id == 4:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. What is this feeling? Pride? Longing? Nostalgia? I do not feel it anywhere else."\033[0m
She quickly changes the topic, \033[38;2;100;100;100m"Do you really need a boat here? Or help with spirits?"\033[0m''')
        elif V.area_id == 5:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. I do not enjoy being in this place. I feel guilt? I hate recalling \033[38;2;100;100;100;3mHim.\033[0m
She quickly changes the topic, \033[38;2;100;100;100m"Do you really need a boat here? Or help with spirits?"\033[0m''')
        elif V.area_id == 6:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Hello again. This place reminds me of... No, not right in anyone's presence."\033[0m
She quickly changes the topic, \033[38;2;100;100;100m"You probably need a boat here. Do you need help with spirits?"\033[0m''')
        else:
            print('''You come across the masked creature again. She speaks,
\033[38;2;100;100;100m"Do you need a boat here? Or help with spirits?"\033[0m''')
        while True:
            print('''Your balance is''', V.player_money, '''
1. Pay''', price, '''coins for a boat
2. Sacrifice 10% of your strength
3. Self Inspect
4. Continue your journey''')
            action = input()
            if action == "1" or action.lower() == "pay":
                if V.player_boat == True:
                    print('''The creature looks at you with confusion,
\033[38;2;100;100;100m"I do not take gratuity. But thank you for the offer?"\033[0m''')
                elif V.player_money >= price:
                    print('''You offer your coins. The creature grabs them, and hands you the boat,
\033[38;2;100;100;100m"I am surprised, that you actually decided to pay. Thank you?"\033[0m''')
                    V.player_money -= price
                    V.player_boat = True
                else:
                    print('''You offer less than she asked. The creature looks at you,
\033[38;2;100;100;100m"I can tell that you are trying trick me."\033[0m
You take your money back.''')
            elif action == "2" or action.lower() == "sacrifice":
                if sacrificed == 0:
                    V.player_base_dmg -= round(V.player_base_dmg * 0.1)
                    V.spirit_anger_reduction += 1
                    sacrificed += 1
                    print('''You feel part of your strength leaving your body. Few moments later you feel safety.
\033[38;2;100;100;100m"They should become weaker. Unlike the boat, this is permanent."\033[0m
Your base damage is now''', V.player_base_dmg, '''DMG!''')
                elif sacrificed == 1:
                    print('''The creature speaks again,
\033[38;2;100;100;100m"No. You are going to be far too weak."\033[0m''')
            elif action == "3" or "self" in action.lower() or "inspect" in action.lower():
                print("\033[38;2;255;0;0mStrength -", V.player_base_dmg, "DMG\033[0m")
            elif action == "4" or action.lower() == "leave":
                print('''The creature speaks again,
\033[38;2;100;100;100m"Good bye. We will meet again."\033[0m You continue your journey...''')
                break

    V.death_encounters += 1