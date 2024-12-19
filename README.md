# Pokédex Django

Ce projet est une application web Pokédex développée avec Django. Elle permet de consulter les informations sur les Pokémon et inclut un mode de batailles.

## Prérequis

- Python 3.x
- Django 5.1.4
- SQLite (inclus par défaut avec Django)

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

- Accédez à la liste des Pokémon à la racine de l'application.
- Cliquez sur un Pokémon pour voir ses détails, y compris ses statistiques et son cri.

### Mode Batailles

- Le mode batailles permet de simuler des combats entre Pokémon.
- (Ajoutez ici des instructions spécifiques sur l'utilisation du mode batailles si nécessaire.)

## Commandes de gestion

### Fetch Pokémon

Pour récupérer les données des Pokémon depuis l'API PokeAPI, exécutez la commande suivante :
```sh
python manage.py fetch_pokemon