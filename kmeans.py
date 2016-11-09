from sklearn.cluster import KMeans
from sklearn import metrics
import csv


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


import matplotlib.pyplot as plt

init = 'random'  # initialization method
iterations = 10  # to run 10 times with different random centroids to choose the final model as the one with the lowest SSE
max_iter = 300  # maximum number of iterations for each single run
tol = 1e-04  # controls the tolerance with regard to the changes in the within-cluster sum-squared-error to declare convergence
random_state = 0  # random

distortions = []
silhouettes = []

for i in range(2, 7):
    km = KMeans(i, init, n_init=iterations, max_iter=max_iter, tol=tol, random_state=random_state)
    labels = km.fit_predict(infos)
    distortions.append(km.inertia_)
    silhouettes.append(metrics.silhouette_score(infos, labels))

# Plot distoritions
plt.plot(range(2, 7), distortions, marker='x')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()

# Plot Silhouette
plt.plot(range(2, 7), silhouettes, marker='x')
plt.xlabel('Number of clusters')
plt.ylabel('Silohouette')
plt.show()

# 4 . Visualization
import sklearn.cluster
k = 3
centroids, labels, z =  sklearn.cluster.k_means(infos, k, init="k-means++" )
plotdata(infos,labels, 'kmeans')