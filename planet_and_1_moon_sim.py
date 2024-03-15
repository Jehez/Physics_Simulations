import gravity_sim

gravity_sim.add_title("Planet and 1 moon")

# make planets/celestial bodies
planet = gravity_sim.planet(375,375,3.75*10**12,50,(0,128,255))
moon = gravity_sim.planet(375,125,1,10,(255,255,255))

# give intial velocities so bodies stay in orbit
moon.velX = 1
gravity_sim.TIMESTEP = 5 # set TIMESTEP (speed up factor) if needed

gravity_sim.start_sim() # start simulation!

# Note: this simulation does not use precise/exact values (only estimates) so the moon will not make a perfect orbit