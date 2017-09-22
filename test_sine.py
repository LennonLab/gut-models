#import necessary packages
from mayavi import mlab
import numpy

#generate and return array r of sine wave plane points given a frequency, amplitude and phase
def sinewave(freqfn, ampfn, phasefn):
    x, y = numpy.mgrid[-10:10:100j, -10:10:100j]
    r = ((ampfn)*numpy.sin((x*freqfn)+ phasefn))*((ampfn)*numpy.sin((y*freqfn)+ phasefn))
    print (r)
    return r

#random freq, amp, and phase to test sine wave plane response
freq, amp, phase = 1.5, 1, (numpy.pi/2)

r = sinewave(freq, amp, phase)

#generate surf from sinewave function with frequency, amplitude, and phase
#mlab.surf(sinewave(freq, amp, phase), warp_scale='auto')

#show mlab figure
#mlab.show()
