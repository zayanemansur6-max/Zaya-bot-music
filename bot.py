import time
from playwright.sync_api import sync_playwright

def rodar_bot():
    with sync_playwright() as p:
        # Abre um navegador invisível na nuvem
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Entra no site do MyMuze
        url_musica = "https://mymuze.vm.co.mz/"
        print("Entrando no site...")
        page.goto(url_musica)
        
        # Espera um pouco para a página carregar
        time.sleep(5)
        
        print("Música iniciada! Aguardando 30 segundos...")
        time.sleep(30)
        
        print("Tempo concluído.")
        browser.close()

if __name__ == "__main__":
    rodar_bot()
  
