import numpy as np
import matplotlib.pyplot as plt

import sys


Tstart=float(sys.argv[1])
Tend=float(sys.argv[2])
TSteps=int(sys.argv[3])

corr_step=int(sys.argv[4])


corrE_T_array=np.zeros(((TSteps+1),corr_step),dtype=np.float32)
corrm_T_array=np.zeros(((TSteps+1),corr_step),dtype=np.float32)
T_array=[]
for i in range(TSteps+1):
	T = Tstart + i * (Tend - Tstart) / TSteps;
	T_array.append(T)
	filename_E="auto_kE_T=%.2f.csv" %T
	filename_m="auto_km_T=%.2f.csv" %T
	corrE_T_array[i] = np.loadtxt(open(filename_E),delimiter=",",skiprows=0)
	corrm_T_array[i] = np.loadtxt(open(filename_m),delimiter=",",skiprows=0)







fig = plt.figure(0,figsize=(31, 16))

plt.plot(np.arange(corr_step),corrE_T_array[0],'o-',ms=2,lw=1.0,color='blue',label='auto_T=1')
plt.plot(np.arange(corr_step),corrE_T_array[1],'o-',ms=2,lw=1.0,color='red',label='auto_T=1.4')
plt.plot(np.arange(corr_step),corrE_T_array[2],'o-',ms=2,lw=1.0,color='yellow',label='auto_T=1.8')
plt.plot(np.arange(corr_step),corrE_T_array[3],'o-',ms=2,lw=1.0,color='black',label='auto_T=2.2')
plt.plot(np.arange(corr_step),corrE_T_array[4],'o-',ms=2,lw=1.0,color='m',label='auto_T=2.6')
plt.plot(np.arange(corr_step),corrE_T_array[5],'o-',ms=2,lw=1.0,color='c',label='auto_T=3.0')

plt.axis([0,400+1,0,0.9])
plt.xlabel('step t',fontsize=25)
plt.ylabel('auto_correlation $c_E(t)/ c_E(0)$',fontsize=25)

#params = {'legend.fontsize': 20,'legend.linewidth': 2}
#plt.rcParams.update(params)
#plt.text(10, 0.4,  r"Traing Step=%d" %Train_Step,color='black',fontsize=20);
plt.title("Energy auto_correlation %d steps" %corr_step,fontsize=40) 
plt.legend()
plt.savefig("auto_correlation_E_%d_steps.png" %corr_step ,dpi=144)
plt.close(0)

fig = plt.figure(1,figsize=(31, 16))

plt.plot(np.arange(corr_step),corrm_T_array[0],'o-',ms=2,lw=1.0,color='blue',label='auto_T=1')
plt.plot(np.arange(corr_step),corrm_T_array[1],'o-',ms=2,lw=1.0,color='red',label='auto_T=1.4')
plt.plot(np.arange(corr_step),corrm_T_array[2],'o-',ms=2,lw=1.0,color='yellow',label='auto_T=1.8')
plt.plot(np.arange(corr_step),corrm_T_array[3],'o-',ms=2,lw=1.0,color='black',label='auto_T=2.2')
plt.plot(np.arange(corr_step),corrm_T_array[4],'o-',ms=2,lw=1.0,color='m',label='auto_T=2.6')
plt.plot(np.arange(corr_step),corrm_T_array[5],'o-',ms=2,lw=1.0,color='c',label='auto_T=3.0')

plt.axis([0,corr_step+1,0,0.9])
plt.xlabel('step t',fontsize=25)
plt.ylabel('auto_correlation $c_m(t)/ c_m(0)$',fontsize=25)

params = {'legend.fontsize': 20,'legend.linewidth': 2}
plt.rcParams.update(params)
#plt.text(10, 0.4,  r"Traing Step=%d" %Train_Step,color='black',fontsize=20);
plt.title("Magnetization auto_correlation %d steps" %corr_step,fontsize=40) 
plt.legend()
plt.savefig("auto_correlation_m_%d_steps.png" %corr_step ,dpi=144)
plt.close(1)
