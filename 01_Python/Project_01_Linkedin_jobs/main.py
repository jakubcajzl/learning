# ================================= #
### Project 01: **LinkedIn Jobs** ###
# ================================= #

# Kaggle dataset of scraped LinkedIn jobs #
# https://www.kaggle.com/datasets/arshkon/linkedin-job-postings/ #


# ======================================================================== #
# Importing main libraries:
import os
import datetime
import logging
from logging.handlers import QueueHandler, QueueListener
from queue import Queue
import yaml
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
    
import pandas as pd
import numpy as np

# Statistics libraries:
import scipy as stats

# Plotting libraries:
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Setting-up the display options for Pandas dataframes to display 100 columns and rows (not truncated):
pd.options.display.max_columns = 1000
pd.options.display.max_rows = 1000
# ======================================================================== #

# Changing the current work directory (cwd):
work_directory = 'C:/Users/Jakub.Cajzl/OneDrive - Adastra, s.r.o/Work/Projects/00_Learning/learning/01_Python/Project_01_Linkedin_jobs/'
os.chdir(work_directory)


# ======================================================================== #

# Importing configuration settings from a YAML file:
if __name__ == '__main__':
    
    configuration_file = "configuration.yaml"
    
    with open(configuration_file, 'r', encoding='utf-8') as stream:
        configuration = yaml.load(stream, Loader)

    # Printing out the values in configuration:
    # for key, value in dictionary.items():
    #     print (key + ": " + str(value))


# Starting a LOGGER:
logger = logging.getLogger(__name__)

# Setting-up a LOGGER:
try:
    logging.basicConfig(
        filename = configuration['logger']['file'],
        encoding = configuration['logger']['encoding'],
        level = logging.DEBUG,
        #level = configuration['logger']['level'],
        format = configuration['logger']['format'],
        )
except Exception as error:
    logger.error(f'Error: {error}')
    logger.warning(f'Logger configuration was not loaded from a file {logger_filename}')


# Deleting log file rows if the log file is too large (> 'max_rows'):
def clear_log(file_path, max_rows):
    """
    The function deletes log file rows if the log file is too large (> 'max_rows').
    
    Parameters:
    - file_path (string): path of the log file
    - max_rows (str): maximum number of rows that the log file should have
    """
    
    # Read the content of the file:
    with open(file_path, 'r', encoding='utf8') as file:
        lines = file.readlines()
    
    # If the log file has more lines than specified 'max_rows', then delete one or more runs:
    while len(lines) > max_rows:
        # If the occurence of the 'New run of the program' is in the log, delete this run:
        for index, line in enumerate(lines[1:]): # Excluding a first row from search, because I want the log to start with a "New run of the program" line.
            if "New run of the program" in line:
                lines = lines[(index+1):]
                break

    with open(file_path, 'w') as file:
        file.writelines(lines)


# Calling the function to delete lines from the log file if larger than 1000:
max_log_lines = 1000
clear_log(configuration['logger']['file'], max_log_lines)


# First logger info message:
logger.info('\n\n============= New run of the program =============\n')

# Examples of different logger levels:
# INFO: logger.info('Info')
# DEBUG: logger.debug('Debugging info')
# WARNING: logger.warning('Warning')
# ERROR: logger.error('Error')

# ======================================================================== #



### FUNCTIONS ###

# =================================================================================================================== #
def get_dataframe_name(dataframe: pd.DataFrame) -> str:
    """
    The function returns a name of the DataFrame variable as a string.
    
    Parameters: 
    - dataframe (pd.DataFrame): DataFrame variable
    
    Returns: 
    - str: name of the DataFrame variable as a string
    """
    
    for obj_name, obj in globals().items():
        if obj is dataframe and isinstance(obj, pd.DataFrame):
            return obj_name
# =================================================================================================================== #


# =================================================================================================================== #
def csv_load(file: str, delimiter: str) -> pd.DataFrame:
    """
    The function loads the files in the CSV format (with specified delimiter) into Pandas dataframe.
    
    Parameters:
    - file (string): the whole path of the CSV file (including a file name with file extension), e.g.: '../dataset/job_postings.csv'
    - delimiter (str): the delimiter used in the CSV, e.g.: comma, semicolon, etc.
    
    Return:
    - pd.Dataframe: the dataframe that holds the data from the CSV file
    """
    
    try:
        print(f'Loading the {file} file using a delimiter: {delimiter}')
        pd.read_csv(file, delimiter=delimiter)
        print(f'File was succesfully loaded into the dataframe using a delimiter: {delimiter}\n')
        logger.info(f'File {file} succesfully loaded into the dataframe using a delimiter: {delimiter}')
    except Exception as error:
        print(f'Error: {error}')
        print('File was not loaded into the dataframe!\n')
        logger.error(f'Error: {error}')
        logger.warning(f'File {file} was not loaded into the dataframe using a delimiter: {delimiter}')
    else:
        return pd.read_csv(file, delimiter=delimiter)
