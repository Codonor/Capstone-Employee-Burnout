Capstone Employee Burnout

1. Project Title

Keep it concise but descriptive.

Example: Customer Churn Analysis for Subscription Services

2. Table of Contents (optional, but helpful)

Quick links to sections:

Overview

Motivation

Dataset

Methods

Results

Conclusion

Installation / Usage

File Structure

References

3. Project Overview / Summary

2–4 sentences about what the project does.

Include context and the business or research problem.

Example:

This project analyzes subscription customer data to predict churn. The goal is to identify key factors that cause customers to leave and to provide actionable recommendations to reduce churn.

4. Motivation / Problem Statement

Why you chose this project.

The problem you are solving and why it matters.

Could include potential impact if implemented in real life.

5. Dataset

Source of the data (public dataset, company dataset, etc.)

Feature Colunms and descriptions:
 - *`employee_id`*: Unique synthetic identifier
- *`role`*: Job title (300+ varieties)
- *`job_level`*: Entry | Mid | Senior | Manager | Lead
- *`department`*: Business unit (38 departments)
- *`tenure_months`*: Time with company (1-357 months)
- *`salary`*: Annual USD ($27K-$3384K range)
- *`performance_score`*: Normalized 0-1 rating
- *`satisfaction_score`*: Employee happiness (0-1)
- *`workload_score`*: Workload burden indicator
- *`team_sentiment`*: Team morale (0-1)
- *`recent_feedback`*: Employee's anonymous assessment of company
- *`communication_patterns`*: Persona-based style
- *`project_completion_rate`*: Delivery success metric
- *`overtime_hours`*: Extra hours logged (0-74 range)
- *`training_participation`*: L&D engagement
- *`collaboration_score`*: Teamwork rating
- *`technical_skills`*: Array of tech skills (4-9 per employee)
- *`soft_skills`*: Array of soft skills (3-7 per employee)
- *`email_sentiment`*: Email tone analysis
- *`slack_activity`*: Chat platform usage
- *`meeting_participation`*: Meeting engagement
- *`goal_achievement_rate`*: Objective completion
- *`stress_level`*: Stress assessment (0-1)
- *`burnout_risk`*: Burnout probability (0-1)
- *`left_company`*: Boolean exit flag
- *`turnover_reason`*: Exit category (if applicable)
- *`risk_factors_summary`*: Low | Medium | High | Severe risk
- *`turnover_probability_generated`**: ML-predicted churn risk
- *`persona_name`*: Type of employee 
- *`role_complexity_score`*: Job difficulty rating
- *`career_progression_score`*: Growth trajectory

Note any preprocessing done or data limitations

6. Methods / Approach

Data Cleaning: Missing values, outlier handling

Exploratory Data Analysis: Key visualizations or insights

Feature Engineering: Any derived variables

Modeling / Analysis: What algorithms or techniques you used

Evaluation Metrics: How you measured success (accuracy, RMSE, R², etc.)

Keep it concise; you don’t need the full code here, just a high-level roadmap.

7. Results

Key findings in simple, readable terms

Include graphs, tables, or summary statistics

Highlight actionable insights if applicable

8. Conclusion / Recommendations

Summarize what you learned

Suggest next steps or improvements

9. Installation / Usage (if applicable)

Steps to run the code/notebooks:

git clone <repo_url>
cd project-folder
pip install -r requirements.txt
jupyter notebook


Mention Python version, dependencies, and environment setup (venv recommended)

10. File Structure

Quick outline of important files:

├── data/
├── notebooks/
├── src/
├── README.md
├── requirements.txt

11. References / Resources

Cite datasets, tutorials, or research papers you used
Feature Colunms and descriptions:
 - *`employee_id`*: Unique synthetic identifier
- *`role`*: Job title (300+ varieties)
- *`job_level`*: Entry | Mid | Senior | Manager | Lead
- *`department`*: Business unit (38 departments)
- *`tenure_months`*: Time with company (1-357 months)
- *`salary`*: Annual USD ($27K-$3384K range)
- *`performance_score`*: Normalized 0-1 rating
- *`satisfaction_score`*: Employee happiness (0-1)
- *`workload_score`*: Workload burden indicator
- *`team_sentiment`*: Team morale (0-1)
- *`recent_feedback`*: Employee's anonymous assessment of company
- *`communication_patterns`*: Persona-based style
- *`project_completion_rate`*: Delivery success metric
- *`overtime_hours`*: Extra hours logged (0-74 range)
- *`training_participation`*: L&D engagement
- *`collaboration_score`*: Teamwork rating
- *`technical_skills`*: Array of tech skills (4-9 per employee)
- *`soft_skills`*: Array of soft skills (3-7 per employee)
- *`email_sentiment`*: Email tone analysis
- *`slack_activity`*: Chat platform usage
- *`meeting_participation`*: Meeting engagement
- *`goal_achievement_rate`*: Objective completion
- *`stress_level`*: Stress assessment (0-1)
- *`burnout_risk`*: Burnout probability (0-1)
- *`left_company`*: Boolean exit flag
- *`turnover_reason`*: Exit category (if applicable)
- *`risk_factors_summary`*: Low | Medium | High | Severe risk
- *`turnover_probability_generated`**: ML-predicted churn risk
- *`persona_name`*: Type of employee 
- *`role_complexity_score`*: Job difficulty rating
- *`career_progression_score`*: Growth trajectory
