# Paqueterí­as, funciones y reiniciación del entorno de trabajo
import matplotlib.pyplot as plt; # Para graficar
from math import sqrt; # Funciones matemáticas
import numpy as np; # Para trabajar arreglos
from scipy.optimize import curve_fit; # Para ajuste paramétrico
from sklearn.metrics import r2_score; # Para correlación de determinación
plt.close(r"all"); # Cerrar todas las figuras anteriores
def CV_porcigual(vp,alpha,CV_max):
    # Calcular CV para válvulas isoporcentuales dada vp y CV_max=CV|vp=1 / flujo inherente con Ec. (8.11)
    return CV_max*alpha**(vp-1);
def q_qmax(alpha,FV,f_,vp):
    # Calcular q/qmax para válvulas isoporcentuales con característica de flujo en instalación relacionada a Ec. (8.11)
    return alpha**(vp-1)*sqrt((1+FV**2*(1-f_)/f_)/(1+FV**2*(1-f_)/f_*(alpha**(vp-1))**2));
def CV_porcigual2(vp,alpha,CV_max):
    # Calcular CV para válvulas isoporcentuales dada vp y CV_max=CV|vp=1 / flujo inherente con Ec. (8.12)
    return CV_max*(alpha*vp)/(1+(alpha-1)*vp);
def q_qmax2(alpha,FV,f_,vp):
    # Calcular q/qmax para válvulas isoporcentuales con característica de flujo en instalación relacionada a Ec. (8.12)
    return (alpha*vp)/(1+(alpha-1)*vp)*sqrt((1+FV**2*(1-f_)/f_)/(1+FV**2*(1-f_)/f_*((alpha*vp)/(1+(alpha-1)*vp))**2));
def q(vp,q_max,F,f,alpha):
    # q con característica de flujo en instalación relacionada a Ec. (8.12)
    return q_max*(alpha*vp)/(1+(alpha-1)*vp)*np.sqrt((1+(F**2*(1-f)/f))/(1+(F**2*(1-f)/f)*((alpha*vp)/(1+(alpha-1)*vp))**2));
