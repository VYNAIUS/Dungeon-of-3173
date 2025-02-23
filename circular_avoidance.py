
from random import choice
from coloring import enemy_name_color, represented_area_color, cons_item_name_color

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

def seeker_AI(V, seeker_coordinates):
    knows = False
    if seeker_coordinates != V.player_coordinates and seeker_coordinates[2] == V.player_coordinates[2]:
        distance = ((V.player_coordinates[0] - seeker_coordinates[0]) ** 2 + (V.player_coordinates[1] - seeker_coordinates[1]) ** 2) ** 0.5
        if distance < (3.5 + V.max_power_level) * V.max_power_level:
            knows = True

    if knows:
        movement_options = []
        unintuitive_movement_options = []
        unintuitive_movement_options_2 = []
        if seeker_coordinates[0] < V.player_coordinates[0]:
            movement_options = movement_options + ["r"]
            unintuitive_movement_options_2 = unintuitive_movement_options_2 + ["l"]
        elif seeker_coordinates[0] > V.player_coordinates[0]:
            movement_options = movement_options + ["l"]
            unintuitive_movement_options_2 = unintuitive_movement_options_2 + ["r"]
        else:
            unintuitive_movement_options = unintuitive_movement_options + ["r", "l"]
        if seeker_coordinates[1] < V.player_coordinates[1]:
            movement_options = movement_options + ["d"]
            unintuitive_movement_options_2 = unintuitive_movement_options_2 + ["u"]
        elif seeker_coordinates[1] > V.player_coordinates[1]:
            movement_options = movement_options + ["u"]
            unintuitive_movement_options_2 = unintuitive_movement_options_2 + ["d"]
        else:
            unintuitive_movement_options = unintuitive_movement_options + ["u", "d"]
        unintuitive = True
        while len(movement_options) > 0:
            direction = choice(movement_options)
            movement_options.remove(direction)
            if map_tile_move(V, seeker_coordinates, direction, 1):
                unintuitive = False
                break
            elif direction in ["u", "d", "r", "l"]:
                if map_tile_move(V, seeker_coordinates, direction, 2):
                    unintuitive = False
                    break
        if unintuitive:
            while len(unintuitive_movement_options_2) +  len(unintuitive_movement_options) > 0:
                if len(unintuitive_movement_options) > 0:
                    direction = choice(unintuitive_movement_options)
                    unintuitive_movement_options.remove(direction)
                else:
                    direction = choice(unintuitive_movement_options_2)
                    unintuitive_movement_options_2.remove(direction)
                if map_tile_move(V, seeker_coordinates, direction, 1):
                    break
                elif direction in ["u", "d", "r", "l"]:
                    if map_tile_move(V, seeker_coordinates, direction, 2):
                        break

    else:
        moved = False
        if V.player_coordinates[2] > seeker_coordinates[2]:
            if [seeker_coordinates[0], seeker_coordinates[1], seeker_coordinates[2] + 1] in V.events_coordinates:
                epic_index = V.events_coordinates.index([seeker_coordinates[0], seeker_coordinates[1], seeker_coordinates[2] + 1])
                if V.events[epic_index] in [0, 6, 15]:
                    V.events[epic_index] = 30
                    V.events[V.events_coordinates.index(seeker_coordinates)] = 0
                    moved = True
        elif V.player_coordinates[2] < seeker_coordinates[2]:
            if [seeker_coordinates[0], seeker_coordinates[1], seeker_coordinates[2] - 1] in V.events_coordinates:
                epic_index = V.events_coordinates.index([seeker_coordinates[0], seeker_coordinates[1], seeker_coordinates[2] - 1])
                if V.events[epic_index] in [0, 6, 15]:
                    V.events[epic_index] = 30
                    V.events[V.events_coordinates.index(seeker_coordinates)] = 0
                    moved = True
        if moved == False:
            movement_options = ["r", "l", "u", "d", "ur", "dr", "ul", "dl"]
            while len(movement_options) > 0:
                direction = choice(movement_options)
                movement_options.remove(direction)
                if map_tile_move(V, seeker_coordinates, direction, 1):
                    moved = True
                    break
                elif direction in ["u", "d", "r", "l"]:
                    if map_tile_move(V, seeker_coordinates, direction, 2):
                        moved = True
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
        if V.area_id > 0:
            dialogue.append("Beware of the Seeker. It wants you and your kind to perish. But it is afraid of the sunlight.")
        if V.final_area:
            dialogue.append("There is tension in the air. Your journey is ending soon.")
        if V.player_consume > 0:
            dialogue.append("I am feeling drained. It wasn't happening before you were here.")
        if V.shopkeeper_deaths == 1:
            dialogue.append("I've been left unconscious recently. Can you avenge me?")
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
        if V.area_id > 1:
            dialogue.append("Ooh, I just remembered, pal! The Seeker guy wants you dead. When you see it, try to stall out until morning")
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
            if V.area_id == 5:
                dialogue.append("The coward that used to live here was the first one to be consumed. The Seeker is the revenge plan of his followers. Beware it.")
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
        if V.area_id > 3:
            dialogue.append("My friend, I've seen the Seeker. It wants to find you, and then... You probably know the rest. Be careful, please.")
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
                dialogue.append("bounty_origin")
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
        if not dialogue in ["bounty_origin"]:
            print('''You look at the tall man. He looks away and says,\n\033[38;2;230;50;0m"''', dialogue, '"\033[0m', sep = "")
        elif dialogue == "bounty_origin":
            print('''You look at the tall man. He looks away and says,\n\033[38;2;230;50;0m"A really long while ago, I was a bounty hunter myself. But then, I WAS CAST OUT of the group."
"And you know what's the reason? I was too 'INHUMANE' with my killing methods. Cowards."\033[0m''')
    if npc_type == "herbalist":
        dialogue = ["If you finish your journey, your parent will be so proud of you. I know it.",
                    "You have a long way to go, outside the Eternal Garden. But remember, only one left. Only one left.",
                    "My flowers are like you. Something of weak, that may become extremely powerful.",
                    "story_existence",
                    "Can you believe it? Some think everyone has the right to have a name. Sounds bizarre, I know.",]
        if V.final_area:
            dialogue = dialogue + ["You know, when you decide to take on the final test, I won't see you ever again.",
                                   "story_gods",
                                   "You can probably tell, who is going to be the only God soon. Your parent, obviously.",
                                   "I've met a nice fellow, called shopkeeper. But something was off about him. Probably, his semi-vertical pupils."]

        removal_dialogue = []
        for i in dialogue:
            if i in V.said_dialogue_herbalist:
                removal_dialogue.append(i)
        for i in removal_dialogue:
            dialogue.remove(i)
        if len(dialogue) == 0:
            dialogue.append("I'm out of stories. Sorry.")
        dialogue = dialogue[0]
        if not dialogue in V.said_dialogue_herbalist:
            V.said_dialogue_herbalist.append(dialogue)

        if not dialogue in ["story_existence", "story_gods"]:
            print('''You lightly tap the herbalist's shoulder, he turns around and begins to speak,
\033[38;2;0;0;255m"''' + dialogue + '''"\033[0m''')
        elif dialogue in ["story_existence"]:
            print('''You lightly tap the herbalist's shoulder, he turns around and begins to speak,
\033[38;2;0;0;255m"How about a story, that would be interesting to my little flowers? It is an old one."\033[0m
He turns to the arachno-flowers and begins,
\033[38;2;0;0;255m"Before the Great Cycle, before Pleasure's fate, before the dense forests covered the lands, there was a single God."
"It was standing on empty land, trying to make some purpose of itself. Then, the God had an idea."\033[0m
After a short pause the man continues, \033[38;2;0;0;255m"It decided to create dense forests, long rivers, and life."
"It poured all of its power and energy to create such impossible concepts."\033[0m
He looks down with somber and then continues,
\033[38;2;0;0;255m"And after doing so, the God, Existence, or however we should call it, perished."
"But when Gods die from exhaustion, more Gods are born..."\033[0m''')
        elif dialogue in ["story_gods"]:
            print('''You lightly tap the herbalist's shoulder, he turns around and begins to speak,
\033[38;2;0;0;255m"Here's another ancient story. Once Existence had perished, more Gods were born."
"Eight of them, to be exact: Life and Death, Exposure and Safety, Suffering and Pleasure... Cycle and Change.\033[0m
He looks up at the glass dome, covering the Garden \033[38;2;0;0;255m"I'm sorry, Cycle, for mentioning him."\033[0m
The herbalist looks back down and continues,
\033[38;2;0;0;255m"They decided to take parts of the infinite forests, that covered the land."
"Each one of them had loyal and not-so-loyal followers, that would worship them..."\033[0m
He pauses and looks at his already sleeping arachno-flowers. \033[38;2;0;0;255m"It seems the story isn't that interesting after all."\033[0m''')
    print("Type anything to continue...")
    action = input()
        


