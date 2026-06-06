# Rapport de Test — Güdlft

## Environnement

|   Paramètre   |     Valeur    |
|---------------|---------------|
| Langage       | Python 3.14.3 |
| Framework     | Flask         |
| Outil de test | pytest 9.0.3  |
| Couverture    | pytest-cov    |
| Plateforme    | Windows       |

---

## Bugs corrigés

|                Bug               |                           Description                           |   Fichier   |   Statut   |
|----------------------------------|-----------------------------------------------------------------|-------------|------------|
| Email inconnu — crash            | `showSummary` : IndexError si l'email n'existe pas dans le JSON | `server.py` | ✅ Corrigé |
| Input négatif ou nul             | `purchasePlaces` : aucune validation de l'input utilisateur     | `server.py` | ✅ Corrigé |
| Limite 12 places non respectée   | Pas de vérification du maximum de 12 places par club            | `server.py` | ✅ Corrigé |
| Points insuffisants non vérifiés | Un club pouvait réserver sans avoir assez de points             | `server.py` | ✅ Corrigé |
| Places disponibles non vérifiées | Possible de surréserver une compétition                         | `server.py` | ✅ Corrigé |
| Points non déduits               | Les points du club n'étaient pas déduits après réservation      | `server.py` | ✅ Corrigé |
| Données non persistées           | Les modifications n'étaient pas sauvegardées dans les JSON      | `server.py` | ✅ Corrigé |

---

## Fonctionnalités implémentées 

|         Fonctionnalité      |                             Description                               |     Statut    |
|-----------------------------|-----------------------------------------------------------------------|---------------|
| Tableau public des points   | Page accessible sans connexion listant tous les clubs et leurs points | ✅ Implémenté |
| Page d'accueil restructurée | Le tableau des points devient la page d'accueil, login séparé         | ✅ Implémenté |

---

## Structure des tests

```
tests/
├── unit/           (14 tests) — une route ou fonction testée isolément
├── integration/    (2 tests)  — plusieurs routes enchaînées
└── functional/     (1 test)   — parcours utilisateur complet
```

---

## Détail des tests

### Tests unitaires (14)

|           Fichier         |              Test              |                     Description                   | Résultat |
|---------------------------|--------------------------------|---------------------------------------------------|----------|
| test_unknow_email.py      | `test_unknown_email`           | Email inconnu → message d'erreur, pas de crash    |    ✅    |
| test_valid_email.py       | `test_valid_email`             | Email valide → redirection welcome                |    ✅    |
| test_purchase_valid.py    | `test_valid_input`             | Réservation valide → confirmation                 |    ✅    |
| test_purchase_negatif.py  | `test_input_negatif`           | Input négatif → message d'erreur                  |    ✅    |
| test_purchase_none.py     | `test_input_none`              | Input = 0 → message d'erreur                      |    ✅    |
| test_club_point.py        | `test_club_point`              | Points insuffisants → message d'erreur            |    ✅    |
| test_place_limit.py       | `test_places_limitation`       | Plus de 12 places → message d'erreur              |    ✅    |
| test_place_competition.py | `test_competition_places`      | Plus de places que disponibles → erreur           |    ✅    |
| test_data_club.py         | `test_data_club`               | Points du club bien sauvegardés dans le JSON      |    ✅    |
| test_data_competition.py  | `test_data_competition`        | Places compétition bien sauvegardées dans le JSON |    ✅    |
| test_board_club.py        | `test_board_clubs`             | Tous les clubs apparaissent sur le tableau        |    ✅    |
| test_board_point.py       | `test_board_points`            | Les points de chaque club sont affichés           |    ✅    |
| test_board_read_only.py   | `test_board_read_only`         | Pas de formulaire sur le tableau (lecture seule)  |    ✅    |
| test_board_no_login.py    | `test_board_no_login_required` | Tableau accessible sans connexion                 |    ✅    |

### Tests d'intégration (2)
 
|                Fichier                 |                 Test              |                Description                  |Résultat|
|----------------------------------------|-----------------------------------|---------------------------------------------|--------|
| test_login_and_purchase.py             | `test_login_and_purchase`         | Login → réservation → confirmation          |   ✅  |
| test_invalid_purchase_and_datacheck.py | `test_invalid_purchase_datacheck` | Réservation invalide → points JSON inchangés|   ✅  |

### Tests fonctionnels (1)

|       Fichier    |       Test      |                                   Description                                    | Résultat |
|------------------|-----------------|----------------------------------------------------------------------------------|----------|
| test_full_app.py | `test_full_app` | Parcours complet : index → login → welcome → réservation → confirmation → logout |    ✅    |

---

## Résultats globaux

|      Métrique      |  Valeur  |
|--------------------|----------|
| Total de tests     |    17    |
| Tests réussis      |    17    |
| Tests échoués      |    0     |
| Couverture du code | **100%** |

---

## Commande pour reproduire les tests

```bash
pytest --cov=server --cov-report=term-missing tests/ -v
```
