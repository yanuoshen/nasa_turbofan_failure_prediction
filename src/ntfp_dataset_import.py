'''
NASA Turbofan Failure Prediction - Dataset Import

This file supports dataset importation and exploratory data analysis.

'''

###################################
# Module Importations (A - Z Format)
###################################
import numpy as np
import pandas as pd

# Constants
dataset_columns = ('Engine', 'Cycles','Set-1', 'Set-2', 'Set-3', 
                    'Sn_01', 'Sn_02', 'Sn_03', 'Sn_04', 'Sn_05', 'Sn_06', 'Sn_07',
                    'Sn_08', 'Sn_09', 'Sn_10', 'Sn_11', 'Sn_12', 'Sn_13', 'Sn_14',
                    'Sn_15', 'Sn_16', 'Sn_17', 'Sn_18', 'Sn_19', 'Sn_20', 'Sn_21' ) 

filename1_string = r'C:\Developer\PMetcalf\nasa_turbofan_failure_prediction\data\train_FD001.txt'
filename2_string = r'C:\Developer\PMetcalf\nasa_turbofan_failure_prediction\data\train_FD002.txt'
filename3_string = r'C:\Developer\PMetcalf\nasa_turbofan_failure_prediction\data\train_FD003.txt'
filename4_string = r'C:\Developer\PMetcalf\nasa_turbofan_failure_prediction\data\train_FD004.txt'

def import_dataset():
    """
    Import the dataset as a dataframe, adding column names.
    ======================================

    Input:
        None.

    Output:
        raw_data_df (dataframe) - Raw data as dataframe, with column names.
    """

    # Import the raw data into series of dataframes.
    first_data_df = pd.read_csv(filename1_string, header = None, names = dataset_columns, delim_whitespace = True, index_col = 0)

    second_data_df = pd.read_csv(filename2_string, header = None, names = dataset_columns, delim_whitespace = True, index_col = 0)

    # Normalise engine number (index) for appending.
    new_engine_number_list = second_data_df.index.tolist()

    for index in range(len(new_engine_number_list)):
        new_engine_number_list[index] += 100

    print(new_engine_number_list)

    # Append dataframes together.
    raw_data_df = first_data_df.append(second_data_df)
    
    print(raw_data_df.head)

    return raw_data_df

def peek_dataset(data_df):
    """
    Prints a series of data about the supplied dataframe.
    ======================================

    Input:
        data_df (dataframe) - Dataframe with data to be visualised.

    Output:
        None.
    """

    # Visualise dataframe information.
    print(data_df.head(5))

    print(data_df.info())

    print(data_df.describe())