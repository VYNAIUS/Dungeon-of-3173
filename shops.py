
from random import seed, randint, choice, choices
from extra_functions import chance
from reset_functions import reset_player
from enemies_and_fighting import fight
from upgrades_functions import shop_grant
from circular_avoidance import npc_talk, brewing
from coloring import enemy_name_color, cons_item_name_color

def shop_items_define(V):
    seed(V.shop_seed)
    V.shop_seed = randint(0, 10000)
    possible_shop_items = [1, 2, 4, 8, 11, 12, 13, 14, 15, 16]
    if V.player_weapon == 4:
        possible_shop_items.append(1)
    possible_alchemist_items = [13, 15, 17, 18, 19, 20]
    V.current_shop_items = []
    V.current_alchemist_items = []
    possible_weapons = [21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 25, 29]
    for i in range(3):
        item = choice(possible_shop_items)
        possible_shop_items.remove(item)
        V.current_shop_items.append(item)
        item = choice(possible_alchemist_items)
        possible_alchemist_items.remove(item)
        V.current_alchemist_items.append(item)
    V.current_shop_items.append(choice(possible_weapons))
    V.leave = 0
    if V.bought_from_alchemist == False and V.alchemist_visited:
        V.alchemist_anger += 0.4
    V.alchemist_visited = False
    V.bought_from_alchemist = False

def peaceful_shop(V):
    if V.shopkeeper_deaths == 0:
        print('''You came across a shop. \033[38;2;100;220;100mThe shopkeeper\033[0m warmly welcomes you,
\033[38;2;100;220;100m"Ah. Customer. Welcome. Take a look at these items!"\033[0m''')
    elif V.shopkeeper_deaths > 0:
        print('''You came across a shop. \033[38;2;100;220;100mThe shopkeeper\033[0m welcomes you,
\033[38;2;100;220;100m"Oh. Customer. Welcome. Look at these items!"\033[0m''')
    V.leave = 0
    while True:
        counter = 0
        print("Your balance is\033[38;2;200;200;0m", V.player_money, "coins\033[0m")
        for i in V.current_shop_items:
            counter += 1
            print(counter, ". ", V.item_names[i], " - \033[38;2;200;200;0m", cost(V, i), " coins\033[0m", sep = "")
        counter += 1
        print(counter, ". Inspect", sep = "")
        print(counter + 1, ". Sell", sep = "")
        print(counter + 2, ". Talk", sep = "")
        print(counter + 3, ". Leave", sep = "")
        while True:
            print("Which one do you want to buy?")
            action = input()
            if action.isdigit():
                action = int(action)
                if action > 0 and action <= len(V.current_shop_items):
                    shop_buy(V, action - 1, "shop")
                    break
                elif action - 1 == len(V.current_shop_items):
                    item_info(V, "shop")
                    break
                elif action - 2 == len(V.current_shop_items):
                    shopkeeper_sell_material(V)
                    break
                elif action - 3 == len(V.current_shop_items):
                    npc_talk(V, "shopkeeper")
                    break
                elif action - 4 >= len(V.current_shop_items):
                    V.leave = 1
                    break
            elif action.lower() == "inspect":
                item_info(V, "shop")
                break
            elif action.lower() == "sell":
                shopkeeper_sell_material(V)
                break
            elif action.lower() == "talk":
                npc_talk(V, "shopkeeper")
                break
            elif action.lower() == "leave":
                V.leave = 1
                break
            else:
                incorrect = True
                for i in V.current_shop_items:
                    if action.lower() in V.item_names[i].lower():
                        incorrect = False
                        shop_buy(V, V.current_shop_items.index(i), "shop")
                        break
                if incorrect:
                    print("Type in the correct action")
                else:
                    break
        if V.leave == 1:
            break
    print("You left the shop and continued your journey...\n\n\n")

