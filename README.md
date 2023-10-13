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
Run the application
``` 
python app.py
```
