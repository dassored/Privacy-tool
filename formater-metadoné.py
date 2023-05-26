import tkinter as tk
from tkinter import filedialog
from PIL import Image, ExifTags

def remove_metadata():
    # Sélectionne le fichier image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        # Ouvre l'image en utilisant PIL
        image = Image.open(file_path)

        # Vérifie s'il y a des données EXIF
        if "exif" in image.info:
            # Obtient les données EXIF
            exif_data = image.info["exif"]

            # Décode les données EXIF
            exif_data_decoded = exif_data.decode()

            # Supprime les métadonnées EXIF
            clean_exif = {
                ExifTags.TAGS[tag]: exif_data_decoded[tag]
                for tag in exif_data_decoded.keys()
                if tag in ExifTags.TAGS
            }

            # Enregistre l'image sans métadonnées
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
            if save_path:
                image.save(save_path, exif=clean_exif)
                print("Métadonnées supprimées avec succès !")
        else:
            print("Aucune métadonnée à supprimer.")
    else:
        print("Aucun fichier sélectionné.")

# Crée une fenêtre Tkinter
window = tk.Tk()

# Ajoute un bouton pour sélectionner l'image
button = tk.Button(window, text="Sélectionner une image", command=remove_metadata)
button.pack()

# Lance la boucle principale de l'interface graphique
window.mainloop()
