import os
import pathlib
from statistics import median
from types import MethodType
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv("~/Documents/BeCode/Projects/challenge-collecting-data/data/Property_structured_data.csv")

features = ['id', 'locality', 'postal_code', 'region', 'province',
       'type_of_property', 'subtype_of_property', 'type_of_sale', 'price',
       'number_of_bedrooms', 'surface', 'kitchen_type',
       'fully_equipped_kitchen', 'furnished', 'open_fire', 'terrace',
       'terrace_surface', 'garden', 'garden_surface', 'land_surface',
       'number_of_facades', 'swimming_pool', 'state_of_the_building']

#converting object_features values into numerical values
for feature in features:
    df[feature].replace(-1,np.nan, inplace = True)

def remove_outliers(dataset, column_name:str):
    #calculate upper and lower limits
    upper_limit = dataset[column_name].mean() +2.6 * dataset[column_name].std()
    lower_limit = dataset[column_name].mean() -2.6 * dataset[column_name].std()

    #select outliers
    dataset[~((dataset[column_name] < upper_limit) & (dataset[column_name]> lower_limit))]

    #outliers removed
    new_dataset = dataset[(dataset[column_name] < upper_limit) & (dataset[column_name] > lower_limit)]
    return new_dataset

# df2 = remove_outliers(df, "terrace_surface")
ro_price = remove_outliers(df, "price")
ro_price = remove_outliers(ro_price, "price")

ro_price = remove_outliers(ro_price, "surface")
ro_price = remove_outliers(ro_price, "surface")

# ro_price = remove_outliers(ro_price, "land_surface")
# ro_price = remove_outliers(ro_price, "land_surface")

ro_price = remove_outliers(ro_price, "number_of_bedrooms")
ro_price = remove_outliers(ro_price, "number_of_bedrooms")
ro_corr = ro_price.corr()

ro = sns.heatmap(ro_corr, annot=True, annot_kws={'fontsize':10})

print(df["price"].corr(df["open_fire"]))
print(df["price"].corr(df["furnished"]))
print(df["price"].corr(df["terrace"]))
print(df["price"].corr(df["terrace_surface"]))
print(df["price"].corr(df["swimming_pool"]))

fig = px.scatter_3d(ro_price, x="number_of_bedrooms", y="surface", z="price", color="locality",
                 size='price')
fig.show()

# print(ro_price['type_of_property'])

# plt.show()

# sns.heatmap(correlation, annot=True)
# print(df["locality"].value_counts()["Namur"])

# my_plot = sns.regplot(data=df2, x="furnished", y="price")
# Do not use price for any of the features

# df_price = pd.DataFrame(df.corrwith(df.price).sort_values(ascending = False))
# df_price.rename(index={"0": "Price"})
# a = sns.heatmap(df_price, annot=True, fmt="g", cmap='YlGnBu') 
# a.tick_params(labelsize=10)
# a.set_xlabel("Price",fontsize=20)
# g = sns.lmplot(x="state_of_the_building", y="price", hue="state_of_the_building", data=df)
# 
