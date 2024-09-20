import pandas as pd
import datetime as dt
from config import DATASET_PATH


def create_rfm(dataframe):
    # Veriyi Hazırlma
    dataframe["order_num_total"] = (
        dataframe["order_num_total_ever_online"]
        + dataframe["order_num_total_ever_offline"]
    )
    dataframe["customer_value_total"] = (
        dataframe["customer_value_total_ever_offline"]
        + dataframe["customer_value_total_ever_online"]
    )
    date_columns = dataframe.columns[dataframe.columns.str.contains("date")]
    dataframe[date_columns] = dataframe[date_columns].apply(pd.to_datetime)

    # RFM METRIKLERININ HESAPLANMASI
    dataframe["last_order_date"].max()  # 2021-05-30
    analysis_date = dt.datetime(2021, 6, 1)
    rfm = pd.DataFrame()
    rfm["customer_id"] = dataframe["master_id"]
    rfm["recency"] = (analysis_date - dataframe["last_order_date"]).apply(
        lambda x: int(str(x).split()[0])
    )
    rfm["frequency"] = dataframe["order_num_total"]
    rfm["monetary"] = dataframe["customer_value_total"]

    # RF ve RFM SKORLARININ HESAPLANMASI
    rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])
    rfm["frequency_score"] = pd.qcut(
        rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]
    )
    rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])
    rfm["RF_SCORE"] = rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(
        str
    )
    rfm["RFM_SCORE"] = (
        rfm["recency_score"].astype(str)
        + rfm["frequency_score"].astype(str)
        + rfm["monetary_score"].astype(str)
    )

    # SEGMENTLERIN ISIMLENDIRILMESI
    seg_map = {
        r"[1-2][1-2]": "hibernating",
        r"[1-2][3-4]": "at_Risk",
        r"[1-2]5": "cant_loose",
        r"3[1-2]": "about_to_sleep",
        r"33": "need_attention",
        r"[3-4][4-5]": "loyal_customers",
        r"41": "promising",
        r"51": "new_customers",
        r"[4-5][2-3]": "potential_loyalists",
        r"5[4-5]": "champions",
    }
    rfm["segment"] = rfm["RF_SCORE"].replace(seg_map, regex=True)

    print("Dataset:")
    print(rfm.head())
    print("-" * 50)
    print("Dataset statistics:")
    print(rfm.describe())
    print("-" * 50)

    return rfm


if __name__ == "__main__":
    df = pd.read_csv(DATASET_PATH / "raw" / "flo_data_20K.csv")
    rfm_df = create_rfm(df)
    rfm_df.to_csv(DATASET_PATH / "processed" / "rfm_segment.csv", index=False)
