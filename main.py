from tkinter import *
import tkinter as tk
from bs4 import BeautifulSoup as bs
import html.parser
import requests as rq
import os, sys
#Create an instance of Tkinter Frame
root = tk.Tk()
#Set the geometry

# Define a function to return the Input data



# entry = Entry(root, width= 42)
# entry.place(relx= .5, rely= .5, anchor= CENTER)


def embedpost():
        input_link = ent_1.get()
        link = str(input_link).replace("www","m")
        res = rq.get(link)
        print("The status code is ", res.status_code)
        print("\n")
        soup_data = bs(res.text, 'html.parser')
        print(soup_data.title)
        print("\n")
        concl = soup_data.find_all('div',{'class' : 'bo bp'})

        s = str(concl[0]).split(",")
        sonuc = s[1]
        # ptype = input("Which format : \n1)Text \n2)Embed \n")
        # if ptype == "2":
        #         sonuc = (s[1])
        # else:
        #         sonuc = (s[2])
        output_widget = tk.Text(root, bg='#fff', fg='#000')
        output_widget.pack()
        output_widget.insert(tk.END, sonuc)
def textpost():
        input_link = ent_1.get()
        link = str(input_link).replace("www","m")
        res = rq.get(link)
        print("The status code is ", res.status_code)
        print("\n")
        soup_data = bs(res.text, 'html.parser')
        print(soup_data.title)
        print("\n")
        concl = soup_data.find_all('div',{'class' : 'bo bp'})

        s = str(concl[0]).split(",")
        sonuc = s[2]
        # ptype = input("Which format : \n1)Text \n2)Embed \n")
        # if ptype == "2":
        #         sonuc = (s[1])
        # else:
        #         sonuc = (s[2])
        output_widget = tk.Text(root, bg='#fff', fg='#000')
        output_widget.pack()
        output_widget.insert(tk.END, sonuc)
def restart():
        if __name__ == "__main__":
                root.quit()
                os.startfile("main.py")


Label(root, text="ID Finder").pack()
ent_1 = Entry(root)
but_1 = Button(root, text='Embed', command=embedpost)
but_2 = Button(root, text='Text', command=textpost)
but_3 = Button(root, text="New",command=restart )
but_1.pack()
but_2.pack()
but_3.pack()
ent_1.pack()
# tk.Button(root,text="Enter link",command = enter_link).pack()

# tk.Button(root, text='Embed Post', command=embedpost).pack()
# tk.Button(root, text='Text Post', command=textpost).pack()


root.geometry("700x250")
root.mainloop()