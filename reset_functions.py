

def true_reset(V):
    from enemies_and_fighting import default_enemies
    from areas import default_areas
    V.player_max_hp = 100
    V.player_base_def = 0
    V.player_base_dmg = 5
    V.player_base_magic_def = 0
    V.player_extra_magic_def = 0
    V.player_min_extra_magic_def = 0
    V.player_crit_chance = 5
    V.player_weapon = 0
    V.player_poison = 0
    V.player_spikes = 0
    V.player_money = 0
    V.player_xp = 0
    V.player_level = 0
    V.lost = 0
    V.win = 0
    V.score = 0
    V.raid_counter = 0
    V.difficulty = V.original_difficulty
    V.score_increase = 0
    V.max_power_level = 1
    V.max_power_level_increase = 0
    V.player_shield = 0
    V.player_magic_shield = 0
    V.player_gold_boost = 0
    V.player_damage_range_boost = 0
    V.player_poison_def = 0
    V.player_spikes_armor_break = 0
    V.player_crit_chance_reduction = 100
    V.last_boss = []
    V.is_boss_battle = False
    V.player_lifesteal = 0
    V.player_immortality = 0
    V.player_current_immortality = V.player_immortality
    V.player_regen = 0
    V.player_consume = 0
    V.player_travel = 0
    V.player_enemy_explotano = 0
    V.player_extra_life = False
    V.player_spent_life = False
    V.player_dodge_chance = 0
    V.player_dodge_count = 0
    V.player_dodged = False
    V.player_weapon_wrath = 0
    V.player_items = []
    V.player_inventory_weapons = []
    V.player_inventory_weapons_psn = []
    V.player_inventory_weapons_explotano = []
    V.player_inventory_weapons_lifesteal = []
    V.player_inventory_weapons_wrath = []
    V.last_altar = []
    V.debt = 0
    V.shopkeeper_sus = 0
    V.shopkeeper_deaths = 0
    V.cur_shopkeeper_dead = False
    V.mimic_bank_encounters = 0
    V.bank_first_time = True
    V.bank_money = 4
    V.alchemist_anger = 0
    V.alchemist_visited = False
    V.bought_from_alchemist = False
    V.alchemist_brewing_first_time = True
    V.brewery_encounters = 0
    V.reaper_trust = 0
    V.reaper_encounters = 0
    V.bounty_target = [-1, -1, -1]
    V.bounty_target_tracking = [0, 0, 0]
    V.bounty_target_goal = [0, 0, 0]
    V.herbalist_encounters = 0
    V.said_dialogue_shopkeeper = []
    V.said_dialogue_gamble_mimic = []
    V.said_dialogue_bank_mimic = []
    V.said_dialogue_boat_person = []
    V.said_dialogue_alchemist = []
    V.said_dialogue_change = []
    V.said_dialogue_reaper = []
    V.said_dialogue_herbalist = []
    V.stalker_stealth = 100
    V.vitality_anger = 0
    V.strength_anger = 0
    V.might_anger = 0
    V.protection_anger = 0
    V.fear_anger = 0
    V.mimic_gamble_encounters = 0
    V.death_encounters = 0
    V.player_oxygen = 3
    V.player_boat = False
    V.death_defeated = False
    V.change_encounters = 0
    V.change_recruited = False
    V.final_area = False
    default_enemies(V)
    default_areas(V)

def settings_reset(V):
    V.weather_amount = 1
    V.original_difficulty = 55
    V.scaling_style = "V0.3.7"
    
def reset_player(V):
    V.player_max_hp = 100
    V.player_base_def = 0
    V.player_base_dmg = 5
    V.player_base_magic_def = 0
    V.player_crit_chance = 5
    V.player_poison = 0
    V.player_spikes = 0
    V.player_money = 0
    V.player_items = []
    V.player_weapon = 0
    V.player_inventory_weapons = []
    V.player_inventory_weapons_psn = []
    V.player_inventory_weapons_explotano = []
    V.player_inventory_weapons_lifesteal = []
    V.player_inventory_weapons_wrath = []
    print("You lost everything but your life.")