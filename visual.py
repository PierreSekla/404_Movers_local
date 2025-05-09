from Databases import Database
from codes import Code
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

class BarGraph:
    def __init__(self, x_axis, data):
        self.__x_axis = x_axis
        self.__data = data
        self.__radio = None
        self.__fig, self.__radio_axis = plt.subplots()

    
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
        # change the color
        plt.show()



if __name__ == "__main__":
    # basic variables
    title = "Educational Attainment"
    xname = "Education"
    yname = "Number of People"
    # all the different titles
    All_Codes = Code()
    # organizing data
    all_edu_empl_data = Database().get_all_edu_empl()
    grouping_empl_data = {}
    for i in range(len(all_edu_empl_data)):
        key = All_Codes.get_HDGREE_code(all_edu_empl_data[i][0])
        if key not in grouping_empl_data.keys():
            grouping_empl_data[key] = 1
        else:
            grouping_empl_data[key] += 1
    print(grouping_empl_data)
    print("")
    # making the bar graph
    some_graph = BarGraph(list(grouping_empl_data.keys()), list(grouping_empl_data.values()))
    # making the radio buttons
    some_graph.add_radio_buttons("white", ["Alberta", "British Columbia", "Saskatchewan", "Manitoba", "Ontario", "Quebec", "New Brunswick", 
    "Prince Edward Island", "Nova Scotia", "Nunavut", "Yukon", "Newfoundland and Labrador", "Northwest Territories"], "blue")
    fig, ax = some_graph.get_figure(), some_graph.get_radio_axis()
    radio = some_graph.get_radio_buttons()
    # changing the graph depending on the button clicked
    def update_button(province_name):
        ax.clear()
        if province_name == "Alberta":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "British Columbia":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "Saskatchewan":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "Manitoba":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "Ontario":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "Quebec":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "New Brunswick":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "Prince Edward Island":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "Nova Scotia":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "Nunavut":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "Yukon":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "Newfoundland and Labrador":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")

        elif province_name == "Northwest Territories":
            ax.bar(list(grouping_empl_data.keys()), list(grouping_empl_data.values()), color="blue")
        
        # labelling and adjustments
        ax.tick_params(axis='x', labelsize=7)
        ax.set_title(title, fontsize=30)
        ax.set_xlabel(xname, fontsize=15)
        ax.set_ylabel(yname, fontsize=15)

        fig.canvas.draw_idle()
    radio.on_clicked(update_button)

    some_graph.draw_graph("Educational Attainment", "Education", "Number of People")