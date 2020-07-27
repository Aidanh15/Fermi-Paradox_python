# Fermi's paradox:
#for a given number of advanced civilisations + an average radio bubble size,
#estimate the probability that any advanced civilisations will intercept any other civ's radio communication.
#radio bubbles represented on a 2d model of Milky Way

#Strategy:
# 1. Estimate the num of advanced civilisations with the Drake equation.
# 2. Choose a size range for their radio bubbles.
# 3. Estimate the probability of one detecting the other.
# 4. represent Earths radio bubble graphically. 



# Most recent (2017) Drake equation solution was estimated to be 15.6X10^6 or 15,600,000 potential civs. 
# radio bubble radius: 30-250 LY(light years)  --> assume peak detection capability, not yet possible to detect 250 LY bubbles.
# estimating probability of detection:
# compartmentalize the galaxy into a series of radio bubbles (equivalent volumes) by (volume of milky way disc / volume of radio bubble)
# radio bubbles will be randomly distributed across the galaxy disc in "equivalent" square volumes (as opposed to disc).
# output presented as probability of detection vs ratio of civilisations per volume(chances of two civs in same volume area of galaxy is 1 in 10000000)

from random import randint
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt 


NUM_EQUIV_VOLUMES = 1000 #Number of locations in which to place civilisations
MAX_CIVS = 5000 # MAX estimated no. of other advanced civs.
TRIALS = 1000 #No. of times to model a given number of civs.
CIV_STEP_SIZE = 100 # civilisations count step size

x = [] # Ratio of civs per volume
y = [] # Probability of detection

for num_civs in range(2, MAX_CIVS + 2, CIV_STEP_SIZE):
    civs_per_vol = num_civs / NUM_EQUIV_VOLUMES
    num_single_civs = 0
    for trial in range(TRIALS):
        locations = []  # eq. volumes containing a civilization
        while len(locations) < num_civs:
            location = randint(1, NUM_EQUIV_VOLUMES)
            locations.append(location)
        overlap_count = Counter(locations)
        overlap_rollup = Counter(overlap_count.values())
        num_single_civs += overlap_rollup[1]

    prob = 1 - (num_single_civs / (num_civs * TRIALS))

    # print ratio of civs-per-volume vs. probability of 2+ civs per location
    print("{:.4f}  {:.4f}".format(civs_per_vol, prob))
    x.append(civs_per_vol)
    y.append(prob)

coefficients = np.polyfit(x, y, 4) 
p = np.poly1d(coefficients)
print("\n{}".format(p))
xp = np.linspace(0, 5)
_ = plt.plot(x, y, '.', xp, p(xp), '-')
plt.ylim(-0.5, 1.5)
plt.show()

