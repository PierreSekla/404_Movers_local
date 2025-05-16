from Databases import Database
from codes import Code
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, StringVar, OptionMenu

class BarGraph:
    def __init__(self, x_axis, data):
        self.__x_axis = x_axis
        self.__data = data
        self.__radio = None
        self.__fig, self.__radio_axis = plt.subplots()

        # variables for tkinter
        self.__tkinter_canvas = None
        self.__tkinter_ax = None

    
    def add_radio_buttons(self, bg_color, radio_labels, active_color):
        """
        purpose: adds radio buttons for the graph
        parameter bg_color: string ==> for changing the background color
        parameter radio_labels: list(strings) ==> for the label of each radio button
        parameter active_color: string ==> for the color of the selected radio button
        return: None
        """
        plt.subplots_adjust(left = 0.4)
        # [left adjustment x position, height level adjustment, box width, box height]
        rax = plt.axes([0.01, 0.5, 0.25, 0.40], facecolor = bg_color)
        self.__radio = RadioButtons(rax, radio_labels, activecolor=active_color)
    
    def get_radio_axis(self):
        return self.__radio_axis
    
    def get_figure(self):
        return self.__fig

    def get_radio_buttons(self):
        return self.__radio
    
    def draw_graph(self, title, xname, yname):
        """
        purpose: draws the bar graph
        parameter: None
        return: None
        """
        self.__radio_axis.bar(self.__x_axis, self.__data, color="blue")
        self.__radio_axis.tick_params(axis='x', labelsize=7)
        # change the titles
        self.__radio_axis.set_title(title, fontsize=30)
        self.__radio_axis.set_xlabel(xname, fontsize=15)
        self.__radio_axis.set_ylabel(yname, fontsize=15)

        plt.show()
    
    def add_tkinter_ax_and_canvas(self, ax, canvas):
        """
        purpose: saves the axis and canvas for when the graph is drawn
        parameter ax: object
        parameter canvas: object
        """
        self.__tkinter_ax = ax
        self.__tkinter_canvas = canvas
    
    def change_graph_data(self, x_data, data):
        """
        purpose: gives the graph different data to make the bar graph
        parameter x_data: list of strings
        parameter data: list of numbers
        return: None
        """
        self.__x_axis = x_data
        self.__data = data
    
    def draw_graph_on_tkinter(self):
        """
        purpose: this is meant for the tkinter integration
        """
        self.__tkinter_ax.clear()
        #plotting and making the graph
        self.__tkinter_ax.bar(self.__x_axis, self.__data, color = "blue")
        self.__tkinter_ax.tick_params(axis='x', labelsize=7)
        self.__tkinter_ax.set_title("Educational Attainment", fontsize=20)
        self.__tkinter_ax.set_xlabel("Education", fontsize=15)
        self.__tkinter_ax.set_ylabel("Number of People", fontsize=15)

        self.__tkinter_canvas.draw()

if __name__ == "__main__":
    # basic variables
    # all the different titles
    title = "Educational Attainment"
    xname = "Education"
    yname = "Number of People"
    All_Codes = Code()
    # for different provinces
    provinces = {}
    prov_values = All_Codes.get_LOC_ST_RES_values()
    for i in range(len(prov_values)):
        provinces[list(prov_values)[i]] = {}
    # organizing data according to province
    all_edu_empl_data = Database().get_all_edu_empl()
    for i in range(len(all_edu_empl_data)):
        province_key = All_Codes.get_LOC_ST_RES_code(all_edu_empl_data[i][-1])
        key = All_Codes.get_HDGREE_code(all_edu_empl_data[i][0])
        province_dictionary = provinces[province_key].keys()
        if key not in province_dictionary:
            provinces[province_key][key] = 1
        else:
            provinces[province_key][key] += 1

    # making the bar graph for Alberta as a start
    some_graph = BarGraph(list(provinces["Alberta"].keys()), list(provinces["Alberta"].values()))
    # making the radio buttons
    some_graph.add_radio_buttons("white", ["Alberta", "British Columbia", "Saskatchewan", "Manitoba", "Ontario", "Quebec", "New Brunswick", 
    "Prince Edward Island", "Nova Scotia", "Newfoundland and Labrador", "Northern Canada"], "blue")
    fig, ax = some_graph.get_figure(), some_graph.get_radio_axis()
    radio = some_graph.get_radio_buttons()
    # changing the graph depending on the button clicked

    def update_button(province_name):
        ax.clear()
        if province_name == "Alberta":
            ax.bar(list(provinces["Alberta"].keys()), list(provinces["Alberta"].values()), color="blue")

        elif province_name == "British Columbia":
            ax.bar(list(provinces["British Columbia"].keys()), list(provinces["British Columbia"].values()), color="blue")

        elif province_name == "Saskatchewan":
            ax.bar(list(provinces["Saskatchewan"].keys()), list(provinces["Saskatchewan"].values()), color="blue")

        elif province_name == "Manitoba":
            ax.bar(list(provinces["Manitoba"].keys()), list(provinces["Manitoba"].values()), color="blue")

        elif province_name == "Ontario":
            ax.bar(list(provinces["Ontario"].keys()), list(provinces["Ontario"].values()), color="blue")

        elif province_name == "Quebec":
            ax.bar(list(provinces["Quebec"].keys()), list(provinces["Quebec"].values()), color="blue")

        elif province_name == "New Brunswick":
            ax.bar(list(provinces["New Brunswick"].keys()), list(provinces["New Brunswick"].values()), color="blue")

        elif province_name == "Prince Edward Island":
            ax.bar(list(provinces["Prince Edward Island"].keys()), list(provinces["Prince Edward Island"].values()), color="blue")

        elif province_name == "Nova Scotia":
            ax.bar(list(provinces["Nova Scotia"].keys()), list(provinces["Nova Scotia"].values()), color="blue")

        elif province_name == "Newfoundland and Labrador":
            ax.bar(list(provinces["Newfoundland and Labrador"].keys()), list(provinces["Newfoundland and Labrador"].values()), color="blue")

        elif province_name == "Northern Canada":
            ax.bar(list(provinces["Northern Canada"].keys()), list(provinces["Northern Canada"].values()), color="blue")
        
        # labelling and adjustments
        ax.tick_params(axis='x', labelsize=7)
        ax.set_title(title, fontsize=30)
        ax.set_xlabel(xname, fontsize=15)
        ax.set_ylabel(yname, fontsize=15)

        fig.canvas.draw_idle()
    
    radio.on_clicked(update_button)

    some_graph.draw_graph("Educational Attainment", "Education", "Number of People")