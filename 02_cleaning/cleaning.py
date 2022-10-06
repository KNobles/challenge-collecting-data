from numpy import float64
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

df = pd.read_csv("cleaned_dataset_properties.csv")

# data.loc[data['construction_year'] == "None", 'construction_year'] = "0"

# #data.insert(loc=4, column='property_age', value=2022 - data['construction_year'])
# #print(data.dtypes)
# data['construction_year'] = data['construction_year'].astype(float).astype(int)
# data.loc[data['construction_year'] > 0, "property_age"] = 2022 - data['construction_year']
# data['property_age'] = data['property_age'].fillna(0).astype(int)
# data['price'] = data['price'].astype(int)
# data.loc[data['swimmingpool'] == "True"] = 1
# data.loc[data['swimmingpool'] == "False"] = 0
# data['swimmingpool'] = data['swimmingpool'].astype(float).astype(int)
# # print(data.dtypes)
# ds = pandas.Series(data['subtype'])
# ps_corr = pandas.DataFrame(data=data, columns=["price", "swimmingpool", "subtype"])
# print(ps_corr.corr(method ='pearson'))
# df_new = ps_corr.set_index('name')['subtype'].astype(str).str.get_dummies().T
# # price_age_plot = seaborn.scatterplot(data=data, x="subtype", y="swimmingpool")
# plt.figure(figsize=(8, 4))
# seaborn.heatmap(ps_corr)
# plt.show()
# plt.yticks(numpy.arange(min(data['price']), max(data['price'])+1, 50000))
# plt.ticklabel_format(style='plain', axis='y', )
# plt.show()
# has_garden has_terrace swimmingpool
df.drop_duplicates(inplace=True)
df.duplicated().sum()
object_features = ['price', 'habitable_surface', 'bedrooms_count', 'garden_area', 'land_area', 'num_facade']
#converting object_features values into numerical values
for object_feature in object_features:
    df[object_feature] = df[object_feature].replace('None',np.nan, inplace = False)
    pd.to_numeric(df[object_feature])

print(df)