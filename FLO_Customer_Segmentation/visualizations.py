import pandas as pd
import datetime as dt

df = pd.read_csv("data/processed/processed_data.csv")
rfm = pd.read_csv("data/processed/rfm_segment.csv")
# Channel performance
channel_performance = df.groupby("order_channel").agg({
    "master_id": "count",  # Number of customers
    "order_num_total_ever_online": "sum",  # Total number of online orders
    "order_num_total_ever_offline": "sum",  # Total number of offline orders
    "customer_value_total_ever_online": "sum",  # Total online spending
    "customer_value_total_ever_offline": "sum"  # Total offline spending
}).reset_index()

channel_performance.to_csv("data/processed/channel_performance.csv", index=False)

import matplotlib.pyplot as plt
import seaborn as sns

# Number of Customers by Channel
plt.figure(figsize=(12, 6))
sns.barplot(data=channel_performance, x='order_channel', y='master_id', palette='viridis')
plt.title('Number of Customers by Channel')
plt.xlabel('Sales Channel')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.savefig("reports/media/channel_performance.png")

# RFM Score Distribution
plt.figure(figsize=(12, 6))
sns.histplot(rfm['RFM_SCORE'].value_counts(), bins=10, kde=True)
plt.title('RFM Score Distribution')
plt.xlabel('RFM Score')
plt.ylabel('Number of Customers')
plt.savefig("reports/media/rfm_score_distribution.png")

# Segment Distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=rfm, x='segment', order=rfm['segment'].value_counts().index)
plt.title('Distribution of Customer Segments')
plt.xlabel('Segment')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.savefig("reports/media/segment_distribution.png")

# Recency vs Frequency
plt.figure(figsize=(12, 6))
sns.scatterplot(x='recency', y='frequency', hue='segment', data=rfm)
plt.title('Recency vs Frequency')
plt.savefig("reports/media/recency_frequency_scatter.png")
plt.close()

# Monetary Distribution
plt.figure(figsize=(12, 6))
sns.boxplot(x='segment', y='monetary', data=rfm)
plt.title('Monetary Distribution by Segment')
plt.savefig("reports/media/monetary_distribution.png")
plt.close()

# Correlation Matrix
correlation_matrix = rfm[['recency', 'frequency', 'monetary', 'recency_score', 'frequency_score', 'monetary_score']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.savefig("reports/media/correlation_matrix.png")

# Customer Behavior Analysis
plt.figure(figsize=(12, 8))
sns.scatterplot(data=rfm, x='recency', y='monetary', hue='segment', palette='Set1')
plt.title('Recency vs Monetary')
plt.xlabel('Recency (Days)')
plt.ylabel('Monetary (Total Spending)')
plt.legend(title='Segment')
plt.savefig("reports/media/customer_behavior_analysis.png")

# Clustering Results
# RFM Segmentation Analysis
plt.figure(figsize=(12, 8))
sns.scatterplot(data=rfm, x='recency', y='frequency', hue='segment', palette='Set2')
plt.title('RFM Segmentation Results: Recency and Frequency')
plt.xlabel('Recency (Days)')
plt.ylabel('Frequency (Number of Orders)')
plt.legend(title='Segment')
plt.savefig("reports/media/rfm_segmentation_results.png")
