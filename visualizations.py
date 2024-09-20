import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import DATASET_PATH


def get_channel_performance(df, save=False):
    channel_performance = (
        df.groupby("order_channel")
        .agg(
            {
                "master_id": "count",
                "order_num_total_ever_online": "sum",
                "order_num_total_ever_offline": "sum",
                "customer_value_total_ever_online": "sum",
                "customer_value_total_ever_offline": "sum",
            }
        )
        .reset_index()
    )
    if save:
        channel_performance.to_csv(
            "data/processed/channel_performance.csv", index=False
        )
    return channel_performance


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_csv(DATASET_PATH / "processed" / "processed_data.csv")
    rfm = pd.read_csv(DATASET_PATH / "processed" / "rfm_segment.csv")
    return df, rfm


def plot_number_of_customers_by_channel(channel_performance, save=True):
    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=channel_performance, x="order_channel", y="master_id", palette="viridis", hue="order_channel", legend=False
    )
    plt.title("Number of Customers by Channel")
    plt.xlabel("Sales Channel")
    plt.ylabel("Number of Customers")
    plt.xticks(rotation=45)
    if save:
        plt.savefig("reports/media/channel_performance.png")
    else:
        plt.show()


def plot_rfm_score_dist(rfm, save=True):
    plt.figure(figsize=(12, 6))
    sns.histplot(rfm["RFM_SCORE"].value_counts(), bins=10, kde=True)
    plt.title("RFM Score Distribution")
    plt.xlabel("RFM Score")
    plt.ylabel("Number of Customers")
    if save:
        plt.savefig("reports/media/rfm_score_distribution.png")
    else:
        plt.show()


def plot_segment_dist(rfm, save=True):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=rfm, x="segment", order=rfm["segment"].value_counts().index)
    plt.title("Distribution of Customer Segments")
    plt.xlabel("Segment")
    plt.ylabel("Number of Customers")
    plt.xticks(rotation=45)
    if save:
        plt.savefig("reports/media/segment_distribution.png")
    else:
        plt.show()


def plot_recency_frequency(rfm, save=True):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x="recency", y="frequency", hue="segment", data=rfm)
    plt.title("Recency vs Frequency")
    if save:
        plt.savefig("reports/media/recency_frequency_scatter.png")
    else:
        plt.show()


def plot_monetary_distribution(rfm, save=True):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x="segment", y="monetary", data=rfm)
    plt.title("Monetary Distribution by Segment")
    if save:
        plt.savefig("reports/media/monetary_distribution.png")
    else:
        plt.show()


def plot_correlation_matrix(rfm, save=True):
    correlation_matrix = rfm[
        [
            "recency",
            "frequency",
            "monetary",
            "recency_score",
            "frequency_score",
            "monetary_score",
        ]
    ].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    if save:
        plt.savefig("reports/media/correlation_matrix.png")
    else:
        plt.show()


def plot_customer_behavior_analysis(rfm, save=True):
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=rfm, x="recency", y="monetary", hue="segment", palette="Set1")
    plt.title("Recency vs Monetary")
    plt.xlabel("Recency (Days)")
    plt.ylabel("Monetary (Total Spending)")
    plt.legend(title="Segment")
    if save:
        plt.savefig("reports/media/customer_behavior_analysis.png")
    else:
        plt.show()


def plot_rfm_segmentation_results(rfm, save=True):
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=rfm, x="recency", y="frequency", hue="segment", palette="Set2")
    plt.title("RFM Segmentation Results: Recency and Frequency")
    plt.xlabel("Recency (Days)")
    plt.ylabel("Frequency (Number of Orders)")
    plt.legend(title="Segment")
    if save:
        plt.savefig("reports/media/rfm_segmentation_results.png")
    else:
        plt.show()


if __name__ == "__main__":
    df, rfm = load_data()
    channel_performance = get_channel_performance(df, save=True)

    plot_number_of_customers_by_channel(channel_performance)
    plot_rfm_score_dist(rfm)
    plot_segment_dist(rfm)
    plot_recency_frequency(rfm)
    plot_monetary_distribution(rfm)
    plot_correlation_matrix(rfm)
    plot_customer_behavior_analysis(rfm)
    plot_rfm_segmentation_results(rfm)
