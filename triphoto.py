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
print("a")
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




####################
# Application
####################

class TriPhoto(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Titre fenetre uwu hihi haha")
        self.geometry("1340x860")
        self.minsize(900, 600)

        # Variables
        self.dossier_source: Path|None = None
        self.dossier_destination: Path | None = None
        self.listage: int = 0
        self.photos:   list[Path] = []
        self.history:  list[tuple[Path, str | None]] = []

        self._tk_img   = None   # éviter le GC
        self._tk_bg    = None
        self._loading  = False

        # Methodes
        self._build_UI()
        #self._bind_keys()

        def _build_UI(self):
            return