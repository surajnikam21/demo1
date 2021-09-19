import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
plt.show()


#MCA results in bar chart
mca_std_list = ["Suraj", "Manoj", "Ramesh", "Shyam"]
mca_std_marks = [98, 45,56,78]

plt.bar(mca_std_list,mca_std_marks,label = 'MCA')
plt.title('MCA Results')
plt.xlabel('MCA Students')
plt.ylabel('MCA Marks Obtained')
plt.legend()
plt.show()


#The easiest way to create a new figure is with pyplot:
#
# fig = plt.figure()  # an empty figure with no Axes
# plt.show()
# fig, ax = plt.subplots()  # a figure with a single Axes
# plt.show()
# fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# plt.show()



x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.

plt.show()



def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})

plt.show()


fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 's'})
my_plotter(ax2, data3, data4, {'marker': 'o'})

plt.show()