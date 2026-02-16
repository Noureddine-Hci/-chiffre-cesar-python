"""
CHIFFRE DE CÉSAR - VERSION INTERACTIVE
========================================
Cette version permet à l'utilisateur de choisir :
- Le message à chiffrer
- Le décalage à utiliser
- Entre chiffrement ou déchiffrement
"""


def chiffrer_cesar(texte, decalage):
    """Chiffre un texte avec le chiffre de César."""
    resultat = ""
    for char in texte:
        if char.isupper():
            # Formule complète : conversion → décalage → modulo → reconversion
            resultat += chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
        elif char.islower():
            resultat += chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))
        else:
            resultat += char  # Garde espaces, ponctuation, chiffres inchangés
    return resultat


def dechiffrer_cesar(texte_chiffre, decalage):
    """Déchiffre un texte en utilisant un décalage négatif."""
    return chiffrer_cesar(texte_chiffre, -decalage)


# ==========================================
# PROGRAMME INTERACTIF
# ==========================================
if __name__ == "__main__":
    print("=" * 60)
    print("🔐 CHIFFRE DE CÉSAR - VERSION INTERACTIVE")
    print("=" * 60)
    
    # ═══════════════════════════════════════════════════════════════
    # CONCEPT CLÉ #1 : input() - Interaction avec l'utilisateur
    # ═══════════════════════════════════════════════════════════════
    # input("question") affiche une question et ATTEND que l'utilisateur tape une réponse
    # Le programme se met en PAUSE jusqu'à ce que l'utilisateur appuie sur ENTRÉE
    # La réponse est TOUJOURS du texte (type str), même si on tape des chiffres
    
    print("\nQue veux-tu faire ?")
    print("  1 - Chiffrer un message")
    print("  2 - Déchiffrer un message")
    
    # input() retourne ce que l'utilisateur a tapé (type : texte/str)
    choix = input("\nTon choix (1 ou 2) : ")
    
    # ═══════════════════════════════════════════════════════════════
    # CONCEPT CLÉ #2 : Conditions if/else - Choix selon la réponse
    # ═══════════════════════════════════════════════════════════════
    # if condition:    → Si la condition est vraie, execute ce bloc
    # else:            → Sinon, execute cet autre bloc
    
    print("\n" + "-" * 60)
    if choix == "1":
        # == vérifie l'égalité (attention : = assigne, == compare)
        message = input("📝 Entre le message à CHIFFRER : ")
    else:
        message = input("📝 Entre le message à DÉCHIFFRER : ")
    
    # ═══════════════════════════════════════════════════════════════
    # CONCEPT CLÉ #3 : int() - Conversion texte → nombre
    # ═══════════════════════════════════════════════════════════════
    # input() retourne TOUJOURS du texte, même si on tape "5"
    # Il faut convertir le texte en nombre avec int() pour faire des calculs
    # Exemples :
    #   int("5")   → 5 (nombre)
    #   int("abc") → ERREUR (impossible de convertir des lettres)
    
    decalage = int(input("🔑 Entre le décalage (nombre entre 1 et 25) : "))
    # Ici, decalage est maintenant un nombre entier (int), pas du texte (str)
    
    # ═══════════════════════════════════════════════════════════════
    # CONCEPT CLÉ #4 : Exécution conditionnelle selon le choix
    # ═══════════════════════════════════════════════════════════════
    
    print("\n" + "=" * 60)
    if choix == "1":
        # Si l'utilisateur a choisi 1 → Chiffrement
        resultat = chiffrer_cesar(message, decalage)
        print(f"🔒 MESSAGE CHIFFRÉ : {resultat}")
    else:
        # Sinon (choix 2 ou autre) → Déchiffrement
        resultat = dechiffrer_cesar(message, decalage)
        print(f"🔓 MESSAGE DÉCHIFFRÉ : {resultat}")
    
    print("=" * 60)
    
    # BONUS : Message informatif
    print("\n💡 Pour relancer le programme, tape : python chiffre_cesar_interactif.py")
