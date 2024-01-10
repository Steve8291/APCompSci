from matplotlib import pyplot as plt

# Matplotlib is a library for creating a variety of visual graphs.
# It uses numpy arrays to do this.
#   sudo pip3 install matplotlib

# Line Graph from two lists:
x = [1, 2, 3, 4]
y = [95, 38, 54, 35]
other_data = [99, 23, 4, 20]

# Plotting the data:
plt.plot(x, y, label='originalData')

# Add another plot to same graph:
plt.plot(x, other_data, label='otherData')

# Adding a title:
plt.title("My Fantastic Graph")

# Adding labels to axes
plt.ylabel("y-axis")
plt.xlabel("x-axis")

# Add a legend:
plt.legend(loc='upper center')

# Labeling your tick marks
labels = ['label1', 'label2', 'label3', 'label4']
plt.xticks(x, labels, rotation='vertical')
# Pad margins so markers don't get clipped by the axes
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)


# Start the event loop
plt.show()

print("matplotlib loop is done!")