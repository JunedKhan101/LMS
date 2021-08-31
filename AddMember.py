from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import traceback

def memberRegister():

    memid = int(bookInfo1.get())
    fname = str(bookInfo2.get())
    lname = str(bookInfo3.get())

    insert_member = "INSERT INTO %s VALUES(%d, '%s', '%s')" % (member_table, memid, fname, lname)
    try:
        cur.execute(insert_member)
        con.commit()
        messagebox.showinfo("Success", "Member added successfully")
    except:
        traceback.print_exc()
        messagebox.showinfo("Error", "Can't add data into Database")

    root.destroy()

def addMember():

    global bookInfo1,bookInfo2,bookInfo3, Canvas1,con,cur,member_table,root

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "52338905"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    member_table = "members" # Book Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Member", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.7)

    # Member ID
    lb1 = Label(labelFrame,text="Member ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.08, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.06)

    # First Name
    lb2 = Label(labelFrame,text="First Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.18, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.06)

    # Last Name
    lb3 = Label(labelFrame,text="Last Name : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.28, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.06)

    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=memberRegister)
    SubmitBtn.place(relx=0.28,rely=0.92, relwidth=0.09,relheight=0.06)

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.92, relwidth=0.09,relheight=0.06)

    root.mainloop()
