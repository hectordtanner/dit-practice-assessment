from tkinter import *

class Person:
    def __init__(self, name, age, has_phone):
        self.name = name
        self.age = age
        self.has_phone = has_phone

class GatherDataGUi:
    def __init__(self, parent):
        self.current_name = StringVar()
        self.current_age = IntVar()
        self.current_has_phone = BooleanVar()
        self.current_has_phone.set(False)
        self.list_pos = 0

        self.get_data_frame = Frame(parent)
        self.display_data_frame = Frame(parent)
        self.get_data_frame.pack()

        self.add_data_label = Label(self.get_data_frame, text="Collecting Person Data")
        self.display_button = Button(self.get_data_frame, text="Show All", command=self.switch_to_display)
        self.add_data_label.grid(column=0, row=0)
        self.display_button.grid(column=1, row=0)

        self.name_entry_label = Label(self.get_data_frame, text="First name:")
        self.name_entry = Entry(self.get_data_frame, textvariable=self.current_name)
        self.name_entry_label.grid(column=0, row=1)
        self.name_entry.grid(column=1, row=1)

        self.age_entry_label = Label(self.get_data_frame, text="Age:")
        self.age_entry = Entry(self.get_data_frame, textvariable=self.current_age)
        self.age_entry_label.grid(column=0, row=2)
        self.age_entry.grid(column=1, row=2)

        self.has_phone_buttons_label = Label(self.get_data_frame, text="Do you have a mobile phone?")
        self.has_phone_yes = Radiobutton(self.get_data_frame, text="Yes", variable=self.current_has_phone, value=True)
        self.has_phone_no = Radiobutton(self.get_data_frame, text="No", variable=self.current_has_phone, value=False)
        self.has_phone_buttons_label.grid(column=0, row=3, rowspan=2)
        self.has_phone_yes.grid(column=1, row=3)
        self.has_phone_no.grid(column=1, row=4)

        self.enter_data_button = Button(self.get_data_frame, text="Enter Data", command=self.enter_data)
        self.enter_data_button.grid(column=0, row=5, columnspan=2)

        self.display_label = Label(self.display_data_frame, text="Displaying Person Data")
        self.add_data_button = Button(self.display_data_frame, text="Add New Person", command=self.switch_to_add)
        self.display_label.grid(column=0, row=0)
        self.add_data_button.grid(column=1, row=0)

        self.name_display_label = Label(self.display_data_frame, text="First name:")
        self.name_display = Label(self.display_data_frame, textvariable=self.current_name)
        self.name_display_label.grid(column=0, row=1)
        self.name_display.grid(column=1, row=1)

        self.age_display_label = Label(self.display_data_frame, text="Age:")
        self.age_display = Label(self.display_data_frame, textvariable=self.current_age)
        self.age_display_label.grid(column=0, row=2)
        self.age_display.grid(column=1, row=2)

        self.has_phone_label = Label(self.display_data_frame, text="__ has a mobile phone.")
        self.has_phone_label.grid(column=0, row=3, columnspan=2)

        self.previous_button = Button(self.display_data_frame, text="Previous", command=lambda: self.change_display(-1))
        self.next_button = Button(self.display_data_frame, text="Next", command=lambda: self.change_display(1))
        self.previous_button.grid(column=0, row=4)
        self.next_button.grid(column=1, row=4)
    
    def switch_to_display(self):
        self.get_data_frame.pack_forget()
        self.display_data_frame.pack()

    def switch_to_add(self):
        self.display_data_frame.pack_forget()
        self.get_data_frame.pack()

    def enter_data(self):
        print(f"Name: {self.current_name.get()} Age: {self.current_age.get()} Phone: {self.current_has_phone.get()}")

    def change_display(self, amount):
        print(f"moved {amount} through list")

if __name__ == "__main__":
    root = Tk()
    gui = GatherDataGUi(root)
    root.mainloop()