#Task 1
import pandas as pd
old=pd.read_csv('old_airline_data_2023.csv')
new=pd.read_json('new_airline_data_2024.json')

new.iloc[:,1:]=new.iloc[:,1:].fillna(new.iloc[:,1:].mean())
new=new.dropna()

new.iloc[:,:1]=new[new.iloc[:,:1] .isin (['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])]


new.iloc[:, 0] = new.iloc[:, 0].str.capitalize()

new.columns=new.columns.str.lower()

new.columns = new.columns.str.replace(' ', '_')

new =new.iloc[:12,:]

#task2
old.columns=old.columns.str.lower()

old.columns = old.columns.str.replace(' ', '_')
old_df=pd.DataFrame(old)
new_df=pd.DataFrame(new)


result = pd.concat([old_df,new_df],ignore_index=False)
print(result)
