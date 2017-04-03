"""
    N-body simulation.
    Numba optimization
    Former Runtime: 118.08728148206137
    Current Runtime: 15.1048829556
    Speedup = 118.08728148206137 / 15.1048829556 = 7.817821683
    
    Modification:
    1) change dictionaries and lists into numpy.arrays
    2) add vec_deltas to deal with array substractions
    3) add jit application
"""

from itertools import combinations
from numba import jit, int32, float64, vectorize, void
import numpy as np
import timeit

PI = 3.14159265358979323
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

BODIES = np.array([
    ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [SOLAR_MASS,0.0,0.0]),
    ([4.84143144246472090e+00,
                 -1.16032004402742839e+00,
                 -1.03622044471123109e-01],
                [1.66007664274403694e-03 * DAYS_PER_YEAR,
                 7.69901118419740425e-03 * DAYS_PER_YEAR,
                 -6.90460016972063023e-05 * DAYS_PER_YEAR],
                [9.54791938424326609e-04 * SOLAR_MASS,0.0,0.0]),
    ([8.34336671824457987e+00,
                4.12479856412430479e+00,
                -4.03523417114321381e-01],
               [-2.76742510726862411e-03 * DAYS_PER_YEAR,
                4.99852801234917238e-03 * DAYS_PER_YEAR,
                2.30417297573763929e-05 * DAYS_PER_YEAR],
               [2.85885980666130812e-04 * SOLAR_MASS,0.0,0.0]),
    ([1.28943695621391310e+01,
                -1.51111514016986312e+01,
                -2.23307578892655734e-01],
               [2.96460137564761618e-03 * DAYS_PER_YEAR,
                2.37847173959480950e-03 * DAYS_PER_YEAR,
                -2.96589568540237556e-05 * DAYS_PER_YEAR],
               [4.36624404335156298e-05 * SOLAR_MASS,0.0,0.0]),
    ([1.53796971148509165e+01,
                 -2.59193146099879641e+01,
                 1.79258772950371181e-01],
                [2.68067772490389322e-03 * DAYS_PER_YEAR,
                 1.62824170038242295e-03 * DAYS_PER_YEAR,
                 -9.51592254519715870e-05 * DAYS_PER_YEAR],
                [5.15138902046611451e-05 * SOLAR_MASS,0.0,0.0])])

body_pairs=np.array(list(combinations(np.arange(BODIES.shape[0]),2)))

@vectorize([float64(float64, float64)])
def vec_deltas(x1, x2):
    return x1 - x2

@jit('void(float64, int32, float64[:,:,:], int32[:,:])')
def advance(dt, iterations, bodies=BODIES, pairs=body_pairs):
    for _ in range(iterations):
       
        for index in range(len(pairs)):

            (i,j) = pairs[index]
            x1 = bodies[i][0]
            v1 = bodies[i][1]
            m1 = bodies[i][2][0]
            x2 = bodies[j][0]
            v2 = bodies[j][1]
            m2 = bodies[j][2][0]

	     # unpack compute_deltas function
            (dx, dy, dz) = vec_deltas(x1, x2)

	     # unpack update_vs/compute_b(m2, dt, dx, dy, dz) function
            mag = dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
            m2r = m2 * mag
            m1r = m1 * mag
            v1[0] -= dx * b2
            v1[1] -= dy * b2
            v1[2] -= dz * b2
            v2[0] += dx * b1
            v2[1] += dy * b1
            v2[2] += dz * b1

        for index in range(len(bodies)):
            r = bodies[index][0]
            v = bodies[index][1]
            r += dt * v

@jit('float64(float64,float64[:,:,:],int32[:,:])')
def report_energy(e=0.0, bodies=BODIES, pairs=body_pairs):
    for index in range(len(body_pairs)):
        (i,j) = pairs[index]
        x1 = bodies[i][0]
        v1 = bodies[i][1]
        m1 = bodies[i][2][0]
        x2 = bodies[j][0]
        v2 = bodies[j][1]
        m2 = bodies[j][2][0]

	    # unpack compute_deltas function
        (dx, dy, dz) = vec_deltas(x1, x2)    
        # unpack report_energy function
        e -= (m1 * m2) / ((dx ** 2 + dy ** 2 + dz ** 2) ** 0.5)

    for index in range(len(bodies)):    
        v = bodies[index][1]
        m = bodies[index][2][0]
        e += m * (np.sum(v**2)) / 2.0
        
    return e

@jit('void(int32, int32, int32, float64[:,:,:])')
def nbody(loops, reference, iterations, bodies=BODIES):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''    
    p = np.array([0.0,0.0,0.0])
    for index in range(len(bodies)): 
        r = bodies[index][0]
        v = bodies[index][1]
        m = bodies[index][2][0]
        p -= v * m
    v = bodies[reference][1]
    m = bodies[reference][2][0]
    v = p / m
    for _ in range(loops):
        advance(0.01,iterations)
        print(report_energy(0.0))

if __name__ == '__main__':
    print(timeit.timeit(lambda:nbody(100, 0, 20000), number=1))