# Note: The openai-python library support for Azure OpenAI is in preview.
import json
import os
import openai

from functions import search_hotels
from dotenv import load_dotenv

load_dotenv()

messages= [
    {"role": "user", "content": "Find beachfront hotels in San Diego for less than $3000 a month with free breakfast."}
]

functions= [  
    {
        "name": "search_hotels",
        "description": "Retrieves hotels from the search index based on the parameters provided",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location of the hotel (i.e. Seattle, WA)"
                },
                "max_price": {
                    "type": "number",
                    "description": "The maximum price for the hotel"
                },
                "features": {
                    "type": "string",
                    "description": "A comma separated list of features (i.e. beachfront, free wifi, etc.)"
                }
            },
            "required": ["location"]
        }
    }
]

available_functions = {
            "search_hotels": search_hotels,
    }

response = openai.ChatCompletion.create(
    deployment_id="openai-gpt-4-deployment",
    model="gpt-4",
    messages=messages,
    functions=functions,
    function_call="auto", 
)

response_message = response['choices'][0]['message']

# Check if the model wants to call a function
if response_message.get("function_call"):

    # Call the function. The JSON response may not always be valid so make sure to handle errors
    function_name = response_message["function_call"]["name"]


    function_to_call = available_functions[function_name] 

    function_args = json.loads(response_message["function_call"]["arguments"])
    function_response = function_to_call(**function_args)

    # Add the assistant response and function response to the messages
    messages.append( # adding assistant response to messages
        {
            "role": response_message["role"],
            "function_call": {
                "name": function_name,
                "arguments": response_message["function_call"]["arguments"],
            },
            "content": None
        }
    )
    messages.append( # adding function response to messages
        {
            "role": "function",
            "name": function_name,
            "content": function_response,
        }
    ) 

    # Call the API again to get the final response from the model
    second_response = openai.ChatCompletion.create(
            messages=messages,
            deployment_id="openai-gpt-4-deployment",
            # optionally, you could provide functions in the second call as well
        )
    print(second_response["choices"][0]["message"])
else:
    print(response["choices"][0]["message"])
