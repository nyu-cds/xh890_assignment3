from mpi4py import MPI
import numpy as np

# distributed sorting
# mpiexec -n 4 python parallel_sorter.py

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
	
	input_size = 10000
	input_arr = np.random.randint(0, input_size, size = input_size)
	
	min = np.amin(input_arr)
	max = np.amax(input_arr)
	bins = np.linspace(min, max, num=size)
	digitized = np.digitize(input_arr, bins)
	
	data = np.array([input_arr[digitized == i+1] for i in range(size)])
else:
	data = None

data = comm.scatter(data, root=0)
data = np.sort(data)
data = comm.gather(data, root=0)
if rank == 0:
	#Concatenate results
	print(np.concatenate(data))
