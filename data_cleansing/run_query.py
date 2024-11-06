import sys
from audio_text import *

sys.path.append("../")
from util import *

import subprocess
import time


#############################
def fix_query(user_query):
    ### Task: fix user query###
    query = """
    We have recorded user's query as "{}". The query is related to the data in a set of CSV files.
    Can you add the puctuation and fixed the query if it is needed?
    As reference, you are given a set of table headers for CSV files listed in #Table headers#.

    Table headers:   TASK_RESULT("Get all headers")
    Please reply with only the fixed query, no other information.
    Answer:

    """

    template = """
    You are an expert on data science and finance security analysis. 
    You are responsible for using the data in CSV files to investigate a company or a person financial credit.
    Make sure you follow these rules:
    1. Ensure all the requirements in the question are met.
    2. Focus only on the feature implementation.
    3. Don't make up things if you don't know. 
    """


    query = query.format(user_query)

    return run_task("fix user query", template, query, T_TEXT)



def run_query(user_query):
    ### Task: Find user query related data###
    query = """
    You are given a set of table headers for CSV files listed in #Table headers#.
    Based on the meaning of the table headers, You should generate a list of CSV files to help to reply user's request of
    "{}"

    Table headers:   TASK_RESULT("Get all headers")
    Answer:

    """

    template = """
    You are an expert on data science and finance security analysis. 
    You are responsible for using the data in CSV files to investigate a company or a person financial credit.
    Make sure you follow these rules:
    1. Ensure all the requirements in the question are met.
    2. Focus only on the feature implementation.
    3. Don't make up things if you don't know. 
    """


    query = query.format(user_query)

    run_task("Find user query related data", template, query, T_TEXT)

    ### Task: Find user query related data code###
    query = """
    You are given a list of CSV files: TASK_RESULT("Find user query related data")
    The files are at ./data directory. 
    we are going to use the data from the CSV files to generate the response for user's query: "{}"
    The table headers of the CSV files are listed in #Table headers#.
    Based on the meaning of the table headers, You should generate the code to pull out the data from the CSV files. 

    The code should write the result to CURRENT_TASK_RESULT_TEXT_FILE

    Table headers:   TASK_RESULT("Get all headers")

    """

    template = """
    You are an expert on data science and finance security analysis. 
    You are responsible for using the data in CSV files to investigate a company or a person financial credit.
    Make sure you follow these rules:
    1. Ensure all the requirements in the question are met.
    2. Focus only on the feature implementation.
    3. Don't make up things if you don't know. 
    """

    query = query.format(user_query)

    run_task("Find user query related data code", template, query, T_CODE)

    ### Task: Generate response for user query###
    query = """
    Here is the data collected to answer user's query:  TASK_RESULT("Find user query related data code")
    Please use and only use the collected data to create a write up for user's query: "{}" 
    Answer:

    """

    template = """
    You are an expert on data science and finance security analysis. 
    You are responsible for using the data in CSV files to investigate a company or a person financial credit.
    Make sure you follow these rules:
    1. Ensure all the requirements in the question are met.
    2. Focus only on the feature implementation.
    3. Don't make up things if you don't know. 
    """

    query = query.format(user_query)

    run_task("Generate response for user query", template, query, T_TEXT)


filename = "recording.wav"  # Output file name

def get_and_run_query():
    while True:
        query = input("Query:")
        if query == 'n':
            break

        text = audio_to_text(filename)
        print(text)

        new_fix = fix_query(text)
        if new_fix is not None:
            text = new_fix
            print("Fixed Query:", text)

        r = input("Generate the response:")

        if r == 'y':
            context_s = run_query(text)
        

get_and_run_query()

#"我想了解一下秦皇岛市高深汽车服务有限公司的基本情况？能帮助我查询吗？"
#"我想了解一下关于广东华阳实业有限公司"

#"我想了解一下关于股东王爷的持股情况姓王的王树叶的叶"