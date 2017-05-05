# A CUDA version to calculate the Mandelbrot set
# SET NUMBA_ENABLE_CUDASIM=1

from numba import cuda
import numpy as np
from pylab import imshow, show
import math

@cuda.jit(device=True)
def mandel(x, y, max_iters):
	'''
	Given the real and imaginary parts of a complex number,
	determine if it is a candidate for membership in the 
	Mandelbrot set given a fixed number of iterations.
	'''
	c = complex(x, y)
	z = 0.0j
	for i in range(max_iters):
		z = z*z + c
		if (z.real*z.real + z.imag*z.imag) >= 4:
			return i

	return max_iters

@cuda.jit
def compute_mandel(min_x, max_x, min_y, max_y, image, iters):
	'''
		Calculate the x,y-th pixel for every block
	'''
	# get image shape
	height = image.shape[0]
	width = image.shape[1]
	
	pixel_size_x = (max_x - min_x) / width
	pixel_size_y = (max_y - min_y) / height
	
	#Get offset in block
	offset_y, offset_x = cuda.grid(2)
	
	# Get total pixels
	threads_y = blockdim[0] * griddim[0]
	threads_x = blockdim[1] * griddim[1]

	# Get number of pixels/blocks
	y_threadPixels = int(math.ceil(width / threads_y))
	x_threadPixels = int(math.ceil(width / threads_x))

	#Go through each block
	for i in range(x_threadPixels):
		x = threads_x * i + offset_x #Get the ith block + x offset
		real = min_x + x * pixel_size_x
		for j in range(y_threadPixels):
			y = threads_y * j + offset_y #Get the jth block + y offset
			if x < width and y < height:
				imag = min_y + y * pixel_size_y
				image[y, x] = mandel(real, imag, iters)		
	
if __name__ == '__main__':
	image = np.zeros((1024, 1536), dtype = np.uint8)
	blockdim = (32, 8)
	griddim = (32, 16)

	image_global_mem = cuda.to_device(image)
	compute_mandel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, image_global_mem, 20) 
	image_global_mem.copy_to_host()
	imshow(image)
	show()
