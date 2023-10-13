# Bootstrapping Langchain function with Azure OpenAI

Sample Application to showcase how langchain can effectively run functions.

## Setup 
```
virualenv venv-lc && source venv-lc/bin/activate
pip install -r requirements.txt
```
Provide below environment variables via .env files
```
OPENAI_API_KEY=
OPENAI_API_BASE=https://{domainname}.openai.azure.com
OPENAI_API_TYPE=azure
OPENAI_API_VERSION=2023-07-01-preview # for functions this version is important
```

### Langchain:  Extract structured data from text
This example is for extracting the data and returning it into json format. 
``` 
python app.py
```

### AzureOpenAI: Sample Weather Bot
This example is for simulating static data chatbot, where you are asking the weather of particular city.
```
python weather_app.py
```
### AzureOpenAI: Sample Hotel Search Bot
This example is for simulating static data hotel search, where you are searching a hotel with the budget range
```
python hotel_app.py
```
