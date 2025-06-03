from codes import Code

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

def organize_by_subject(All_Codes, provinces, choosen_province, subject_choosen):
    """
    purpose: organize the data in each province by subject
    parameter All_codes: object
    parameter provinces: dictionary data of all provinces and subjects
    parameter choosen_province: string
    parameter: subject_choosen: string
    returns: dictionary of strings
    """
    province_and_subject_data = {}
    if choosen_province != "Country Wide":
        if subject_choosen not in provinces[choosen_province].keys():
            province_and_subject_data[choosen_province] = 0
        else: 
            province_and_subject_data[choosen_province] = provinces[choosen_province][subject_choosen]
    else:
        country_data = get_country_data(provinces, All_Codes.get_HDGREE_values())
        province_and_subject_data[choosen_province] = country_data[subject_choosen]

    return province_and_subject_data

def get_country_data(provinces, subject_codes):
    """
    purpose: organizes for it to be country-wide
    parameter provinces: dictionary of strings containing the information of each province
    parameter subject_codes: dictionary of all the different possible subjects and education
    returns: dictionary (of country data)
    """
    country_data = {}
    for subject in subject_codes:
        country_data[subject] = 0
    for province in provinces.keys():
        for education in provinces[province].keys():
            country_data[education] += provinces[province][education]
    return country_data
