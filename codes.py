"""
Code Description Unweighted Weighted Includes
 1 No certificate, diploma or degree
 2 High (secondary) school diploma or
equivalency certificate
 3 Non-apprenticeship trades certificate or diploma
 4 Apprenticeship certificate 
 5 Program of 3 months to less than 1 year (College, CEGEP and other nonuniversity certificates or diplomas)
 6 Program of 1 to 2 years (College, CEGEP and other non-university certificates or diplomas)
 7 Program of more than 2 years
(College, CEGEP and other nonuniversity certificates or diplomas)
 8 University certificate or diploma
below bachelor level
 9 Bachelor's degree 
 10 University certificate or diploma
above bachelor level
 11 Degree in medicine, dentistry,
veterinary medicine or optometry
 12 Master's degree 
 13 Earned doctorate 
 88 Not available 
 99 Not applicable Persons less than 15 years of age

"""


class Code:
    def __init__(self):
        self.__HDGREE_codes = {
            1 : "NC",
            2 : "HSDO",
            3 : "NATC",
            4 : "AC",
            5 : "PO3",
            6 : "PO1",
            7 : "POM",
            8 : "UBCOD",
            9 : "BD",
            10 : "UACOD",
            11 : "DIMD",
            12 : "MD",
            13 : "ED",
            88 : "NAV",
            99 : "NAP"
        }

        self.__HDGREE_Full = {
            1 : "No certificate",
            2 : "High (secondary) school diploma or equivalency certificate",
            3 : "Non-apprenticeship trades certificate or diploma",
            4 : "Apprenticeship Certificate",
            5 : "Program of 3 months to less than 1 year",
            6 : "Program of 1 to 2 years",
            7 : "Program of more than 2 years",
            8 : "University certificate or diploma below bachelor level",
            9 : "Bachelor's Degree",
            10 : "University certificate or diploma above bachelor level",
            11 : "Degree in medicine, dentistry, veterinary medicine or optometry",
            12 : "Master's degree",
            13 : "Earned doctorate",
            88 : "Not available",
            99 : "Not applicable"
        }

        self.__LOC_ST_RES_codes = {
            10: "Newfoundland and Labrador",
            11: "Prince Edward Island",
            12: "Nova Scotia",
            13: "New Brunswick",
            24: "Quebec",
            35: "Ontario",
            46: "Manitoba",
            47: "Saskatchewan",
            48: "Alberta",
            59: "British Columbia",
            70: "Northern Canada",
            88: "Not available",
            99: "Not applicable"
        }

        self.__HDGREE_Full_to_Short = {
            "No certificate": "NC",
            "High (secondary) school diploma or equivalency certificate": "HSDO",
            "Non-apprenticeship trades certificate or diploma": "NATC",
            "Apprenticeship Certificate": "AC",
            "Program of 3 months to less than 1 year": "PO3",
            "Program of 1 to 2 years": "PO1",
            "Program of more than 2 years": "POM",
            "University certificate or diploma below bachelor level": "UBCOD",
            "Bachelor's Degree": "BD",
            "University certificate or diploma above bachelor level": "UACOD",
            "Degree in medicine, dentistry, veterinary medicine or optometry": "DIMD",
            "Master's degree": "MD",
            "Earned doctorate": "ED",
            "Not available": "NAV",
            "Not applicable": "NAP"
        }
    
    def get_HDGREE_code(self, code_num):
        """
        purpose: returns the code value
        parameter code_num: integer
        returns: string
        """
        return self.__HDGREE_codes[int(code_num)]

    def get_HDGREE_values(self):
        """
        purpose: returns all the possible code values for HDGREE variable
        parameter: None
        return: list of strings
        """
        return self.__HDGREE_codes.values()

    def get_HDGREE_full_names(self):
        """
        purpose: returns all the names of each subject in Education Attainment in full strings
        parameter: None
        return: list of strings
        """
        return list(self.__HDGREE_Full.values())

    def get_HDGREE_full_to_short(self, full_name):
        """
        purpose: converts the full name to the short name abrevasion
        parameter full_name: string
        return: string
        """
        return self.__HDGREE_Full_to_Short[full_name]

    def get_LOC_ST_RES_code(self, code_num):
        """
        purpose: returns the code value for the province name
        parameter code_num: int
        return: string * province name
        """
        return self.__LOC_ST_RES_codes[int(code_num)]
    
    def get_LOC_ST_RES_values(self):
        """
        purpose: returns the values in the Province name dictionary
        parameter: none
        return: dictionary set of strings
        """
        return self.__LOC_ST_RES_codes.values()