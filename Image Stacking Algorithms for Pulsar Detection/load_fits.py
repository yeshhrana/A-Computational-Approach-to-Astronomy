from astropy.io import fits
import numpy as np
def load_fits(x):
    hdulist = fits.open(x)
    data = hdulist[0].data
    
    arg_max = np.argmax(data)
    pos_max = np.unravel_index(arg_max, data.shape)
    
    return pos_max