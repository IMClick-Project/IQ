# Paqueterí­as y reiniciación del entorno de trabajo
import matplotlib.pyplot as plt; # Para graficas,ajuste paramétrico y correlación de determinación
import pandas as pd; import numpy as np; # Para trabajar tablas y arreglos
from sklearn.metrics import r2_score; # Para correlación de determinación
import os; import win32com.client as win32; # Para conectar aplicaciones 
plt.close(r"all"); # Cerrar todas las figuras anteriores
n=100; # Número de puntos de evaluación en general
######################################################################################################################## 
# Ajuste de propiedades de therminol 66
# Exportar datos de csv
dt66=pd.read_csv(r"t66.csv",header=None); dt66=pd.DataFrame(dt66).to_numpy();
MWt66=252; # Peso molecular [kg/kmol]
Tt66=dt66[:,0]+273.15; # Temperatura [K]
rhot66=dt66[:,1]/MWt66; # Densidad [kmol/m3]
ht66=dt66[:,2]*MWt66; # Entalpía [kJ/kmol]
# Ajuste por mínimos cuadrados, coeficiente de determinación y rango de operación de TT-6 y TT-7
G=np.vstack([Tt66**2,Tt66,np.ones(len(Tt66))]).T; pr=np.linalg.lstsq(G,rhot66,rcond=None)[0]; ph=np.linalg.lstsq(G,ht66,rcond=None)[0]; 
rhot66_pred=pr[0]*Tt66**2+pr[1]*Tt66+pr[2]; ht66_pred=ph[0]*Tt66**2+ph[1]*Tt66+ph[2]; R2r=r2_score(rhot66,rhot66_pred); R2h=r2_score(ht66,ht66_pred);
mindT=4; maxdT=10; minT67=230+273.15-maxdT; maxT67=265+273.15; # Mínima y máxima diferencia con mínima y máxima T en la operación de TT-6 y TT-7
print(r"Ajuste rho vs T: rho [kmol/m3]=("+str(pr[0])+r")T2+("+str(pr[1])+r")T+("+str(pr[2])+r"),R2="+str(R2r));
print(r"Ajuste h vs T: h [kJ/kmol]=("+str(ph[0])+r")T2+("+str(ph[1])+r")T+("+str(ph[2])+r"),R2="+str(R2h));
print(r"Mínimo rho [kmol/m3] en operación de TT-6 y TT-7: "+str(pr[0]*maxT67**2+pr[1]*maxT67+pr[2]));
print(r"Máximo rho [kmol/m3] en operación de TT-6 y TT-7: "+str(pr[0]*minT67**2+pr[1]*minT67+pr[2]));
print(r"Mínimo h [kJ/kmol] en operación de TT-6 y TT-7: "+str(ph[0]*minT67**2+ph[1]*minT67+ph[2]));
print(r"Máximo h [kJ/kmol] en operación de TT-6 y TT-7: "+str(ph[0]*maxT67**2+ph[1]*maxT67+ph[2]));
# Gráficas de datos reales rho y h con ajuste - Figura D.12
fig,ax1=plt.subplots(figsize=(7.5,6)); plt.title(r"Ajuste por mínimos cuadrados de propiedades de t66",fontweight=r"bold"); 
ax1.set_xlabel(r"$T$ $[K]$"); ax1.set_ylabel(r"$\overline{\rho}$ $[kmol/m^3]$",color=r"b"); plt.grid();
ax1.plot(Tt66,rhot66,r"b*",label=r"$\overline{\rho}$ Real"); ax1.plot(Tt66,rhot66_pred,r"b--",label=r"$\overline{\rho}$ Ajustado"); 
ax1.tick_params(axis=r"y",labelcolor=r"b"); ax2=ax1.twinx(); ax2.set_ylabel(r"$\overline{h}$ $[kJ/kmol]$",color=r"r"); 
ax2.plot(Tt66,ht66,r"r*",label=r"$\overline{h}$ Real"); ax2.plot(Tt66,ht66_pred,r"r--",label=r"$\overline{h}$ Ajustado"); 
ax2.tick_params(axis=r"y",labelcolor=r"r"); ax2.ticklabel_format(axis=r"y",style=r"sci",scilimits=(5,5));
ax2.fill([minT67,minT67,maxT67,maxT67],[0,2.1E5,2.1E5,0],color=r"k",alpha=0.2); plt.ylim(0,2.1E5);
fig.tight_layout(); plt.show(); fig.legend(loc=r"outside right"); fig.subplots_adjust(top=0.892,bottom=0.126,left=0.101,right=0.711);
plt.text(350.4,1.7e5,r"$R^2=$"+str(round(R2r,6)),color=r"b"); plt.text(300,6e4,r"$R^2=$"+str(round(R2h,6)),color=r"r");
plt.text(430,0.1e5,r"Operación de TT-6 y TT-7",color=r"k");
plt.savefig(r"t66.pdf"); 
# Gráfica de análisis de calor sensible - Figura D.16
Tintt6=np.linspace(minT67+maxdT,maxT67,n); # Posibles temperaturas de entrada TT-6 [°C]
dTtt6=np.linspace(mindT,maxdT,n); # Posibles variaciones de (TT-6)-(TT-7) [°C]
cs=np.zeros((len(Tintt6),len(dTtt6))); # Calor sensible h(TT-6)-h(TT-7) [kJ/kmol]
T6,dT=np.meshgrid(Tintt6,dTtt6);
for j in range(len(Tintt6)):
    for i in range(len(dTtt6)):
        cs[j][i]=ph[0]*(Tintt6[j]**2-(Tintt6[j]-dTtt6[i])**2)+ph[1]*(Tintt6[j]-(Tintt6[j]-dTtt6[i]));        
