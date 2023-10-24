from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import calculador
import colorama

def burcarCoord(add):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    navegador = webdriver.Chrome(options=options)
    wait = WebDriverWait(navegador, 10)
    navegador.get(f'https://www.google.com/maps/place/{add}')
    time.sleep(5)
    url = navegador.current_url
    url = url.split('@')[1]
    url = url.split(',')
    
    return (float(url[0]), float(url[1]))

if __name__ == '__main__':
    
    repetir = True
    i = 1
    points = []

    startPoint = input('Digite o ponto inicial: ')
    startPoint = startPoint.split(' ')
    if 'Endereço:' in startPoint:
        startPoint.pop(0)

    end = ''

    for j, word in enumerate(startPoint):

        if j == 0:
            end = word
        else:
            end += ' ' + word
    startPoint = end
    startPoint = burcarCoord(startPoint)

    while repetir:
        point = input(f"\nQual o ponto {i}? [Presione enter sem escrever nada para finalizar a coleta de pontos]\n")
        if point == '':
            break
        point = point.split(' ')
        if 'Endereço:' in point:
            point.pop(0)
        end = ''
        for j, word in enumerate(point):
            if j == 0:
                end = word
            else:
                end += ' ' + word
        point = end
        point = burcarCoord(point)
        points.append(point)
        i += 1

    
    url = calculador.calcularRota(points, startPoint)
    print(colorama.Fore.CYAN + str(url) + colorama.Fore.RESET)