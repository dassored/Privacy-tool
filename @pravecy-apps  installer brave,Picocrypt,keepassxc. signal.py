import tkinter as tk
import urllib.request
import subprocess
import os

class applications(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Installateur d'applications")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Cliquez sur les boutons pour télécharger et installer les applications")
        self.label.pack()

        self.brave_button = tk.Button(self, text="Installer Brave", command=self.install_brave)
        self.brave_button.pack()

        self.picocrypt_button = tk.Button(self, text="Installer Picocrypt", command=self.install_picocrypt)
        self.picocrypt_button.pack()

        self.keepassxc_button = tk.Button(self, text="Installer KeepassXC", command=self.install_keepassxc)
        self.keepassxc_button.pack()

        self.signal_button = tk.Button(self, text="Installer Signal", command=self.install_signal)
        self.signal_button.pack()

        self.quit_button = tk.Button(self, text="Quitter", command=self.master.destroy)
        self.quit_button.pack()

    def install_brave(self):
        self.label.config(text="Téléchargement de Brave en cours...")
        url = "https://laptop-updates.brave.com/latest/winx64"
        filename = "BraveBrowserSetup.exe"
        urllib.request.urlretrieve(url, filename)
        self.label.config(text="Installation de Brave en cours...")
        subprocess.Popen([filename, '/silent', '/install'])
        self.label.config(text="Brave a été installé avec succès !")

    def install_picocrypt(self):
        self.label.config(text="Installation de Picocrypt en cours...")
        subprocess.Popen(["powershell", "choco install picocrypt"])
        self.label.config(text="Picocrypt a été installé avec succès !")

    def install_keepassxc(self):
        self.label.config(text="Installation de KeepassXC en cours...")
        subprocess.Popen(["powershell", "choco install keepassxc"])
        self.label.config(text="KeepassXC a été installé avec succès !")

    def install_signal(self):
        self.label.config(text="Installation de Signal en cours...")
        subprocess.Popen(["powershell", "choco install signal-desktop"])
        self.label.config(text="Signal a été installé avec succès !")

root = tk.Tk()
app = applications(master=root)
app.mainloop()
