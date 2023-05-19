import os
import shutil

# Chemin vers le dossier de cache de Chrome
cache_path = os.path.expanduser("~/.cache/google-chrome/Default/Cache")

# Supprimer tous les fichiers du cache
shutil.rmtree(cache_path)

# Recréer le dossier du cache
os.makedirs(cache_path)

# Chemin vers le fichier des cookies de Chrome
cookies_path = os.path.expanduser("~/.config/google-chrome/Default/Cookies")

# Supprimer le fichier des cookies
os.remove(cookies_path)

# Chemin vers le dossier de l'historique de navigation de Chrome
history_path = os.path.expanduser("~/.config/google-chrome/Default/History")

# Supprimer le dossier de l'historique de navigation
shutil.rmtree(history_path)

# Recréer le dossier de l'historique de navigation
os.makedirs(history_path)

# Chemin vers le fichier des données de formulaire de Chrome
form_data_path = os.path.expanduser("~/.config/google-chrome/Default/Web Data")

# Supprimer le fichier des données de formulaire
os.remove(form_data_path)

print("Votre Chrome a été Neuralyzer avec succès le cache de Chrome a été vidé et la vie privée du navigateur a été améliorée  !")

