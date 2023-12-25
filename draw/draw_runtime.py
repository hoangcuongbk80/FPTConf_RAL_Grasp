import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data points
methods = ['GG-CNN', 'GPD', 'PointNetGPD', 'Fang et al.', 'Gou et al.', 'Contact-GraspNet', 'VoteGrasp', 'Ours']
accuracy = [6.0, 8.8, 10.0, 11.0, 12.7, 13.5, 17.0, 20.6]
speed_hz = [3, 0.4, 0.5, 8, 10.5, 4, 7, 10]
markers = ['o', 's', '^', 'd', 'X', '<', 'P', '*']  # Different marker types for each data point

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the data points with different markers
for i in range(len(methods)):
    ax.scatter(speed_hz[i], accuracy[i], marker=markers[i])

    # Add labels to each data point
    ax.annotate(methods[i], (speed_hz[i], accuracy[i]), xytext=(5, -5), textcoords='offset points')

# Add an arrow from (0, 0) to (6, 6) with label "better"
#arrow = patches.FancyArrowPatch((0, 0), (12, 28), arrowstyle='->', mutation_scale=15, color='black')
#ax.add_patch(arrow)
#ax.annotate('better', (11, 25), xytext=(5, -5), textcoords='offset points')

# Set the desired X and Y axis limits
x_min = 0
x_max = 14
y_min = 0
y_max = 28
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Add labels and title
ax.set_xlabel('Speed (Hz)')
ax.set_ylabel('Average Precision (AP)')

# Display the plot
plt.show()
