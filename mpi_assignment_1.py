from mpi4py import MPI
rank=MPI.COMM_WORLD.Get_rank()#setup the rank

if rank%2 ==1: #Odd rank print goodbye
    print("Goodbye from process %d" % rank)
else:          #even rank print hello
    print("Hello from process %d" % rank)
