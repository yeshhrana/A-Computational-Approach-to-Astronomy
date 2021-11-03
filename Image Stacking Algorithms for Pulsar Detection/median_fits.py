import time, numpy as np
from astropy.io import fits

def median_fits(filenames):

  start = time.time()   # Starts timer
  # Reads in all the FITS files and stores in list
  FITS_list = []
  for filename in filenames: 
    hdulist = fits.open(filename)
    FITS_list.append(hdulist[0].data)
    hdulist.close()

  # Stacks image arrays in 3D array for median calculation
  FITS_stack = np.dstack(FITS_list)

  median = np.median(FITS_stack, axis=2)

  # Calculates the memory consumed by the data
  memory = FITS_stack.nbytes
  # or, equivalently:
  #memory = 200 * 200 * len(filenames) * FITS_stack.itemsize

  # converts to kB:
  memory /= 1024
  
  stop = time.time() - start   # stops timer
  return median, stop, memory