######################################################################################################################## 
# Datos de característica de flujo inherente
pvp=np.linspace(0,1,11);
CV_LV1=[4.2*0.0001,0.13,0.18,0.27,0.4,0.6,0.88,1.3,1.9,2.9,4.2];
CV_TV1=[62*0.0001,2.3,3.5,5.1,7.5,11,16,24,35,52,62];	
CV_PV2=[106*0.0001,4.6,6.6,9.8,14,21,28,41,69,90,106];	
CV_FV1=[0.47*0.0001,0.02,0.03,0.05,0.08,0.11,0.16,0.22,0.29,0.45,0.47];
# Ajuste paramétrico y correlación de determinación para cada válvula con Ec. (8.11)
colores=[r"#1f77b4",r"#fa861f",r"#39a641",r"#d62b2c"]; fig,ax=plt.subplots(figsize=(7,7)); plt.title(r"Característica de flujo inherente",fontweight=r"bold"); 
ax.set_ylabel(r"$C_V$ $[US\:gpm/\sqrt{psi}]$"); ax.set_xlabel(r"$vp$"); plt.grid();
popt=curve_fit(lambda vp,alpha:CV_porcigual(vp,alpha,CV_LV1[-1]),pvp,CV_LV1)[0]; CV_LV1_pred=CV_porcigual(pvp,*popt,CV_LV1[-1]); R2_CV_LV1=r2_score(CV_LV1,CV_LV1_pred);
ax.plot(pvp,CV_LV1,r"k*",label=r"Datos"); ax.plot(pvp,CV_LV1_pred,r"k--",label=r"Ec. (8.11)"); 
ax.plot(pvp,CV_LV1,r"*",color=colores[0]); ax.plot(pvp,CV_LV1_pred,r"--",color=colores[0]); alpha=str(round(popt[0],4)); CV_max=str(round(CV_LV1[-1],4)); R2=str(round(R2_CV_LV1,4));
plt.text(0.002,95,r"$\bf{LV-1:}$$\:C_V=($"+CV_max+r"$)($"+alpha+r"$^{vp-1}),\:R^2=$"+R2,color=colores[0],backgroundcolor=r"w"); alpha_LV1=popt[0];
popt=curve_fit(lambda vp,alpha:CV_porcigual(vp,alpha,CV_TV1[-1]),pvp,CV_TV1)[0]; CV_TV1_pred=CV_porcigual(pvp,*popt,CV_TV1[-1]); R2_CV_TV1=r2_score(CV_TV1,CV_TV1_pred);
ax.plot(pvp,CV_TV1,r"*",color=colores[1]); ax.plot(pvp,CV_TV1_pred,r"--",color=colores[1]); alpha=str(round(popt[0],4)); CV_max=str(round(CV_TV1[-1],4)); R2=str(round(R2_CV_TV1,4));
plt.text(0.002,90,r"$\bf{TV-1:}$$\:C_V=($"+CV_max+r"$)($"+alpha+r"$^{vp-1}),\:R^2=$"+R2,color=colores[1],backgroundcolor=r"w");  alpha_TV1=popt[0];
popt=curve_fit(lambda vp,alpha:CV_porcigual(vp,alpha,CV_PV2[-1]),pvp,CV_PV2)[0]; CV_PV2_pred=CV_porcigual(pvp,*popt,CV_PV2[-1]); R2_CV_PV2=r2_score(CV_PV2,CV_PV2_pred);
ax.plot(pvp,CV_PV2,r"*",color=colores[2]); ax.plot(pvp,CV_PV2_pred,r"--",color=colores[2]); alpha=str(round(popt[0],4)); CV_max=str(round(CV_PV2[-1],4)); R2=str(round(R2_CV_PV2,4));
plt.text(0.002,85,r"$\bf{PV-2:}$$\:C_V=($"+CV_max+r"$)($"+alpha+r"$^{vp-1}),\:R^2=$"+R2,color=colores[2],backgroundcolor=r"w"); alpha_PV2=popt[0];
popt=curve_fit(lambda vp,alpha:CV_porcigual(vp,alpha,CV_FV1[-1]),pvp,CV_FV1)[0]; CV_FV1_pred=CV_porcigual(pvp,*popt,CV_FV1[-1]); R2_CV_FV1=r2_score(CV_FV1,CV_FV1_pred);
ax.plot(pvp,CV_FV1,r"*",color=colores[3]); ax.plot(pvp,CV_FV1_pred,r"--",color=colores[3]); alpha=str(round(popt[0],4)); CV_max=str(round(CV_FV1[-1],4)); R2=str(round(R2_CV_FV1,4));
plt.text(0.002,80,r"$\bf{FV-1:}$$\:C_V=($"+CV_max+r"$)($"+alpha+r"$^{vp-1}),\:R^2=$"+R2,color=colores[3],backgroundcolor=r"w");  alpha_FV1=popt[0];
ax.legend(loc=r"upper left"); plt.axis([-0.02,1.02,-1,110]); plt.savefig(r"CV_vp_inherente.png");
# Ajuste paramétrico y correlación de determinación para cada válvula con Ec. (8.12)
colores=[r"#1f77b4",r"#fa861f",r"#39a641",r"#d62b2c"]; fig1,ax=plt.subplots(figsize=(7,7)); plt.title(r"Característica de flujo inherente",fontweight=r"bold"); 
ax.set_ylabel(r"$C_V$ $[US\:gpm/\sqrt{psi}]$"); ax.set_xlabel(r"$vp$"); plt.grid();
popt=curve_fit(lambda vp,alpha:CV_porcigual2(vp,alpha,CV_LV1[-1]),pvp,CV_LV1)[0]; CV_LV1_pred=CV_porcigual2(pvp,*popt,CV_LV1[-1]); R2_CV_LV1=r2_score(CV_LV1,CV_LV1_pred);
ax.plot(pvp,CV_LV1,r"k*",label=r"Datos"); ax.plot(pvp,CV_LV1_pred,r"k--",label=r"Ec. (8.12)"); 
ax.plot(pvp,CV_LV1,r"*",color=colores[0]); ax.plot(pvp,CV_LV1_pred,r"--",color=colores[0]); alpha=str(round(popt[0],4)); CV_max=str(round(CV_LV1[-1],4)); R2=str(round(R2_CV_LV1,4));
plt.text(0.002,95,r"$\bf{LV-1:}$$\:C_V=("+CV_max+r")\left[\dfrac{"+alpha+r"vp}{1+("+alpha+r"-1)vp}\right],\:R^2=$"+R2,color=colores[0],backgroundcolor=r"w"); alpha_LV1=popt[0];
popt=curve_fit(lambda vp,alpha:CV_porcigual2(vp,alpha,CV_TV1[-1]),pvp,CV_TV1)[0]; CV_TV1_pred=CV_porcigual2(pvp,*popt,CV_TV1[-1]); R2_CV_TV1=r2_score(CV_TV1,CV_TV1_pred);
ax.plot(pvp,CV_TV1,r"*",color=colores[1]); ax.plot(pvp,CV_TV1_pred,r"--",color=colores[1]); alpha=str(round(popt[0],4)); CV_max=str(round(CV_TV1[-1],4)); R2=str(round(R2_CV_TV1,4));
plt.text(0.002,85,r"$\bf{TV-1:}$$\:C_V=("+CV_max+r")\left[\dfrac{"+alpha+r"vp}{1+("+alpha+r"-1)vp}\right],\:R^2=$"+R2,color=colores[1],backgroundcolor=r"w"); alpha_TV1=popt[0];
popt=curve_fit(lambda vp,alpha:CV_porcigual2(vp,alpha,CV_PV2[-1]),pvp,CV_PV2)[0]; CV_PV2_pred=CV_porcigual2(pvp,*popt,CV_PV2[-1]); R2_CV_PV2=r2_score(CV_PV2,CV_PV2_pred);
ax.plot(pvp,CV_PV2,r"*",color=colores[2]); ax.plot(pvp,CV_PV2_pred,r"--",color=colores[2]); alpha=str(round(popt[0],4)); CV_max=str(round(CV_PV2[-1],4)); R2=str(round(R2_CV_PV2,4));
plt.text(0.002,75,r"$\bf{PV-1:}$$\:C_V=("+CV_max+r")\left[\dfrac{"+alpha+r"vp}{1+("+alpha+r"-1)vp}\right],\:R^2=$"+R2,color=colores[2],backgroundcolor=r"w"); alpha_PV2=popt[0];
popt=curve_fit(lambda vp,alpha:CV_porcigual2(vp,alpha,CV_FV1[-1]),pvp,CV_FV1)[0]; CV_FV1_pred=CV_porcigual2(pvp,*popt,CV_FV1[-1]); R2_CV_FV1=r2_score(CV_FV1,CV_FV1_pred);
ax.plot(pvp,CV_FV1,r"*",color=colores[3]); ax.plot(pvp,CV_FV1_pred,r"--",color=colores[3]); alpha=str(round(popt[0],4)); CV_max=str(round(CV_FV1[-1],4)); R2=str(round(R2_CV_FV1,4));
plt.text(0.002,65,r"$\bf{FV-1:}$$\:C_V=("+CV_max+r")\left[\dfrac{"+alpha+r"vp}{1+("+alpha+r"-1)vp}\right],\:R^2=$"+R2,color=colores[3],backgroundcolor=r"w"); alpha_FV1=popt[0];
ax.legend(loc=r"upper left"); plt.axis([-0.02,1.02,-1,110]); plt.savefig(r"CV_vp_inherente2.png");
######################################################################################################################## 
# Análisis de sensibilidad de f_ y FV con Ec. (8.11)
pvp=np.linspace(0,1,25); q_qmaxFvf_=np.zeros((len(pvp),1)); fig2,ax=plt.subplots(figsize=(8.5,7)); plt.title(r"Característica de flujo en instalación (Ec. (8.11) con $\alpha_V=50$)",fontweight=r"bold"); 
ax.set_ylabel(r"$\dot{q}/\dot{q}|_{vp=1}$"); ax.set_xlabel(r"$vp$"); plt.grid();
f_=[0.25,0.5,1]; FV=[2,5,10]; marca=[r"+",r"x",r"--"]; colores=[r"#1f77b4",r"#39a641",r"#d62b2c"];
for k in range(3):
    for j in range(3):
        for i in range(len(pvp)):
            q_qmaxFvf_[i]=q_qmax(50,FV[k],f_[j],pvp[i]);
        ax.plot(pvp,q_qmaxFvf_,marca[k],color=colores[j],label=r"$F_V=$"+str(FV[k])+r", $\overline{f}=$"+str(f_[j]));
