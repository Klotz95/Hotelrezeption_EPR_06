"""A simple GUI for a hotelreception software
"""

import tkinter

#creating a new window for reservation entry
def add_reservation():
    reservation_window = tkinter.Tk()
    reservation_window.title('add reservation')
    #create label 'first name'
    add_firstname_label = tkinter.Label(reservation_window, text='first name')
    #pack it in the reservation window
    add_firstname_label.pack()
    #create entry field for first name
    firstname_entry = tkinter.Entry(reservation_window)
    #pack it in reservatoin window
    firstname_entry.pack()

    #create label 'last name'
    add_lastname_label = tkinter.Label(reservation_window, text='last name')
    #pack it in the reservation window
    add_lastname_label.pack()
    #create entry field for first name
    lastname_entry = tkinter.Entry(reservation_window)
    #pack it in reservatoin window
    lastname_entry.pack()

    #create label 'birthdate'
    add_birthdate_label = tkinter.Label(reservation_window, text='Enter birthdate')
    #pack it in the reservation window
    add_birthdate_label.pack()
    #create entry field for first name
    birthdate_entry = tkinter.Entry(reservation_window)
    #pack it in reservatoin window
    birthdate_entry.pack()

    #creating a button to save reservation
    save_button = tkinter.Button(reservation_window, text='save')
    save_button.pack()

    #creating a button to close reservation window
    close_button = tkinter.Button(reservation_window, text='close')
    close_button.pack()



#create a new window
window = tkinter.Tk()
window.title('Hotelreception')

#creating a button for reservation
add_reservation_button = tkinter.Button(window, text='add reservation', command=add_reservation)
add_reservation_button.pack()

#creating a button for cancelling reservation
cancel_reservation_button = tkinter.Button(window, text='cancel reservation')
cancel_reservation_button.pack()

#creating a button for room management
room_management_button = tkinter.Button(window, text='room management')
room_management_button.pack()

#creating a button for customer management
customer_management_button = tkinter.Button(window, text='customer management')
customer_management_button.pack()

#creating a button for key management
key_management_button = tkinter.Button(window, text='key management')
key_management_button.pack()




#draw window at start
window.mainloop()
