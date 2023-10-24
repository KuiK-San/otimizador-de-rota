import math
import random
import colorama
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
    print(colorama.Fore.RED + str(url) + colorama.Fore.RESET)

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
    print(colorama.Fore.CYAN + str(url) + colorama.Fore.RESET)


if __name__ == "__main__":
    repetir = True
    while repetir:
        startPoint = input('Insira o endereço inicial:\n')
        url = f'https://us1.locationiq.com/v1/search?key=pk.8f71e14e24927150bc7d607a0c4b0c49&q={startPoint}&format=json'
        response = requests.get(url=url)
        
        if response.status_code == 200:
            # print(response.json())
            resposta = response.json()
            escolha = input(f"{resposta[0]['display_name'].split('Região')[0]}é o endereço correto? [1] SIM [0] NÃO\n")
            if len(escolha) == 1:
                if int(escolha) == 1:
                    startPoint = [resposta[0]['lat'],resposta[0]['lon']]
                    repetir = False
            else:
                print('invalido')
        else:
            print('Falha na procura...')

    repetir = True
    i = 1
    points = []
    while repetir:
        point = input(f'Insira o {i} ponto:\n')
        url = f'https://us1.locationiq.com/v1/search?key=pk.8f71e14e24927150bc7d607a0c4b0c49&q={point}&format=json'
        response = requests.get(url=url)

        if response.status_code == 200:
            # print(response.json())
            resposta = response.json()
            escolha = input(f"{resposta[0]['display_name'].split('Região')[0]}é o endereço correto? [1] SIM [0] NÃO\n")
            if len(escolha) == 1:
                if int(escolha) == 1:
                    points.append([resposta[0]['lat'],resposta[0]['lon']])
                    escolha = input(f"Deseja adicionar mais um ponto? [1] SIM [0] NÃO\n")
                    i += 1
                    if len(escolha) == 1:
                        if int(escolha) == 0:
                            repetir = False
                    else:
                        print('Invalido')

            else:
                print('Invalido')
        else:
            print('Falha na procura...')
    
    print('Criando melhor rota...')

    calcularRota(points, startPoint)