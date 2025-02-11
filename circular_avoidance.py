
from random import choice
from coloring import enemy_name_color, represented_area_color

def max_x(V):
    cur_max = 0
    for i in V.events_coordinates:
        if cur_max < i[0]:
            cur_max = i[0]
    return cur_max

def min_x(V):
    cur_min = 0
    for i in V.events_coordinates:
        if cur_min > i[0]:
            cur_min = i[0]
    return cur_min

def max_y(V):
    cur_max = 0
    for i in V.events_coordinates:
        if cur_max < i[1]:
            cur_max = i[1]
    return cur_max

def min_y(V):
    cur_min = 0
    for i in V.events_coordinates:
        if cur_min > i[1]:
            cur_min = i[1]
    return cur_min

def map_tile_move(V, coordinates, direction, step = 1):
    old_event_index = V.events_coordinates.index(coordinates)
    event_type = V.events[old_event_index]
    bad_path = False
    if direction == "u":
        new_coordinates = [coordinates[0], coordinates[1] - step, coordinates[2]]
        if new_coordinates in V.events_coordinates:
            for i in range(step):
                test_coords = [coordinates[0], coordinates[1] - i, coordinates[2]]
                if not test_coords in V.events_coordinates or V.events[V.events_coordinates.index(test_coords)] == 10:
                    bad_path = True
            if bad_path == False:
                new_event_index = V.events_coordinates.index(new_coordinates)
                if V.events[new_event_index] in [0, 6, 9, 15, 25, 26, 27, 28]:
                    V.events[new_event_index], V.events[old_event_index] = event_type, 0
                    V.no_update_coordinates.append(new_coordinates)
                    return True
    if direction == "l":
        new_coordinates = [coordinates[0] - step, coordinates[1], coordinates[2]]
        if new_coordinates in V.events_coordinates:
            for i in range(step):
                test_coords = [coordinates[0] - i, coordinates[1], coordinates[2]]
                if not test_coords in V.events_coordinates or V.events[V.events_coordinates.index(test_coords)] == 10:
                    bad_path = True
            if bad_path == False:
                new_event_index = V.events_coordinates.index(new_coordinates)
                if V.events[new_event_index] in [0, 6, 9, 15, 25, 26, 27, 28]:
                    V.events[new_event_index], V.events[old_event_index] = event_type, 0
                    V.no_update_coordinates.append(new_coordinates)
                    return True
    if direction == "d":
        new_coordinates = [coordinates[0], coordinates[1] + step, coordinates[2]]
        if new_coordinates in V.events_coordinates:
            for i in range(step):
                test_coords = [coordinates[0], coordinates[1] + i, coordinates[2]]
                if not test_coords in V.events_coordinates or V.events[V.events_coordinates.index(test_coords)] == 10:
                    bad_path = True
            if bad_path == False:
                new_event_index = V.events_coordinates.index(new_coordinates)
                if V.events[new_event_index] in [0, 6, 9, 15, 25, 26, 27, 28]:
                    V.events[new_event_index], V.events[old_event_index] = event_type, 0
                    V.no_update_coordinates.append(new_coordinates)
                    return True
    if direction == "r":
        new_coordinates = [coordinates[0] + step, coordinates[1], coordinates[2]]
        if new_coordinates in V.events_coordinates:
            for i in range(step):
                test_coords = [coordinates[0] + i, coordinates[1], coordinates[2]]
                if not test_coords in V.events_coordinates or V.events[V.events_coordinates.index(test_coords)] == 10:
                    bad_path = True
            if bad_path == False:
                new_event_index = V.events_coordinates.index(new_coordinates)
                if V.events[new_event_index] in [0, 6, 9, 15, 25, 26, 27, 28]:
                    V.events[new_event_index], V.events[old_event_index] = event_type, 0
                    V.no_update_coordinates.append(new_coordinates)
                    return True
    if direction == "ul":
        new_coordinates = [coordinates[0] - step, coordinates[1] - step, coordinates[2]]
        if new_coordinates in V.events_coordinates:
            for i in range(step):
                test_coords = [coordinates[0] - i, coordinates[1], coordinates[2]]
                if test_coords in V.events_coordinates and V.events[V.events_coordinates.index(test_coords)] != 10:
                    continue
                test_coords = [coordinates[0], coordinates[1] - i, coordinates[2]]
                if test_coords in V.events_coordinates and V.events[V.events_coordinates.index(test_coords)] != 10:
                    continue
                bad_path = True
            if bad_path == False:
                new_event_index = V.events_coordinates.index(new_coordinates)
                if V.events[new_event_index] in [0, 6, 9, 15, 25, 26, 27, 28]:
                    V.events[new_event_index], V.events[old_event_index] = event_type, 0
                    V.no_update_coordinates.append(new_coordinates)
                    return True
    if direction == "dl":
        new_coordinates = [coordinates[0] - step, coordinates[1] + step, coordinates[2]]
        if new_coordinates in V.events_coordinates:
            for i in range(step):
                test_coords = [coordinates[0] - i, coordinates[1], coordinates[2]]
                if test_coords in V.events_coordinates and V.events[V.events_coordinates.index(test_coords)] != 10:
                    continue
                test_coords = [coordinates[0], coordinates[1] + i, coordinates[2]]
                if test_coords in V.events_coordinates and V.events[V.events_coordinates.index(test_coords)] != 10:
                    continue
                bad_path = True
            if bad_path == False:
                new_event_index = V.events_coordinates.index(new_coordinates)
                if V.events[new_event_index] in [0, 6, 9, 15, 25, 26, 27, 28]:
                    V.events[new_event_index], V.events[old_event_index] = event_type, 0
                    V.no_update_coordinates.append(new_coordinates)
                    return True
    if direction == "dr":
        new_coordinates = [coordinates[0] + step, coordinates[1] + step, coordinates[2]]
        if new_coordinates in V.events_coordinates:
            for i in range(step):
                test_coords = [coordinates[0] + i, coordinates[1], coordinates[2]]
                if test_coords in V.events_coordinates and V.events[V.events_coordinates.index(test_coords)] != 10:
                    continue
                test_coords = [coordinates[0], coordinates[1] + i, coordinates[2]]
                if test_coords in V.events_coordinates and V.events[V.events_coordinates.index(test_coords)] != 10:
                    continue
                bad_path = True
            if bad_path == False:
                new_event_index = V.events_coordinates.index(new_coordinates)
                if V.events[new_event_index] in [0, 6, 9, 15, 25, 26, 27, 28]:
                    V.events[new_event_index], V.events[old_event_index] = event_type, 0
                    V.no_update_coordinates.append(new_coordinates)
                    return True
    if direction == "ur":
        new_coordinates = [coordinates[0] + step, coordinates[1] - step, coordinates[2]]
        if new_coordinates in V.events_coordinates:
            for i in range(step):
                test_coords = [coordinates[0] + i, coordinates[1], coordinates[2]]
                if test_coords in V.events_coordinates and V.events[V.events_coordinates.index(test_coords)] != 10:
                    continue
                test_coords = [coordinates[0], coordinates[1] - i, coordinates[2]]
                if test_coords in V.events_coordinates and V.events[V.events_coordinates.index(test_coords)] != 10:
                    continue
                bad_path = True
            if bad_path == False:
                new_event_index = V.events_coordinates.index(new_coordinates)
                if V.events[new_event_index] in [0, 6, 9, 15, 25, 26, 27, 28]:
                    V.events[new_event_index], V.events[old_event_index] = event_type, 0
                    V.no_update_coordinates.append(new_coordinates)
                    return True
    return False

