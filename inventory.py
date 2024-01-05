import tkinter as tk
from tkinter import ttk #used for Tree View and Combobox
import sqlite3
from tkinter import messagebox #for error messageboxes

def inventoryDisplay(window, row): #displays the current inventory in a tree view
    inventoryTable = ttk.Treeview(window, columns = ("Item", "Quantity"), show = ["headings"])
    inventoryTable.grid(row = row, column = 0, columnspan = 3, padx = 10, pady = 5)
    inventoryTable.heading("Item", text = "Item")
    inventoryTable.heading("Quantity", text = "Quantity")

    conn = sqlite3.connect("C:\\Users\\Hannah\\OneDrive\\Desktop\\summer python\\SQLite\\Inventory Application.db")
    c = conn.cursor() #connect to inventory database

    c.execute("SELECT Item, Quantity FROM Inventory")
    rows = c.fetchall() #retrieves all from SQL database
    for i in rows:
        inventoryTable.insert('', 'end', values=(i[0], i[1])) #displays every row in the tree view table

def inventoryPage(window):
    inventoryDisplay(window, 0)
    conn = sqlite3.connect("C:\\Users\\Hannah\\OneDrive\\Desktop\\summer python\\Inventory Application.db")
    c = conn.cursor()
        
def quantityAdjust(window): #contains all functions for the check in/check out window
    prompt = tk.Label(window, text = "Select an item from the list: ")
    prompt.grid(row = 0, column = 0)
    
    menuValues = ["shirts", "hoodies", "dri-fit", "jackets"] #list of initial items to use as default

    def selectionBox(): #initializing the combobox
        selected = tk.StringVar()
        global menu
        menu = ttk.Combobox(window, textvariable = selected)
        menu['values'] = menuValues
        menu.grid(row = 1, column = 0)
    
    selectionBox()#calls combobox function to refresh the options

    #label and entry for the quantity
    quantityLabel = tk.Label(window, text = "Enter the Quantity to Add or Subtract: ")
    quantityLabel.grid(row = 0, column = 1, columnspan = 2)

    quantityEntry = tk.Entry(window)
    quantityEntry.grid(row = 1, column = 1, columnspan = 2)

    def addQuantity(): #function to increase item quantity
        conn = sqlite3.connect("C:\\Users\\Hannah\\OneDrive\\Desktop\\summer python\\SQLite\\Inventory Application.db")
        c = conn.cursor()
        add = quantityEntry.get()
        try:#try to insert the item and quantity to the data table
            c.execute("INSERT into Inventory (item, quantity) values (?, ?)", (menu.get(), add))
            conn.commit()
            if menu.get() not in menuValues:
                menuValues.append(menu.get())
            selectionBox()
        except:#if item is already in table, add to the quantity
            c.execute("SELECT quantity from Inventory WHERE item = ?", (menu.get(),))
            currQuantity = c.fetchone()
            quantity = int(currQuantity[0]) + int(add)
            c.execute("UPDATE Inventory SET quantity = ? WHERE item = ?", (quantity, menu.get()))
            conn.commit()
        
        inventoryDisplay(window, 4)


    def subQuantity(): #function to decrease item quantity
        conn = sqlite3.connect("C:\\Users\\Hannah\\OneDrive\\Desktop\\summer python\\SQLite\\Inventory Application.db")
        c = conn.cursor()
        sub = quantityEntry.get()
        c.execute("SELECT quantity from Inventory WHERE item = ?", (menu.get(),))
        currQuantity = c.fetchone() #gets the current quantity from the SQL table
        quantity = int(currQuantity[0]) - int(sub)
        if quantity > 0:
            c.execute("UPDATE Inventory SET quantity = ? WHERE item = ?", (quantity, menu.get()))
            conn.commit()
        else:
            warning = messagebox.showerror(title = "Error", message = "Quantity cannot be negative")

        inventoryDisplay(window, 4)

    
    def delItem(): #deletes row of selected item
        try:
            conn = sqlite3.connect("C:\\Users\\Hannah\\OneDrive\\Desktop\\summer python\\SQLite\\Inventory Application.db")
            c = conn.cursor()
            c.execute("DELETE from Inventory WHERE item = ?", (menu.get(),))
            conn.commit()
        except: #if item is not in inventory, show an error
            warning = messagebox.showerror(title = "Error", message = "Must Select an Item in Inventory")
        
        inventoryDisplay(window, 4)

    #buttons to delete items and add/remove item quantity
    delButton = tk.Button(window, text = "Delete Item", command = lambda : delItem())
    delButton.grid(row = 2, column = 0, pady = 5)

    addButton = tk.Button(window, text = "Add Quantity", command = lambda : addQuantity())
    addButton.grid(row = 2, column = 1, pady = 5)

    subtractButton = tk.Button(window, text = "Subtract Quantity", command = lambda : subQuantity())
    subtractButton.grid(row = 2, column = 2, pady = 5)

def itemAdjust(window):
    quantityAdjust(window)
    inventoryDisplay(window, 4)