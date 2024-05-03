from functools import partial
import tkinter as tk
import pyodbc




class Login_RegisterPage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
     


        login_label = tk.Label(self, text='Please Login:', font=('Tw Cen MT Condensed Extra Bold', 28))
        login_label.place(relx=0.17, rely=0.3, anchor='center')
        login_label.configure(bg='#B1A1ED',fg='white')


        titel_label = tk.Label(self, text='Welcome to YALLA BEENA!', font=('Tw Cen MT Condensed Extra Bold', 35))
        titel_label.place(relx=0.5, rely=0.1, anchor='center')
        titel_label.configure(bg='#B1A1ED',fg='white')

        # Create username label and entry
        self.login_username_label = tk.Label(self, text='Username:', font=('Irace Bold ITC', 20))
        self.login_username_label.place(relx=0.25, rely=0.45, anchor='e')
        self.login_username_label.configure(bg='#B1A1ED',fg='white')


        self.login_username_entry = tk.Entry(self)
        self.login_username_entry.place(relx=0.26, rely=0.55, anchor='e')

        # Create password label and entry
        login_password_label = tk.Label(self, text='Password:', font=('Irace Bold ITC', 20))
        login_password_label.place(relx=0.25, rely=0.65, anchor='e')
        login_password_label.configure(bg='#B1A1ED',fg='white')


        self.login_password_entry = tk.Entry(self, show='*')
        self.login_password_entry.place(relx=0.26, rely=0.75, anchor='e')

        # Create login button
        login_button = tk.Button(self, text='Login', width=10, bg='blue', fg='white', command=partial(self.login_onclick, parent))
        login_button.place(relx=0.231, rely=0.85, anchor='e')

        self.configure(bg= "#B1A1ED")

        self.reg_label = tk.Label(self, text='Dont Have an Account?,\n Sign up!', font=('Tw Cen MT Condensed Extra Bold', 22))
        self.reg_label.place(relx=0.95, rely=0.3, anchor = 'e')
        self.reg_label.configure(bg='#B1A1ED',fg='white')

        

        self.reg_button = tk.Button(self, text='Register', width=10, bg='blue', fg='white', command=partial(self.registerpage_onclick, parent))
        self.reg_button.place(relx=0.8, rely=0.4, anchor='e')


    def registerpage_onclick(self, parent):
        parent.show_screen(parent.registerpage)

    def login_onclick(self,parent): 
      
        Fanid = self.login_password_entry.get()
        Name = self.login_username_entry.get()

        print(Fanid)
        print(Name)


        query = "EXEC GetUserInfo1 @Fanid=?, @FName=?"
        parent.cursor.execute(query, (Fanid, Name))       
        rows = parent.cursor.fetchall()
        print(rows)

        parent.conn.commit()    

        for row in rows:
            if row.FanID==Fanid and row.FName == Name:
                parent.show_screen(parent.main)

                parent.setUserID(Fanid)

                print(parent.activeUserId)
            
            else:
                print ("no")
                


        


       
    
    

            

class registerPage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.back_button = tk.Button(self, text='Back', width=10, bg='blue', fg='white', command=partial(self.back_onclick, parent))
        self.back_button.place(relx=0, rely=0)

        self.login_label = tk.Label(self, text='Register:', font=('Tw Cen MT Condensed Extra Bold', 35))
        self.login_label.place(relx=0.25, rely=0.2, anchor='center')
        self.login_label.configure(bg='#B1A1ED',fg='white')


        self.titel_label = tk.Label(self, text='YALLA BEENA!', font=('Tw Cen MT Condensed Extra Bold', 35))
        self.titel_label.place(relx=0.5, rely=0.1, anchor='center')
        self.titel_label.configure(bg='#B1A1ED',fg='white')

    #1
        self.reg_username_label = tk.Label(self, text='Enter Username:', font=('Tw Cen MT Condensed Extra Bold', 22))
        self.reg_username_label.place(relx=0.15, rely=0.3, anchor='center')
        self.reg_username_label.configure(bg='#B1A1ED',fg='white')


        self.reg_username_entry = tk.Entry(self)
        self.reg_username_entry.place(relx=0.305, rely=0.35, anchor='e')
    #2
        self.reg_fanid_label = tk.Label(self, text='Enter Fan ID:', font=('Tw Cen MT Condensed Extra Bold', 22))
        self.reg_fanid_label.place(relx=0.115, rely=0.45, anchor='center')
        self.reg_fanid_label.configure(bg='#B1A1ED',fg='white')


        self.reg_fanid_entry = tk.Entry(self)
        self.reg_fanid_entry.place(relx=0.305, rely=0.5, anchor='e')
    #3
        self.reg_bdate_label = tk.Label(self, text='Enter Birth Date:', font=('Tw Cen MT Condensed Extra Bold', 22))
        self.reg_bdate_label.place(relx=0.15, rely=0.6, anchor='center')
        self.reg_bdate_label.configure(bg='#B1A1ED',fg='white')


        self.reg_bdate_entry = tk.Entry(self)
        self.reg_bdate_entry.place(relx=0.305, rely=0.65, anchor='e')

        self.reg_button = tk.Button(self, text='Register', width=10, bg='green', fg='white', command=partial(self.register_onclick, parent))
        self.reg_button.place(relx=0.231, rely=0.8, anchor='e')

        self.configure(bg= "#B1A1ED")

    def register_onclick(self, parent):
        # Retrieve input values from entry widgets
        fan_id = self.reg_fanid_entry.get()
        fan_name = self.reg_username_entry.get()
        birth_date = self.reg_bdate_entry.get()

        # Check if any field is empty
        if not fan_id.strip() or not fan_name.strip() or not birth_date.strip():
            # Display an error message if any field is empty
            print("Please fill in all fields.")
            return

        # Execute the registration procedure if all fields are filled
        parent.cursor.execute("EXEC addFan @FanId = ?, @FName = ?, @bdate = ?", (fan_id, fan_name, birth_date))
        parent.conn.commit()
        parent.show_screen(parent.loginPage)

    def back_onclick(self,parent):
        parent.show_screen(parent.loginPage)


def main():
    root = tk.Tk()
    root.title("Test Login Page")
    root.geometry('600x500')

    # Create and pack the Login_RegisterPage frame
    login_register_page = registerPage(root)
    login_register_page.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()