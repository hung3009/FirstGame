from tkinter import*
from tkinter import ttk
from functools import partial
from tkinter.messagebox import showinfo

root = Tk ()
root.geometry ("350x250")
root.title ("Login")

fo = open("data.txt", "w")
def getvals():
    print("username entered: ", username.get(),"\npassword entered: ", password.get())
    print ("SUCCESS")
    fo = open("data.txt", "w")
    fo.write("username enterred: ")
    fo.write(username.get())
    fo.write("\npassword entered: ")
    fo.write(password.get())
    fo.close()
 
#Heading
Label (root, text = "Login here ", font =("Impact", 35, "bold"),fg="#6162FF").grid(row=0,column=4)
#Field Name
username = Label(root, text = "User Name")
password = Label(root, text = "Password")

#Packing Name
username.grid(row=10, column=3)
password.grid(row=12, column=3)

# Variable for storing data
username = StringVar()
password = StringVar()

#Creating entry field
checkvalue = IntVar
nameentry = Entry(root, textvariable=username)
passentry = Entry(root, textvariable=password, show="*")


# Packing entry field
nameentry.grid (row=10, column=4)
passentry.grid (row=12, column=4)

validateLogin = partial(getvals, username, password)

#Creating check box
checkbtn = Checkbutton(text = "remember me?", variable=checkvalue)
checkbtn.grid (row=20, column=4)

#Submit button
Button (text ="Submit", command=getvals).grid(row=25,column=4)

root.mainloop()