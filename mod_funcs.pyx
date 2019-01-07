import numpy as np
cimport cython

cdef extern from "math.h":
    double sqrt(double m)

@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.

cpdef assignGlobalRewardMod(data):
    
    cdef int[:] itemHeld=data["Item Held"]
    cdef int number_agents = data['Number of Agents']
    cdef int number_pois = data['Number of POIs'] 
    cdef double minDistanceSqr = data["Minimum Distance"] ** 2
    cdef int historyStepCount = data["Steps"] + 1
    cdef int coupling = data["Coupling"]
    cdef double observationRadiusSqr = data["Observation Radius"] ** 2
    cdef double[:, :, :] agentPositionHistory = data["Agent Position History"]
    cdef double[:] poiValueCol = data['Poi Values']
    cdef double[:, :] poiPositionCol = data["Poi Positions"]
  
    
    cdef int poiIndex, stepIndex, agentIndex, observerCount
    cdef double separation0, separation1, closestObsDistanceSqr, distanceSqr, stepClosestObsDistanceSqr
    cdef double Inf = float("inf")
    
    cdef double globalReward = 0.0
 
    
    for poiIndex in range(number_pois//2):
        closestObsDistanceSqr = Inf
        for stepIndex in range(historyStepCount):
            # Count how many agents observe poi, update closest distance if necessary
            observerCount = 0
            stepClosestObsDistanceSqr = Inf
            for agentIndex in range(number_agents):
                # Calculate separation distance between poi and agent
                separation0 = poiPositionCol[poiIndex, 0] - agentPositionHistory[stepIndex, agentIndex, 0]
                separation1 = poiPositionCol[poiIndex, 1] - agentPositionHistory[stepIndex, agentIndex, 1]
                distanceSqr = separation0 * separation0 + separation1 * separation1
                
                # Check if agent observes poi, update closest step distance
                if distanceSqr < observationRadiusSqr and itemHeld[agentIndex]:
                    observerCount += 1
                    if distanceSqr < stepClosestObsDistanceSqr:
                        stepClosestObsDistanceSqr = distanceSqr
                        
                        
            # update closest distance only if poi is observed    
            if observerCount >= coupling:
                if stepClosestObsDistanceSqr < closestObsDistanceSqr:
                    closestObsDistanceSqr = stepClosestObsDistanceSqr
        
        # add to global reward if poi is observed 
        if closestObsDistanceSqr < observationRadiusSqr:
            if closestObsDistanceSqr < minDistanceSqr:
                closestObsDistanceSqr = minDistanceSqr
            globalReward += poiValueCol[poiIndex] / closestObsDistanceSqr
    
    data["Global Reward"] = globalReward
    data["Agent Rewards"] = np.ones(number_agents) * globalReward 
    
    
@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
cpdef doAgentSenseMod(data):
    """
     Sensor model is <aNE, aNW, aSW, aSE, pNE, pNE, pSW, pSE>
     Where a means (other) agent, p means poi, and the rest are the quadrants
    """
    cdef double obsRadius=data["Observation Radius"] ** 2
    cdef double viewDistance = data['View Distance'] ** 2
    
    cdef int number_agents = data['Number of Agents']
    cdef int number_pois = data['Number of POIs'] 
    cdef double minDistanceSqr = data["Minimum Distance"] ** 2
    cdef double[:, :] agentPositionCol = data["Agent Positions"]
    cdef double[:] poiValueCol = data['Poi Values']
    cdef double[:, :] poiPositionCol = data["Poi Positions"]
    cdef double[:, :] orientationCol = data["Agent Orientations"]
    npObservationCol = np.zeros((number_agents, 8), dtype = np.float64)
    
    
   
    
    cdef int[:] itemHeld
    
    if data["Sequential"]:
        itemHeld=data["Item Held"]
        npObservationCol = np.zeros((number_agents, 13), dtype = np.float64)
    else:
        npObservationCol = np.zeros((number_agents, 8), dtype = np.float64)
    cdef double[:, :] observationCol = npObservationCol
    
    
    cdef int agentIndex, otherAgentIndex, poiIndex, obsIndex
    cdef double globalFrameSeparation0, globalFrameSeparation1
    cdef double agentFrameSeparation0, agentFrameSeparation1

    cdef double distanceSqr
    
    
    for agentIndex in range(number_agents):

        # calculate observation values due to other agents
        for otherAgentIndex in range(number_agents):
            
            # agents do not sense self (ergo skip self comparison)
            if agentIndex == otherAgentIndex:
                continue
                
            # Get global separation vector between the two agents    
            globalFrameSeparation0 = agentPositionCol[otherAgentIndex,0] - agentPositionCol[agentIndex,0]
            globalFrameSeparation1 = agentPositionCol[otherAgentIndex,1] - agentPositionCol[agentIndex,1]
            
            # Translate separation to agent frame using inverse rotation matrix
            agentFrameSeparation0 = orientationCol[agentIndex, 0] * globalFrameSeparation0 + orientationCol[agentIndex, 1] * globalFrameSeparation1 
            agentFrameSeparation1 = orientationCol[agentIndex, 0] * globalFrameSeparation1 - orientationCol[agentIndex, 1] * globalFrameSeparation0 
            distanceSqr = agentFrameSeparation0 * agentFrameSeparation0 + agentFrameSeparation1 * agentFrameSeparation1
            
            if viewDistance > 0 and distanceSqr > viewDistance :
                continue
            
            # By bounding distance value we implicitly bound sensor values
            if distanceSqr < minDistanceSqr:
                distanceSqr = minDistanceSqr
        	
            
            # other is east of agent
            if agentFrameSeparation0 > 0:
                # other is north-east of agent
                if agentFrameSeparation1 > 0:
                    observationCol[agentIndex,0] += 1.0 / distanceSqr
                else: # other is south-east of agent
                    observationCol[agentIndex,3] += 1.0  / distanceSqr
            else:  # other is west of agent
                # other is north-west of agent
                if agentFrameSeparation1 > 0:
                    observationCol[agentIndex,1] += 1.0  / distanceSqr
                else:  # other is south-west of agent
                    observationCol[agentIndex,2] += 1.0  / distanceSqr



        # calculate observation values due to pois
        for poiIndex in range(number_pois):
            
            # Get global separation vector between the two agents    
            globalFrameSeparation0 = poiPositionCol[poiIndex,0] - agentPositionCol[agentIndex,0]
            globalFrameSeparation1 = poiPositionCol[poiIndex,1] - agentPositionCol[agentIndex,1]
            
            # Translate separation to agent frame unp.sing inverse rotation matrix
            agentFrameSeparation0 = orientationCol[agentIndex, 0] * globalFrameSeparation0 + orientationCol[agentIndex, 1] * globalFrameSeparation1 
            agentFrameSeparation1 = orientationCol[agentIndex, 0] * globalFrameSeparation1 - orientationCol[agentIndex, 1] * globalFrameSeparation0 
            distanceSqr = agentFrameSeparation0 * agentFrameSeparation0 + agentFrameSeparation1 * agentFrameSeparation1
            
            if viewDistance > 0 and distanceSqr > viewDistance:
                continue
            
            # By bounding distance value we implicitly bound sensor values
            if distanceSqr < minDistanceSqr:
                distanceSqr = minDistanceSqr
            
            # half of poi give a "key" and the other half are a "lock" which need multiple agents to unlock
            shift=0
            
            if (poiIndex < number_pois//2 and data["Sequential"]):
                shift = 4
                
                if (obsRadius > distanceSqr):
                    itemHeld[agentIndex]=1
                
                
                if ( itemHeld[agentIndex] ) :
                    observationCol[12]=1
            
            # poi is east of agent
            if agentFrameSeparation0> 0:
                # poi is north-east of agent
                if agentFrameSeparation1 > 0:
                    observationCol[agentIndex,4+shift] += poiValueCol[poiIndex]  / distanceSqr
                else: # poi is south-east of agent
                    observationCol[agentIndex,7+shift] += poiValueCol[poiIndex]  / distanceSqr
            else:  # poi is west of agent
                # poi is north-west of agent
                if agentFrameSeparation1 > 0:
                    observationCol[agentIndex,5+shift] += poiValueCol[poiIndex]  / distanceSqr
                else:  # poi is south-west of agent
                    observationCol[agentIndex,6+shift] += poiValueCol[poiIndex]  / distanceSqr
                    
    data["Agent Observations"] = npObservationCol

