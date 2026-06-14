import os
import sys
import shutil
import threading
from pathlib import Path
from tkinter import filedialog, messagebox
import tkinter as tk

import customtkinter as ctk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

import rawpy
import numpy as np

### TriPhoto
#-------------------------------------------------------------
# Affichage image
#-------------------------------------------------------------

def Ouvre_photo(path : Path) -> Image.Image | None :
    try :
        Image.open(path)
    except Exception as e:
        print(f"[ERREUR] {path.name}: {e}")
        return None
    
def Affiche_photo(photo : Image.Image, H, L):
    photo : photo.copy()
    photo.thumbnail((L, H), Image.LANCZOS)
    return photo


print("a")

####################
# Application
####################

class TriPhoto(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Titre fenetre uwu hihi haha")
        self.geometry("1300x400")
        self.minsize(900, 600)

        # Variables
        self.dossier_source: Path|None = None
        self.dossier_destination: Path | None = None
        self.listage: int = 0
        self.photos:   list[Path] = ["C:/Users/thaoh/Pictures/Iris/Boom 31-01-2025P1250899.RW2"]
        self.history:  list[tuple[Path, str | None]] = []

        self._tk_img   = None   # éviter le GC
        self._tk_bg    = None
        self._loading  = False

        # Methodes
        self._build_UI()

        self._bind_keys() #ok

    
    
    #definition des methodes
    #methode pour construire l'interface utilisateur
    def _build_UI(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
    # visuel
        self._visionneur()
        self._barre_outils() #ok
        self._barre_raccourcis() #presque je narrive pas a le faire coller a la barre d'outils

    #donnée
        
        
    def _visionneur(self):
        self.frame_visionneur = ctk.CTkFrame(self)
        self.frame_visionneur.grid(row=0, column=2, padx=10, sticky="nws")
        self.Image_label = ctk.CTkLabel(self.frame_visionneur, image=Affiche_photo(self.photos[0], 400,400), text="")
        self.Image_label.grid(row=0, column = 0, padx=10, pady=(10, 0), sticky="w")
        
            


    def _barre_outils(self):

        self.frame_outil = ctk.CTkFrame(self,  corner_radius=0, width=270)
        self.frame_outil.grid(row=0, column=0, sticky="new")
           
        self.label_outil = ctk.CTkLabel(self.frame_outil, text="Barre d'outils", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_outil.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        
        self.bouton_dossier_source = ctk.CTkButton(self.frame_outil, text="Choisir dossier source", command=lambda: self._choisir_dossier_source())
        self.bouton_dossier_source.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.bouton_dossier_destination = ctk.CTkButton(self.frame_outil, text="Choisir dossier destination", command=lambda: self._choisir_dossier_destination())
        self.bouton_dossier_destination.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="w")

    def _barre_raccourcis(self):
        self.frame_raccourcis = ctk.CTkFrame(self, corner_radius=0)
        self.frame_raccourcis.grid(row=1, column=0, columnspan=2, padx=0, pady=(0, 0), sticky="nw")

        self.label_raccourcis = ctk.CTkLabel(self.frame_raccourcis, text="Raccourcis clavier:", font=ctk.CTkFont(size=15, weight="bold"))
        self.label_raccourcis.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nw")
        Raccourci = [
            ("O  ou  →", "Viable"),
            ("N",        "Non viable"),
            ("← ou Z",  "Retour"),
            ("Espace",   "Passer"),
        ]

        for i, (key, label) in enumerate(Raccourci):
            ctk.CTkLabel(self.frame_raccourcis, text=key, font=ctk.CTkFont("Courier", 12, "bold"), width=80, anchor="w").grid(row=i+1, column=0, padx=12, pady=5, sticky="nw")
            ctk.CTkLabel(self.frame_raccourcis, text=label, font=ctk.CTkFont(size=12)).grid(row=i+1, column=1, padx=4, pady=5, sticky="nw")

    #méthode pour lier les touches du clavier aux actions correspondantes
    def _bind_keys(self):
            self.bind("<Left>",  lambda e: self._retour()) #non il fautse déplacer dans les photos
            self.bind("<Right>", lambda e: self._decision("skip"))
            self.bind("<o>",     lambda e: self._decision("ok"))
            self.bind("<O>",     lambda e: self._decision("ok"))
            self.bind("<n>",     lambda e: self._decision("non"))
            self.bind("<N>",     lambda e: self._decision("non"))
            self.bind("<space>", lambda e: self._decision("skip"))
            self.bind("<z>",     lambda e: self._retour())
            self.bind("<Z>",     lambda e: self._retour())
            self.bind("<Delete>",lambda e: self._retour())

    #------Méthode pour choisir les dossiers source et destination
    def _choisir_dossier_source(self):
        self.dossier_source = filedialog.askdirectory(title="Choisi ton dossier source")
        print("Selected Folder:", self.dossier_source)
        self._lister_photo()

    #------Méthode pour choisir le dossier destination
    def _choisir_dossier_destination(self):
        self.dossier_destination = filedialog.askdirectory(title="choisi ton dossier destination")
        print("Selected Folder:", self.dossier_destination)


    def _lister_photo(self):
        print(self.dossier_source)
        for i in os.listdir(self.dossier_source):
            if i.endswith(".RW2")  | i.endswith(".jpeg") | i.endswith(".jpg")  | i.endswith(".png") :
                self.photos.append(self.dossier_source + i)
        return
    

    
app = TriPhoto()
app.mainloop()
