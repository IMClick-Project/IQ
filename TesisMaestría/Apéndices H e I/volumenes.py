# Paqueterías y funciones
from math import pi, asin;
def longcarac_vol_tories(DI,DO):
    """Calcula las longitudes características [m] y volumen [m3] de una base torisférica con base a DI y DO [ambos m]: Fig. 2.6, Ecs. (2.1)-(2.6),(2.8)"""
    Rc=DO; rn=0.06*DO; c=DI/2-rn; th=(DO-DI)/2; 
    C=Rc-((Rc-rn)**2-c**2)**(1/2); rc=c*(1+(Rc/rn-1)**(-1)); B=C-(Rc-C)/(Rc-rn)*rn; b=(rn**2-(C-B)**2)**(1/2);
    V=pi*(Rc*B**2-C**3/3+C*(C**2-B**2)+(rn**2-C**2+rc**2-2*b*rc+b**2)*(C-B)-(rc-b)*((B-C)*b+rn**2*asin((B-C)/rn)));
    return Rc,rn,c,th,C,rc,B,b,V;
def z_LT1(pLT1):
    """z [m] en función de %LT-1: Ec. (2.12)"""
    return 0.2946+pLT1*(2.0796-0.2946);
def pLT1_z(z):
    """%LT-1 en función de z [m]: Despejar Ec. (2.12)"""
    return (z-0.2946)/(2.0796-0.2946);
def VS(pLT1):
    """Volumen líquido de sumidero en función de %LT-1: Ec. (2.13)"""
    if pLT1>=0 and pLT1<=pLT1_z(1.9246):
        return longcarac_vol_tories(0.75,0.79)[-1]+0.75**2*(z_LT1(pLT1)-0.1236)*pi/4;
    elif pLT1>=pLT1_z(1.9246) and pLT1<=1:
        return longcarac_vol_tories(0.75,0.79)[-1]+0.75**2*(1.9246-0.1236)*pi/4+ \
               pi*((z_LT1(pLT1)-1.9246)**3/12-3*(z_LT1(pLT1)-1.9246)**2/16+(z_LT1(pLT1)-1.9246)*0.75**2/4);
def VR(pLT1):
    """Volumen líquidp en reboiler E-2 en función de %LT-1: Ec. (2.17)"""
    if pLT1>=0 and pLT1<=pLT1_z(1.4226):
        return longcarac_vol_tories(0.438,0.45705)[-1]+191*0.01483**2*(z_LT1(pLT1)+0.4062)*pi/4;
    elif pLT1>=pLT1_z(1.4226) and pLT1<=pLT1_z(1.4816):
        return longcarac_vol_tories(0.438,0.45705)[-1]+191*0.01483**2*(1.4226+0.4062)*pi/4+ \
               0.438**2*(z_LT1(pLT1)-1.4226)*pi/4;
    elif pLT1>=pLT1_z(1.4816) and pLT1<=pLT1_z(1.8816):
        return longcarac_vol_tories(0.438,0.45705)[-1]+191*0.01483**2*(1.4226+0.4062)*pi/4+ \
               0.438**2*(1.4816-1.4226)*pi/4+ \
               pi*((z_LT1(pLT1)-1.4816)**3*0.087025/3-0.12921*(z_LT1(pLT1)-1.4816)**2/2+0.047961*(z_LT1(pLT1)-1.4816));
    elif pLT1>=pLT1_z(1.8816) and pLT1<=1:
        return longcarac_vol_tories(0.438,0.45705)[-1]+191*0.01483**2*(1.4226+0.4062)*pi/4+ \
               0.438**2*(1.4816-1.4226)*pi/4+ \
               pi*((1.8816-1.4816)**3*0.087025/3-0.12921*(1.8816-1.4816)**2/2+0.047961*(1.8816-1.4816))+ \
               0.202**2*(z_LT1(pLT1)-1.8816)*pi/4;
