import pandas as pd
import datetime as dt

rfm = pd.read_csv("data/processed/rfm_data.csv")

#Calculate RF and RFM Scores
rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5,4,3,2,1])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1,2,3,4,5])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1,2,3,4,5])

rfm.head()

# Recency and Frequency Scores as a Single Variable
rfm["RF_SCORE"] = (rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str))

# Recency, Frequency, and Monetary Scores as a Single Variable
rfm["RFM_SCORE"] = (rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str) + rfm["monetary_score"].astype(str))
rfm.head()

rfm.to_csv("data/processed/rfm_scores.csv", index=False)