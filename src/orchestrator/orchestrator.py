import json
from pathlib import Path

from src.agents.planner import PlannerAgent
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.agents.creative_generator import CreativeGenerator


class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.data_agent = DataAgent()
        self.insight_agent = InsightAgent()
        self.evaluator = EvaluatorAgent()
        self.creative = CreativeGenerator()

        self.reports_path = Path("reports/")
        self.reports_path.mkdir(exist_ok=True)

    def run(self, user_query: str):
        print("\n🔹 Step 1: Planning...")
        plan = self.planner.run(user_query)
        print("Plan:", plan)

        print("\n🔹 Step 2: Data Summary...")
        data_summary = self.data_agent.run()
        print("Data Summary:", data_summary)

        print("\n🔹 Step 3: Generating Hypotheses...")
        insights = self.insight_agent.run(data_summary)
        print("Hypotheses:", insights)

        print("\n🔹 Step 4: Evaluating Hypotheses...")
        validated = self.evaluator.run(insights, data_summary)
        print("Validated:", validated)

        print("\n🔹 Step 5: Generating Creative Recommendations...")
        creatives = self.creative.run(data_summary)
        print("Creatives:", creatives)

        print("\n🔹 Step 6: Saving Output Files...")

        # Save insights.json
        with open("reports/insights.json", "w") as f:
            json.dump(validated, f, indent=2)

        # Save creatives.json
        with open("reports/creatives.json", "w") as f:
            json.dump(creatives, f, indent=2)

        # Save report.md
        self.generate_report(validated, creatives)

        print("\n✅ All done! Check the 'reports/' folder.\n")

    def generate_report(self, validated, creatives):
        report_path = self.reports_path / "report.md"

        with open(report_path, "w", encoding="utf-8") as f:

            f.write("# Facebook Ads ROAS Analysis Report\n\n")

            f.write("## 🔍 Validated Insights\n")
            f.write("These insights are validated based on data trends:\n\n")
            f.write("```\n")
            f.write(json.dumps(validated, indent=2))
            f.write("\n```\n\n")

            f.write("## 🎨 Creative Recommendations\n")
            f.write("Generated suggestions to improve low CTR campaigns:\n\n")
            f.write("```\n")
            f.write(json.dumps(creatives, indent=2))
            f.write("\n```\n\n")

        print(f"Report saved: {report_path}")
