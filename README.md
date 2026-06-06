# Güdlft — Application de Réservation

Ce projet est une version du système de réservation phare de Güdlft, destinée aux compétitions locales et régionales. L'objectif est de permettre aux secrétaires de clubs de gérer les inscriptions aux compétitions en utilisant un système de points sans passer par l'organisateur directement.

**Auteur :** [senegas-arnaud](https://github.com/senegas-arnaud)  
**Repo original :** [OpenClassrooms Python_Testing](https://github.com/OpenClassrooms-Student-Center/Python_Testing)

---

## Sommaire

- [Présentation du projet](#présentation-du-projet)
- [Stack technique](#stack-technique)
- [Installation](#installation)
- [Lancer l'application](#lancer-lapplication)
- [Lancer les tests](#lancer-les-tests)
- [Lancer les tests de performance](#lancer-les-tests-de-performance)
- [Structure du projet](#structure-du-projet)
- [Structure GitHub](#structure-github)
- [Conventions de nommage](#conventions-de-nommage)
- [Ressources externes](#ressources-externes)

---

## Présentation du projet

### Fonctionnalités

- Connexion via email (secrétaires uniquement)
- Consultation des compétitions à venir et des places disponibles
- Réservation de places via un système de points (1 point = 1 place)
- Limite de 12 places par club par compétition
- Tableau public des points accessible sans connexion

### Bugs corrigés

- Email inconnu provoquant un crash de l'application
- Absence de validation de l'input utilisateur (négatif, nul)
- Limite de 12 places par club non respectée
- Points insuffisants non vérifiés avant réservation
- Places disponibles non vérifiées avant réservation
- Points non déduits après réservation
- Données non persistées dans les fichiers JSON

### Nouvelle fonctionnalité

- Tableau public des points accessible sans connexion depuis la page d'accueil

---

## Stack technique

|    Outil    |                    Usage                   |
|-------------|--------------------------------------------|
| Python 3.14 | Langage principal                          |
| Flask       | Framework web                              |
| JSON        | Stockage des données                       |
| pytest      | Tests unitaires, intégration, fonctionnels |
| pytest-cov  | Couverture de code                         |
| Locust      | Tests de performance                       |

---

## Installation

### Prérequis

- Python 3.10+
- pip

### Cloner le repo

```bash
git clone https://github.com/senegas-arnaud/Gudlft.git
cd Gudlft
```

### Créer et activer le virtualenv

```bash
# Créer le virtualenv
python -m venv venv

# Activer le virtualenv
venv\Scripts\activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Lancer l'application

```bash
flask --app server.py run
```

L'application est accessible sur `http://127.0.0.1:5000`

### Comptes de test disponibles

|         Email        |     Club    | Points |
|----------------------|-------------|--------|
| john@simplylift.co   | Simply Lift |   15   |
| admin@irontemple.com | Iron Temple |   4    |
| kate@shelifts.co.uk  | She Lifts   |   12   |

---

## Lancer les tests

### Tous les tests

```bash
pytest tests/ -v
```

### Avec couverture de code

```bash
pytest --cov=server --cov-report=term-missing tests/ -v
```

### Par catégorie

```bash
pytest tests/unit/ -v          
pytest tests/integration/ -v   
pytest tests/functional/ -v    
```

### Résultats attendus

- 17 tests au total
- 0 échecs
- 100% de couverture de code

---

## Lancer les tests de performance

### Prérequis

Avoir l'application Flask lancée dans un terminal séparé :
```bash
flask --app server.py run
```

### Lancer Locust

```bash
locust -f locustfile.py
```

Ouvrir `http://localhost:8089` dans le navigateur puis configurer :

|    Paramètre    |         Valeur        |
|-----------------|-----------------------|
| Number of users |           6           |
| Ramp up         |           1           |
| Host            | http://127.0.0.1:5000 |

### Critères de performance (cahier des charges)

|                   Route                     | Seuil requis | Résultat obtenu |
|---------------------------------------------|--------------|-----------------|
| `POST /showSummary` (liste compétitions)    |   < 5000 ms  |      ~7 ms      |
| `POST /purchasePlaces` (mise à jour points) |   < 2000 ms  |      ~7 ms      |

---

## Structure du projet

```
Gudlft/
├── server.py                   # Application Flask — routes et logique métier
├── clubs.json                  # Données des clubs (nom, email, points)
├── competitions.json           # Données des compétitions (nom, date, places)
├── locustfile.py               # Script de test de performance
├── conftest.py                 # Configuration pytest et fixtures partagées
├── requirements.txt            # Dépendances Python
├── RAPPORT_TEST.md             # Rapport de test
├── RAPPORT_PERFORMANCE.md      # Rapport de performance
├── templates/
│   ├── index.html              # Page d'accueil — tableau public des points
│   ├── login.html              # Page de connexion
│   ├── welcome.html            # Tableau de bord secrétaire
│   └── booking.html            # Formulaire de réservation
└── tests/
    ├── unit/                   # Tests unitaires (une route/fonction isolée)
    ├── integration/            # Tests d'intégration (routes enchaînées)
    └── functional/             # Tests fonctionnels (parcours utilisateur complet)
```

---

## Structure GitHub

|         Branche         |                    Description                    |
|-------------------------|---------------------------------------------------|
| `main`                  | Code stable et finalisé                           |
| `bug/tests_unit`        | Correction des bugs + tests unitaires             |
| `bug/tests_integration` | Tests d'intégration                               |
| `bug/tests_full_app`    | Test fonctionnel parcours utilisateur complet     |
| `feature/points_board`  | Tableau public des points                         |
| `QA`                    | Branche de revue finale — ne pas merger dans main |


---

## Conventions de nommage

### Python

- **Variables et fonctions** : `snake_case` → `places_required`, `found_clubs`
- **Routes Flask** : `camelCase` → `showSummary`, `purchasePlaces`, `pointsBoard`
- **Fonctions de test** : préfixe `test_` obligatoire → `test_unknown_email()`

### Git

- **Branches bug** : `bug/nom-descriptif`
- **Branches feature** : `feature/nom-descriptif`

### JSON

- Les valeurs numériques (points, places) sont stockées en **string** dans les JSON : `"points": "15"`

---

## Ressources externes

- [Flask Documentation](https://flask.palletsprojects.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [Locust Documentation](https://locust.io/)
- [Repo original OpenClassrooms](https://github.com/OpenClassrooms-Student-Center/Python_Testing)
