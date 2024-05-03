import tkinter as tk
from tkinter import ttk
import random
from functools import partial



class TicketPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
       
        self.back_button = tk.Button(self, text='Back', width=10, bg='blue', fg='white', command=partial(self.back_onclick, parent))
        self.back_button.place(relx=0, rely=0)
                               
        self.GameID = ''
        self.FanID = ''
        self.Sname = ''
        self.configure(bg= "#B1A1ED")



        
        # Create empty lists to store category and seat number data
        self.categories = ['1','2','3']
        self.seat_numbers = []
        
        # Populate the lists with data from the SQL function
        self.populate_data(parent)
        
        # Create Combobox widgets for categories and seat numbers

        self.heading_label = ttk.Label(self, text="Book Your Ticket", font=("Tw Cen MT Condensed Extra Bold", 26), foreground = "white",background="#B1A1ED")
        self.heading_label.place(relx=0.5, rely=0.35, anchor = 'center')

        self.category_label = tk.Label(self, text="Select Category",background="#B1A1ED", fg="white", font = 18 )
        self.category_label.place(relx=0.5,rely=0.45, anchor='center')
        self.category_combo = ttk.Combobox(self, values=self.categories)
        self.category_combo.place(relx=0.5,rely=0.5, anchor='center')
        
        self.seat_label = tk.Label(self, text="Select Seat Number",background="#B1A1ED", fg="white", font = 18)
        self.seat_label.place(relx=0.5,rely=0.6, anchor='center')
        self.seat_combo = ttk.Combobox(self, values=self.seat_numbers)
        self.seat_combo.place( relx=0.5,rely=0.65, anchor='center')

        self.fetch_button = tk.Button(self, text="BUY", command=partial(self.fetch_data, parent))
        self.fetch_button.place(relx=0.5, rely = 0.75, anchor='center')

    def populate_data(self,parent):
        # Call the SQL function to fetch available seats data
        parent.cursor.execute("SELECT category, SeatNumber FROM GetAvailableSeats()")
        rows = parent.cursor.fetchall()

        # Populate the lists with category and seat number data
        for row in rows:
            self.seat_numbers.append(row[1])

    def back_onclick(self,parent):
        parent.show_screen(parent.main)

    def fetch_data(self, parent):
        
        # Get the selected category and seat number
        selected_category = int(self.category_combo.get())
        selected_seat = self.seat_combo.get()
        
        # Calculate price based on category
        if selected_category == 1:
            price = 100
        elif selected_category == 2:
            price = 80
        elif selected_category == 3:
            price = 50
        else:
            # Handle invalid category
            price = 0  # Or any other default value
        
        # Calculate VNumber based on sport
        if self.Sname == "Basketball":
            vnumber = 'Gym1'
        elif self.Sname == "Volleyball":
            vnumber = 'Court1'
        elif self.Sname == "Handball":
            vnumber = 'Arena1'
        elif self.Sname == "Football":
            vnumber = 'Stadium1'
        else:
            # Handle invalid sport
            vnumber = 0  # Or any other default value
        
        # Generate random gate and ticket number
        generated_gate = int(self.generate_random_gate())
        generated_ticket = self.generate_random_ticket_number()
        print(generated_gate)
        print(generated_ticket)
        # Execute the SQL query with parameters
        parent.cursor.execute("EXEC UpdateSeatVariable ?", (selected_seat))
        parent.conn.commit()



        parent.cursor.execute("EXEC InsertTicket ?, ?, ?, ?, ?, ?, ?, ?, ?", 
                            (selected_category, price, generated_gate, 
                            generated_ticket, self.GameID, self.FanID, 
                            selected_seat, vnumber, self.Sname,))
        parent.conn.commit()
        ticket_details = {
            "Category": selected_category,
            "Price": price,
            "Gate": generated_gate,
            "Ticket Number": generated_ticket,
            "Game ID": self.GameID,
            "Fan ID": self.FanID,
            "Seat Number": selected_seat,
            "V Number": vnumber,
            "S Name": self.Sname
        }
        self.TicketDisplay(self, ticket_details)
        parent.show_screen(parent.selectUpcoming)
    

    class TicketDisplay(tk.Toplevel):
        def __init__(self, parent, ticket_details):
            super().__init__(parent)
            self.parent = parent
            self.ticket_details = ticket_details
            self.title("Ticket Details")
            self.config(bg = '#FFDE05')

            self.create_widgets()
            

        def create_widgets(self):
            ttk.Label(self,background='#FFDE05', text="Ticket Details", font=("Tw Cen MT Condensed Extra Bold", 16,"bold")).pack(pady=10)

            for key, value in self.ticket_details.items():
                ttk.Label(self,background='#FFDE05',text=f"{key}: {value}").pack(pady=5)

    @staticmethod
    def generate_random_gate():
        """Generate a random gate number from 1 to 5."""
        
        return random.randint(1, 5)
    
    @staticmethod
    def generate_random_ticket_number():
        """Generate a random ticket number in the format 'TicketXXXX'."""
        ticket_prefix = 'Ticket'
        ticket_suffix = str(random.randint(0, 9999)).zfill(4)  # Ensure 4-digit number
        return f"{ticket_prefix}{ticket_suffix}"
        

def main():
    root = tk.Tk()
    root.title("Test Login Page")
    root.geometry('400x300')
    root.configure(bg="green")

    ticket_page = TicketPage(root)
    ticket_page.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
