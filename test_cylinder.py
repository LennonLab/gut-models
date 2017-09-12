import numpy
from mayavi import mlab
from mayavi.sources.builtin_surface import BuiltinSurface
from mayavi.modules.surface import Surface

def cylinder(engine, radius, height, resolution):
    test = BuiltinSurface()
    test.source = 'cylinder'
    test.data_source.center = numpy.array([0.,0.,0.])
    test.data_source.radius = radius
    test.data_source.height = height
    test.data_source.capping = False
    test.data_source.resolution = resolution
    test_surface = Surface()
    engine.add_source(test)
    engine.add_filter(test_surface)

rad, hgt, res = 1, 4, 6
eng = mlab.get_engine()
cylinder(eng, rad, hgt, res)
mlab.show()