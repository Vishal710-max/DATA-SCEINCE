#ALL EXAMLPES ARE RELATED TO THE MATPLOT BARS 
import matplotlib.pyplot as plt
import numpy as np

#Matplotlib Bars
#Creating Bars
#With Pyplot, you can use the bar() function to draw bar graphs:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show()

#Horizontal Bars
#If you want the bars to be displayed horizontally instead of vertically, use the barh() function:
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y)
plt.show()
 
#Bar Color
#The bar() and barh() take the keyword argument color to set the color of the bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "red")
plt.show()
 
#Bar Width
#The bar() takes the keyword argument width to set the width of the bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, width = 0.1)
plt.show()
 
#Bar Height
#The barh() takes the keyword argument height to set the height of the bars this property is applied to barh
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y, height = 0.1)
plt.show()

# Matplotlib Histograms
# Histogram
# A histogram is a graph showing frequency distributions.
# It is a graph showing the number of observations within each given interval

x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()

# Matplotlib Pie Charts
# Creating Pie Charts
# With Pyplot, you can use the pie() function to draw pie charts:
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()

# Labels
# Add labels to the pie chart with the labels parameter.
# The labels parameter must be an array with one label for each wedge:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.show()

# Start Angle
# As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a 
# startangle parameter.
# The startangle parameter is defined with an angle in degrees, default angle is 0:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 

# Explode
# Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.
# The explode parameter, if specified, and not None, must be an array with one value for each wedge.
# Each value represents how far from the center each wedge is displayed:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()

# Colors
# You can set the color of each wedge with the colors parameter.
# The colors parameter, if specified, must be an array with one value for each wedge
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

# Legend
# To add a list of explanation for each wedge, use the legend() function:
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend()
plt.show()

# Legend With Header
# To add a header to the legend, add the title parameter to the legend function.
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()
