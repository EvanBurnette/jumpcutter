import tkinter as tk
from tkinter import filedialog
import sys, os

userFolder = filedialog.askdirectory()
os.chdir(os.path(userFolder))
print(os.getcwd())