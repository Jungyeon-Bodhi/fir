#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:18:51 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import bodhi_data_preprocessing as dp

project_name = "East Africa Fund Evaluation"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/25-SS-GLO-1 - Raw Dataset"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/25-SS-GLO-1 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

enumerator_name = 'E2'
respondent_name = 'Respondent Name'
# Original column name for respondents' names (for anonymisation and duplicate removal)

identifiers = [respondent_name, 'start', '_id', '_uuid']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = [] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['start','end', 'start-geopoint','_start-geopoint_latitude','_start-geopoint_longitude','_start-geopoint_altitude','_start-geopoint_precision',
 'today','deviceid','E1', 'E1-2','E1-3','E1-4','E2-1','E2-2','E2-3','E2-4','E2-5','E2-6','E2-7','E2-8','E2-9','E2-11', 
 'E3-1', 'E3-2', 'E3-3', 'E4', 'E5', 'E6-1', 'E6-2',
 '1', '2', '3', '4-1', '4-2', '4-3', '5-1', '5-2', '5-2-2', '5-2-3', '5-3',
 'Respondent Name', '7', '8', '9', '9-o', '10', '10-o', '11a', '11-1', '11-2', '11-3', '11-4', '11-5', '11-6', '11-7', '11-8', '11-o',
 '12', '13', '14', '15','16', '17', '18','18-2a','18-2-1','18-2-2','18-2-3','18-2-4',
 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28a', '28-1', '28-2', '28-3', '28-4', '28-5', '28-6', '28-o',
 '29', '30', '31', '32', '33', '33-o', '34', '34-o', '35', '35-1a', '35-1-1', '35-1-2', '35-1-3',
 '36', '37', '38', '39', '40', '41', '42', '43', '44', '44-o', '45', '46', '47a',
 '47-1', '47-2', '47-3', '47-4', '47-5', '47-6', '47-7', '47-8', '47-9', '47-o',
 '48', '49', '50-1', '50-2','51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '60-1', '61', '62',
 '63', '64', '65', "66", '67', '68', '69', '70', '71', '72', '73', '74', '75',
 '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '85-o', '86', '87a', 
 '87-1', '87-2', '87-3', '87-4', '87-5', '87-6', '88', '89', '90', '91a',
 '91-1', '91-2', '91-3', '91-4', '91-5', '91-6', '91-o', '92', '93', '94', '95', '96', '97', '98', '99',
 '100', '101', '102', '103', '103-1', '104', '105a',
 '105-1', '105-2', '105-3', '105-4', '105-5', '105-6', '105-7', '105-8', '105-o',
 '106', '107', '108', '109', '110', '111', '112', '113', '113-o', '114',
 '115a', '115-1', '115-2', '115-3', '115-4', '115-5', '115-6', '115-7', '115-o',
 '116', "117", "118", '119', '120', '121', '122', '123', '124', '125', '125-o', '126', 'none1', 'none2', 'none3',
 '_id', '_uuid', '_submission_time', '_validation_status', '_notes', '_status', '_submitted_by',
 '__version__', '_tags', '_index', 'none4','none5','none6','none7']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['start-geopoint','_start-geopoint_latitude','_start-geopoint_longitude','_start-geopoint_altitude','_start-geopoint_precision',
 'today','deviceid','start','end','E4','E6-1','E6-2', '11a', '18-2a','28a', '35-1a','47a','87a','91a','105a',
                 '115a','none1', 'none2', 'none3',
                 '_id', '_uuid', '_submission_time', '_validation_status', '_notes', '_status', '_submitted_by',
                 '__version__', '_tags', '_index', 'none4','none5','none6','none7']
# Specify the columns to be excluded from the data analysis

miss_col = ['2', '3','7','12', '13', '14', '15','16', '17','125']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['9-o','10-o', '11-o', '28-o', '33-o','34-o','44-o','47-o', '65','85-o',
             '91-o','103-1','105-o','113-o','115-o','124','125-o','126']
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = '1'
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['12', '13', '14', '15','16', '17']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

fir = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, respondent_name, enumerator_name, identifiers, open_cols, cols_new, age_col, diss_cols, del_type = 0, file_type=file_type)
fir.processing()