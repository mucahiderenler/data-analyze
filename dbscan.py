import os
import csv
import codecs
import matplotlib.pyplot as plt
import sklearn.cluster

def plotdata(data,labels,name): #def function plotdata
#colors = ['black']
    fig, ax = plt.subplots()
    plt.scatter([row[0] for row in data], [row[1] for row in data], c=labels)
    ax.grid(True)
    fig.tight_layout()
    plt.title(name)
    plt.show()

infos = []

f = open('player_career.csv','r')
count = 0
try:
    datos = None
    reader = csv.DictReader(f)
    for row in reader:
        datos = []
        if row[('minutes')] == None or count == 1000 :
            break
        datos.append(row[('minutes')])
        datos.append(row[('pts')])
        datos.append(row[('reb')])
        datos.append(row[('asts')])
        datos.append(row[('stl')])
        datos.append(row[('blk')])
        infos.append(datos)
        count = count +1
finally:
    f.close()

# dbscan
# setting parameters

from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
norminfo = min_max_scaler.fit_transform(infos)

from sklearn.decomposition import PCA

estimator = PCA(n_components=2)
X_pca = estimator.fit_transform(norminfo)

# 2.1 Parametrization
import sklearn.neighbors

dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(X_pca)

minPts = 3
from sklearn.neighbors import kneighbors_graph

A = kneighbors_graph(X_pca, minPts, include_self=False)
Ar = A.toarray()

seq = []
for i, s in enumerate(X_pca):
    for j in range(len(X_pca)):
        if Ar[i][j] != 0:
            seq.append(matsim[i][j])

seq.sort()
plt.plot(seq)
plt.show()


labels = sklearn.cluster.DBSCAN(eps=0.84, min_samples=5).fit_predict(infos)
plotdata(infos,labels, 'dbscan')