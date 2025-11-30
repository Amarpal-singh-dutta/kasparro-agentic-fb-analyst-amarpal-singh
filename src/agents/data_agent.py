import pandas as pd
from pathlib import Path
from src.utils.helpers import call_llm, load_yaml

class DataAgent:
    def __init__(self):
        config = load_yaml("config/config.yaml")
        self.csv_path = config["data_path"]
        self.prompt = Path("prompts/data_agent.md").read_text()

    def run(self):
        df = pd.read_csv(self.csv_path)

        summary = {
            "roas_mean": df["roas"].mean(),
            "ctr_mean": df["ctr"].mean(),
            "top_campaigns": df["campaign_name"].value_counts().head(5).to_dict(),
            "low_ctr": df[df["ctr"] < df["ctr"].mean()]["campaign_name"].unique().tolist(),
        }

        llm_input = self.prompt + "\n\nDATA SUMMARY:\n" + str(summary)
        return call_llm(llm_input)
