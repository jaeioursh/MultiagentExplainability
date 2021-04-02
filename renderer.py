

import numpy as np
import matplotlib
import pickle
from rover_domain_core_gym import RoverDomainGym

import matplotlib.pyplot as plt

imageIndex=0

nagents=5
sim = RoverDomainGym(nagents,100)

def render(data,hist):
    global imageIndex
    imageIndex+=1
    scale=.5
   
 
    plt.clf()
    
    
    
    plt.xlim(-data["World Width"]*scale,data["World Width"]*(1.0+scale))
    plt.ylim(-data["World Length"]*scale,data["World Length"]*(1.0+scale))
   

    if 1:
        markers=["o","*","s","p"]
        ntypes=4
        xpoints=[[] for i in range(ntypes)]
        ypoints=[[] for i in range(ntypes)]
        for i in range(len(data["Poi Positions"])):
            xpoints[i%ntypes].append(data["Poi Positions"][i,0])
            ypoints[i%ntypes].append(data["Poi Positions"][i,1])
        for i in range(ntypes):
            plt.scatter(xpoints[i],ypoints[i],label=str(i),s=150,marker=markers[i])
        plt.legend(["Type "+i for i in ["A","B","C","D"]])
    
    else:
        print("Single")
             
    points=[[]for i in range(nagents)]
    plt.scatter(hist[0,:,0],hist[0,:,1],s=20)
    for i in range(50):
        for j in range(nagents):
            points[j].append(hist[i][j])
    
    for i in range(nagents):
        x,y=np.array(points[i]).T
        plt.plot(x,y)
    
    #plt.savefig("ims/test"+str(imageIndex)+".png")
    plt.show()
    


with open("data5.pkl" , 'rb') as f:
    states,history,nets=pickle.load(f)


    render(sim.data,history)