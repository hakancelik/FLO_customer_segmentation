import pandas as pd
import datetime as dt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.width',1000)

#reading data

df_ = pd.read_csv("data/raw/flo_data_20K.csv")
df = df_.copy()
df.head()

#data analysis
df.head(10)
df.columns
df.shape
df.describe().T
df.isnull().sum()
df.info()

#converting data types
date_columns = df.columns[df.columns.str.contains("date")]
df[date_columns] = df[date_columns].apply(pd.to_datetime)

df["order_num_total"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df["customer_value_total"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
df.info()
df.dtypes
df.to_csv("data/processed/processed_data.csv", index=False, date_format='%Y-%m-%d')

def data_prep(dataframe):
    dataframe["order_num_total"] = dataframe["order_num_total_ever_online"] + dataframe["order_num_total_ever_offline"]
    dataframe["customer_value_total"] = dataframe["customer_value_total_ever_offline"] + dataframe["customer_value_total_ever_online"]
    date_columns = dataframe.columns[dataframe.columns.str.contains("date")]
    dataframe[date_columns] = dataframe[date_columns].apply(pd.to_datetime)
    dataframe.to_csv("data/processed/processed_data.csv", index=False, date_format='%Y-%m-%d')
    return dataframe