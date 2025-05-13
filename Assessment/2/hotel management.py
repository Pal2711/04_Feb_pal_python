import tkinter
from tkinter import messagebox, ttk
import sqlite3

screen = tkinter.Tk()
screen.title("Hotel Management")
screen.geometry("400x500")
screen.config(background="white")

screen.grid_columnconfigure(0, weight=1)
screen.grid_columnconfigure(1, weight=1)
screen.grid_columnconfigure(2, weight=1)

db = sqlite3.connect("hotel.db")
cursor = db.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS studinfo (
    name TEXT,
    contact INTEGER,
    email TEXT,
    gender TEXT,
    state TEXT,
    city TEXT
) 
""")
db.commit()

checkin_window = list_window = checkout_window = info_window = None

def chekin():
    global checkin_window
    if checkin_window and checkin_window.winfo_exists():
        checkin_window.lift()
        return

    checkin_window = tkinter.Toplevel(screen)
    checkin_window.title("Guest Check-in")
    checkin_window.geometry("300x300")

    def close_window():
        global checkin_window
        checkin_window.destroy()
        checkin_window = None

    checkin_window.protocol("WM_DELETE_WINDOW", close_window)

    tkinter.Label(checkin_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    entry_name = tkinter.Entry(checkin_window)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    tkinter.Label(checkin_window, text="Contact:").grid(row=1, column=0, padx=10, pady=5)
    entry_contact = tkinter.Entry(checkin_window)
    entry_contact.grid(row=1, column=1, padx=10, pady=5)

    tkinter.Label(checkin_window, text="Email:").grid(row=2, column=0, padx=10, pady=5)
    entry_email = tkinter.Entry(checkin_window)
    entry_email.grid(row=2, column=1, padx=10, pady=5)

    tkinter.Label(checkin_window, text="Gender:").grid(row=3, column=0, padx=10, pady=5)
    gender_var = tkinter.StringVar(value="Male")
    tkinter.Radiobutton(checkin_window, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, sticky="w")
    tkinter.Radiobutton(checkin_window, text="Female", variable=gender_var, value="Female").grid(row=3, column=1, sticky="e")

    tkinter.Label(checkin_window, text="State:").grid(row=4, column=0, padx=10, pady=5)
    state_var = tkinter.StringVar()
    state_dropdown = ttk.Combobox(checkin_window, textvariable=state_var, values=["California", "Texas", "New York", "Florida", "Illinois"], state="readonly")
    state_dropdown.grid(row=4, column=1, padx=10, pady=5)
    state_dropdown.current(0)

    tkinter.Label(checkin_window, text="City:").grid(row=5, column=0, padx=10, pady=5)
    city_var = tkinter.StringVar()
    city_dropdown = ttk.Combobox(checkin_window, textvariable=city_var, values=["Los Angeles", "Houston", "Chicago", "Miami", "Dallas"], state="readonly")
    city_dropdown.grid(row=5, column=1, padx=10, pady=5)
    city_dropdown.current(0)

    def submit_data():
        name = entry_name.get()
        contact = entry_contact.get()
        email = entry_email.get()
        gender = gender_var.get()
        state = state_var.get()
        city = city_var.get()

        if name and contact and email:
            try:
                cursor.execute("INSERT INTO studinfo VALUES (?, ?, ?, ?, ?, ?)", (name, contact, email, gender, state, city))
                db.commit()
                messagebox.showinfo("Success", "Guest checked in successfully!")
                close_window()
            except Exception as e:
                messagebox.showerror("Error", f"Error occurred: {e}")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    tkinter.Button(checkin_window, text="Submit", command=submit_data, bg="green", fg="white").grid(row=6, column=1, pady=10)

def showlist():
    global list_window
    if list_window and list_window.winfo_exists():
        list_window.lift()
        return

    list_window = tkinter.Toplevel(screen)
    list_window.title("Guest List")
    list_window.geometry("500x300")

    def close_window():
        global list_window
        list_window.destroy()
        list_window = None

    list_window.protocol("WM_DELETE_WINDOW", close_window)

    tree = ttk.Treeview(list_window, columns=("Name", "Contact", "Email", "Gender", "State", "City"), show='headings')
    for col in tree["columns"]:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)

    cursor.execute("SELECT * FROM studinfo")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)

def checkout():
    global checkout_window
    if checkout_window and checkout_window.winfo_exists():
        checkout_window.lift()
        return

    checkout_window = tkinter.Toplevel(screen)
    checkout_window.title("Check Out")
    checkout_window.geometry("300x150")

    def close_window():
        global checkout_window
        checkout_window.destroy()
        checkout_window = None

    checkout_window.protocol("WM_DELETE_WINDOW", close_window)

    tkinter.Label(checkout_window, text="Enter Name to Check Out:").pack(pady=5)
    entry = tkinter.Entry(checkout_window)
    entry.pack(pady=5)

    def delete_guest():
        name = entry.get()
        if name:
            cursor.execute("DELETE FROM studinfo WHERE name = ?", (name,))
            db.commit()
            messagebox.showinfo("Success", "Guest checked out.")
            close_window()
        else:
            messagebox.showwarning("Input Error", "Enter a valid name.")

    tkinter.Button(checkout_window, text="Check Out", command=delete_guest, bg="red", fg="white").pack(pady=10)

def get_info():
    global info_window
    if info_window and info_window.winfo_exists():
        info_window.lift()
        return

    info_window = tkinter.Toplevel(screen)
    info_window.title("Get Info")
    info_window.geometry("300x200")

    def close_window():
        global info_window
        info_window.destroy()
        info_window = None

    info_window.protocol("WM_DELETE_WINDOW", close_window)

    tkinter.Label(info_window, text="Enter Name:").pack(pady=5)
    entry = tkinter.Entry(info_window)
    entry.pack(pady=5)

    def fetch():
        name = entry.get()
        if name:
            cursor.execute("SELECT * FROM studinfo WHERE name = ?", (name,))
            data = cursor.fetchone()
            if data:
                msg = f"Name: {data[0]}\nContact: {data[1]}\nEmail: {data[2]}\nGender: {data[3]}\nState: {data[4]}\nCity: {data[5]}"
                messagebox.showinfo("Guest Info", msg)
            else:
                messagebox.showwarning("Not Found", "No guest found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a name.")

    tkinter.Button(info_window, text="Search", command=fetch, bg="blue", fg="white").pack(pady=10)

def exit_app():
    db.close()
    screen.destroy()

tkinter.Button(screen, text="Check In", command=chekin, width=20, height=2).grid(row=2, column=1, pady=25)
tkinter.Button(screen, text="Show Guest List", command=showlist, width=20, height=2).grid(row=3, column=1, pady=10)
tkinter.Button(screen, text="Check Out", command=checkout, width=20, height=2).grid(row=4, column=1, pady=10)
tkinter.Button(screen, text="Guest Info", command=get_info, width=20, height=2).grid(row=5, column=1, pady=10)
tkinter.Button(screen, text="Exit", command=exit_app, bg="red", fg="white", width=20, height=2).grid(row=6, column=1, pady=25)

screen.mainloop()
