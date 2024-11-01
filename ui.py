from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

title = Tk()
title.configure(bg="Black")
title.title("MAIN MENU")
title.geometry("600x600")

image = Image.open(r"C:\Users\ASUS\Downloads\SPACE (2).jpg")
img = ImageTk.PhotoImage(image)
lab = Label(title, image=img)
lab.place(x=300, y=300, anchor="center")

def tit():
    Button(title, text="Sign up", command=signup, font=("Courier", 14, "bold")).place(x=300, y=300, anchor="center", height=50, width=200)
    Button(title, text="Log in", command=login, font=("Courier", 14, "bold")).place(x=300, y=400, anchor="center", height=50, width=200)
    Button(title, text="Play", font=("Courier", 14, "bold")).place(x=300, y=500, anchor="center", height=50, width=200)
    Label(title, text="Space Shooters", font=("Retro 8-Bit", 32, "bold")).place(x=300, y=100, anchor="center", height=50, width=500)

def signup():
    title.withdraw()
    Signup = Toplevel()
    Signup.geometry("600x600")
    Signup.config(bg="Black")

    def save():
        nam = cbb3.get().strip()
        password = pas.get().strip()
        confirm = conf.get().strip()
        filename = r"C:\Users\ASUS\OneDrive\Máy tính\Nordihydrocapsaicin\final-report\userlist.txt"

        if password == confirm and nam:
            with open(filename, "a") as f:
                f.write(f"{nam}:{password}\n")
            messagebox.showinfo("Success", "Information registered successfully.")
            title.wm_deiconify()
            Signup.withdraw()
        else:
            messagebox.showwarning("Failed", "Passwords do not match or fields are empty. Please try again.")

    Label(Signup, text="SIGN UP", fg="White", bg="Black", font=("Courier", 14, "bold"), height=50, width=200).place(anchor="center", x=300, y=100)

    cbb3 = Entry(Signup)
    cbb3.place(x=350, y=200, anchor="center", height=50, width=200)
    Label(Signup, text="Name", fg="White", bg="Black", font=("Courier", 14, "bold")).place(x=150, y=200, anchor="center")

    pas = Entry(Signup, show="*")
    pas.place(x=350, y=300, anchor="center", height=50, width=200)
    Label(Signup, text="Password", fg="White", bg="Black", font=("Courier", 14, "bold")).place(x=150, y=300, anchor="center")

    conf = Entry(Signup, show="*")
    conf.place(x=350, y=400, anchor="center", height=50, width=200)
    Label(Signup, text="Confirm password", fg="White", bg="Black", font=("Courier", 14, "bold")).place(x=150, y=400, anchor="center")

    Button(Signup, text="Register", command=save, font=("Courier", 14, "bold"), height=2, width=20).place(x=300, y=500, anchor="center")
    Signup.mainloop()

def login():
    title.withdraw()
    Login = Toplevel()
    Login.geometry("600x600")
    Login.config(bg="Black")

    def validate_login():
        nam = cbb3.get().strip()
        password = pas.get().strip()
        filename = r"C:\Users\ASUS\OneDrive\Máy tính\Nordihydrocapsaicin\final-report\userlist.txt"

        try:
            with open(filename, "r") as f:
                user_found = False
                for line in f:
                    user_info = line.strip().split(":")
                    if len(user_info) == 2:
                        user_name, user_password = user_info
                        if user_name == nam and user_password == password:
                            user_found = True
                            break

                if user_found:
                    messagebox.showinfo("Success", "You successfully logged in to your account.")
                    title.wm_deiconify()
                    Login.withdraw()
                else:
                    messagebox.showwarning("Failed", "Invalid username or password. Please try again.")
        except FileNotFoundError:
            messagebox.showwarning("Error", "User data not found. Please sign up first.")

    Label(Login, text="LOG IN", fg="White", bg="Black", font=("Courier", 14, "bold"), height=50, width=200).place(anchor="center", x=300, y=100)

    cbb3 = Entry(Login)
    cbb3.place(x=350, y=200, anchor="center", height=50, width=200)
    Label(Login, text="Name", fg="White", bg="Black", font=("Courier", 14, "bold")).place(x=150, y=200, anchor="center")

    pas = Entry(Login, show="*")
    pas.place(x=350, y=300, anchor="center", height=50, width=200)
    Label(Login, text="Password", fg="White", bg="Black", font=("Courier", 14, "bold")).place(x=150, y=300, anchor="center")

    Button(Login, text="Login", command=validate_login, font=("Courier", 14, "bold"), height=2, width=20).place(x=300, y=500, anchor="center")
    Login.mainloop()

tit()
title.mainloop()