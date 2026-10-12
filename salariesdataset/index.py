import pandas as pd
import numpy as np
df=pd.read_csv('Salaries.csv')
# print(df.head(10))
# print(df.tail(10))
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())

# df=df.drop(['Status','Id','Notes','Agency'], axis=1)
# print(df.head())
# ovrall statistics is provided by describe method:
# print(df.describe(()))
# print(df['EmployeeName'].value_counts().head(5))
# print(df['JobTitle'].value_counts().head(5))
# print(df['JobTitle'].str.contains('CAPTAIN').count())
# print(df[df['JobTitle'].str.contains('Fire',case=False)])
print(df.columns)
# print(df['BasePay'].mean())
# print(df['BasePay'].min())
# print(df['BasePay'].max())
# df['EmployeeName']=df['EmployeeName'].replace(' Not provided',np.nan)
# print("Jobtitle of albert pardini here:")
# print(df[df['EmployeeName']=='ALBERT PARDINI']['JobTitle'])
# print(df[df['EmployeeName']=='ALBERT PARDINI']['TotalPayBenefits'])
# name of person highest basePay:
# print(df[df['BasePay'].max()==df['BasePay']]['EmployeeName'])
# grp_val=df[['Year','BasePay']].groupby('Year').mean()  
# grp_val=df[['JobTitle','BasePay']].groupby('JobTitle').mean()  
# print(grp_val)
single_val=df[df['JobTitle']=='ACCOUNTANT']['BasePay'].mean() 
print(single_val)
print(df['JobTitle'].value_counts().head(5))
 
# print(df.groupby('JobTitle').mean()['BasePay'])

# print(df['BasePay'].value_counts())