def bestiary(V):
    page = 0
    bestiary_progress = len(V.bestiary_entries)
    bestiary_total_enemies = len(V.enemys_name)
    while True:
        print("\n\n")
        print("Discovered", str(round(bestiary_progress / bestiary_total_enemies * 100)) + "% (" + str(bestiary_progress) + "/" + str(bestiary_total_enemies) + ")")
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
                    print("\n\nThis bestiary entry is locked!\nType anything to continue...")
                    action = input()
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
    for i in V.material_drops:
        if i[0] == enemy_id:
            print("Drops:")
            for r in range(len(i[1])):
                print("*", cons_item_name_color(V, i[1][r]) + V.consumable_item_names[i[1][r]] + "\033[0m", "-", str(round(i[2][r] * 100)) + "%")
            break
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

def item_encyclopedia(V):
    page = 0
    item_progress = len(V.encyclopedia_consumable_items_entries)
    total_items = len(V.encyclopedia_consumable_items_order)
    recipe_progress = len(V.encyclopedia_recipe_entries)
    total_recipes = len(V.recipes) - 1
    while True:
        print("\n\n")
        print("Items discovered", str(round(item_progress / total_items * 100)) + "% (" + str(item_progress) + "/" + str(total_items) + ")")
        if recipe_progress > 0:
            print("Brewing recipes discovered", str(round(recipe_progress / total_recipes * 100)) + "% (" + str(recipe_progress) + "/" + str(total_recipes) + ")")
        starting_index = page * 10
        index = starting_index
        while index < starting_index + 10 and index < len(V.encyclopedia_consumable_items_order):
            print(str(index + 1) + ". ", end = "")
            if V.encyclopedia_consumable_items_order[index] in V.encyclopedia_consumable_items_entries:
                actual_item_index = V.encyclopedia_consumable_items_order[index]
                print(cons_item_name_color(V, actual_item_index) + V.consumable_item_names[actual_item_index] + "\033[0m")
            else:
                print("???")
            index += 1
        if starting_index != 0:
            print("A. Previous Page")
        if index != len(V.encyclopedia_consumable_items_order):
            print("D. Next Page")
        print("0. Back")
        print("Type in the number of the action or the action itself.")
        action = input()
        if action.lower() in ["0", "back"]:
            break
        elif (action == "a" or "previous" in action.lower()) and starting_index != 0:
            page -= 1
        elif (action == "d" or "next" in action.lower()) and index != len(V.encyclopedia_consumable_items_order):
            page += 1
        elif action.strip() == "":
            pass
        elif action.isdigit():
            action = int(action) - 1
            if action in range(len(V.encyclopedia_consumable_items_order)):
                item_index = V.encyclopedia_consumable_items_order[action]
                if item_index in V.encyclopedia_consumable_items_entries:
                    print("\n")
                    item_entry(V, item_index)
                else:
                    print("\n\nThis item entry is locked!\nType anything to continue...")
                    action = input()
        else:
            for i in V.encyclopedia_consumable_items_order:
                if i in V.encyclopedia_consumable_items_entries and action.lower() in V.consumable_item_names[i].lower():
                    item_entry(V, i)
                    break

