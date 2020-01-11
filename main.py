from tkinter import *
from tkinter import messagebox
import smtplib
from functools import partial
import re

subject = "Test"
msg = "This is a test message!"

EMAIL_ADDRESS = "Your Email Address"
PASSWORD = "Your Password"
emailaddr = []

root = Tk()


def validate(t):
    reg = '[\w./-]{1,20}@[\w.-]{1,20}.[A-za-z]{2,3}'
    if re.search(reg, t):
        return True
    else:
        return False


def txt():
    with open('emails.txt', 'w') as f:
        for item in emailaddr:
            f.write("%s\n" % item)
    f.close()


def getmail():
    e = e1.get()
    if validate(e)== True:
        emailaddr.append(e)
        e1.delete('0', END)
        txt()
    else:
        messagebox.showerror("Error", "Invalid Email")


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        for e in emailaddr:
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(EMAIL_ADDRESS, e, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Message failed")


root.title("Calculating square root")
root.geometry('200x50')

Label(root, text="Enter Email: ").grid(column=0, row=0)
e1 = Entry(root)
e1.grid(column=1, row=0)

Button(root, command=getmail, text="Submit").grid(column=0, row=1)
Button(root, command=partial(send_email, subject, msg), text="Send").grid(column=1, row=1)
root.mainloop()

print(emailaddr)
