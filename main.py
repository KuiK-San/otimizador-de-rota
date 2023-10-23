import math
import random
import colorama

def calcular_distancia_geografica(lat1, lat2, lon1, lon2):

    raio_terra_metros = 6371000

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = raio_terra_metros * c

    return distancia

points = [(-49.25391333333334, -25.508744999999998),(-49.24901333333334, -25.515295),(-49.240494999999996, -25.51330666666667),(-49.23087833333334, -25.51711833333333),(-49.25783499999999, -25.50466833333333),( -49.2101635, -25.5415646),(-49.2103243, -25.536708),(-49.255829999999996, -25.505578333333332)]

# random.shuffle(points)

startPoint = (-49.2101635, -25.5415646)

url = f'https://www.google.com/maps/dir'
for point, j in enumerate(points):
    url = f'{url}/{points[point][1]},{points[point][0]}'
print(colorama.Fore.RED + str(url) + colorama.Fore.RESET)

route = []
i = 0
while len(points) != 0:
    route.append(startPoint)
    smallDistance = 9999999999
    for j, point in enumerate(points):
        distance = calcular_distancia_geografica(startPoint[1], point[1], startPoint[0], point[0])
        if distance < smallDistance:
            smallDistance = distance
            newPoint = j
    
    
    startPoint = points[newPoint]
    points.pop(newPoint)
    i+=1

url = f'https://www.google.com/maps/dir'
for point, j in enumerate(route):
    url = f'{url}/{route[point][1]},{route[point][0]}'
print(colorama.Fore.CYAN + str(url) + colorama.Fore.RESET)