def stalker_AI(V, stalker_coordinates):
    if V.stalker_stealth % 2 == 0:
        if stalker_coordinates != V.player_coordinates:
            movement_options = []
            if stalker_coordinates[0] < V.player_coordinates[0]:
                movement_options = movement_options + ["l"]
                if stalker_coordinates[1] < V.player_coordinates[1]:
                    movement_options = movement_options + ["ul"]
                elif stalker_coordinates[1] > V.player_coordinates[1]:
                    movement_options = movement_options + ["dl"]
                else:
                    movement_options = movement_options + ["ul", "dl"]
            elif stalker_coordinates[0] > V.player_coordinates[0]:
                movement_options = movement_options + ["r"]
                if stalker_coordinates[1] < V.player_coordinates[1]:
                    movement_options = movement_options + ["ur"]
                elif stalker_coordinates[1] > V.player_coordinates[1]:
                    movement_options = movement_options + ["dr"]
                else:
                    movement_options = movement_options + ["ur", "dr"]
            else:
                movement_options = movement_options + ["l", "r"]
            if stalker_coordinates[1] < V.player_coordinates[1]:
                movement_options = movement_options + ["u"]
            elif stalker_coordinates[1] > V.player_coordinates[1]:
                movement_options = movement_options + ["d"]
            else:
                movement_options = movement_options + ["u", "d"]
            while len(movement_options) > 0:
                direction = choice(movement_options)
                movement_options.remove(direction)
                if map_tile_move(V, stalker_coordinates, direction, 1):
                    break
                elif direction in ["u", "d", "r", "l"]:
                    if map_tile_move(V, stalker_coordinates, direction, 2):
                        break

