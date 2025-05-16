from tkinter import *

def some_function(option_choosen):
    print(f"Option Choosen: {option_choosen}")

if __name__ == "__main__":
    root = Tk()
    root.geometry('1200x800')

    some_string = StringVar(root, value="Alberta")
    province_list = ["Alberta", "British Columbia", "Manitoba", "Saskatchewan"]
    for i in range(len(province_list)):
        Radiobutton(root, text = province_list[i], variable = some_string, value = province_list[i], command = lambda: some_function(some_string.get()), tristatevalue=0).pack()

    root.mainloop()