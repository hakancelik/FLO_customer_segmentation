import pandas as pd
df = pd.read_csv("data/processed/processed_data.csv")
rfm = pd.read_csv("data/processed/rfm_segment.csv")
rfm.head()

#RFM Analysis
rfm_analysis = rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])


#CASES
'''
# a. FLO is introducing a new women's shoe brand. 
# The product prices of the brand are above the general customer preferences. 
# Therefore, it is planned to contact customers who are likely to be interested in the promotion and sales of the brand. 
# These customers are expected to be loyal and have shopped in the women's category. 
# Save the customer IDs to a CSV file named new_brand_target_customer_ids.csv.
'''
target_segments_woman_customer_ids = rfm[rfm["segment"].isin(["champions","loyal_customers"])]["customer_id"]
cust_ids = df[(df["master_id"].isin(target_segments_woman_customer_ids)) & (df["interested_in_categories_12"].str.contains("KADIN"))]["master_id"]
cust_ids.to_csv("data/processed/new_brand_target__woman_customer_ids.csv", index=False)



'''
# b. A discount of nearly 40% is planned for men's and children's products.
# Customers who have previously shown interest in these categories but have not shopped for a long time,
# as well as new customers, are to be specifically targeted.
# Save the IDs of the suitable customers to a CSV file named discount_target_customer_ids.csv.
'''
target_segments_man_customer_ids = rfm[rfm["segment"].isin(["cant_loose","hibernating","new_customers"])]
cust_ids = df[(df["master_id"].isin(target_segments_man_customer_ids)) & ((df["interested_in_categories_12"].str.contains("ERKEK")) | (df["interested_in_categories_12"].str.contains("COCUK")))]["master_id"]
cust_ids.to_csv("data/processed/discount_target_customer_ids.csv", index=False)

