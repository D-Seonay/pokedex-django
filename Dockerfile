# Utiliser une image de base officielle Python
FROM python:3.12

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de votre projet dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exposer le port pour l'application Django
EXPOSE 8000

# Commande par défaut pour démarrer le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