def item_entry(V, item_id):
    print(cons_item_name_color(V, item_id) + V.consumable_item_names[item_id] + "\033[0m")
    print("Description:", cons_item_name_color(V, item_id) + V.consumable_item_desc[item_id] + "\033[0m")
    print("Method(s) of obtaining: ", end = "")
    counter = 0
    for i in V.consumable_obtainment_methods[item_id]:
        if counter > 0:
            print("; ", end = "")
        if i == "none":
            print("None", end = "")
        elif i == "shopkeeper":
            print("\033[38;2;100;220;100mShopkeeper", end = "")
        elif i == "mimic":
            print("\033[38;2;200;240;0mGolden Chest", end = "")
        elif i == "alchemist":
            print("\033[38;2;200;0;150mAlchemist", end = "")
        elif i == "brewing":
            print("\033[38;2;200;200;150mBrewing", end = "")
        elif i == "remnants":
            print("\033[33;1mWarrior's Remnants", end = "")
        elif i == "reaper":
            print("\033[38;2;230;50;0mBounty Chieftain", end = "")
        elif i == "enemy drop":
            enemies_known = False
            enemies_who_drop = []
            for r in V.material_drops:
                if item_id in r[1] and r[0] in V.bestiary_entries:
                    enemies_known = True
                    enemies_who_drop.append(r[0])
            if enemies_known:
                counter_2 = 0
                print("Enemies: ", end = "")
                for r in enemies_who_drop:
                    if counter_2 > 0:
                        print(", ", end = "")
                    print(enemy_name_color(V, r) + V.enemys_name[r], end = "\033[0m")
                    counter_2 += 1
        counter += 1
        print("\033[0m", end = "")
    print()
    used_in_brewery_recipes = []
    got_in_brewery_recipes = []
    for i in V.recipes:
        if not V.recipes.index(i) in V.encyclopedia_recipe_entries:
            continue
        if item_id in i[0]:
            used_in_brewery_recipes.append(i)
        elif item_id in i[1]:
            got_in_brewery_recipes.append(i)
    if len(got_in_brewery_recipes) > 0:
        print("Can be obtained by:")
        for i in got_in_brewery_recipes:
            counter = 0
            for k in i:
                if counter > 0:
                    print(" = ", end = "")
                counter_2 = 0
                for l in k:
                    if counter_2 > 0:
                        print(" + ", end = "")
                    print(cons_item_name_color(V, l) + V.consumable_item_names[l], end = "\033[0m")
                    counter_2 += 1
                counter += 1
            print()
    if len(used_in_brewery_recipes) > 0:
        print("Can be used for:")
        for i in used_in_brewery_recipes:
            counter = 0
            for k in i:
                if counter > 0:
                    print(" = ", end = "")
                counter_2 = 0
                for l in k:
                    if counter_2 > 0:
                        print(" + ", end = "")
                    print(cons_item_name_color(V, l) + V.consumable_item_names[l], end = "\033[0m")
                    counter_2 += 1
                counter += 1
            print()
            
    print("\n\nType anything to continue...")
    action = input()