plt.axis([0,1,0,1]); fig2.legend(loc=r"outside right");
fig2.subplots_adjust(top=0.88,bottom=0.11,left=0.09,right=0.785); plt.savefig(r"f_FV.png");
# Análisis de sensibilidad de f_ y FV con Ec. (8.12) 
pvp=np.linspace(0,1,25); q_qmaxFvf_=np.zeros((len(pvp),1)); fig3,ax=plt.subplots(figsize=(8.5,7)); plt.title(r"Característica de flujo en instalación (Ec. (8.12) con $\alpha_V=0.1$)",fontweight=r"bold"); 
ax.set_ylabel(r"$\dot{q}/\dot{q}|_{vp=1}$"); ax.set_xlabel(r"$vp$"); plt.grid();
f_=[0.25,0.5,1]; FV=[2,5,10]; marca=[r"+",r"x",r"--"]; colores=[r"#1f77b4",r"#39a641",r"#d62b2c"];
for k in range(3):
    for j in range(3):
        for i in range(len(pvp)):
            q_qmaxFvf_[i]=q_qmax2(0.1,FV[k],f_[j],pvp[i]);
        ax.plot(pvp,q_qmaxFvf_,marca[k],color=colores[j],label=r"$F_V=$"+str(FV[k])+r", $\overline{f}=$"+str(f_[j]));
