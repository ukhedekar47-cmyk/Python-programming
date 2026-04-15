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

total_cases = df.groupby("Country/Region")["Confirmed"].sum()

print("\nTotal Cases by Country:")
print(total_cases)

plt.plot(df["Date"], df["Confirmed"])
plt.title("COVID Cases Trend")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.show()

total_cases.plot(kind='bar')
plt.title("Cases by Country")
plt.show()

df["Confirmed"].plot(kind='hist')
plt.title("Distribution of Cases")
plt.show()

plt.scatter(df["Confirmed"], df["Deaths"],alpha=0.5)
plt.xlabel("Cases")
plt.ylabel("Deaths")
plt.title("Cases vs Deaths")
plt.show()



