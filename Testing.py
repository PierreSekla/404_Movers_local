from codes import Code
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import Frame, Label, Tk, StringVar, OptionMenu, Radiobutton, RIGHT, NE, NW, Button
from Databases import Database
from visual import BarGraph

def get_edu_data(All_Codes, all_edu_empl_data):
    """
    purpose: this organizes the data from the edu_empl database
    parameter All_Codes: Code class
    parameter all_edu_empl_data: tuple (strings)
    return: dictionary dicionary of strings and inter
    """
    # for different provinces
    provinces = {}
    prov_values = All_Codes.get_LOC_ST_RES_values()
    for i in range(len(prov_values)):
        provinces[list(prov_values)[i]] = {}
    # organizing data according to province
    for i in range(len(all_edu_empl_data)):
        province_key = All_Codes.get_LOC_ST_RES_code(all_edu_empl_data[i][-1])
        key = All_Codes.get_HDGREE_code(all_edu_empl_data[i][0])
        province_dictionary = provinces[province_key].keys()
        if key not in province_dictionary:
            provinces[province_key][key] = 1
        else:
            provinces[province_key][key] += 1
    
    return provinces

def organize_by_subject(provinces, choosen_province, subject_choosen):
    """
    purpose: organize the data in each province by subject
    parameter provinces: dictionary data of all provinces and subjects
    parameter choosen_province: string
    parameter: subject_choosen: string
    returns: dictionary of strings
    """
    province_and_subject_data = {}
    if subject_choosen not in provinces[choosen_province].keys():
        province_and_subject_data[choosen_province] = 0
    else: 
        province_and_subject_data[choosen_province] = provinces[choosen_province][subject_choosen]
    return province_and_subject_data



if __name__ == "__main__":
    # Data gathering and organization
    all_edu_empl_data = Database().get_all_edu_empl()
    All_Codes = Code()
    provinces = None
    provinces = get_edu_data(All_Codes, all_edu_empl_data)

    the_graph = BarGraph(list(provinces["Alberta"].keys()), list(provinces["Alberta"].values()))


    # options
    root = Tk()
    root.geometry('1600x800')
    fig, ax = plt.subplots()

    # Tkinter application
    frame = Frame(root, height=700, width=1000)
    label = Label(text = "Matplotlib + Tkinter")
    label.pack()
    frame.pack(side=RIGHT, anchor=NE)

    # adding some functional buttons on tkinter
    exit_button = Button(root, text="Exit", command=exit, width=5, height=1)
    exit_button.pack(anchor=NW)

    # adding the radiobuttons from tkinter
    province_choosen = StringVar(root, value="Alberta")

    def choosen_province(province_choosen):
        """
        purpose: Adds functionality to the radio buttons
        parameter province_choosen: string
        return: none
        """
        if province_choosen == "Alberta":
            the_graph.change_graph_data(list(provinces['Alberta'].keys()), list(provinces['Alberta'].values()))

        elif province_choosen == "British Columbia":
            the_graph.change_graph_data(list(provinces["British Columbia"].keys()), list(provinces["British Columbia"].values()))

        elif province_choosen == "Saskatchewan":
            the_graph.change_graph_data(list(provinces["Saskatchewan"].keys()), list(provinces["Saskatchewan"].values()))

        elif province_choosen == "Manitoba":
            the_graph.change_graph_data(list(provinces["Manitoba"].keys()), list(provinces["Manitoba"].values()))

        elif province_choosen == "Ontario":
            the_graph.change_graph_data(list(provinces["Ontario"].keys()), list(provinces["Ontario"].values()))

        elif province_choosen == "Quebec":
            the_graph.change_graph_data(list(provinces["Quebec"].keys()), list(provinces["Quebec"].values()))

        elif province_choosen == "New Brunswick":
            the_graph.change_graph_data(list(provinces["New Brunswick"].keys()), list(provinces["New Brunswick"].values()))

        elif province_choosen == "Prince Edward Island":
            the_graph.change_graph_data(list(provinces["Prince Edward Island"].keys()), list(provinces["Prince Edward Island"].values()))

        elif province_choosen == "Nova Scotia":
            the_graph.change_graph_data(list(provinces["Nova Scotia"].keys()), list(provinces["Nova Scotia"].values()))

        elif province_choosen == "Newfoundland and Labrador":
            the_graph.change_graph_data(list(provinces["Newfoundland and Labrador"].keys()), list(provinces["Newfoundland and Labrador"].values()))

        elif province_choosen == "Northern Canada":
            the_graph.change_graph_data(list(provinces["Northern Canada"].keys()), list(provinces["Northern Canada"].values()))
        
        # labelling and adjustments
        the_graph.draw_graph_on_tkinter()


    for i in range(len(provinces.keys())):
        the_string = list(provinces.keys())[i]
        Radiobutton(root, text = the_string, variable = province_choosen, value=the_string, command=lambda: choosen_province(province_choosen.get())).pack()

    # adding the option menu
    subject_choosen = StringVar(root, value="No Certificate")

    def choosen_subject(provinces, province, subject):
        """
        purpose: checks to see what province is choosen and displays the data accordingly
        parameter provinces: dictionary of strings for all province data
        parameter province: string
        parameter subject: string
        return: None
        """
        province_subject_info = organize_by_subject(provinces, province, All_Codes.get_HDGREE_full_to_short(subject))
        the_graph.change_graph_data([subject], province_subject_info[province])
        the_graph.draw_graph_on_tkinter()
        

    drop = OptionMenu(root, subject_choosen, *All_Codes.get_HDGREE_full_names(), command = lambda x: choosen_subject(provinces, province_choosen.get(), subject_choosen.get()))
    drop.pack(pady=40)

    # integrating the matplotlib as backend for tkinter
    canvas = FigureCanvasTkAgg(fig, master = frame)
    canvas.get_tk_widget().pack()

    # adding the axis and canvas the to the bar graph class attributes
    the_graph.add_tkinter_ax_and_canvas(ax, canvas)
    # adding the toolbar
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    toolbar.pack()

    the_graph.draw_graph_on_tkinter()

    root.mainloop()
