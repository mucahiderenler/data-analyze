import os
import csv
import codecs
import matplotlib.pyplot as plt

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
        ++count

finally:
    f.close()

print(infos)

labels = [0 for x in range(len(infos))]
plotdata(infos,labels,'basic')

import sklearn.cluster
k = 3
centroids, labels, z =  sklearn.cluster.k_means(infos, k, init="k-means++" )
plotdata(infos,labels, 'kmeans')

# dbscan
# setting parameters
labels = sklearn.cluster.DBSCAN(eps=0.01, min_samples=5).fit_predict(infos)
plotdata(infos,labels, 'dbscan')

from scipy import cluster
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(infos)
clusters = cluster.hierarchy.linkage(matsim, method = 'single')
labels = cluster.hierarchy.fcluster(clusters, 21, criterion = 'distance')
plotdata(infos,labels, 'hierarchical single')

model = sklearn.cluster.AgglomerativeClustering(n_clusters=3,linkage="complete", affinity='euclidean')
labels = model.fit_predict(infos)
plotdata(infos,labels, 'hierarchical ward')