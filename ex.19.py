#AIM: Write a Python script to do basic Data Analysis using Pandas and Matplot.
print("UIN: 251P107, NAME: Aryan Khedekar")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid_19.csv")  

print("First 5 rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nSummary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

df = df.fillna(0)

df = df.drop_duplicates()

total_cases = df.groupby("country")["cases"].sum()

print("\nTotal Cases by Country:")
print(total_cases)

plt.plot(df["date"], df["cases"])
plt.title("COVID Cases Trend")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.show()

total_cases.plot(kind='bar')
plt.title("Cases by Country")
plt.show()

df["Cases"].plot(kind='hist')
plt.title("Distribution of Cases")
plt.show()

plt.scatter(df["Cases"], df["Deaths"])
plt.xlabel("Cases")
plt.ylabel("Deaths")
plt.title("Cases vs Deaths")
plt.show()