plt.axis([0,1,0,1]); fig3.legend(loc=r"outside right");
fig3.subplots_adjust(top=0.88,bottom=0.11,left=0.09,right=0.785); plt.savefig(r"f_FV2.png");
########################################################################################################################
# Ajuste de característica de flujo en instalación de LV-1 y PV-2
# Datos con simulaciones del modelo propuesto para LV-1
pvp_LV1=np.array([0.142857,0.148148,0.110645]); 
q_LV1=np.array([0.454206909,0.693178549,0.486171237]); 
# Datos del resto de casos estacionarios, calculando q como (FT-1/17.8093-FIT-1/17.03518)/54.6
q_LV1otros=np.array([0.819784279,0.528931256,0.435958171,0.434002273,0.502833725,0.922429979,0.488324618,\
                     0.71719643,0.758162189,0.45957613,0.663933063,0.72141992,0.419616015,0.63690515,\
                     0.721233178,0.336474597,0.856665051,0.736172103,0.798745867,0.514582642,0.520876903,\
                     0.503631786,0.675365303,0.702638513,0.751261749,0.873687054,0.41193322,0.469917674,\
                     0.621814649,1.056627437,0.471651082,0.95987416,0.782691686]);
pvp_LV1otros=np.array([0.24026,0.134615,0.12,0.115942,0.152542,0.256667,0.155556,0.134444,0.136552,0.081356,\
                       0.116159,0.155172,0.0784,0.108046,0.13617,0.052041,0.1625,0.122444,0.133,0.095,\
                       0.077027,0.0825,0.12,0.13,0.14,0.164516,0.062909,0.083146,0.121429,0.200047,0.095094,\
                       0.15,0.155649]);
