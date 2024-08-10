
import os
your_access_key = input("access key:")
your_secret_key = input("secret key:")
us_region = input("region:")
your_api_key = input("your openai api key:")

os.environ["AWS_ACCESS_KEY_ID"]=your_access_key
os.environ["AWS_SECRET_ACCESS_KEY"]=your_secret_key
os.environ["AWS_DEFAULT_REGION"]=us_region

project_data_dir = "scratchpad"

from openai import OpenAI

client = OpenAI(
  api_key=your_api_key,
)

def user_query_with_prompt(system_message,  user_message):
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
        ]
    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0
        )
    return response.choices[0].message.content

def code_start(s, start_mark="```python", end_mark="```"):
   i1 = s.find(start_mark)
   s1 = s[i1+len(start_mark):]

   i2 = s1.find(end_mark)
   s2 = s1[:i2]

   print("Generated Code:", s2)
   return s2

import json
def get_previous_json_result(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_current_json_result(file_path, json_data):
    with open(file_path, "w") as file:
        json.dump(json_data, file, indent=4)

def get_previous_text_result(file_path):
    with open(file_path, "r") as file:
        return file.read()

def save_current_text_result(file_path, result):
    with open(file_path, "w") as file:
        file.write(result)

def get_previous_code_result(file_path):
    with open(file_path, "r") as file:
        return file.read()

def save_current_code_result(file_path, result):
    with open(file_path, "w") as file:
        file.write(result)

import subprocess
def execute_file_with_error_handling(script_path):
    result = subprocess.run(['python3', script_path], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(result.stderr)
        return result.stderr

def run_and_debug_generated_code(task_name):
    check = 'y'
    while check == 'y':
        check = input("Do you want to run the generated code:")
        if check == 'y':
            code_str =  get_previous_task_result(task_name)
            output = execute_file_with_error_handling(task_name.replace(' ', '_')+".py")
            if output and output.find("Traceback") != -1:
                print(output)
                check = input("Do you want LLM to debug and update the code:")
                if check == 'y':
                    check_result=check_running_result(output, code_str)
                    if check_result:
                        code_str = code_start(check_result)
                        save_current_task_result(task_name, code_str)
                check = 'y'
            else:
                print("The code has run successfully.")
                check = 'n'

def check_running_result(error, code_str):
    query = """
        Request: Identify the root cause from this traceback: {list}.
        From the code: {code}. 
        Identify the issue with one line of message.
        And return with the updated code if there is. The updated code should be complete and executable"""
    
    template = """You are a helpful agent on debugging boto3 and python code"""

    query = query.format(list=error, code=code_str)
    result = user_query_with_prompt(template, query)
    return result

def run_text_generation_task(task_name, template, query):
    # print("TEMPLATE:", template)
    # print("QUERY:", query)

    check = input(f"Do you want to run task: <<{task_name}>>:")
    if check == 'y':
        result = user_query_with_prompt(template, query)
        save_current_task_result(task_name, result)
        print(result)

def run_code_generation_task(task_name, template, query):
    # print("TEMPLATE:", template)
    # print("QUERY:", query)

    check = input(f"Do you want to run task: <<{task_name}>>:")
    if check == 'y':
        result = user_query_with_prompt(template, query)
        code_str = code_start(result)
        save_current_task_result(task_name, code_str)
        print(result)

    print(f"The Code in {task_name}.py is ready to run")

    run_and_debug_generated_code(task_name)

def run_json_generation_task(task_name, template, query):
    # print("TEMPLATE:", template)
    # print("QUERY:", query)

    check = input(f"Do you want to run task: <<{task_name}>>:")
    if check == 'y':
        result = user_query_with_prompt(template, query)
        result = code_start(result, start_mark="```json")
        json_data = json.loads(result)
        save_current_task_result(task_name, json_data)

T_JSON=1
T_TEXT=2
T_CODE=3
task_list = {}
def run_task(task_name, template, query, type):
    task_list[task_name] = type
    if type == T_JSON:
        run_json_generation_task(task_name, template, query)
    elif type == T_TEXT:
        run_text_generation_task(task_name, template, query)
    elif type == T_CODE:
        run_code_generation_task(task_name, template, query)

def save_current_task_result(task_name, data):
    if task_list[task_name] == T_JSON:
        return save_current_json_result(task_name.replace(' ', '_')+".json", data)
    if task_list[task_name] == T_TEXT:
        return save_current_text_result(task_name.replace(' ', '_')+".txt", data)
    if task_list[task_name] == T_CODE:
        return save_current_code_result(task_name.replace(' ', '_')+".py", data)
    
def get_previous_task_result(task_name):
    if task_list[task_name] == T_JSON:
        return get_previous_json_result(task_name.replace(' ', '_')+".json")
    if task_list[task_name] == T_TEXT:
        return get_previous_text_result(task_name.replace(' ', '_')+".txt")
    if task_list[task_name] == T_CODE:
        return get_previous_code_result(task_name.replace(' ', '_')+".py")
    return None
    
        
 
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(sources, relationships, p_node=700, p_edge=20, p_font=12):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes from sources
    for source in sources:
        G.add_node(source)

    # Add edges from relationships
    for source, target, label in relationships:
        G.add_edge(source, target, label=label)

    # Get the positions of the nodes for the layout
    pos = nx.spring_layout(G)

    # Draw the nodes
    nx.draw_networkx_nodes(G, pos, node_size=p_node, node_color='lightblue')

    # Draw the edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='->', arrowsize=p_edge)

    # Draw the node labels
    nx.draw_networkx_labels(G, pos, font_size=p_font)

    # Draw the edge labels
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # Display the graph
    plt.title("Relationship Graph")
    plt.show()
