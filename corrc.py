import codecs
from numpy import corrcoef, transpose, arange
from pylab import pcolor, show, colorbar, xticks, yticks
import numpy as np
import matplotlib.pyplot as plt

f = codecs.open("pivot_player.csv", "r", "utf-8")
names = []

count = 0
for line in f:
	if count > 0:
		# remove double quotes
		row = line.replace ('"', '').split(",")
		row.pop(0)
		if row != []:
			names.append(map(float, row))
	count += 1

R = corrcoef(transpose(names))

pcolor(R)
colorbar()
yticks(arange(0,6),range(0,6))
xticks(arange(0,6),range(0,6))
show()

"""sns.set(style="white")
mask = np.zeros_like(R, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(200, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(R, mask=mask, cmap=cmap, vmax=.8,
            square=True, xticklabels=2, yticklabels=2,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)"""