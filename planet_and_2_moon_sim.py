import gravity_sim

gravity_sim.add_title("Planet and 2 moons")

# resize window if needed
gravity_sim.window_height = 800
gravity_sim.window_width = 800

# make planets/celestial bodies
planet = gravity_sim.planet(400,400,4.26e8,10,(0,255,0))
moon1 = gravity_sim.planet(400,350.5,7.106,5,(255,255,0))
moon2 = gravity_sim.planet(400,100,1,2.5,(0,255,255))

# give intial velocities so bodies stay in orbit
moon1.velX = 0.03
moon2.velX = -0.009

gravity_sim.TIMESTEP = 60 # set TIMESTEP (speed up factor) if needed

gravity_sim.start_sim() # start simulation!

# Note: this simulation does not use precise/exact values (only estimates) so the moon will not make a perfect orbit