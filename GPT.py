import os
import yaml
import completions

from openai import AzureOpenAI

with open('key.yaml') as f:
    key = yaml.load(f, Loader=yaml.FullLoader)
    os.environ['AZURE_OPENAI_ENDPOINT'] = key['AZURE_OPENAI_ENDPOINT']
    os.environ['AZURE_OPENAI_API_KEY'] = key['AZURE_OPENAI_API_KEY']
    os.environ['API_VERSION'] = key['API_VERSION']

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

messages=[
        {
            "role": "system",
            "content": "Who is DRI?",
        },
        {
            "role": "user",
            "content": "DRI stands for Directly Responsible Individual of a service. Which service are you asking about?"
        },
        {
            "role": "user",
            "content": "Opinion mining service"
        }
]

response = completions.get_completion_result(client, "GPT4O", messages)
print(response)