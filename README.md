# Projet DATA sur les prenoms de l'INSEE

Application WEB qui permet d'explorer les données sur les prenoms donnés en France depuis 1900 recensés par l'INSEE.

## Fonctionnalités

- **Evolution des prenoms** : Choisis un prénom dans la liste (entrer les premieres lettres pour filtrer) et visualise les nombre de naissances par années pour ce prénom.
- **Top 50 des prenoms par année** : Choisis une année avec le curseur et visualise les 50 prénoms les plus donnés
   
## Données

-  Fichier CSV fournit par [l'INSEE](https://www.insee.fr/fr/statistiques/8595130?sommaire=8595113) publié sour licence Ouverte
-  Le fichier est déjà dans data/
  
## Structure du projet

```

Prenoms/
|- README.md
|- requirements.txt  
|- data/
|--- prenom.db      # Base de donnée SQLite
|--- prenoms-2025nat.csv        # Fichier CSV de l'INSEE
|- src/
|--- build_db.py    # construction et connexion à la base
|--- queries.py     # requête SQL vers la base 
|--- app.py         # Interface streamlit

```

## Installation 

Il faut Python 3.10 ou plus récent

```bash
git clone <adresse_depot>
cd Prenoms
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Lancement 

1. Construire la base de donnée 
    ```bash
        python src/build_db.py
    ```
2. Lancement du site
    ```bash
        streamlit run src/app.py
    ```

La page s'ouvrira sur votre navigateur par défaut

## Auteur 

Edoardo GRAZIANO : projet personnel réalisé en L3 informatique à l'université Claude Bernard Lyon 1.
11/10/2026