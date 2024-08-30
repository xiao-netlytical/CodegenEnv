import sys
sys.path.append("../")
from util import *
from test_gen import *

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
# run_task("Converting xlsx file to csv file", template, query, T_CODE)

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
# run_task("Generate dirty data report", template, query, T_CODE)

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

# run_task("Find problem cells", template, query, T_CODE)

### Task: Get table headers ###
query = """
Request:  Your task is to generate python3 code to get the header names from all the csv files.
The result should be in the format of file_name followed by a list of column names in Json format.
The code will take the csv files from ./data directory and write the result 
to <<running_result_name("Get table and headers", T_JSON)>>. 
With the generated code, attach a output sample strcuture.

The code should be executable by itself.

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

# run_task("Get table and headers", template, query, T_CODE)


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

# run_task("Get all headers", template, query, T_CODE)

### Task: Common column grouping ###
query = """
You are given a list of table headers in #Table headers# for CSV files. 
Group these headers based on their semantic meaning to represent the same data. 

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

# run_task("Common column grouping", template, query, T_TEXT)

### Task: Similar column grouping ###

query = """
You are given a list of table headers in #Table headers# for CSV files. 
Group these headers based on their meaning to represent the same data.

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

# run_task("Similar column grouping", template, query, T_TEXT)

### Task: Similar table column grouping ###
query = """
Request: Your task is to generate python3 code to associate the header names with the table names.
Your code will take the following inputs: 
1. a list header groups: <<task_result("Similar column grouping")>>
2. a list of table to headers mapping from file  <<running_result_name("Get table and headers")>>.
   This is an example data structure of the file:
   {
    "file1.csv": ["column1", "column2", "column3"],
    "file2.csv": ["columnA", "columnB", "columnC"],
    "file3.csv": ["header1", "header2"]
    }

The code will generate a list of header groups in which the table name is associated with the header name.
The code should write the result in json to file - <<running_result_name("Similar table column grouping", T_JSON)>>
With the generated code, attach a output sample structure.

Answer:
"""

template = """
You are an expert on data science and responsible for data analysis.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

# run_task("Similar table column grouping", template, query, T_CODE)

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

# run_task("Find loan related dataset", template, query, T_TEXT)

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

# run_task("Find wrong doing dataset", template, query, T_TEXT)

### Task: Identify redundant column ###
query = """
Request: Your task is to generate python3 code to identify the similarity of any two columns within a csv file.
The code will compare values from every row from the two columns, and give the similarity report in percentage 
when the similarity is  > 80.
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
# run_task("Identify redundant column within table", template, query, T_CODE)

### Task: Identify column similarity ###
query = """
Request:  Your task is to generate python3 code to identify the similarity of two columns by the rows from the csv files.
The code should ignore the order of the rows and skip the column which does not have more than one unique value.
The code should compare any two columns from the same group listed in the file <<running_result_name("Similar table column grouping")>>. 
Two columns under a group can be in same or different tables. The comparation should include both scenarios.
The input JSON file will have the following structure as an example:

{
    "Company Information": {
        "file1.csv": ["公司ID", "公司唯一标识"],
        "file2.csv": ["注册资金"]
    },
    "Legal Information": {
        "file1.csv": ["案号", "立案时间"],
        "file3.csv": ["案件类型"]
    },
    "Risk Information": {
        "file2.csv": ["风险类型"]
    },
    ...
}

Where "Company Information" is a group name, "file1.csv" is a table name, and the lists contain the group members.
The table names is also the csv file names in ./data directory. The code should write the result to ./data/similar_columns.txt when the similarity percentage > 0 
and also provide the percentages. The code should be executable by itself.

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

run_task("Identify column similarity", template, query, T_CODE)


test_request = """In your setup of grouping mapping, the headers associated to the same file
should be in same csv file. And the columns belonging to same group should share some common values.
For example for 
    grouping_data = {
        "Company Information": {
            "file1.csv": ["公司ID", "公司唯一标识"],
            "file2.csv": ["注册资金"]
        },
        "Legal Information": {
            "file1.csv": ["案号", "立案时间"],
            "file3.csv": ["案件类型"]
        },
        "Risk Information": {
            "file2.csv": ["风险类型"]
        }
    }

The file1.csv should have the headers of "公司ID", "公司唯一标识", "案号" and "立案时间".
The file2.csv should have the headers of "注册资金" and "风险类型".
For testing purpose, You should set cells in the following pairs of columns to be same: 
cells of "案号" and "案件类型" should have same values, cells of "公司ID" and "公司唯一标识" should have same values.

The test should cover the cases:
1. For the headers in the same group and the same file, there should be a similarity result if the percentage > 0.
2. For the headers in the same group but in different files, there should be a similarity result if the percentage > 0.
3. For headers in different groups, there should not be any comparation.
Verify that you can find "案号" and "案件类型" in the same line and 
"公司ID" and "公司唯一标识" in the same line."""

test_case_task("Identify column similarity", test_request, query)

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

# run_task("Design dirty data cleansing", template, query, T_TEXT)

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

# run_task("Generate report code", template, query, T_CODE)