# Paqueterí­as, funciones y reiniciación del entorno de trabajo
import matplotlib.pyplot as plt; # Para graficar
import numpy as np; from math import sqrt,log; # Para trabajar arreglos
plt.close(r"all"); # Cerrar todas las figuras anteriores
n=500; # Número de puntos de evaluación en general
def F(P,R,npHF):
    if R!=1:
        alpha=((1-R*P)/(1-P))**(1/npHF); # Ec. (F.3)
        S=(alpha-1)/(alpha-R); # Ec. (F.4)
        # Cuidar casos donde log tenga valores negativos o divisiones con aproximadamente 0: Casos F<0.4 - Diseños no ideales
        try:
            return sqrt(R**2+1)*log((1-S)/(1-R*S))/(R-1)/log((2-S*(R+1-sqrt(R**2+1)))/(2-S*(R+1+sqrt(R**2+1)))); # Ec. (F.5)
        except:
            return;
    else:
        S=P/(npHF-(npHF-1)*P); # Ec. (F.6)
        # Cuidar casos donde log tenga valores negativos o divisiones con aproximadamente 0: Casos F<0.4 - Diseños no ideales
        try:
            return S*sqrt(2)/(1-S)/log((2-S*(2-sqrt(2)))/(2-S*(2+sqrt(2)))); # Ec. (F.7)
        except:
            return;
######################################################################################################################## 
# Cálculo de F en intercambiadores
RF=np.concatenate((np.linspace(0.1,1,10),np.linspace(1.2,2,5),np.array([2.5,3,4,6,8,10,15,20]))); # Casos de R
# Intercambiador 1-2
P12=np.array([0.95,0.9,0.85,0.81,0.76,0.72,0.68,0.65,0.61,0.59,0.53,0.48,0.45,0.41,0.38,0.33,0.28,\
              0.22,0.17,0.12,0.1,0.098,0.08]); # Límites de P
# Figura F.1
fig1,ax=plt.subplots(figsize=(12,6)); c12=np.empty(len(RF),dtype=r"object");
for i in range(len(RF)):
    Pi=np.linspace(1E-5,P12[i],n); Fi=np.zeros(n);
    for j in range(n):
        Fi[j]=F(float(Pi[j]),float(RF[i]),1);
    ax.plot(Pi,Fi); c12[i]=plt.gca().lines[-1].get_color();
plt.show(); plt.axis([0,1,0.5,1]); plt.grid(); plt.title(r"F de intercambiadores de calor 1-2",fontweight=r"bold"); 
ax.set_xlabel(r"$P$"); ax.set_ylabel(r"$F$"); fig1.subplots_adjust(top=0.88,bottom=0.11,left=0.06,right=0.975);
px12=[0.855,0.8,0.75,0.71,0.678,0.64,0.61,0.582,0.556,0.534,0.485,0.445,0.41,0.382,0.355,0.3,0.26,\
      0.205,0.14,0.105,0.085,0.055,0.04];
py12=[0.875,0.83,0.79,0.76,0.735,0.71,0.694,0.684,0.672,0.66,0.645,0.635,0.63,0.624,0.62,0.617,0.614,\
      0.612,0.611,0.611,0.68,0.61,0.68];
r12=[-47,-50,-52,-54,-57,-59,-62,-65,-68,-73,-76,-79,-81,-83,-84,-85,-86,-87,-88,-89,-90,-90,-90];
for i in range(len(RF)):    
    plt.text(px12[i],py12[i],r"$R$="+str(round(RF[i],1)),color=c12[i],backgroundcolor=r"w",rotation=r12[i]);
plt.savefig(r"F12.pdf");
# Intercambiador 2-4
P24=np.array([0.9992,0.99,0.975,0.95,0.917,0.885,0.847,0.81,0.77,0.732,0.665,0.6,0.548,0.5,0.458,0.4,0.38,\
              0.3585,0.3555,0.135,0.09992,0.09004,0.090004]); # Límites de P9
# Figura F.2
fig2,ax=plt.subplots(figsize=(12,6)); c24=np.empty(len(RF),dtype=r"object");
for i in range(len(RF)):
    Pi=np.linspace(1E-5,P24[i],n); Fi=np.zeros(n);
    for j in range(n):
        Fi[j]=F(float(Pi[j]),float(RF[i]),2);
    ax.plot(Pi,Fi); c24[i]=plt.gca().lines[-1].get_color();
plt.show(); plt.axis([0,1,0.5,1]); plt.grid(); plt.title(r"F de intercambiadores de calor 2-4",fontweight=r"bold"); 
ax.set_xlabel(r"$P$"); ax.set_ylabel(r"$F$"); fig2.subplots_adjust(top=0.88,bottom=0.11,left=0.06,right=0.975);
px24=[0.94,0.91,0.88,0.85,0.82,0.79,0.76,0.73,0.695,0.665,0.61,0.558,0.51,0.47,0.435,0.36,0.308,\
      0.235,0.155,0.115,0.092,0.06,0.04];
py24=[0.92,0.885,0.86,0.84,0.82,0.8,0.785,0.77,0.755,0.742,0.725,0.705,0.695,0.69,0.685,0.68,0.678,\
      0.675,0.675,0.611,0.68,0.61,0.68];
r24=[-46,-48,-50,-53,-55,-56,-58,-61,-63,-66,-68,-75,-81,-83,-84,-85,-87,-89,-89,-90,-90,-90,-90];
for i in range(len(RF)):    
    plt.text(px24[i],py24[i],r"$R$="+str(round(RF[i],1)),color=c12[i],backgroundcolor=r"w",rotation=r24[i]);
plt.savefig(r"F24.pdf");
######################################################################################################################## 
# Cálculo de dle en intercambiadores a partir de la Figura F.5
dsiE1=0.3048; # dsi [m] de E-1
dsiE2=0.438; # dsi [m] de E-2
dsi=np.array([484.576049,2491.852128])/1000; # dsi [m] obtenida de grabit
dsimdle=np.array([15.42467739,25.03240543])/1000; # dsi-dle [m] obtenida de grabit
G=np.vstack([dsi,np.ones(len(dsi))]).T; pdsi=np.linalg.lstsq(G,dsimdle,rcond=None)[0]; 
print("dle de E-1 [m]: "+str(dsiE1-pdsi[0]*dsiE1-pdsi[1]));
print("dle de E-2 [m]: "+str(dsiE2-pdsi[0]*dsiE2-pdsi[1]));