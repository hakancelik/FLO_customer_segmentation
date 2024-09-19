import pandas as pd
from jinja2 import Environment, FileSystemLoader
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
from io import StringIO

# Yardımcı fonksiyonlar
def format_describe(dataframe):
    return dataframe.describe().T.to_markdown() + "\n"

def format_data_types(dataframe):
    return dataframe.dtypes.reset_index().rename(columns={'index': 'Column', 0: 'Data Type'}).to_markdown()

def get_data_info(dataframe):
    buffer = StringIO()
    dataframe.info(buf=buffer)
    return buffer.getvalue()

def format_missing_data(dataframe):
    missing = dataframe.isnull().sum()
    missing = missing[missing > 0]
    
    if missing.empty:
        return "There are no missing values in the dataset."
    
    formatted_missing = missing.reset_index()
    formatted_missing.columns = ['Variable', 'Number of Missing Values']
    
    return formatted_missing.to_markdown(index=False)

# Sütunları daha okunabilir hale getirmek için formatlama fonksiyonu ekleyin
def format_columns(columns):
    return ', '.join(columns)  # Sütunları virgülle ayırarak birleştir

# Veri yükleme
df = pd.read_csv("data/processed/rfm_segment.csv")  # Yolu güncelledim

# Temel istatistikler
df_shape = df.shape
df_head = df.head().to_markdown(index=False)
df_tail = df.tail().to_markdown(index=False)
describe_data = format_describe(df)
data_types = format_data_types(df)
data_info = get_data_info(df)
missing_data = format_missing_data(df)

categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Grafikler
plt.figure(figsize=(10, 6))
sns.histplot(df['RFM_SCORE'], kde=True)
plt.title('RFM Score Distribution')
plt.savefig('reports/media/rfm_score_distribution.png')  # Yolu güncelledim
plt.close()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='segment', order=df['segment'].value_counts().index)
plt.title('Segment Distribution')
plt.xticks(rotation=45)
plt.savefig('reports/media/segment_distribution.png')  # Yolu güncelledim
plt.close()

correlation_matrix = df[['recency', 'frequency', 'monetary', 'recency_score', 'frequency_score', 'monetary_score']].corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.savefig('reports/media/correlation_matrix.png')  # Yolu güncelledim
plt.close()

# Eksik olan diğer grafikleri de oluşturun
# Channel Performance
# Customer Behavior Analysis
# RFM Segmentation Results

# Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))  # Yolu güncelledim
template = env.get_template('RFM_REPORT.md')  # Yolu güncelledim

# Dinamik veri aktarımı
project_data = {
    'project_name': 'FLO RFM Analysis',
    'obs_count': df_shape[0],
    'var_count': df_shape[1],
    'data_columns': format_columns(df.columns.tolist()),  # Sütunları formatla
    'data_head': df_head,
    'data_tail': df_tail,
    'data_types': data_types,
    'categorical_columns': categorical_columns,
    'numerical_columns': numerical_columns,
    'describe_data': describe_data,
    'missing_data': missing_data,
    'data_info': data_info,
    'channel_performance_image': 'reports/media/channel_performance.png',
    'rfm_score_distribution_image': 'reports/media/rfm_score_distribution.png',
    'segment_distribution_image': 'reports/media/segment_distribution.png',
    'correlation_matrix_image': 'reports/media/correlation_matrix.png',
    'customer_behavior_analysis_image': 'reports/media/customer_behavior_analysis.png',
    'rfm_segmentation_results_image': 'reports/media/rfm_segmentation_results.png',
}

# Şablonu doldur
output = template.render(project_data)

# Çıktıyı dosyaya yaz
with open('reports/generated_RFM_REPORT.md', 'w') as f:  # Yolu güncelledim
    f.write(output)

print("RFM Report successfully generated!")