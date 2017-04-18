import numpy
from mpi4py import MPI
comm=MPI.COMM_WORLD
rank=comm.Get_rank() #set rank
size=comm.Get_size() #set size

datal= numpy.zeros(1)

if rank ==0: #when rank is 0, input the data
    data=101 #initialize the data
    while (data>=100) :
        try:           
            data = input('input an integer less than 100: ')
            data=int(data) 
        except :
            print("not an int, try again")
            data=101   
            continue

    datal[0]=data
    comm.Send(datal, dest=1 )
    comm.Recv(datal,source=size-1) 
    print(datal[0])

elif rank<size-1:                   
    comm.Recv( datal,source=rank-1 )
    datal =datal*(rank+1) 
    comm.Send(datal,(rank+1)) 
else:                                
    comm.Recv( datal,source=rank-1 )
    comm.Send(datal,dest=0)