fig1=plt.figure(figsize=(7.5,6)); ax=fig1.add_subplot(projection=r"3d"); 
plt.title(r"Calor sensible de tt6",fontweight=r"bold"); ax.plot_surface(T6-273.15,dT,cs.T,cmap=r"autumn");
ax.ticklabel_format(axis=r"z",style=r"sci",scilimits=(3,3));
plt.tight_layout(); ax.view_init(elev=29,azim=-45,roll=0);
ax.set_xlabel(r"$TT-6$ $[°C]$"); ax.set_ylabel(r"$\Delta T$ $[°C]$"); ax.set_zlabel(r"$\Delta \overline{h}$ $[kJ/kmol]$"); plt.savefig(r"QR.pdf");
######################################################################################################################## 
# Propiedades de mezcla predominante de agua en el sumidero y agua fría del condensador
# Iniciar Aspen Plus
Propiedades=win32.Dispatch(r"Apwn.Document"); Propiedades.InitFromArchive2(os.path.abspath(r"Propiedades_termo_AP.bkp"));
rutaaf=r"\Data\Properties\Analysis\AGUACF"; rutasr=r"\Data\Properties\Analysis\SR";
rutac=r"\Data\Properties\Analysis\C"; rutatbubp=r"\Data\Properties\Analysis\TBUBP";
rutarhop=r"\Data\Properties\Analysis\RHOP";
# Agua fría
Tmaxout=45; # T máxima de salida [°C]
Propiedades.Tree.FindNode(rutaaf+r"\Input\UPPER\#1").Value=Tmaxout; Propiedades.Tree.FindNode(rutaaf+r"\Input\NPOINT\#1").Value=n;
Taf=np.zeros((n+1,1)); # Temperaturas [K]
rhoaf=np.zeros((n+1,1)); # Densidad [kmol/m3]
haf=np.zeros((n+1,1)); # Entalpía [kJ/kmol]
uaf=np.zeros((n+1,1)); # Energía interna [kJ/kmol] 
# Mezcla en sumidero y rehervidor
xasr=np.linspace(0.1,0,n); # Fracción másica de amoníaco 
P=np.linspace(7,16,10); # Presiones [bar]
for i in range(len(P)):    
    Propiedades.Tree.FindNode(rutac+r"\Input\LIST\#0\#"+str(i)).Value=P[i]; Propiedades.Tree.FindNode(rutac+r"\Input\LIST\#0\#"+str(i)).Value=P[i];
