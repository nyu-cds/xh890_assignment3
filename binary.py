from itertools import product  # import itertools module
def zbits(n, k):
    arrays = [(0, 1) for _ in range(n)]
    cp = list(product(*arrays))
    cp = [list(item) for item in cp if sum(item)==n-k]
    for item in cp:
        item = [str(val) for val in item]
        print(''.join(item))