# =================================================================================================================== #


# =================================================================================================================== #
def basic_info(dataframe: pd.DataFrame):
    """"
    The function displays an info about the dataset - both as a print and log.
    
    Parameters:
    - dataframe (pd.DataFrame): dataframe for which we want to have a basic info
    """
    
    dataframe_name = get_dataframe_name(dataframe)
    duplicates = dataframe[dataframe.iloc[:, 0].duplicated()].shape[0]
    print(f'=={dataframe_name}== is object of type: | {type(dataframe)}')
    print(f'Number of rows:         | {dataframe.shape[0]}')
    print(f'Number of columns:      | {dataframe.shape[1]}')
    print(f'Number of duplicated rows of {dataframe.columns[0]} column:      | {duplicates}\n')
    
    logger.info('\n'
                f'\t=={dataframe_name}== is object of type: \t| {type(dataframe)}\n'
                f'\tNumber of rows: \t\t\t\t\t| {dataframe.shape[0]}\n'
                f'\tNumber of columns: \t\t\t\t\t| {dataframe.shape[1]}\n'
                f'\tColumns names: | {dataframe.columns}'
                '\n'
                )
# =================================================================================================================== #   


# =================================================================================================================== #
def print_data_types(dataframe: pd.DataFrame):
    """
    The function displays column data types of the given dataframe.
    
    Parameters:
    - dataframe (pd.DataFrame): the dataframe for which we want to know column data types
    """
    
    for column in dataframe.columns:
        print(f'{column: <28} | {dataframe[column].dtype}')
# =================================================================================================================== #


# =================================================================================================================== #
def column_unique_values(dataframe: pd.DataFrame, column: str):
    """
    The function displays unique values of the specified column.
    
    Parameters:
    - dataframe (pd.DataFrame): the dataframe for which we want to know column unique values
    - column (str): the dataframe column name
    """
    
    # Column name:
    print(f'Column name: {column}')
    
    # Getting the unique values in the column, sorted ascending:
    if dataframe[column].dtype != 'O':
        unique_values = np.sort(dataframe[column].unique()) # If dataframe is not string, then do also the sort() function. 
        print('Number of unique values:', len(unique_values))
        
        # Setting numpy print formatter to display numbers as floats, not scientific:
        float_formatter = '{:.1f}'.format
        np.set_printoptions(formatter={'float_kind': float_formatter})
        #np.set_printoptions(formatter=None)  # Undo the changes to formatter, if necessary
    
        print('Min:', min(unique_values))
        print('Max:', max(unique_values))
        print('Values:', unique_values)
    else:
        unique_values = dataframe[column].unique()
        print('Number of unique values:', len(unique_values))
        print('Values:', unique_values[0:10])
    
    # If the dataframe type doesn't support min() and max(), don't count min and max values:
    #try:
    #    print('Min:', min(unique_values))
    #    print('Max:', max(unique_values))
    #except:
    #    pass
# =================================================================================================================== #


# =================================================================================================================== #
def compare(dataframe: pd.DataFrame, column_name_1: str, column_name_2: str) -> pd.DataFrame:
    """
    The function compares two columns of a given dataframe to return a comparison dataframe.
    
    Parameters:
    - dataframe (pd.DataFrame): the dataframe for which we want to know column unique values
    - column_name_1 (str): the first dataframe column to compare
    - column_name_2 (str): the second dataframe column to compare
    
    Return:
    - pd.DataFrame: the comparison dataframe that has both columns
    """
    return dataframe[column_name_1].compare(dataframe[column_name_2], result_names=(column_name_1, column_name_2))
# =================================================================================================================== #


