"""
🔐 CRYPTO ADVANCED - Chiffrement Multi-Algorithmes
===================================================
Script Python sophistiqué explorant plusieurs concepts avancés :
- Multiples algorithmes de chiffrement (César, Vigenère, XOR)
- Menu interactif avec boucle while
- Gestion d'erreurs avec try/except
- Dictionnaires pour stocker des fonctions
- Manipulation de fichiers

Objectif : Comprendre des concepts Python plus avancés de manière pédagogique
"""

# ═══════════════════════════════════════════════════════════════
# ALGORITHME 1 : CHIFFRE DE CÉSAR (déjà vu)
# ═══════════════════════════════════════════════════════════════

def cesar(texte, decalage, mode="chiffrer"):
    """
    Chiffrement César classique.
    mode : "chiffrer" ou "dechiffrer"
    """
    if mode == "dechiffrer":
        decalage = -decalage
    
    resultat = ""
    for char in texte:
        if char.isupper():
            resultat += chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
        elif char.islower():
            resultat += chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))
        else:
            resultat += char
    return resultat


# ═══════════════════════════════════════════════════════════════
# ALGORITHME 2 : CHIFFRE DE VIGENÈRE (NOUVEAU)
# ═══════════════════════════════════════════════════════════════

def vigenere(texte, cle, mode="chiffrer"):
    """
    Chiffrement de Vigenère - Plus sécurisé que César.
    
    FONCTIONNEMENT :
    ================
    Au lieu d'un décalage fixe, on utilise un MOT-CLÉ.
    Chaque lettre du mot-clé donne un décalage différent.
    
    Exemple :
        Texte : HELLO
        Clé   : KEY
        
        H + K (décalage 10) = R
        E + E (décalage 4)  = I
        L + Y (décalage 24) = J
        L + K (on recommence) = V
        O + E = S
        
        Résultat : RIJVS
    
    NOUVEAUX CONCEPTS :
    ===================
    - Modulo pour boucler sur la clé : cle[i % len(cle)]
    - Conversion lettre → décalage : ord(cle_char) - ord('A')
    """
    
    # Nettoyer la clé (enlever espaces, mettre en majuscules)
    cle = cle.upper().replace(" ", "")
    
    # Vérifier que la clé contient bien des lettres
    if not cle.isalpha():
        return "ERREUR : La clé doit contenir uniquement des lettres"
    
    resultat = ""
    index_cle = 0  # Position dans la clé
    
    for char in texte:
        if char.isalpha():
            # ═══════════════════════════════════════════════════════
            # CONCEPT CLÉ : Récupérer le décalage depuis la clé
            # ═══════════════════════════════════════════════════════
            # On prend la lettre actuelle de la clé
            # Si la clé est plus courte que le texte, on boucle avec %
            cle_char = cle[index_cle % len(cle)]
            
            # Convertir la lettre de la clé en décalage (0-25)
            # 'A' → 0, 'B' → 1, 'C' → 2, etc.
            decalage = ord(cle_char) - ord('A')
            
            # Si on déchiffre, inverser le décalage
            if mode == "dechiffrer":
                decalage = -decalage
            
            # Appliquer le décalage (comme César)
            if char.isupper():
                resultat += chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
            else:
                resultat += chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))
            
            # Passer à la lettre suivante de la clé
            index_cle += 1
        else:
            # Garder les non-lettres inchangées
            resultat += char
    
    return resultat


# ═══════════════════════════════════════════════════════════════
# ALGORITHME 3 : CHIFFREMENT XOR (NOUVEAU - NIVEAU AVANCÉ)
# ═══════════════════════════════════════════════════════════════

