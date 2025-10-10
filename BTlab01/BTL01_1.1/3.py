# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from scipy import stats

wine_data = pd.read_csv("winequality-red.csv")

# Chọn cột quality
col = "quality"

#Tính toán thống kê mô tả 
data_mean = np.nanmean(wine_data[col])
data_median = np.nanmedian(wine_data[col])
data_mode = stats.mode(wine_data[col], nan_policy='omit', keepdims=False).mode
data_variance = np.nanvar(wine_data[col])
data_sd = np.nanstd(wine_data[col])
data_max = np.nanmax(wine_data[col])
data_min = np.nanmin(wine_data[col])
data_range = data_max - data_min
data_percentile_60 = np.nanpercentile(wine_data[col], 60)
q1 = np.nanquantile(wine_data[col], 0.25)
q3 = np.nanquantile(wine_data[col], 0.75)
data_IQR = stats.iqr(wine_data[col], nan_policy='omit')

print("\nTHONG KE MO TA CHAT LUONG RUOU DO")
print(f"Quantity: {wine_data.shape[0]}")
print(f"Mean: {data_mean:.2f}")
print(f"Median: {data_median:.2f}")
print(f"Mode: {data_mode}")
print(f"Variance: {data_variance:.2f}")
print(f"Sd: {data_sd:.2f}")
print(f"Min: {data_min:.2f}, Max: {data_max:.2f}, Range: {data_range:.2f}")
print(f"60th Percentile: {data_percentile_60:.2f}")
print(f"Q1 (25%): {q1:.2f}, Q3 (75%): {q3:.2f}")
print(f"IQR: {data_IQR:.2f}")