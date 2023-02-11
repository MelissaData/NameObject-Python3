import mdName_pythoncode
import os
import sys
import json


class DataContainer:
    def __init__(self, name="", result_codes=[]):
        self.name = name
        self.result_codes = result_codes

class NameObject:
    """ Set license string and set path to data files  (.dat, etc) """
    def __init__(self, license, data_path):
        self.md_name_obj = mdName_pythoncode.mdName()
        self.md_name_obj.SetLicenseString(license)
        self.data_path = data_path
        self.md_name_obj.SetPathToNameFiles(data_path)

        """
        If you see a different date than expected, check your license string and either download the new data files or use the Melissa Updater program to update your data files.  
        """
        
        p_status = self.md_name_obj.InitializeDataFiles()
        if (p_status != mdName_pythoncode.ProgramStatus.NoError):
            print("Failed to Initialize Object.")
            print(p_status)
            return
        
        print(f"                DataBase Date: {self.md_name_obj.GetDatabaseDate()}")
        print(f"              Expiration Date: {self.md_name_obj.GetLicenseExpirationDate()}")
      
        """
        This number should match with file properties of the Melissa Object binary file.
        If TEST appears with the build number, there may be a license key issue.
        """
        print(f"               Object Version: {self.md_name_obj.GetBuildNumber()}\n")
    

    def execute_object_and_result_codes(self, data):
        self.md_name_obj.ClearProperties()

        self.md_name_obj.SetFullName(data.name)
        self.md_name_obj.Parse()
        self.md_name_obj.Genderize()
        self.md_name_obj.Salutate()
        result_codes = self.md_name_obj.GetResults()

        """ 
        ResultsCodes explain any issues Name Object has with the object.
        List of result codes for Name Object
        https://wiki.melissadata.com/?title=Result_Code_Details#Name_Object
        """

        return DataContainer(data.name, result_codes)


def parse_arguments():
    license, test_name, data_path = "", "", ""

    args = sys.argv
    index = 0
    for arg in args:
        
        if (arg == "--license") or (arg == "-l"):
            if (args[index+1] != None):
                license = args[index+1]
        if (arg == "--name") or (arg == "-p"):
            if (args[index+1] != None):
                test_name = args[index+1]
        if (arg == "--dataPath") or (arg == "-d"):
            if (args[index+1] != None):
                data_path = args[index+1]
        index += 1

    return (license, test_name, data_path)

def run_as_console(license, test_name, data_path):
    print("\n\n=========== WELCOME TO MELISSA NAME OBJECT WINDOWS PYTHON3 ============\n")

    name_object = NameObject(license, data_path)

    should_continue_running = True

    if name_object.md_name_obj.GetInitializeErrorString() != "No Error":
      should_continue_running = False
      
    while should_continue_running:
        if test_name == None or test_name == "":        
          print("\nFill in each value to see the Name Object results")
          name = str(input("Name: "))
        else:        
          name = test_name
        
        data = DataContainer(name)

        """ Print user input """
        print("\n=============================== INPUTS ================================\n")
        print(f"\t               Name: {name}")

        """ Execute Name Object """
        data_container = name_object.execute_object_and_result_codes(data)

        """ Print output """
        print("\n=============================== OUTPUT ================================\n")
        print("\n\tName Object Information:")

        print(f"\t      Prefix: {name_object.md_name_obj.GetPrefix()}")
        print(f"\t  First Name: {name_object.md_name_obj.GetFirstName()}")
        print(f"\t Middle Name: {name_object.md_name_obj.GetMiddleName()}")
        print(f"\t   Last Name: {name_object.md_name_obj.GetLastName()}")
        print(f"\t      Suffix: {name_object.md_name_obj.GetSuffix()}")
        print(f"\t      Gender: {name_object.md_name_obj.GetGender()}")
        print(f"\t  Salutation: {name_object.md_name_obj.GetSalutation()}")
        print(f"\tResult Codes: {data_container.result_codes}")

        rs = data_container.result_codes.split(',')
        for r in rs:
            print(f"        {r}: {name_object.md_name_obj.GetResultCodeDescription(r, mdName_pythoncode.ResultCdDescOpt.ResultCodeDescriptionLong)}")


        is_valid = False
        if not (test_name == None or test_name == ""):
            is_valid = True
            should_continue_running = False    
        while not is_valid:
        
            test_another_response = input(str("\nTest another name? (Y/N)\n"))
            

            if not (test_another_response == None or test_another_response == ""):         
                test_another_response = test_another_response.lower()
            if test_another_response == "y":
                is_valid = True
            
            elif test_another_response == "n":
                is_valid = True
                should_continue_running = False            
            else:
            
              print("Invalid Response, please respond 'Y' or 'N'")

    print("\n=============== THANK YOU FOR USING MELISSA PYTHON OBJECT =============\n")
    


"""  MAIN STARTS HERE   """

license, test_name, data_path = parse_arguments()

run_as_console(license, test_name, data_path)