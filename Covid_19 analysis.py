import pandas as pd
import matplotlib.pyplot as plt
print("Load the data set: \n")
df=pd.read_csv("C:\\Users\\MEHWISH\\Downloads\\covid_19 data.csv")
print(df) 
print("this gives summery statistics: \n")
print(df.describe())
print("whole data information: \n")
print(df.info())
print("give top 5 rows: \n")
print(df.head())
print("give last 5 rows: \n")
print(df.tail())
print("missing values in each column and their sum: \n")
print(df.isnull().sum())
print("give duplicates in each column: \n")
print(df.duplicated())
                                         # Total covid_19 cases globally
                                         
Total_confirmed=df["Confirmed"].sum()
Total_deaths=df["Deaths"].sum()
Total_recovered=df["Recovered"].sum()
print(f"total_confirmed cases: {Total_confirmed}")
print(f"total_deaths: {Total_deaths}")
print(f"total_recovered: {Total_recovered}")

country_summery=df.groupby("Country").sum().sort_values(by="Confirmed",ascending=False)
print(country_summery.head(10))

                            # COVID_19 IN Pakistan

pakistan_data=df[df["Country"]=="Pakistan"]
print(pakistan_data.tail())
                           # LINE PLOT FOR PAKISTAN CONFIRMED CASES
plt.figure(figsize=(10,5))
plt.plot(pakistan_data["Date"],pakistan_data["Confirmed"],color="blue",label="Confirmed")
plt.plot(pakistan_data["Date"],pakistan_data["Deaths"],color="red",label="Deaths")
plt.plot(pakistan_data["Date"],pakistan_data["Recovered"],color="green",label="Recovered")

# plt.plot(pakistan_data['Date'], pakistan_data['Confirmed'], color='blue', label='Confirmed')
# plt.plot(pakistan_data['Date'], pakistan_data['Deaths'], color='red', label='Deaths')
# plt.plot(pakistan_data['Date'], pakistan_data['Recovered'], color='green', label='Recovered')

plt.title("Covid_19 trend in Pakistan")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend()
plt.show()  
                 # Save cleaned Data
print(country_summery.to_csv("country_summery.csv"))