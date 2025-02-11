

from audioop import add


def enemy_name_color(V, enemy_id = 0):
    string = "\033[38;2"
    for i in range(3):
        try:
            string = string + ";" + str(V.enemys_name_colors[enemy_id][i])
        except:
            string = string + ";255"
    string = string + "m"
    return string

def area_color(V, height = 5, affected_by_weather = False, affected_by_time = False):
    string = "\033[38;2"
    weather_colors = []
    weather_color_effect = 0
    readable = False
    if affected_by_time and not V.area_id in [2, 6]:
        if V.game_time >= 6 and V.game_time < 12:
            factor = 1
        elif V.game_time < 6:
            factor = (V.game_time + 3) / 9 + 0.45
            if factor > 1:
                factor = 1
        elif V.game_time >= 12 and V.game_time < 18:
            factor = (17 - V.game_time) / 9 + 0.45
        else:
            factor = (V.game_time - 20) / 9 + 0.45
            if factor < 0.45:
                factor = 0.45
    else:
        factor = 1
    factor = factor * V.V_gamma
    for i in range(3):
        #try:
            if affected_by_weather and (1 in V.current_weather or 6 in V.current_weather or 7 in V.current_weather or 8 in V.current_weather):
                weather_colors.append(V.water_colors_0[V.area_id][i])
            if affected_by_weather and 5 in V.current_weather:
                weather_colors.append(50)
            if affected_by_weather and (2 in V.current_weather or 4 in V.current_weather):
                weather_colors.append(200)
            if affected_by_weather and 9 in V.current_weather:
                weather_colors.append(140)
            if len(weather_colors) > 0:
                counter = 0
                for r in weather_colors:
                    counter += 1
                    weather_color_effect += r
                weather_color_effect = weather_color_effect // counter
            else:
                weather_color_effect = V.areas_colors[V.area_id][i]
            color = round(((V.areas_colors[V.area_id][i] + weather_color_effect) // 2) * factor)
            if V.area_id != 6:
                color = color + int(12 * height) - 60
            else:
                color = color + int(7 * height) - 35
            if color > 255:
                color = 255
            elif color < 0:
                color = 0
            string = string + ";" + str(color)
            if color >= 35:
                readable = True
        #except:
            #string = string + ";255"
    if readable == False:
        string = "\033[38;2;35;35;35"
    string = string + "m"
    return string

def represented_area_color(V, area=0):
    string = "\033[38;2"
    for i in range(3):
        color = V.areas_colors[area][i]
        string = string + ";" + str(color)
    string = string + "m"
    return string

def water_color(V, water_type = 0, affected_by_time = False):
    string = "\033[38;2"
    if affected_by_time and not V.area_id in [2, 6]:
        if V.game_time >= 6 and V.game_time < 12:
            factor = 1
        elif V.game_time < 6:
            factor = V.game_time / 9 + 0.45
        elif V.game_time >= 12 and V.game_time < 18:
            factor = (17 - V.game_time) / 9 + 0.45
        else:
            factor = 0.45
    else:
        factor = 1
    factor = factor * V.V_gamma
    for i in range(3):
        try:
            additive_string = 0
            if water_type == 0:
                additive_string = round(V.water_colors_0[V.area_id][i] * factor)
            elif water_type == 1:
                additive_string = round(V.water_colors_1[V.area_id][i] * factor)
            if additive_string < 0:
                additive_string = 0
            elif additive_string > 255:
                additive_string = 255
            string = string + ";" + str(additive_string)
        except:
            string = string + ";50"
    string = string + "m"
    return string
