from pathlib import Path
from src.utils.helpers import call_llm

class InsightAgent:
    def __init__(self):
        self.prompt = Path("prompts/insight.md").read_text()

    def run(self, data_summary):
        llm_input = self.prompt + "\n\nDATA SUMMARY:\n" + str(data_summary)
        return call_llm(llm_input)