# =================================================================================================================== #
def columns_rename(dataframe: pd.DataFrame, columns_names: dict):
    """
    The function renames columns in the specified dataframe.
    
    Parameters:
    - dataframe (pd.DataFrame): the dataframe for which we want to rename the columns
    - columns_names (dict): the columns to rename
    """
    
    dataframe_name = get_dataframe_name(dataframe)
    
    print(f'Renaming columns in dataframe {dataframe_name}:\n')
    logger.info(f'Renaming columns in dataframe =={dataframe_name}==')
    
    for column_name_original, column_name_new in columns_names.items():
        dataframe.rename(columns={column_name_original:column_name_new}, inplace = True)
    
    print(f"Renamed columns are ('old_name', 'new_name'): \n\t{columns_names.items()}\n")
    logger.info(
                f"Renamed columns are ('old_name', 'new_name'): \n\t{columns_names.items()}"
                )
# =================================================================================================================== #


# =================================================================================================================== #
def columns_rename_prefix(dataframe: pd.DataFrame, prefix: str):
    """
    The function puts a given prefix in front of all the column names in the specified dataframe.
    Info: The function will not add a prefix if there is already a prefix in the column. 
    
    Parameters:
    - dataframe (pd.DataFrame): the dataframe for which we want to add a prefix
    - prefix (str): prefix string
    """
    
    dataframe_name = get_dataframe_name(dataframe)
    
    print(f'Renaming columns in dataframe =={dataframe_name}== by adding a prefix "{prefix}":\n')
    logger.info(f'Renaming columns in dataframe =={dataframe_name}== by adding a prefix "{prefix}"')
    
    for column in dataframe.columns:
        if prefix not in column:
            dataframe.rename(columns={column: f'{prefix}{column}'}, inplace = True)
        else:
            continue
        
    print(f'Renamed columns are: \n\t{dataframe.columns}\n')
    logger.info(
                f'Renamed columns are: \n\t{dataframe.columns}'
                )
# =================================================================================================================== #


# =================================================================================================================== #
def columns_drop(dataframe: pd.DataFrame, columns_list: list):
    """
    The function deletes/drops columns in the specified dataframe. 
    
    Parameters:
    - dataframe (pd.DataFrame): the dataframe for which we want to delete/drop column(s)
    - columns_list (list): a list of columns to drop from a dataframe
    """
    
    dataframe_name = get_dataframe_name(dataframe)
    
    print(f'Deleting columns in dataframe {dataframe_name}:')
    logger.info(f'Deleting columns in dataframe =={dataframe_name}==')
    
    for column in columns_list:
        print(f'Deleted column: {column}')
        logger.info(f'Deleted column: {column}')
        
        dataframe.drop(column, axis='columns', inplace=True)
        
    print('Deleting of columns finished succesfully!\n')
    logger.info('Deleting of columns finished succesfully!')
# =================================================================================================================== #



# == Main code ====================================================================================================== #

