import pyautogui
import time
import webbrowser

def show():
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab('https://treinamento.koden.com.br/Usuarios/Create')
    print('Posicione o MOUSE')
    time.sleep(2)
    x, y = pyautogui.position()
    print ("Posicao atual do mouse:")
    print ("x = "+str(x)+" y = "+str(y))