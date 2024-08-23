import os

your_access_key = "aws access key"
your_secret_key = "aws secret key"
us_region = "aws region"
os.environ["AWS_ACCESS_KEY_ID"]=your_access_key
os.environ["AWS_SECRET_ACCESS_KEY"]=your_secret_key
os.environ["AWS_DEFAULT_REGION"]=us_region



your_api_key = "your_api_key "
os.environ["OPENAI_API_KEY"] = your_api_key

project_data_dir = "./scratchpad/"
