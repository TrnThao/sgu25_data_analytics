import numpy as np
import pandas as pd
from scipy import stats
# Load the .csv into a dataframe using read_csv
covid_data = pd.read_csv("covid-data.csv")
covid_data = covid_data[['Entity','Day',"Cumulative excess deaths per 100,000 people (central estimate)","Cumulative excess deaths per 100,000 people (95% CI, lower bound)","Cumulative excess deaths per 100,000 people (95% CI, upper bound)","Total confirmed deaths due to COVID-19 per 100,000 people"]]
# Take a quick look at the data
covid_data.head(5)
covid_data.dtypes
covid_data.shape
# Get the mean of the data
data_mean = np.nanmean(covid_data["Total confirmed deaths due to COVID-19 per 100,000 people"])
# Get the median of the data
data_median = np.nanmedian(covid_data["Total confirmed deaths due to COVID-19 per 100,000 people"])
# Get the mode of the data
data_mode = stats.mode(covid_data["Total confirmed deaths due to COVID-19 per 100,000 people"], nan_policy='omit', keepdims=False).mode
# Obtain the variance of the data
data_variance = np.nanvar(covid_data["Total confirmed deaths due to COVID-19 per 100,000 people"])
# Obtain the standard deviation of the data
data_sd = np.nanstd(covid_data["Total confirmed deaths due to COVID-19 per 100,000 people"])
# Compute the maximum and minimum values of the data
data_max = np.nanmax(covid_data["Total confirmed deaths due to COVID-19 per 100,000 people"])
data_min = np.nanmin(covid_data["Total confirmed deaths due to COVID-19 per 100,000 people"])
# Obtain the 60th percentile of the data
data_percentile = np.nanpercentile(covid_data["Total confirmed deaths due to COVID-19 per 100,000 people"], 60)
# Obtain the quartiles of the data
data_quartile = np.nanquantile(covid_data["Total confirmed deaths due to COVID-19 per 100,000 people"], 0.75)
# Get the IQR of the data
data_IQR = stats.iqr(covid_data["Total confirmed deaths due to COVID-19 per 100,000 people"], nan_policy='omit')
print("Mean: ", data_mean )
print("Median: ", data_median )
print("Mode: ", data_mode )
print("Variance: ", data_variance)
print("Sd: ", data_sd)
print("Max: ", data_max)
print("Min: ", data_min)
print("Percentile: ", data_percentile)
print("Quartile: ", data_quartile)
print("IQR: ", data_IQR)