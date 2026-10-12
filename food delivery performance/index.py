import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Ecommerce Purchases.csv')
# print(df)
# print(df.head(10))
# print(df.tail(10))
# print("Datatype of column:")
# print(df.dtypes)
# print(df.isnull())
# print(df.info())
# print(len(df.columns))
# print(df['Purchase Price'].max())
# print(df['Purchase Price'].mean())
# print (len(df[(df['Language']=='fr')]))
# print (df[(df['Language']=='fr')].count())
# print(df[df['Job'].str.contains('engineer',case=False)])
print(df.columns)
# print(df[df[ 'IP Address']=='132.207.160.22']['Email'])
# print(len (df [(df['CC Provider']=='Mastercard') &(df['Purchase Price']>50)]))

# print (df[df['Credit Card']==4664825258997302]['Email'])
# 
# print(df['AM or PM'].value_counts())
# print(len(df[df['CC Exp Date']=='20']) )
# How many people have a credit card that expires in 2020?

def fun():
    count=0
    for date in df['CC Exp Date']:
        if date.split('/')[1]=='20':
            count+=1
    print(count)
fun()
# or

print(len(df[df['CC Exp Date'].apply(lambda x:x[3:]=='20')]) )

list1=[]
for email in df['Email']:
    list1.append(email.split('@')[1])
df['temp']=list1
df['temp'].value_counts().head(5)
    
# or
print(df['Email'].apply(lambda x:x.split('@')[1]).value_counts().head(5))