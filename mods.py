import datetime
from code.reward_2 import * # Agent Reward 
from code.curriculum import * # Agent Curriculum
from mod_funcs import * 


def globalRewardMod(sim):
    sim.data["Mod Name"] = "global"
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] =assignGlobalReward
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def differenceRewardMod(sim):
    sim.data["Mod Name"] = "difference"
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] =assignDifferenceReward
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)

def dppRewardMod(sim):
    sim.data["Mod Name"] = "dpp"
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] =assignDppReward
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)



def globalRewardSizeCurrMod10(sim):
    sim.data["Schedule"] = ((10.0, 2000), (50.0,3000))
    sim.data["Mod Name"] = "globalSizeCurr10"
    sim.trainBeginFuncCol.insert(0, setCurriculumWorldSize)
    sim.testBeginFuncCol.insert(0, restoreWorldSize)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] =assignGlobalReward
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def globalRewardSizeCurrMod20(sim):
    sim.data["Schedule"] = ((20.0, 2000), (50.0,3000))
    sim.data["Mod Name"] = "globalSizeCurr20"
    sim.trainBeginFuncCol.insert(0, setCurriculumWorldSize)
    sim.testBeginFuncCol.insert(0, restoreWorldSize)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] =assignGlobalReward
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
        
def globalRewardSizeCurrMod30(sim):
    sim.data["Schedule"] = ((30.0, 2000), (50.0,3000))
    sim.data["Mod Name"] = "globalSizeCurr30"
    sim.trainBeginFuncCol.insert(0, setCurriculumWorldSize)
    sim.testBeginFuncCol.insert(0, restoreWorldSize)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] =assignGlobalReward
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def globalRewardSizeCurrMod40(sim):
    sim.data["Schedule"] = ((40.0, 2000), (50.0,3000))
    sim.data["Mod Name"] = "globalSizeCurr40"
    sim.trainBeginFuncCol.insert(0, setCurriculumWorldSize)
    sim.testBeginFuncCol.insert(0, restoreWorldSize)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] =assignGlobalReward
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
        

def globalRewardCoupCurrMod1(sim):
    sim.data["Schedule"] = sim.data["Schedule"] = ((1, 2000), (6, 3000))
    sim.data["Mod Name"] = "globalCoupCurr1"
    sim.trainBeginFuncCol.insert(0, setCurriculumCoupling)
    sim.testBeginFuncCol.insert(0, restoreCoupling)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignGlobalReward 
    
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def globalRewardCoupCurrMod2(sim):
    sim.data["Schedule"] = sim.data["Schedule"] = ((2, 2000), (6, 3000))
    sim.data["Mod Name"] = "globalCoupCurr2"
    sim.trainBeginFuncCol.insert(0, setCurriculumCoupling)
    sim.testBeginFuncCol.insert(0, restoreCoupling)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignGlobalReward 
    
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def globalRewardCoupCurrMod3(sim):
    sim.data["Schedule"] = sim.data["Schedule"] = ((3, 2000), (6, 3000))
    sim.data["Mod Name"] = "globalCoupCurr3"
    sim.trainBeginFuncCol.insert(0, setCurriculumCoupling)
    sim.testBeginFuncCol.insert(0, restoreCoupling)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignGlobalReward 
    
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def globalRewardCoupCurrMod4(sim):
    sim.data["Schedule"] = sim.data["Schedule"] = ((4, 2000), (6, 3000))
    sim.data["Mod Name"] = "globalCoupCurr4"
    sim.trainBeginFuncCol.insert(0, setCurriculumCoupling)
    sim.testBeginFuncCol.insert(0, restoreCoupling)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignGlobalReward 
    
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def globalRewardCoupCurrMod5(sim):
    sim.data["Schedule"] = sim.data["Schedule"] = ((5, 2000), (6, 3000))
    sim.data["Mod Name"] = "globalCoupCurr5"
    sim.trainBeginFuncCol.insert(0, setCurriculumCoupling)
    sim.testBeginFuncCol.insert(0, restoreCoupling)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignGlobalReward 
    
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
##################################################################################


        
def differenceRewardSizeCurrMod10(sim):
    sim.data["Schedule"] = ((10.0, 2000), (50.0,3000))
    sim.data["Mod Name"] = "differenceSizeCurr10"
    sim.trainBeginFuncCol.insert(0, setCurriculumWorldSize)
    sim.testBeginFuncCol.insert(0, restoreWorldSize)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignDifferenceReward
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def differenceRewardSizeCurrMod20(sim):
    sim.data["Schedule"] = ((20.0, 2000), (50.0,3000))
    sim.data["Mod Name"] = "differenceSizeCurr20"
    sim.trainBeginFuncCol.insert(0, setCurriculumWorldSize)
    sim.testBeginFuncCol.insert(0, restoreWorldSize)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignDifferenceReward
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
        
