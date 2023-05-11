
import tkinter as tk
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Firefox Privacy Settings")
        self.master.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        self.instructions_label = tk.Label(self.master, text="Please make sure Firefox is closed before continuing.")
        self.instructions_label.pack(pady=10)

        self.execute_button = tk.Button(self.master, text="Execute", command=self.execute_script)
        self.execute_button.pack(pady=10)

    def execute_script(self):
        preferences = {
            "privacy.firstparty.isolate": "true",
            "privacy.resistFingerprinting": "true",
            "privacy.trackingprotection.fingerprinting.enabled": "true",
            "privacy.trackingprotection.cryptomining.enabled": "true",
            "privacy.trackingprotection.enabled": "true",
            "browser.send_pings": "false",
            "browser.urlbar.speculativeConnect.enabled": "false",
            "dom.event.clipboardevents.enabled": "false",
            "media.eme.enabled": "false",
            "media.gmp-widevinecdm.enabled": "false",
            "media.navigator.enabled": "false",
            "network.cookie.cookieBehavior": "1",
            "network.http.referer.XOriginPolicy": "2",
            "network.http.referer.XOriginTrimmingPolicy": "2",
            "webgl.disabled": "true",
            "browser.sessionstore.privacy_level": "2",
            "beacon.enabled": "false",
            "browser.safebrowsing.downloads.remote.enabled": "false",
            "network.dns.disablePrefetch": "true",
            "network.dns.disablePrefetchFromHTTPS": "true",
            "network.predictor.enabled": "false",
            "network.predictor.enable-prefetch": "false",
            "network.prefetch-next": "false",
            "network.IDN_show_punycode": "true"
        }

        try:
            os.system("start firefox.exe about:config")
            os.system("timeout 3")
            for pref, val in preferences.items():
                os.system(f'echo user_pref("{pref}", {val}); >> "%APPDATA%\\Mozilla\\Firefox\\Profiles\\*.default-release\\prefs.js"')
            os.system("taskkill /f /im firefox.exe")
            self.execute_button["text"] = "Success!"
            self.execute_button["state"] = "disabled"
        except Exception as e:
            self.execute_button["text"] = "Error"
            print(e)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