def npc_talk(V, npc_type):
    if npc_type == "shopkeeper":
        dialogue = ["How are your travels? I might have a hallow for them.",
                    "Beware of the Canyon. Venomous spiders reside there. But I have an antidote for that!",
                    "Do you know the alchemist? He's similar to me. But unlike me, he is insane with our competition. Beware.",
                    "Have you seen the bounty chieftain? I think he is one of the Gods' followers. I don't know, which one though."]
        if V.events_heights[V.events.index(3)] < V.water_level:
            dialogue.append("I am sorry for the flood. It wasn't like this before.")
            if V.area_id == 6:
                dialogue.append("Why can I persist in this water? Don't worry about it.")
        if V.area_id == 6:
            dialogue.append("Don't touch the water here. It will hurt you badly.")
        if V.death_encounters > 0:
            dialogue.append("Have you seen the boat person? She seemed nice to me. But she is too obsessed with the Gods.")
        if V.mimic_gamble_encounters > 0:
            dialogue.append("Have you met the golden chest? That gambling addict. Don't get scammed by it.")
        if V.mimic_bank_encounters > 0:
            dialogue.append("Have you met the steel chest? That thing constantly wants attention. Can you keep it busy?")
        if V.final_area:
            dialogue.append("There is tension in the air. Your journey is ending soon.")
        if V.player_consume > 0:
            dialogue.append("I am feeling drained. It wasn't happening before you were here.")
        if V.shopkeeper_deaths == 1:
            dialogue.append("I've been left unconscious recently. Can you find them?")
        elif V.shopkeeper_deaths > 1:
            dialogue.append("Somebody keeps leaving me unconscious. I can't understand who.")
        removal_dialogue = []
        for i in dialogue:
            if i in V.said_dialogue_shopkeeper:
                removal_dialogue.append(i)
        for i in removal_dialogue:
            dialogue.remove(i)
        if len(dialogue) == 0:
            dialogue = dialogue + ["I don't think I have anything to say anymore."]
        dialogue = choice(dialogue)
        if not dialogue in V.said_dialogue_shopkeeper:
            V.said_dialogue_shopkeeper.append(dialogue)
        print("You come up to \033[38;2;100;220;100mthe shopkeeper\033[0m.\033[38;2;100;220;100m")
        print('"', dialogue, '"', sep = "", end = "")
        print("\033[0m")
    if npc_type == "mimic_gamble":
        dialogue = ["Have you seen the shopkeeper, pal? That silly guy lost his money trying to get somethin' besides traveller's hallow",
                    "Err... Have I mentioned that I dislike the Stale Cave the most? That's cuz it just reminds me of my past life, pal.",
                    "Pal, have you seen the bounty chieftain guy? He has some powerful stuff that not even I have"]
        if V.stalker_stealth < 100:
            dialogue.append("Pal, have you drunk any doppelganger potion by chance? 'cuz I've seen your weird twin stalking you")
        if V.player_consume > 0:
            dialogue.append("You have consuming abilities, right? Well, pal, I don't feel so good when you're around. I feel somewhat exhausted")
        if V.final_area:
            dialogue.append("Pal, you're powerful. And there's something in the air telling me that your journey's ending soon. Good luck")
        if V.mimic_bank_encounters > 0:
            dialogue.append("Have you seen my cousin, pal? The steel chest? Can you keep 'em busy? I don't like talking to it. It's weird")
        if V.brewery_encounters > 0:
            dialogue.append("Why do you smell like some potions that that brewer guy sells? You should buy at least one of his potions a day, to keep 'em at bay.")
        if V.death_encounters > 0:
            dialogue.append("Pal, have you seen the boat person? Somethin' about her is otherworldly. Maybe her unnatural appearance. Who knows, pal")
        removal_dialogue = []
        for i in dialogue:
            if i in V.said_dialogue_gamble_mimic:
                removal_dialogue.append(i)
        for i in removal_dialogue:
            dialogue.remove(i)
        if len(dialogue) == 0:
            dialogue = dialogue + ["So are you gonna take the item, pal?"]
        dialogue = choice(dialogue)
        if not dialogue in V.said_dialogue_gamble_mimic:
            V.said_dialogue_gamble_mimic.append(dialogue)
        print("The golden chest notices your stare and says,")
        print('\033[38;2;200;240;0m"', dialogue, '"\033[0m', sep = "")
    if npc_type == "death":
        if V.area_id != 6:
            dialogue = ["Do you remember the shopkeeper? I have talked to him a few times. I think he dislikes me after I realised he is an orphan.",
                        "Beware of your own reflection. Fighting yourself is not always a winning battle."]
            if V.mimic_gamble_encounters > 0:
                dialogue.append("You should have seen the golden chest mimic by now. What a funny mimic. It always makes me laugh whenever we talk.")
            if V.mimic_bank_encounters > 0:
                dialogue.append("I feel sorry for the steel mimic. Its excitement when it sees someone is akin to mine when the Great Cycle had just begun.")
            if V.change_encounters > 0 and not V.area_id in [0, 2]:
                dialogue.append("Have you seen the man in the Stale Cave? He used to live in it. That is, until the Great Cycle began. Now he survives in it.")
            if V.death_encounters >= 2:
                dialogue.append("Spirits? They are forces of the elements. They are hostile to those, whose power is too much for this world.")
            if V.change_recruited and V.area_id == 0:
                dialogue.append("I wonder whether the otherworldly man realises who I acutally am. I hope that at least you do.")
            if V.brewery_encounters > 0:
                dialogue.append("Have you seen the alchemist's brewery? Avoid it at all cost. If you cannot, do not make him furious.")
            if V.player_consume > 0:
                dialogue.append("Do you have consume? My mortal body feels that. You might anger the spirits with that kind of power.")
            if V.reaper_trust >= 0.1:
                dialogue.append("You have met the 'bounty chieftain'. He has told me about you several times. It seems he is becoming more fond of you, or less hateful at least.")
        else:
            dialogue = ["I do not want to talk, right now.", "Can we talk later?", "No. I will not elaborate."]
        removal_dialogue = []
        for i in dialogue:
            if i in V.said_dialogue_boat_person:
                removal_dialogue.append(i)
        for i in removal_dialogue:
            dialogue.remove(i)
        if len(dialogue) == 0:
            if V.area_id != 6:
                dialogue = ["I have nothing more to say."]
            else:
                dialogue = ["No."]
        dialogue = choice(dialogue)
        if not dialogue in V.said_dialogue_boat_person:
            V.said_dialogue_boat_person.append(dialogue)
        print("You look at the masked creature. She notices that and speaks,\033[38;2;100;100;100m")
        print('"', dialogue, '"\033[0m', sep = "")
    if npc_type == "change":
        dialogue = ["Your creator forced this madness. 'The Great Cycle...' I've been hiding for so long.",
                    "Ever-warriors, like you, have continued the Great Cycle for ages..."]
        if V.area_id == 0:
            dialogue = ["The Eternal Garden... it's been a while since I've been here. I didn't miss it.",
                        "The path to this place was surprisingly easy. The boat lady was actually useful for once."]
            if V.death_defeated:
                dialogue.append("The boat lady mentioned, how powerful you are. I see that most of her claims, about you, are true.")
        removal_dialogue = []
        for i in dialogue:
            if i in V.said_dialogue_change:
                removal_dialogue.append(i)
        for i in removal_dialogue:
            dialogue.remove(i)
        if len(dialogue) == 0:
            dialogue = dialogue + ["Oh, I will get my revenge. I know it, I know it.", "I don't have much more to say."]
        dialogue = choice(dialogue)
        if not dialogue in V.said_dialogue_change:
            V.said_dialogue_change.append(dialogue)
        print("You look up at the man. After a pause he speaks again,")
        print('\033[38;2;100;100;175m"', dialogue, '"\033[0m', sep = "")
    if npc_type == "mimic_bank":
        dialogue = ["My friend, have you heard about the shopkeeper? It's been a long time since I've seen him. I wonder what happened to him."]
        if V.mimic_bank_encounters > 2:
            dialogue.append("I sometimes I wonder if it should be you instead of him. But then I remember the sad fate that awaits you. I'm sorry, my friend.")
        if V.stalker_stealth < 100:
            dialogue.append("My friend, why is that doppleganger of yours stalking you? Is it trying to get your attention? I hope not.")
        if V.mimic_gamble_encounters > 0:
            dialogue.append("My friend, where did you get those shinies? Are they from my cousin? I knew you two would get along very well!")
        if V.death_encounters > 0:
            dialogue.append("I miss her. Do you miss her too, my friend? The boat lady is so nice and caring.")
        if V.brewery_encounters > 0:
            dialogue.append("My friend! Beware of the alchemist! He can get angry very easily! He would beat me if I were late to our... err... meeting.")
        if V.player_consume > 0:
            dialogue.append("My friend! Why do you have this draining aura? I kind of like it.")
        removal_dialogue = []
        for i in dialogue:
            if i in V.said_dialogue_bank_mimic:
                removal_dialogue.append(i)
        for i in removal_dialogue:
            dialogue.remove(i)
        if len(dialogue) == 0:
            dialogue = dialogue + ["My friend, I don't usually talk that much. I am more of a listener."]
        dialogue = choice(dialogue)
        if not dialogue in V.said_dialogue_bank_mimic:
            V.said_dialogue_bank_mimic.append(dialogue)
        print("You look at the steel chest. It carefully closes its mouth and starts talking to you,")
        print('\033[38;2;150;150;150m"', dialogue, '"\033[0m', sep="")
    if npc_type == "alchemist":
        dialogue = []
        if V.alchemist_anger <= 0.6:
            if V.alchemist_anger <= 0.3 and V.brewery_encounters > 10:
                dialogue.append("Haff I mentioned, zat you are my favorite cuztomer? Well, now I haff.")
            if V.alchemist_defeated > 0:
                dialogue.append("For ze record, I'm not zelling impentralability potionz. But wiz zem, not even Death herzelf can defeat me!")
            if V.mimic_bank_encounters > 0:
                dialogue.append("I zmell ferrum... Are you havink some business wiz zat 'zteel' mimic? Just remember zat, it iz not loyal to you.")
            if V.mimic_gamble_encounters > 0:
                dialogue.append("Iz that aurum that I zmell? Zat scammer of a chest! But itz couzin iz zlightly better. Don't waste too much money on zem.")
            if V.final_area:
                dialogue.append("I zmell tenzion in ze air. Your jorney iz endink soon.")
            if V.player_consume > 0:
                dialogue.append("I zmell foul magik. Conzume? I'm not afraid of you.")
            removal_dialogue = []
            for i in dialogue:
                if i in V.said_dialogue_alchemist:
                    removal_dialogue.append(i)
            for i in removal_dialogue:
                dialogue.remove(i)
            if len(dialogue) == 0:
                dialogue = dialogue + ["Look at zese kreat potionz! You zhould try zem out!"]
                if V.alchemist_anger > 0.3:
                    dialogue.append("You zhould buy zome of my ztuff. It'z really goot!")
        else:
            dialogue.append("Buy zomethink, and I will talk.")
        dialogue = choice(dialogue)
        if not dialogue in V.said_dialogue_alchemist:
            V.said_dialogue_alchemist.append(dialogue)
        print("You look at \033[38;2;200;0;150mthe alchemist\033[0m directly. He says,")
        print('\033[38;2;200;0;150m"', dialogue, '"\033[0m', sep = "")
    if npc_type == "reaper":
        dialogue = []
        if V.reaper_trust < 0.05:
            dialogue.append("Why are you looking at me? Do you want me to talk? Alright. I feel disgust looking at you. Happy? You'd better be.")
            dialogue.append("What? Don't like my speaking style? Go cry about it. Oh right, YOU CAN'T.")
        elif V.reaper_trust >= 0.1:
            dialogue = dialogue + ["I'm quite surprised with the amount of progress you managed to achieve. Keep it up.",
                                   "Are you yet to see the alchemist? Honestly, he sells really good potions. You should buy some of them."]
            if V.mimic_bank_encounters > 2:
                dialogue.append("Steely told me some wondrous things about you, which are half true, it seems. Just remember, it is loyal to ME.")
            if V.mimic_gamble_encounters > 0 and V.mimic_bank_encounters > 0:
                dialogue.append("You must've met Goldy. It's really a comedian, though it says, that it doesn't like joking.")
            if V.area_id == 6:
                dialogue.append("This forest is flooded in hurtful weird water. Yet, the orphans, that call this place home, SOMEHOW aren't affected by it.")
                if V.reaper_trust >= 0.6:
                    dialogue.append("Whenever she sees this forest, she can't help think about her brother. It was his domain after all. She mourns the loss.")
            if V.reaper_trust >= 0.15:
                dialogue.append('''A really long while ago, I was a bounty hunter myself. But then, I WAS CAST OUT of the group."\n"And you know what's the reason? I was too 'INHUMANE' with my killing methods. Cowards.''')
                if V.reaper_trust >= 0.3:
                    dialogue.append("I have to confess to you. I am not a bounty chieftain. I am the reaper. I've used to punish those, who cheat Death, but now... I am not allowed.")
                    dialogue.append("Yourself is your own reflection. I've only seen a few ever-warriors that have defeated them, but I believe all others, including you, have them stalking.")
                    if V.reaper_trust >= 0.6:
                        dialogue.append('''I wasn't the reaper my entire life. After getting cast out, I searched for purpose in my life. And then I met Death, who then tasked me with collecting souls."\n"And that's what I've been doing, UNTIL THE 'GREAT CYCLE'.''')
                        if V.death_defeated:
                            dialogue.append("I see, that you have defeated her. Perhaps, you are really that powerful. I can't tell just from a glance.")
        if V.final_area:
            dialogue.append("I don't know, how you are getting more stuff done, and I kind of DON'T CARE.")
        removal_dialogue = []
        for i in dialogue:
            if i in V.said_dialogue_reaper:
                removal_dialogue.append(i)
        for i in removal_dialogue:
            dialogue.remove(i)
        if len(dialogue) == 0:
            dialogue = dialogue + ["I have absolutely NOTHING to say anymore."]
        dialogue = choice(dialogue)
        if not dialogue in V.said_dialogue_reaper:
            V.said_dialogue_reaper.append(dialogue)
        print('''You look at the tall man. He looks away and says,\n\033[38;2;230;50;0m"''', dialogue, '"\033[0m', sep = "")
    print("Type anything to continue...")
    action = input()
        


