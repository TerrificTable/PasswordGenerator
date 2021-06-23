import tkinter as tk
import random
import time

window = tk.Tk()
window.title("PasswordGen ")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

label2 = tk.Label(text="enter how much digits your password should have")
length = tk.Entry(fg="black", bg="white", width=25)

def create():
        if(length.get() != ""):
            print("just debug: ")
            print('password:')
            password = ''
            for c in range(int(length.get())):
                password += random.choice(chars)
                print(password)
                f = open("passwords.txt", "w+")
                f.write(password)
                f.write("")
                f.write("this program was made by: Dom10k and TerrificTable55")
        
            window.destroy
            f.close


button = tk.Button(
    text="Create Password/s",
    width=15,
    height=2,
    bg="white",
    fg="black",
    command=create
)


label2.pack()
length.pack()
button.pack()
window.mainloop()