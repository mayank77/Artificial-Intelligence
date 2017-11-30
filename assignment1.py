# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:22:27 2017

@author: mayank
"""

import math
import timeit 
t = timeit.Timer(stmt="lst = ['c'] * 100")  
flag = 0

class puzzle8:
    def __init__(self):
        self.front=[] #To append the heuristic values
        self.GoalNode=['1','2','3','4','5','6','7','8','0']     #The Final State We Wish To Reach
        self.StartNode=['8','6','7','2','5','4','3','0','1'] #Default Initialization. FILLED IN BY USER
        for i in range(8,int(max(self.StartNode))-1,-1):
           self.GoalNode[i] = '0'
        self.PreviousNode=[]    #The Previous Configurations
        self.count=1
    
    def Solve(self):
        #self.StartNode=['8','1','3','4','0','2','7','6','5'] #The Initial Configuration 
        inf=0
        #self.StartNode=['8','6','7','2','5','4','3','0','1']
        self.nxtsucc(self.StartNode) #Send It Over For The Successor Computations
        nxNode=self.nxt() #Get the next plausible conguration
        print (nxNode) #Display the intermediate configuration
        a=nxNode
        self.count=1 #This was the first count step
        while nxNode!=self.GoalNode: #Run if final configuration has not been achieved yet
            #print(self.fronts)
            print(self.count) #Print which step it is
            self.count+=1 #Increment to demonstrate that it is the next step
            self.nxtsucc(nxNode) ##Send It Over For The Successor Computations
            nxNode=self.nxt() #Get the next plausible conguration
            if a==nxNode:
                inf=inf+1
                if inf==10:
                    print "UNSOLVABLE"
                    break
            else:
                inf=0
            a = nxNode
            print (a) #Display the intermediate configuration
            if nxNode!=self.GoalNode:
                print(self.count) #Print which step it is
                self.count+=1 #Increment to demonstrate that it is the next step
                self.nxtsucc(nxNode) ##Send It Over For The Successor Computations
                nxNode=self.nxt() #Get the next plausible conguration
                b = nxNode
                print (b) #Display the intermediate configuration
        print 'result',nxNode #Final Result

                
    def boundries(self,location):
        lst=[[1,2,3],[4,5,6],[7,8,9]] #Idealistic Configuration
        low=0 #The Minimum in That Row
        high=0 #The Maximum in That Row
        for i in lst: #Looking For The Minimum and Maximum in The Row Which Has The Zero/Blank
            if location in i:
                low=i[0]
                high=i[2]
        
        return [low,high]
    
    def nxt(self):
        nxNode=[]
        tNode=[]
        while True:
            hrCost= 999999  #Setting at a very high value (imitating the role of infinity in this case)
            for i in self.fronts:
                    if(i[-1]<hrCost):   #Look for the least heuristic value 
                        hrCost=i[-1]    #Extract the heuristic value (at the end) which was appended to each list in the list of lists
                        nxNode=i[0:-1]  #Extract the configuration with least heuristic value
                        tNode=i          #Configuration along with Value of the configuration with the least heuristic value
            
            if tNode in self.PreviousNode and tNode in self.fronts:
                self.fronts.remove(tNode) #Remove from the list of current configurations (Already visited configuration)
                self.PreviousNode.append(tNode) #Add to the list of visited configurations
                
            else:
                self.PreviousNode.append(tNode) #Add to the list of visited configurations
                return nxNode 

    
    def heruistic(self,node):
        #In this case, I use a combination of both the heuristics mentioned in the lecture slides.
        herMisplaced=0      #Number of Tiles in Non-Target Location in the Current State
        herDist=0   #Distance From Element and It's Correct Element Position (Manhattan)
        
        for i in range(9):
            if node[i]!=self.GoalNode[i] and node[i]!='0':   #Not in the correct position
                herMisplaced +=1    #Add one extra mis-placed element count
        for i in node:
            herDist +=math.fabs(node.index(i)-self.GoalNode.index(i))%3 #The Top-Left Count For Each Element   
        if flag==0:
            totalHerst=herDist+herMisplaced #Combining it as a heuristic as A*
        if flag==1:
            totalHerst=1*herDist+10*herMisplaced #Combining it as a heuristic as WA*
        if flag==2:
            totalHerst=0*herDist+1*herMisplaced #Combining it as a heuristic as WA*
        node.append(totalHerst) #Return Heuristic Value
        return node
        
        
    
    def nxtsucc(self,node=[]): #To get the successor nodes, the program will look for an empty space and the allowed move and will return
    #an array consisting of the available moves and their heuristic values.
        subNode=[]
        getZeroLocation=node.index('0')+1 #Finding Index of 0 -- Added 1 Since Indexing Starts from Zero
        subNode.extend(node) #Extending The List By Appending Values From The Iterable i.e node

        boundry=self.boundries(getZeroLocation) #boundry[0] will have minimum value and boundry[1] will have maximum value
        self.fronts=[]
                
        if getZeroLocation+3<=9:    #Not In The Last Row (Since we check swap with bottom here)
            temp=subNode[node.index('0')] #Which is essentially zero
            subNode[node.index('0')]=subNode[node.index('0')+3] #Checking w.r.t bottom
            subNode[node.index('0')+3]=temp #Swapping w.r.t bottom i.e 0 is swapped with the element below it.
            self.fronts.append(self.heruistic(subNode)) #Get Heuristic Value
            subNode=[]
            subNode.extend(node) #Reset : Extending The List By Appending Values From The Iterable i.e node
        if getZeroLocation-3>=1: #Not In The Top Row (Since we check swap with upper-most row here)
            temp=subNode[node.index('0')] #Which is essentially zero
            subNode[node.index('0')]=subNode[node.index('0')-3] #Checking w.r.t top
            subNode[node.index('0')-3]=temp #Swapping w.r.t top i.e 0 is swapped with the element above it.
            self.fronts.append(self.heruistic(subNode)) #Get Heuristic Value
            subNode=[]
            subNode.extend(node) #Reset : Extending The List By Appending Values From The Iterable i.e node
        if getZeroLocation-1>=boundry[0]: #Not In The Left Row (Since we check swap with left row here)
            temp=subNode[node.index('0')] #Which is essentially zero
            subNode[node.index('0')]=subNode[node.index('0')-1] #Checking w.r.t left
            subNode[node.index('0')-1]=temp #Swapping w.r.t left i.e 0 is swapped with the element left of it.
            self.fronts.append(self.heruistic(subNode)) #Get Heuristic Value
            subNode=[]
            subNode.extend(node) #Reset : Extending The List By Appending Values From The Iterable i.e node
        if getZeroLocation+1<=boundry[1]: #Not In The Right Row (Since we check swap with right row here)
            temp=subNode[node.index('0')] #Which is essentially zero
            subNode[node.index('0')]=subNode[node.index('0')+1] #Checking w.r.t right
            subNode[node.index('0')+1]=temp #Swapping w.r.t right i.e 0 is swapped with the element right of it.
            self.fronts.append(self.heruistic(subNode)) #Get Heuristic Value
            subNode=[]
            subNode.extend(node) #Reset : Extending The List By Appending Values From The Iterable i.e node

#FLAG = 0 IS A*
#FLAG = 1 IS WA*
#FLAG = 2 IS GREEDY BFS
puzzle=puzzle8()     #Creating an Object
puzzle.Solve()      #Solve The Puzzle Now
t1 = timeit.Timer(stmt="lst = ['c' for x in xrange(100)]")  
print t1.timeit()-t.timeit()
