import tkinter as tk
from login import Login_RegisterPage, registerPage
import pyodbc
from sportsMain import Mainpage
from selectedSport import displayGames, displayGamesUpcoming
from ClassViewPlayers import Sportpage
from ClassBuyTicket import TicketPage



import tkinter as tk
from PIL import ImageTk, Image

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YALLA BEENA")
        self.geometry("620x500")
        self.current_screen = None
        self.activeUserId = -1
        server = 'DESKTOP-ANQOUQS'
        database = 'stadiumFinal'
        username = 'Badr'
        password = '123456789'

        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

        self.cursor = self.conn.cursor()
    

 
        self.green = "#21897E"
        self.beige = "#efe3da"
  

    def show_screen(self, screen):
        if self.current_screen:
            self.current_screen.pack_forget()  # Hide the current screen
        screen.pack(fill=tk.BOTH, expand=True)  # Show the new screen
        self.current_screen = screen

    def setUserID(self, id):
        self.activeUserId = id



if __name__ == "__main__":
    app = App()
    app.loginPage = Login_RegisterPage(app)
    app.main=Mainpage(app)
    app.registerpage = registerPage(app)
    app.select = displayGames(app)
    app.selectUpcoming = displayGamesUpcoming(app)
    app.viewplayers = Sportpage(app)
    app.tickets = TicketPage(app)

    app.show_screen(app.loginPage)  # Show the initial screen
    app.mainloop()



