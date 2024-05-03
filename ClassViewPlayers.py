import tkinter as tk
from tkinter import ttk
from functools import partial

class Sportpage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create the Back button
        self.back_button = tk.Button(self, text='Back', width=10, bg='blue', fg='white', command=partial(self.back_onclick, parent))
        self.back_button.place(relx=0, rely=0, anchor='nw')  # Place the button in the top-left corner
        
        self.table_data = ''

    def fetch_data(self, parent):
        # Fetch data from the database using parent's cursor and select.GameID
        parent.cursor.execute("SELECT * FROM dbo.ViewTeamMembersWithParameters(?)", (parent.select.GameID,))
        self.table_data = parent.cursor.fetchall()

    def back_onclick(self, parent):
        # Show the main screen when Back button is clicked
        parent.show_screen(parent.main)

    def display_table(self, parent):
        # Create a Treeview widget to display the table data
        tree = ttk.Treeview(self)
        tree["columns"] = ("Team Name", "Players")

        # Configure columns and headings
        tree.column("#0", anchor="center", width=100)
        tree.heading("#0", text="Index")
        for column in ("Team Name", "Players"):
            tree.column(column, anchor="center", width=100)
            tree.heading(column, text=column)

        # Insert data into the Treeview
        for index, row in enumerate(self.table_data):
            tree.insert("", "end", text=str(index), values=(row[0], row[1]))

        # Place the Treeview widget below the Back button
        tree.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)  # Adjust placement and size

        # Ensure the Treeview widget remains visible and expandable
        tree.pack_propagate(False)
