import pandas as pd
from sklearn.decomposition import PCA
from sklearn import linear_model
import numpy as npp
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

sheet1 = pd.read_excel(r"C:\Users\user\Documents\LRdata.xlsx", sheet_name=0)

data1 = sheet1[['Finished Good', 'Demand', 'Production time', 'Production workers ',
                'Total outputs ', 'Quality products ', 'Gross cost', 'Total sales  ',
                'Revenue  ']]
data1 = (data1 - data1.mean()) / (data1.max() - data1.min())
pca = PCA(n_components=2, svd_solver='full')
pca.fit(data1)
T = pca.transform(data1)
print(data1.shape)
print(T.shape)
print(pca.explained_variance_ratio_)
components = pd.DataFrame(pca.components_, columns=data1.columns, index=[1, 2])

import math


def get_important_features(transformed_features, components_, columns):
    """
    This function will return the most 'important'
    features, so we can determine which have the most
    effect on multidimensional scaling
    """
    num_columns = len(columns)

    # Scale the principal components by the max value in
    # the transformed set belonging to that component
    xvector = components_[0] * max(transformed_features[:, 0])
    yvector = components_[1] * max(transformed_features[:, 1])
    # Sort each column by its length. These are your *original*
    # columns, not the principal components.
    important_features = {columns[i]: math.sqrt(xvector[i] ** 2 + yvector[i] ** 2) for i in range(num_columns)}
    important_features = sorted(zip(important_features.values(), important_features.keys()), reverse=True)
    print(important_features)


get_important_features(T, pca.components_, data1.columns.values)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