# #######################################################################################################################
# # Longitudes características [m] y volúmenes [m3] en E-1
# res=longcarac_vol_tories(0.3048,0.31115);
# print("Longitudes características [m] y volumen [m3] de base toriesférica en E-1:\nRc="+str(res[0])+"\nrn=" \
#       +str(res[1])+"\nc="+str(res[2])+"\nth="+str(res[3])+"\nC="+str(res[4])+"\nrc="+str(res[5])+"\nB="+str(res[6]) \
#       +"\nb="+str(res[7])+"\nV="+str(res[8]));
# res1=2.972*pi*0.3048**2/4;
# res2=pi*0.01905**2/4*5.954*26;
# print("Volumen de cilindro de la coraza [m3]="+str(res1));
# print("Volumen de tubos al exterior [m3]="+str(res2));
# print("Volumen de lado de coraza en E-1 [m3]="+str(res1-res2+res[8]));
# res1=0.349*pi*0.3048**2/4;
# res2=pi*(0.01905-0.00211*2)**2/4*5.954*26;
# print("Volumen de cilindro de los tubos [m3]="+str(res1));
# print("Volumen de tubos al interior [m3]="+str(res2));
# print("Volumen de lado de tubos en E-1 [m3]="+str(res1+res2+res[8]));
# #######################################################################################################################
# # Longitudes características [m] y volumen [m3] de base toriesférica de sumidero
# res=longcarac_vol_tories(0.75,0.79);
# print("Longitudes características [m] y volumen [m3] de base toriesférica de sumidero:\nRc="+str(res[0])+"\nrn=" \
#       +str(res[1])+"\nc="+str(res[2])+"\nth="+str(res[3])+"\nC="+str(res[4])+"\nrc="+str(res[5])+"\nB="+str(res[6]) \
#       +"\nb="+str(res[7])+"\nV="+str(res[8]));    
# #######################################################################################################################
# # Volumen total del sumidero [m3]: Suma de los 5 Segmentos (Ecs. (2.8)-(2.11))
# res=longcarac_vol_tories(0.75,0.79)[-1]+\
#     0.75**2*1.801*pi/4+\
#     pi*(0.3**3/12-3*0.3**2/16+0.3*0.75**2/4)+\
#     0.45**2*0.511*pi/4;
# print("Volumen total del sumidero [m3]="+str(res));
# #######################################################################################################################
# # Longitudes características [m] de la base toriesférica y volumen total del R,CF [m3]: Ec. (2.17) más lo faltante del cilindro de menor diámetro
# res=longcarac_vol_tories(0.438,0.45705);
# print("Longitudes características [m] de base toriesférica en E-2:\nRc="+str(res[0])+"\nrn=" \
#       +str(res[1])+"\nc="+str(res[2])+"\nth="+str(res[3])+"\nC="+str(res[4])+"\nrc="+str(res[5])+"\nB="+str(res[6]) \
#       +"\nb="+str(res[7]));
# res=res[-1]+191*0.01483**2*1.8288*pi/4+ \
#     0.438**2*0.059*pi/4+ \
#     pi*(0.4**3*0.087025/3-0.12921*0.4**2/2+0.047961*0.4)+ \
#     0.202**2*0.375*pi/4;
# print("Volumen total del R,CF [m3]="+str(res));
# #######################################################################################################################
# # Volumen del R,HF [m3]
# res1=0.438**2*1.8288*pi/4;
# res2=191*0.01905**2*1.8288*pi/4;
# print("Volumen de cilindro [m3]="+str(res1));
# print("Volumen de tubos al exterior [m3]="+str(res2));
# print("Volumen de lado de coraza en E-2 [m3]="+str(res1-res2));
# #######################################################################################################################
# # Longitudes características [m] y volúmenes [m3] en E-3
# res=longcarac_vol_tories(0.489,0.50805);
# print("Longitudes características [m] y volumen [m3] de base toriesférica de E-3:\nRc="+str(res[0])+"\nrn=" \
#       +str(res[1])+"\nc="+str(res[2])+"\nth="+str(res[3])+"\nC="+str(res[4])+"\nrc="+str(res[5])+"\nB="+str(res[6]) \
#       +"\nb="+str(res[7])+"\nV="+str(res[8]));  
# res1=0.489**2*(3.736-res[3]-res[4])*pi/4;
# res2=pi*0.01905**2/4*7.0285*104;
# print("Volumen de cilindro de la coraza [m3]="+str(res1));
# print("Volumen de tubos al exterior [m3]="+str(res2));
# print("Volumen de lado de coraza en E-3 [m3]="+str(res1-res2+res[8]));
# res1=0.489**2*(0.613-res[3]-res[4])*pi/4;
# res2=pi*(0.01905-0.00211*2)**2/4*7.0285*104;
# print("Volumen de cilindro de los tubos [m3]="+str(res1));
# print("Volumen de tubos al interior [m3]="+str(res2));
# print("Volumen de lado de tubos en E-3 [m3]="+str(res1+res2+res[8]));