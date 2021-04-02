
import pickle 
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering

with open("data13.pkl",'rb') as f:
    states,actions,g,d,nets=pickle.load(f)
    #print(states[0])
    #print(nets[0][0].hiddenToOutMat)
    #a=nets[0][0].get_action(states[0][0])
    #print(np.array(a))

def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)

def preproc(s):
    n1=len(s)
    n2=len(s[0])
    S=[]
    for i in range(n1):
        for j in range(n2):
            S.append(s[i][j])
    maxi=np.max(S,axis=0)
    mini=np.min(S,axis=0)
    for i in range(n1):
        for j in range(n2):
            s[i][j]=s[i][j]/(maxi-mini)-mini
    return s 
def pairwise_sim(s1,s2,d1,d2):
    n=len(s1)
    mat=np.zeros((n,n))
    dif=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            mat[i,j]=np.sqrt(np.sum((s1[i]-s2[i])**2.0))
            dif[i,j]=np.sqrt(np.sum((d1[i]-d2[j])**2.0))
            
    mat=1/(mat+1)
    mat/=np.sum(mat)
    


    #dif=1/(dif+0.01)
    #dif/=np.sum(dif)
    
    mat*=dif
    return np.sum(mat)



def sim_mat(d,s):
    nsamples=len(d)
    nagents=len(d[0])
    S=[[] for i in range(nagents)]
    D=[[] for i in range(nagents)]
    mat=np.zeros((nagents,nagents))

    for i in range(nagents):
        for j in range(nsamples):
            D[i].append(d[j][i])
            S[i].append(states[j][i])
    for i in range(nagents):
        for j in range(i):
            mat[i,j]=pairwise_sim(S[i],S[j],D[i],D[j])
            mat[j,i]=mat[i,j]
    return mat    
    

eplen=50
popsize=len(states)
IDX=0
for i in range(popsize):
    if g[i][-1]==1.75:
        IDX=i
        print(i)
print(IDX)



states=list(states[IDX])[-eplen:]
actions=list(actions[IDX])[-eplen:]
g=list(g[IDX])[-eplen:]
d=list(d[IDX])[-eplen:]


d=np.array(d)
plt.subplot(2,2,1)
end = d[-1]
summ=np.sum(d,axis=0)
count=summ/end
labels=[i for i in range(len(end))]
for i in range(len(end)):
    print(i,round(end[i],2))

#print(g)
plt.plot(d)
#plt.show()


plt.subplot(2,2,2)
model = AgglomerativeClustering(distance_threshold=0.000000, n_clusters=None,affinity="precomputed",linkage="complete",compute_full_tree=1)
states=preproc(states)
d=preproc(d)

X=sim_mat(d,states)
model = model.fit(X)
plt.title('Hierarchical Clustering Dendrogram')
# plot the top three levels of the dendrogram
plot_dendrogram(model, truncate_mode='level', p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")


plt.subplot(2,2,3)
plt.imshow(X)
plt.colorbar()

plt.subplot(2,2,4)
plt.bar(labels,end)
txt=[str(int(i)) for i in count]
for i in range(len(end)):
    plt.text(labels[i],end[i]-.1,txt[i],horizontalalignment='center')
plt.show()