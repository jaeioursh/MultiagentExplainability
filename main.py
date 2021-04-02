"""
An example using the rover domain gym-style interface and the standard, included CCEA learning algorithms.
This is a minimal example, showing the minimal Gym interface.
"""
import numpy as np

from rover_domain_core_gym import RoverDomainGym
import code.ccea_2 as ccea
import code.agent_domain_2 as domain
import mods
from multiq.learner import learner
from sys import argv,exit
import pickle
from collections import deque


episodeCount = 15000  # Number of learning episodes
populationSize = 50

nagents=10
RENDER=0


sim = RoverDomainGym(nagents,50)
#mods.recipePoi(sim)
obs=sim.reset()


sim.data["Coupling"]=5
sim.data['Number of Agents']=nagents
sim.data["Act Freq"]=10

obs_size=len(obs[0])




ccea.initCcea(input_shape=obs_size, num_outputs=2, num_units=32)(sim.data)
populationSize=len(sim.data['Agent Populations'][0])
SAMPLES=500
STATES=[deque(maxlen=SAMPLES) for i in range(populationSize)]
ACTIONS=[deque(maxlen=SAMPLES) for i in range(populationSize)]
G=[deque(maxlen=SAMPLES) for i in range(populationSize)]
D=[deque(maxlen=SAMPLES) for i in range(populationSize)]
COUNT=0

for episodeIndex in range(episodeCount):
    sim.data["Episode Index"] = episodeIndex
    
    GlobalRewards=[]
    DiffRewards=[]
    for worldIndex in range(populationSize):
        sim.data["World Index"]=worldIndex
        
        
            
        obs = sim.reset()
        
        ccea.assignCceaPolicies(sim.data)
        #mods.assignHomogeneousPolicy(sim)

        done = False
        stepCount = 0
        
        while not done:


            
            domain.doAgentProcess(sim.data)

            jointAction = sim.data["Agent Actions"]
            
            obs2, reward, done, info = sim.step(jointAction)
            
            STATES[worldIndex].append(np.array(obs))
            ACTIONS[worldIndex].append(np.array(jointAction))
            G[worldIndex].append(sim.data["Global Reward"])
            D[worldIndex].append(np.array(sim.data["Agent Rewards"]))

            obs=obs2
            stepCount += 1
        #print(reward)
        
        if sim.data["Global Reward"]==1.75:
            COUNT+=1
            
        GlobalRewards.append(sim.data["Global Reward"])    
        DiffRewards.append(sim.data["Agent Rewards"])
        ccea.rewardCceaPolicies(sim.data)
    idx=np.argmax(GlobalRewards)
    print(episodeIndex,GlobalRewards[idx],DiffRewards[idx]) 
    if COUNT>10:
        with open("data13.pkl",'wb') as f:
            #data=[STATES,np.array(sim.data["Agent Position History"]),sim.data["Agent Policies"]]
            data=[STATES,ACTIONS,G,D,sim.data['Agent Populations']]
            pickle.dump(data,f)
        exit()
    ccea.evolveCceaPolicies(sim.data)