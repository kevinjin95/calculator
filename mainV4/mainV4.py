import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.font import Font
import display

root = tk.Tk()

def main():
    resulttext = tk.StringVar()
    operationtext = tk.StringVar()
    numbers = []
    deconcat_number = []
    entered_operators = []
    operationlist = []
    last_Pressed = []
    display.display(root)

if __name__=="__main__": 
    main()
