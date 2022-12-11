import os
import getpass
import testSystem 

'''
- Each data file should be placed in one of a set of subdirs based on the date in the first line of the file
- The year, month, and day should all be subfolders within fileToSort
- At each level, we need to check whether a new folder needs to be created or not
- use `testSystem` module to get the current system 
- use `getpass` to get the users name 
'''

def main():
    username = getpass.getuser()
    _, user_path = testSystem.switch_system()
    current_directory = os.path.join(user_path, username)
    os.chdir(current_directory)
    file_path = "Python_Data"
    cwd = os.path.join(current_directory, file_path)
    
    files_dir = os.path.join(cwd, "filesToSort")
    
    for filename in os.listdir(files_dir):     # Loop through every file in filesToSort
        if filename.endswith(".txt"):          # if the file ends in .txt, we ignore it
            continue

        file = os.path.join(files_dir, filename)
        log = open(file, "r").read()
        date = log[:11].strip() # [start:end]
        year = date[:4]
        month = date[5:7]
        day = date[8:]
        
        current_path_with_year = os.path.join(files_dir, year)    # Adds year to file dir
        
        try:
            os.chdir(current_path_with_year)
        except:
            os.mkdir(current_path_with_year)
            os.chdir(current_path_with_year)
        
        current_path_with_month = os.path.join(current_path_with_year, month) # Adds year to file dir
        
        try:
            os.chdir(current_path_with_month) 
        except:
            os.mkdir(current_path_with_month)
            os.chdir(current_path_with_month)
        
        current_path_with_day = os.path.join(current_path_with_month, day)
        new_file_path = os.path.join(current_path_with_day, filename)
        
        try:
            os.chdir(current_path_with_day)
            os.rename(file, new_file_path)
        except:
            os.mkdir(current_path_with_day)
            os.chdir(current_path_with_day)
            os.rename(file, new_file_path)    
            
    
    
if __name__ == '__main__':
    main()