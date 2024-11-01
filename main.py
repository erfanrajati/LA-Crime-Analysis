import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Crime_Data_from_2020_to_Present.csv")

crime_types = list(set(data["Crm Cd Desc"]))
crime_counts = []
for crm in crime_types:
    count = list(data["Crm Cd Desc"]).count(crm)
    crime_counts.append(count)

temp = dict(zip(crime_types, crime_counts))


to_delete = [crm for crm, count in temp.items() if count < 5000]

for crm in to_delete:
    del temp[crm]

plt.bar(temp.keys(), temp.values())
plt.show()

# for item in temp.items():
#     with open("output.txt", 'a') as file:
#         file.write(str(item) + '\n')

