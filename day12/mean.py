import pandas as pd

dict = {
      "name":["arun", "basu", "atul"],
       "marks":[30, 40, 50],
       "city":["bikapur","belgaua","solapur"],
        "pincode":[45,67,90]
}
df = pd.DataFrame(dict)
print(df)
print(df.describe()) #gives the description of numercial values
print(df.sum(axis=1)) #eturn mean values of existing numerical values
print(df.mean(axis=0)) #return mean values of existing numercal values
print(df.max(axis=1)) #print maximum from the columns
print(df.min(axis=1)) #prints min of the column
print(df.shape) #return the matrix of the dataframe
df1 = df.drop(["name", "city"], axis=1) #delete rows and columns according to axis
print(df1)
print(df.loc[0, "pincode"])
print(df.iloc[1, 2])
print(df[0:3])#slicing method