def differenceRewardSizeCurrMod30(sim):
    sim.data["Schedule"] = ((30.0, 2000), (50.0,3000))
    sim.data["Mod Name"] = "differenceSizeCurr30"
    sim.trainBeginFuncCol.insert(0, setCurriculumWorldSize)
    sim.testBeginFuncCol.insert(0, restoreWorldSize)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignDifferenceReward
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def differenceRewardSizeCurrMod40(sim):
    sim.data["Schedule"] = ((40.0, 2000), (50.0,3000))
    sim.data["Mod Name"] = "differenceSizeCurr40"
    sim.trainBeginFuncCol.insert(0, setCurriculumWorldSize)
    sim.testBeginFuncCol.insert(0, restoreWorldSize)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignDifferenceReward
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
        

def differenceRewardCoupCurrMod1(sim):
    sim.data["Schedule"] = sim.data["Schedule"] = ((1, 2000), (6, 3000))
    sim.data["Mod Name"] = "differenceCoupCurr1"
    sim.trainBeginFuncCol.insert(0, setCurriculumCoupling)
    sim.testBeginFuncCol.insert(0, restoreCoupling)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignDifferenceReward 
    
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def differenceRewardCoupCurrMod2(sim):
    sim.data["Schedule"] = sim.data["Schedule"] = ((2, 2000), (6, 3000))
    sim.data["Mod Name"] = "differenceCoupCurr2"
    sim.trainBeginFuncCol.insert(0, setCurriculumCoupling)
    sim.testBeginFuncCol.insert(0, restoreCoupling)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignDifferenceReward 
    
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def differenceRewardCoupCurrMod3(sim):
    sim.data["Schedule"] = sim.data["Schedule"] = ((3, 2000), (6, 3000))
    sim.data["Mod Name"] = "differenceCoupCurr3"
    sim.trainBeginFuncCol.insert(0, setCurriculumCoupling)
    sim.testBeginFuncCol.insert(0, restoreCoupling)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignDifferenceReward 
    
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def differenceRewardCoupCurrMod4(sim):
    sim.data["Schedule"] = sim.data["Schedule"] = ((4, 2000), (6, 3000))
    sim.data["Mod Name"] = "differenceCoupCurr4"
    sim.trainBeginFuncCol.insert(0, setCurriculumCoupling)
    sim.testBeginFuncCol.insert(0, restoreCoupling)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignDifferenceReward 
    
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
def differenceRewardCoupCurrMod5(sim):
    sim.data["Schedule"] = sim.data["Schedule"] = ((5, 2000), (6, 3000))
    sim.data["Mod Name"] = "differenceCoupCurr5"
    sim.trainBeginFuncCol.insert(0, setCurriculumCoupling)
    sim.testBeginFuncCol.insert(0, restoreCoupling)
    
    dateTimeString = datetime.datetime.now().strftime("%m_%d_%Y %H_%M_%S_%f")
    print("Starting %s test at\n\t%s\n"%(sim.data["Mod Name"], dateTimeString))
    
    # Agent Reward 
    sim.data["Reward Function"] = assignDifferenceReward 
    
    
    sim.data["Performance Save File Name"] = "log/%s/%s/performance/perf %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Trajectory Save File Name"] = "log/%s/%s/trajectory/traj %s.csv"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
    sim.data["Pickle Save File Name"] = "log/%s/%s/pickle/data %s.pickle"%\
        (sim.data["Specifics Name"], sim.data["Mod Name"], dateTimeString)
        
