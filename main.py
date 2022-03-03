import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
from string import ascii_lowercase, ascii_uppercase
from random import choice, randint
import csv


password1 = ""

# Gets password

def getps():
    usrname1 = usernameentry.get()
    url2 = websiteentry.get().title()
    data = pd.read_csv("./data.csv")
    data1 = data.website.to_list()
    if url2 in data1:
        data2 = data[data.website == url2]
        data3 = data[data.website == url2].username.to_list()
        if usrname1 in data3:
            data4 = data2[data2.username == usrname1]
            data5 = data4.password.to_list()
            return data5[0]
        else:
            return "none"
    else:
        return "none"

def gps1():
    ps3 = getps()
    passwordentry.delete(0,"end")
    passwordentry.insert(0, ps3)

# Password Creator

lcl = [i for i in ascii_lowercase]
ucl = [i for i in ascii_uppercase]
no_s = [str(i) for i in range(10)]
symbs = ["!","@","#","^","_"]
def passy():
    i = randint(8, 15)
    passw = ""
    for j in range(i):
        passw += choice(lcl + ucl + no_s + symbs)
    return passw

# Generate password

def genps():
    global password1
    text = passy()
    passwordentry.delete(0, "end")
    passwordentry.insert(0, text)
    

# Database

def store1():
    password1 = passwordentry.get()
    username1 = usernameentry.get()
    url1 = websiteentry.get()
    with open("./data.csv", mode="a") as file:
        file.write(f"\n{url1},{username1},{password1}")

# UI Setup

windows = tk.Tk()
windows.title("Password - Manager")
# windows.minsize(500, 400)
windows.config(padx=10, pady=20, bg="black")

img1 = Image.open("./lock.png")
img2 = img1.resize((150, 150), Image.BOX)
img = ImageTk.PhotoImage(img2)


canvas = tk.Canvas(windows, width=200, height=200, bg="black", highlightthickness=0)
canvas.grid()

canvas.create_image(150, 100, image = img)

website = tk.Label(text="Website:", bg="black", fg="white")
website.grid(column=0, row=2)

websiteentry = tk.Entry(width=35, highlightthickness=0, highlightcolor="black")
websiteentry.grid(column=1, row=2, pady=10)

username = tk.Label(text="Email/Username:", bg="black", fg="white")
username.grid(column=0, row=3)

usernameentry = tk.Entry(width=35, highlightthickness=0)
usernameentry.grid(column=1, row=3, pady=10)

password = tk.Label(text="Pasword:", fg="white", bg="black", highlightthickness=0)
password.grid(column=0, row=4)

passwordentry = tk.Entry(highlightthickness=0, bd=0, width=20)
passwordentry.grid(column=1, row=4, pady=10)

generatepassword = tk.Button(text="Generate Password", command=genps,
 highlightthickness=0, bg="black", fg="white")
generatepassword.grid(column=2, row=4)

addbtn = tk.Button(text="Add", highlightthickness=0, bg="black", fg="white", command=store1)
addbtn.grid(column=1, row=5)

getbtn = tk.Button(text="Get Password", highlightthickness=0, bg="black", fg="white", command=gps1)
getbtn.grid(column=1, row=6, pady=20)

windows.mainloop()