xsr,ysr=np.meshgrid(xasr,P);
rhosrl=np.zeros((len(xasr),len(P))); # Densidad en punto de burbuja [kmol/m3]
rhosrg=np.zeros((len(xasr),len(P))); # Densidad en punto de rocío [kmol/m3]
Propiedades.Tree.FindNode(rutasr+r"\Input\FLOW\WATER").Value=1-xasr[0];
Propiedades.Tree.FindNode(rutasr+r"\Input\FLOW\AMMONIA").Value=xasr[0];
# Mezcla en condensador
xac=np.linspace(0.9,1,n); # Fracción másica de amoníaco 
xc,yc=np.meshgrid(xac,P);
rhocl=np.zeros((len(xac),len(P))); # Densidad en punto de burbuja [kmol/m3]
rhocg=np.zeros((len(xac),len(P))); # Densidad en punto de rocío [kmol/m3]
Propiedades.Tree.FindNode(rutac+r"\Input\FLOW\WATER").Value=1-xac[0];
Propiedades.Tree.FindNode(rutac+r"\Input\FLOW\AMMONIA").Value=xac[0];
# Mezcla en postenfriamiento a 7,10,13 y 16 bar
Tbubp=np.zeros((1,10)); # Temperatura en el punto de burbuja [°C]
Tp=np.zeros((n+1,10)); # Temperaturas Tbub a Tbub-20 [°C]
rhop=np.zeros((n+1,10)); # Densidad líquida [kmol/m3]
# Primer reiniciar valores y ejecutar
Propiedades.Reinit; Propiedades.SuppressDialogs=1; Propiedades.Engine.Run2();
for i in range(1,n+2):
    Taf[i-1][0]=Propiedades.Tree.FindNode(rutaaf+r"\Output\PROP_DATA\TEMP"+"\\"+str(i)).Value;
    rhoaf[i-1][0]=Propiedades.Tree.FindNode(rutaaf+r"\Output\PROP_DATA\RHOMX\TOTAL"+"\\"+str(i)).Value;
    haf[i-1][0]=Propiedades.Tree.FindNode(rutaaf+r"\Output\PROP_DATA\HMX\TOTAL"+"\\"+str(i)).Value;
    uaf[i-1][0]=Propiedades.Tree.FindNode(rutaaf+r"\Output\PROP_DATA\UMX\TOTAL"+"\\"+str(i)).Value;
for i in range(len(P)):
    rhosrl[0][i]=Propiedades.Tree.FindNode(rutasr+r"\Output\PROP_DATA\RHOMX\TOTAL"+"\\"+str(2*i+1)).Value;
    rhosrg[0][i]=Propiedades.Tree.FindNode(rutasr+r"\Output\PROP_DATA\RHOMX\TOTAL"+"\\"+str(2*i+2)).Value;
    rhocl[0][i]=Propiedades.Tree.FindNode(rutac+r"\Output\PROP_DATA\RHOMX\TOTAL"+"\\"+str(2*i+1)).Value;
    rhocg[0][i]=Propiedades.Tree.FindNode(rutac+r"\Output\PROP_DATA\RHOMX\TOTAL"+"\\"+str(2*i+2)).Value;
for i in range(len(P)):
    Tbubp[0][i]=Propiedades.Tree.FindNode(rutatbubp+r"\Output\PROP_DATA\TBUB\TOTAL"+"\\"+str(i+1)).Value;