##############################
#
#name:assignHomogeneousPolicy
#
#desc:assigns the same policy to each agent
#
#call function after sim.reset
#note: data["World Index"] is used to determine which 
#population to use and must also be set
##############################            
        
def assignHomogeneousPolicy(sim):
    data=sim.data
    number_agents = data['Number of Agents']
    populationCol = data['Agent Populations']
    worldIndex = data["World Index"]
    policyCol = [None] * number_agents
    for agentIndex in range(number_agents):
        policyCol[agentIndex] = populationCol[0][worldIndex]
    data["Agent Policies"] = policyCol 


##############################
#
#name:poiVelocity(sim)
#
#desc:poi move with a seeded random velocity
#
#call function after each sim.step 
##############################    
def poiVelocity(sim):
    data=sim.data
    
    if not "Poi Velocity" in data:
        state=np.random.get_state()
        np.random.seed(123)
        data["Poi Velocity"]=np.random.random(data["Poi Positions"].shape)-.5  
        np.random.set_state(state)   
    data["Poi Positions"]+=data["Poi Velocity"]*0.5
    
##############################
#
#name:abilityVariation
#
#desc:agents have varying max speeds from 50% to 100%
#
#call function after action is calculated
##############################

        
def abilityVariation(sim):
    data=sim.data
    
    variation=np.linspace(0.5,1.0, sim.data["Number of Agents"])
    
    for n in range(sim.data["Number of Agents"]):
        sim.data["Agent Actions"][n,:] *= variation[n]  
              
##############################
#
# name:sequentialPoi
#
# desc:agents must go to poi type-a to recieve a "key" 
# and then group at poi type-b to open the "lock" and
# recieve a reward. Poi[0:n/2] = Type B and Poi[n/2:n] = Type A
#
#call function after sim is created and after each sim.reset
##############################
def sequentialPoi(sim):

    sim.data["Sequential"]=True
    sim.data["Observation Function"]=doAgentSenseMod
    
    sim.data["Reward Function"]=assignGlobalRewardMod
    sim.data["Item Held"] =np.zeros((sim.data["Number of Agents"]), dtype = np.int32)
    if not "View Distance" in sim.data: sim.data["View Distance"]= -1
    
##############################
#
#name:lowVisibility
#
#desc:agents can only see poi within 15 units
#
#call function after sim is created
##############################
    
def lowVisibility(sim):
    if not "Sequential" in sim.data: sim.data["Sequential"]= False
    
    sim.data["View Distance"]=15    
	
    sim.data["Observation Function"]=doAgentSenseMod


def simpleReward(data):
    number_agents=data["Number of Agents"]
    globalReward=np.sum(data["Item Held"])
    data["Global Reward"] = globalReward
    data["Agent Rewards"] = np.ones(number_agents) * globalReward

    
##############################
#
# name:recipePoi
#
# desc: A recipe of POI types is given to the agent. The agents 
# must go to each poi on the list to recieve a reward. The global reward 
# is determined by the number of agents which complete the recipe
#  
#
#call function after sim is created and before each sim.reset
##############################
def recipePoi(sim):

    
    sim.data["Observation Function"]=doAgentSenseRecipe2
    #sim.data["Reward Function"]=assignGlobalRewardSimple  #reward for each recipe completed
    sim.data["Reward Function"]=simpleReward              #reward for each step of recipe completed 
    
    sim.data["Recipe"] = np.array([0,3,2],dtype=np.int32) #recipe, each item is a POI type from 0 to (N-Poi Types)-1 
    sim.data["Recipe Size"]=len(sim.data["Recipe"])
    sim.data["Ordered"] = 1                              #flag for whether order matters
    sim.data["Number of POI Types"] = 4
    sim.data["Coupling Limit"]=5                            #max number of agents which can see view a poi at a time 
    sim.data["Item Held"] =np.zeros((sim.data["Number of Agents"],sim.data["Recipe Size"]), dtype = np.int32)



