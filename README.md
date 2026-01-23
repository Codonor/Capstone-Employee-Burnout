
# Employee Burnout & Turnover — Capstone Project

This repository contains a data analysis and modelling project that explores drivers of employee burnout and turnover using a synthetic employee dataset. The goal is to identify signals associated with higher burnout and exit risk, and to produce interpretable recommendations for reducing turnover.

---

## Table of Contents
- [Overview](#overview)
- [Quick Start](#quick-start)
- [Dataset](#dataset)
- [Notebooks & Code](#notebooks--code)
- [Results Summary](#results-summary)
- [File Structure](#file-structure)
- [How to Run](#how-to-run)
- [Ethics, GDPR and Governance](#ethics-gdpr-and-governance)
- [Use of AI Tools](#use-of-ai-tools)
- [Reflections, Learning and Development](#reflections-learning-and-development)
- [Next Steps](#next-steps)
- [Reproducibility](#reproducibility)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview
This project performs data cleaning, exploratory analysis, feature engineering and supervised modelling to predict burnout risk and employee exits. It produces visualizations and a set of notebooks that document the analysis pipeline and findings.

---
## Quick Start

Clone the repository and set up a Python virtual environment.

1. Clone the repo
   git clone <repo_url>
   cd Capstone

2. Create and activate a virtual environment

   Windows:
   python -m venv .venv
   .venv\Scripts\activate

   macOS / Linux:
   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. VS Code
   Open the project in VS Code and select the `.venv` interpreter:
   Command Palette → Python: Select Interpreter

5. Run
   Open notebooks in the `notebooks/` folder or run `app.py`.

---

## Dataset
- The project uses a synthetic employee dataset downloaded from kaggle, included in the `data/` folder: `synthetic-employee-dataset-raw`. The dataset proved too large to be managed on my system with 850,000 rows, thus it was randomly sampled to 100,000 rows and saved as `sampled_data.csv`, see `notebooks/notebook1_Sampling.ipynb`.
- Data is synthetic but designed to resemble real employee records: role, department, tenure, compensation, engagement/performance scores, work patterns, and exit flags.
- Key columns (high level): `employee_id`, `role`, `job_level`, `department`, `tenure_months`, `salary`, `performance_score`, `satisfaction_score`, `workload_score`, `team_sentiment`, `overtime_hours`, `training_participation`, `stress_level`, `burnout_risk`, `left_company`.
- See `notebooks/notebook2_feature_inspection_and_cleaning.ipynb` for preprocessing steps and data quality notes after which `data_cleaned.csv` was produced and used for all downstream analyses.

---

## Notebooks & Code
- `notebooks/notebook1_Sampling.ipynb` — sampling and initial dataset exploration
- `notebooks/notebook2_feature_inspection_and_cleaning.ipynb` — cleaning, missing-value strategy, type fixes, EDA
- `notebooks/notebook3_Feature_relationships_and_modelling.ipynb` — feature relationships, modelling and evaluation
- `app.py` — small app (Streamlit/Flask) to surface selected visualizations and model outputs.

---

## Results Summary
- Models and analysis consistently show that `stress_level`, `burnout_risk`,`satisfaction_score`, and `team_sentiment` are among the strongest signals associated with elevated exit probability.
- Feature importance and partial dependence plots are produced in Notebook 3; inspect them to see effect directions and thresholds.
- Actionable recommendations include, improving team-level morale interventions, monitoring and reducing stress levels, and targeted re-skilling / career-path support for high-risk groups.

---

## File Structure
- `app.py`: lightweight app to view results and visualizations
- `notebooks/`: analysis notebooks (see above)
- `data/`: raw and cleaned CSVs (`data_cleaned.csv`, `sampled_data.csv`)
- `requirements.txt`: Python dependencies

---

## How to Run
- Run the notebooks (Jupyter or VS Code):

```bash
jupyter notebook
```

- Or run the app (if using Streamlit):

```bash
streamlit run app.py
```

- To reproduce modelling results, open `notebooks/notebook3_Feature_relationships_and_modelling.ipynb` and run cells in order. The notebook documents package versions where relevant.

---

---

## Ethics, GDPR and Governance


## Use of AI Tools


## Reflections, Learning and Development


## Next Steps
- Add unit tests for data-processing functions.
- Persist model artifacts and add an inference script.
- Add an interactive dashboard with filtering by department / role.

---

## Reproducibility

Recommended Python version: 3.11+.
Use the included `requirements.txt` to create a matching environment.

- Notebooks set a random seed where required (seed = 42). If you re-run experiments, set the same seed to reproduce results.
- Notebook run order: `notebooks/notebook1_Sampling.ipynb` → `notebooks/notebook2_feature_inspection_and_cleaning.ipynb` → `notebooks/notebook3_Feature_relationships_and_modelling.ipynb`.

- Version control was used through Git/GitHub, with regular commits for all stages of work such as cleaning, processesing and modelling.

---

## Contributing
- Contributions are welcome. Open an issue to discuss major changes or create a branch and a pull request for smaller fixes.
- Add tests for any new data-processing functions and document new dependencies in `requirements.txt`.

---

## License
This project is provided under the MIT License — see the `LICENSE` file for details.

---

## Acknowledgements
Project produced as part of the Code Institute Capstone. Data included in `data/` is synthetic.

---

**Author / Contact:** Conor O'Brien

