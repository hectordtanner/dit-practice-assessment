from tkinter import *

class Person:
    def __init__(self, name, age, has_phone):
        self.name = name
        self.age = age
        self.has_phone = has_phone

class GatherDataGUi:
    """Creates the looks and functionality of the GUI."""


    def __init__(self, parent):
        """Creates all GUI elements"""
        self.current_has_phone = BooleanVar()
        self.current_has_phone.set(False)
        self.people = []
        self.display_pos = 0

        self.get_data_frame = Frame(parent)
        self.display_data_frame = Frame(parent)
        self.get_data_frame.pack()

        self.add_data_label = Label(self.get_data_frame, text="Collecting Person Data")
        self.display_button = Button(self.get_data_frame, text="Show All", command=self.switch_to_display, state="disabled")
        self.add_data_label.grid(column=0, row=0)
        self.display_button.grid(column=1, row=0)

        self.name_entry_label = Label(self.get_data_frame, text="First name:")
        self.name_entry = Entry(self.get_data_frame)
        self.name_entry.bind("<KeyRelease>", self.disable_buttons)
        self.name_entry_label.grid(column=0, row=1)
        self.name_entry.grid(column=1, row=1)

        self.age_entry_label = Label(self.get_data_frame, text="Age:")
        self.age_entry = Entry(self.get_data_frame)
        self.age_entry.insert(0, "0")
        self.age_entry.bind("<KeyRelease>", self.disable_buttons)
        self.age_entry_label.grid(column=0, row=2)
        self.age_entry.grid(column=1, row=2)

        self.has_phone_buttons_label = Label(self.get_data_frame, text="Do you have a mobile phone?")
        self.has_phone_yes = Radiobutton(self.get_data_frame, text="Yes", variable=self.current_has_phone, value=True)
        self.has_phone_no = Radiobutton(self.get_data_frame, text="No", variable=self.current_has_phone, value=False)
        self.has_phone_buttons_label.grid(column=0, row=3, rowspan=2)
        self.has_phone_yes.grid(column=1, row=3)
        self.has_phone_no.grid(column=1, row=4)

        self.enter_data_button = Button(self.get_data_frame, text="Enter Data", command=self.enter_data, state="disabled")
        self.enter_data_button.grid(column=0, row=5, columnspan=2)

        self.display_label = Label(self.display_data_frame, text="Displaying Person Data")
        self.add_data_button = Button(self.display_data_frame, text="Add New Person", command=self.switch_to_data)
        self.display_label.grid(column=0, row=0)
        self.add_data_button.grid(column=1, row=0)

        self.name_display_label = Label(self.display_data_frame, text="First name:")
        self.name_display = Label(self.display_data_frame, text="")
        self.name_display_label.grid(column=0, row=1)
        self.name_display.grid(column=1, row=1)

        self.age_display_label = Label(self.display_data_frame, text="Age:")
        self.age_display = Label(self.display_data_frame, text="")
        self.age_display_label.grid(column=0, row=2)
        self.age_display.grid(column=1, row=2)

        self.has_phone_label = Label(self.display_data_frame, text="")
        self.has_phone_label.grid(column=0, row=3, columnspan=2)

        self.previous_button = Button(self.display_data_frame, text="Previous", command=lambda: self.change_display_pos(-1))
        self.next_button = Button(self.display_data_frame, text="Next", command=lambda: self.change_display_pos(1))
        self.previous_button.grid(column=0, row=4)
        self.next_button.grid(column=1, row=4)
    

    def switch_to_display(self):
        """Switches from data frame display frame"""
        self.get_data_frame.pack_forget()
        self.display_data_frame.pack()
        self.display_pos = 0
        self.update_display()


    def switch_to_data(self):
        """Switches from data frame display frame"""
        self.display_data_frame.pack_forget()
        self.get_data_frame.pack()


    def enter_data(self):
        """Adds the input data to the people list (as a Person object)"""
        self.people.append(Person(self.name_entry.get(), self.age_entry.get(), self.current_has_phone.get()))
        self.age_entry.delete(0, END)
        self.age_entry.insert(0, "0")
        self.name_entry.delete(0, END)
        self.current_has_phone.set(False)
        self.disable_buttons("")


    def change_display_pos(self, amount):
        """Changes the list position by amount, looping if it excedes the length of the people list"""
        self.display_pos += amount
        while self.display_pos < 0:
            self.display_pos += len(self.people)
        while self.display_pos >= len(self.people):
            self.display_pos -= len(self.people)
        self.update_display()


    def update_display(self):
        """Updates the labels on the display frame"""
        self.name_display.configure(text=self.people[self.display_pos].name)
        self.age_display.configure(text=self.people[self.display_pos].age)
        if self.people[self.display_pos].has_phone:
            self.has_phone_label.configure(text=f"{self.people[self.display_pos].name} has a phone.")
        else:
            self.has_phone_label.configure(text=f"{self.people[self.display_pos].name} does not have a phone.")
    
    def disable_buttons(self, arg):
        """Disables buttons that shouldn't be active"""
        if self.name_entry.get() == "" or int(self.age_entry.get()) <= 0:
            self.enter_data_button.configure(state="disabled")
        else:
            self.enter_data_button.configure(state="active")
        if len(self.people) == 0:
            self.display_button.configure(state="disabled")    
        else:
            self.display_button.configure(state="active") 
        print(arg)


if __name__ == "__main__":
    root = Tk()
    gui = GatherDataGUi(root)
    root.mainloop()