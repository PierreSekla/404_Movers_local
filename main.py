from Databases import Database

# Order of columns
# 1 Unique records identifier
# 2 Idengenous identity
# 3 Age
# 4 Age at immigration
# 5 School attendance
# 6 Membership at first nation band
# 7 Bedrooms
# 8 Total income of census family
# 9 After tax income of census family
# 10 Household living arrangements
# 11 Child benefits
# 12 Major field of study (CIP at 2021)
# 13 Major field of study, STEM and  BHASE (non-STEM) groupings - Summary (based on CIP Canada 2021)
# 14 Census Metropolitian area
# 15 Condonium Status
# 16 Emergency and Recovery benefits

if __name__ == "__main__":
    All_Databses = Database()
    # numbers for demograhpic are 3, 37, 10 and 25 
    with open("data_donnees_2021_ind_v2.csv", 'r') as file:
        file_data = file.readlines()
        
        """
        Header = file_data[0].split(",")
        for i in range(len(Header)):
            print(f"{i+1}. {Header[i]}")
        """