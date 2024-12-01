

def enemy_name_color(V, enemy_id = 0):
    string = "\033[38;2"
    for i in range(3):
        try:
            string = string + ";" + str(V.enemys_name_colors[enemy_id][i])
        except:
            string = string + ";255"
    string = string + "m"
    return string

def area_color(V, height = 5, affected_by_weather = False):
    string = "\033[38;2"
    weather_colors = []
    weather_color_effect = 0
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
            color = (V.areas_colors[V.area_id][i] + weather_color_effect) // 2
            if V.area_id != 6:
                color = color + int(12 * height) - 60
            else:
                color = color + int(7 * height) - 35
            if color > 255:
                color = 255
            elif color < 0:
                color = 0
            string = string + ";" + str(color)
        #except:
            #string = string + ";255"
    string = string + "m"
    return string

def represented_area_color(V, area=0):
    string = "\033[38;2"
    for i in range(3):
        color = V.areas_colors[area][i]
        string = string + ";" + str(color)
    string = string + "m"
    return string

def water_color(V, water_type = 0):
    string = "\033[38;2"
    for i in range(3):
        try:
            if water_type == 0:
                string = string + ";" + str(V.water_colors_0[V.area_id][i])
            elif water_type == 1:
                string = string + ";" + str(V.water_colors_1[V.area_id][i])
        except:
            string = string + ";50"
    string = string + "m"
    return string
