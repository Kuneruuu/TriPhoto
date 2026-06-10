# TriPhoto
Logiciel de tri de photos au clavier, rapide et EFFICACE (meme sur un pc-cale porte)
Visualisation de nos photos (.rw2, .jpeg, .png) pour pouvoir les trier rapidement en viables ou non viables en appuyant sur deux touches pas besoin de toucher la souris !

--> Projet du dimanche pour se mettre du python dans les pattes

## Workflow
- Choix du dossier
- Chargement des photos en threads : pas trop de latence lors de la récupération de photos lourdes
- Tri au clavier — une touche pour valider, une pour rejeter, une pour revenir en arrière
- Exports des photos choisies : on les copie dans un dossier "photos viables"

## Requis
- Support le RAW : lit les fichiers .rw2 (Panasonic Lumix) --> rawpy; et plus tard d'autres fichiers raw
- Fond flouté — chaque photo est affichée sur un fond tiré d'elle-même pour apprendre à manipuler les images avec PIL et rendre le tout esthétique
- Historique complet — revenirez en arrière autant de fois que nécessaire quand on est pas sur de notre choix
- Lié les photos jumelles, lorsqu'il y a une version .jpeg et .rw2 d'une meme photo

## Installation

Lancer depuis le **terminal**

### 1. Cloner le dépôt
 
```bash
git clone https://github.com/votre-utilisateur/TriPhoto.git
cd TriPhoto
```

 
### 2. Créer un environnement virtuel 
 
```bash
python -m venv my_venv # Faire gaffe au nom j'ai galérer s'il exise déja un venv à ce nom
 
# puis
my_venv\Scripts\activate
 

```
 
### 3. Installer les librairis
 
```bash
pip install customtkinter Pillow rawpy numpy
```

 
### 4. Lancer l'application
 
```bash
python TriPhoto.py
```