def xor_cipher(texte, cle):
    """
    Chiffrement XOR - Opération bit à bit.
    
    FONCTIONNEMENT :
    ================
    XOR (OU exclusif) est une opération mathématique binaire :
    - 0 XOR 0 = 0
    - 0 XOR 1 = 1
    - 1 XOR 0 = 1
    - 1 XOR 1 = 0
    
    Exemple avec un caractère :
        'A' en ASCII = 65 en décimal = 01000001 en binaire
        Clé 5        = 5 en décimal  = 00000101 en binaire
        
        XOR :  01000001
               00000101
               --------
               01000100  = 68 en décimal = 'D'
    
    PROPRIÉTÉ MAGIQUE :
    ===================
    XOR est son propre inverse !
    - chiffrer('A', 5) → 'D'
    - chiffrer('D', 5) → 'A'
    
    Donc : pas besoin de fonction déchiffrer, on utilise la même !
    
    NOUVEAUX CONCEPTS :
    ===================
    - Opérateur ^ : XOR en Python
    - ord() pour avoir le code ASCII
    - chr() pour reconvertir en caractère
    - % pour boucler sur la clé si elle est courte
    """
    
    resultat = ""
    
    for i, char in enumerate(texte):
        # ═══════════════════════════════════════════════════════
        # CONCEPT : enumerate() donne l'index ET la valeur
        # ═══════════════════════════════════════════════════════
        # enumerate("ABC") → (0, 'A'), (1, 'B'), (2, 'C')
        
        # Récupérer le caractère de clé correspondant (avec boucle)
        cle_char = cle[i % len(cle)]
        
        # ═══════════════════════════════════════════════════════
        # OPÉRATION XOR avec l'opérateur ^
        # ═══════════════════════════════════════════════════════
        # ord(char) : code ASCII du caractère du texte
        # ord(cle_char) : code ASCII du caractère de la clé
        # ^ : opérateur XOR
        char_chiffre = ord(char) ^ ord(cle_char)
        
        # Reconvertir en caractère
        resultat += chr(char_chiffre)
    
    return resultat


# ═══════════════════════════════════════════════════════════════
# CONCEPT AVANCÉ : DICTIONNAIRE DE FONCTIONS
# ═══════════════════════════════════════════════════════════════

# En Python, les fonctions sont des OBJETS
# On peut les stocker dans des variables, des listes, des dictionnaires !

ALGORITHMES = {
    "cesar": cesar,
    "vigenere": vigenere,
    "xor": xor_cipher
}

# Maintenant on peut appeler une fonction via le dictionnaire :
# ALGORITHMES["cesar"]("HELLO", 3) est équivalent à cesar("HELLO", 3)


# ═══════════════════════════════════════════════════════════════
# FONCTIONS UTILITAIRES
# ═══════════════════════════════════════════════════════════════

def afficher_menu():
    """Affiche le menu principal."""
    print("\n" + "="*60)
    print("🔐 CRYPTO ADVANCED - Menu Principal")
    print("="*60)
    print("1 - Chiffrement César")
    print("2 - Chiffrement Vigenère")
    print("3 - Chiffrement XOR")
    print("4 - Sauvegarder le résultat dans un fichier")
    print("0 - Quitter")
    print("="*60)


def sauvegarder_fichier(texte, nom_fichier="resultat.txt"):
    """
    Sauvegarde du texte dans un fichier.
    
    CONCEPT : Gestion de fichiers avec 'with'
    ==========================================
    with open(fichier, mode) as f:
        f.write(texte)
    
    Le 'with' garantit que le fichier sera fermé automatiquement,
    même en cas d'erreur !
    
    Modes :
    - "w" : write (écriture, écrase le contenu)
    - "r" : read (lecture)
    - "a" : append (ajouter à la fin)
    """
    try:
        # ═══════════════════════════════════════════════════════
        # CONCEPT : with open() - Gestionnaire de contexte
        # ═══════════════════════════════════════════════════════
        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            fichier.write(texte)
        print(f"✅ Résultat sauvegardé dans : {nom_fichier}")
        
    except Exception as e:
        # Si erreur (permissions, disque plein, etc.)
        print(f"❌ Erreur lors de la sauvegarde : {e}")


# ═══════════════════════════════════════════════════════════════
# PROGRAMME PRINCIPAL
# ═══════════════════════════════════════════════════════════════

