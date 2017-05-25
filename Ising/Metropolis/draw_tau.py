import numpy as np
import matplotlib.pyplot as plt

import sys

corr_tau = np.loadtxt(open("auto_tau.csv"),delimiter=",",skiprows=0)


T=corr_tau[:,0]
E=corr_tau[:,1]
m=corr_tau[:,2]


fig = plt.figure(1,figsize=(31, 16))

plt.plot(T,E,'o-',ms=5,lw=1.0,color='blue',label='auto_E')
plt.plot(T,m,'o-',ms=5,lw=1.0,color='red',label='auto_m')

#plt.axis([0,corr_step+1,0,1])
plt.xlabel('T',fontsize=25)
plt.ylabel('auto_correlation time $\\tau$',fontsize=25)

#params = {'legend.fontsize': 20,'legend.linewidth': 2}
#plt.rcParams.update(params)
#plt.text(10, 0.4,  r"Traing Step=%d" %Train_Step,color='black',fontsize=20);
plt.title("Ising 40x40 auto correlation time for different T",fontsize=20) 
plt.legend()
plt.savefig("auto_correlation_time.png",dpi=144)
plt.close(1)