# Ajuste de LV-1
pvpt=np.concatenate((pvp_LV1,pvp_LV1otros)); qt=np.concatenate((q_LV1,q_LV1otros)); 
popt=curve_fit(lambda vp,q_max,F,f:q(vp,q_max,F,f,alpha_LV1),pvpt,qt,bounds=((max(qt),0,0),(np.inf,np.inf,1)))[0]; 
q_LV1_pred=q(pvpt,*popt,alpha_LV1); R2_q_LV1=r2_score(qt,q_LV1_pred); q_LV1_pred=q(pvp,*popt,alpha_LV1);
fig4,ax=plt.subplots(figsize=(7,7)); ax.plot(pvp_LV1,q_LV1,r"x",color=colores[2],label=r"Casos 1, 33 y 36"); 
ax.plot(pvp_LV1otros,q_LV1otros,r"+",color=colores[1],label=r"Otros casos"); ax.plot(pvp,q_LV1_pred,r"--",color=colores[0],label=r"Ec. (8.14)"); plt.grid();   
poptLV1=popt; ax.legend(loc=r"lower right"); ax.set_ylabel(r"$\dot{q}$ $[m^3/h]$"); ax.set_xlabel(r"$vp$"); 
plt.title(r"Característica de flujo en instalación de LV-1",fontweight=r"bold"); 
plt.text(0.70,0.28,r"$\dot{q}|_{vp=1}$ $[m^3/h]=$"+str(round(poptLV1[0],4)),color=colores[0],backgroundcolor=r"w"); 
plt.text(0.70,0.23,r"$F_V=$"+str(round(poptLV1[1],4)),color=colores[0],backgroundcolor=r"w"); 
plt.text(0.70,0.18,r"$\overline{f}=$"+str(round(poptLV1[2],4)),color=colores[0],backgroundcolor=r"w"); 
plt.text(0.70,0.13,r"$R^2=$"+str(round(R2_q_LV1,4)),color=colores[0],backgroundcolor=r"w"); plt.savefig(r"AjusteLV1.pdf");
# Datos con simulaciones del modelo propuesto para LV-1
pvp_PV2=np.array([0.196599,0.240774,0.308772]); 
q_PV2=np.array([94.70939925,116.2311143,116.7157664]);
# Ajuste de PV-2
popt=curve_fit(lambda vp,q_max,F,f:q(vp,q_max,F,f,alpha_PV2),pvp_PV2,q_PV2,bounds=((max(q_PV2),0,0),(np.inf,np.inf,1)))[0]; 
q_PV2_pred=q(pvp_PV2,*popt,alpha_PV2); R2_q_PV2=r2_score(q_PV2,q_PV2_pred); q_PV2_pred=q(pvp,*popt,alpha_PV2); 
fig5,ax=plt.subplots(figsize=(7,7)); ax.plot(pvp_PV2,q_PV2,r"x",color=colores[2],label=r"Casos 1, 33 y 36"); ax.plot(pvp,q_PV2_pred,r"--",color=colores[0],label=r"Ec. (8.14)"); plt.grid();
poptPV2=popt; ax.legend(loc=r"lower right"); ax.set_ylabel(r"$\dot{q}$ $[m^3/h]$"); ax.set_xlabel(r"$vp$"); 
plt.title(r"Característica de flujo en instalación de PV-2",fontweight=r"bold");  
plt.text(0.67,32,r"$\dot{q}|_{vp=1}$ $[m^3/h]=$"+str(round(poptPV2[0],4)),color=colores[0],backgroundcolor=r"w"); 
plt.text(0.67,25,r"$F_V=$"+str(round(poptPV2[1],4)),color=colores[0],backgroundcolor=r"w"); 
plt.text(0.67,18,r"$\overline{f}=$"+str(round(poptPV2[2],4)),color=colores[0],backgroundcolor=r"w"); 
plt.text(0.67,11,r"$R^2=$"+str(round(R2_q_PV2,4)),color=colores[0],backgroundcolor=r"w"); plt.savefig(r"AjustePV2.pdf");