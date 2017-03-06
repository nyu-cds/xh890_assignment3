"""
    N-body simulation.
    Entire optimization
    Runtime: 33.638261215994135
    Speedup = 118.08728148206137 / 32.1815428734 = 3.669410194
"""
"""
    4000346 function calls in 32.943 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.676    0.676   33.941   33.941 nbody_iter.py:106(nbody)
        1    0.000    0.000   33.941   33.941 nbody_iter.py:121(<lambda>)
  2000000   32.932    0.000   33.245    0.000 nbody_iter.py:53(advance)
        1    0.001    0.001   33.943   33.943 nbody_iter.py:6(<module>)
      100    0.002    0.000    0.002    0.000 nbody_iter.py:80(report_energy)
        1    0.000    0.000    0.000    0.000 nbody_iter.py:96(offset_momentum)
       15    0.000    0.000    0.000    0.000 nbody_iter.py:99(<lambda>)
        1    0.000    0.000    0.000    0.000 timeit.py:105(Timer)
        1    0.000    0.000    0.000    0.000 timeit.py:121(__init__)
        1    0.000    0.000    0.000    0.000 timeit.py:150(setup)
        1    0.000    0.000   33.941   33.941 timeit.py:185(timeit)
        1    0.000    0.000   33.941   33.941 timeit.py:234(timeit)
        1    0.001    0.001    0.001    0.001 timeit.py:53(<module>)
        1    0.000    0.000    0.000    0.000 timeit.py:94(_template_func)
        1    0.000    0.000   33.941   33.941 timeit.py:96(inner)
        1    0.000    0.000    0.000    0.000 {gc.disable}
        1    0.000    0.000    0.000    0.000 {gc.enable}
        1    0.000    0.000    0.000    0.000 {gc.isenabled}
        1    0.000    0.000    0.000    0.000 {globals}
        1    0.000    0.000    0.000    0.000 {hasattr}
        2    0.000    0.000    0.000    0.000 {isinstance}
        5    0.000    0.000    0.000    0.000 {map}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
  2000100    0.314    0.000    0.314    0.000 {method 'values' of 'dict' objects}
      101    0.018    0.000    0.018    0.000 {range}
        2    0.000    0.000    0.000    0.000 {time.time}
"""
"""
4000346 function calls in 32.902 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.646    0.646   33.900   33.900 nbody_iter.py:106(nbody)
        1    0.000    0.000   33.900   33.900 nbody_iter.py:121(<lambda>)
  2000000   32.884    0.000   33.236    0.000 nbody_iter.py:53(advance)
        1    0.001    0.001   33.902   33.902 nbody_iter.py:6(<module>)
      100    0.001    0.000    0.001    0.000 nbody_iter.py:80(report_energy)
        1    0.000    0.000    0.000    0.000 nbody_iter.py:96(offset_momentum)
       15    0.000    0.000    0.000    0.000 nbody_iter.py:99(<lambda>)
        1    0.000    0.000    0.000    0.000 timeit.py:105(Timer)
        1    0.000    0.000    0.000    0.000 timeit.py:121(__init__)
        1    0.000    0.000    0.000    0.000 timeit.py:150(setup)
        1    0.000    0.000   33.900   33.900 timeit.py:185(timeit)
        1    0.000    0.000   33.900   33.900 timeit.py:234(timeit)
        1    0.001    0.001    0.001    0.001 timeit.py:53(<module>)
        1    0.000    0.000    0.000    0.000 timeit.py:94(_template_func)
        1    0.000    0.000   33.900   33.900 timeit.py:96(inner)
        1    0.000    0.000    0.000    0.000 {gc.disable}
        1    0.000    0.000    0.000    0.000 {gc.enable}
        1    0.000    0.000    0.000    0.000 {gc.isenabled}
        1    0.000    0.000    0.000    0.000 {globals}
        1    0.000    0.000    0.000    0.000 {hasattr}
        2    0.000    0.000    0.000    0.000 {isinstance}
        5    0.000    0.000    0.000    0.000 {map}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
  2000100    0.352    0.000    0.352    0.000 {method 'values' of 'dict' objects}
      101    0.017    0.000    0.017    0.000 {range}
        2    0.000    0.000    0.000    0.000 {time.time}
"""

