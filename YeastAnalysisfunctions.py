import re
import scipy
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

def CountMotifs(currentDF, motiflist,column='ADseq',plothist=True):
    for motif in motiflist:
        tempcol = []
        for seq in currentDF[column]:
            hits = re.search(motif,seq)
            if hits:
                matches = re.findall(motif,seq)
                tempcol.append(len(matches))
            else:
                tempcol.append(0)
        currentDF[motif]=tempcol
        if plothist:
            plt.hist(currentDF[Activity],150)
            indx = (currentDF[motif]>0)&(currentDF.Recovered)
            tempDF = currentDF[indx]
            notDF = currentDF[~indx]
            test = stats.ttest_ind(tempDF[Activity],notDF[Activity], equal_var=False)
            print(motif)
            print('%.1f (n=%i) with vs %.1f without'%(np.mean(tempDF[Activity]),sum(indx),np.mean(notDF[Activity])))
            print(test)
            plt.hist(tempDF[Activity],50,alpha=.5)
            plt.show()
    return currentDF

def ReturnMotifLocations(currentDF, motif,column='Seq'):
    tempcol = []
    for seq in currentDF[column]:
        hits = re.search(motif,seq)
        if hits:
            tempcol.append(hits.start())
        else:
            tempcol.append(-1)
    return tempcol

def plot2ProperitesSpacePoints(CurrentDF,PropertySet, Activity, Figname):
    fig = plt.figure(figsize=(10,5))
    
    SortedDF=CurrentDF.sort_values(by=Activity,ascending=True)
    minXprop, maxXprop = min(SortedDF[PropertySet[0]]),max(SortedDF[PropertySet[0]])
    minYprop, maxYprop = min(SortedDF[PropertySet[1]]),max(SortedDF[PropertySet[1]])
    
    Xs,Ys,activities,medians,medX,medY = [],[],[],[],[],[]
    print( '%i %i %i %i' %(minXprop, maxXprop,    minYprop, maxYprop))
    counts,markersizes = [],[]
    #systematically step through the grid of property space.
    for i in  np.arange(minXprop,maxXprop+1,1):
        for j in np.arange(minYprop,maxYprop+1,1):
            indx = (SortedDF[PropertySet[0]]==i)&((SortedDF[PropertySet[1]]==j))
            if sum(indx)>0:
                counts.append(sum(indx))
#                 markersizes.append(np.sqrt(sum(indx))*5)
                markersizes.append((sum(indx)))

                tempDF = SortedDF[indx]
                # make lists for plotting
                Xs.append(i) 
                Ys.append(j)
                activities.append(tempDF[Activity])
                medians.append(np.median(tempDF[Activity])) #hold medians for plotting.

    print(min(markersizes))
    print( max(markersizes))
    plt.scatter(Xs,Ys,c=medians,s=markersizes,cmap='plasma',marker='o') # marker size represents #of points
#     plt.scatter(medX,medY,c=medians,s=70,cmap='plasma',marker='s')# constant marker size.
    cbar =plt.colorbar()
    cbar.set_label('Median Activity')
    #plt.xlabel(labelDict[PropertySet[0]]),
    #plt.ylabel(labelDict[PropertySet[1]])
    plt.yticks([5,10,15])  

#     plotWT()
    plt.legend(frameon=False,fontsize=8)
    plt.savefig(Figname+'.pdf')
    plt.show()
    
def visualize_AA_Changes(AD_DF,WT,plotname,color='r',colname='shortname'):
    fig3, axes = plt.subplots( figsize=(18,len(AD_DF)*.3+1))
    ypos = 0
    
    # print WT
    for pos, ADaa in enumerate(WT):
        plt.text(pos,ypos, ADaa, color='k',fontsize=14, fontweight='bold')
    plt.text(pos+3,ypos,'WT',fontsize=12)
    ypos+=1
    # for each variant
    for j,entry in AD_DF.iterrows():
        AD = entry.ADseq
        for pos, ADaa in enumerate(AD):
            if ADaa == WT[pos]:
                # print AA in black if it is WT
                plt.text(pos,ypos, ADaa, color='k',fontsize=14, fontweight='bold')
            else:
                # print AA in red if it is NOT WT
                plt.text(pos,ypos, ADaa, color=color,fontsize=14, fontweight='bold')

#         plt.text(pos+3,ypos,'%.1f'%entry[currentItem],fontsize=12)

        plt.text(pos+6,ypos,entry[colname],fontsize=12)
        ypos+=1
    plt.axis([-1, pos+12, ypos,-1])
    plt.xticks([]),    plt.yticks([])
    plt.title(plotname)
    plt.savefig('Figures/'+Folder+plotname+'MutantList.pdf')
    plt.show()