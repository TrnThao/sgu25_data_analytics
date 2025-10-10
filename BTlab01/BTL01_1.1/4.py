import numpy as np
import pandas as pd
from scipy import stats

diabetes_data = pd.read_csv("diabetes.csv")

# Ở đây chọn cột Glucose
col = "Glucose"

# Tính toán thống kê mô tả chi tiết glucose
data_mean = np.nanmean(diabetes_data[col])
data_median = np.nanmedian(diabetes_data[col])
data_mode = stats.mode(diabetes_data[col], nan_policy='omit', keepdims=False).mode
data_variance = np.nanvar(diabetes_data[col])
data_sd = np.nanstd(diabetes_data[col])
data_max = np.nanmax(diabetes_data[col])
data_min = np.nanmin(diabetes_data[col])
data_range = data_max - data_min
data_percentile_60 = np.nanpercentile(diabetes_data[col], 60)
q1 = np.nanquantile(diabetes_data[col], 0.25)
q3 = np.nanquantile(diabetes_data[col], 0.75)
data_IQR = stats.iqr(diabetes_data[col], nan_policy='omit')

# --- In kết quả chi tiết ---
print(f"\nTHONG KE CHI TIET")
print(f"Quantity: {len(diabetes_data[col])}")
print(f"Mean: {data_mean:.2f}")
print(f"Median: {data_median:.2f}")
print(f"Mode: {data_mode}")
print(f"Variance: {data_variance:.2f}")
print(f"Sd: {data_sd:.2f}")
print(f"Min: {data_min:.2f}, Max: {data_max:.2f}, Range: {data_range:.2f}")
print(f"60th Percentile: {data_percentile_60:.2f}")
print(f"Q1 (25%): {q1:.2f}, Q3 (75%): {q3:.2f}")
print(f"IQR: {data_IQR:.2f}")