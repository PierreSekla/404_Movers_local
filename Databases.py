import sqlite3

class Database:
    def __init__(self):
        self.__Database_Demo = "Demography_Data.db"
        self.__Database_Edu_Empl = "Edu_Empl.db"
        self.__Database_Inc_Econ = "Inc_Econ.db"
        self.__Database_Hou_Livi = "Hou_Livi.db"
        self.__Database_Mig_Mobi = "Mig_Mobi.db"
        self.__Database_Lan_Cultural = "Lan_Cultural.db"
    
    def create_demo(self):
            """
            purpose:
            parameter:
            returns:
            """
            #Demography
            cursor, connection = self.open_database(self.__Database_Demo)
            cursor.execute("""
                CREATE TABLE DemographyData(
                    Population integer,
                    Age text,
                    Gender text,
                    Household_Composition text
                )
            """)
            self.close_database(connection)
    
    def create_edu_empl(self):
            """
            purpose:
            parameter:
            returns:
            """
            # Education/Employment
            cursor, connection = self.open_database(self.__Database_Edu_Empl)
            cursor.execute("""
                CREATE TABLE EducationEmploymentData(
                    EducationalAtttainment text,
                    FieldOfStudy text,
                    EmploymentStatus text,
                    WorkActivity text,
                    Occupation text,
                    Residence text
                )
            """)
            self.close_database(connection)
    
    def create_inc_econ(self):
            """
            purpose:
            parameter:
            returns:
            """
            # Income/Economic
            cursor, connection = self.open_database(self.__Database_Inc_Econ)
            cursor.execute("""
                CREATE TABLE IncomeEconomicData(
                    IncomeLevel text,
                    PovertyRate text,
                    GovernmentAsistance text
                )
            """)
            self.close_database(connection)
    
    def create_hou_livi(self):
            """
            purpose:
            parameter:
            returns:
            """
            # Housing/Living
            cursor, connection = self.open_database(self.__Database_Hou_Livi)
            cursor.execute("""
                CREATE TABLE HousingLivingData(
                    OwnershipRent text,
                    HousingConditions text,
                    ShelterCosts text
                )
            """)
            self.close_database(connection)
    
    def create_mig_mobi(self):
            """
            purpose:
            parameter:
            returns:
            """
            # Migration and Mobility
            cursor, connection = self.open_database(self.__Database_Mig_Mobi)
            cursor.execute("""
                CREATE TABLE MigrationMobilityData(
                    PlaceOfBirth text,
                    RecentImmigrants text,
                    InternalMobility text
                )
            """)
            self.close_database(connection)
    
    def create_lan_cultural(self):
            """
            purpose:
            parameter:
            returns:
            """
            # Languages/Cultural
            cursor, connection = self.open_database(self.__Database_Lan_Cultural)
            cursor.execute("""
                CREATE TABLE LanguageCulturalData(
                    LanguagesSpoken text,
                    ReligiousPractices text
                )
            """)
            self.close_database(connection)
    
    def open_database(self, database_name):
        """
        purpose: opens a database if it exists
        parameter database: string
        return: object, object
        """
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        return cursor, connection
    
    def close_database(self, connection):
        """
        purpose: closes the database afterwards
        parameter connection: object
        return: None
        """
        connection.commit()
        connection.close()
    
    def add_to_demo(self, Population, Age, Gender, HouseholdComposition):
        """
        purpose: adds to the Demography Database
        parameter: 
        return: 
        """
        cursor, connection = self.open_database(self.__Database_Demo)
        cursor.execute("""
        INSERT INTO DemographyData
        VALUES (?, ?, ?, ?)
        """, [Population, Age, Gender, HouseholdComposition])
        self.close_database(connection)
        print("Added to Demography Data")
    
    def add_to_edu_empl(self, EducationalAtttainment, FieldOfStudy, EmploymentStatus, WorkActivity, Occupation, Residence):
        """
        purpose: adds to the Demography Database
        parameter: 
        return: 
        """
        cursor, connection = self.open_database(self.__Database_Edu_Empl)
        cursor.execute("""
        INSERT INTO EducationEmploymentData
        VALUES (?, ?, ?, ?, ?, ?)
        """, [EducationalAtttainment, FieldOfStudy, EmploymentStatus, WorkActivity, Occupation, Residence])
        self.close_database(connection)
        #print(f"Added {[EducationalAtttainment, FieldOfStudy, EmploymentStatus, WorkActivity, Occupation, Residence]}to Education/Employment Data")
    
    def add_to_inc_econ(self, IncomeLevel, PovertyRate, GovernmentAsistance):
        """
        purpose: adds to the Demography Database
        parameter: 
        return: 
        """
        cursor, connection = self.open_database(self.__Database_Inc_Econ)
        cursor.execute("""
        INSERT INTO IncomeEconomicData
        VALUES (?, ?, ?)
        """, [IncomeLevel, PovertyRate, GovernmentAsistance])
        self.close_database(connection)
        print("Added to Income Economic Data")
    
    def add_to_hou_livi(self, OwnershipRent, HousingConditions, ShelterCosts):
        """
        purpose: adds to the Demography Database
        parameter: 
        return: 
        """
        cursor, connection = self.open_database(self.__Database_Hou_Livi)
        cursor.execute("""
        INSERT INTO HousingLivingData
        VALUES (?, ?, ?)
        """, [OwnershipRent, HousingConditions, ShelterCosts])
        self.close_database(connection)
        print("Added to Housing and Living Data")

    def add_to_mig_mobi(self, PlaceOfBirth, RecentImmigrants, InternalMobility):
        """
        purpose: adds to the Demography Database
        parameter: 
        return: 
        """
        cursor, connection = self.open_database(self.__Database_Hou_Livi)
        cursor.execute("""
        INSERT INTO MigrationMobilityData
        VALUES (?, ?, ?)
        """, [PlaceOfBirth, RecentImmigrants, InternalMobility])
        self.close_database(connection)
        print("Added to Migration and Mobility Data")
    
    def add_to_lan_cultural(self, LanguagesSpoken, ReligiousPractices):
        """
        purpose: adds to the Demography Database
        parameter: 
        return: 
        """
        cursor, connection = self.open_database(self.__Database_Lan_Cultural)
        cursor.execute("""
        INSERT INTO LanguageCulturalData
        VALUES (?, ?)
        """, [LanguagesSpoken, ReligiousPractices])
        self.close_database(connection)
        print("Added to Languages and Cultural Data")

    def delete_all_demo_data(self):
        """
        purpose: deletes all demo data (for testing purposes)
        parameter: TBD
        returns: None
        """
        cursor, connection = self.open_database(self.__Database_Demo)
        cursor.execute("""
            DELETE FROM DemographyData
        """)
        self.close_database(connection)
        print("Everything has been deleted from the Demography database")
    
    def delete_all_edu_empl_data(self):
        """
        purpose: deletes all the data in the employment database
        parameter: None
        return: None
        """
        cursor, connection = self.open_database(self.__Database_Edu_Empl)
        cursor.execute("""
            DELETE FROM EducationEmploymentData
        """)
        self.close_database(connection)
        print("Everything has been deleted from the Education Employment database")
    
    def get_all_demo_data(self):
        """
        purpose: geta all the data from the database
        return: list of tuples
        """
        cursor, connection = self.open_database(self.__Database_Demo)
        demography_data = cursor.execute("""
            SELECT * FROM DemographyData
        """).fetchall()
        self.close_database(connection)
        return demography_data

    def get_all_edu_empl(self):
        """
        purpose:
        parameter:
        return:
        """
        cursor, connection = self.open_database(self.__Database_Edu_Empl)
        edu_empl_data = cursor.execute("""
            SELECT * FROM EducationEmploymentData
        """).fetchall()
        self.close_database(connection)
        return edu_empl_data