from itertools import repeat
from itertools import combinations
from itertools import chain
import numpy as np

PI = 3.14159265358979323
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

BODIES = {
    'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),

    'jupiter': ([4.84143144246472090e+00,
                 -1.16032004402742839e+00,
                 -1.03622044471123109e-01],
                [1.66007664274403694e-03 * DAYS_PER_YEAR,
                 7.69901118419740425e-03 * DAYS_PER_YEAR,
                 -6.90460016972063023e-05 * DAYS_PER_YEAR],
                9.54791938424326609e-04 * SOLAR_MASS),

    'saturn': ([8.34336671824457987e+00,
                4.12479856412430479e+00,
                -4.03523417114321381e-01],
               [-2.76742510726862411e-03 * DAYS_PER_YEAR,
                4.99852801234917238e-03 * DAYS_PER_YEAR,
                2.30417297573763929e-05 * DAYS_PER_YEAR],
               2.85885980666130812e-04 * SOLAR_MASS),

    'uranus': ([1.28943695621391310e+01,
                -1.51111514016986312e+01,
                -2.23307578892655734e-01],
               [2.96460137564761618e-03 * DAYS_PER_YEAR,
                2.37847173959480950e-03 * DAYS_PER_YEAR,
                -2.96589568540237556e-05 * DAYS_PER_YEAR],
               4.36624404335156298e-05 * SOLAR_MASS),

    'neptune': ([1.53796971148509165e+01,
                 -2.59193146099879641e+01,
                 1.79258772950371181e-01],
                [2.68067772490389322e-03 * DAYS_PER_YEAR,
                 1.62824170038242295e-03 * DAYS_PER_YEAR,
                 -9.51592254519715870e-05 * DAYS_PER_YEAR],
                5.15138902046611451e-05 * SOLAR_MASS)}

body_pairs=list(combinations(BODIES.keys(),2))

def advance(dt=0.01, bodies=BODIES, pairs=body_pairs):
    for (body1, body2) in pairs:
        deltas = bodies[body1,0:3]-bodies[body2,0:3]
        mag = dt * (np.sum(deltas**2) ** (-1.5))
        bodies[body1,3:6]-=deltas*mag*bodies[body2,-1:]
        bodies[body2,3:6]+=deltas*mag*bodies[body1,-1:]

    bodies[:,0:3]+=dt*bodies[:,3:6]

def report_energy(e=0.0, bodies=BODIES, pairs=body_pairs):
    for (body1, body2) in pairs:
        deltas=bodies[body1,0:3]-bodies[body2,0:3]
        e-=bodies[body1,-1]*bodies[body2,-1]/(np.sum(deltas**2)**0.5)

    for i in range(bodies.shape[0]):
        e += bodies[i,-1] * np.sum(bodies[i, 3:6]**2) / 2.0
        
    return e

def offset_momentum(reference, px=0.0, py=0.0, pz=0.0, bodies=BODIES):
    for body in bodies.keys():
        (r, [vx, vy, vz], m_) = bodies[body]
        [px, py, pz] = list(map(lambda x,y: y-x*m_, [vx,vy,vz],[px,py,pz]))
        
    (r, v, m) = reference
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m

def nbody(loops, reference, iterations, bodies=BODIES):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''    
    offset_momentum(bodies[reference])
    for _ in chain(range(loops)):
        print(report_energy())
        for _ in chain(range(iterations)):
            advance()

if __name__ == '__main__':
    import timeit
    print(timeit.timeit(lambda:nbody(100, 'sun', 20000), number=1))