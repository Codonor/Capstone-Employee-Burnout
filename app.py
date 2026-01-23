# streamlit_app.py
# --------------------------------------------------
# Purpose: Summarise EDA, statistics, and ML findings
# --------------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# -----------------------------
# App configuration
# -----------------------------
st.set_page_config(
    page_title="Employee Turnover Dashboard",
    layout="wide"
)

st.title("Employee Turnover Analysis")
st.markdown("""
This dashboard presents insights from a synthetic employee dataset.
It is designed for **non-technical readers**, combining statistics,
visual analysis, and machine learning results.
""")

# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/data_cleaned.csv")

df = load_data()

# -----------------------------
# Section 1: Overview metrics
# -----------------------------
st.header("1. Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total employees", len(df))

with col2:
    st.metric("Employees who left (%)", f"{df['left_company'].mean()*100:.1f}%")

with col3:
    st.metric("Avg satisfaction", f"{df['satisfaction_score'].mean():.2f}")

with col4:
    st.metric("Avg stress", f"{df['stress_level'].mean():.2f}")

st.markdown("""
**Summary:** Roughly one quarter of employees in the dataset have left the company.
Stress, burnout, and satisfaction are key themes explored below.
""")

# -----------------------------
# Section 2: Core statistics
# -----------------------------
st.header("2. Core statistical concepts")

stats_features = [
    'satisfaction_score',
    'stress_level',
    'burnout_risk'
]

stats_df = df[stats_features].agg(['mean', 'median', 'std']).T
st.dataframe(stats_df)

st.markdown("""
- **Mean**: average value across employees
- **Median**: typical employee (less sensitive to outliers)
- **Standard deviation**: how much values vary

These statistics help summarise employee wellbeing at a high level.
""")

# Distribution plot
fig, ax = plt.subplots()
sns.histplot(df['satisfaction_score'], kde=True, ax=ax)
ax.set_title("Distribution of Satisfaction Score")
st.pyplot(fig)

# -----------------------------
# Section 3: Who leaves the company?
# -----------------------------
st.header("3. Who leaves the company?")

fig, ax = plt.subplots()
sns.countplot(x='left_company', data=df, ax=ax)
ax.set_xticklabels(['Stayed', 'Left'])
ax.set_title("Employee Turnover Count")
st.pyplot(fig)

# Boxplots
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

sns.boxplot(x='left_company', y='satisfaction_score', data=df, ax=axes[0])
axes[0].set_title("Satisfaction vs Leaving")

sns.boxplot(x='left_company', y='stress_level', data=df, ax=axes[1])
axes[1].set_title("Stress vs Leaving")

sns.boxplot(x='left_company', y='burnout_risk', data=df, ax=axes[2])
axes[2].set_title("Burnout vs Leaving")

st.pyplot(fig)

st.markdown("""
Employees who leave generally report:
- **Lower satisfaction**
- **Higher stress**
- **Higher burnout risk**
""")

# -----------------------------
# Section 4: Feature relationships
# -----------------------------
st.header("4. Feature relationships")

corr_features = [
    'satisfaction_score', 'stress_level', 'burnout_risk',
    'workload_score', 'performance_score'
]

corr = df[corr_features].corr()

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
ax.set_title("Correlation between key features")
st.pyplot(fig)

st.markdown("""
Correlation analysis highlights relationships between wellbeing,
workload, and performance indicators.
""")

# -----------------------------
# Section 5: Machine learning model
# -----------------------------

st.header("5. Predicting employee turnover")

st.markdown("""
A **Random Forest classifier** was trained to predict whether an employee
will leave the company.

This model was chosen because it:
- Captures non-linear relationships
- Handles interactions between features
- Performs well with mixed behavioural signals
""")

# Define high-signal features
high_signal_features = [
    'burnout_risk',
    'stress_level',
    'satisfaction_score',
    'email_sentiment',
    'workload_score',
    'project_completion_rate',
    'collaboration_score',
    'meeting_participation'
]

X = df[high_signal_features]
y = df['left_company']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train Random Forest
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    class_weight='balanced_subsample',
    random_state=42
)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
ax.set_title("Confusion Matrix")
st.pyplot(fig)

st.text("Classification report:")
st.text(classification_report(y_test, y_pred))

st.markdown("""
**Interpretation:**
After applying class weighting, the model substantially improves recall for employees who leave, identifying approximately 63% of leavers. This improvement comes at the cost of a high false positive rate, with many employees incorrectly flagged as at risk.

This highlights a common trade-off in real-world HR attrition modelling: increasing sensitivity to leavers often results in more false alarms, requiring careful consideration of decision thresholds and business impact.
""")

# -----------------------------
# Section 6: Feature importance

# -----------------------------
st.header("6. Key drivers of turnover")

importances = pd.DataFrame({
    'feature': high_signal_features,
    'importance': rf.feature_importances_
}).sort_values(by='importance', ascending=True)

fig = px.bar(
    importances,
    x='importance',
    y='feature',
    orientation='h',
    title="Feature importance from Random Forest"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Section 7: Ethics & governance
# -----------------------------
st.header("7. Ethics, governance, and limitations")

st.markdown("""
- The dataset is **synthetic**, reducing privacy risks
- Real-world HR data may contain bias
- Predictions should **support**, not replace, human decision-making
- GDPR principles such as transparency and fairness must be considered
""")


