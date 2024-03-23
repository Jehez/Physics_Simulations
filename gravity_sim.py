# get only necessary/required functions from pygame
from pygame.draw import circle as draw_circle
from pygame import init as init_pygame, QUIT
from pygame.display import set_mode as set_display_mode, set_caption, update as update_display
from pygame.time import Clock
from pygame.event import get as get_events


init_pygame() # initialize pygame
window_width, window_height = 750,750 # set window dimensions
window = set_display_mode((window_width,window_height)) # initialize window using pygame
clock = Clock() # initialize the clock

# Universal Gravitational constant in SI Unit
G = 6.67e-11

# for each frame, the planet is moved by some distance
# this motion represents a motion for a certain duration of time
# For each small step in the simulation, calculations are done taking into account the TIMESTEP
# For each calculation done for calculating acceleration, velocity and displacement, the time passed is assumed to be equal to the TIMESTEP
# However, this can cause inaccurate results at high values of TIMESTEP
# Simulations can vary by large margins if the TIMESTEP is increased with identical initial conditions
# As gravity is a weak force, time needs to be sped up by a large margin to get useful simulations
# To achieve this, each multiple simulations will be done per frame

# set default starting values for simulation
simulations_per_frame = 1
TIMESTEP = 1
FPS = 60

#function to add title to window
def add_title(title):   set_caption(title)

all_planets = [] # array/list to store all planets created

# Planet class
class planet:
    # object initializing function
    def __init__(self,x,y,mass,radius,color):
        self.x,self.y = x,y # initializing co-ordinates
        self.velX, self.velY = 0,0 # initializing velocities (x,y)
        self.mass, self.radius, self.color = mass, radius, color # set mass, radius and color
        all_planets.append(self)
    
    # draw planet
    def draw(self,win):
        draw_circle(win, self.color, (self.x, self.y), self.radius)
    
    # calculate acceleration towards another object (planet)
    def calc_acceleration(self,other_planet):
        # calculate distance between the 2 planets
        distance_x = other_planet.x - self.x
        distance_y = other_planet.y - self.y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        # To calculate acceleration:
        # Newton's law of gravitation:  F = G*m1*m2 / r^2 where G is the gravitational constant, m1 and m2 are masses of both bodies, r is the distance between the 2 bodies
        # but also, F=m*a
        # this gives us: a = G*m2/r^2
        # so the acceleration caused by the other planet is G*mass / distance squared
        acceleration = G*other_planet.mass/distance**2

        # acceleration is a vector
        # it will act on the 'self' planet in the direction of 'other' planet
        # Hence, the accleration vector forms a right angle traingle with equal angles as the displacement vector
        # ratios of the acceleration traingle will be equal to the ratios of the displacement triangle
        # acceleration_dimension/acceleration_magnitude = displacement_dimension/displacement_magnitude     (note that displacement magnitude is just distance)
        # This gives us:
        acceleration_x = acceleration*distance_x/distance
        acceleration_y = acceleration*distance_y/distance

        # we now return the resultant acceleration as a list (array) with 2 elements (x and y)
        return [acceleration_x, acceleration_y]
    
    def update_pos(self,other_planets):
        net_acceleration = [0,0] # array to store resultant acceleration due to gravity
        for planet in other_planets:
            if self == planet:  continue # don't count the 'self' planet as a body cannot exert gravitational force on itself
            acc_x,acc_y = self.calc_acceleration(planet)
            net_acceleration[0]+=acc_x
            net_acceleration[1]+=acc_y
        
        # for the given time frame, the acceleration is assumed to be constant/uniform
        # We know the acceleration, initial velocity and time period
        # the distance moved in the respective dimension/direction can be calculated using:
        # S = ut + 0.5*a*t^2
        displacement_x = self.velX*TIMESTEP + 0.5*net_acceleration[0]*TIMESTEP**2
        displacement_y = self.velY*TIMESTEP + 0.5*net_acceleration[1]*TIMESTEP**2

        # accordingly, the co-ordinates of the planet are updated
        self.x += displacement_x
        self.y += displacement_y

        # the velocities of the planet are also updated based on the formula v = u + a*t
        self.velX += net_acceleration[0]*TIMESTEP
        self.velY += net_acceleration[1]*TIMESTEP

def start_sim():
    # while loop to run simulation    
    flag = True
    while flag:
        clock.tick(FPS) # set fps
        window.fill((0,0,0)) # make background black

        for event in get_events(): # if the close button is clicked (Quit event triggered), the while loop should end
            if event.type == QUIT:  return
        
        # calculate net acceleration of all planets and update screen
        for _ in range(simulations_per_frame):
            for p in all_planets:
                p.update_pos(all_planets)
        for p in all_planets:    p.draw(window)
        update_display()
