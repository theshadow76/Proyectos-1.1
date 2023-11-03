import pandas as pd
# creating the dataframe
df = pd.DataFrame({"Name": ['Zach', 'Don'],
                   "ID": [27123, 26124,]    }) # simple dataframe
print("=====Original DataFrame :")
print(df)
result = df.to_html()  #  convert to_html
print("=====HTML :")
print(result)