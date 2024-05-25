import tkinter as tk
from tkinter import messagebox
import re

def validate_email(email):
    pattern = r'^\w+@\w+\.(com|net|org|edu)$'
    return re.match(pattern, email) is not None

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(pattern, password) is not None

def submit_form():
    username = username_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    dob = dob_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid Email. It should end with @gmail.com, @yahoo.com, etc.")
        return
    if not validate_password(password):
        messagebox.showerror("Error", "Password must be at least 8 characters long, include an uppercase letter, a lowercase letter, a number, and a special character.")
        return
    
    print("Username:", username)
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("DOB:", dob)
    print("Email:", email)
    print("Password:", password)
    
    messagebox.showinfo("Submission Successful", "Thank you for registering!")
    
    username_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

app = tk.Tk()
app.title("Registration Form")

app.geometry("300x300")
padding = {"padx": 5, "pady": 5}

tk.Label(app, text="Username:").grid(row=0, column=0, sticky="w", **padding)
username_entry = tk.Entry(app)
username_entry.grid(row=0, column=1, **padding)

tk.Label(app, text="First Name:").grid(row=1, column=0, sticky="w", **padding)
first_name_entry = tk.Entry(app)
first_name_entry.grid(row=1, column=1, **padding)

tk.Label(app, text="Last Name:").grid(row=2, column=0, sticky="w", **padding)
last_name_entry = tk.Entry(app)
last_name_entry.grid(row=2, column=1, **padding)

tk.Label(app, text="DOB (dd/mm/yyyy):").grid(row=3, column=0, sticky="w", **padding)
dob_entry = tk.Entry(app)
dob_entry.grid(row=3, column=1, **padding)

tk.Label(app, text="Email:").grid(row=4, column=0, sticky="w", **padding)
email_entry = tk.Entry(app)
email_entry.grid(row=4, column=1, **padding)

tk.Label(app, text="Password:").grid(row=5, column=0, sticky="w", **padding)
password_entry = tk.Entry(app, show="*")
password_entry.grid(row=5, column=1, **padding)

submit_button = tk.Button(app, text="Submit", command=submit_form)
submit_button.grid(row=6, column=0, columnspan=2, **padding)

app.mainloop()
