# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:54:58 2017

@author: mayank
"""

import math as mt
import random
import numpy as np
import matplotlib.pyplot as plt 



class cell(object):

    def __init__(self, state):
        self.state = state
        self.ti = [1,1,1,1]
        self.q = [0,0,0,0]
        self.utility = [0,0,0,0]

    def ti(self):
        return self.ti
    
    def q(self):
        return self.q

    def utility(self):
        return self.utility
        

state = []
r = [0,0,0,0,0,0,-1,0,0,0,1]
for i in range(0,11):
    state.append(cell(i))
    
state[10].utility = [1,1,1,1]
state[6].utility = [-1,-1,-1,-1]
    
S = 0
n = 1

plot_counter = []
q0 = []
q1 = []
q2 = []
q3 = []
q4 = []
q5 = []
q6 = []
q7 = []
q8 = []
q9 = []
q10 = []

while(n<800000):
    
    if(n%100==0):
        plot_counter.append(n)
        q0.append( max(state[0].q) )
        q1.append( max(state[1].q) )
        q2.append( max(state[2].q) )
        q3.append( max(state[3].q) )
        q4.append( max(state[4].q) )
        q5.append( max(state[5].q) )
        q6.append( max(state[6].q) )
        q7.append( max(state[7].q) )
        q8.append( max(state[8].q) )
        q9.append( max(state[9].q) )
        q10.append( max(state[10].q) )
    
    if S== 10:
        up = 0
        down = 0
        right = 0
        left = 0

    if ((S>=7 and S<=9)or S==1):
        up = S
    elif (S>=2 and S<=4):
        up = S+3
    elif (S==0 or S==5 or S==6):
        up = S+4
        

        
    if(S==8 or S<=3):
        down = S
    elif (S>=5 and S<=7):
        down = S-3
    elif (S==4 or S==9):
        down = S-4



    
    if (S==3 or S==4 or S==6):
        right = S
    elif(S != 10):
        right = S+1
  


      
    if (S==0 or S==4 or S==7 or S==5):
        left = S
    elif(S != 10):
        left = S-1
    
    MAB = []
    MAB.append(state[S].utility[0]/state[S].ti[0] + mt.sqrt((2*mt.log(n))/state[S].ti[0])) #UP
    MAB.append(state[S].utility[1]/state[S].ti[1] + mt.sqrt((2*mt.log(n))/state[S].ti[1])) #RIGHT
    MAB.append(state[S].utility[2]/state[S].ti[2] + mt.sqrt((2*mt.log(n))/state[S].ti[2])) #DOWN
    MAB.append(state[S].utility[3]/state[S].ti[3] + mt.sqrt((2*mt.log(n))/state[S].ti[3])) #LEFT
    
    chosen = MAB.index(max(MAB))
    
    rnd = random.random()
    if rnd<=0.1:
        taken = (chosen-1)%4
    elif rnd<=0.2:
        taken = (chosen+1)%4
    else:
        taken = chosen
    
    if (taken == 0 ):
        nxt_taken = up
    if (taken == 1 ):
        nxt_taken = right
    if (taken == 2 ):
        nxt_taken = down
    if (taken == 3 ):
        nxt_taken = left
        
    state[S].q[chosen] = (1-0.01)*state[S].q[chosen] + 0.01*(r[nxt_taken] + 0.95*max(state[nxt_taken].q))
    state[S].ti[chosen] =  state[S].ti[chosen] + 1
    state[S].utility[chosen] = (r[nxt_taken] + 0.95*max(state[nxt_taken].q))
    
    S = nxt_taken   
    n = n + 1
    
for i in range(0,11):
    if state[i].q.index(max(state[i].q))==0:
        print "UP"
    if state[i].q.index(max(state[i].q))==1:
        print "RIGHT"
    if state[i].q.index(max(state[i].q))==2:
        print "DOWN"
    if state[i].q.index(max(state[i].q))==3:
        print "LEFT"
    
    print max(state[i].q)
#print n
plt.plot(plot_counter,q0)
plt.plot(plot_counter,q1)
plt.plot(plot_counter,q2)
plt.plot(plot_counter,q3)
plt.plot(plot_counter,q4)
plt.plot(plot_counter,q5)
plt.plot(plot_counter,q6)
plt.plot(plot_counter,q7)
plt.plot(plot_counter,q8)
plt.plot(plot_counter,q9)
plt.plot(plot_counter,q10)
