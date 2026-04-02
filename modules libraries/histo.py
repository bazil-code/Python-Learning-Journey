import matplotlib.pyplot as plt


data = [12,25,33,41,18,29,37,44,22,31,27,15,39,48,20,24,35,28,30,46,14,26,38,42,19,21,23,34,40,47,13,16,32,36,17,45,43,49,11,27]
bins = [0,10,20,30,40,50,60]
plt.hist(data,bins=bins,color='blue',edgecolor='black')
plt.title('Histogram of Marks')
plt.xlabel('Marks Group (Class Interval)')
plt.ylabel('Frequency')
plt.xticks(bins)
plt.show()
