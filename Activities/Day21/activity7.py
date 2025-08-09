import pandas as pd
df=pd.read_csv('student.csv')
filter_data=df[((df["class"]=="Four")|(df["class"]=="Five"))&(df["gender"]=="male") & (df["mark"]>70)]
print(filter_data.to_string(index=False))