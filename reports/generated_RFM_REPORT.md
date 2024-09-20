# FLO RFM Analysis Report

## About the Project

This project was conducted to perform customer segmentation and RFM (Recency, Frequency, Monetary) analysis for the FLO company. The analysis will help the company better understand customer behavior and develop targeted marketing strategies.

## Data Set Examination

Before starting the analysis, a thorough examination of the dataset was performed. Below are the general characteristics of the dataset:

### Dataset Size
The dataset size: 19945 rows and 10 columns

### Columns
The columns in the dataset are listed as follows:
customer_id, recency, frequency, monetary, recency_score, frequency_score, monetary_score, RF_SCORE, RFM_SCORE, segment

### First 10 Rows of the Dataset
| customer_id                          |   recency |   frequency |   monetary |   recency_score |   frequency_score |   monetary_score |   RF_SCORE |   RFM_SCORE |   segment |
|:-------------------------------------|----------:|------------:|-----------:|----------------:|------------------:|-----------------:|-----------:|------------:|----------:|
| cc294636-19f0-11eb-8d74-000d3a38a36f |        95 |           5 |     939.37 |               3 |                 4 |                4 |         34 |         344 |       344 |
| f431bd5a-ab7b-11e9-a2fc-000d3a38a36f |       105 |          21 |    2013.55 |               3 |                 5 |                5 |         35 |         355 |       355 |
| 69b69676-1a40-11ea-941b-000d3a38a36f |       186 |           5 |     585.32 |               2 |                 4 |                3 |         24 |         243 |       243 |
| 1854e56c-491f-11eb-806e-000d3a38a36f |       135 |           2 |     121.97 |               3 |                 1 |                1 |         31 |         311 |       311 |
| d6ea1074-f1f5-11e9-9346-000d3a38a36f |        86 |           2 |     209.98 |               3 |                 1 |                1 |         31 |         311 |       311 |

---

### Last 10 Rows of the Dataset  
| customer_id                          |   recency |   frequency |   monetary |   recency_score |   frequency_score |   monetary_score |   RF_SCORE |   RFM_SCORE |   segment |
|:-------------------------------------|----------:|------------:|-----------:|----------------:|------------------:|-----------------:|-----------:|------------:|----------:|
| 727e2b6e-ddd4-11e9-a848-000d3a38a36f |       331 |           3 |     401.96 |               1 |                 3 |                2 |         13 |         132 |       132 |
| 25cd53d4-61bf-11ea-8dd8-000d3a38a36f |       161 |           2 |     390.47 |               2 |                 2 |                2 |         22 |         222 |       222 |
| 8aea4c2a-d6fc-11e9-93bc-000d3a38a36f |         8 |           3 |     632.94 |               5 |                 3 |                3 |         53 |         533 |       533 |
| e50bb46c-ff30-11e9-a5e8-000d3a38a36f |       108 |           6 |    1009.77 |               3 |                 4 |                4 |         34 |         344 |       344 |
| 740998d2-b1f7-11e9-89fa-000d3a38a36f |       360 |           2 |     261.97 |               1 |                 2 |                1 |         12 |         121 |       121 |

---

### Data Types
The data types of the columns are as follows:
|    | Column          | Data Type   |
|---:|:----------------|:------------|
|  0 | customer_id     | object      |
|  1 | recency         | int64       |
|  2 | frequency       | float64     |
|  3 | monetary        | float64     |
|  4 | recency_score   | int64       |
|  5 | frequency_score | int64       |
|  6 | monetary_score  | int64       |
|  7 | RF_SCORE        | int64       |
|  8 | RFM_SCORE       | int64       |
|  9 | segment         | int64       |

---

### Categorical Columns
The categorical columns in the dataset are:
['customer_id']

---

### Numerical Columns
The numerical columns in the dataset are:
['recency', 'frequency', 'monetary', 'recency_score', 'frequency_score', 'monetary_score', 'RF_SCORE', 'RFM_SCORE', 'segment']

---

### Descriptive Statistics
Descriptive statistics of the numerical variables were examined:
|                 |   count |      mean |       std |    min |    25% |    50% |    75% |     max |
|:----------------|--------:|----------:|----------:|-------:|-------:|-------:|-------:|--------:|
| recency         |   19945 | 134.458   | 103.281   |   2    |  43    | 111    | 202    |   367   |
| frequency       |   19945 |   5.02477 |   4.74271 |   2    |   3    |   4    |   6    |   202   |
| monetary        |   19945 | 751.244   | 895.402   |  44.98 | 339.98 | 545.27 | 897.78 | 45905.1 |
| recency_score   |   19945 |   3.00978 |   1.42011 |   1    |   2    |   3    |   4    |     5   |
| frequency_score |   19945 |   3       |   1.41425 |   1    |   2    |   3    |   4    |     5   |
| monetary_score  |   19945 |   2.9999  |   1.41421 |   1    |   2    |   3    |   4    |     5   |
| RF_SCORE        |   19945 |  33.0978  |  14.4536  |  11    |  22    |  33    |  45    |    55   |
| RFM_SCORE       |   19945 | 333.978   | 144.859   | 111    | 221    | 333    | 454    |   555   |
| segment         |   19945 | 333.978   | 144.859   | 111    | 221    | 333    | 454    |   555   |


