import numpy as np
import matplotlib.pyplot as plt
import time
import pickle
import os
import copy
from concurrent.futures import ProcessPoolExecutor

class Agent:
    """
    Agent class encapsulates the information about the position and phenotpye of the agent as well as the agent's current birth and relocation rate.

        Parameters:
            birth (array like): the associated birth rate at each resource level
            hop (array like): relocation rate (a.k.a hopping rate) of the agent at resource levels 1 to 5, which comprises the agent's phenotype
            x, y (int): the x and y coordinate of the agent's location in the 2-dimensional environment
            pos (int,int): the agent's current location
            b (int): the agent's current birth rate
            h (float): the agent's current relocation rate
        Methods:
            updatepos(x,y): update the agent's location to (x,y) and update its current birth and relocation rate accordingly
    """

    def __init__(self, birth, hop, x, y):
        self.birth = tuple(birth)
        self.hop = list(hop)
        self.pos = (x, y)
        # resource goes as 0, 1, 2, 3, 4
        self.b = self.birth[int(resource[x, y])]
        self.h = self.hop[int(resource[x, y])]

    def updatepos(self, x, y):
        self.pos = (x, y)
        # resource goes as 0, 1, 2, 3, 4
        self.b = self.birth[int(resource[x, y])]
        self.h = self.hop[int(resource[x, y])]

    def __str__(self):
        return 'hopping rate {} at location {}'.format(self.hop, self.pos)

    def __repr__(self):
        return 'Agent({},{},{},{})'.format(self.birth, self.hop, *self.pos)


class Agent_network():
    def __init__(self, birth, hop, x, y):
        self.birth = tuple(birth)
        self.hop = list(hop)
        self.pos = (x, y)
        # resource goes as 0, 1, 2, 3, 4
        self.b = self.birth[int(resource[x, y])]
        self.h = self.hop[int(resource[x, y])]

    def updatepos(self, x, y):
        self.pos = (x, y)
        # resource goes as 0, 1, 2, 3, 4
        self.b = self.birth[int(resource[x, y])]
        self.h = self.hop[int(resource[x, y])]



def get_num(a, n):
    """
    Count agent numbers at all the locations

        Parameters: 
            a (array_like): list of agent object;
            n (int): size of the square environment
        Return:
            num (array_like): entry at i,j represents the number of agent at location (i,j)
    """
    num = np.zeros((n, n), dtype=int)
    for pos in [a[i].__dict__['pos'] for i in range(len(a))]:
        num[pos] += 1
    return num


def get_i(x, arr, l, r):
    """
    Binary search for the index of an element in a sorted list

        Parameters:
            x (float): target to be located for
            arr (array_like): a sorted list where the target will be located at
            l (int): left pointer, usually start with 0
            r (int): right pointer, usually start with len(a)
        Return:
            i (int): index of the element so that arr[i]<=x<=arr[i+1]
    """
    if x <= arr[0]:
        return 0
    else:
        while l <= r:
            mid = l + int((r - l)/2)
            # Check if x is present at mid
            if arr[mid] < x and arr[mid+1] >= x:
                return mid+1
            # If x is greater, ignore left half
            elif arr[mid+1] < x:
                l = mid + 1
            # If x is smaller, ignore right half
            else:
                r = mid
        raise Exception("Target not found")


def uniform_resource(x, y):
    """Return a uniformly generated 2-dimensional numpy array representing the resource level at each site"""
    rng = np.random.default_rng()
    return rng.choice([0, 1, 2, 3, 4], size=(x, y))


def exponetial_resource(x, y, c):
    rng = np.random.default_rng()
    p = [np.exp(-i*c) for i in range(5)]
    w = p/np.sum(p)
    return rng.choice([0, 1, 2, 3, 4], size=(x, y), p=w)


