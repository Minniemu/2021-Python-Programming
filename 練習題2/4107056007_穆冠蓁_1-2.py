import matplotlib.pyplot as plt
grades = [48, 67, 56, 80, 78, 54, 88, 75, 43, 69, 23, 59, 7, 27, 100, 62, 82, 66, 73, 47, 93, 34]
bin_list = [i for i in range(0,110,10)]
plt.hist(grades, bins = bin_list, color = '#f06215', rwidth = 0.5 , label = "grades")
plt.xticks([i for i in range(0,110,10)])
plt.xlabel("grades")
plt.yticks([i for i in range(0,5,1)])
plt.show()