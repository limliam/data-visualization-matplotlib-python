import matplotlib.pyplot as plt

# data
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# styling
plt.style.use('seaborn-v0_8')

# The variable fig represents the entire figure, which is the collection
# of plots that are generated. 
# The variable ax represents a single plot in the figure
fig, ax = plt.subplots()

# plot() method, which tries to plot the data it’s given in a meaningful way
ax.plot(input_values, squares, linewidth=3)

# set chart title and label axis.
ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('square of Value', fontsize=14)

# set size of tick labels
ax.tick_params(labelsize=14)

# open Matplotlib viewer and display th eplot
plt.show()