# Add two excel and remove duplicates and store it in a new excel
import pandas as pd
df1=pd.read_excel ("C:\\Users\\User\\Desktop\\python1\\Excel\\List1.xlsx")
df2=pd.read_excel (r"C:\Users\User\Desktop\python1\Excel\List2.xlsx")
df3=pd.concat([df1,df2])
df3=df3.drop_duplicates()
df1.to_excel(r"C:\Users\User\Desktop\python1\Excel\List3.xlsx",index=False)

