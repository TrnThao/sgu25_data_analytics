import pandas as pd
marketing_data = pd.read_csv("marketing_campaign.csv", sep="\t")
marketing_data = marketing_data[['ID','Year_Birth', 'Education',
'Marital_Status','Income','Kidhome', 'Teenhome',
'Dt_Customer', 'Recency','NumStorePurchases',
'NumWebVisitsMonth']]
marketing_data.head()
# Remove duplicates across the columns in our dataset:
marketing_data.drop_duplicates(subset='ID', keep='first',inplace=True)
# Delete a specified row at index value 1:
marketing_data.drop(labels=[1], axis=0, inplace=True)
# Delete a single column
marketing_data.drop(labels=['Year_Birth'], axis=1, inplace=True)
print(marketing_data.head())
# Replace the values in Teenhome with has teen and has no teen
marketing_data['Teenhome'] = marketing_data['Teenhome'].replace([0,1,2],['has no teen','has teen','has teen'])
# Fill NAs in the Income column
marketing_data['Income'] = marketing_data['Income'].fillna(0)
# Change the data type of the Income column from float to int
marketing_data['Income'] = marketing_data['Income'].astype(int)
print(marketing_data.head())
# Check for missing values using the isnull and sum methods
print(marketing_data.isnull().sum())
# Drop missing values using the dropna method
marketing_data = marketing_data.dropna(how = 'any')
marketing_data.shape