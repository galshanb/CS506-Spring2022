import math
import cairo
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import PysimpleGUI as sg
import os
import tkinter
import io

def draw_library():
    
    print("library not found")
    return
    img= Image.open("lib.jpg")
    img.thumbnail((1200,800))
    
    bi = io.BytesIO()
    img.save(bi, format = "PNG")
    
    #layout = [[ sg.Text ("Library", font = ("Ariel",20)),[sg.Image(data
