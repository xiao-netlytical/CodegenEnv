from util import *
# import boto3
# from datetime import datetime

### Step 1 ###

query = """
Request:  Your task is getting a complet list of resources supported by AWS cloud platform
and the possible relationships between the resources. Only include the list and relationship in your answer.
Answer:"""

template = """ 
You are an expert on cloud computing and responsible for researching 
the technolodge and implementation for a cloud platform. 
You will only use the fact you know to create your answer.
"""

run_task("Generate resource category", template, query, T_TEXT)

### Step 1_0 ###

query = """
Request: Verify the provided list for the resources supported by AWS cloud platform
and the relationships between the resources. Make sure the list is complete.
You can use the features supported by Wiz as references.
Only provide the updated list and the differences if there is.

List of sources and relationship: {list}

Answer:
"""

template = """ 
System: You are an expert on cloud computing and responsible for researching 
the technolodge and implementation for a cloud platform. 
You will only use the fact you know to create your answer.
"""
data = get_previous_task_result("Generate resource category")
query = query.format(list=data)

run_task("Generate resource category", template, query, T_TEXT)

### Step 2 ###

query = """
Request: Your task is converting the relationship given by the List of source and relationship
to two lists with one as node and one as relationships.

Using the following as an example for the output format:
with the discovered relationships:
    'A' and 'B' with relationship of 'L1',
    'B' and 'C' with relationship of 'L2',
    'C' and 'A' with relationship of 'L3',
the answer should be:
    {{
    "sources": ["A", "B", "C"],
    "relationships": [["A", "B", "L1"], ["B", "C", "L2"], ["C", "A", "L3"]]
    }}

List of source and relationship: {list}
Answer:

"""

template = """you are a helpful agent."""

data = get_previous_task_result("Generate resource category")
query = query.format(list=data)

run_task("Generate overall list", template, query, T_JSON)


query = """
Request: Your task is generating the code to draw the relationships using the input 
from the List of source and relationship.
You should use python, networkx and matplotlib for your coding. 
The code should be executable. 

List of source and relationship: {list}
Answer:
"""

template = """
You are an expert on cloud computing and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

data = get_previous_task_result("Generate overall list")
query = query.format(list=data)

run_task("Generate overall_visual_code", template, query, T_CODE)

### Step 3 ###

query = """
Request: Your task is generating the code to scan and discover all the resources in a given AWS environment. 
The resource type to scan is listed by the #List of source and relationship#.
You should use python and SDK for your code. 
The code should write the result to a file - code_str_result.json. 
When generating the code, put import line inside the main section. The code should be executable. 

List of source and relationship: {list}

Code:

"""

template = """You are an expert on cloud computing and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. """

data = get_previous_task_result("Generate resource category")
query = query.format(list=data)

run_task("Generate scan_resource_code", template, query, T_CODE)

### Step 4 ###

query = """
Request: Your task is generating the code to get the details for the discovered resources.
You are given the list of Discovered resources for getting the details.
You should use python and SDK for your code. The code should be executable. 
The code should write the result to a file - code_str_detail_result.json. 
Try to have seperate API for per resource and per relationship.

Discovered resources: {list}

Code:"""

template = """You are an expert on cloud computing and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
   """

data = get_previous_json_result("code_str_result.json")
query = query.format(list=data)

run_task("Generate get_resource_detaiil_code", template, query, T_CODE)

### Step 5 ###

query = """
Request: Your task is to discover the relationship between the resources using the provided Resource details.
you will generat two lists with one as nodes and one as relationship edges. 
For discovered relationships use the resource's type and specific name as the node name if possible.
So the next task can use your result to plot a relationship graph.

Using the following as an example for the output format:
    with the discovered relationships:
        'A' and 'B' with relationship of 'L1',
        'B' and 'C' with relationship of 'L2',
        'C' and 'A' with relationship of 'L3',
    the answer should be:
        {{
        "sources": ["A", "B", "C"],
        "relationships": [["A", "B", "L1"], ["B", "C", "L2"], ["C", "A", "L3"]]
        }}


Resource details: {list}

Answer:

"""

template = """You are an expert on cloud computing and python coding.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

data = get_previous_json_result("code_str_detail_result.json")
query = query.format(list=data)

run_task("Visualize relationship", template, query, T_JSON)

json_data = get_previous_task_result("Visualize relationship")

check = input("Do you want to visualize the realtionships:")
p_node=700
p_edge=20
p_font=12
while check == 'y':
   print(json_data)
   draw_graph(json_data["sources"], json_data["relationships"], p_node=int(p_node), p_edge=int(p_edge), p_font=int(p_font))
   check = input(f"The current node,edge,font is {p_node},{p_edge},{p_font}. Do you want to adjust with new number:")
   try:
      p_node, p_edge, p_font = check.split(",")
      check = 'y'
   except:
      check = 'n'
      pass
   


