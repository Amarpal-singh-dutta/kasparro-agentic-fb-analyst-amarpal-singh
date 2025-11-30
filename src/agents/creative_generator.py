from pathlib import Path
from src.utils.helpers import call_llm

class CreativeGenerator:
    def __init__(self):
        self.prompt = Path("prompts/creative.md").read_text()

    def run(self, data_summary):
        llm_input = self.prompt + "\n\nLOW CTR SUMMARY:\n" + str(data_summary)
        return call_llm(llm_input)
