#This code will combine all the Excel files that were extracted from the MAUDE database
#install pandas: Setting>Project RZ_MIS581>Python Interpreter>click the +>search for pandas and install
import pandas as pd   #After installing the pandas library, we need to import it to this python project.  common practice is to name it "pd"
import os   #Need to import the os library
input_location = "C:/Users/rubi_/OneDrive/Desktop/Ricardo/MIS581-1/MAUDE_Data/MAUDE_Extract" #variable of where the extracts are located
output_location = "C:/Users/rubi_/OneDrive/Desktop/Ricardo/MIS581-1/MAUDE_Data/MAUDE_Final" #variable of where the final excel file will load
#When copying file paths to folders change the backslash "\" to a forward slash "/"
file_list = os.listdir(input_location) #variable for list of input file
#Creation of for loop to read each of the excel files
MAUDE_CombinedDf = pd.DataFrame()
for files in file_list:  #direct where the for loop to should point to
    if files.endswith(".xlsx"):   #instead of naming each file one by one, use a shortcut and search for ".xlsx"
        df = pd.read_excel(input_location+files)   #location of where to read the files
        MAUDE_CombinedDf = MAUDE_CombinedDf.append(df)
MAUDE_CombinedDf.to_excel(output_location+"MAUDE_CombinedDf.xlsl") #Loads the combined excel file into the output location
