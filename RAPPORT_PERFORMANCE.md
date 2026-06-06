# Rapport de Performance — Güdlft

## Conditions du test

|        Paramètre      |         Valeur        |
|-----------------------|-----------------------|
| Outil                 | Locust                |
| Nombre d'utilisateurs | 6                     |
| Ramp up               | 1 utilisateur/seconde |
| Durée du test         | 8 minutes 54 secondes |
| Host                  | http://127.0.0.1:5000 |

## Routes testées

| Méthode |                Route                |            Description              |
|---------|-------------------------------------|-------------------------------------|
|   GET   |                 `/`                 | Page d'accueil — tableau des points |
|   GET   |            `/pointsBoard`           | Tableau public des points           |
|   GET   | `/book/Spring Festival/Simply Lift` | Formulaire de réservation           |
|   POST  |            `/showSummary`           | Login + liste des compétitions      |
|   POST  |          `/purchasePlaces`          | Achat de places                     |

## Résultats — Request Statistics

| Méthode |      Route      | # Requêtes | # Fails | Average (ms) | Min (ms) | Max (ms) |    RPS   |
|---------|-----------------|------------|---------|--------------|----------|----------|----------|
|   GET   |        /        |     326    |    0    |     6.38     |     2    |    29    |   0.61   |
|   GET   |    /book/...    |     337    |    0    |     6.80     |     3    |    127   |   0.63   |
|   GET   |  /pointsBoard   |     317    |    0    |     6.28     |     2    |    14    |   0.59   |
|   POST  | /purchasePlaces |     283    |    0    |     6.73     |     3    |    14    |   0.53   |
|   POST  |  /showSummary   |     326    |    0    |     6.97     |     3    |    41    |   0.61   |
|         | **Aggregated**  |  **1589**  |  **0**  |   **6.63**   |   **2**  |  **130** | **2.98** |

## Résultats — Response Time Statistics (percentiles en ms)

| Méthode |       Route     |  50%  |  90%  |  95%   |  99%   |   100%  |
|---------|-----------------|-------|-------|--------|--------|---------|
|   GET   |         /       |   7   |   9   |   10   |   13   |   29    |
|   GET   |     /book/...   |   6   |   9   |   10   |   13   |   130   |
|   GET   |   /pointsBoard  |   6   |   9   |   9    |   12   |   14    |
|   POST  | /purchasePlaces |   6   |   10  |   10   |   13   |   14    |
|   POST  |   /showSummary  |   7   |   10  |   11   |   18   |   41    |
|         | **Aggregated**  | **7** | **9** | **10** | **13** | **130** |

## Analyse des résultats

### Critères du cahier des charges

|                       Critère                        | Seuil requis |  Résultat obtenu  | Statut |
|------------------------------------------------------|--------------|-------------------|--------|
| Récupérer la liste des compétitions (`/showSummary`) | < 5000 ms    | 6.97 ms (average) |   ✅  |
| Mettre à jour le total de points (`/purchasePlaces`) | < 2000 ms    | 6.73 ms (average) |   ✅  |
| Nombre d'utilisateurs simultanés                     | 6            | 6                 |   ✅  |
| Taux d'échec                                         | 0            | 0 / 1589 requêtes |   ✅  |

### Conclusion

L'application respecte largement les critères de performance définis dans le cahier des charges. Les temps de réponse sont bien en dessous des seuils requis avec une moyenne globale de **6.63 ms** pour l'ensemble des routes, et un maximum absolu de **130 ms**. Aucun échec n'a été enregistré sur les **1589 requêtes** effectuées durant le test.

Ces performances s'expliquent par l'architecture légère de l'application (Flask + JSON en mémoire, sans base de données), ce qui est cohérent avec l'objectif POC du projet.
