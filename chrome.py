import webbrowser

def openChrome(url = 'https://treinamento.koden.com.br/Usuarios/Create'):
    if (url != ""):
        site = url
    else:
        site = 'https://treinamento.koden.com.br/Usuarios/Create'

    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(site)