from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import main
import colorama

def buscarCep(add):
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
    startPoint = buscarCep(startPoint)

    while repetir:
        point = input(f"Qual o ponto {i}?\n")
        point = buscarCep(point)
        points.append(point)

        continuar = input('Deseja inserir mais um ponto? [1] SIM [0] NÃO\n')
        i = i + 1
        if continuar == '0':
            repetir = False
        if continuar != '1':
            while continuar != '1':
                continuar = input('Deseja inserir mais um ponto? [1] SIM [0] NÃO\n')

    
    url = main.calcularRota(points, startPoint)
    print(colorama.Fore.CYAN + str(url) + colorama.Fore.RESET)