def main():
    """
    Fonction principale avec menu interactif.
    
    CONCEPT : Boucle while True - Menu infini
    ==========================================
    while True:     → Boucle qui ne s'arrête jamais
        ...
        if choix == 0:
            break   → 'break' sort de la boucle
    """
    
    print("🎓 Bienvenue dans Crypto Advanced !")
    print("Explore plusieurs algorithmes de chiffrement en Python")
    
    dernier_resultat = ""  # Pour sauvegarder le dernier résultat
    
    # ═══════════════════════════════════════════════════════════
    # BOUCLE INFINIE POUR LE MENU
    # ═══════════════════════════════════════════════════════════
    while True:
        afficher_menu()
        
        # ═══════════════════════════════════════════════════════
        # GESTION D'ERREURS avec try/except
        # ═══════════════════════════════════════════════════════
        # Si l'utilisateur tape "abc" au lieu d'un nombre,
        # int("abc") provoque une erreur ValueError
        # On la capture avec except ValueError
        
        try:
            choix = int(input("\n👉 Ton choix : "))
        except ValueError:
            # L'utilisateur n'a pas tapé un nombre
            print("❌ Entrée invalide ! Tape un nombre.")
            continue  # 'continue' retourne au début de la boucle while
        
        # ═══════════════════════════════════════════════════════
        # OPTION 0 : Quitter
        # ═══════════════════════════════════════════════════════
        if choix == 0:
            print("\n👋 Au revoir !")
            break  # Sortir de la boucle while
        
        # ═══════════════════════════════════════════════════════
        # OPTION 4 : Sauvegarder
        # ═══════════════════════════════════════════════════════
        elif choix == 4:
            if dernier_resultat:
                nom = input("Nom du fichier (défaut: resultat.txt) : ") or "resultat.txt"
                sauvegarder_fichier(dernier_resultat, nom)
            else:
                print("❌ Aucun résultat à sauvegarder ! Chiffre d'abord un message.")
        
        # ═══════════════════════════════════════════════════════
        # OPTIONS 1-3 : Algorithmes de chiffrement
        # ═══════════════════════════════════════════════════════
        elif choix in [1, 2, 3]:
            print("\n" + "-"*60)
            
            # Choix de l'action
            print("1 - Chiffrer")
            print("2 - Déchiffrer")
            
            try:
                action = int(input("Action : "))
                mode = "chiffrer" if action == 1 else "dechiffrer"
            except ValueError:
                print("❌ Choix invalide")
                continue
            
            # Saisie du texte
            texte = input("📝 Texte : ")
            
            # ═══════════════════════════════════════════════════
            # ALGORITHME CÉSAR
            # ═══════════════════════════════════════════════════
            if choix == 1:
                try:
                    decalage = int(input("🔑 Décalage (1-25) : "))
                    resultat = cesar(texte, decalage, mode)
                except ValueError:
                    print("❌ Décalage invalide")
                    continue
            
            # ═══════════════════════════════════════════════════
            # ALGORITHME VIGENÈRE
            # ═══════════════════════════════════════════════════
            elif choix == 2:
                cle = input("🔑 Mot-clé (ex: SECRET) : ")
                resultat = vigenere(texte, cle, mode)
            
            # ═══════════════════════════════════════════════════
            # ALGORITHME XOR
            # ═══════════════════════════════════════════════════
            elif choix == 3:
                cle = input("🔑 Clé (ex: KEY) : ")
                resultat = xor_cipher(texte, cle)
                # XOR est son propre inverse, pas besoin de mode !
            
            # Afficher le résultat
            print("\n" + "="*60)
            action_texte = "CHIFFRÉ" if mode == "chiffrer" else "DÉCHIFFRÉ"
            print(f"🔒 RÉSULTAT {action_texte} : {resultat}")
            print("="*60)
            
            # Sauvegarder pour l'option 4
            dernier_resultat = resultat
        
        else:
            print("❌ Choix invalide ! Choisis entre 0 et 4.")


# ═══════════════════════════════════════════════════════════════
# POINT D'ENTRÉE DU PROGRAMME
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    """
    Ce bloc s'exécute seulement si on lance ce fichier directement.
    Si on importe ce fichier (import crypto_advanced), ce bloc ne s'exécute pas.
    """
    main()
