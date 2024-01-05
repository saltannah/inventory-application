import tkinter as tk #import the gui interface controls
from tkinter import messagebox #imports the messagebox display
import sqlite3 #import sqlite for database management
from tkinter import ttk #additional features such as TREE VIEW WINDOW
from inventory import * #import everything from inventory file

#view current inventory function
def viewCurr(currentWin):
    global inventoryWin
    inventoryWin = tk.Tk()
    inventoryWin.title("Current Inventory")
    inventoryWin.geometry("420x280+450+200")
    currentWin.withdraw()#temporarily close main window

    inventoryPage(inventoryWin)

    itemBtn = tk.Button(inventoryWin, text = "[Item Check In/Check Out]", command = lambda : itemPage(inventoryWin), relief = "groove", activebackground = "mint cream")
    itemBtn.grid(row = 2, column = 0, padx = 5)
    # requestBtn = tk.Button(inventoryWin, text = "[Order Request Form]", command = lambda : requestPage(inventoryWin), relief = "groove", activebackground = "mint cream")
    # requestBtn.grid(row = 2, column = 1)
    homeBtn = tk.Button(inventoryWin, text = "[Back to Home Page]", command = lambda : homePage(), relief = "groove", activebackground = "mint cream")
    homeBtn.grid(row = 2, column = 2, padx = 5)

    inventoryWin.mainloop()

def itemPage(currentWin):
    global itemWin
    itemWin = tk.Tk()
    itemWin.title("Check In/Out")
    itemWin.geometry("420x350+450+180")
    currentWin.withdraw()

    itemAdjust(itemWin)

    #buttons to navigate to other windows
    inventoryBtn = tk.Button(itemWin, text = "[View Current Inventory]", command = lambda : viewCurr(itemWin), relief = "groove", activebackground = "mint cream")
    inventoryBtn.grid(row = 5, column = 0, padx = 5, pady = 5)
    # requestBtn = tk.Button(itemWin, text = "[Order Request Form]", command = lambda : requestPage(itemWin), relief = "groove", activebackground = "mint cream")
    # requestBtn.grid(row = 5, column = 1, padx = 5, pady = 5)
    homeBtn = tk.Button(itemWin, text = "[Back to Home Page]", command = lambda : homePage(), relief = "groove", activebackground = "mint cream")
    homeBtn.grid(row = 5, column = 2, padx = 5, pady = 5)

    itemWin.mainloop()

#optional request page if necessary
# def requestPage(currentWin):
#     global requestWin
#     requestWin = tk.Tk()
#     requestWin.title("Materials Request")
#     requestWin.geometry("300x250+500+200")
#     currentWin.withdraw()

def closeWin(): #if any windows are open, close them
    try:
        inventoryWin.destroy()
    except:
        pass

    try:
        itemWin.destroy()
    except:
        pass

def homePage():
    closeWin()

    global mainWin
    mainWin = tk.Tk() #create the window interface
    mainWin.geometry("300x250+500+200")
    mainWin.title("Welcome Page") #Label for the title

    prompt = tk.Label(mainWin, text = "Welcome to the inventory application!\nPlease select an action: ")
    prompt.pack()

    #window navigation buttons
    inventoryBtn = tk.Button(mainWin, text = "[View Current Inventory]", command = lambda : viewCurr(mainWin), relief = "groove", activebackground = "mint cream")
    inventoryBtn.pack(fill = "both", expand = True)
    itemBtn = tk.Button(mainWin, text = "[Item Check In/Check Out]", command = lambda : itemPage(mainWin), relief = "groove", activebackground = "mint cream")
    itemBtn.pack(fill = "both", expand = True)
    # requestBtn = tk.Button(mainWin, text = "[Order Request Form]", command = lambda : requestPage(mainWin), relief = "groove", activebackground = "mint cream")
    # requestBtn.pack(fill = "both", expand = True)

    mainWin.mainloop()

homePage()