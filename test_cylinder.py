import numpy as np
from mayavi import mlab
from mayavi.sources.builtin_surface import BuiltinSurface
from mayavi.modules.surface import Surface

def sinewave(freqfn, ampfn, phasefn):
    x, y = np.mgrid[-10:10:100j, -10:10:100j]
    r = ((ampfn)*np.sin((x*freqfn)+ phasefn))*((ampfn)*np.sin((y*freqfn)+ phasefn))
    print (r)
    return r


def cylinder(engine, radius, height, resolution):
    test = BuiltinSurface()
    test.source = 'cylinder'
    test.data_source.center = np.array([0.,0.,0.])
    test.data_source.radius = radius
    test.data_source.height = height
    test.data_source.capping = False
    test.data_source.resolution = resolution
    test_surface = Surface()
    engine.add_source(test)
    engine.add_filter(test_surface)



freq, amp, phase = 1.5, 1, (np.pi/2)
#mlab.surf(sinewave(freq, amp, phase), warp_scale='auto')

rad, hgt, res = 1, 4, 8
eng = mlab.get_engine()
cylinder(eng, rad, hgt, res)
mlab.show()
