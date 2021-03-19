import matplotlib.pyplot as plt



# X and Y values 
x = [-7.33,-7.0,-6.7,-6.4,-6.1]
y = [6.42,26.63,38.97,42.80,45.86]

# Graph Settings
plt.scatter(x, y, alpha=0.5)

# Title and lables
plt.title('The effects of Histamine')
plt.xlabel("Final bath concentration",fontsize=10)
plt.ylabel("Force (mV)",fontsize=10)
 
# Add the grid and show the plots
plt.grid()
plt.show()
