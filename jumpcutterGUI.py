import tkinter as tk
from tkinter import filedialog, simpledialog
import sys, os

userFile = filedialog.askopenfilename()
userSpeed = simpledialog.askfloat(title = "Silent Speed", prompt = 'Enter a number between 1 and 999999 for the "silent speed" multiplier\n(the playback speed of the silent regions of the video from 1x up)')

print(userFile)

print(os.getcwd())

os.system("python jumpcutter.py --input_file " + userFile + " --silent_speed " + str(userSpeed) + " --output_file " + userFile[:-4] + "_silentSpeed" + str(int(userSpeed)) + userFile[-4:])