---

### Missing Data Analysis
The dataset was examined for missing values, and there are
There are no missing values in the dataset. 
missing values. This analysis helped identify which columns needed attention during the data cleaning process.

### Dataset Information
The data types and the number of non-null values for each column were analyzed:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 19945 entries, 0 to 19944
Data columns (total 10 columns):
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----  
 0   customer_id      19945 non-null  object 
 1   recency          19945 non-null  int64  
 2   frequency        19945 non-null  float64
 3   monetary         19945 non-null  float64
 4   recency_score    19945 non-null  int64  
 5   frequency_score  19945 non-null  int64  
 6   monetary_score   19945 non-null  int64  
 7   RF_SCORE         19945 non-null  int64  
 8   RFM_SCORE        19945 non-null  int64  
 9   segment          19945 non-null  int64  
dtypes: float64(2), int64(7), object(1)
memory usage: 1.5+ MB


---

## Data Preparation and RFM Metrics

After examining the dataset, the necessary metrics for RFM analysis were calculated:

- Recency (R): The number of days since the customer's last purchase
- Frequency (F): The total number of orders placed by the customer
- Monetary (M): The total amount spent by the customer

Using these metrics, RFM scores were created for each customer, and customers were segmented into different groups.

## Channel Performance Analysis

![Channel Performance](https://github.com/hakancelik/FLO_customer_segmentation/blob/a5b26c950124d90af90fb11756fb9e44c622b8e2/FLO_Customer_Segmentation/reports/media/channel_performance.png)

The graph above shows the performance of various sales channels. Each channel's performance can be compared in terms of the number of customers, total orders, and total revenue.

## RFM Score Distribution

![RFM Score Distribution](https://github.com/hakancelik/FLO_customer_segmentation/blob/a5b26c950124d90af90fb11756fb9e44c622b8e2/FLO_Customer_Segmentation/reports/media/rfm_score_distribution.png)

This histogram displays the distribution of customers' RFM scores. Areas where the scores are concentrated offer insights into general customer behavior patterns.

## Segment Distribution

![Segment Distribution](https://github.com/hakancelik/FLO_customer_segmentation/blob/a5b26c950124d90af90fb11756fb9e44c622b8e2/FLO_Customer_Segmentation/reports/media/segment_distribution.png)

This graph illustrates how customers are distributed across various segments. The size of each segment provides information about the structure of the company's customer base.

## Correlation Matrix

![Correlation Matrix](https://github.com/hakancelik/FLO_customer_segmentation/blob/a5b26c950124d90af90fb11756fb9e44c622b8e2/FLO_Customer_Segmentation/reports/media/correlation_matrix.png)

The correlation matrix highlights the relationships between the RFM metrics, helping to understand which metrics are more closely related to one another.

## Customer Behavior Analysis

![Customer Behavior Analysis](https://github.com/hakancelik/FLO_customer_segmentation/blob/a5b26c950124d90af90fb11756fb9e44c622b8e2/FLO_Customer_Segmentation/reports/media/customer_behavior_analysis.png)

This scatter plot shows the Recency and Monetary values of customers. Different colors represent different segments, helping to visualize customer behavior patterns.

## RFM Segmentation Results

![RFM Segmentation Results](https://github.com/hakancelik/FLO_customer_segmentation/blob/a5b26c950124d90af90fb11756fb9e44c622b8e2/FLO_Customer_Segmentation/reports/media/rfm_segmentation_results.png)

This graph illustrates the results of the RFM segmentation in terms of Recency and Frequency. Each point represents a customer, and the color indicates their segment.

## Conclusion and Recommendations

As a result of the RFM analysis, customers have been divided into various segments. This segmentation will allow for more personalized marketing strategies and the development of specific approaches for each customer group.

Recommendations:
1. Loyalty programs can be designed for customers in the "Champions" segment.
2. Special campaigns can be organized for "At Risk" customers.
3. Personalized offers can be provided to retain "Can't Lose" customers.
4. Product variety can be increased, and cross-selling strategies can be applied for the "New Customers" segment.

Repeating this analysis regularly and continuously evaluating the results will contribute to the improvement of customer relationship management strategies.

---
