import os

def remove_files_with_string(directory, string):
    # Parcourir tous les fichiers et répertoires dans le répertoire donné
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Vérifier si le nom du fichier contient la chaîne spécifiée
            if string in file:
                # Construire le chemin absolu du fichier
                file_path = os.path.join(root, file)
                # Supprimer le fichier
                os.remove(file_path)
                print(f"File removed: {file_path}")

# Spécifier le répertoire dans lequel vous souhaitez supprimer les fichiers
directory_to_clean = os.getcwd()  # Dossier actuel
# Spécifier la chaîne de caractères à rechercher dans les noms de fichier
string_to_search = "Zone.Identifier"

remove_files_with_string(directory_to_clean, string_to_search)
