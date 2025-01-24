# Pokédex Django

Ce projet est une application web Pokédex développée avec Django. Elle permet de consulter les informations sur les Pokémon, de créer et gérer des équipes, et inclut un mode de batailles.

## Prérequis

- Python 3.x
- Django 5.1.4
- SQLite (inclus par défaut avec Django)

## Description

Ce projet est une application web Django permettant de créer et gérer des équipes de Pokémon. Les informations des Pokémon sont récupérées depuis l'API PokeAPI. Les utilisateurs peuvent créer des équipes, ajouter des Pokémon, mettre à jour les noms des équipes, et afficher des informations détaillées pour chaque Pokémon.

### Fonctionnalités principales :
- **Création et gestion d'équipes** : Créez des équipes de Pokémon et mettez à jour leur nom.
- **Ajout de Pokémon à l'équipe** : Sélectionnez des Pokémon à ajouter dans votre équipe.
- **Suppression de Pokémon** : Retirez un Pokémon de votre équipe.
- **Types de Pokémon** : Affichez les types (comme `Feu`, `Eau`, `Plante`, etc.) de chaque Pokémon dans l'équipe.
- **Statistiques des Pokémon** : Visualisez les statistiques détaillées pour chaque Pokémon, telles que l'attaque, la défense, et la vitesse.
- **Recherche de Pokémon** : Recherchez des Pokémon à ajouter à votre équipe via une barre de recherche.

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/votre-utilisateur/pokedex-django.git
    cd pokedex-django
    ```

2. Créez et activez un environnement virtuel :
    ```sh
    python -m venv env
    source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
    ```

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

4. Appliquez les migrations de la base de données :
    ```sh
    python manage.py migrate
    ```

5. Lancez le serveur de développement :
    ```sh
    python manage.py runserver
    ```

6. Accédez à l'application dans votre navigateur à l'adresse `http://127.0.0.1:8000/`.

## Utilisation

### Pokédex

- Accédez à la liste des Pokémon dans l'application.
- Cliquez sur un Pokémon pour voir ses détails, y compris son sprite, ses types, ses statistiques et son cri.
- Vous pouvez également ajouter des Pokémon à vos équipes ou les supprimer.

### Gestion des Équipes

- Créez des équipes de Pokémon en leur attribuant un nom.
- Ajoutez des Pokémon à une équipe en cliquant sur leur carte dans la section "Choisissez des pokémons à ajouter à l'équipe".
- Supprimez un Pokémon d'une équipe en cliquant sur sa carte dans la section "Pokémons dans votre équipe".

### Mode Batailles

- Le mode batailles permet de simuler des combats entre Pokémon (si implémenté dans le projet, vous pouvez ajouter des détails ici sur la façon de l'utiliser).

## Commandes de gestion

### Fetch Pokémon

Pour récupérer les données des Pokémon depuis l'API PokeAPI, exécutez la commande suivante :

```sh
python manage.py fetch_pokemon
```
## Structure du projet

```sh
pokedex-django/
├── manage.py                # Fichier principal pour exécuter les commandes Django
├── pokedex-django/           # Répertoire principal du projet Django
│   ├── __init__.py
│   ├── settings.py           # Paramètres de configuration Django
│   ├── urls.py               # Définition des routes
│   └── wsgi.py
├── pokemon/                  # Application principale de Pokémon
│   ├── __init__.py
│   ├── admin.py              # Administration des modèles
│   ├── apps.py               # Configuration de l'application
│   ├── models.py             # Définition des modèles de Pokémon
│   ├── views.py              # Vues de l'application
│   ├── migrations/           # Dossier des migrations de base de données
│   ├── management/           # Commandes personnalisées de gestion
│   │   └── commands/         # Commandes de gestion pour récupérer les données de Pokémon
│   │       └── fetch_pokemon.py
│   ├── templates/            # Templates HTML
│   │   └── components/       # Composants réutilisables
│   └── static/               # Fichiers statiques (CSS, images)
├── requirements.txt          # Liste des dépendances Python
└── static/
    └── css/
        └── global.css        # Styles CSS globaux
