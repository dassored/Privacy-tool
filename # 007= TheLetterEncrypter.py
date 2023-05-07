# 007= cryptor et decrypter 

# Fonction pour encoder une phrase en transposition

def encode_transposition(message):
    encoded_message = ""
    for i in range (len (message) -1, -1, -1):
        encoded_message += message [i]
        return encoded_message

    # Fonction pour décoder une phrase en transposition
    def decode_transposition(encoded_message):
        decoded_message = ""
        for i in range (len(encoded_message) -1,-1, -1):
            decoded_message += encoded_message[i]
        return decoded_message

    # Demander l'entrée de l'utilisateur
    message = input ("entrer le message à coder : ")

    # Encoder le message en transposition
encoded_message = encodé_transposition(message)
print ("Message encodé :", encoded_message)

# Décoder le message en transposition
decoded_message = decode_transposition(encoded_message)
print("Message décrypté :", decoded_message)
