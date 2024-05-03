import tkinter as tk
from PIL import Image, ImageTk
from functools import partial


class Mainpage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.sport = ""
        
        
        # Function to create buttons with images as background
        def create_image_button(self, image_path, command):
            img = Image.open(image_path)
            img = img.resize((100, 100))
            img = ImageTk.PhotoImage(img)
            button = tk.Button(self, image=img, command=command, bg="white", borderwidth=0)
            button.image = img  # Keep a reference to the image to prevent garbage collection
            return button

    
        # Set background color
        self.configure(bg="white")


        # Create welcome message
        welcome_label = tk.Label(self, text="YALLABEENA", bg="white", fg="black", font=("Irace Bold ITC", 25))
        welcome_label.place(relx=0.5, rely=0.05, anchor="center")

        #  Create title label
        title_label = tk.Label(self, text="Choose your Sport", bg="white", fg="black", font=("Tw Cen MT Condensed Extra Bold", 22))
        title_label.place(relx=0.5, rely=0.13, anchor="center")

        # Create buttons for sports
        football_button = create_image_button(self, "football.png", lambda: self.display_selected_sport(parent, "Football"))
        volleyball_button = create_image_button(self, "volleyball.png", lambda: self.display_selected_sport(parent,"Volleyball"))
        handball_button = create_image_button(self, "handball.png", lambda: self.display_selected_sport(parent,"Handball"))
        basketball_button = create_image_button(self, "basketball.png", lambda: self.display_selected_sport(parent,"Basketball"))

        football_button.place(relx=.4, rely=.5, anchor="center")
        volleyball_button.place(relx=.66, rely=.49, anchor="center")
        handball_button.place(relx=0.4, rely=.8, anchor="center")
        basketball_button.place(relx=0.66, rely=.79, anchor="center")

        self.back_button = tk.Button(self, text='Back', width=10, bg='blue', fg='white', command=partial(self.back_onclick, parent))
        self.back_button.place(relx=0, rely=0)

        # Create a label to display selected sport

        options = ["Previous", "Upcoming"]
        



      
        # Create a Tkinter variable to hold the selected option
        self.var = tk.StringVar(value = "")
        i=-0.235
        for option in options:
                # Create a radio button for each option
            i=i+0.20
            radio_button = tk.Radiobutton(self, text=option, variable=self.var, value=option)
            radio_button.pack(anchor=tk.W)
            radio_button.configure(indicatoron=False)

            radio_button.place(relx=(0.4+i), rely=0.25)

    def display_selected_sport(self,parent,selected_sport):
            self.sport=selected_sport
            #print(self.sport)
            if self.var.get() == 'Previous':
                parent.select.createTreePrevious(parent)
                parent.show_screen(parent.select)
            elif self.var.get() == 'Upcoming':
                parent.selectUpcoming.createTree(parent)
                parent.show_screen(parent.selectUpcoming)
            else:
                print("Please select type")

    def back_onclick(self,parent):
        parent.show_screen(parent.loginPage)
        parent.loginPage.login_password_entry.delete(0, tk.END)
        parent.loginPage.login_username_entry.delete(0, tk.END)




















def main():
    root = tk.Tk()
    root.title("Test Login Page")
    root.geometry('600x500')

    # Create and pack the Login_RegisterPage frame
    login_register_page = Mainpage(root)
    login_register_page.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()