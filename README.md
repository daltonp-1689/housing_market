# Housing Market Analysis
### El Dorado Hills & Folsom, CA

A structured data science project that goes from zero to a fully automated, AI-powered housing market analysis system — one small step at a time.

---

## What This Project Does

Analyzes real home sales data from El Dorado Hills and Folsom, CA to:
- Identify pricing trends and market patterns
- Train machine learning models that predict home prices
- Automatically generate plain-English market summaries using Claude AI
- Run the full pipeline on a schedule with no manual effort

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.14 |
| Data | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Machine Learning | scikit-learn |
| Notebooks | Jupyter |
| AI / Agents | Anthropic Claude API |
| Scheduling | APScheduler |
| Version Control | Git + GitHub |

---

## Project Structure

```
housing_market/
├── data/
│   ├── raw/          # Original downloaded data — never modified
│   └── processed/    # Cleaned, feature-engineered data ready for modeling
├── notebooks/        # Jupyter notebooks for exploration and analysis
├── src/
│   ├── agents/       # Autonomous agents (fetcher, analyst, reporter)
│   ├── pipeline/     # Data cleaning and feature engineering scripts
│   └── models/       # Model training and evaluation code
├── models/           # Saved trained model files
├── reports/          # Auto-generated market summary reports
├── dashboard.html    # Living learning dashboard (open in any browser)
├── requirements.txt  # Python dependencies
└── README.md
```

---

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/housing_market.git
cd housing_market
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate      # Mac/Linux
# .venv\Scripts\activate       # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set your Anthropic API key** *(needed for Module 8+)*
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

---

## Learning Roadmap

This project is structured as 9 progressive modules. Each builds directly on the last.

| Module | Topic | Key Concept Introduced |
|---|---|---|
| 1 | GitHub & Project Setup | Version control, project structure |
| 2 | Data & First Agent | Scheduled data fetching, agentic thinking |
| 3 | pandas Fundamentals | DataFrames, data manipulation |
| 4 | Jupyter Notebooks | Interactive analysis, documentation |
| 5 | Exploratory Analysis | Distributions, correlations, outliers |
| 6 | Data Pipeline | Automated cleaning, agent interface |
| 7 | Machine Learning | Regression models, price prediction |
| 8 | AI Integration | Claude API, tool use, Reporter agent |
| 9 | Agentic Systems | Multi-agent orchestration, scheduling |

Track progress in `dashboard.html` — open it in any browser, no server needed.

---

## The Agentic Pipeline (Module 9 Goal)

By the end of this project, three agents run automatically on a schedule:

```
[Fetcher Agent]  →  pulls fresh listing data on a schedule
      ↓
[Analyst Agent]  →  runs the ML pipeline, detects market shifts
      ↓
[Reporter Agent] →  calls Claude API, writes a plain-English summary to reports/
```

---

*Built as a learning project. Data sourced from public records and listing aggregators.*
