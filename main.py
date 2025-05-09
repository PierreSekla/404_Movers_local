from Databases import Database
from codes import Code

if __name__ == "__main__":
    All_Databses = Database()
    All_Codes = Code()
    # All_Databses.create_edu_empl()
    # 3: AGEGRP
    # 37: Gender
    # 10: CFSTAT
    # 25: DPGRSUM
    # numbers for demograhpic are 3, 37, 10 and 25 
    # 42: HDGREE
    # 12: CIP2021
    # 60: LFACT
    # 125: WRKACT
    # 86: NOC21
    # numbers for employment are 42, 12, 125, 86, 60

    with open("data_donnees_2021_ind_v2.csv", 'r') as file:
        file_data = file.readlines()
        header = file_data[0].split(",")
        print(f"{header[41]}, {header[11]}, {header[59]}, {header[124]}, {header[85]}")
        test_line = file_data[1].split(",")
        print(f"{test_line[41]}, {test_line[11]}, {test_line[59]}, {test_line[124]}, {test_line[85]}")
        # print(f"{All_Codes.get_HDGREE_code(int(test_line[59]))}")
        """
        for i in range(1, len(file_data)):
            file_line = file_data[i].split(",")
            All_Databses.add_to_edu_empl(file_line[41], file_line[11], file_line[59], test_line[124], test_line[84])

        """
        edu_empl_data = All_Databses.get_all_edu_empl()
        for i in range(len(edu_empl_data)):
            print(f"{i+1}. {edu_empl_data[i]}")
        