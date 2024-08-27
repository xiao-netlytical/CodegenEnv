import sys
sys.path.append("../")
from util import *

### Task: Converting xlsx file to csv file ###
query = """ 
    Your task is to generate python3 code which will find all the .xlsx files in ./data directory and
    converts the .xlsx files to .csv files. The code should generate different .csv files 
    for different tables. The generated files will be stored in the same ./data directory.
    If a column does not have a name, the code should not include the column in conversion. 
    If a row is empty, the code should not include the row in conversion.
    The code should not try to fix any bad data.
    The code should be executable. 

Answer:
"""

template = """
    You are an expert on data science and python coding, 
    responsible for writing the python code to implement the required features.
    Make sure you follow these rules:
    1. Ensure all the requirements in the question are met.
    2. Focus only on the feature implementation.
    3. Don't make up things if you don't know. 
"""
run_task("Converting xlsx file to csv file", template, query, T_CODE)

### Task: Generate and run dirty data report ###
query = """
Request: As a data scientist, you need to clean csv files before doing data analysis.
Your task is to generate python3 code to identify any issue with the data in csv files.
Your code should:
    1. **Identify Missing Values**: 
    - Report the number and percentage of missing values in each column.
    2. **Detect Duplicates**: 
    - Identify and report duplicate rows in the dataset.
    3. **Data Type Validation**: 
    - Check if the data types of each column are as expected (e.g., integers or floats vs strings).
    4. **Outlier Detection**: 
    - Implement methods to detect outliers in numerical columns (e.g., using Z-scores or IQR).
    - Provide a summary of detected outliers and their impact on the dataset.
    5. **Inconsistent Data Formats**: 
    - Identify inconsistencies in data formats (e.g., date formats, string casing).

The code will take the csv files from ./data directory and write the report to ./data/dirty_data_report.txt. 
The code should ignore special character related report. The code should be executable by itself.

Answer:
"""

template = """
You are an expert on data science and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""
run_task("Generate dirty data report", template, query, T_CODE)

### Task: Find bad cell##

query = """
As a data scientist, you need to clean csv files before doing any data analysis.
You need to clean the cells which includes any Accented Characters
or have leading or trailing Whitespace characters.

Your task is to generate python3 code to identify any cell which need to be cleaned.
The output should include the file name, the cell, the value and the identified issue. 
Ignore the cell with more than 50 characters or the cell which is Whitespace only.
The code will take all the csv files from ./data directory 
and write the result to ./data/problem_cells.txt. The code should be executable by itself.

Answer:
"""


template = """
You are an expert on data science and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

run_task("Find problem cells", template, query, T_CODE)

### Task: Get table headers ###
query = """
Request:  Your task is to generate python3 code to get the header names from all the csv files.
The result should be in the format of file_name followed by a list of column names.
The code will take the csv files from ./data directory and write the result 
to <<running_result_name("Get table and headers", T_TEXT)>>. The code should be executable by itself.

Answer:
"""

template = """
You are an expert on data science and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

run_task("Get table and headers", template, query, T_CODE)


### Task: Get all headers ###
query = """
Request:  Your task is to generate python3 code to get the header names from all the csv files.
The result should be in one list of header names in the format of file_name:header_name.
The code will take the csv files from ./data directory and write the result 
to  <<running_result_name("Get all headers", T_TEXT)>>. The code should be executable by itself.

Answer:
"""

template = """
You are an expert on data science and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

run_task("Get all headers", template, query, T_CODE)

### Task: Find common column ###
query = """
Request: You are given a list by #Table headers# as CSV headers.
You will group the headers to the same group if you think they should represent the same content just 
because some typo in the name. 

Table headers: <<running_result("Get all headers")>>
Answer:
"""

template = """
You are an expert on data science and responsible for data analysis.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

run_task("Find common column", template, query, T_TEXT)


### Task: Find loan related dataset ###
query = """
Request: You are given a list by #Table headers# as CSV headers.
Please fine the set of headers which can be used to derive loan related info and relationships.

Table headers: <<running_result("Get all headers")>>
Answer:
"""

template = """
You are an expert on data science and responsible for data analysis.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

run_task("Find loan related dataset", template, query, T_TEXT)

### Task: Find wrong doing dataset ###
query = """
Request: You are given a list by #Table headers# as CSV headers.
Please fine the set of headers which can be used to find any wrong doing with a compay or individual.

Table headers: <<running_result("Get all headers")>>
Answer:
"""

template = """
You are an expert on data science and responsible for data analysis.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

run_task("Find wrong doing dataset", template, query, T_TEXT)

### Task: Identify redundant column ###
query = """
Request: Your task is to generate python3 code to identify the similarity of any two columns within a csv file.
The code will compare values from every row from the two columns, and give the similarity report in percentage 
when the similarity is  > 60.
The code will take the csv files from ./data directory, walk through all the columns 
and write the report to file ./data/redundant_columns.txt.  The code should be executable by itself.

Answer:
"""

template = """
You are an expert on data science and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""
run_task("Identify redundant column in a table", template, query, T_CODE)

### Task: Identify similar column ###
query = """
Request: As a data scientist, you need to correlate tables before doing data analysis.
Your task is to generate python3 code to identify the similarity of two columns from two csv files.
The two columns should be in the same group listed in the ##Same grouping##. 
The column should have more than one unique values. The code can use a threshold like 50% to start with.
The code will take the csv files from ./data directory and write the report to ./data/similar_columns.txt. 
The code should be executable by itself.

Same grouping:  <<task_result("Find common column")>>

Answer:
"""

template = """
You are an expert on data science and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

run_task("Identify similar column", template, query, T_CODE)


###############################
# By listing all the possible cleansing techniques before generating the code, it may generate better coverage.
### Step 1 ###
query = """
As a data scientist, you need to clean csv files before doing any analysis. 
You could write python code to help you collect the entries which you need to clean. 
Please list and define the functionalities of such reporting software.
Don't write the code, someone will implement the code for you."""

template = """
You are an expert on data science and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

run_task("Design dirty data cleansing", template, query, T_TEXT)

### Step 2 ###
query = """
Request: Your task is to generate python3 code with the functionality specified by #Function spec#.
The code will take the csv files from ./data directory as input and write the report to ./data/complete_dirty_data_report.txt. 
Don't include special characters report and don't include summary statistics in the report.
No user interface is needed in the generated code, the code should be executable by itself.

Function spec: <<task_result("Design dirty data cleansing")>>
Answer:
"""

template = """
You are an expert on data science and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

run_task("Generate report code", template, query, T_CODE)