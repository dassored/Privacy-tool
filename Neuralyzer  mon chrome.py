import os

# Chemin vers le dossier de profil Chrome
profile_path = os.path.expanduser("~/.config/google-chrome/Default")

# Effacer l'historique de navigation
os.system(f"rm -r {profile_path}/History {profile_path}/History Provider Cache")

# Effacer les cookies

os.system(f"rm -r {profile_path}/Cookies {profile_path}/Cookies-journal")

# Effacer les mots de passe enregistrés
os.system(f"rm -r {profile_path}/Login Data {profile_path}/Login Data-journal")

# Effacer les données de formulaire
os.system(f"rm -r {profile_path}/Web Data {profile_path}/Web Data-journal")

print("Votre Chrome a été Neuralyzer avec succès !")
