# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 23:17:43 2021
Python 3.8
@author: Dito
Aplikasi Shop Management dengan simple GUI
"""

# Penggunaan library tkinter sebagai GUI
import tkinter as tk
from tkinter import ttk

### Functions ###
#Fungsi System Menu Button
def ShowChoice():
    if v.get() == 1:
        itemList()
    elif v.get() == 2:
        addNewItem()
    elif v.get() == 3:
        restockItem()
    elif v.get() == 4:
        sellItem()
    elif v.get() == 5:
        editItem()
    elif v.get() == 6:
        closeWindow()
        
#Fungsi untuk 'mereset' data button dan Entry (menghide widget dalam GUI)
def forgetPack():
    #Hide
    chooseItem.forget()
    inputItemName.forget()
    inputPrice.forget()
    inputQty.forget()
    addButton.forget()
    
    #Reset content
    chooseItem.delete(0,"end")
    inputItemName.delete(0,"end")
    inputPrice.delete(0,"end")
    inputQty.delete(0,"end")
    
#Mendisplay Tabel
def Display():
    #Mereset isi tabel
    for i in table.get_children():
        table.delete(i)
    
    count = 0
    #Memasukkan data kembali
    for data in items:
        table.insert(parent='', index='end', iid=count, text="Parent", values=(count+1,data[0], data[1], data[2]))
        count += 1
    #Menampilkan tabel di GUI
    table.pack(pady=10)

#Function untuk menu Item List
def itemList():
    forgetPack()
    Display()
        
#Function untuk menu Add New Item - mereset widget => edit button & entry => tampilkan seluruh widget dalam frame
def addNewItem():
    forgetPack()
    
    inputItemName.insert(0, "Enter the Item Name. . .")
    inputPrice.insert(0, "Enter the Item Price. . .")
    inputQty.insert(0, "Enter the Item Quantity. . .")
    
    addButton.config(command=inputNewItem)
    
    inputItemName.pack(pady=5, anchor="w")
    inputPrice.pack(pady=5, anchor="w")
    inputQty.pack(pady=5, anchor="w")
    addButton.pack(pady=5, anchor="w")
    
#Function Button untuk Add New Item - memproses data - clear array => add data dalam array => tampilkan
def inputNewItem():
    if items == [["no data", "no data", "no data"]]:
        items.clear()
        if int(inputPrice.get()) < 0 or int(inputQty.get()) < 0:
            tk.messagebox.showerror("ERROR", "Invalid NUMBER!")
        else:
            addItem = [inputItemName.get(), int(inputPrice.get()), int(inputQty.get())]
            items.append(addItem)
            Display()
    else:
        if int(inputPrice.get()) < 0 or int(inputQty.get()) < 0:
            tk.messagebox.showerror("ERROR", "Invalid NUMBER!")
        else:
            addItem = [inputItemName.get(), int(inputPrice.get()), int(inputQty.get())]
            items.append(addItem)
            Display()
    
#Function untuk menu restockItem - mereset widget => edit button & entry => tampilkan seluruh widget dalam frame
def restockItem():
    forgetPack()
    
    addButton.config(command=inputRestockItem)
    
    chooseItem.insert(0, "Nomor Item yang akan diRestock. . .")
    inputQty.insert(0,"Jumlah Restock. . .")
    
    chooseItem.pack(pady=5, anchor="w")
    inputQty.pack(pady=5, anchor="w")
    addButton.pack(pady=5, anchor="w")
    
#Function Button untuk restockItem - memproses data - if else untuk menghindari error => edit data di array => tampilkan
def inputRestockItem():
    if int(inputQty.get()) < 0 or (int(chooseItem.get()) < 0 or (int(chooseItem.get()) - 1) >= len(items)):
        tk.messagebox.showerror("ERROR", "Invalid NUMBER!")
    else:
        items[int(chooseItem.get()) - 1][2] = items[int(chooseItem.get()) - 1][2] + int(inputQty.get())
        Display()

#Function untuk menu sellItem - mereset widget => edit button & entry => tampilkan seluruh widget dalam frame
def sellItem():
    forgetPack()
    
    addButton.config(command=inputSellItem)
    
    chooseItem.insert(0, "Nomor Item yang akan diJual. . .")
    inputQty.insert(0,"Jumlah Jual. . .")
    
    chooseItem.pack(pady=5, anchor="w")
    inputQty.pack(pady=5, anchor="w")
    addButton.pack(pady=5, anchor="w")

#Function Button untuk sellItem - memproses data - if else untuk menghindari error => edit data di array => tampilkan
def inputSellItem():
    if int(inputQty.get()) < 0 or (int(chooseItem.get()) < 0 or (int(chooseItem.get()) - 1) >= len(items)):
        tk.messagebox.showerror("ERROR", "Invalid NUMBER!")
    else:
        items[int(chooseItem.get()) - 1][2] = items[int(chooseItem.get()) - 1][2] - int(inputQty.get())
        Display()
        total = items[int(chooseItem.get()) - 1][1] * int(inputQty.get())
        tk.messagebox.showinfo("INCOME", "Total Penjualan: " +str(total))

#Function untuk menu Edit Item - mereset widget => edit button & entry => tampilkan seluruh widget dalam frame
def editItem():
    forgetPack()
    
    chooseItem.insert(0, "Nomor Item yang akan diEdit. . .")
    inputItemName.insert(0, "Enter the Item Name. . .")
    inputPrice.insert(0, "Enter the Item Price. . .")
    inputQty.insert(0, "Enter the Item Quantity. . .")
    
    addButton.config(command=inputEditItem)
    
    chooseItem.pack(pady=5, anchor="w")
    inputItemName.pack(pady=5, anchor="w")
    inputPrice.pack(pady=5, anchor="w")
    inputQty.pack(pady=5, anchor="w")
    addButton.pack(pady=5, anchor="w")
    
#Function Button untuk Edit Item - memproses data - if else digunakan untuk menghindari terjadinya sebuah error
def inputEditItem():
    if int(inputPrice.get()) < 0 or int(inputQty.get()) < 0 or (int(chooseItem.get()) < 0 or (int(chooseItem.get()) - 1) >= len(items)):
            tk.messagebox.showerror("ERROR", "Invalid NUMBER!")
    else:
        items.pop(int(chooseItem.get()) - 1)
        items.insert(int(chooseItem.get()) - 1, [inputItemName.get(), int(inputPrice.get()), int(inputQty.get())])
        Display()

#Function untuk keluar dari GUI
def closeWindow():
    root.destroy()

### Database - Name,Price,Stock ### - Untuk menyimpan Data
items = [["no data", "no data", "no data"]]
### END Database ###


### Window Settings ###
root = tk.Tk()  #Pembuatan Window GUI
root.title("Shop Management")   #Title GUI
root.geometry("1000x600")   #Besaran GUI
root.configure(bg="#708090")    #Warna BG GUI
### END Window Settings ###


### Frame Settings ### - Untuk meng'layout' tampilan di GUI agar rapi
topFrame = tk.Frame(root, width=100, height=100, bg="#778899")  #Pembuatan Frame
topFrame.pack() #Menampilkan Frame
botFrame = tk.Frame(root, width=900, height=300, bg="#B0C4DE")  #Pembuatan Frame
botFrame.pack(pady = 20)    #Menampilkan Frame dengan jarak
### END Frame Settings ###


### System Menu ###
v = tk.IntVar()
v.set(1)  # menginisialisasi pilihan dalam menu

#Array untuk menyimpan attribut Menu Button
choose = [("Item List", 1),
   	     ("Add New Item", 2),
    	 ("Restock Item", 3),
         ("Sell Item", 4),
         ("Edit Item", 5), 
         ("Exit", 6)]

#Menambah tulisan pada GUI diatas Menu Button
tk.Label(topFrame, 
         text="""Select Menu:""", font="CourierNew 16 bold",
         justify = tk.LEFT,
         padx = 20).pack(side=tk.TOP)

#Pembuatan Button Menu
for show, val in choose:
    tk.Radiobutton(topFrame, 
                  text=show, font="CourierNew 13 italic",
                  indicatoron = 0,
                  width = 10,
                  height = 5,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(side=tk.LEFT, anchor ="n", padx=3, pady = 6)
### END System Menu ###


### Pembuatan Tabel ###
table = ttk.Treeview(botFrame)
    
#Mendefinisikan Tabel
table['columns'] = ("No", "Name", "Price", "Qty")
    
#Format Kolom
table.column("#0", width=0,stretch=tk.NO)   #Meniadakan Phantom Heading
table.column("No", anchor=tk.CENTER, width=40, minwidth=40) #Set untuk minimal lebar dan alignment pada kolom
table.column("Name", anchor=tk.W, width=120, minwidth=100)
table.column("Price", anchor=tk.CENTER, width=120, minwidth=100)
table.column("Qty", anchor=tk.CENTER, width=100, minwidth=70)
    
#Headings - untuk menampilkan text di Headings
table.heading("#0") #Phantom heading
table.heading("No", text="No.", anchor=tk.CENTER)
table.heading("Name", text="Item Name", anchor=tk.CENTER)
table.heading("Price", text="Item Price", anchor=tk.CENTER)
table.heading("Qty", text="Item Stock", anchor=tk.CENTER)
### END Tabel ###


### Menu pada addNewItem ###
#box untuk input
inputItemName = tk.Entry(botFrame, width=40)
inputPrice = tk.Entry(botFrame, width=40)
inputQty = tk.Entry(botFrame, width=40)

#Button untuk input
addButton = tk.Button(botFrame, width=15, height=3, text="Input Data")
### END addNewItem ###


### Menu pada restockItem ###
#box untuk input
chooseItem = tk.Entry(botFrame, width=40)
### END restrockItem ###
    

### Main ###
Display()
root.mainloop()