def shopkeeper_sell_material(V):
    if len(V.player_items) > 0:
        print('''\033[38;2;100;220;100mThe shopkeeper\033[0m notices you pulling out items of your own and comes to selling stand. He says,
    \033[38;2;100;220;100m"Offer item. I name the price."\033[0m''')
    else:
        print('''You don't have any items to sell!''')
    print("Type anything to continue...")
    action = input()
    page = 0
    while True:
        counter = 0
        starting_index = page * 10
        index = starting_index
        while index < starting_index + 10 and index < len(V.player_items):
            counter += 1
            print(str(index + 1) + ".", cons_item_name_color(V, V.player_items[index]) + V.consumable_item_names[V.player_items[index]], "-\033[38;2;200;200;0m", sell_cost(V, V.player_items[index], 0), "coins\033[0m")
            index += 1
        if counter == 0:
            page -= 1
            if page < 0:
                break
            else:
                continue
        if starting_index != 0:
            print("A. Previous Page")
        if index != len(V.player_items):
            print("D. Next Page")
        print("0. Cancel")
        print("Choose an item")
        action = input()
        if action.lower() in ["0", "cancel"]:
            break
        elif action.lower() in ["a", "previous", "previous page"] and starting_index != 0:
            page -= 1
        elif action.lower() in ["d", "next", "next page"] and index != len(V.player_items):
            page += 1
        elif action.isdigit():
            action = int(action) - 1
            if action >= 0 and action < len(V.player_items):
                item = V.player_items[action]
                while True:
                    print("Currently selected:", cons_item_name_color(V, item) + V.consumable_item_names[item], "-\033[38;2;200;200;0m", sell_cost(V, item, 0), "coins\033[0m")
                    print("1. Sell\n2. Inspect\n0. Cancel")
                    action = input()
                    if action == '1' or action.lower() == "sell":
                        V.player_money += sell_cost(V, item, 0)
                        print("You gave", cons_item_name_color(V, item) + V.consumable_item_names[item], "\033[0mto \033[38;2;100;220;100mthe shopkeeper\033[0m. He handed over\033[38;2;200;200;0m", sell_cost(V, item, 0), "coins!\033[0m\nYour balance is\033[38;2;200;200;0m", V.player_money, "coins!\033[0m")
                        print("\033[0m\nType anything to continue...")
                        V.player_items.remove(item)
                        action = input()
                        break
                    elif action == '2' or action.lower() == "inspect":
                        print(V.consumable_item_desc[item])
                        print("\033[0m\nType anything to continue...")
                        action = input()
                    elif action == '0' or action.lower() == "cancel":
                        break
                    print("\n\n")

def sell_cost(V, item, type):
    if type == 0:
        cost = V.consumable_item_sell_costs[item]
        for i in range(V.score):
            if cost < 170000000000000000000000:
                if V.scaling_style == "legacy":
                    cost *= 1.1
                elif V.scaling_style == "V0.3.7":
                    cost *= 1.05
                cost = round(cost)
            else:
                cost += cost // 10000000000000
    return cost

def cost(V, item, type = 0):
    if type == 0:
        cost = V.item_base_costs[item]
        for i in range(V.score + (V.item_bought[item] * 3)):
            if cost < 170000000000000000000000:
                if V.scaling_style == "legacy":
                    cost *= 1.1
                elif V.scaling_style == "V0.3.7":
                    cost *= 1.05
                cost = round(cost)
            else:
                cost += cost // 10000000000000
    return cost

def item_info(V, shop_type = "shop"):
    print("Which item is the confusing one?")
    if shop_type == "shop":
        counter = 0
        for i in V.current_shop_items:
            counter += 1
            print(counter, ". ", V.item_names[i], sep = "")
        action = input()
        if action.isdigit():
            action = int(action)
            if action > 0 and action <= len(V.current_shop_items):
                print()
                print(V.item_descriptions[V.current_shop_items[action - 1]])
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
            print("Are you sure you want to buy", V.item_names[item_id] + "?\n1. Yes\n2. No")
            action = input()
            if action == "1" or action.lower() == "yes":
                V.player_money -= cost(V, item_id)
                print("\n\n\n")
                shop_grant(V, item_id)
                print("Type anything to continue...")
                action = input()
                print("\n\n\n")
                V.item_bought[item_id] += 1
                V.current_shop_items[item] = 0
                V.shopkeeper_sus -= 0.05
                if V.shopkeeper_sus <= 0:
                    V.shopkeeper_sus = 0
                    V.debt = 0
        else:
            print("You don't have enough money to buy", V.item_names[item_id] + '''!
But you could try stealing it...
What will you do?
1. Steal
2. Not Steal''')
            action = input()
            if action == "1":
                print("You stole", V.item_names[item_id])
                V.debt += cost(V, item_id)
                print("\n\n\n")
                shop_grant(V, item_id)
                print("Type anything to continue...")
                action = input()
                print("\n\n\n")
                V.current_shop_items[item] = 0
                V.shopkeeper_sus += 0.125
                V.leave = 1
            elif action == "2":
                print("You put the item back down and continued shopping...")
    elif shop_type == "alchemist":
        item_id = V.current_alchemist_items[item]
        if V.player_money >= cost(V, item_id):
            print("Are you sure you want to buy", V.item_names[item_id] + "?\n1. Yes\n2. No")
            action = input()
            if action == "1" or action.lower() == "yes":
                V.bought_from_alchemist = True
                V.alchemist_anger -= 0.25
                if V.alchemist_anger < 0:
                    V.alchemist_anger = 0
                V.player_money -= cost(V, item_id)
                print("\n\n\n")
                shop_grant(V, item_id)
                print("Type anything to continue...")
                action = input()
                print("\n\n\n")
                V.item_bought[item_id] += 1
                V.current_alchemist_items[item] = 0
        else:
            print("You don't have enough money to buy", V.item_names[item_id] + '''!
And the gaze of \033[38;2;200;0;150mthe alchemist\033[0m is too keen...
Type anything to continue...''')
            action = input()

