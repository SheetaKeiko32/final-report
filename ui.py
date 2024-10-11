from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
title = Tk()
title.config(bg="Black")
def tit():
    Button(title, text="Sign up",command=menu_signup).place(x=700, y=600, anchor="center")
    Button(title, text="Log in").place(x=800, y=600, anchor="center")

def menu_signup():
    title.withdraw()
    Signup = Toplevel()
    Signup.geometry("600x600")
    Signup.config(bg="Black")
    profile_files = []

    def save():
        nam = cbb3.get()
        password = pas.get()
        confirm = conf.get()
        filename = r"C:\Users\ASUS\OneDrive\Máy tính\Nordihydrocapsaicin\final-report\userlist.txt"

        if password == confirm and not(password == "" and nam == ""):
            with open(filename, "w") as f:
                f.write(f"Name: {nam} ")
                f.write(f"Password: {password}\n\n")
            messagebox.showinfo("Success", f"Information registered successfully to {profile_files}.")
        else:
            messagebox.showwarning("Failed", "Passwords do not match. Please try again.")


    cbb3 = Entry(Signup)
    cbb3.place(x=800, y=400, anchor="center",height=50,width=200)
    cbb3lab = Label(Signup, text="Name", fg="White", bg="Black", font=("Courier", 14, "bold"))
    cbb3lab.place(x=650, y=400, anchor="center")

    pas = Entry(Signup, show="*")
    pas.place(x=600, y=500, anchor="center",height=50,width=200)
    paslab = Label(Signup, text="Password", fg="White", bg="Black", font=("Courier", 14, "bold"))
    paslab.place(x=450, y=500, anchor="center")

    conf = Entry(Signup, show="*")
    conf.place(x=1000, y=500, anchor="center",height=50,width=200)
    conflab = Label(Signup, text="Confirm password", fg="White", bg="Black", font=("Courier", 14, "bold"))
    conflab.place(x=800, y=500, anchor="center")

    Button(Signup, text="Register", command=save).place(x=750, y=600, anchor="center")
    
    Signup.mainloop()

tit()
title.mainloop()