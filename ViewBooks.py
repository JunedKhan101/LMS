from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import traceback
import tkinter as tk

# Add your own database name and password here to reflect in the code
mypass = "52338905"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"

def View():

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    y = 0.25

    getBooks = "SELECT * FROM " + bookTable

    try:
        cur.execute(getBooks)
        con.commit()
        rows = cur.fetchall()
        # lst = rows
        # total_rows = len(lst)
        # total_columns = len(lst[0])

        # print(rows[0])
        # print(rows[0][1])
        # print("Rows: ", len(rows))
        # print("Columns: ", len(rows[0]))
        # for i in range(0, len(rows)):
        #     Label(labelFrame, text="%-10s%40s%-20s%-20s%-40s%-20s%-10s%-10s"%(rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],rows[i][5],rows[i][6],rows[i][7]),bg='black',fg='white').place(relx=0.07,rely=y)
        #     print(i)
        #     y += 0.1
        print(rows)
        num_fields = len(cur.description)
        field_names = [i[0] for i in cur.description]




        for i in range(0, len(field_names)):
            e = tk.Entry(root)
            e.grid(row=0, column=i, sticky='we')
            root.grid_columnconfigure(0, weight=1)
            e.insert(END, field_names[i])

        for i in range(0, len(rows)):
            for j in range(0, len(rows[0])):
                # print("i = ", i)
                # print("j = ", j)
                # print(rows[i][j])

                e = tk.Entry(root)
                e.grid(row=i+1, column=j, sticky='we')
                root.grid_columnconfigure(0, weight=1)

                if rows[i][j] is not None:
                  e.insert(END, rows[i][j])
                else:
                  e.insert(END, "None")

    except Exception as err:
        traceback.print_exc()
        messagebox.showinfo("Error", "Failed to fetch files from database")

    root.mainloop()