def shop(V):
    if V.game_time < 18:
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
                    V.player_money -= V.debt
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
                        print("With guilt overwhelming you, you step over the unconscious \033[38;2;100;220;100mshopkeeper\033[0m's, and continue your journey...\nType anything to continue...")
                        V.shopkeeper_deaths += 1
                        V.cur_shopkeeper_dead = True
                        action = input()
                        print("\n\n")
                    break
                elif action == "2" and V.player_money >= V.debt:
                    print('''\033[38;2;100;220;100m"Greedy? I will take it away by force, then."\033[0m''')
                    fight(V, [33])
                    if V.lost == 1:
                        reset_player(V)
                        V.lost = 0
                    else:
                        print("With guilt overwhelming you, you step over the unconscious \033[38;2;100;220;100mshopkeeper\033[0m's, and continue your journey...\nType anything to continue...")
                        V.shopkeeper_deaths += 1
                        V.cur_shopkeeper_dead = True
                        action = input()
                        print("\n\n")
                    break
            V.shopkeeper_sus = 0
    else:
        print('''When you came across the shop, it was locked. The sign at the entrance said,
\033[38;2;100;220;100m"Please, come back in the morning!"\033[0m
Type anything to continue...''')
        action = input()

def alchemist_shop(V):
    if not chance(V.alchemist_anger - 1):
        V.alchemist_visited = True
        if V.brewery_encounters == 0:
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
\033[38;2;200;0;150m"I have impenetrabalelity potion. Which iz why I keep living. Idiot."\033[0m''')
            else:
                if V.alchemist_defeated < 1:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I giff you last chanze. BUY ZOMETHINK"\033[0m''')
                else:
                    print('''You came across a brewery. \033[38;2;200;0;150mThe alchemist\033[0m greets you,
\033[38;2;200;0;150m"I have impenetrabalelality potion. Which iz why I keep living. NOW BUY ZOMETHINK"\033[0m''')
        V.leave = 0
        V.brewery_encounters += 1
        while True:
            counter = 0
            print("Your balance is\033[38;2;200;200;0m", V.player_money, "coins\033[0m")
            for i in V.current_alchemist_items:
                counter += 1
                print(counter, ". ", V.item_names[i], " - \033[38;2;200;200;0m", cost(V, i), " coins\033[0m", sep = "")
            counter += 1
            print(counter, ". Inspect", sep = "")
            print(counter + 1, ". Brew", sep = "")
            print(counter + 2, ". Talk", sep = "")
            print(counter + 3, ". Leave", sep = "")
            while True:
                print("Which one do you want to buy?")
                action = input()
                if action.isdigit():
                    action = int(action)
                    if action > 0 and action <= len(V.current_alchemist_items):
                        shop_buy(V, action - 1, "alchemist")
                        break
                    elif action - 1 == len(V.current_alchemist_items):
                        item_info(V, "alchemist")
                        break
                    elif action - 2 == len(V.current_alchemist_items):
                        brewing(V)
                        break
                    elif action - 3 == len(V.current_alchemist_items):
                        npc_talk(V, "alchemist")
                        break
                    elif action - 4 >= len(V.current_alchemist_items):
                        V.leave = 1
                        break
                elif "inspect" in action.lower():
                    item_info(V, "alchemist")
                    break
                elif "brew" in action.lower():
                    brewing(V)
                    break
                elif "talk" in action.lower():
                    npc_talk(V, "alchemist")
                    break
                elif "leave" in action.lower():
                    V.leave = 1
                    break
                else:
                    incorrect = True
                    for i in V.current_alchemist_items:
                        if action.lower() in V.item_names[i].lower():
                            incorrect = False
                            shop_buy(V, V.current_alchemist_items.index(i), "alchemist")
                            break
                    if incorrect:
                        print("Type in the correct action")
                    else:
                        break
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
        if V.scaling_style == "legacy":
            change_cost += round(change_cost * 0.1)
        elif V.scaling_style == "V0.3.7":
            change_cost += round(change_cost * 0.05)
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
        change_item = True
        while V.mimic_got_item == False:
            if change_item:
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
                change_item = False
            print('\033[38;2;200;240;0m"So, how about ', V.item_names[item], '?"\033[0m', sep ="")
            print("Your balance is", V.player_money, "coins")
            print("1. Take it\n2. Pay", change_cost, "coins to reroll\n3. Inspect\n4. Talk")
            print("Type in the action")
            action = input()
            if action == "1":
                print("\n\n\n")
                shop_grant(V, item)
                print("Type anything to continue...")
                action = input()
                print("\n\n\n")
                V.mimic_got_item = True
                V.mimic_given_items += 1
                break
            elif action == "2":
                if V.player_money >= change_cost:
                    V.player_money -= change_cost
                    change_item = True
                    print('''\033[38;2;200;240;0m"Alright, gimme a second, pal."\033[0m''')
                else:
                    print('''\033[38;2;200;240;0m"Ay, ay, ay! Don't you scam me like that. I can clearly tell that you don't have enough. Just take the item."\033[0m''')
            elif action == "3":
                print('\033[38;2;200;240;0m"', V.item_descriptions_mimic[item], '"\033[0m', sep = "")
                print("Type anything to continue...")
                action = input()
            elif action == "4":
                npc_talk(V, "mimic_gamble")
        if V.mimic_given_items <= 5:
            change_cost = round(10 * (V.mimic_given_items / 1.8 + 1))
            for i in range(V.score):
                if V.scaling_style == "legacy":
                    change_cost += round(change_cost * 0.1)
                elif V.scaling_style == "V0.3.7":
                    change_cost += round(change_cost * 0.05)
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
    if V.mimic_bank_encounters == 0 and V.bank_locked == False:
        V.mimic_bank_encounters += 1
        print('''You see a locked steel chest with extremely sharp edges. You see a key lying right next to it.
You unlock the chest and reach to open it, but it springs back as if it is alive. It starts talking,
\033[38;2;150;150;150m"Ah, my friend! Thank you for setting me free from this prison. I will never be able to repay you!"\033[0m
After an awkwardly long pause, it continues,
\033[38;2;150;150;150m"I think I can actually. If you invest a little of your earnings, I can get you even more!"\033[0m''')
    elif V.mimic_bank_encounters <= 0 and V.bank_locked:
        V.mimic_bank_encounters += 1
        print("How did you manage to trigger these conditions?")
    elif V.mimic_bank_encounters > 0 and V.bank_first_time:
        V.mimic_bank_encounters += 1
        print('''You come across the familiar steel chest. You see the key lying right next to it.
You unlock the chest and let it speak.''')
    elif V.mimic_bank_encounters > 0 and V.bank_locked == False:
        print('''You come across the familiar steel chest. It springs to life.''')
    V.bank_first_time = False
    if V.bank_locked == False:
        if V.mimic_bank_encounters > 1:
            dialogue = randint(1, 4)
            if dialogue == 1:
                print('''\033[38;2;150;150;150m"My friend! Hello again! I am glad to see you again! Let's cut to business?"\033[0m''')
            elif dialogue == 2:
                print('''\033[38;2;150;150;150m"Hello! I am glad to see you again! Have I mentioned that before? Anyway, my services..."\033[0m''')
            elif dialogue == 3:
                print('''\033[38;2;150;150;150m"Hello, my friend! The fresh air that you bring with your arrival is amazing! Let's do business?"\033[0m''')
            elif dialogue == 4:
                print('''\033[38;2;150;150;150m"My dear friend! Are you hurt? Are you hurt financially? I can help you with that, I think!"\033[0m''')
        while True:
            print('''\033[38;2;150;150;150m"I have''', V.bank_money, '''coins inside me. Do you want to deposit or take some?"\033[0m''')
            print("Your balance is", V.player_money, "coins")
            print('''1. Deposit
2. Take
3. Talk
4. Leave''')
            action = input()
            if action == "1" or action.lower() == "deposit":
                if V.player_money > 0:
                    print("How much do you want to deposit?")
                    action = input()
                    if action.isdigit():
                        if int(action) == 0:
                            print("Stop wasting this poor mimic's time!")
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
            elif action == "3" or action.lower() == "talk":
                npc_talk(V, "mimic_bank")
            elif action == "4" or action.lower() == "leave":
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
        if V.scaling_style == "legacy":
            price += round(price / 11)
        elif V.scaling_style == "V0.3.7":
            price += round(price / 22)
    if V.death_encounters == 0:
        print('''You see a weird creature with four heads, each wearing a mask.
You brace yourself, but the creature speaks,
\033[38;2;100;100;100m"Hello, another one. I am no threat to you."\033[0m
You lower your weapon. She continues,
\033[38;2;100;100;100m"I can provide you a boat. But it might break soon."\033[0m''')
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
                V.player_has_boat = True
                V.player_boat_hp = 100
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
2. Talk
3. Continue your journey''')
            action = input()
            if action == "1" or action.lower() == "pay":
                if V.player_has_boat == True and V.player_boat_hp >= 100:
                    print('''The creature looks at you with confusion,
\033[38;2;100;100;100m"Your boat is not damaged. I do not take gratuity. But thank you?"\033[0m''')
                elif V.player_money >= price:
                    print('''You offer your coins. The creature grabs them, and hands you the boat,
\033[38;2;100;100;100m"I am surprised, that you have actually decided to pay. Thank you?"\033[0m''')
                    V.player_money -= price
                    V.player_has_boat = True
                    V.player_boat_hp = 100
                else:
                    print('''You offer less than she asked. The creature looks at you,
\033[38;2;100;100;100m"I can tell that you are trying trick me."\033[0m
You take your money back.''')
            elif action == "2" or action.lower() == "talk":
                npc_talk(V, "death")
            elif action == "3" or action.lower() == "leave":
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
4. Talk
5. Continue your journey''')
            action = input()
            if action == "1" or action.lower() == "pay":
                if V.player_has_boat == True and V.player_boat_hp >= 100:
                    print('''The creature looks at you with confusion,
\033[38;2;100;100;100m"Your boat is not damaged. I do not take gratuity. But thank you for the offer?"\033[0m''')
                elif V.player_money >= price:
                    print('''You offer your coins. The creature grabs them, and hands you the boat,
\033[38;2;100;100;100m"I am surprised, that you have actually decided to pay. Thank you?"\033[0m''')
                    V.player_money -= price
                    V.player_has_boat = True
                    V.player_boat_hp = 100
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
            elif action == "4" or action.lower() == "talk":
                npc_talk(V, "death")
            elif action == "5" or action.lower() == "leave":
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
            print('''Your balance is''', V.player_money, '''coins.
1. Pay''', price, '''coins for a boat
2. Sacrifice 10% of your strength
3. Self Inspect
4. Talk
5. Continue your journey''')
            action = input()
            if action == "1" or action.lower() == "pay":
                if V.player_has_boat == True and V.player_boat_hp >= 100:
                    print('''The creature looks at you with confusion,
\033[38;2;100;100;100m"Your boat is not damaged. I do not take gratuity. But thank you for the offer?"\033[0m''')
                elif V.player_money >= price:
                    print('''You offer your coins. The creature grabs them, and hands you the boat,
\033[38;2;100;100;100m"I am surprised, that you actually decided to pay. Thank you?"\033[0m''')
                    V.player_money -= price
                    V.player_has_boat = True
                    V.player_boat_hp = 100
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
            elif action == "4" or action.lower() == "talk":
                npc_talk(V, "death")
            elif action == "5" or action.lower() == "leave":
                print('''The creature speaks again,
\033[38;2;100;100;100m"Good bye. We will meet again."\033[0m You continue your journey...''')
                break

    V.death_encounters += 1

def reaper_bounty(V):
    if V.reaper_encounters == 0:
        print('''You come across a wooden board with carvings on it. A tall man stands next to it.
\033[38;2;230;50;0m"Another one of your kind. I WOULD KILL YOU, if it wasn't a taboo,"\033[0m says the man. He continues without hesitation,
\033[38;2;230;50;0m"My name has been lost to time, and now I have the nickname of the re-- a bounty chieftain."\033[0m
He pulls out a dagger and says, \033[38;2;230;50;0m"Pull out your hand."\033[0m
Pull out your hand?
1. Yes
2. No''')
        agree = False
        while True:
            action = input()
            if action == '1' or action.lower() == "yes":
                agree = True
                break
            elif action == '2' or action.lower() == "no":
                agree = False
                break
        if agree:
            print('''You hesitantly pull out your hand. The man quickly grabs it and makes a small cut in it.''')
        else:
            print('''The man says, \033[38;2;230;50;0m"Doubting? JUST GIVE ME YOUR HAND!"\033[0m He grabs your hand anyway and makes a small cut in it.''')
        print('''He picks up a droplet of your blood and smears it along the board.
\033[38;2;230;50;0m"There. Now you can read the board, and I can track how many creatures you have killed."\033[0m
He lets go of your hand and backs off slightly. You notice that you can in fact read the carvings on it.
Type anything to continue...''')
        action = input()
        reaper_bounty_define(V, 1)
        reaper_bounty_define(V, 2)
        reaper_bounty_define(V, 3)
        V.reaper_encounters += 1
    elif V.reaper_encounters >= 1:
        print('''You come across the board with the man, standing next to it.''')
        if V.reaper_trust < 0.1:
            print('''\033[38;2;230;50;0m"Hello, again. I hope you will get something done in the near future."\033[0m''')
        elif V.reaper_trust < 0.3:
            print('''\033[38;2;230;50;0m"Hello, again. Your travels have been fine, I assume."\033[0m''')
        elif V.reaper_trust < 0.6:
            print('''\033[38;2;230;50;0m"Hello, again. How have you-- oh right, I forgot. Sorry."\033[0m''')
        elif V.reaper_trust < 0.9:
            print('''\033[38;2;230;50;0m"Welcome back. Did you come to check on the board or to visit me?"\033[0m''')
        else:
            print('''\033[38;2;230;50;0m"Welcome back, friend. How have you been? I hope good."\033[0m''')
        if V.bounty_target_tracking[0] >= V.bounty_target_goal[0]:
            if V.scaling_style == "legacy":
                money = round((V.score + V.score_increase) * 10)
            elif V.scaling_style == "V0.3.7":
                money = round((V.score + V.score_increase) * 6)
            else:
                money = 0
            V.player_money += money
            reaper_bounty_define(V, 1)
            print('''The man comes up to you and says,
\033[38;2;230;50;0m"Good job. You killed those beasts, and that deserves some sort of reward."\033[0m
He hands you a small bag with coins inside. You got''', money, "coins! Your current balance", V.player_money, "coins!")
            print("Type anything to continue...")
            action = input()
        if V.bounty_target_tracking[1] >= V.bounty_target_goal[1]:
            reaper_bounty_define(V, 2)
            print('''The man comes up to you and says,
\033[38;2;230;50;0m"Good job. You have killed quite formidable beasts. That is more than enough for a reward. Take this instead."\033[0m''')
            seed(V.reaper_reward_seed)
            V.reaper_reward_seed = randint(0, 1000)
            shop_grant(V, choice([26, 27]))
            print("Type anything to continue...")
            action = input()
        if V.bounty_target_tracking[2] >= V.bounty_target_goal[2]:
            reaper_bounty_define(V, 3)
            print('''The man comes up to you and says,
\033[38;2;230;50;0m"I won't ask how you did it, or how you are still alive. Just take this gift. Take good care of it."\033[0m''')
            shop_grant(V, 28)
            print("Type anything to continue...")
            action = input()
    while True:
        print("The board:")
        print(enemy_name_color(V, V.bounty_target[0]) + "1.", V.enemys_name[V.bounty_target[0]], "-", str(V.bounty_target_tracking[0]) + "/" + str(V.bounty_target_goal[0]), "killed.")
        print(enemy_name_color(V, V.bounty_target[1]) + "2.", V.enemys_name[V.bounty_target[1]], "-", str(V.bounty_target_tracking[1]) + "/" + str(V.bounty_target_goal[1]), "killed.")
        print(enemy_name_color(V, V.bounty_target[2]) + "3.", V.enemys_name[V.bounty_target[2]], "-", str(V.bounty_target_tracking[2]) + "/" + str(V.bounty_target_goal[2]), "killed.")
        print("\033[0m4. Talk")
        print("5. Leave")
        action = input()
        if action.strip() == "":
            pass
        elif action == "1" or action.lower() in V.enemys_name[V.bounty_target[0]].lower():
            reaper_enemy_talk(V, V.bounty_target[0])
        elif action == "2" or action.lower() in V.enemys_name[V.bounty_target[1]].lower():
            reaper_enemy_talk(V, V.bounty_target[1])
        elif action == "3" or action.lower() in V.enemys_name[V.bounty_target[2]].lower():
            reaper_enemy_talk(V, V.bounty_target[2])
        elif action == "4" or action.lower() == "talk":
            npc_talk(V, "reaper")
        elif action.lower() == "leave":
            break
        else:
            if action.isdigit():
                action = int(action)
                if action >= 5:
                    break

def reaper_enemy_talk(V, enemy_id):
    print('''You point at one of the carvings. The man looks at the carving and says,\033[38;2;230;50;0m''')
    change_stuff = False
    if V.reaper_enemy_description_unlocks[V.reaper_included_enemys.index(enemy_id)] == False:
        V.reaper_enemy_description_unlocks[V.reaper_included_enemys.index(enemy_id)] = True
        change_stuff = True
    if enemy_id == 0:
        print('''"That bush had been causing me some trouble, back when I was a bounty hunter. It's usually in the Eternal Garden or in the Bandits' Forest."''')
    elif enemy_id == 3:
        print('''"If the bush man was only a nuisance, this thing... I HATE IT. Just like the bush man, I've seen it only in the Eternal Garden and in the Bandits' Forest."''')
    elif enemy_id == 4:
        print('''"This spirit is angered when you are way too 'innocent', which is such a stupid term. I think those weird altars can make it angry. Just kill it."''')
    elif enemy_id == 12:
        print('''"That serpent is quite unnerving. One of those has eaten my brother. I hope, that you will avenge me."''')
    elif enemy_id == 17:
        print('''"I HATE SNOWMEN! They are a stupid attempt at replacement of bounty hunters, whom if you couldn't notice I take great pride in."''')
    elif enemy_id == 20:
        if V.reaper_trust > 0.6:
            print('''"Death has told me that she feels disgust, knowing her canyon got infested with these spiders. I wanted to take action myself, but I am far too weak."''')
        else:
            print('''"Uhh... Back in my childhood I enjoyed walking around in the Deathly Canyon, but now... these spiders... uh... don't let me relive the childhood memories. Yes, that's why."''')
            if change_stuff:
                V.reaper_enemy_description_unlocks[V.reaper_included_enemys.index(enemy_id)] = False
    elif enemy_id == 31:
        print('''"Regular ents are nothing compared to these. Instead of protecting the Holy Forest, they now protect the... uh... Rotten Forest. Get it?"''')
    elif enemy_id == 38:
        print('''"This spirit is angered when you are way too 'healthy', I guess. I don't know how to describe it. Just use altars to be more healthy."''')
    elif enemy_id == 39:
        print('''"This spirit is angered when you are way too 'strong', which is quite self explanatory. Why do I want you to kill it? Yes."''')
    elif enemy_id == 40:
        print('''"This spirit is angered when you are way too 'mighty', which I have no idea what it means. Use altars, I think?"''')
    elif enemy_id == 41:
        print('''"This spirit is angered when you are way too 'protected', which is defense, I assume. Use altars for this."''')
    elif enemy_id == 42:
        if V.reaper_trust > 0.3:
            print('''"Have you seen your doppleganger? Kill it. That's it."''')
        else:
            print('''"I am not implying. I am outright telling you what to do. And you have to do it twice."''')
            if change_stuff:
                V.reaper_enemy_description_unlocks[V.reaper_included_enemys.index(enemy_id)] = False
    elif enemy_id == 45:
        print('''"They swarmed me once, which is why I have so many scars on my face. I've seen them only in the Stale Cave, and some in Bandits' Forest."''')
    elif enemy_id == 46:
        print('''"Unlike regular snowmen, these are constructs of war. They use some magic wand, called 'shotgun', I think. I've seen them only in the Barren Tundra."''')
    elif enemy_id == 55:
        print('''"I'm always down for a revolution, but not with these heretics. They are a group of orphans, that roam the... Rotten Forest. That's a good one."''')
    elif enemy_id == 63:
        print('''"It isn't a mistake, that's what their name actually is. I've had some issues with them in the Suffering Sands, but my father... perhaps, not now."''')
    elif enemy_id == 68:
        print('''"That disgusting insect was the bane of my existence, when I used to do bounty hunting in the Suffering Sands."''')
    else:
        print('''"Well, the developer of this game is so bad, that he forgot to write a dialogue line for this creature.\nWhen you see him, tell him about this and the fact, that it is caused by creature id''', str(enemy_id) + ''', okay?"''')
    print("\033[0m", end = "")
    print("Type anything to continue...")
    action = input()

def reaper_bounty_define(V, index = 1):
    if index == 1:
        previous = V.bounty_target[0]
        seed(V.reaper_seed)
        if V.game_mode in ["infinite", "story"]:
            while previous == V.bounty_target[0]:
                V.bounty_target[0] = choices([0, 45, 17, 20, 63, 55], [20, 20, 14, 14, 20, 12])[0]
        elif V.game_mode in ["raid"]:
            if V.area_id == 0:
                V.bounty_target[0] = 0
            elif V.area_id == 1:
                V.bounty_target[0] = choice([0, 45])
            elif V.area_id == 2:
                V.bounty_target[0] = 45
            elif V.area_id == 3:
                V.bounty_target[0] = 17
            elif V.area_id == 4:
                V.bounty_target[0] = 20
            elif V.area_id == 5:
                V.bounty_target[0] = 63
            elif V.area_id == 6:
                V.bounty_target[0] = 55
        if V.bounty_target[0] in [0, 63]:
            V.bounty_target_goal[0] = 7
        elif V.bounty_target[0] in [45, 17]:
            V.bounty_target_goal[0] = 9
        elif V.bounty_target[0] in [20, 55]:
            V.bounty_target_goal[0] = 12
        V.bounty_target_tracking[0] = 0
    if index == 2:
        previous = V.bounty_target[1]
        seed(V.reaper_seed)
        if V.game_mode in ["infinite", "story"]:
            while previous == V.bounty_target[1]:
                V.bounty_target[1] = choices([3, 12, 46, 68, 31], [28, 24, 20, 15, 13])[0]
        elif V.game_mode in ["raid"]:
            if V.area_id == 0:
                V.bounty_target[1] = 3
            elif V.area_id == 1:
                V.bounty_target[1] = 3
            elif V.area_id == 2:
                V.bounty_target[1] = 12
            elif V.area_id == 3:
                V.bounty_target[1] = 46
            elif V.area_id == 4:
                V.bounty_target[1] = 12
            elif V.area_id == 5:
                V.bounty_target[1] = 68
            elif V.area_id == 6:
                V.bounty_target[1] = 31
        if V.bounty_target[1] in [3]:
            V.bounty_target_goal[1] = 3
        elif V.bounty_target[1] in [68]:
            V.bounty_target_goal[1] = 7
        elif V.bounty_target[1] in [12, 46, 31]:
            V.bounty_target_goal[1] = 5
        V.bounty_target_tracking[1] = 0
    if index == 3:
        previous = V.bounty_target[2]
        seed(V.reaper_seed)
        if V.game_mode in ["infinite", "story", "raid"]:
            while previous == V.bounty_target[2]:
                V.bounty_target[2] = choices([4, 38, 39, 40, 41, 42], [10, 20, 20, 15, 15, 20])[0]
            if V.bounty_target[2] in [42]:
                V.bounty_target_goal[2] = 4
            elif V.bounty_target[2] in [4, 38, 39, 40, 41]:
                V.bounty_target_goal[2] = 1
            V.bounty_target_tracking[2] = 0
    seed(V.reaper_seed)
    V.reaper_seed = randint(0, 1000)