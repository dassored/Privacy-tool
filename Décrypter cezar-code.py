import string

# Demander l'entrée de l'utilisateur
message = input("Entrez le message chiffré: ")

# Brute force pour déchiffrer le message
for key in range(len(string.ascii_lowercase)):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - key - 97) % 26 + 97)
            decrypted_message += shifted_char.upper() if char.isupper() else shifted_char
        else:
            decrypted_message += char
    print(f"clé={key}: {decrypted_message}")
