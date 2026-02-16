# 🔐 Chiffre de César - TP Python

Implémentation du chiffre de César en Python (algorithme de chiffrement par substitution).

## 📁 Fichiers

- **`chiffre_cesar_detaille.py`** - Version pédagogique avec commentaires détaillés
- **`chiffre_cesar_concis.py`** - Version professionnelle optimisée  
- **`chiffre_cesar_interactif.py`** - Version interactive avec saisie utilisateur

## 🚀 Utilisation

### Version interactive (recommandée)
```bash
python chiffre_cesar_interactif.py
```

### Versions de démonstration
```bash
python chiffre_cesar_concis.py
python chiffre_cesar_detaille.py
```

## 📚 Concepts Python utilisés

- Fonctions `ord()` et `chr()` pour conversion caractère ↔ code ASCII
- Opérateur modulo `%` pour boucle cyclique sur l'alphabet
- Fonction `input()` pour interaction utilisateur
- Conditions `if/else` pour le contrôle de flux

## 🔑 Exemple

```python
from chiffre_cesar_concis import chiffrer_cesar, dechiffrer_cesar

message = "HELLO"
chiffre = chiffrer_cesar(message, 3)  # → "KHOOR"
dechiffre = dechiffrer_cesar(chiffre, 3)  # → "HELLO"
```

## 📖 Auteur

Projet réalisé dans le cadre d'un TP Python
