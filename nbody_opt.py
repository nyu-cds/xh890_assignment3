"""
    N-body simulation.
    Entire optimization
    Runtime: 33.638261215994135
    Speedup = 118.08728148206137 / 33.638261215994135 = 3.510504919
"""
def nbody(loops, reference, iterations):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    # change global variables into local variables
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
    
    # unpack offset_momentum function
    [px, py, pz] = [0.0, 0.0, 0.0]
    for body, content in BODIES.items():
        (r, [vx, vy, vz], m_) = content
        [px, py, pz] = list(map(lambda x,y: y-x*m_, [vx,vy,vz],[px,py,pz]))
        
    (r, v, m) = BODIES[reference]
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m

    # set up body pairs
    from itertools import combinations
    body_pairs=list(combinations(BODIES.keys(),2))

    for i in range(loops * iterations):

        # unpack advance function
        dt=0.01

        for (body1, body2) in body_pairs:
            ([x1, y1, z1], v1, m1) = BODIES[body1]
            ([x2, y2, z2], v2, m2) = BODIES[body2]

	     # unpack compute_deltas function
            (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)

	     # unpack update_vs/compute_b(m2, dt, dx, dy, dz) function
            mag = dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
            v1[0] -= dx * m2 * mag 
            v1[1] -= dy * m2 * mag
            v1[2] -= dz * m2 * mag
            v2[0] += dx * m1 * mag
            v2[1] += dy * m1 * mag
            v2[2] += dz * m1 * mag

        for body, content in BODIES.items():
            (r, [vx, vy, vz], m) = content

            # unpack update_rs(r, dt, vx, vy, vz) function
            r[0] += dt * vx
            r[1] += dt * vy
            r[2] += dt * vz
		
        if i != 0 and i % iterations == 0:
            report_energy = 0.0

            for (body1, body2) in body_pairs:
                ((x1, y1, z1), v1, m1) = BODIES[body1]
                ((x2, y2, z2), v2, m2) = BODIES[body2]

	         # unpack compute_deltas function
                (dx, dy, dz) = (x1 - x2, y1 - y2, z1 - z2)

	         # unpack report_energy function
                report_energy -= (m1 * m2) / ((dx ** 2 + dy ** 2 + dz ** 2) ** 0.5)

            for body, content in BODIES.items():
                (r, [vx, vy, vz], m) = content
                report_energy += m * (vx * vx + vy * vy + vz * vz) / 2.
        
            print(report_energy)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit(lambda:nbody(100, 'sun', 20000), number=1))

