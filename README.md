# Kasparro — Agentic Facebook Performance Analyst  
### Assignment Submission — *Amarpal Singh Dutta*

---

## 🚀 Quick Start

```bash
python -V  # should be >= 3.10
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
python src\run.py "Analyze ROAS drop in last 7 days"
```

---

## 📂 Project Structure

```
config/
  config.yaml
data/
  sample.csv
prompts/
reports/
  report.md
  insights.json
  creatives.json
logs/
src/
  agents/
  orchestrator/
  utils/
tests/
README.md
```

---

## 🧠 Agent Architecture

**Planner Agent**  
Breaks the user query into subtasks.

**Data Agent**  
Loads dataset and returns summarized trends (ROAS, CTR, drops).

**Insight Agent**  
Generates hypotheses explaining performance.

**Evaluator Agent**  
Validates hypotheses using quantitative data signals.

**Creative Agent**  
Creates improved headlines/messages for low-CTR ads.

**Orchestrator**  
Controls the full workflow and saves outputs.

👉 Diagram available in **`agent_graph.md`**

---

## 📊 Example Output (Generated)

- `reports/insights.json`  
- `reports/creatives.json`  
- `reports/report.md`  

These files are generated when running:

```bash
python src/run.py "Analyze ROAS drop in last 7 days"
```

---

## 🧪 Validation Layer

Evaluator checks:

- Metric grounding  
- Insight completeness  
- Confidence scoring  
- CTR/ROAS thresholds from config  

Evaluator tests included under:

```
tests/test_evaluator.py
```

---

## 🔁 Reproducibility

- Seed fixed (config.yaml)  
- Sample dataset included  
- Instructions fully reproducible  
- Requirements pinned  

---

## ✔ Submission Checklist Status

- ✓ Correct repo name  
- ✓ README with commands + architecture  
- ✓ All agents implemented  
- ✓ prompts/ folder  
- ✓ reports/ folder (3 files)  
- ✓ logs/ added  
- ✓ config.yaml added  
- ✓ evaluator test added  
- ✓ v1.0 release created  
- ✓ PR “self-review” created  

---

