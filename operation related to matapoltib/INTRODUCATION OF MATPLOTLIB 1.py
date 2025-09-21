#ALL EXAMLPES ARE RELATED TO THE MATPLOT GRAPHS

import matplotlib.pyplot as plt
import numpy as np

#checking the version pyplot is a submodule/package which contain most of the 
print (plt.__version__)

x=np.array ([0,100]) #[0,100]where 0 is an x-axis 100 is an y-axis
y=np.array ([100,0]) #same like above
plt.plot (x,y) #plot is an inbuilt function 
plt.show () #display the result
 
#To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
x=np.array ([0,100]) 
y=np.array ([100,0]) 
plt.plot (x,y,'o')  
plt.show () 
 
#Matplotlib Line
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dotted')#You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
plt.show()
#possible values are :dotted & dashed and their shortcuts dotted =':' dashed ='--' dashdot ='-.'

#Line Color
#You can use the keyword argument color or the shorter c to set the color of the line:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, color = 'r')
plt.show()

#Line Width
#You can use the keyword argument linewidth or the shorter lw to change the width of the line
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = '20.5')
plt.show()

#Multiple Lines
#You can plot as many lines as you like by simply adding more plt.plot() functions:
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()
 
#Create Labels for a Plot
#With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()
 
#Create a Title for a Plot
#With Pyplot, you can use the title() function to set a title for the plot
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()
 
#Set Font Properties for Title and Labels
#You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title 
#and labels
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(x, y)
plt.show()

#Matplotlib Adding Grid Lines
#Add Grid Lines to a Plot
#With Pyplot, you can use the grid() function to add grid lines to the plot
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid()
plt.show()
 
#Matplotlib Scatter
#Creating Scatter Plots
#With Pyplot, you can use the scatter() function to draw a scatter plot.
#The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for 
#the values of the x-axis, and one for values on the y-axis:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()
