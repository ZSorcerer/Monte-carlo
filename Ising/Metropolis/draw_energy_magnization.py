

import numpy as np
import matplotlib.pyplot as plt

import sys



Tstart=float(sys.argv[1])
Tend=float(sys.argv[2])
TSteps=int(sys.argv[3])

MC_step=int(sys.argv[4])


E_T_array=np.zeros(((TSteps+1),MC_step),dtype=np.float32)
m_T_array=np.zeros(((TSteps+1),MC_step),dtype=np.float32)
T_array=[]

filename_E="Energy_PerSpin_T=3.0.csv"
filename_m="Magnetization_PerSpin_T=3.0.csv"


E_T_array_all = np.loadtxt(open(filename_E),delimiter=",",skiprows=0)
m_T_array_all = np.loadtxt(open(filename_m),delimiter=",",skiprows=0)
for i in range(TSteps+1):
	T = Tstart + i * (Tend - Tstart) / TSteps;
	T_array.append(T)
	
	
	E_T_array[i] = E_T_array_all[(i*MC_step):(i+1)*MC_step]
	m_T_array[i] = m_T_array_all[(i*MC_step):(i+1)*MC_step]



fig = plt.figure(0,figsize=(31, 16))

plt.plot(np.arange(MC_step),E_T_array[0],'o-',ms=2,lw=1.0,color='blue',label='T=1')
#plt.plot(np.arange(MC_step),E_T_array[2],'o-',ms=2,lw=1.0,color='red',label='T=1.4')
plt.plot(np.arange(MC_step),E_T_array[4],'o-',ms=2,lw=1.0,color='yellow',label='T=1.8')
plt.plot(np.arange(MC_step),E_T_array[6],'o-',ms=2,lw=1.0,color='black',label='T=2.2')
plt.plot(np.arange(MC_step),E_T_array[8],'o-',ms=2,lw=1.0,color='m',label='T=2.6')
#plt.plot(np.arange(MC_step),E_T_array[10],'o-',ms=2,lw=1.0,color='c',label='T=3.0')

plt.axis([0,MC_step+1,-4,4])
plt.xlabel('step t',fontsize=25)
plt.ylabel('Energy_PerSpin',fontsize=25)

#params = {'legend.fontsize': 20,'legend.linewidth': 2}
#plt.rcParams.update(params)
#plt.text(10, 0.4,  r"Traing Step=%d" %Train_Step,color='black',fontsize=20);
plt.title("Energy_PerSpin %d steps" %MC_step,fontsize=20) 
plt.legend()
plt.savefig("Energy_PerSpin_%d_steps.png" %MC_step ,dpi=144)
plt.close(0)

fig = plt.figure(1,figsize=(31, 16))

plt.plot(np.arange(MC_step),m_T_array[0],'o-',ms=2,lw=1.0,color='blue',label='T=1')
#plt.plot(np.arange(MC_step),m_T_array[2],'o-',ms=2,lw=1.0,color='red',label='T=1.4')
plt.plot(np.arange(MC_step),m_T_array[4],'o-',ms=2,lw=1.0,color='yellow',label='T=1.8')
plt.plot(np.arange(MC_step),m_T_array[6],'o-',ms=2,lw=1.0,color='black',label='T=2.2')
plt.plot(np.arange(MC_step),m_T_array[8],'o-',ms=2,lw=1.0,color='m',label='T=2.6')
#plt.plot(np.arange(MC_step),m_T_array[10],'o-',ms=2,lw=1.0,color='c',label='T=3.0')

plt.axis([0,MC_step+1,-4,4])
plt.xlabel('step t',fontsize=25)
plt.ylabel('Magnetization_PerSpin',fontsize=25)

#params = {'legend.fontsize': 20,'legend.linewidth': 2}
#plt.rcParams.update(params)
#plt.text(10, 0.4,  r"Traing Step=%d" %Train_Step,color='black',fontsize=20);
plt.title("Magnetization_PerSpin %d steps" %MC_step,fontsize=20) 
plt.legend()
plt.savefig("Magnetization_PerSpin_%d_steps.png" %MC_step ,dpi=144)
plt.close(1)

