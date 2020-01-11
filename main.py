from tkinter import *
from tkinter import messagebox
import smtplib
from functools import partial
import re

subject = "Test"
msg = "This is a test message!"
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
    if validate(e) == True:
        emailaddr.append(e)
        e1.delete('0', END)
        txt()
    else:
        messagebox.showerror("Error", "Invalid Email")


def send_email(subject, msg):
    try:
        EMAIL_ADDRESS = email.get()
        PASSWORD = key.get()
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        for e in emailaddr:
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(EMAIL_ADDRESS, e, message)
        server.quit()
        messagebox.showinfo("Success", "Emails Sent Successfully")
        print("Success: Email sent!")
    except:
        messagebox.showerror("Error", "Failed To Send Email")


root.title("Email BOT")
root.geometry('200x200')


Label(root, text="Username:").grid(column=0, row=0)
Label(root, text="Password:").grid(column=0, row=1)
Label(root, text="Enter Email:").grid(column=0, row=3)

email = Entry(root)
email.grid(column=2, row=0)

key = Entry(root, show="*")
key.grid(column=2, row=1)

e1 = Entry(root)
e1.grid(column=2, row=3)


Button(root, command=getmail, text="Submit").grid(column=0, row=5)
Button(root, command=partial(send_email, subject, msg), text="Send").grid(column=2, row=5)
root.mainloop()

print(emailaddr)
