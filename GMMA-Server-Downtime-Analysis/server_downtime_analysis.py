"""
Global Motor Manufacturers Australia - Server Fail Log Analysis
Fujitsu Service Delivery Team - Server Refresh Project

Tasks:
1. Plot the fail log data
2. Build a predictive model (train = Jul-Nov, test = Dec)
3. Validate with MAE
4. (Recommendations documented in the accompanying report)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error

# ---- Load data ----
df = pd.read_excel("Task_Data__Server_Down_Data.xlsx", sheet_name="Fail Logs")
df = df.dropna(subset=["Asset ID"]).copy()
df["Fail Date"] = pd.to_datetime(df["Fail Date"])
month_order = ["July", "August", "September", "October", "November", "December"]
df["Fail Month"] = pd.Categorical(df["Fail Month"], categories=month_order, ordered=True)

# ---- Task 1: Visualise current state ----
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
monthly = df.groupby("Fail Month", observed=True)["Downtime (Min)"].sum().reindex(month_order)
axes[0, 0].bar(monthly.index, monthly.values, color="#2E5EAA")
axes[0, 0].set_title("Total Downtime (Min) by Month")

counts = df.groupby("Fail Month", observed=True).size().reindex(month_order)
axes[0, 1].bar(counts.index, counts.values, color="#C0504D")
axes[0, 1].set_title("Number of Fail Incidents by Month")

cause = df.groupby("Event Notes")["Downtime (Min)"].sum().sort_values()
axes[1, 0].barh(cause.index, cause.values, color="#9BBB59")
axes[1, 0].set_title("Total Downtime (Min) by Failure Cause")

office = df.groupby("Office")["Downtime (Min)"].sum().sort_values()
axes[1, 1].barh(office.index, office.values, color="#8064A2")
axes[1, 1].set_title("Total Downtime (Min) by Office")
plt.tight_layout()
plt.savefig("task1_fail_logs_plot.png", dpi=150)

# ---- Task 2: Predictive model, train/test split (December = test) ----
train = df[df["Fail Month"] != "December"]
test = df[df["Fail Month"] == "December"]
features = ["Office", "Event Notes"]
target = "Downtime (Min)"

preprocess = ColumnTransformer([("cat", OneHotEncoder(handle_unknown="ignore"), features)])
rf_pipe = Pipeline([("prep", preprocess), ("model", RandomForestRegressor(n_estimators=300, random_state=42))])
rf_pipe.fit(train[features], train[target])
pred = rf_pipe.predict(test[features])

# ---- Task 3: Validate with MAE ----
mae = mean_absolute_error(test[target], pred)
print(f"Random Forest MAE on December test set: {mae:.1f} minutes (target: < 30 minutes)")

results = test[["Office", "Fail Date", "Event Notes", "Downtime (Min)"]].copy()
results["Predicted (min)"] = pred.round(1)
results["Abs Error (min)"] = (results["Downtime (Min)"] - results["Predicted (min)"]).abs().round(1)
print(results.to_string(index=False))
