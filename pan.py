# #cleaning Empty cells
import pandas as pd
# df=pd.read_csv('data1.csv')
# print(f"Before: {df}")
# new_df=df.dropna()
# # df.dropna(inplace=True) alternative
# print(f"After: {new_df.to_string}") #it removes all the null data in the data frame

# df=pd.read_csv('data1.csv')
# # df.fillna(130,inplace=True) #replace 130 in every place of NaN
# # #cleaning wrong format 
# # df.fillna({"Calories":130,"Date":"2020"},inplace=True) #can specify column giving dictionary with column name and new thing to replace with
# # print(df)
# x=df["Calories"].mean() #calculate the mean of calories and store it in x and replace it in NaN of calories
# df.fillna({"Calories":x},inplace=True)
# print(df)


#Wrong Format

df=pd.read_csv('data1.csv')
# df.dropna(subset=['Date'],inplace=True) #removes NaN on the basis of Date only 
# df['Date']=pd.to_datetime(df['Date'],format='mixed') #reformat the wrong format into date format 
# print(df)

# df.loc[7,'Duration']=45
# print("After 450 replaced with 45: \n")
# print(df)

for x in df.index:
    if df.loc[x,"Duration"]>120:
        df.loc[x,"Duration"]=120

print(df)

for x in df.index:
    if df.loc[x,"Duration"]>120:
        df.drop(x,inplace=True)
print(df)

#to remove duplicate
print(df.duplicated()) #gives false for all non duplicate value and gives true for duplicated value
df.drop_duplicates(inplace=True)
df.to_csv("final.csv",index=False) #write in final.csv after all cleaning process.
print(df) 

