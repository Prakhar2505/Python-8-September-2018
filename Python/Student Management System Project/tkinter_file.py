


import tkinter as tk
import student_database_sample as st


mainWindow = tk.Tk()
mainWindow.title('Student Management System')

heading = tk.Label(mainWindow, text='Student Management System')
heading.pack()

student_name = tk.Label(mainWindow, text = 'Student Name')
student_name.pack()

student_name_entry = tk.Entry(mainWindow)
student_name_entry.pack()

student_name = tk.Label(mainWindow, text = 'College Name')
student_name.pack()

college_entry = tk.Entry(mainWindow)
college_entry.pack()

student_name = tk.Label(mainWindow, text = 'Phone Name')
student_name.pack()

phone_entry = tk.Entry(mainWindow)
phone_entry.pack()

student_name = tk.Label(mainWindow, text = 'Address Name')
student_name.pack()

address_entry = tk.Entry(mainWindow)
address_entry.pack()

def takeValueInput():
    name = student_name_entry.get()
    college = college_entry.get()
    address = address_entry.get()
    phone = int(phone_entry.get())

    st.insert_record(name, college, address, phone)


save_button = tk.Button(mainWindow, text='Save Record',
                        command = lambda : takeValueInput())
save_button.pack()

display_button = tk.Button(mainWindow, text='Display Record')
display_button.pack()



mainWindow.mainloop()


