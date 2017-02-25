from itertools import product  # import itertools module
def zbits(n, k):
    arrays = [(0, 1) for _ in range(n)] # generate a list of n tuples (0,1)
    cp = list(product(*arrays)) # generate permutations
    # filter cp so that it only contains tuples that have k zeros
    #  and convert cp to list
    cp = [list(item) for item in cp if sum(item)==n-k]
    output = set()
    for item in cp:
        # convert intergers to strings for join
        item = [str(val) for val in item]
        # print binary strings out
        output.add(''.join(item))
    return output

if __name__ == '__main__':
    
    assert zbits(4, 3) == {'0100', '0001', '0010', '1000'}
    assert zbits(4, 1) == {'0111', '1011', '1101', '1110'}
    assert zbits(5, 4) == {'00001', '00100', '01000', '10000', '00010'}