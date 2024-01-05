import tkinter as tk
from tkinter import ttk #used for Tree View and Combobox
from tkinter import messagebox #for error messageboxes


def materialsRequest(window): #contains all functions for requesting materials
    prompt = tk.Label(window, text = "What item would you\nlike to request?")
    prompt.grid(row = 0, column = 0)
    
    menuValues = ["shirts", "hoodies", "dri-fit", "jackets"] #list of initial items to use as default

    def selectionBox(): #initializing the combobox
        selected = tk.StringVar()
        global menu
        menu = ttk.Combobox(window, textvariable = selected)
        menu['values'] = menuValues
        menu.grid(row = 1, column = 0, padx = 5, pady = 5)
    
    selectionBox()#calls combobox function to refresh the options

    #label and entry for the quantity
    quantityLabel = tk.Label(window, text = "How many would\nyou like to order?")
    quantityLabel.grid(row = 0, column = 1, columnspan = 2)

    quantityEntry = tk.Entry(window)
    quantityEntry.grid(row = 1, column = 1, columnspan = 2)

    #buttons to delete items and add/remove item quantity
    delButton = tk.Button(window, text = "Delete Item", command = lambda : delItem())
    delButton.grid(row = 2, column = 0, pady = 5)

    addButton = tk.Button(window, text = "Add Quantity", command = lambda : addQuantity())
    addButton.grid(row = 2, column = 1, pady = 5)

    subtractButton = tk.Button(window, text = "Subtract Quantity", command = lambda : subQuantity())
    subtractButton.grid(row = 2, column = 2, pady = 5)