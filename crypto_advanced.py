"""
TP Crypto : Chiffrement César et XOR
"""

# Fonction pour le chiffrement de César
def cesar(texte, decalage, mode="chiffrer"):
    # Si on veut déchiffrer, on décale dans l'autre sens
    if mode == "dechiffrer":
        decalage = -decalage
    
    resultat = ""
    for char in texte:
        # On traite les majuscules
        if char.isupper():
            # Formule : (Code ASCII - 65 + decalage) % 26 + 65
            resultat += chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
        # On traite les minuscules
        elif char.islower():
            resultat += chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))
        else:
            # On ne change pas les caractères spéciaux / chiffres
            resultat += char
    return resultat

# Fonction pour le chiffrement XOR
def xor_cipher(texte, cle):
    resultat = ""
    # On parcourt chaque lettre du texte
    for i, char in enumerate(texte):
        # On vérifie qu'on a une clé pour éviter les erreurs
        if len(cle) > 0:
            # On boucle sur la clé si elle est plus courte que le texte
            cle_char = cle[i % len(cle)]
            
            # Opération XOR bit à bit (^)
            char_chiffre = ord(char) ^ ord(cle_char)
            resultat += chr(char_chiffre)
        else:
            # Sans clé, on renvoie le texte tel quel
            resultat += char
    return resultat

# Dictionnaire pour appeler les fonctions plus facilement
ALGORITHMES = {
    "cesar": cesar,
    "xor": xor_cipher
}

def afficher_menu():
    print("\n" + "-"*30)
    print("MENU PRINCIPAL")
    print("-"*30)
    print("1 - Chiffrement César")
    print("2 - Chiffrement XOR")
    print("0 - Quitter")
    print("-"*30)



def main():
    print("Bienvenue dans le programme de chiffrement.")
    
    # Boucle infinie pour garder le menu ouvert
    while True:
        afficher_menu()
        
        try:
            choix = int(input("\nTon choix : "))
        except ValueError:
            print("Erreur : il faut entrer un nombre.")
            continue
        
        # Quitter le programme
        if choix == 0:
            print("Au revoir !")
            break
        
        # Sauvegarde

        
        # Algorithmes de chiffrement
        elif choix in [1, 2]:
            print("\n" + "-"*20)
            print("1 - Chiffrer")
            print("2 - Déchiffrer")
            
            try:
                action = int(input("Action : "))
                if action == 1:
                    mode = "chiffrer"
                else:
                    mode = "dechiffrer"
            except ValueError:
                print("Choix incorrect.")
                continue
            
            texte = input("Texte à traiter : ")
            
            if choix == 1: # César
                try:
                    decalage = int(input("Décalage (1-25) : "))
                    resultat = cesar(texte, decalage, mode)
                except ValueError:
                    print("Le décalage doit être un nombre.")
                    continue
            
            elif choix == 2: # XOR
                cle = input("Clé secrète : ")
                if not cle:
                    print("Erreur : La clé est vide.")
                    continue
                resultat = xor_cipher(texte, cle)
            
            print("\nRESULTAT :")
            print(resultat)
        
        else:
            print("Option inconnue.")

# Lancement du programme
if __name__ == "__main__":
    main()
