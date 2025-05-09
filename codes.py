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
            5 : "PO3TLT1Y",
            6 : "PO1T2Y",
            7 : "POMT2Y",
            8 : "UCOD",
            9 : "BD",
            10 : "UCOD",
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