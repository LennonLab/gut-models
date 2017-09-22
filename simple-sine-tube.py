from mayavi import mlab
import numpy as np

# AUTHOR: KEN LOCEY

# Generate some random data along a straight line in the x-direction
x = np.arange(0.0, 10, 0.1)
y = np.zeros(len(x))
z = np.zeros(len(x))

s = 4 + np.sin(x)

# Plot using mayavi's mlab api
fig = mlab.figure()

# First we need to make a line source from our data
line = mlab.pipeline.line_source(x, y, z, s)

# Then we apply the "tube" filter to it, and vary the radius by "s"
tube = mlab.pipeline.tube(line, tube_sides=40, tube_radius=1)
tube.filter.vary_radius = 'vary_radius_by_absolute_scalar'

# Now we display the tube as a surface
mlab.pipeline.surface(tube)

# And finally visualize the result
mlab.show()
