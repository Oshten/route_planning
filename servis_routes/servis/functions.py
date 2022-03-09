import json

def distance_between_points(coordinats_1: tuple, coordinats_2: tuple):
    """Определение расстояния между двумя точками на кардинатной сетке"""
    try:
        distance = ((int(coordinats_1[0])-int(coordinats_2[0]))**2 +
                    (int(coordinats_1[1])-int(coordinats_2[1]))**2)**(0.5)
    except ValueError:
        print('Неверные координаты')
        distance = 0
    return distance


def determining_length_route(route: dict):
    """Определение растояние между маршрутами"""
    route['length_route'] = 0
    route['startpoint'] = json.loads(route['startpoint'].replace("'", '"'))
    route['endpoint'] = json.loads(route['endpoint'].replace("'", '"'))
    route['waypoints'] = json.loads(route['waypoints'].replace("'", '"'))
    route['length_route'] += distance_between_points(
        (route['startpoint']['latitude'], route['startpoint']['longitude']),
        (route['waypoints'][0]['latitude'], route['waypoints'][0]['longitude'])
    )
    for index, point in enumerate(route['waypoints']):
        if index == 0:
            previous_point = point
            continue
        route['length_route'] += distance_between_points(
            (previous_point['latitude'], previous_point['longitude']),
            (point['latitude'], point['longitude'])
        )
    route['length_route'] += distance_between_points(
        (route['waypoints'][-1]['latitude'], route['waypoints'][0]['longitude']),
        (route['endpoint']['latitude'], route['endpoint']['longitude'])
    )
    route['length_route'] = round(route['length_route'], 2)
    return route