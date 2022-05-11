import pandas as pd
#os.chdir("C:\Users\Sai Prathap\Downloads")
df = pd.read_csv('C:\\Users\\Sai Prathap\\Downloads\\Salary_Data.csv')
print(df)
print(df.shape)
print(df.values)
samp = df.copy(deep = False)
print(samp)
samp[10.5]['Salary'] = 0
print(samp)
print(df)