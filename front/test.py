import matplotlib.pyplot as plt
import numpy as np


def creer_rose_des_vents(probas):
    """
    Crée et affiche une rose des vents à partir de probabilités directionnelles, sans la bibliothèque windrose.

    Args:
        probas (dict): Un dictionnaire contenant les probabilités pour chaque direction.
                       Les clés doivent être les points cardinaux (N, NE, E, SE, S, SO, O, NO).
                       Les valeurs doivent être des nombres entre 0 et 1 représentant les probabilités.
    """

    # Vérification des données
    if len(probas) != 8:
        raise ValueError("Le dictionnaire doit contenir 8 directions.")
    if not all(0 <= probas[direction] <= 1 for direction in probas):
        raise ValueError("Les probabilités doivent être entre 0 et 1.")

    # Conversion des probabilités en fréquences (pour l'affichage)
    freqs = np.array(list(probas.values())) * 100

    # Création des directions en radians
    dirs_rad = np.deg2rad(np.array([0, 45, 90, 135, 180, 225, 270, 315]))

    # Création de la figure et des axes polaires
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Largeur des barres
    width = np.deg2rad(45)  # 45 degrés en radians

    # Création des barres
    bars = ax.bar(dirs_rad, freqs, width=width, bottom=0.0)

    # Mise en page
    ax.set_theta_zero_location("N")  # Le zéro est au Nord
    ax.set_theta_direction(-1)  # Sens horaire
    ax.set_thetagrids(np.degrees(dirs_rad))  # Affiche les degrés
    ax.set_title("Rose des vents des probabilités directionnelles")
    ax.set_rlabel_position(0)  # Position labels des rayons
    ax.set_rticks(np.linspace(0, max(freqs) + 10, 4))  # Ajuste les ticks radiaux
    ax.set_rlabel_position(22.5)  # Positionne les labels radiaux au milieu des barres

    # Ajout des étiquettes de direction (N, NE, E, etc.)
    direction_labels = ['N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO']
    ax.set_xticklabels(direction_labels)

    # Affichage du graphique
    plt.show()


# Exemple d'utilisation
probas_exemple = {
    'N': 0.5,
    'NE': 0.1,
    'E': 0.06,
    'SE': 0.06,
    'S': 0.06,
    'SO': 0.06,
    'O': 0.06,
    'NO': 0.1
}


creer_rose_des_vents(probas_exemple)
