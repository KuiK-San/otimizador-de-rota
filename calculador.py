import math
import random
import requests

def calcular_distancia_geografica(lat1, lat2, lon1, lon2):

    raio_terra_metros = 6371000

    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = raio_terra_metros * c

    return distancia


def calcularRota(points, startPoint):

    url = f'https://www.google.com/maps/dir'
    for point, j in enumerate(points):
        url = f'{url}/{points[point][0]},{points[point][1]}'

    route = []
    i = 0
    while len(points) != 0:
        route.append(startPoint)
        smallDistance = 9999999999
        for j, point in enumerate(points):
            distance = calcular_distancia_geografica(startPoint[0], point[0], startPoint[1], point[1])
            if distance < smallDistance:
                smallDistance = distance
                newPoint = j
        
        
        startPoint = points[newPoint]
        points.pop(newPoint)
        i+=1

    url = f'https://www.google.com/maps/dir'
    for point, j in enumerate(route):
        url = f'{url}/{route[point][0]},{route[point][1]}'
    
    return url

