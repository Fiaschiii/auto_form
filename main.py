import time 
import pyautogui
from playwright.sync_api import sync_playwright
import pandas as pd


# leitura dos dados da tabela
tabela = pd.read_csv("funcionarios_brasil_150.csv")



# Automação para preenchimento de formulário Google Forms
print("Início do código...")
def main():
    for linha in tabela.index:
        # puxar os dados da tabela aqui dentro do loop
        nome = str(tabela.loc[linha, "Nome"])
        sobrenome = str(tabela.loc[linha, "Sobrenome"])
        setor = str(tabela.loc[linha, "Setor"])
        id_empresa = str(tabela.loc[linha, "ID da Empresa"])
        cargo = str(tabela.loc[linha, "Cargo"])

        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False,
                args=["--start-maximized"]
            )
            
            context = browser.new_context(viewport=None)
            page = context.new_page()
            page.goto("https://forms.gle/bSTZ11m5g311F6an6")
            
            time.sleep(1)
            pyautogui.hotkey("win", "up")
            
            # nome  
            time.sleep(0.5)
            page.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', nome)
            
            # sobrenome
            time.sleep(0.5)
            page.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input', sobrenome)
            
            # setor
            time.sleep(0.5)
            page.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea', setor)
            
            # id empresa 
            time.sleep(0.5)
            page.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', id_empresa)
            
            # cargo 
            time.sleep(0.5)
            page.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea', cargo)
            
            # enviar
            time.sleep(0.5)
            page.locator('xpath=//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
            pyautogui.press("home")
            


            
            


           
            

       
main()
print("Fim do código.")   




        
    
    




    





    
