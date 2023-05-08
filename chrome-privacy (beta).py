
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import tkinter as tk

# Fonction pour activer le mode incognito
def enable_incognito():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.quit()

# Fonction pour activer le blocage des traqueurs
def enable_tracker_blocking():
    chrome_options = Options()
    chrome_options.add_extension('path/to/ublock/extension')
    driver = webdriver.Chrome(options=chrome_options)
    driver.quit()

# Création de l'interface graphique
root = tk.Tk()
root.title("Améliorer la vie privée sur Google Chrome")

incognito_button = tk.Button(root, text="Activer le mode incognito", command=enable_incognito)
incognito_button.pack()

tracker_blocking_button = tk.Button(root, text="Activer le blocage des traqueurs", command=enable_tracker_blocking)
tracker_blocking_button.pack()

root.mainloop()