# Segundo a n reiniciar valores y ejecutar
for j in range(1,n):
    Propiedades.Tree.FindNode(rutasr+r"\Input\FLOW\WATER").Value=1-xasr[j]; Propiedades.Tree.FindNode(rutasr+r"\Input\FLOW\AMMONIA").Value=xasr[j];
    Propiedades.Tree.FindNode(rutac+r"\Input\FLOW\WATER").Value=1-xac[j]; Propiedades.Tree.FindNode(rutac+r"\Input\FLOW\AMMONIA").Value=xac[j];
    Propiedades.Reinit; Propiedades.SuppressDialogs=1; Propiedades.Engine.Run2();
    for i in range(len(P)):
        rhosrl[j][i]=Propiedades.Tree.FindNode(rutasr+r"\Output\PROP_DATA\RHOMX\TOTAL"+"\\"+str(2*i+1)).Value;
        rhosrg[j][i]=Propiedades.Tree.FindNode(rutasr+r"\Output\PROP_DATA\RHOMX\TOTAL"+"\\"+str(2*i+2)).Value;
        rhocl[j][i]=Propiedades.Tree.FindNode(rutac+r"\Output\PROP_DATA\RHOMX\TOTAL"+"\\"+str(2*i+1)).Value;
        rhocg[j][i]=Propiedades.Tree.FindNode(rutac+r"\Output\PROP_DATA\RHOMX\TOTAL"+"\\"+str(2*i+2)).Value;
# Estados post-enfriemiento en las diferentes P
for j in range(len(P)):
    Propiedades.Tree.FindNode(rutarhop+r"\Input\LOWER\#1").Value=Tbubp[0][j]-20; Propiedades.Tree.FindNode(rutarhop+r"\Input\UPPER\#1").Value=Tbubp[0][j]; 
    Propiedades.Tree.FindNode(rutarhop+r"\Input\NPOINT\#1").Value=n; Propiedades.Tree.FindNode(rutarhop+r"\Input\LIST\#0\#0").Value=P[j];
    Propiedades.Reinit; Propiedades.SuppressDialogs=1; Propiedades.Engine.Run2();
    for i in range(1,n+2):
        Tp[i-1][j]=Propiedades.Tree.FindNode(rutarhop+r"\Output\PROP_DATA\TEMP"+"\\"+str(i)).Value;
        rhop[i-1][j]=Propiedades.Tree.FindNode(rutarhop+r"\Output\PROP_DATA\RHOMX\TOTAL"+"\\"+str(i)).Value;
