import tkinter as tk
from tkinter import messagebox


class Person:
    def __init__(self, name: str, age: int, has_phone: bool):
        self.name = name
        self.age = age
        self.has_phone = has_phone
    

    def data_string(self):
        """Formats data into a string for external storage"""
        return (f"{self.name}|{self.age}|{self.has_phone}")
    

    def has_phone_string(self):
        """Formats phone data"""
        if self.has_phone:
            return f"{self.name} has a phone."
        else:
            return f"{self.name} does not have a phone."


class GatherDataGUi:
    """Creates the looks and functionality of the GUI."""


    def __init__(self, parent: tk.Tk):
        """Creates all GUI elements"""
        self.current_has_phone = tk.BooleanVar()
        self.current_has_phone.set(False)
        self.people: list[Person] = []
        self.display_pos = 0

        self.get_data_frame = tk.Frame(parent)
        self.display_data_frame = tk.Frame(parent)
        self.get_data_frame.pack()

        self.add_data_label = tk.Label(self.get_data_frame, text="Collecting Person Data")
        self.display_button = tk.Button(self.get_data_frame, text="Show All", command=lambda: self.switch_frame(True), state="disabled")
        self.add_data_label.grid(column=0, row=0)
        self.display_button.grid(column=1, row=0)

        self.name_entry_label = tk.Label(self.get_data_frame, text="First name:")
        self.name_entry = tk.Entry(self.get_data_frame)
        self.name_entry.bind("<KeyRelease>", self.disable_buttons)
        self.name_entry_label.grid(column=0, row=1)
        self.name_entry.grid(column=1, row=1)

        self.age_entry_label = tk.Label(self.get_data_frame, text="Age:")
        self.age_entry = tk.Entry(self.get_data_frame)
        self.age_entry.insert(0, "0")
        self.age_entry.bind("<KeyRelease>", self.disable_buttons)
        self.age_entry_label.grid(column=0, row=2)
        self.age_entry.grid(column=1, row=2)

        self.has_phone_buttons_label = tk.Label(self.get_data_frame, text="Do you have a mobile phone?")
        self.has_phone_yes = tk.Radiobutton(self.get_data_frame, text="Yes", variable=self.current_has_phone, value=True)
        self.has_phone_no = tk.Radiobutton(self.get_data_frame, text="No", variable=self.current_has_phone, value=False)
        self.has_phone_buttons_label.grid(column=0, row=3, rowspan=2)
        self.has_phone_yes.grid(column=1, row=3)
        self.has_phone_no.grid(column=1, row=4)

        self.enter_data_button = tk.Button(self.get_data_frame, text="Enter Data", command=self.enter_data, state="disabled")
        self.enter_data_button.grid(column=0, row=5, columnspan=2)

        self.display_label = tk.Label(self.display_data_frame, text="Displaying Person Data")
        self.add_data_button = tk.Button(self.display_data_frame, text="Add New Person", command=lambda: self.switch_frame(False))
        self.display_label.grid(column=0, row=0)
        self.add_data_button.grid(column=1, row=0)

        self.name_display_label = tk.Label(self.display_data_frame, text="First name:")
        self.name_display = tk.Label(self.display_data_frame, text="")
        self.name_display_label.grid(column=0, row=1)
        self.name_display.grid(column=1, row=1)

        self.age_display_label = tk.Label(self.display_data_frame, text="Age:")
        self.age_display = tk.Label(self.display_data_frame, text="")
        self.age_display_label.grid(column=0, row=2)
        self.age_display.grid(column=1, row=2)

        self.has_phone_label = tk.Label(self.display_data_frame, text="")
        self.has_phone_label.grid(column=0, row=3, columnspan=2)

        self.previous_button = tk.Button(self.display_data_frame, text="Previous", command=lambda: self.change_display_pos(-1))
        self.next_button = tk.Button(self.display_data_frame, text="Next", command=lambda: self.change_display_pos(1))
        self.previous_button.grid(column=0, row=4)
        self.next_button.grid(column=1, row=4)

        self.import_data_button = tk.Button(self.display_data_frame, text="Import Data", command=lambda: self.import_data(self.people, self.people))
        self.export_data_button = tk.Button(self.display_data_frame, text="Export Data", command=lambda: self.export_data(self.people))
        self.import_data_button.grid(column=0, row=5, columnspan=2)
    

    def switch_frame(self, to_display: bool):
        """Switches from data frame to display frame and vice versa"""
        if to_display:
            self.get_data_frame.pack_forget()
            self.display_data_frame.pack()
            self.display_pos = 0
            self.update_display()
        else:
            self.display_data_frame.pack_forget()
            self.get_data_frame.pack()


    def enter_data(self):
        """Adds the input data to the people list (as a Person object)"""
        person = Person(self.name_entry.get(), int(self.age_entry.get()), self.current_has_phone.get())
        if not self.check_duplicate(person.name, self.people):
            self.add_data(person.data_string())
            self.people.append(person)
        else:
            messagebox.showerror(title="Duplicate", message="Name already in database")
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, "0")
        self.name_entry.delete(0, tk.END)
        self.current_has_phone.set(False)
        self.disable_buttons("")
        

    def change_display_pos(self, amount: int):
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
        try:
            if self.name_entry.get() == "" or int(self.age_entry.get()) <= 0 or "|" in self.name_entry.get():
                self.enter_data_button.configure(state="disabled")
            else:
                self.enter_data_button.configure(state="active")
        except ValueError:
            self.enter_data_button.configure(state="disabled")
        
        if len(self.people) == 0:
            self.display_button.configure(state="disabled")    
        else:
            self.display_button.configure(state="active")
    

    def import_data(self, import_loc: list[Person], exclude: list[Person]):
        """Imports data from a file"""
        with open("people_data.txt", "r") as file:
            imported:list[str] = file.read().splitlines()
        
        for person_data in imported:
            if len(person_data.split("|")) == 3:
                person = Person(person_data.split("|")[0], int(person_data.split("|")[1]), False)                
                if person_data.split("|")[2] == "True":
                    person.has_phone = True

                if not self.check_duplicate(person.name, exclude):    
                    import_loc.append(person)


    def check_duplicate(self, name: str, check_against:list[Person]):
        for p in check_against:
            if p.name == name:
                return True
        return False


    def add_data(self, data):
        """Adds data to a file"""
        with open("people_data.txt", "a") as file:
            file.write(f"\n{data}")


    def export_data(self, data: list[Person]):
        checking_list = []
        self.import_data(checking_list, [])
        for new_person in data:
            if not self.check_duplicate(new_person.name, checking_list):
                self.add_data(new_person.data_string())


if __name__ == "__main__":
    root = tk.Tk()
    gui = GatherDataGUi(root)
    root.mainloop()