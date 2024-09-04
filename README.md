AI-Driven Software Development: A Practical Approach

To bridge the gap from AI assistant to AI software engineer, a half-step approach is adopted by integrating human engineering expertise with AI-driven code generation in a no-code development process.

With this approach, human engineers leverage their domain expertise and software development experience to create a multitasking workflow. Tasks are isolated and designed using prompts, guiding the LLM to either derive task-specific results or generate the code for task implementation. These tasks are then combined to build comprehensive applications, with some tasks performed by LLM agents, others executed using LLM-generated code, and some involving LLM calling LLM-generated APIs.

Carefully engineered modularities ensure that feature enhancements and bug fixes can be managed through prompt updates and code regeneration within an isolated scope, without manual coding. This multitasking approach enables the application of prompt engineering for task refinement through iterative prompt tuning, autonomous code regeneration and retesting.

To support this AI-driven approach, we’ve developed a code generation platform. In this environment, prompts are organized by task names. With a single trigger, the platform automatically populates the prompt with inputs from the dependent task's running results. The platform handles prompt completion and stages the running results, ensuring that stored results are available for task isolation and iterative refinement. For code generation prompts, the platform calls the LLM to generate the code, execute it, and automatically engage the LLM to fix any running issues. For unit test prompts, the platform associates the code generation prompt as the test specification and stores the LLM-generated test code in a dedicated directory.

In this repository, we demonstrate how to build a custom code generation environment. We recommend tailoring the environment to your specific needs for software testing and maintenance and selecting appropriate storage solutions to manage intermediate results and interfaces between generated code modules.

Future enhancements:

1. Finalize prompt templates for various types of requests.
2. Develop prompts and processes to integrate LLM-generated data structures into task definitions.
3. Convert LLM-generated code into LLM callback registration prompts.
4. Package autonomous task code into final software.
5. Package autonomous unit test code into testing software.

This repository also includes three application projects:

1. Multitasking Workflow for Cloud Asset Discovery:  

   This project demonstrates breaking down asset and relationship discovery into multi-staged tasks. Through effective prompt engineering, tasks can learn the output data structures from LLM-generated code.

2. Integration of LLM-Performed Tasks with AI-Generated Code for Dataset Cleansing and Preparation:  
   We utilize LLM-generated code to extract insights from CSV files. Additionally, we prompt the LLM to analyze and group table headers without exposing the entire dataset, and then generate code to analyze the dataset based on this grouping.

3. RAG Project with LLM for HW Specification Chatbot: 
   We showcase using LLM to evaluate RAG contexts based on the LLM responses generated from the provided contexts.



For inquiries, consulting, or collaboration opportunities, please contact: xiao.netlitical@gmail.com.
