import tkinter
from tkinter import ttk
from tkinter import messagebox
import openpyxl
import os
import sqlite3

window = tkinter.Tk()
window.title("Data Entry Form")

#Data Entry Function
def data_entry():
    terms = terms_var.get()

    if terms == "Accepted.":
        first_name = fist_name_entry.get()
        last_name = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()

        registration = reg_var.get()
        courses = courses_spinbox.get()
        semester = semester_spinbox.get()

        print("Title: ", title,
              "\nFirst Name: ", first_name,
              "\nLast Name:", last_name,
              "\nAge: ", age,
              "\nNationality: ", nationality,
              "\nRegistration: ", registration,
              "\nCourses: ", courses,
              "\nSemesters: ", semester
              )
        messagebox.showinfo(title="Success", message= terms)
        print("\n--------------------------------------------------------------\n")

        #use raw string (r)
        filepath = r"D:\Python_Home_Exercise\Python_GUI\data.xlsx"
        heading = ["Title", "First Name", "Last Name", "Age", "Nationality",
                   "Registration", "Courses", "Semesters"]
        data = [title, first_name, last_name, age, nationality, registration, courses, semester]

        #os means (Operating System)
        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active

            sheet.append(heading)
            sheet.append(data)
            workbook.save(filepath)

        else:
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append(data)
            workbook.save(filepath)

        #Create table
        conn = sqlite3.connect('data.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                                (title TEXT, first_name TEXT, last_name TEXT, age INT,
                                nationality TEXT, registration TEXT, courses INT, semester INT)
                             '''
        conn.execute(table_create_query)

        #Insert data
        data_insert_query = '''INSERT INTO Student_Data 
                                (title, first_name, last_name, age, nationality, registration, courses, semester) 
                                VALUES (?,?,?,?,?,?,?,?)
                             '''

        #data tuple
        data_insert_tuple = (title, first_name, last_name, age, nationality, registration, courses, semester)
        cursor = conn.cursor()
        cursor.execute(data_insert_query,data_insert_tuple)
        conn.commit()
        conn.close()

    else:
        messagebox.showwarning(title="Error", message= terms)

#The whole frame
frame = tkinter.Frame(window)
frame.pack()

#User Information Frame
user_info_frame = tkinter.LabelFrame(frame, text= "User Information")
user_info_frame.grid(row= 0, column= 0)

#First Name (Label and Entry)
first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row= 0, column= 0)

fist_name_entry = tkinter.Entry(user_info_frame)
fist_name_entry.grid(row= 1, column= 0)

#Last Name (Label and Entry)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row= 0, column= 1)

last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row= 1, column= 1)

#Title (Label and Combobox)
title_label = tkinter.Label(user_info_frame, text="Title")
title_label.grid(row= 0, column= 2)

title_combobox = ttk.Combobox(user_info_frame, values= ["MR", "MISS"])
title_combobox.grid(row= 1, column= 2)

#Age (Label and Spinbox)
age_label = tkinter.Label(user_info_frame, text="Age")
age_label.grid(row= 2, column= 0)

age_spinbox = tkinter.Spinbox(user_info_frame, from_= 18, to= 200)
age_spinbox.grid(row= 3, column= 0)

#Nationality (Label and Combobox)
nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_label.grid(row= 2, column= 1)

nationality_combobox = ttk.Combobox(user_info_frame, values= ["Myanmar", "Thailand"])
nationality_combobox.grid(row= 3, column= 1)

#The user_info frame widget
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx= 10, pady= 5)

#Save Frame
save_frame = tkinter.LabelFrame(frame)
save_frame.grid(row= 1, column= 0)

#Registered (label and Checkbox)
reg_label = tkinter.Label(save_frame, text= "Registration")
reg_label.grid(row= 0, column= 0)

reg_var = tkinter.StringVar()
reg_checkbutton = tkinter.Checkbutton(save_frame, text= "Currently Registered.", variable= reg_var,
                                      onvalue= "Registered.", offvalue= "Not Registered.")
reg_checkbutton.grid(row= 1, column= 0)

#Courses (Label and Spinbox)
courses_label = tkinter.Label(save_frame, text="# Courses Completed.")
courses_label.grid(row= 0, column= 1)

courses_spinbox = tkinter.Spinbox(save_frame, from_= 0, to= 200)
courses_spinbox.grid(row= 1, column= 1)

#Semesters (Label and Spinbox)
semester_label = tkinter.Label(save_frame, text="# Semesters")
semester_label.grid(row= 0, column= 2)

semester_spinbox = tkinter.Spinbox(save_frame, from_= 0, to= 200)
semester_spinbox.grid(row= 1, column= 2)

#Save frame widget
for widget in save_frame.winfo_children():
    widget.grid_configure(padx= 12, pady= 5)

#Terms & Conditions frame
terms_conditions_frame = tkinter.LabelFrame(frame, text= "Terms & Conditions")
terms_conditions_frame.grid(row= 2, column= 0, sticky= "news")

#Terms & Conditions (Label and Check Button)
terms_var = tkinter.StringVar()
terms_conditions_checkbutton = tkinter.Checkbutton(terms_conditions_frame, text= "I accept the terms and conditions.",
                                                   variable= terms_var, onvalue= "Accepted.",
                                                   offvalue= "You didn't accept the terms and conditions.")
terms_conditions_checkbutton.grid(row= 0, column= 0, sticky= "news")

#Data Entry
entry_button = tkinter.Button(frame, text= "Data Entry", command= data_entry)
entry_button.grid(row= 3, column=0, sticky= "news")

#The whole frame widget
for widget in frame.winfo_children():
    widget.grid_configure(padx= 10, pady= 5)
window.mainloop()