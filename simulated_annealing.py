import numpy as np
import matplotlib.pyplot as plt


"""randomly spreading particles"""
def arrange_charges(n,r):
    xy = np.zeros((2,n))                    #empty 2D array for n charges
    alpha = np.random.uniform(0,2*np.pi,n)  # random angle
    rad = np.random.uniform(0,r,n)          # random radius
    xy[0,] = rad * np.cos(alpha)            # x coordinates
    xy[1,] = rad * np.sin(alpha)            # y coordinates
    return xy


"""distance between all pairs of particles"""
def distances(x,n):
    d = np.zeros(0)
    for i in range(n-1):            # all charges 1 to n-1
        for j in range(i+1,n):      # all charges i+1 to n
            # pythagorus theorem to calculate each distance
            d = np.append(d,np.sqrt((x[0,i]-x[0,j])**2 + (x[1,i]-x[1,j])**2))
    return d # array of d_1,2 ... d_1,n ... d_n-1,n


"""Calculate energy of system"""
def energy(x,n):
    d = distances(x,n) # create array all all distances
    W = 0.5 * sum(1/d) # equation for Energy (all charges are equal)
    return W


"""randomly moving particles"""
def random_move(x,n,r,d):
    xnew = np.array(x)                          # dummy array equal to array of coordiantes
    rx = np.random.choice((0,1))    # random x or y coordinate
    ry = np.random.randint(0,n)     # random charge
    xnew[rx,ry] = x[rx,ry] + np.random.choice((-d,d)) # change random charge by +-d
    if np.any((xnew[0,]**2 + xnew[1,]**2) > r**2) == True: # if a charge is out of disc
        #repeat until all charges are within disc
        while np.any((xnew[0,]**2 + xnew[1,]**2) > r**2) == True:
            xnew[rx,ry] = x[rx,ry] + np.random.choice((-d,d))
    return xnew # return new array of coordinates



"""SET_UP"""
r = 10 # radius of disc
n = 8 # number of charges
c  = np.ones(n) # each charge
delta = 0.1 # amount to change the particle position by
m = 100000 # number of time steps
T = np.logspace(2,-5,m) # Temperature
W_plot = []
#var_plot = []


disc = arrange_charges(n,r)                 # start with initial arrangement of charges
for a in range(m):
    W_in = energy(disc,n)                   # initial energy
    disc_new = random_move(disc,n,r,delta)  # new candidate
    W_out = energy(disc_new,n)              # new energy
    dW = W_out - W_in                       # change in energy
    # Acceptance Test 
    if np.random.uniform() < np.exp((-dW)/T[a]):
        disc = disc_new                     # accept candidte
        W_plot.append(W_out)
    else:                                   #reject candidate
        W_plot.append(W_in)
    #var_plot.append(np.var(W_plot))
print(disc)
    
    
#plt.plot(range(m),W_plot)
#plt.show()
"""plot disc"""
theta = np.linspace(0, 2*np.pi, 100)
d1 = r*np.cos(theta)
d2 = r*np.sin(theta)
plt.plot(d1,d2, color='k')

"""plot charges"""
plt.scatter(disc[0,],disc[1,], label = 'charges')
plt.axis('scaled')
plt.axis('off')
plt.legend(loc = 'upper right')
plt.show
