#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install requests #install requests using pip


# In[3]:


import requests #import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': '',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')


def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_sms(num, msg)
    if r:
        showinfo("Send Success", "Successfully sent") #sends the success response to the system
    else:
        showerror("Error 404!", "Something went wrong..") #shows an error if its not found


# Creating GUI
root = Tk()
root.title("Message Sender ")
root.geometry("500x550")
font = ("Helvetica", 22, "bold")
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)
textMsg = Text(root)
textMsg.pack(fill=X) #pack up the message
sendBtn = Button(root, text="SEND SMS", command=btn_click)
sendBtn.pack()
root.mainloop()


# In[ ]:




