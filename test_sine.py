from mayavi import mlab
import numpy
x, y = numpy.mgrid[-10:10:100j, -10:10:100j]
r = numpy.sin(x)*numpy.sin(y)
mlab.surf(r, warp_scale='auto')
mlab.show()