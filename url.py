import pyperclip
import pyshorteners

from tkinter import *                # tkinter for GUI design

#define GUI for shortener

import urlshortener as urlshortener

root = Tk()

#set the geometry
root.geometry("400x250")
root.minsize(300,100)
root.maxsize(450,250)

# give a title
root.title("URL Shortener")

#set a background color
root.configure(bg="#49F")

#take 2 string variable for keep long and short URL
url = StringVar()
url_address = StringVar()

#define 2 function for shortening url and copy the url
def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root , text="  URL Shortener  " , font="poppins",
      bg="purple",fg="white").pack(pady=20)
Entry(root, textvariable=url,width=50).pack(pady=5)
Button(root, text="Generate Short URL", command=urlshortener,
       font=("verdana",10,"bold"),bg="#50C878",fg="white").pack(pady=7)
Entry(root, textvariable=url_address,width=30).pack(pady=5)
Button(root, text="Copy Short URL",command=copyurl,
       font=("verdana",10,"bold"),bg="#50C878",fg="white").pack(pady=5)

root.mainloop()