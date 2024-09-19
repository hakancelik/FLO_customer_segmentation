import pandas as pd
import datetime as dt

df = pd.read_csv("data/processed/processed_data.csv")
date_columns = df.columns[df.columns.str.contains("date")]
df[date_columns] = df[date_columns].apply(pd.to_datetime)
df.dtypes

# 5. Examine the distribution of the number of customers, total number of products purchased, and total expenditures across shopping channels.
df.groupby("order_channel").agg({"master_id":"count",
                                "order_num_total":"sum",
                                "customer_value_total":"sum"})

# 6. Find the top 10 customers with the highest revenue.

df.sort_values("customer_value_total", ascending=False)[:10]

# 7. Find the top 10 customers with the highest number of orders.

df.sort_values("order_num_total", ascending=False)[:10]

#Analysis Date
df["last_order_date"].max() # 2021-05-30
analysis_date = dt.datetime(2021,6,1)

#RFM Metrics
rfm = pd.DataFrame()
rfm["customer_id"] = df["master_id"]
rfm["recency"] = (analysis_date - df["last_order_date"]).dt.days
rfm["frequency"] = df["order_num_total"]
rfm["monetary"] = df["customer_value_total"]
# RFM verisini kaydet
rfm.to_csv("data/processed/rfm_data.csv", index=False)

rfm.head()