from functools import partial
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class displayGames(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.back_button = tk.Button(self, text='<--', width=10, bg='blue', fg='white', command=partial(self.back_onclick, parent))
        self.back_button.place(relx=0,rely=0)

        print(parent.main.sport + "mmm")

        self.GameID=""

        games_label = tk.Label(self, text='Games:', font=('Helvetica', 30))
        games_label.place(relx=0.5, rely=0.16, anchor='center')

        select_label = tk.Label(self, text='Select Game ID:', font=('Helvetica', 15))
        select_label.place(relx=0.5, rely=0.8, anchor='center')

        select_button = tk.Button(self, text='View Teams\' Info', width=10, bg='pink', fg='white', command = partial(self.viewPlayers,parent))
        select_button.configure(width=13, fg='black')
        select_button.place(relx=0.6, rely=0.9, anchor='center')

        self.select_entry = tk.Entry(self)
        self.select_entry.place(relx=0.4, rely=0.9, anchor='center')

        self.rowsin = []


        parent.conn.commit()
        parent.cursor.execute("Exec printAllGames")
        self.rows = parent.cursor.fetchall()
        print(self.rows)

    def createTreePrevious(self,parent):
        tree = ttk.Treeview(self)
        tree["columns"] = ("Game ID","Team 1", "Team 2", "Score", "Date")
        tree.column("#0", anchor="center", width=100)
        tree.heading("#0", text="Index")
        
        for column in ("Game ID","Team 1", "Team 2", "Score", "Date"):
            tree.column(column, anchor="center", width=100)
            tree.heading(column, text=column)
        
        for index, row in enumerate(self.rows):
            if row.Sname == parent.main.sport and row.Date < '2024-04-28':
                tree.insert("", "end", text=str(index), values=(row.GameID ,row.Team1, row.Team2, row.Score, row.Date))
        
        tree.place(relx = 0.5, rely=0.5, anchor="center")
    
    def viewPlayers(self, parent):
        self.GameID = self.select_entry.get()
        # Fetch data and display table
        parent.viewplayers.fetch_data(parent)
        parent.viewplayers.display_table(parent)
        parent.show_screen(parent.viewplayers)






    def back_onclick(self,parent):
        parent.show_screen(parent.main)
        




class displayGamesUpcoming(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.back_button = tk.Button(self, text='Back', width=10, bg='blue', fg='white', command=partial(self.back_onclick, parent))
        self.back_button.place(relx=0,rely=0)

        

        print(parent.main.sport + 'badrawi')

        games_label = tk.Label(self, text='Games:', font=('Helvetica', 30))
        games_label.place(relx=0.5, rely=0.1, anchor='center')

        select_label = tk.Label(self, text='Select Game ID:', font=('Helvetica', 15))
        select_label.place(relx=0.5, rely=0.7, anchor='center')

        select_button = tk.Button(self, text='View Teams\' Info', width=10, bg='pink', fg='white', command = partial(self.viewPlayers1, parent))
        select_button.configure(width=13, fg='black')
        select_button.place(relx=0.6, rely=0.9, anchor='center')

        buy_button = tk.Button(self, text='Buy', width=10, bg='pink', fg='white',command = partial(self.buyTicket, parent))
        buy_button.configure(width=13, fg='black') 
        buy_button.place(relx=0.4, rely=0.9, anchor='center')

        self.select_entry = tk.Entry(self)
        self.select_entry.place(relx=0.5, rely=0.8, anchor='center')


        parent.conn.commit()
        parent.cursor.execute("Exec printAllGames")
        self.rows = parent.cursor.fetchall()
        
    
    def createTree(self,parent):
        tree = ttk.Treeview(self)
        tree["columns"] = ("Game ID","Team 1", "Team 2", "Score", "Date")
        tree.column("#0", anchor="center", width=100)
        tree.heading("#0", text="Index")
        
        for column in ("Game ID","Team 1", "Team 2", "Score", "Date"):
            tree.column(column, anchor="center", width=100)
            tree.heading(column, text=column)
        
        for index, row in enumerate(self.rows):
            if row.Sname == parent.main.sport and row.Date > '2024-04-28':
                tree.insert("", "end", text=str(index), values=(row.GameID ,row.Team1, row.Team2, row.Score, row.Date))
        
        tree.place(relx = 0.5, rely=0.4, anchor="center")
    
    def back_onclick(self,parent):
        parent.show_screen(parent.main)

    def viewPlayers1(self,parent):
        parent.select.GameID = self.select_entry.get()
        parent.viewplayers.fetch_data(parent)
        parent.viewplayers.fetch_data(parent)
        parent.viewplayers.display_table(parent)
        parent.show_screen(parent.viewplayers)
            
    
    def buyTicket(self, parent):
        
        parent.tickets.populate_data(parent)
        parent.tickets.Sname=parent.main.sport
        parent.tickets.GameID = self.select_entry.get()
        parent.tickets.FanID = parent.activeUserId
        print(parent.activeUserId)
        parent.show_screen(parent.tickets)

        
        
    




def main():
    root = tk.Tk()
    root.title("Allsports")
    window_width = 600
    window_height = 500  # Adjusted height to accommodate sport names
    root.geometry(f"{window_width}x{window_height}")

    # Create and pack the Login_RegisterPage frame
    login_register_page = displayGames(root)
    login_register_page.pack(fill=tk.BOTH, expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()