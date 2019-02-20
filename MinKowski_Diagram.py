import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.lines as mlines
import sys

def abline(slope, intercept,appearance,style,frame):
    """Plot a line from slope and intercept"""
    #axes = plt.gca()
    x_vals = np.array(frame.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, color = appearance, linestyle = style) 
    
def newline(point, slope, ax):
    xmin, xmax = ax.get_xbound()
    p1 = point
    p2 = [point[0] + 1,point[1] + slope]
    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax], color="yellow")
    ax.add_line(l)
    return l
def set_axis():
    fig = plt.figure() #Initializes the graph
    ax = plt.gca() #Creates a graph axis object
    ax.spines['right'].set_color('none') #Makes the right outside bar of the graph disappear
    ax.spines['top'].set_color('none') #Makes the top outside bar of the graph dissapear
    ax.xaxis.set_ticks_position('bottom') #Moves the ticks to the bottom of the graph
    ax.spines['bottom'].set_position(('data',0)) #Makes a new axix (spine) at center of data 
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))#Makes a new axix (spine) at center of data 
    ax.axes.get_xaxis().set_ticks([])  #Makes ticks invisble 
    ax.axes.get_yaxis().set_ticks([])  #Makes ticks visible 
    scale_factor = unit_scale(beta)
    return ax, fig

def y_values_fill(slope,intercept,frame):
    x_vals = np.array(frame.get_xlim())
    y_vals = intercept + slope * x_vals
    return y_vals

def light_cone(line1, line2,frame,point):
    x_vals = frame.get_ylim()
    offset = 2*(point[1] - point[0])
    y1_vals = line1.get_ydata()
    y1_vals[0] -= offset
    y1_vals[1] -= offset 
    y2_vals = line2.get_ydata()
    print(offset)
    print(y1_vals)
    print(y2_vals)
    plt.fill_betweenx(x_vals,y1_vals,y2_vals,facecolor='gold',interpolate=True)
    
def alpha(beta):
    return theta(1/((beta*math.pi)/180)) #Returns angle between ct(prime) and the x axis
    #The 1/B in radians
    #Remember beta is also the slope of the velocity of the S' reference frame

def theta(beta):
    c = 299792458 #speed of light in m/s
    return np.arctan(beta) #Returns angle between x(prime) and x axis

def point_value(length,angle):
    return length * np.cos(angle)

def initialize_graph(args):
    if show_scale == True:
        scale_factor = unit_scale(beta) #Calculates the scaling factor U(prime) as it relates to U
        ax.axes.get_xaxis([scale_factor])
        ax.axes.get_yaxis([scale_factor])
    if depth != None:
        plt.xlim(-1 * depth, depth) #Sets the limit size of graph according to depth
        plt.ylim(-1 * depth, depth)

def setup(beta, point):
    
    #angle_ct = alpha(beta)
    #angle_x = theta(beta)
    angle_ct = beta
    angle_x = 1/beta
    x_offset = 3
    y_offset = 4
    plt.ylim(-10,10)
    plt.xlim(-10,10)
    abline(1,0,'green','-',ax)
    abline(angle_x,0,'red','-',ax)
    abline(angle_ct,0,'blue','-',ax)
    for i in range (-20,20):
        abline(angle_x,scale_factor*i,'red','--',ax)
        abline(angle_ct,scale_factor*i,'blue','--',ax)

    line1 = newline(point,1, ax)
    line2 = newline(point,-1, ax)
    light_cone(line1,line2,ax,point)
    plt.show()
    
def unit_scale(beta):
    return np.sqrt((1+(beta**2))/(1-(beta**2)))

#setup(.66)
def main():
    beta = float(sys.argv[1])
    point = [int(sys.argv[2]),int(sys.argv[3])]
    setup(beta, point)

if __name__ == "__main__":
    main()
