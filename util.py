
import os
from config import *

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

def get_task_file_path(task_name):
    return project_data_dir+task_name.replace(' ', '_')

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
            output = execute_file_with_error_handling(get_task_file_path(task_name)+".py")
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
    print("QUERY:", query)

    check = input(f"Do you want to generate code for task: <<{task_name}>>:")
    if check == 'y':
        result = user_query_with_prompt(template, query)
        code_str = code_start(result)
        save_current_task_result(task_name, code_str)
        print(result)

    code_path = get_task_file_path(task_name)+".py"
    print(f"The Code in {code_path} is ready to run\n(make sure to set the required env and pip install if needed)")

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
    query = populate_task_query(query)
    task_list[task_name] = type
    if type == T_JSON:
        run_json_generation_task(task_name, template, query)
    elif type == T_TEXT:
        run_text_generation_task(task_name, template, query)
    elif type == T_CODE:
        run_code_generation_task(task_name, template, query)


def run_task_silent(task_name, template, query, type):
    task_list[task_name] = type
    print("Run Task: ", task_name)
    result = user_query_with_prompt(template, query)
    save_current_task_result(task_name, result)
    print(result)
    return result

def evel_llm_answer(context_collect, user_query):

    query = """You are given a list of <<Context, Answer>> pairs.
Please rank the answers based on how well they match the given question, 
considering that the Context is the sole source for the answers.
If there is a dedicated section to address the Request, the generated answer from the Contex is the best match.
A better answer should be more specific and technical, strictly based on the facts provided.
A better answer does not reason, extend, or simplify the topic.
Rank the answers from best match to least match.
    
    The Question, Context and Answer are given as following:

    Question: {u_query}

    {contx_list}
    """

    contx_list = """

        <<
        Context: {contx}
        Answer: {ans}
        >>

    """


    contx_l = ''
    for pair in context_collect:
        contx_l += contx_list.format(contx=pair[0], ans=pair[1])


    template = """You are a helpful agent."""

    query = query.format(contx_list=contx_l, u_query=user_query)

    reply = run_task_silent("Final Answer: ", template, query, T_TEXT)



def run_task_with_multi_context(task_name, context_list, template_m, query, t_type=T_TEXT):
    context_collect = []

    for i, data in enumerate(context_list):
        if not data.strip():
            continue
        template = template_m.format(contx=data)
        reply = run_task_silent(task_name+str(i), template, query, t_type)
        if "I don't know" not in reply.strip():
            context_collect.append((data, reply))

    if len(context_collect) > 1:
        evel_llm_answer(context_collect, query)


def save_current_task_result(task_name, data):
    if task_list[task_name] == T_JSON:
        return save_current_json_result(get_task_file_path(task_name)+".json", data)
    if task_list[task_name] == T_TEXT:
        return save_current_text_result(get_task_file_path(task_name)+".txt", data)
    if task_list[task_name] == T_CODE:
        return save_current_code_result(get_task_file_path(task_name)+".py", data)
    
def get_previous_task_result(task_name):
    if task_list[task_name] == T_JSON:
        return get_previous_json_result(get_task_file_path(task_name)+".json")
    if task_list[task_name] == T_TEXT:
        return get_previous_text_result(get_task_file_path(task_name)+".txt")
    if task_list[task_name] == T_CODE:
        return get_previous_code_result(get_task_file_path(task_name)+".py")
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


import re

def find_file_type(file_path):
    # Construct the full paths for .json and .txt files
    json_filepath = os.path.join(f"{file_path}.json")
    txt_filepath = os.path.join(f"{file_path}.txt")
    
    # Check if each file exists and return the type
    if os.path.isfile(json_filepath):
        return 'T_JSON'
    elif os.path.isfile(txt_filepath):
        return 'T_TEXT'
    else:
        return None

def running_result_name(task_name, type=''):

    file_path = get_task_file_path(task_name)+"_running_result"
    if not type:
        type = find_file_type(file_path)

    if type == 'T_JSON':
        return file_path+".json"
    if type == 'T_TEXT':
        return file_path+".txt"
    
    raise TypeError("Missing file: "+file_path)


def running_result(task_name):
    file_path = get_task_file_path(task_name)+"_running_result"

    type = find_file_type(file_path)
    
    if type == 'T_JSON':
        return get_previous_json_result(file_path+".json")
    if type == 'T_TEXT':
        return get_previous_text_result(file_path+".txt")
    
    raise TypeError("Missing file: "+file_path)

def task_result(task_name):
    file_path = get_task_file_path(task_name)

    type = find_file_type(file_path)
    
    if type == 'T_JSON':
        return get_previous_json_result(file_path+".json")
    if type == 'T_TEXT':
        return get_previous_text_result(file_path+".txt")
    
    raise TypeError("Missing file: "+file_path)

def task_result_name(task_name):

    file_path = get_task_file_path(task_name)

    type = find_file_type(file_path)

    if type == 'T_JSON':
        return file_path+".json"
    if type == 'T_TEXT':
        return file_path+".txt"
    
    raise TypeError("Missing file: "+file_path)
    
def populate_task_query(original_string):
    allowed_functions = {
        "task_result": task_result,
        "running_result": running_result,
        "running_result_name": running_result_name

    }

    pattern = r"<<(task_result|running_result|running_result_name)\((.*?)\)>>"
    matches = re.findall(pattern, original_string)

    final_string = original_string
    for func_name, args in matches:
        if func_name in allowed_functions:
            a_list = args.split(',')

            if len(a_list) == 1:
                result = allowed_functions[func_name](args.strip('"'))
            elif len(a_list) == 2:
                result = allowed_functions[func_name](a_list[0].strip().strip('"'), a_list[1].strip())
            else:
                raise TypeError("Not handled result file format")

            final_string = final_string.replace(f"""<<{func_name}({args})>>""", str(result))

    return(final_string)



def save_documents():
    import typing as t
    import jsonlines
    from langchain.schema import Document


    def save_docs_to_jsonl(documents: t.Iterable[Document], file_path: str) -> None:
        with jsonlines.open(file_path, mode="w") as writer:
            for doc in documents:
                writer.write(doc.dict())


    def load_docs_from_jsonl(file_path) -> t.Iterable[Document]:
        documents = []
        with jsonlines.open(file_path, mode="r") as reader:
            for doc in reader:
                documents.append(Document(**doc))
        return documents