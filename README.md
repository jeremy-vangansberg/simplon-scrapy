# Projet de Scraping avec Scrapy

Ce projet organise plusieurs configurations de scraping avec le framework Scrapy. Il est composé de plusieurs dossiers, chacun correspondant à un projet de scraping distinct.

## Structure générale

- **allocine/** : Projet Scrapy pour récupérer des informations depuis Allocine. Inclut un script de déploiement Azure Functions.
- **final/** : Projet Scrapy ciblant des données de livres (fichier CSV présent).
- **start/** : Autre configuration Scrapy pour des livres, utilisant Poetry.

## Installation

1. **Cloner le dépôt** puis naviguer dans le répertoire souhaité.
2. **Installer les dépendances** pour chaque projet :
   - **Dans le dossier `allocine`** :
     ```bash
     pip install -r requirements.txt
     ```
   - **Dans le dossier `start`** :
     ```bash
     poetry install
     ```

## Utilisation

Lancer un spider Scrapy en se plaçant dans le dossier approprié :

```bash
scrapy crawl <nom_du_spider>
```

## Contribuer

Les pull requests et issues sont les bienvenues pour toute proposition d’amélioration.

## Licence

Ce projet est sous licence MIT.