def intialcondtiongenerator_uniform(hop_high=10, n=128, m=500, birth=[0, 1, 2, 3, 4]):
    """Generate a list of agents with randomly chosen relocation rates and locations; locations do not repeat
    """
    rng = np.random.default_rng()
    pos = np.array([[i//n, i % n]
                   for i in rng.choice(n*n, m, replace=False)])
    return [Agent(birth, hop, x, y) for hop, x, y in zip(rng.uniform(0, hop_high, (m, 5)), pos[:, 0], pos[:, 1])]

def evolve_gillespie(birth=[0, 1, 2, 3, 4], tot_iter=201, env_size=128, birth_noise=0.05, hop_high=10,
                     save_data=False, trial=0,  save_iter=50, agents=500, duration_iter=0.3, carrying_capacity=1, c=0, simulation_notes=None):
    print('Running')
    rng = np.random.default_rng()
    a = intialcondtiongenerator_uniform(
        birth=birth, hop_high=hop_high, n=env_size, m=agents)
    if save_data == True:
        _path = './evolve_data' + \
            '/{}'.format(time.strftime("%Y_%m_%d_%H_%M",
                         time.localtime()))+'/trial_{}'.format(trial)
#         _path = './evolve_data/b5_c_plane'+'/b5_{}_c_{}'.format(birth[-1],c)+'/trial_{}'.format(trial)
#         _path = './evolve_data/noise_std' + '/std_{}_with_agents_number'.format(birth_noise) + '/trial_{}'.format(trial)
        os.makedirs(_path, exist_ok=True)
        info = {"lattice": "{}*{}".format(env_size, env_size), "exponential_coefficient": c, "total_iteartion": tot_iter, "evolve_time": duration_iter, "noise": birth_noise,
                "carrying_capacity": carrying_capacity, "initial_angent_number": agents, "data_stored_every": save_iter, "notes": simulation_notes}
        with open(_path+'/simulation_info.txt', "wb") as fp:
            pickle.dump(info, fp)
        with open(_path+'/resource.txt', "wb") as fp:
            pickle.dump(resource, fp)
        with open(_path+'/iteration_00', "wb") as fp:
            pickle.dump(a, fp)

    for iteration in range(tot_iter):
        t = 0
        num = get_num(a, env_size)
        br = [a[i].b for i in range(len(a))]
        hr = [a[i].h for i in range(len(a))]
        brsum = sum(br)
        tot_rates = brsum + sum(hr)  # total rates

        br_cumsum = np.cumsum(br)
        hr_cumsum = np.cumsum(hr)
        while t < duration_iter:

            dt = -np.log(rng.random()) / tot_rates
            t = t + dt
            r = tot_rates * rng.random()

            if r < brsum:
                # birth
                i = get_i(r, br_cumsum, 0, len(a)-1)
                hop_advance = [[1, 0], [0, 1], [-1, 0],
                               [0, -1]][rng.integers(0, 4)]
                pos_new = (np.array(a[i].pos)+np.array(hop_advance)) % env_size

                if num[pos_new[0], pos_new[1]] < carrying_capacity:
                    noise = rng.normal(0, birth_noise, 5)
                    hop_new = np.clip(np.array(a[i].hop)+noise, 0, hop_high)
                    a.append(Agent(birth, hop_new, pos_new[0], pos_new[1]))
                    num[pos_new[0], pos_new[1]] += 1
                    br.append(a[-1].b)
                    hr.append(a[-1].h)
                    brsum += a[-1].b
                    tot_rates += a[-1].b+a[-1].h
                    br_cumsum = np.append(br_cumsum, a[-1].b+br_cumsum[-1])
                    hr_cumsum = np.append(hr_cumsum, a[-1].h+hr_cumsum[-1])

            else:
                # hopping
                i = get_i(r, brsum+hr_cumsum, 0, len(a)-1)
                hop_advance = [[1, 0], [0, 1], [-1, 0],
                               [0, -1]][rng.integers(0, 4)]
                pos_new = (np.array(a[i].pos)+np.array(hop_advance)) % env_size

                if num[pos_new[0], pos_new[1]] < carrying_capacity:
                    num[pos_new[0], pos_new[1]] += 1
                    num[a[i].pos[0], a[i].pos[1]] -= 1
                    a[i].updatepos(pos_new[0], pos_new[1])
                    brsum += a[i].b-br[i]
                    tot_rates += a[i].b-br[i]+a[i].h-hr[i]
                    br_cumsum[i:] += a[i].b-br[i]
                    hr_cumsum[i:] += a[i].h-hr[i]
                    br[i] = a[i].b
                    hr[i] = a[i].h

        if len(a) > agents:
            # bring back the population back to its initial size
            reset = rng.choice(len(a), agents, replace=False)
            a = [a[i] for i in reset]
        if save_data == True:
            if iteration % save_iter == 0:
                with open(_path+'/iteration_{}'.format(iteration), "wb") as fp:
                    pickle.dump(a, fp)

    return a

resource = uniform_resource(128, 128)
if __name__ == '__main__':
    trials_in_parallel = 20  # number of trials to run in parallel
    ###Scale it down to if the number of cores available on your machine CPU is less than 20, otherwise it can run longer###
    total_iterations = 20001 # number of iterations to run
    start_time = time.time()

    with ProcessPoolExecutor() as executor:
        test = [executor.submit(evolve_gillespie, birth=[0, 1, 2, 3, 4], tot_iter=total_iterations, env_size=128, birth_noise=0.05, hop_high=10,
                                save_data=True, trial=i, save_iter=50, agents=500, duration_iter=0.3, carrying_capacity=1, simulation_notes='Just for fun') for i in range(trials_in_parallel)]
   
    print("--- %s seconds ---" % (time.time() - start_time))