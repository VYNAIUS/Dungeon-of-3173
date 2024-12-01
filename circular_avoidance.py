


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