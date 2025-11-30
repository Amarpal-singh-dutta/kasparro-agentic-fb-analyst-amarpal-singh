import json
from pathlib import Path
from src.utils.helpers import call_llm

class PlannerAgent:
    def __init__(self):
        prompt_path = Path("prompts/planner.md")
        self.prompt_template = prompt_path.read_text()

    def run(self, query):
        prompt = self.prompt_template.replace("{query}", query)
        result = call_llm(prompt)
        return result  # should be {"tasks": [...]}
