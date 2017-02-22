from itertools import product  # import itertools module
def zbits(n, k):
    arrays = [(0, 1) for _ in range(n)] # generate a list of n tuples (0,1)
    cp = list(product(*arrays)) # generate permutations
    # filter cp so that it only contains tuples that have k zeros
    #  and convert cp to list
    cp = [list(item) for item in cp if sum(item)==n-k]
    for item in cp:
        # convert intergers to strings for join
        item = [str(val) for val in item]
        # print binary strings out
        print(''.join(item))
