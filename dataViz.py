from sklearn import linear_model
import numpy as npp
import pandas as pd
from sklearn.preprocessing import StandardScaler

sheet1 = pd.read_excel(r"C:\Users\user\Documents\LRdata.xlsx", sheet_name=0)
data1 = sheet1[['Finished Good', 'Demand', 'Production time', 'Production workers ',
                'Total outputs ', 'Quality products ', 'Gross cost', 'Total sales  ',
                'Revenue  ']]
x_std = StandardScaler().fit_transform(data1)
features = x_std.T
co_mat = npp.cov(features)
eig_vals, eig_vecs = npp.linalg.eig(co_mat)
eig_vals[0] / sum(eig_vals)
significance = [np.abs(i) / np.sum(eigenval) for i in eigenval]
print(eig_vals)
proj_x = x_std.dot(eig_vecs.T[0])
result = pd.DataFrame(proj_x, columns=["PC1"])
result["y-axis"] = 0.0
result['label'] = 'Y'
result.head(10)
# print(proj_x)