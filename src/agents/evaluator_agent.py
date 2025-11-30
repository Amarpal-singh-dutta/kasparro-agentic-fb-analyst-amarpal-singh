from pathlib import Path
from src.utils.helpers import call_llm

class EvaluatorAgent:
    def __init__(self):
        self.prompt = Path("prompts/evaluator.md").read_text()

    def run(self, hypotheses, data_summary):
        combined = {
            "hypotheses": hypotheses,
            "summary": data_summary
        }
        llm_input = self.prompt + "\n\nINPUT:\n" + str(combined)
        return call_llm(llm_input)
