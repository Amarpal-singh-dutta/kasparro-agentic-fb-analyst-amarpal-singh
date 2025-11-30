import json
import openai
import yaml

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def call_llm(prompt, model="gpt-4o-mini"):
    response = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    try:
        return json.loads(response.choices[0].message.content)
    except:
        return {"error": response.choices[0].message.content}