def bestiary(V):
    page = 0
    while True:
        print("\n\n")
        starting_index = page * 10
        index = starting_index
        while index < starting_index + 10 and index < len(V.bestiary_order):
            print(str(index + 1) + ". ", end = "")
            if V.bestiary_order[index] in V.bestiary_entries:
                actual_enemy_index = V.bestiary_order[index]
                print(enemy_name_color(V, actual_enemy_index) + V.enemys_name[actual_enemy_index] + "\033[0m")
            else:
                print("???")
            index += 1
        if starting_index != 0:
            print("A. Previous Page")
        if index != len(V.bestiary_order):
            print("D. Next Page")
        print("0. Back")
        print("Type in the number of the action or the action itself.")
        action = input()
        if action.lower() in ["0", "back"]:
            break
        elif (action == "a" or "previous" in action.lower()) and starting_index != 0:
            page -= 1
        elif (action == "d" or "next" in action.lower()) and index != len(V.bestiary_order):
            page += 1
        elif action.strip() == "":
            pass
        elif action.isdigit():
            action = int(action) - 1
            if action in range(len(V.bestiary_order)):
                enemy_index = V.bestiary_order[action]
                if enemy_index in V.bestiary_entries:
                    bestiary_entry(V, enemy_index)
                else:
                    print("This bestiary entry is locked!")
        else:
            for i in V.bestiary_order:
                if i in V.bestiary_entries and action.lower() in V.enemys_name[i].lower():
                    bestiary_entry(V, i)
                    break

