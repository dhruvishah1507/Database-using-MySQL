# import pymysql as ps

# conn = ps.connect(host="127.0.0.1", port=3306, user="root",password="", database="user")

# cur = conn.cursor()
# # cur.execute("Create Table NewData(userid int, name text, email text, address text)")
# # cur.execute("Insert into NewData Values(1,'Vikash','vikash@gmail.com','Mumbai')")
# cur.execute("Select * from NewData")
# print(cur.fetchall())
# conn.commit()

'''import pymysql as ps
conn = ps.connect(host="127.0.0.1", port = 3306, user = "root", password ="", database="user")
cur = conn.cursor()
# cur.execute("Create Table NewData (userid int, name text, email text, address text)")
userid = input("Enter ur id: ")
name = input ("Enter your name: ")
email = input("Enter your email: ")
address = input("Enter your address: ")
cur.execute("Insert into NewData values(%s,%s,%s,%s)", (userid,name ,email, address))
cur.execute("Select * from NewData")
for i in cur.fetchall():
    print(i)
conn.commit()'''

import customtkinter as ctk
import pymysql as ps

window = ctk.CTk()
window.geometry("400x500")
window.resizable(width=False,height=False)
window.title("Database")

label=ctk.CTkLabel(window, text = "Database",font=("Vardana",24)).pack(pady=10)
userid =ctk.CTkEntry(window, placeholder_text= "userid",font=("Vardana",18))
userid.pack(pady=10)
name =ctk.CTkEntry(window, placeholder_text= "name",font=("Vardana",18))
name.pack(pady=10)
email =ctk.CTkEntry(window, placeholder_text= "email",font=("Vardana",18))
email.pack(pady=10)
addrs =ctk.CTkEntry(window, placeholder_text= "address",font=("Vardana",18))
addrs.pack(pady=10)
newbtnn = ctk.CTkButton(window, text="Save to the Database", command=lambda:data())
newbtnn.pack()

def data():
    conn = ps.connect(host="127.0.0.1", port = 3306, user = "root", password ="", database="user")
    cur = conn.cursor()
    id = userid.get()
    n = name.get()
    e = email.get()
    a = addrs.get()
    cur.execute("Insert into NewData values(%s,%s,%s,%s)", (id,n ,e, a))
    cur.execute("Select * from NewData")
    for i in cur.fetchall():
     print(i)
    conn.commit()

window.mainloop()






