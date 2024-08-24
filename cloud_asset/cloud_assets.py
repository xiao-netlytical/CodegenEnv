from util import *

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

run_task("Generate resource catalog", template, query, T_TEXT)

### Step 1_0 ###

query = """
Request: Verify the provided list for the resources supported by AWS cloud platform
and the relationships between the resources. Make sure the list is complete.
You can use the features supported by Wiz as references.
Only provide the updated list and the differences if there is.

List of sources and relationship: <<task_result("Generate resource catalog")>>

Answer:
"""

template = """ 
System: You are an expert on cloud computing and responsible for researching 
the technolodge and implementation for a cloud platform. 
You will only use the fact you know to create your answer.
"""

# run_task("Generate resource catalog", template, query, T_TEXT)

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

List of source and relationship: <<task_result("Generate resource catalog")>>
Answer:

"""

template = """you are a helpful agent."""


# run_task("Generate catalog relationship", template, query, T_JSON)


query = """
Request: Your task is generating the code to draw the relationships using the input 
from the List of source and relationship.
You should use python, networkx and matplotlib for your coding. 
The code should be executable. 

List of source and relationship: <<task_result("Generate catalog relationship")>>
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

# run_task("Generate drawing", template, query, T_CODE)

### Step 3 ###

query = """
Request: Your task is generating the code to scan and discover all the resources in a given AWS environment. 
The resource type to scan is listed by the #List of source and relationship#.
You should use python and SDK for your code. 
The code should write the result to a file - <<running_result_name("Scan resources", T_JSON)>>. 
When generating the code, put import line inside the main section. The code should be executable. 

List of source and relationship: <<task_result("Generate resource catalog")>>

Code:

"""

template = """You are an expert on cloud computing and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. """

run_task("Scan resources", template, query, T_CODE)

### Step 4 ###

query = """
Request: Your task is generating the code to get the details for the discovered resources.
You are given the list of Discovered resources for getting the details.
You should use python and SDK for your code. The code should be executable. 
The code should write the result to a file - <<running_result_name("Get resource details", T_JSON)>>. 
Try to have seperate API for per resource and per relationship.

Discovered resources: <<running_result("Scan resources")>>

Code:"""

template = """You are an expert on cloud computing and python coding, 
responsible for writing the python code to implement the required features.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
   """


run_task("Get resource details", template, query, T_CODE)

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


Resource details: <<running_result("Get resource details")>>

Answer:

"""

template = """You are an expert on cloud computing and python coding.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know. 
"""

# run_task("Get resource relationship", template, query, T_JSON)

### Step 6 ###
   
query = """Your task is to generate python code to convert a json data structure.
The code's input is a dictionary of key:value pairs with the value as a list of dictionaries.
The code's output is a dictionary with only the first member kept in the value list.

The input data structure is in the file <<running_result_name("Get resource details", T_JSON)>>
The output file should be in <<running_result_name("Generate sample data", T_JSON)>>

Input example:

{
    "EC2": [
        {data1: value1,
        },
        {data2: value2,
        }
    ]
    "VPC": [
        {data3: value3,
        },
        {data4: value4,
        }
    ]
}
Output example:
{
    "EC2": [
        {data1: value1,
        }
    ]
    "VPC": [
        {data3: value3,
        }
    ]
}


"""

template = """You are an expert on cloud computing and python coding.
Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know."""

run_task("Generate sample data", template, query, T_CODE)


query = """Your task is to generate python code to find relationship between the resources in an AWS environment.
The code should use the cloud computing knowledge to discover the relationships from **the detailed resource data strcuture**. 
The code can cross reference the resources by using ties such as names, Ids, cidr blocks or IAM role attachment.
The format of the data strcuture is in the following Examples.

**Example**: <<running_result("Generate sample data")>>


The code should find **the detailed resource data strcuture** from the file <<running_result_name("Generate sample data", T_JSON)>>
The code should write the output to the file <<running_result_name("Generate relationship", T_JSON)>>

The output format should be in two lists with one as resource nodes and one as relationship edges. 

This is an example to demonstrate the formate:

    For the relatationships:
            'A' and 'B' with relationship of 'L1',
            'B' and 'C' with relationship of 'L2',
            'C' and 'A' with relationship of 'L3',

    The output should be
            {{
            "sources": ["A", "B", "C"],
            "relationships": [["A", "B", "L1"], ["B", "C", "L2"], ["C", "A", "L3"]]
            }}
"""

template = """You are an expert on cloud computing and python coding.
    Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know."""


run_task("Generate relationship", template, query, T_CODE)
visualize_result(running_result("Generate relationship"))

#####
query = """Your task is to generate python code to find relationship between the AWS resources 
and the IAM configurations in an AWS environment.
The resources are listed in the **Discovered resources**.
The code should use the cloud computing knowledge and boto3 api to get describe_instances to discover the relationships. 


Discovered resources: <<running_result("Scan resources")>>

The code should write the output to the file <<running_result_name("Generate IAM relationship", T_JSON)>>

The output format should be in two lists with one as resource nodes and one as relationship edges. 

This is an example to demonstrate the formate:

    For the relatationships:
            'A' and 'B' with relationship of 'L1',
            'B' and 'C' with relationship of 'L2',
            'C' and 'A' with relationship of 'L3',

    The output should be
            {{
            "sources": ["A", "B", "C"],
            "relationships": [["A", "B", "L1"], ["B", "C", "L2"], ["C", "A", "L3"]]
            }}
"""

template = """You are an expert on cloud computing and python coding.
    Make sure you follow these rules:
1. Ensure all the requirements in the question are met.
2. Focus only on the feature implementation.
3. Don't make up things if you don't know."""


run_task("Generate IAM relationship", template, query, T_CODE)

def visualize_result(json_data):
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
    
visualize_result(running_result("Generate IAM relationship"))