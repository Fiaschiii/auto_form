import time 
import pyautogui
from playwright.sync_api import sync_playwright
import pyperclip
import keyboard
import pandas as pd


# importar os dados da tabela de funcionários
tabela = pd.read_csv("funcionarios_brasil_150.csv")



# Automação para preenchimento de formulário Google Forms
print("Início do código...")
def main():

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
        time.sleep(1)
        page.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', "Miguel")
        
        # sobrenome
        time.sleep(1)
        page.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input', "Fiaschi")
        
        # setor
        time.sleep(1)
        page.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea', "TI")

        # id empresa 
        time.sleep(1)
        page.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input', "1002")

        # cargo 
        time.sleep(1)
        page.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea', "Developer")

        # enviar
        time.sleep(1)
        page.locator('xpath=//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

        
        time.sleep(1)
        pyautogui.hotkey("win", "down")
        pyautogui.hotkey("win", "down")


        time.sleep(5)
        browser.close()

       
main()
print("Fim do código.")   




        
    
    




    





    
