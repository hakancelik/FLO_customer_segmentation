# FLO RFM Analysis Report

## About the Project

This project was conducted to perform customer segmentation and RFM (Recency, Frequency, Monetary) analysis for FLO company. The analysis will help the company better understand customer behaviors and develop targeted marketing strategies.

## Data Set Examination

Before starting the analysis, we thoroughly examined our dataset. Here are the general characteristics of our dataset:

### Dataset Size
The size of our dataset: {df.shape[0]} rows and {df.shape[1]} columns

### Columns
The columns in our dataset were listed using the {df.columns.to_list()} .

### First 10 Rows
The first 10 rows of the dataset  {df.head(10)}
The last 10 rows of the dataset  {df.tail(10)}

### Data Types
The data types of the columns are as follows:
{df.dtypes}

### Categorical Columns
The categorical columns in our dataset are:
{df.select_dtypes(include=['object']).columns.to_list()}

### Numerical Columns
The numerical columns in our dataset are:
{df.select_dtypes(include=['int64', 'float64']).columns.to_list()}


### Descriptive Statistics
We examined the descriptive statistics of the numerical variables 
 {df.describe().T} 

### Missing Data Analysis
We examined the missing values in the dataset and it has {df.isnull().sum()} missing values. This analysis helped us determine which columns to focus on during the data cleaning phase.

### Dataset Information
We examined the data type and number of non-null values for each column in the dataset using the {df.info()}

## Data Preparation and RFM Metrics

After examining the dataset, the metrics necessary for RFM analysis were calculated:

- Recency (R): Number of days since the customer's last purchase
- Frequency (F): Total number of orders by the customer
- Monetary (M): Total amount spent by the customer

Using these metrics, RFM scores were created for each customer, and customers were divided into segments.

## Channel Performance Analysis

![Channel Performance](media/channel_performance.png)

The above graph shows the performance of different sales channels. The performance of each channel can be compared in terms of number of customers, total number of orders, and total revenue.

## RFM Score Distribution

![RFM Score Distribution](media/rfm_score_distribution.png)

This histogram shows the distribution of customers' RFM scores. Areas where scores are concentrated provide insight into general customer behaviors.

## Segment Distribution

![Segment Distribution](media/segment_distribution.png)

This graph shows how customers are distributed across different segments. The size of each segment provides information about the structure of the company's customer base.

## Correlation Matrix

![Correlation Matrix](media/correlation_matrix.png)

The correlation matrix shows the relationships between RFM metrics. This helps us understand which metrics are more closely related to each other.

## Customer Behavior Analysis

![Customer Behavior Analysis](media/customer_behavior_analysis.png)

This scatter plot shows the Recency and Monetary values of customers. Different colors represent different segments and visualize patterns in customer behaviors.

## RFM Segmentation Results

![RFM Segmentation Results](media/rfm_segmentation_results.png)

This graph shows the results of RFM segmentation in terms of Recency and Frequency. Each point represents a customer, and its color indicates which segment it belongs to.

## Conclusion and Recommendations

As a result of the RFM analysis, our customers have been divided into various segments. This segmentation will allow us to personalize our marketing strategies and develop specific approaches for each customer group.

Recommendations:
1. Loyalty programs can be developed for customers in the "Champions" segment.
2. Special campaigns can be organized for "At Risk" customers.
3. Personalized offers can be presented to regain "Can't Lose" customers.
4. Product variety can be increased and cross-selling strategies can be applied for the "New Customers" segment.

Regular repetition of this analysis and continuous evaluation of the results will contribute to the continuous improvement of our customer relationship management strategies.