def main():
    """
    The function executes the main code of this file.
    """

    global configuration  # global variable of configuration from configuration.yaml
    
    # ===== Importing CSV files ====== #
    
    # Reading the CSV file into a Pandas DataFrames from configuration YAML file:
    for filename, file in configuration['files'].items():
        globals()[filename] = csv_load(file, configuration['delimiter_import'])
        # locals() needs to be here in order that Python saves the data in the local variables


    # ====== Basic info about data ====== #
    
    # Displaying first 5 rows of loaded files:
    for filename in configuration['files']:
        filename = globals()[filename]
        basic_info(filename)


    # ===== Merging all the tables ====== #

    # Deleting columns before merge:
    
    # jobs #
    columns_drop(jobs, ['work_type'])


    # Renaming columns before merge:
    
    # jobs #
    columns_names={'formatted_work_type':'work_type', 'formatted_experience_level':'experience_level','expiry':'expiry_time'}
    columns_rename(jobs, columns_names)
    
    # companies #
    # Renaming the columns in companies with prefix 'company_':
    columns_rename_prefix(companies, 'company_')


    ### Merging skills tables ###
    
    print('Merging skills tables.')
    logger.info('Merging skills tables')
    
    # Merging the tables of skills:
    globals()['skills'] = pd.merge(job_skills, skills_map, on='skill_abr', how='left', suffixes=('_#jobs', '_#skills_map'))
    
    # Renaming the columns in skills table:
    skills.rename(columns={
        'skill_abr': 'skills_abbr', 
        'skill_name': 'skills',
        }, inplace = True)
    
    print('Merging of skills tables finished succesfully!\n')
    logger.info('Merging of skills tables finished succesfully!')


    ### Dealing with the duplicates ###

    # Loading names of dataframes to check from 'configuration.yaml' file:
    globals()['dataframes_to_check'] = configuration['dataframes_to_check']
    
    # dataframes_to_check = {
    #     'jobs':'job_id', 
    #     'companies': 'company_id',
    #     'salaries': 'job_id',
    #     'industries':'company_id',
    #     'employee_counts': 'company_id',
    #     'skills': 'job_id'
    #     }

    # Iterating through different keys and values in dictionary:
    for key, value in dataframes_to_check.items():
        column = value  # Column name
        dataframe = globals()[key]  # Accessing dataframe by its name in globals()

        duplicates = dataframe[dataframe[column].duplicated()].shape[0]
        
        # Displaying and removing the duplicates:
        print('Removing duplicates:\n')
        
        if duplicates == 0:
            print(f'Column {column} from =={key}== table has {duplicates} duplicates.\n')
            logger.info(f'Column {column} from =={key}== table has {duplicates} duplicates.')
        else:
            duplicates_top_5 = dataframe.loc[dataframe.duplicated(subset=[column], keep=False) == True].sort_values(by=column, ascending=True)[0:5]
            
            print(f'Column {column} from =={key}== table has {duplicates} duplicates:')
            print('Duplicates (top 5 rows):')
            print(duplicates_top_5)
            logger.info(f'Column {column} from =={key}== table has {duplicates} duplicates:\n'
                    'Duplicates (top 5 rows):'
                    f'\n{duplicates_top_5}'
                    )

            print(f'Removing the duplicates in =={key}== by grouping the records...')
            logger.info(f'Removing the duplicates in =={key}== by grouping the records...')
                
            groupby_column = column

            # # Grouping with the result in the list:
            dataframe = dataframe.groupby(groupby_column).agg({
                col: list for col in dataframe.columns if col != groupby_column
                }).reset_index()
            
            globals()[key] = dataframe  # Assigning the modified DataFrame back to its original variable
            
            # Checking the duplicates:
            duplicates = dataframe.loc[dataframe[column].duplicated() == True, column].shape[0]
            print(f'Final result: column {column} has {duplicates} duplicates.\n')
            logger.info(f'Final result: column {column} has {duplicates} duplicates.')
        
        
    ### Merging all the tables ###

    print('Starting merge of all tables.')
    logger.info('Starting merge of all tables.')

    # Creating a main table 'data' by merging the datasets:
    data = pd.merge(jobs, companies[['company_id','company_name','company_url']], on='company_id', how='left', suffixes=('_#jobs', '_#companies'))
    data = pd.merge(data, industries, on='company_id', how='left', suffixes=('_#jobs', '_#industries'))
    data = pd.merge(data, salaries, on='job_id', how='left', suffixes=('_#jobs', '_#salaries'))
    data = pd.merge(data, employee_counts[['company_id', 'employee_count', 'follower_count']], on='company_id', how='left', suffixes=('_#jobs', '_#employee_counts'))
    data = pd.merge(data, skills, on='job_id', how='left', suffixes=('_#jobs', '_#skills'))

    print('Merging of all tables completed succesfully!\n')
    logger.info('Merging of all tables completed succesfully!')


    ### Creating a discription dataframe ###
    print('Creating a description dataframe...\n')
    logger.info('Creating a description dataframe...')
    data_counts = pd.DataFrame(index = data.columns, columns = ['Rows', 'Values', 'Unique values', 'NULLs', 'Zeros','Duplicates'])

    # Filling the values into the dataframe:
    for column in data.columns:
        data_counts.loc[column, 'Rows'] = len(data[column])
        data_counts.loc[column, 'Values'] = data.loc[data[column].notnull() == True, column].shape[0]
        data_counts.loc[column, 'Unique values'] = data.loc[data[column].duplicated() == False, column].shape[0]
        data_counts.loc[column, 'NULLs'] = data.loc[data[column].isnull() == True, column].shape[0]
        data_counts.loc[column, 'Zeros'] = data.loc[data[column] == 0, column].shape[0]
        data_counts.loc[column, 'Duplicates'] = data.loc[data[column].duplicated() == True, column].shape[0]

    # Ordering the dataframe by number of NULLs descending:
    data_counts = data_counts.sort_values(by = 'NULLs', ascending=False)

    print('Discription table:')
    print(f'{data_counts}\n')
    logger.info('Discription table:\n'
                f'{data_counts}'
                )



    # ============================================================= #

    print('Altering columns of the data...')
    logger.info('Altering columns of the data...')


    ### TITLE ###
    # Clearing leading and trailing whitespaces:
    data['title'] = data['title'].str.strip()


    ### TIMESTAMP ###
    # Converting the UNIX time (in ms) to datetime:
    data['original_listed_time_ms'] = pd.to_datetime(data['original_listed_time'], unit='ms')
    data['expiry_time_ms'] = pd.to_datetime(data['expiry_time'], unit='ms')
    data['closed_time_ms'] = pd.to_datetime(data['closed_time'], unit='ms')
    data['listed_time_ms'] = pd.to_datetime(data['listed_time'], unit='ms')


    ### SALARY ###
    # Deleting salary columns from jobs table:
    data.drop(
        ['min_salary_#jobs', 'med_salary_#jobs', 'max_salary_#jobs', 'pay_period_#jobs', 'currency_#jobs', 'compensation_type_#jobs']
        , axis='columns'
        , inplace=True
        )

    # Renaming salary columns from salaries table:
    data.rename(columns={
        'min_salary_#salaries': 'min_salary', 
        'med_salary_#salaries': 'med_salary',
        'max_salary_#salaries': 'max_salary',
        'pay_period_#salaries': 'pay_period',
        'compensation_type_#salaries': 'compensation_type',
        'currency_#salaries': 'currency'
        }, inplace = True)

    # Creating a dictionary with time multiplier values:
    time_multiplier = {'YEARLY':1, 'MONTHLY':12, 'WEEKLY':52, 'HOURLY':52*40}

    # Creating new columns and initializing them with None values:
    data.loc[:, ['min_salary_normalized','med_salary_normalized','max_salary_normalized']] = np.NaN

    # Iterating through different multipliers in dictionary and calculating normalized salary columns:
    for key, value in time_multiplier.items():
        for column, column_normalized in {
            'min_salary':'min_salary_normalized', 
            'med_salary':'med_salary_normalized', 
            'max_salary':'max_salary_normalized'}.items():
                data.loc[data['pay_period'] == key, column_normalized] = data.loc[data['pay_period'] == key, column] * time_multiplier[key]


    ### LOCATION ###
    
    # ------------------------------------------------------------------ #
    # Defining a function to resolve a state name from a string input:
    def find_USA_states(location: str) -> pd.Series:
        '''
        Function description: This function resolves a USA state name from the input string.
        '''
        
        # Dictionary of USA states (dictionary is faster than a list because it uses a hashmap):
        states_USA = {
            'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
            'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
            'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
            'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
            'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
            'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
            'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
            'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
            'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
            'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
        }

        # Lowercase of 'states_USA' dictionary (for case-insensitive search):
        states_USA_lowercase = {key.lower(): value.lower() for key,value in states_USA.items() 
                                if isinstance(key, str) and isinstance(value, str)}
        
        # Splitting the input location string into words:
        words = location.lower().split()
        
        # Defining column names of the return:
        column_name_state = 'state'
        column_name_state_abbr = 'state_abbr'
        
        # Iterate through the words and check if they match the state names or abbreviations:
        for word in words:
            for state_abbr, state in states_USA_lowercase.items():
                # First check state abbreviations (it is faster):
                if word in state_abbr:
                    return pd.Series([states_USA[word.upper()].capitalize(), word.upper()], index=[column_name_state, column_name_state_abbr])
                # If no abbreviation match is found, check for full state names:
                elif word == state.lower():
                    return pd.Series([state.capitalize(), state_abbr.upper()], index=[column_name_state, column_name_state_abbr])
                # If no match is found, return NaN:
                else:
                    return pd.Series([None, None], index=[column_name_state, column_name_state_abbr])  
    # ------------------------------------------------------------------ #
    
    # Applying the 'find_USA_states' function to the final dataset (appending 2 columns to the main dataset: 'state' and 'state_abbr'):
    data = pd.concat([data, data['location'].apply(find_USA_states)], axis=1)



    print('Altering of the columns of data finished succesfully!\n')
    logger.info('Altering of the columns of data finished succesfully!')

    # ============================================================= #


    # Exporting final dataset to CSV (using delimiter: `):
    print('Exporting data to CSV!')
    logger.info('Exporting data to CSV!')

    data.to_csv('final_dataset.csv', sep = configuration['delimiter_export'], index=False)

    print('Exporting data to CSV completed succesfully!\n')
    logger.info('Exporting data to CSV completed succesfully!')

    print(f'Number of rows: {len(data)}')


    # Clearing the log file if larger than 1000 rows:
    clear_log(configuration['logger']['file'], max_log_lines)


### Running the main code: ###
if __name__ == "__main__":
    main()