def brewing(V):
    ingredients = []
    if V.alchemist_brewing_first_time:
        print('''You come up to the brewing station. \033[38;2;200;0;150mThe alchemist\033[0m comes closer and says,''')
        if V.alchemist_anger <= 1:
            print('''\033[38;2;200;0;150m"Ah, I uze zis zing to brew my potionz. It'z quite zimple."
"Put iengriediantz into water. Heat it up and mix."\033[0m''')
        else:
            print('''\033[38;2;200;0;150m"Uzing my brewer? Fikure it out yourzelf."\033[0m''')
        print('''He turns around and walks back to the selling stand.''')
        V.alchemist_brewing_first_time = False
        print("Type anything to continue...")
        action = input()
    else:
        print('''You come up to the brewing station.''')
    while True:
        print("\nThe current ingredients:")
        if len(ingredients) == 0:
            print("None", end = "")
        else:
            counter = 0
            for i in ingredients:
                if counter > 0:
                    print(", ", end = "")
                counter += 1
                print(cons_item_name_color(V, i) + V.consumable_item_names[i] + "\033[0m", end = "")
        print("\n\n1. Add an ingredient")
        print("2. Heat and mix")
        print("3. Take out the ingredients")
        print("4. Back to shop")
        print("Type in the number of action.")
        action = input()
        print("\n")
        if action.lower() in ["1", "add", "add an ingredient"]:
            if len(V.player_items) == 0:
                print("You don't have any items!\nType anything to continue...")
                action = input()
            else:
                page = 0
                while True:
                    counter = 0
                    starting_index = page * 10
                    index = starting_index
                    while index < starting_index + 10 and index < len(V.player_items):
                        counter += 1
                        print(str(index + 1) + ".", cons_item_name_color(V, V.player_items[index]) + V.consumable_item_names[V.player_items[index]] + "\033[0m")
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
                            ingredients.append(item)
                            V.player_items.remove(item)
                            break
        elif action.lower() in ["2", "heat", "mix", "craft", "heat and mix"]:
            craftable = False
            for i in V.recipes:
                if sorted(i[0]) == sorted(ingredients):
                    if not V.recipes.index(i) in V.encyclopedia_recipe_entries and ingredients != []:
                        V.encyclopedia_recipe_entries.append(V.recipes.index(i))
                    craftable = True
                    ingredients = i[1]
                    print('''You turn on the flame under the pot and mix the ingredients. After a few seconds you notice something changing in the brewing station.
You turn off the flame and notice that you have ''', end = "")
                    if ingredients == []:
                        print("nothing", end = "")
                    else:
                        counter = 0
                        for i in ingredients:
                            if counter > 0:
                                print(", ", end = "")
                            counter += 1
                            print(cons_item_name_color(V, i) + V.consumable_item_names[i] + "\033[0m", end = "")
                    print(''' in your pot!
Type anything to continue...''')
                    action = input()
                    break
            if craftable == False:
                print('''As you reach to turn on the flame under the pot, \033[38;2;200;0;150mthe alchemist\033[0m rushes in and stops you.
\033[38;2;200;0;150m"Wat are you doink?! Are you tryink to blow up my brewery? Zis is not a correct recype! Do zomezink elze."\033[0m
He returns to his selling stand.
Type anything to continue...''')
                action = input()

        elif action.lower() in ["3", "take", "take out the ingredients"]:
            V.player_items = V.player_items + ingredients
            for i in ingredients:
                if not i in V.encyclopedia_consumable_items_entries:
                    V.encyclopedia_consumable_items_entries.append(i)
            ingredients = []
        elif action.lower() in ["4", "back", "shop", "back to shop"]:
            if len(ingredients) == 0:
                break
            else:
                print("Take out your ingredients before leaving!\nType anything to continue...")
                action = input()



def extras(V):
    while True:
        print('''1. Bestiary
2. Item Encyclopedia
9. Back''')
        action = input()
        if action.lower() in ["1", "bestiary"]:
            bestiary(V)
        elif action.lower() in ["2", "item", "item encyclopedia"]:
            item_encyclopedia(V)
        elif action == "9" or "back" in action.lower():
            break