# Gráfica de agua fría - Figura D.21
fig2,ax1=plt.subplots(figsize=(7.5,6)); plt.title(r"Propiedades del agua fría en el condensador",fontweight=r"bold"); 
ax1.set_xlabel(r"$T$ $[°C]$"); ax1.set_ylabel(r"$\overline{\rho}$ $[kmol/m^3]$",color=r"b"); plt.grid();
ax1.plot(Taf,rhoaf,r"b-",label=r"$\overline{\rho}$"); ax1.tick_params(axis=r"y",labelcolor=r"b");  
ax2=ax1.twinx(); ax2.set_ylabel(r"$\overline{h}/\overline{u}$ $[kJ/kmol]$",color=r"r"); 
ax2.plot(Taf,haf,r"r-",label=r"$\overline{h}$"); ax2.plot(Taf,uaf,r"r.",label=r"$\overline{u}$");  
ax2.tick_params(axis=r"y",labelcolor=r"r"); ax2.ticklabel_format(axis=r"y",style=r"sci",scilimits=(5,5)); fig2.tight_layout(); 
plt.show(); fig2.legend(loc=r"outside right"); fig2.subplots_adjust(top=0.892,bottom=0.126,left=0.131,right=0.776); plt.savefig(r"af.pdf");
# Gráfica densidad en punto de burbuja de mezcla en sumidero y rehervidor - Figura D.14
fig3=plt.figure(figsize=(7.5,6)); ax=fig3.add_subplot(projection=r"3d"); 
plt.title(r"Densidad del punto de burbuja en el termosifón",fontweight=r"bold"); ax.plot_surface(xsr,ysr,rhosrl.T,cmap=r"winter");
plt.tight_layout(); ax.view_init(elev=27,azim=46,roll=0); plt.xticks([0.1,0.05,0]);
ax.set_xlabel(r"$x_a$"); ax.set_ylabel(r"$P$ $[bar]$"); ax.set_zlabel(r"$\overline{\rho}$ $[kmol/m^3]$"); plt.savefig(r"rhosrl.pdf");
# Gráfica densidad en punto de rocío de mezcla en sumidero y rehervidor - Figura D.15
fig4=plt.figure(figsize=(7.5,6)); ax=fig4.add_subplot(projection=r"3d"); 
plt.title(r"Densidad del punto de rocío en el termosifón",fontweight=r"bold"); ax.plot_surface(xsr,ysr,rhosrg.T,cmap=r"autumn");
plt.tight_layout(); ax.view_init(elev=32,azim=-49,roll=0); plt.xticks([0.1,0.05,0]);
ax.set_xlabel(r"$x_a$"); ax.set_ylabel(r"$P$ $[bar]$"); ax.set_zlabel(r"$\overline{\rho}$ $[kmol/m^3]$"); plt.savefig(r"rhosrg.pdf");
# Gráfica densidad en punto de burbuja de mezcla en condensador - Figura D.18
fig5=plt.figure(figsize=(7.5,6)); ax=fig5.add_subplot(projection=r"3d"); 
plt.title(r"Densidad del punto de burbuja en el condensador",fontweight=r"bold"); ax.plot_surface(xc,yc,rhocl.T,cmap=r"winter");
plt.tight_layout(); ax.view_init(elev=27,azim=45,roll=0); plt.xticks([0.9,0.95,1]);
ax.set_xlabel(r"$x_a$"); ax.set_ylabel(r"$P$ $[bar]$"); ax.set_zlabel(r"$\overline{\rho}$ $[kmol/m^3]$"); plt.savefig(r"rhocl.pdf");
# Gráfica densidad en punto de rocío de mezcla en condensador - Figura D.19
fig6=plt.figure(figsize=(7.5,6)); ax=fig6.add_subplot(projection=r"3d"); 
plt.title(r"Densidad del punto de rocío en el condensador",fontweight=r"bold"); ax.plot_surface(xc,yc,rhocg.T,cmap=r"autumn");
plt.tight_layout(); ax.view_init(elev=32,azim=-132,roll=0); plt.xticks([0.9,0.95,1]);
ax.set_xlabel(r"$x_a$"); ax.set_ylabel(r"$P$ $[bar]$"); ax.set_zlabel(r"$\overline{\rho}$ $[kmol/m^3]$"); plt.savefig(r"rhocg.pdf");
# Gráfica de densidad de mezcla post-enfriada (xa=0.95) - Figura D.20
fig7,ax1=plt.subplots(figsize=(7.5,6)); plt.title(r"Ejemplo de densidad de mezcla post-enfriada ($x_{a}$=0.95)",fontweight=r"bold"); 
ax1.set_xlabel(r"$T$ $[°C]$"); ax1.set_ylabel(r"$\overline{\rho}$ $[kmol/m^3]$"); plt.grid();
colorp=[r"#1f77b4",r"#fa861f",r"#39a641",r"#d62b2c"]; ax1.plot(Tp[-1,9],rhop[-1,9],r"k*",label=r"$T_{bub}$",markersize=9);
for i in [0,3,6,9]:
    ax1.plot(Tp[:,i],rhop[:,i],r"--",label=r"$P$ $[bar]$="+str(int(P[i])),linewidth=2,color=colorp[int(i/3)]);  
for i in [0,3,6,9]:
    ax1.plot(Tp[-1,i],rhop[-1,i],r"*",markersize=9,color=colorp[int(i/3)]);
fig7.legend(loc=r"outside right"); fig7.subplots_adjust(top=0.892,bottom=0.126,left=0.131,right=0.776); plt.savefig(r"rhop.pdf");
Propiedades.close(); Propiedades.quit();