def bestiary_entry(V, enemy_id):
    print("\n\n")
    print(enemy_name_color(V, enemy_id) + V.enemys_name[enemy_id] + ":\033[0m")
    print("> HP:", V.enemys_base_hp[enemy_id])
    print("> DMG:", V.enemys_base_dmg[enemy_id])
    print("> DEF:", V.enemys_base_def[enemy_id])
    print("> CRT: ", round(V.enemys_base_crit[enemy_id] * 100), "%", sep = "")
    if V.enemys_base_spk[enemy_id] > 0:
        print("> SPK:", V.enemys_base_spk[enemy_id])
    if V.enemys_base_psn[enemy_id] > 0:
        print("> PSN:", V.enemys_base_psn[enemy_id])
    if V.enemys_base_immortality[enemy_id] > 0:
        print("> IMM:", V.enemys_base_immortality[enemy_id])
    if V.enemys_spawners[enemy_id][0] == 1:
        print("> On death spawns: ", end = "")
        spawn_counter = 0
        for i in V.enemys_spawners[enemy_id]:
            if spawn_counter > 1:
                print(", ", end = "")
            spawn_counter += 1
            if spawn_counter == 1:
                continue
            print(enemy_name_color(V, i) + V.enemys_name[i], end = "")
        print("\033[0m")


    print("--------------")
    print("Defeated:", V.enemies_killed[enemy_id], "time(s)")
    print("> Power level:", V.enemys_power_level[enemy_id])
    if V.enemy_is_boss[enemy_id]:
        print("* A boss!")
    if enemy_id in V.enemy_unconsumable and V.consume_discovered:
        print("* Unconsumable")
    print("> AI:", V.enemy_patterns_names[V.enemys_patterns[enemy_id]])
    if V.enemy_areas[enemy_id] == []:
        print("Can be found only in special encounters")
    else:
        print("Can be found in: ", end = "")
        area_count = 0
        for i in V.enemy_areas[enemy_id]:
            if area_count > 0:
                print("\033[0m, ", end = "")
            if str(i).isdigit():
                if i <= 6:
                    print(represented_area_color(V, i) + V.areas[i], end = "")
            elif i == "drought":
                print("\033[38;2;230;230;100mDrought", end = "")
            area_count += 1
        print("\033[0m")
    print("--------------")
    print("Inspection Description:", enemy_name_color(V, enemy_id) + V.enemys_descriptions[enemy_id] + "\033[0m")
    print("Elements: ", end = "")
    if len(V.enemys_elements[enemy_id]) == 0:
        print("None")
    else:
        element_count = 0
        for i in V.enemys_elements[enemy_id]:
            if element_count > 0:
                print("\033[0m, ", end = "")
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
        print("\033[0m")
    if enemy_id in V.reaper_included_enemys:
        reaper_enemy_index = V.reaper_included_enemys.index(enemy_id)
        if V.reaper_enemy_description_unlocks[reaper_enemy_index]:
            print('''Bounty Chieftain's description:
\033[38;2;230;50;0m"''' + V.reaper_enemy_descriptions[reaper_enemy_index] + '''"\033[0m''')

    print("\nType anything to continue...")
    action = input()