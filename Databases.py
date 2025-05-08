import sqlite3

class Database:
    def __init__(self):
        self.__Database_Demo = "Demography_Data.db"
        self.__Database_Edu_Empl = "Edu_Empl.db"
        self.__Database_Inc_Econ = "Inc_Econ.db"
        self.__Database_Hou_Livi = "Hou_Livi.db"
        self.__Database_Mig_Mobi = "Mig_Mobi.db"
        self.__Database_Lan_Cultural = "Lan_Cultural.db"
    
    def create_databases(self):
        try:
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
            # Education/Employment
            cursor, connection = self.open_database(self.__Database_Edu_Empl)
            cursor.execute("""
                CREATE TABLE EducationEmploymentData(
                    EducationalAtttainment text,
                    FieldOfStudy text,
                    EmploymentStatus text
                )
            """)
            self.close_database(connection)
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
            # Languages/Cultural
            cursor, connection = self.open_database(self.__Database_Lan_Cultural)
            cursor.execute("""
                CREATE TABLE LanguageCulturalData(
                    LanguagesSpoken text,
                    ReligiousPractices text
                )
            """)
            self.close_database(connection)
        except:
            print("All 6 Databases have already been made")
    
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
    
    def add_to_edu_empl(self, EducationalAtttainment, FieldOfStudy, EmploymentStatus):
        """
        purpose: adds to the Demography Database
        parameter: 
        return: 
        """
        cursor, connection = self.open_database(self.__Database_Edu_Empl)
        cursor.execute("""
        INSERT INTO EducationEmploymentData
        VALUES (?, ?, ?)
        """, [EducationalAtttainment, FieldOfStudy, EmploymentStatus])
        self.close_database(connection)
        print("Added to Education/Employment Data")
    
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
        cursor, connection = self.open_database(self.__Database_Hou_Livi)
        cursor.execute("""
        INSERT INTO LanguageCulturalData
        VALUES (?, ?)
        """, [LanguagesSpoken, ReligiousPractices])
        self.close_database(connection)
        print("Added to Languages and Cultural Data")
    