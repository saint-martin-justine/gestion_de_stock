import tkinter as tk
from tkinter import ttk
import mysql.connector

class StockManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Stock")

      
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Justine11081994.",
            database="store"
        )
        self.cursor = self.connection.cursor()

      
        self.create_gui()

    def create_gui(self):
        # Création du tableau 
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Nom', 'Description', 'Prix', 'Quantité', 'Catégorie'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Nom')
        self.tree.heading('#2', text='Description')
        self.tree.heading('#3', text='Prix')
        self.tree.heading('#4', text='Quantité')
        self.tree.heading('#5', text='Catégorie')

        # Ajout des boutons 
        btn_frame = ttk.Frame(self.root)
        btn_add = ttk.Button(btn_frame, text='Ajouter', command=self.add_product)
        btn_remove = ttk.Button(btn_frame, text='Supprimer', command=self.remove_product)
        btn_update = ttk.Button(btn_frame, text='Modifier', command=self.update_product)

       
        self.tree.pack(padx=10, pady=10)
        btn_add.grid(row=0, column=0, padx=5, pady=5)
        btn_remove.grid(row=0, column=1, padx=5, pady=5)
        btn_update.grid(row=0, column=2, padx=5, pady=5)
        btn_frame.pack()

      
        self.display_products()

    def display_products(self):
       
        for record in self.tree.get_children():
            self.tree.delete(record)

        # Récupérer les données 
        query = "SELECT * FROM product"
        self.cursor.execute(query)
        products = self.cursor.fetchall()

        # Affiche les produits dans le tableau
        for product in products:
            self.tree.insert('', 'end', values=product)

    def add_product(self):
      
        pass

    def remove_product(self):
      
        pass

    def update_product(self):
       
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = StockManagementApp(root)
    root.mainloop()
