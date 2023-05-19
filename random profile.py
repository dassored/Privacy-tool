import random
import string

# Liste de prénoms masculins
first_names = ["Eric", "Michael", "Bruce", "James", "Peter", "David", "Joseph", "Daniel"]

# Liste de noms de famille
last_names = ["Smith", "Johnson", "Brown", "Davis", "Miller", "Wilson", "Moore", "Larson"]

# Générer un profil complet
def generate_profile():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    gender = "Masculin"
    username = generate_username(first_name, last_name)
    password = generate_password()

    profile = {
        "Prénom": first_name,
        "Nom": last_name,
        "Genre": gender,
        "Pseudo": username,
        "Mot de passe": password
    }

    return profile

# Générer un pseudo à partir du prénom et du nom de famille
def generate_username(first_name, last_name):
    username = first_name.lower() + last_name.lower() + random.choice(string.digits)
    return username

# Générer un mot de passe complexe
def generate_password():
    password_length = random.randint(10, 15)
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    return password

# Générer un profil complet
profile = generate_profile()

# Afficher le profil
for key, value in profile.items():
    print(f"{key}: {value}")

