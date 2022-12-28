import pandas
import matplotlib.pyplot as plt

FILENAME = "data.xlsx"
df = ""
try:
    # openpyxl is required for excel file
    df = pandas.read_excel(FILENAME)
except FileNotFoundError:
    print(f"'{FILENAME}' Can't be found!")

# Which Quarter is the most popular?
df1 = df["quarter"].groupby(df['quarter']).count()
print(df1)
df1.plot(kind="pie")
plt.show()

print("-"*50)

# Most popular travel purpose
df2 = df["Country"].groupby(df['purpose']).count()
print(df2)

print(df2.keys())
plt.bar(df2.keys(), df2.values)
plt.show()

print("-"*50)

# Group by 2 Data
df3 = df["Money "].groupby([df['Country'], df['Transport']]).count()
print(df3)
df3.plot(kind="bar")
plt.show()
