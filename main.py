from Databases import Database
from codes import Code
from time import sleep

if __name__ == "__main__":
    All_Databases = Database()
    All_Codes = Code()
    #All_Databases.create_edu_empl()
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
    # 109: PWPR
    # numbers for employment are 42, 12, 60, 125, 86 and 109
    # reads the CSV PUMF file and copies only the necessary information to the database
    with open("data_donnees_2021_ind_v2.csv", 'r') as file:
        file_data = file.readlines()
        for i in range(1, len(file_data)):
            file_line = file_data[i].split(",")
            All_Databases.add_to_edu_empl(file_line[41], file_line[11], file_line[59], file_line[124], file_line[85], file_line[108])
        
        print("Process Finished")
        
        
    
        