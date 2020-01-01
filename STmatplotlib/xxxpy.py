import pandas as pd
import matplotlib.pyplot as plt

data = [{'name': 'Mexico City', 'group': 'Latin America', 'year': 2016, 'value': 21172.8}, {'name': 'Delhi', 'group': 'India', 'year': 2016, 'value': 26432.0}, {'name': 'Beijing', 'group': 'Asia', 'year': 2016, 'value': 21147.4}, {'name': 'Dhaka', 'group': 'Asia', 'year': 2016, 'value': 18276.2}, {'name': 'Cairo', 'group': 'Middle East', 'year': 2016, 'value': 19131.2}, {'name': 'Sao Paulo', 'group': 'Latin America', 'year': 2016, 'value': 21276.6}, {'name': 'Tokyo', 'group': 'Asia', 'year': 2016, 'value': 38065.4}, {'name': 'Shanghai', 'group': 'Asia', 'year': 2016, 'value': 24420.2}, {'name': 'Mumbai', 'group': 'India', 'year': 2016, 'value': 21402.0}, {'name': 'New York', 'group': 'North America', 'year': 2016, 'value': 18633.0}, {'name': 'Osaka', 'group': 'Asia', 'year': 2016, 'value': 20295.0}]
dff = pd.DataFrame(data).sort_values(by='value', ascending=False).tail(5)
scale = 9/16
colors = dict(zip(
    ['India', 'Europe', 'Asia', 'Latin America',
     'Middle East', 'North America', 'Africa'],
    ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
     '#aafbff', '#f7bb5f', '#eafb50']
))

group_lk = dff.set_index('name')['group'].to_dict()
fig, ax = plt.subplots(figsize=(15,15*scale))
print(dff.shape[0])
# print(dff['index'].values)

ax.barh(dff['index'].values, dff['value'].values, color=[colors[group_lk[x]] for x in dff['name']],)
# # ax.barh([1,2.5,3], [1,2,3],height=0.5)
plt.savefig("xx.jpg")
