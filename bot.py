import time
from playwright.sync_api import sync_playwright

def rodar_bot():
    with sync_playwright() as p:
        # Abre um navegador invisível na nuvem
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Link exato da música/tag do MyMuze
        url_musica = "https://api.prod.kuackmedia.com/share/mymuze/tag/197/Pop?redirect=1"
        print("Entrando no link do MyMuze...")
        page.goto(url_musica)
        
        # Espera a página carregar e redirecionar
        page.wait_for_load_state("networkidle")
        time.sleep(5)
        
        # Tenta dar play na música (clicando no botão ou simulando a tecla de espaço)
        try:
            page.click('button[aria-label*="Play"], .play-btn, button.play', timeout=5000)
            print("Botão de play acionado!")
        except:
            # Caso não ache o botão exato, simula apertar espaço para tocar
            page.keyboard.press("Space")
            print("Comando de play enviado via teclado.")
        
        print("Música iniciada! Aguardando 30 segundos...")
        time.sleep(30)
        
        print("Tempo concluído com sucesso.")
        browser.close()

if __name__ == "__main__":
    rodar_bot()
