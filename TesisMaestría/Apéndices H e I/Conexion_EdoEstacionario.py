# Paqueterí­as y funciones
import os; import win32com.client as win32; import xlwings as xw; from pathlib import Path; # Para conectar aplicaciones 
import pandas as pd; import numpy as np; # Para trabajar tablas y arreglos
import matplotlib.pyplot as plt; # Para graficar
from volumenes import z_LT1; # Calcular z respecto a % LT-1
from math import sqrt,log; # Funciones matemáticas
from scipy.optimize import fsolve; # Para resolver ecuaciones no lineales
import warnings; # Evitar avisos de advertencias DeprecationWarning
from sys import exit; # Para usar exit();
warnings.filterwarnings(r"ignore",category=DeprecationWarning);
plt.close(r"all"); # Cerrar todas las figuras anteriores
def fFToutCF(ToutCF,TinHF,ToutHF,TinCF,npHF,F): # Calcular ToutCF dada una F
    R=(TinHF-ToutHF)/(ToutCF-TinCF);
    P=(ToutCF-TinCF)/(TinHF-TinCF);
    if R!=1:
        alpha=((1-R*P)/(1-P))**(1/npHF);
        S=(alpha-1)/(alpha-R);
        return F-sqrt(R**2+1)*log((1-S)/(1-R*S))/(R-1)/log((2-S*(R+1-sqrt(R**2+1)))/(2-S*(R+1+sqrt(R**2+1))));
    else:
        S=P/(npHF-(npHF-1)*P);
        return F-S*sqrt(2)/(1-S)/log((2-S*(2-sqrt(2)))/(2-S*(2+sqrt(2)))); 
def F(P,R,npHF): # Calcular F, apéndice F
    if R!=1:
        alpha=((1-R*P)/(1-P))**(1/npHF); 
        S=(alpha-1)/(alpha-R); 
        return sqrt(R**2+1)*log((1-S)/(1-R*S))/(R-1)/log((2-S*(R+1-sqrt(R**2+1)))/(2-S*(R+1+sqrt(R**2+1)))); 
    else:
        S=P/(npHF-(npHF-1)*P); 
        return S*sqrt(2)/(1-S)/log((2-S*(2-sqrt(2)))/(2-S*(2+sqrt(2))));  
######################################################################################################################## 
# Primera parte de Aspen Plus
# Simulación en estado estacionario y patrón de flujo MIXED, LPLUG y VPLUG en Aspen Plus con cada sección empacada dividida en: 
# simtype=0 para partes iguales y simtype=1 para mayores divisiones en parte superior e inferior de zona de rectificación y agotamiento
flowmode1=r"VPLUG"; flowmode2=r"VPLUG"; caso=36; ps1=17; ps2=17; simtype=0; pborde1=0.1; nborde1=6; pborde2=0.1; nborde2=6; 
nombre_hoja_cal=r"Caso"+str(caso)+r"-"+flowmode1+r"-"+str(simtype)+r"-"+str(ps1); # Mismo patrón de flujo y discretización en ambas zonas empacadas
# Validar caso propuesto si simtype=1
if simtype==1 and (pborde1>0.5 or pborde2>0.5 or 2*nborde1>ps1-3 or 2*nborde2>ps2-3):
    print("Caso symtype=1 no válido, checa el porcentaje o cantidad de etapas de los bordes"); exit();
# Iniciar Aspen Plus
EdoEstacionario=win32.Dispatch(r"Apwn.Document"); 
if simtype==0:
    EdoEstacionario.InitFromArchive2(os.path.abspath(r"EdoEstacionario.bkp"));
else:
    EdoEstacionario.InitFromArchive2(os.path.abspath(r"EdoEstacionario2.bkp"));
# Extraer datos especí­ficos por caso y opciones de simulación
datos=pd.read_excel(r"Casos_Estacionarios.xlsx",sheet_name=r"Datos_promedios"); 
# Configurar variables especí­ficas por caso
ind=caso-1; rutacin=r"\Data\Streams\CIN\Input"; rutab=r"\Data\Blocks\C-1\Input"; rutas=r"\Data\Blocks\C-1\Subobjects\Column Internals\INT-1";
EdoEstacionario.Tree.FindNode(rutacin+r"\TEMP\MIXED").Value=datos[r"TE,CF,in"][ind]; # Temperatura de entrada a la columna [°C]
EdoEstacionario.Tree.FindNode(rutacin+r"\TOTFLOW\MIXED").Value=datos[r"FT-1"][ind]; # Entrada a la columna [kh/h]
EdoEstacionario.Tree.FindNode(rutab+r"\BASIS_D").Value=datos[r"FIT-1"][ind]; # Destilado [kg/h]
EdoEstacionario.Tree.FindNode(rutab+r"\BASIS_L1").Value=datos[r"FT-2"][ind]*0.585022; # Reflujo [kg/h]
EdoEstacionario.Tree.FindNode(rutab+r"\PRES1").Value=datos[r"PT-2"][ind]/1.01972; # Presión en el condensador [bar]
EdoEstacionario.Tree.FindNode(rutas+r"\Input\CA_LIQ_LEVEL\INT-1").Value=z_LT1(datos[r"LT-1"][ind]/100); # Altura en el sumidero [m]
# Configurar modo de simulación
EdoEstacionario.Tree.FindNode(rutab+r"\NSTAGE").Value=ps1+ps2-2; # Total de etapas
EdoEstacionario.Tree.FindNode(rutab+r"\FEED_STAGE\COUT").Value=ps1; # Etapa de alimentación
if simtype==0:
    # Variar datos de rango de etapas
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO\Input\CA_STAGE2\INT-1\AGO").Value=""; EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO\Input\CA_STAGE1\INT-1\AGO").Value="";
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT\Input\CA_STAGE2\INT-1\RECT").Value=""; EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT\Input\CA_STAGE1\INT-1\RECT").Value=""; 
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO\Input\CA_STAGE2\INT-1\AGO").Value=ps1+ps2-3; # Última etapa de agotamiento
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO\Input\CA_STAGE1\INT-1\AGO").Value=ps1; # Primera etapa de agotamiento
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT\Input\CA_STAGE2\INT-1\RECT").Value=ps1-1; # Última etapa de rectificación
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT\Input\CA_STAGE1\INT-1\RECT").Value=2; # Primera etapa de rectificación   
    EdoEstacionario.Tree.FindNode(rutab+r"\CA_FLOW_MDL\INT-1\RECT").Value=flowmode1; # Propiedades de bulk en rectificación
    EdoEstacionario.Tree.FindNode(rutab+r"\CA_FLOW_MDL\INT-1\AGO").Value=flowmode2; # Propiedades de bulk en agotamiento
else:
    # Variar datos de rango de etapas
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO3\Input\CA_STAGE2\INT-1\AGO3").Value=""; EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO3\Input\CA_STAGE1\INT-1\AGO3").Value="";
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO2\Input\CA_STAGE2\INT-1\AGO2").Value=""; EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO3\Input\CA_STAGE1\INT-1\AGO2").Value=""; 
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO1\Input\CA_STAGE2\INT-1\AGO1").Value=""; EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO3\Input\CA_STAGE1\INT-1\AGO1").Value=""; 
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT3\Input\CA_STAGE2\INT-1\RECT3").Value=""; EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO3\Input\CA_STAGE1\INT-1\RECT3").Value="";
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT2\Input\CA_STAGE2\INT-1\RECT2").Value=""; EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO3\Input\CA_STAGE1\INT-1\RECT2").Value=""; 
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT1\Input\CA_STAGE2\INT-1\RECT1").Value=""; EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO3\Input\CA_STAGE1\INT-1\RECT1").Value="";
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO3\Input\CA_STAGE2\INT-1\AGO3").Value=ps1+ps2-3; # Última etapa de agotamiento inferior
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO3\Input\CA_STAGE1\INT-1\AGO3").Value=ps1+ps2-nborde2-2; # Primera etapa de agotamiento inferior
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO2\Input\CA_STAGE2\INT-1\AGO2").Value=ps1+ps2-nborde2-3; # Última etapa de agotamiento central
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO2\Input\CA_STAGE1\INT-1\AGO2").Value=ps1+nborde2; # Primera etapa de agotamiento central
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO1\Input\CA_STAGE2\INT-1\AGO1").Value=ps1+nborde2-1; # Última etapa de agotamiento superior
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO1\Input\CA_STAGE1\INT-1\AGO1").Value=ps1; # Primera etapa de agotamiento superior
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT3\Input\CA_STAGE2\INT-1\RECT3").Value=ps1-1; # Última etapa de rectificación inferior
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT3\Input\CA_STAGE1\INT-1\RECT3").Value=ps1-nborde1; # Primera etapa de rectificación inferior
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT2\Input\CA_STAGE2\INT-1\RECT2").Value=ps1-nborde1-1; # Última etapa de rectificación central
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT2\Input\CA_STAGE1\INT-1\RECT2").Value=nborde1+2; # Primera etapa de rectificación central
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT1\Input\CA_STAGE2\INT-1\RECT1").Value=nborde1+1; # Última etapa de rectificación superior
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT1\Input\CA_STAGE1\INT-1\RECT1").Value=2; # Primera etapa de rectificación superior
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT1\Input\CA_PACK_HT\INT-1\RECT1").Value=1.89*pborde1; # Altura de rectificación superior
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT2\Input\CA_PACK_HT\INT-1\RECT2").Value=1.89*(1-2*pborde1); # Altura de rectificación central
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\RECT3\Input\CA_PACK_HT\INT-1\RECT3").Value=1.89*pborde1; # Altura de rectificación inferior
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO1\Input\CA_PACK_HT\INT-1\AGO1").Value=3.99*pborde2; # Altura de agotamiento superior
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO2\Input\CA_PACK_HT\INT-1\AGO2").Value=3.99*(1-2*pborde2); # Altura de agotamiento central
    EdoEstacionario.Tree.FindNode(rutas+r"\Subobjects\Sections\AGO3\Input\CA_PACK_HT\INT-1\AGO3").Value=3.99*pborde2; # Altura de agotamiento inferior
    EdoEstacionario.Tree.FindNode(rutab+r"\CA_FLOW_MDL\INT-1\RECT1").Value=flowmode1; EdoEstacionario.Tree.FindNode(rutab+r"\CA_FLOW_MDL\INT-1\RECT2").Value=flowmode1; 
    EdoEstacionario.Tree.FindNode(rutab+r"\CA_FLOW_MDL\INT-1\RECT3").Value=flowmode1; # Propiedades de bulk en rectificación
    EdoEstacionario.Tree.FindNode(rutab+r"\CA_FLOW_MDL\INT-1\AGO1").Value=flowmode2; EdoEstacionario.Tree.FindNode(rutab+r"\CA_FLOW_MDL\INT-1\AGO2").Value=flowmode2; 
    EdoEstacionario.Tree.FindNode(rutab+r"\CA_FLOW_MDL\INT-1\AGO3").Value=flowmode2; # Propiedades de bulk en agotamiento
# Reiniciar valores y ejecutar
EdoEstacionario.Reinit; EdoEstacionario.SuppressDialogs=1; EdoEstacionario.Engine.Run2();
# Verificar un caso si corre correctamente para continuar
try:
    estado=EdoEstacionario.Tree.FindNode(r"\Data\Results Summary\Run-Status\Output\UOSSTAT2").Value;
    if estado==8: # 8 = corrió correctamente
        print(r"Aspen Plus generó resultados exitosamente"); EdoEstacionario.SaveAs(nombre_hoja_cal+r".bkp",True);
    else: # 9 = error, 10 = warning
        print(r"Aspen Plus no generó resultados exitosamente"); exit();
except: # Cuando no genera resultados
    print(r"No genera resultados Aspen Plus"); exit();
if flowmode1==r"LPLUG" or flowmode2==r"LPLUG":
    exit();  
# Segunda para de Aspen Plus
# También exporta los resultados a un Excel de MIXED y VPLUG, genera gráficas correspondientes, corrobora aproximaciones,  
# y guarda valores iniciales para futuras simulaciones en Aspen Custom Modeler      
# Pasar plantilla de resultados
wb=xw.Book(r"Casos_Estacionarios.xlsx"); sheet=wb.sheets[r"Exportar_resultados_AP",r"Exportar_resultados_ACM"]; sheet.api.Copy(); xw.books.active.save(str(Path.cwd())+"\\"+nombre_hoja_cal+r".xlsx"); wb.save(); wb.close();
# Exportar resultados de Aspen Plus a Excel
wb=xw.Book(nombre_hoja_cal+r".xlsx"); sheet=wb.sheets[r"Exportar_resultados_AP"]; 
rutab=r"\Data\Blocks\C-1\Output"; rutae1=r"\Data\Blocks\E-1\Output"; rutas=r"\Data\Streams"; strs=str(ps1+ps2-2);
# Datos principales
sheet[r"B1"].value=caso; sheet[r"B2"].value=ps1; sheet[r"B3"].value=ps2; sheet[r"B4"].value=flowmode1; sheet[r"B5"].value=flowmode2; sheet[r"B6"].value=simtype;
if simtype==0:
    sheet[r"B7"].value=r"'-"; sheet[r"B8"].value=r"'-"; sheet[r"B9"].value=r"'-"; sheet[r"B10"].value=r"'-"; 
else:
    sheet[r"B7"].value=pborde1; sheet[r"B8"].value=nborde1; sheet[r"B9"].value=pborde2; sheet[r"B10"].value=nborde2;
sheet[r"B11"].value=EdoEstacionario.Tree.FindNode(rutab+r"\MOLE_RR").Value; sheet[r"B12"].value=EdoEstacionario.Tree.FindNode(rutab+r"\MOLE_BR").Value; 
sheet[r"B13"].value=EdoEstacionario.Tree.FindNode(rutab+r"\TH_VFRAC_OUT").Value; sheet[r"B14"].value=EdoEstacionario.Tree.FindNode(rutas+r"\D\Output\MASSFRAC\MIXED\AMMONIA").Value; sheet[r"B15"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HIN\Output\MASSFRAC\MIXED\AMMONIA").Value;
# Economizador
sheet[r"B31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\CIN\Output\MOLEFLMX\MIXED").Value; sheet[r"C31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\COUT\Output\MOLEFLMX\MIXED").Value;
sheet[r"D31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HIN\Output\MOLEFLMX\MIXED").Value; sheet[r"E31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HOUT\Output\MOLEFLMX\MIXED").Value;
sheet[r"F31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\CIN\Output\MOLEFRAC\MIXED\AMMONIA").Value; sheet[r"G31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\COUT\Output\MOLEFRAC\MIXED\AMMONIA").Value;
sheet[r"H31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HIN\Output\MOLEFRAC\MIXED\AMMONIA").Value; sheet[r"I31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HOUT\Output\MOLEFRAC\MIXED\AMMONIA").Value;
sheet[r"J31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\CIN\Output\TEMP_OUT\MIXED").Value; sheet[r"K31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\COUT\Output\TEMP_OUT\MIXED").Value;
sheet[r"L31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HIN\Output\TEMP_OUT\MIXED").Value; sheet[r"M31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HOUT\Output\TEMP_OUT\MIXED").Value;
sheet[r"N31"].value=EdoEstacionario.Tree.FindNode(rutae1+r"\HX_DUTY").Value; sheet[r"O31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\CIN\Output\HMX\MIXED").Value;
sheet[r"P31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\COUT\Output\HMX\MIXED").Value; sheet[r"Q31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HIN\Output\HMX\MIXED").Value;
sheet[r"R31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HOUT\Output\HMX\MIXED").Value; sheet[r"S31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\CIN\Output\PRES_OUT\MIXED").Value;
sheet[r"T31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\COUT\Output\PRES_OUT\MIXED").Value; sheet[r"U31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HIN\Output\PRES_OUT\MIXED").Value;
sheet[r"V31"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HOUT\Output\PRES_OUT\MIXED").Value;
# Condensador
sheet[r"B36"].value=1; sheet[r"C36"].value=10.2497; 
sheet[r"D36"].value=r"'-"; sheet[r"E36"].value=EdoEstacionario.Tree.FindNode(rutab+r"\LIQ_FLOW_FRM\1").Value;
sheet[r"F36"].value=r"'-"; sheet[r"G36"].value=EdoEstacionario.Tree.FindNode(rutas+r"\D\Output\MOLEFLMX\MIXED").Value;
sheet[r"H36"].value=r"'-"; sheet[r"I36"].value=EdoEstacionario.Tree.FindNode(rutab+r"\X\1\AMMONIA").Value;
sheet[r"J36"].value=r"'-"; sheet[r"K36"].value=EdoEstacionario.Tree.FindNode(rutas+r"\D\Output\MOLEFRAC\MIXED\AMMONIA").Value;
sheet[r"L36"].value=r"'-"; sheet[r"M36"].value=EdoEstacionario.Tree.FindNode(rutab+r"\TLIQ\1").Value;
sheet[r"N36"].value=r"'-"; sheet[r"O36"].value=EdoEstacionario.Tree.FindNode(rutas+r"\D\Output\TEMP_OUT\MIXED").Value;
sheet[r"P36"].value=EdoEstacionario.Tree.FindNode(rutab+r"\COND_DUTY").Value; sheet[r"Q36"].value=r"'-"; 
sheet[r"R36"].value=EdoEstacionario.Tree.FindNode(rutab+r"\LIQ_ENTH\1").Value; sheet[r"S36"].value=r"'-"; 
sheet[r"T36"].value=EdoEstacionario.Tree.FindNode(rutas+r"\D\Output\HMX\MIXED").Value; sheet[r"U36"].value=r"'-";
sheet[r"V36"].value=EdoEstacionario.Tree.FindNode(rutab+r"\B_PRES\1").Value; sheet[r"W36"].value=r"'-";
sheet[r"X36"].value=EdoEstacionario.Tree.FindNode(rutas+r"\D\Output\PRES_OUT\MIXED").Value;
# Rehervidor   
sheet[r"B37"].value=ps1+ps2-2; sheet[r"C37"].value=0; 
sheet[r"D37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_FLOW_FRM"+"\\"+strs).Value; sheet[r"E37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\LIQ_FLOW_FRM"+"\\"+strs).Value;
sheet[r"F37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\PROD_VFLOW"+"\\"+strs).Value; sheet[r"G37"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HIN\Output\MOLEFLMX\MIXED").Value;
sheet[r"H37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\Y"+"\\"+strs+r"\AMMONIA").Value; sheet[r"I37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\X"+"\\"+strs+r"\AMMONIA").Value; 
sheet[r"J37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\TH_Y\AMMONIA").Value; sheet[r"K37"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HIN\Output\MOLEFRAC\MIXED\AMMONIA").Value;
sheet[r"L37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\TVAP"+"\\"+strs).Value; sheet[r"M37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\TLIQ"+"\\"+strs).Value;
sheet[r"N37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\TH_TEMP_OUT").Value; sheet[r"O37"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HIN\Output\TEMP_OUT\MIXED").Value;
sheet[r"P37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\TH_DUTY").Value; sheet[r"Q37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_ENTH"+"\\"+strs).Value; 
sheet[r"T37"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HIN\Output\HMX\MIXED").Value; sheet[r"U37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\B_PRES"+"\\"+strs).Value; 
sheet[r"V37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\B_PRES"+"\\"+strs).Value; sheet[r"W37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\TH_PRES_OUT").Value; 
sheet[r"X37"].value=EdoEstacionario.Tree.FindNode(rutas+r"\HIN\Output\PRES_OUT\MIXED").Value; 
sheet[r"Z36"].value=sheet[r"E37"].value-sheet[r"F37"].value-sheet[r"G37"].value; sheet[r"AA36"].value=EdoEstacionario.Tree.FindNode(rutab+r"\TH_X\AMMONIA").Value;
sheet[r"AB36"].value=EdoEstacionario.Tree.FindNode(rutab+r"\TH_TEMP_OUT").Value; sheet[r"AD36"].value=sheet[r"W37"].value=EdoEstacionario.Tree.FindNode(rutab+r"\TH_PRES_OUT").Value; 
sheet[r"AF36"].value=z_LT1(datos[r"LT-1"][ind]/100);
# Columna: Rectificación y Agotamiento
if simtype==0:
    h=np.concatenate((np.linspace(9.6416,7.7516,ps1-1),np.linspace(6.8706,2.8806,ps2-1)));
else:
    h=np.concatenate((np.linspace(9.6416,9.6416-pborde1*1.89,nborde1+1),np.linspace(9.6416-pborde1*1.89,9.6416-(1-pborde1)*1.89,ps1-2*nborde1-1)[1:],np.linspace(9.6416-(1-pborde1)*1.89,7.7516,nborde1+1)[1:], \
                      np.linspace(6.8706,6.8706-pborde2*3.99,nborde2+1),np.linspace(6.8706-pborde2*3.99,6.8706-(1-pborde2)*3.99,ps2-2*nborde2-1)[1:],np.linspace(6.8706-(1-pborde2)*3.99,2.8806,nborde2+1)[1:]));
for s in range(2,ps1+ps2-2):
    fila=str(40+s); strs=str(s); sheet[r"B"+fila].value=str(s);
    if s<=ps1-1:
        sheet[r"A"+fila].value=r"Rectificación"; sheet[r"C"+fila].value=str(h[s-2]); sheet[r"D"+fila].value=str(h[s-1]); sheet[r"E"+fila].value=r"'-"; sheet[r"F"+fila].value=r"'-"; 
        sheet[r"L"+fila].value=r"'-"; sheet[r"M"+fila].value=r"'-"; sheet[r"AE"+fila].value=r"'-"; sheet[r"AF"+fila].value=r"'-"; sheet[r"AS"+fila].value=r"'-"; sheet[r"AT"+fila].value=r"'-";
        sheet[r"AW"+fila].value=r"'-"; sheet[r"AX"+fila].value=r"'-";
        if flowmode1!=r"VPLUG":
            sheet[r"I"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_FLOW_FRM"+"\\"+strs).Value; sheet[r"O"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\Y"+"\\"+strs+r"\AMMONIA").Value;
            sheet[r"AH"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\TVAP"+"\\"+strs).Value; sheet[r"AU"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_ENTH"+"\\"+strs).Value;
        if flowmode1!=r"LPLUG":
            sheet[r"J"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\LIQ_FLOW_FRM"+"\\"+strs).Value; sheet[r"R"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\X"+"\\"+strs+r"\AMMONIA").Value;
            sheet[r"AJ"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\TLIQ"+"\\"+strs).Value; sheet[r"AV"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\LIQ_ENTH"+"\\"+strs).Value;
    else:
        sheet[r"A"+fila].value=r"Agotamiento"; sheet[r"C"+fila].value=str(h[s-1]); sheet[r"D"+fila].value=str(h[s]);
        if s!=ps1 and s!=ps1+ps2-3:
            sheet[r"E"+fila].value=r"'-"; sheet[r"F"+fila].value=r"'-"; sheet[r"L"+fila].value=r"'-"; sheet[r"M"+fila].value=r"'-"; sheet[r"AE"+fila].value=r"'-"; sheet[r"AF"+fila].value=r"'-"; 
            sheet[r"AS"+fila].value=r"'-"; sheet[r"AT"+fila].value=r"'-"; sheet[r"AW"+fila].value=r"'-"; sheet[r"AX"+fila].value=r"'-";
        elif s==ps1: # Alimentación a C-1
            sheet[r"E"+fila].value=r"'-"; sheet[r"F"+fila].value=EdoEstacionario.Tree.FindNode(rutas+r"\COUT\Output\MOLEFLMX\MIXED").Value;
            sheet[r"L"+fila].value=r"'-"; sheet[r"M"+fila].value=EdoEstacionario.Tree.FindNode(rutas+r"\COUT\Output\MOLEFRAC\MIXED\AMMONIA").Value;
            sheet[r"AE"+fila].value=r"'-"; sheet[r"AF"+fila].value=EdoEstacionario.Tree.FindNode(rutas+r"\COUT\Output\TEMP_OUT\MIXED").Value;
            sheet[r"AS"+fila].value=r"'-"; sheet[r"AT"+fila].value=EdoEstacionario.Tree.FindNode(rutas+r"\COUT\Output\HMX\MIXED").Value; 
            sheet[r"AW"+fila].value=r"'-"; sheet[r"AX"+fila].value=EdoEstacionario.Tree.FindNode(rutas+r"\COUT\Output\PRES_OUT\MIXED").Value;
        else: # Producto vapor del Rehervidor que alimenta la etapa
            sheet[r"E"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\PROD_VFLOW"+"\\"+str(ps1+ps2-2)).Value; sheet[r"F"+fila].value=r"'-";
            sheet[r"L"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\TH_Y\AMMONIA").Value; sheet[r"M"+fila].value=r"'-";
            sheet[r"AE"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\TH_TEMP_OUT").Value; sheet[r"AF"+fila].value=r"'-"; 
            sheet[r"AT"+fila].value=r"'-"; sheet[r"AW"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\TH_PRES_OUT").Value; sheet[r"AX"+fila].value=r"'-";
        if flowmode2!=r"VPLUG":
            sheet[r"I"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_FLOW_FRM"+"\\"+strs).Value; sheet[r"O"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\Y"+"\\"+strs+r"\AMMONIA").Value;
            sheet[r"AH"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\TVAP"+"\\"+strs).Value; sheet[r"AU"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_ENTH"+"\\"+strs).Value; 
        if flowmode2!=r"LPLUG":  
            sheet[r"J"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\LIQ_FLOW_FRM"+"\\"+strs).Value; sheet[r"R"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\X"+"\\"+strs+r"\AMMONIA").Value;
            sheet[r"AJ"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\TLIQ"+"\\"+strs).Value; sheet[r"AV"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\LIQ_ENTH"+"\\"+strs).Value;
    sheet[r"G"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_FLOW_FRM"+"\\"+strs).Value; sheet[r"H"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\LIQ_FLOW_FRM"+"\\"+strs).Value;
    sheet[r"K"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\I_AREA"+"\\"+strs).Value; sheet[r"CO"+fila].value=sheet[r"K"+fila].value/(sheet[r"C"+fila].value-sheet[r"D"+fila].value)/sheet[r"BI38"].value;
    sheet[r"N"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\Y"+"\\"+strs+r"\AMMONIA").Value; sheet[r"P"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\YINTF"+"\\"+strs+r"\AMMONIA").Value; 
    sheet[r"Q"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\XINTF"+"\\"+strs+r"\AMMONIA").Value; sheet[r"S"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\X"+"\\"+strs+r"\AMMONIA").Value; 
    sheet[r"BH"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\V_DENSITY"+"\\"+strs).Value; sheet[r"BI"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\L_DENSITY"+"\\"+strs).Value;
    sheet[r"BL"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\DIFF_COEFF\Vapor"+"\\"+strs+r"\AMMONIA\WATER").Value*3600; sheet[r"BM"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\DIFF_COEFF\Liquid"+"\\"+strs+r"\AMMONIA\WATER").Value*3600; 
    sheet[r"BY"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\SCHMIDT\Vapor"+"\\"+strs+r"\AMMONIA\WATER").Value; sheet[r"BZ"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\SCHMIDT\Liquid"+"\\"+strs+r"\AMMONIA\WATER").Value;
    sheet[r"CC"+fila].value=4*sheet[r"BK38"].value*EdoEstacionario.Tree.FindNode(rutab+r"\V_REYNOLDS"+"\\"+strs).Value; sheet[r"CD"+fila].value=4*sheet[r"BK38"].value*EdoEstacionario.Tree.FindNode(rutab+r"\L_REYNOLDS"+"\\"+strs).Value;
    sheet[r"CG"+fila].value=4*sheet[r"BK38"].value*EdoEstacionario.Tree.FindNode(rutab+r"\L_WEBBER"+"\\"+strs).Value; sheet[r"CI"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\L_FROUDE"+"\\"+strs).Value/4/sheet[r"BK38"].value;
    sheet[r"T"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\MASS_LCOEF\Vapor"+"\\"+strs+r"\AMMONIA\WATER").Value/sheet[r"BH"+fila].value/sheet[r"K"+fila].value;
    sheet[r"U"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\MASS_LCOEF\Liquid"+"\\"+strs+r"\AMMONIA\WATER").Value/sheet[r"BI"+fila].value/sheet[r"K"+fila].value;
    sheet[r"V"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\MASS_RATE\Vapor"+"\\"+strs+r"\AMMONIA").Value; sheet[r"W"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\MASS_RATE\Vapor"+"\\"+strs+r"\WATER").Value
    sheet[r"X"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\MASS_RATE\Vapor"+"\\"+strs+r"\AMMONIA").Value+EdoEstacionario.Tree.FindNode(rutab+r"\MASS_RATE\Vapor"+"\\"+strs+r"\WATER").Value;
    sheet[r"AG"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\TVAP"+"\\"+strs).Value; sheet[r"AI"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\TINTF"+"\\"+strs).Value;
    sheet[r"AK"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\TLIQ"+"\\"+strs).Value; sheet[r"AL"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\VHT_COEF"+"\\"+strs).Value*3600;
    sheet[r"AM"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\LHT_COEF"+"\\"+strs).Value*3600; sheet[r"AN"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\HEAT_RATE"+"\\"+strs).Value;
    sheet[r"AO"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_COND"+"\\"+strs).Value; sheet[r"AP"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_CONV"+"\\"+strs).Value;
    sheet[r"AQ"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\LIQ_COND"+"\\"+strs).Value; sheet[r"AR"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\LIQ_CONV"+"\\"+strs).Value;
    sheet[r"AY"+fila].value=EdoEstacionario.Tree.FindNode(rutab+r"\B_PRES"+"\\"+strs).Value; 
sheet[r"AG36"].value=EdoEstacionario.Tree.FindNode(rutab+r"\HYD_RHOL"+"\\"+str(ps1+ps2-2)).Value;
sheet[r"AH36"].value=sheet[r"V37"].value-sheet[r"AY"+str(40+ps1+ps2-3)].value; sheet[r"AI36"].value=sheet[r"AF36"].value*sheet[r"AG36"].value*sheet[r"BQ38"].value/100000; 
# Calcular propiedades promedio dependiendo flowmode
if flowmode2==r"VPLUG":
    strs=str(ps1+ps2-3); fila=str(ps1+ps2-3+40); sheet[r"AU"+str(fila)].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_ENTH"+"\\"+strs).Value; sheet[r"I"+fila].value=(sheet[r"G"+fila].value+sheet[r"D37"].value+sheet[r"E"+fila].value)/3; sheet[r"O"+fila].value=(sheet[r"N"+fila].value+sheet[r"H37"].value+sheet[r"L"+fila].value)/3;
    sheet[r"AH"+fila].value=(sheet[r"AG"+fila].value+sheet[r"L37"].value+sheet[r"AE"+fila].value)/3; 
    for s in range(ps1+ps2-4,ps1-1,-1):
        strs=str(s); fila=s+40; sheet[r"AU"+str(fila)].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_ENTH"+"\\"+strs).Value; sheet[r"I"+str(fila)].value=(sheet[r"G"+str(fila)].value+sheet[r"G"+str(fila+1)].value)/2; sheet[r"O"+str(fila)].value=(sheet[r"N"+str(fila)].value+sheet[r"N"+str(fila+1)].value)/2;
        sheet[r"AH"+str(fila)].value=(sheet[r"AG"+str(fila)].value+sheet[r"AG"+str(fila+1)].value)/2;
if flowmode1==r"VPLUG":
    for s in range(ps1-1,1,-1):
        strs=str(s); fila=s+40; sheet[r"AU"+str(fila)].value=EdoEstacionario.Tree.FindNode(rutab+r"\VAP_ENTH"+"\\"+strs).Value; sheet[r"I"+str(fila)].value=(sheet[r"G"+str(fila)].value+sheet[r"G"+str(fila+1)].value)/2; sheet[r"O"+str(fila)].value=(sheet[r"N"+str(fila)].value+sheet[r"N"+str(fila+1)].value)/2;
        sheet[r"AH"+str(fila)].value=(sheet[r"AG"+str(fila)].value+sheet[r"AG"+str(fila+1)].value)/2;
# Calcular propiedades restantes dependientes del bulk
for s in range(2,ps1+ps2-2):    
    fila=str(40+s); strs=str(s); sheet[r"AA"+fila].value=sheet[r"X"+fila].value*sheet[r"O"+fila].value; sheet[r"Y"+fila].value=sheet[r"V"+fila].value-sheet[r"AA"+fila].value;
    sheet[r"Z"+fila].value=sheet[r"Y"+fila].value/EdoEstacionario.Tree.FindNode(rutab+r"\MASS_LCOEF\Vapor"+"\\"+strs+r"\AMMONIA\WATER").Value/(sheet[r"O"+fila].value-sheet[r"P"+fila].value);
    sheet[r"AD"+fila].value=sheet[r"X"+fila].value*sheet[r"R"+fila].value; sheet[r"AB"+fila].value=sheet[r"V"+fila].value-sheet[r"AD"+fila].value;
    sheet[r"AC"+fila].value=sheet[r"AB"+fila].value/EdoEstacionario.Tree.FindNode(rutab+r"\MASS_LCOEF\Liquid"+"\\"+strs+r"\AMMONIA\WATER").Value/(sheet[r"Q"+fila].value-sheet[r"R"+fila].value);
# Tranferencia de masa y energía por cada zona
sheet[r"BC48"].value=sheet.range(r"V42:V"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD48"].value=sheet.range(r"V"+str(40+ps1)+r":V"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC49"].value=sheet.range(r"W42:W"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD49"].value=sheet.range(r"W"+str(40+ps1)+r":W"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC50"].value=sheet.range(r"X42:X"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD50"].value=sheet.range(r"X"+str(40+ps1)+r":X"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC51"].value=sheet.range(r"Y42:Y"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD51"].value=sheet.range(r"Y"+str(40+ps1)+r":Y"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC52"].value=sheet.range(r"AA42:AA"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD52"].value=sheet.range(r"AA"+str(40+ps1)+r":AA"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC53"].value=sheet.range(r"AB42:AB"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD53"].value=sheet.range(r"AB"+str(40+ps1)+r":AB"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC54"].value=sheet.range(r"AD42:AD"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD54"].value=sheet.range(r"AD"+str(40+ps1)+r":AD"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC55"].value=sheet.range(r"AN42:AN"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD55"].value=sheet.range(r"AN"+str(40+ps1)+r":AN"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC56"].value=sheet.range(r"AO42:AO"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD56"].value=sheet.range(r"AO"+str(40+ps1)+r":AO"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC57"].value=sheet.range(r"AP42:AP"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD57"].value=sheet.range(r"AP"+str(40+ps1)+r":AP"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC58"].value=sheet.range(r"AQ42:AQ"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD58"].value=sheet.range(r"AQ"+str(40+ps1)+r":AQ"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC59"].value=sheet.range(r"AR42:AR"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD59"].value=sheet.range(r"AR"+str(40+ps1)+r":AR"+str(40+ps1+ps2-3)).options(np.array).value.sum();
EdoEstacionario.close(); EdoEstacionario.quit(); print(r"Exportación de resultados de Aspen Plus exitosa");
# Resumir resultados de temperatura y generar gráfica
# Arreglos de ubicación y temperatura
if ps1!=3:
    zR_top=sheet.range(r"C42:C"+str(40+ps1-1)).options(np.array).value; zR_lower=sheet.range(r"D42:D"+str(40+ps1-1)).options(np.array).value;
    TgR=sheet.range(r"AH42:AH"+str(40+ps1-1)).options(np.array).value; TlR=sheet.range(r"AJ42:AJ"+str(40+ps1-1)).options(np.array).value;
    yR=sheet.range(r"O42:O"+str(40+ps1-1)).options(np.array).value; xR=sheet.range(r"R42:R"+str(40+ps1-1)).options(np.array).value;
else:
    zR_top=[sheet.range(r"C42:C"+str(40+ps1-1)).options(np.array).value]; zR_lower=[sheet.range(r"D42:D"+str(40+ps1-1)).options(np.array).value];
    TgR=[sheet.range(r"AH42:AH"+str(40+ps1-1)).options(np.array).value]; TlR=[sheet.range(r"AJ42:AJ"+str(40+ps1-1)).options(np.array).value];
    yR=[sheet.range(r"O42:O"+str(40+ps1-1)).options(np.array).value]; xR=[sheet.range(r"R42:R"+str(40+ps1-1)).options(np.array).value];
if ps2!=3:            
    zA_top=sheet.range(r"C"+str(40+ps1)+r":C"+str(40+ps1+ps2-3)).options(np.array).value; zA_lower=sheet.range(r"D"+str(40+ps1)+r":D"+str(40+ps1+ps2-3)).options(np.array).value;
    TgA=sheet.range(r"AH"+str(40+ps1)+r":AH"+str(40+ps1+ps2-3)).options(np.array).value; TlA=sheet.range(r"AJ"+str(40+ps1)+r":AJ"+str(40+ps1+ps2-3)).options(np.array).value;
    yA=sheet.range(r"O"+str(40+ps1)+r":O"+str(40+ps1+ps2-3)).options(np.array).value; xA=sheet.range(r"R"+str(40+ps1)+r":R"+str(40+ps1+ps2-3)).options(np.array).value;
else:
    zA_top=[sheet.range(r"C"+str(40+ps1)+r":C"+str(40+ps1+ps2-3)).options(np.array).value]; zA_lower=[sheet.range(r"D"+str(40+ps1)+r":D"+str(40+ps1+ps2-3)).options(np.array).value];
    TgA=[sheet.range(r"AH"+str(40+ps1)+r":AH"+str(40+ps1+ps2-3)).options(np.array).value]; TlA=[sheet.range(r"AJ"+str(40+ps1)+r":AJ"+str(40+ps1+ps2-3)).options(np.array).value];
    yA=[sheet.range(r"O"+str(40+ps1)+r":O"+str(40+ps1+ps2-3)).options(np.array).value]; xA=[sheet.range(r"R"+str(40+ps1)+r":R"+str(40+ps1+ps2-3)).options(np.array).value];
TgCond=sheet[r"AG42"].value; TlReb=sheet[r"M37"].value; 
yCond=sheet[r"N42"].value; xReb=sheet[r"K37"].value;
# Etapa y ubicación de cada TT
indeT2=np.argmin(np.abs(np.array(zA_top)-3.9246)); indeT3=np.argmin(np.abs(np.array(zA_top)-5.5946)); indeT4=np.argmin(np.abs(np.array(zR_top)-8.7696)); 
sheet[r"BE41"].value=ps1+ps2-2; sheet[r"BF41"].value=10.2497;
sheet[r"BE42"].value=indeT2+ps1; sheet[r"BF42"].value=8.7696;
sheet[r"BE43"].value=indeT3+ps1; sheet[r"BF43"].value=5.5946;
sheet[r"BE44"].value=indeT4+2; sheet[r"BF44"].value=3.9246;
sheet[r"BE45"].value=1; sheet[r"BF45"].value=0;
# Temperaturas reales por TT
sheet[r"BB41"].value=datos[r"TT-1"][ind]; sheet[r"BB42"].value=datos[r"TT-2"][ind]; sheet[r"BB43"].value=datos[r"TT-3"][ind]; sheet[r"BB44"].value=datos[r"TT-4"][ind]; sheet[r"BB45"].value=datos[r"TT-5"][ind];
# Temperaturas de simulación en la ubicación de TT
sheet[r"BC41"].value=r"-"; sheet[r"BD41"].value=TlReb;
sheet[r"BC42"].value=TgA[indeT2]; sheet[r"BD42"].value=TlA[indeT2];
sheet[r"BC43"].value=TgA[indeT3]; sheet[r"BD43"].value=TlA[indeT3];
sheet[r"BC44"].value=TgR[indeT4]; sheet[r"BD44"].value=TlR[indeT4];
sheet[r"BC45"].value=TgCond; sheet[r"BD45"].value=r"-";
# Gráficas
figtodoT=plt.figure(figsize=(6,9)); axtodoT=figtodoT.gca(); axtodoT.set_xlabel(r"$T$ $[°C]$"); axtodoT.set_ylabel(r"$z$ $[m]$"); axtodoT.grid();
figtodoxy=plt.figure(figsize=(6,9)); axtodoxy=figtodoxy.gca(); axtodoxy.set_xlabel(r"$\overline{x}_a/\overline{y}_a$"); axtodoxy.set_ylabel(r"$z$ $[m]$"); axtodoxy.grid();
figRT=plt.figure(figsize=(6,9)); axRT=figRT.gca(); axRT.set_xlabel(r"$T$ $[°C]$"); axRT.set_ylabel(r"$z$ $[m]$"); axRT.grid();
figAT=plt.figure(figsize=(6,9)); axAT=figAT.gca(); axAT.set_xlabel(r"$T$ $[°C]$"); axAT.set_ylabel(r"$z$ $[m]$"); axAT.grid();
figRxy=plt.figure(figsize=(6,9)); axRxy=figRxy.gca(); axRxy.set_xlabel(r"$\overline{x}_a/\overline{y}_a$"); axRxy.set_ylabel(r"$z$ $[m]$"); axRxy.grid();
figAxy=plt.figure(figsize=(6,9)); axAxy=figAxy.gca(); axAxy.set_xlabel(r"$\overline{x}_a/\overline{y}_a$"); axAxy.set_ylabel(r"$z$ $[m]$"); axAxy.grid();
axtodoT.set_title(r"C-1: Perfil de temperaturas",fontweight=r"bold"); axRT.set_title(r"Rectificación: Perfil de temperaturas",fontweight=r"bold"); axAT.set_title(r"Agotamiento: Perfil de temperaturas",fontweight=r"bold");
axtodoxy.set_title(r"C-1: Perfil de composiciones",fontweight=r"bold"); axRxy.set_title(r"Rectificación: Perfil de composiciones",fontweight=r"bold"); axAxy.set_title(r"Rectificación: Perfil de composiciones",fontweight=r"bold");
# Rectificación
for s in range(ps1-2):
    if s!=0:
        axtodoT.plot([TgR[s],TgR[s]],[zR_top[s],zR_lower[s]],r"-r"); axRT.plot([TgR[s],TgR[s]],[zR_top[s],zR_lower[s]],r"-r"); 
        axtodoT.plot([TlR[s],TlR[s]],[zR_top[s],zR_lower[s]],r"-b"); axRT.plot([TlR[s],TlR[s]],[zR_top[s],zR_lower[s]],r"-b"); 
    else:
        axtodoT.plot([TgR[s],TgR[s]],[zR_top[s],zR_lower[s]],r"-r",label=r"Fase vapor en etapa"); axRT.plot([TgR[s],TgR[s]],[zR_top[s],zR_lower[s]],r"-r",label=r"Fase vapor en etapa"); 
        axtodoT.plot([TlR[s],TlR[s]],[zR_top[s],zR_lower[s]],r"-b",label=r"Fase líquida en etapa"); axRT.plot([TlR[s],TlR[s]],[zR_top[s],zR_lower[s]],r"-b",label=r"Fase líquida en etapa"); 
    axtodoT.plot([TlR[s],TgR[s]],[zR_top[s],zR_top[s]],r"-k"); axRT.plot([TlR[s],TgR[s]],[zR_top[s],zR_top[s]],r"-k");
    axtodoT.plot([TlR[s],TgR[s]],[zR_lower[s],zR_lower[s]],r"-k"); axRT.plot([TlR[s],TgR[s]],[zR_lower[s],zR_lower[s]],r"-k");
    axtodoT.fill([TgR[s],TgR[s],TlR[s],TlR[s]],[zR_top[s],zR_lower[s],zR_lower[s],zR_top[s]],r"plum"); axRT.fill([TgR[s],TgR[s],TlR[s],TlR[s]],[zR_top[s],zR_lower[s],zR_lower[s],zR_top[s]],r"plum");
    if s!=0:
        axtodoxy.plot([yR[s],yR[s]],[zR_top[s],zR_lower[s]],r"-r"); axRxy.plot([yR[s],yR[s]],[zR_top[s],zR_lower[s]],r"-r"); 
        axtodoxy.plot([xR[s],xR[s]],[zR_top[s],zR_lower[s]],r"-b"); axRxy.plot([xR[s],xR[s]],[zR_top[s],zR_lower[s]],r"-b");
    else:
        axtodoxy.plot([yR[s],yR[s]],[zR_top[s],zR_lower[s]],r"-r",label=r"Fase vapor en etapa"); axRxy.plot([yR[s],yR[s]],[zR_top[s],zR_lower[s]],r"-r",label=r"Fase vapor en etapa"); 
        axtodoxy.plot([xR[s],xR[s]],[zR_top[s],zR_lower[s]],r"-b",label=r"Fase líquida en etapa"); axRxy.plot([xR[s],xR[s]],[zR_top[s],zR_lower[s]],r"-b",label=r"Fase líquida en etapa");
    axtodoxy.plot([xR[s],yR[s]],[zR_top[s],zR_top[s]],r"-k"); axRxy.plot([xR[s],yR[s]],[zR_top[s],zR_top[s]],r"-k");
    axtodoxy.plot([xR[s],yR[s]],[zR_lower[s],zR_lower[s]],r"-k"); axRxy.plot([xR[s],yR[s]],[zR_lower[s],zR_lower[s]],r"-k");
    axtodoxy.fill([yR[s],yR[s],xR[s],xR[s]],[zR_top[s],zR_lower[s],zR_lower[s],zR_top[s]],r"plum"); axRxy.fill([yR[s],yR[s],xR[s],xR[s]],[zR_top[s],zR_lower[s],zR_lower[s],zR_top[s]],r"plum");
axtodoT.plot(TgCond,10.2497,r"or",label=r"Vapor al condensador"); axRT.plot(TgCond,10.2497,r"or",label=r"Vapor al condensador"); axtodoxy.plot(yCond,10.2497,r"or",label=r"Vapor al condensador"); axRxy.plot(yCond,10.2497,r"or",label=r"Vapor al condensador");
axtodoT.plot(datos[r"TT-5"][ind],10.2497,r"^g"); axRT.plot(datos[r"TT-5"][ind],10.2497,r"^g",label=r"TT real"); axtodoT.plot(datos[r"TT-4"][ind],8.7696,r"^g"); axRT.plot(datos[r"TT-4"][ind],8.7696,r"^g");
# Agotamiento
for s in range(ps2-2):
    axtodoT.plot([TgA[s],TgA[s]],[zA_top[s],zA_lower[s]],r"-r"); axtodoT.plot([TlA[s],TlA[s]],[zA_top[s],zA_lower[s]],r"-b"); 
    if s!=0:
        axAT.plot([TgA[s],TgA[s]],[zA_top[s],zA_lower[s]],r"-r"); axAT.plot([TlA[s],TlA[s]],[zA_top[s],zA_lower[s]],r"-b"); 
    else:
        axAT.plot([TgA[s],TgA[s]],[zA_top[s],zA_lower[s]],r"-r",label=r"Fase vapor en etapa"); axAT.plot([TlA[s],TlA[s]],[zA_top[s],zA_lower[s]],r"-b",label=r"Fase líquida en etapa"); 
    axtodoT.plot([TlA[s],TgA[s]],[zA_top[s],zA_top[s]],r"-k"); axAT.plot([TlA[s],TgA[s]],[zA_top[s],zA_top[s]],r"-k");
    axtodoT.plot([TlA[s],TgA[s]],[zA_lower[s],zA_lower[s]],r"-k"); axAT.plot([TlA[s],TgA[s]],[zA_lower[s],zA_lower[s]],r"-k");
    axtodoT.fill([TgA[s],TgA[s],TlA[s],TlA[s]],[zA_top[s],zA_lower[s],zA_lower[s],zA_top[s]],r"plum"); axAT.fill([TgA[s],TgA[s],TlA[s],TlA[s]],[zA_top[s],zA_lower[s],zA_lower[s],zA_top[s]],r"plum");
    axtodoxy.plot([yA[s],yA[s]],[zA_top[s],zA_lower[s]],r"-r"); axtodoxy.plot([xA[s],xA[s]],[zA_top[s],zA_lower[s]],r"-b"); 
    if s!=0:
        axAxy.plot([yA[s],yA[s]],[zA_top[s],zA_lower[s]],r"-r"); axAxy.plot([xA[s],xA[s]],[zA_top[s],zA_lower[s]],r"-b");
    else:
        axAxy.plot([yA[s],yA[s]],[zA_top[s],zA_lower[s]],r"-r",label=r"Fase vapor en etapa"); axAxy.plot([xA[s],xA[s]],[zA_top[s],zA_lower[s]],r"-b",label=r"Fase líquida en etapa");
    axtodoxy.plot([xA[s],yA[s]],[zA_top[s],zA_top[s]],r"-k"); axAxy.plot([xA[s],yA[s]],[zA_top[s],zA_top[s]],r"-k");
    axtodoxy.plot([xA[s],yA[s]],[zA_lower[s],zA_lower[s]],r"-k"); axAxy.plot([xA[s],yA[s]],[zA_lower[s],zA_lower[s]],r"-k");
    axtodoxy.fill([yA[s],yA[s],xA[s],xA[s]],[zA_top[s],zA_lower[s],zA_lower[s],zA_top[s]],r"plum"); axAxy.fill([yA[s],yA[s],xA[s],xA[s]],[zA_top[s],zA_lower[s],zA_lower[s],zA_top[s]],r"plum");
axtodoT.plot(TlReb,0,r"ob",label=r"Líquido al rehervidor"); axAT.plot(TlReb,0,r"ob",label=r"Líquido al rehervidor"); axtodoxy.plot(xReb,0,r"ob",label=r"Líquido al rehervidor"); axAxy.plot(xReb,0,r"ob",label=r"Líquido al rehervidor");
axtodoT.plot(datos[r"TT-1"][ind],0,r"^g",label=r"TT Real"); axAT.plot(datos[r"TT-1"][ind],0,r"^g",label=r"TT Real"); axtodoT.plot(datos[r"TT-2"][ind],3.9246,r"^g"); axAT.plot(datos[r"TT-2"][ind],3.9246,r"^g");
axtodoT.plot(datos[r"TT-3"][ind],5.5946,r"^g"); axAT.plot(datos[r"TT-3"][ind],5.5946,r"^g");
axtodoT.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0); axtodoxy.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0); axRT.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0); 
axAT.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0); axRxy.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0); axAxy.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0);
figtodoT.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68); figRT.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68); figAT.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68); 
figtodoxy.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68); figRxy.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68); figAxy.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68);
fila=63; espacio=44;
sheet.pictures.add(figtodoT,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); fila=fila+espacio;
sheet.pictures.add(figRT,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); fila=fila+espacio;
sheet.pictures.add(figAT,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); fila=fila+espacio;
sheet.pictures.add(figtodoxy,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); fila=fila+espacio;
sheet.pictures.add(figRxy,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); fila=fila+espacio;
sheet.pictures.add(figAxy,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); 
# Calor en rehervidor mediante TT-6 y TT-7: Estado cuasi-estacionario de aceite térmico
TT6=datos[r"TT-6"][ind]+273.15; TT7=datos[r"TT-7"][ind]+273.15; # [K]
FIC1=datos[r"FIC-1"][ind];
rhoHO=-1.27492E-6*TT7**2-0.001732*TT7+4.61675; # Densidad [kmol/m3]
sheet[r"BT27"].value=TT6-273.15; sheet[r"BT28"].value=TT7-273.15; # [°C]
sheet[r"BV27"].value=FIC1; sheet[r"BV28"].value=FIC1*rhoHO;
sheet[r"BX25"].value=(0.45784*(TT6**2-TT7**2)+121.3161*(TT6-TT7))*rhoHO*FIC1; # Calor sensible como dh*Fmolar [kJ/kmol]
########################################################################################################################
# Comprobación de propiedades relacionadas al bulk con propuesta en Aspen Custom Modeler y guardado de valores iniciales de bulk en Bulkres
Bulkres=np.zeros((81,ps1+ps2-4)); ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"Bulk.dynf")); 
Sim=ACM.Simulation; Bulk=Sim.Flowsheet.Blocks(r"Bulk"); 
dh=4*Bulk.epsilon.Value/Bulk.ap.Value; deq=6*(1-Bulk.epsilon.Value)/Bulk.ap.Value;
ap=Bulk.ap.Value; gc=Bulk.gc.Value; epsilon=Bulk.epsilon.Value;
for s in range(2,ps1+ps2-2):    
    fila=str(40+s); Bulk.Vs.Value=sheet[r"G"+fila].value; Bulk.Ls.Value=sheet[r"H"+fila].value; Bulk.Tsg.Value=sheet[r"AG"+fila].value; Bulk.Tsl.Value=sheet[r"AK"+fila].value; Bulk.Ps.Value=sheet[r"AY"+fila].value;
    Bulk.ys(r"AMMONIA").Value=sheet[r"N"+fila].value; Bulk.ys(r"WATER").Value=1-sheet[r"N"+fila].value; Bulk.xs(r"AMMONIA").Value=sheet[r"S"+fila].value; Bulk.xs(r"WATER").Value=1-sheet[r"S"+fila].value;
    Bulk.Vb.Value=sheet[r"I"+fila].value; Bulk.Lb.Value=sheet[r"J"+fila].value; Bulk.Tbg.Value=sheet[r"AH"+fila].value; Bulk.Tbl.Value=sheet[r"AJ"+fila].value; Bulk.Zs.Value=sheet[r"C"+fila].value-sheet[r"D"+fila].value;
    Bulk.Pb.Value=sheet[r"AY"+fila].value; Bulk.yb(r"AMMONIA").Value=sheet[r"O"+fila].value; Bulk.yb(r"WATER").Value=1-sheet[r"O"+fila].value; Bulk.xb(r"AMMONIA").Value=sheet[r"R"+fila].value; Bulk.xb(r"WATER").Value=1-sheet[r"R"+fila].value; 
    Bulk.TI.Value=sheet[r"AI"+fila].value; Bulk.yI(r"AMMONIA").Value=sheet[r"P"+fila].value; Bulk.yI(r"WATER").Value=1-sheet[r"P"+fila].value; Bulk.xI(r"AMMONIA").Value=sheet[r"Q"+fila].value; Bulk.xI(r"WATER").Value=1-sheet[r"Q"+fila].value;
    Bulk.Nas.Value=sheet[r"V"+fila].value; Bulk.Nts.Value=sheet[r"X"+fila].value; Bulk.Es.Value=sheet[r"AN"+fila].value/1000000; Sim.Run(True);
    sheet[r"BJ"+fila].value=Bulk.rhobg.Value; sheet[r"BK"+fila].value=Bulk.rhobl.Value; sheet[r"BN"+fila].value=Bulk.Dbg(r"AMMONIA",r"WATER").Value*0.36; sheet[r"BO"+fila].value=Bulk.Dbl(r"AMMONIA",r"WATER").Value*0.36;
    sheet[r"BP"+fila].value=Bulk.Cpbg.Value; sheet[r"BQ"+fila].value=Bulk.Cpbl.Value; sheet[r"BR"+fila].value=Bulk.kappabg.Value*3.6; sheet[r"BS"+fila].value=Bulk.kappabl.Value*3.6;
    sheet[r"BT"+fila].value=Bulk.mubg.Value*3.6; sheet[r"BU"+fila].value=Bulk.mubl.Value*3.6; sheet[r"BV"+fila].value=Bulk.sigmabl.Value*(3600**2);
    sheet[r"BW"+fila].value=Bulk.Uspg.Value*3600; sheet[r"BX"+fila].value=Bulk.Uspl.Value*3600; sheet[r"CA"+fila].value=Bulk.Scg.Value; sheet[r"CB"+fila].value=Bulk.Scl.Value; sheet[r"BS38"].value=Bulk.dh.Value;
    sheet[r"CE"+fila].value=Bulk.Regc.Value; sheet[r"CF"+fila].value=Bulk.Relc.Value; sheet[r"CH"+fila].value=Bulk.Wel.Value; sheet[r"CJ"+fila].value=Bulk.Frlc.Value; 
    sheet[r"CK"+fila].value=Bulk.kbmg.Value*3600; sheet[r"CL"+fila].value=Bulk.kbml.Value*3600; sheet[r"CM"+fila].value=Bulk.khg.Value*3600; sheet[r"CN"+fila].value=Bulk.khl.Value*3600; 
    sheet[r"CP"+fila].value=Bulk.aef.Value; sheet[r"CQ"+fila].value=Bulk.ubg.Value*1000000; sheet[r"CR"+fila].value=Bulk.ubl.Value*1000000; sheet[r"CS"+fila].value=Bulk.Gammabl.Value;
    sheet[r"CT"+fila].value=Bulk.hpabg.Value*1000000; sheet[r"CU"+fila].value=Bulk.hpwbg.Value*1000000; sheet[r"CV"+fila].value=Bulk.hpabl.Value*1000000; sheet[r"CW"+fila].value=Bulk.hpwbl.Value*1000000;
    sheet[r"CX"+fila].value=sheet[r"CT"+fila].value*sheet[r"V"+fila].value+sheet[r"CU"+fila].value*sheet[r"W"+fila].value; sheet[r"CY"+fila].value=sheet[r"CV"+fila].value*sheet[r"V"+fila].value+sheet[r"CW"+fila].value*sheet[r"W"+fila].value;
    sheet[r"CZ"+fila].value=Bulk.dPirr.Value*(sheet[r"C"+fila].value-sheet[r"D"+fila].value)/100000; 
    sheet[r"DA"+fila].value=Bulk.Nas.Value; sheet[r"DB"+fila].value=Bulk.Nts.Value; sheet[r"DC"+fila].value=Bulk.Es.Value*1000000; 
    sheet[r"DD"+fila].value=Bulk.yI(r"AMMONIA").Value; sheet[r"DE"+fila].value=Bulk.xI(r"AMMONIA").Value; sheet[r"DF"+fila].value=Bulk.TI.Value;
    Bulkres[0][s-2]=Bulk.hsg.Value; Bulkres[1][s-2]=Bulk.hsl.Value; Bulkres[2][s-2]=Bulk.rhobg.Value; Bulkres[3][s-2]=Bulk.rhobl.Value; 
    Bulkres[4][s-2]=Bulk.Dbg(r"AMMONIA",r"AMMONIA").Value; Bulkres[5][s-2]=Bulk.Dbl(r"AMMONIA",r"AMMONIA").Value; Bulkres[6][s-2]=Bulk.Dbg(r"AMMONIA",r"WATER").Value; Bulkres[7][s-2]=Bulk.Dbl(r"AMMONIA",r"WATER").Value;
    Bulkres[8][s-2]=Bulk.Dbg(r"WATER",r"AMMONIA").Value; Bulkres[9][s-2]=Bulk.Dbl(r"WATER",r"AMMONIA").Value; Bulkres[10][s-2]=Bulk.Dbg(r"WATER",r"WATER").Value; Bulkres[11][s-2]=Bulk.Dbl(r"WATER",r"WATER").Value;
    Bulkres[12][s-2]=Bulk.Cpbg.Value; Bulkres[13][s-2]=Bulk.Cpbl.Value; Bulkres[14][s-2]=Bulk.kappabg.Value; Bulkres[15][s-2]=Bulk.kappabl.Value; Bulkres[16][s-2]=Bulk.mubg.Value; Bulkres[17][s-2]=Bulk.mubl.Value; Bulkres[18][s-2]=Bulk.sigmabl.Value;
    Bulkres[19][s-2]=Bulk.Uspg.Value; Bulkres[20][s-2]=Bulk.Uspl.Value; Bulkres[21][s-2]=Bulk.MWg.Value; Bulkres[22][s-2]=Bulk.MWl.Value; Bulkres[23][s-2]=Bulk.Scg.Value; Bulkres[24][s-2]=Bulk.Scl.Value;  
    Bulkres[25][s-2]=Bulk.Regc.Value; Bulkres[26][s-2]=Bulk.Relc.Value; Bulkres[27][s-2]=Bulk.Wel.Value; Bulkres[28][s-2]=Bulk.Frlc.Value; Bulkres[29][s-2]=Bulk.kbmg.Value; Bulkres[30][s-2]=Bulk.kbml.Value; 
    Bulkres[31][s-2]=Bulk.khg.Value; Bulkres[32][s-2]=Bulk.khl.Value; Bulkres[33][s-2]=Bulk.aef.Value; Bulkres[34][s-2]=Bulk.hbg.Value; Bulkres[35][s-2]=Bulk.hbl.Value; 
    Bulkres[36][s-2]=Bulk.cabl(r"AMMONIA").Value; Bulkres[37][s-2]=Bulk.cabl(r"WATER").Value; Bulkres[38][s-2]=Bulk.yba(r"AMMONIA").Value; Bulkres[39][s-2]=Bulk.yba(r"WATER").Value; Bulkres[40][s-2]=Bulk.ybd(r"AMMONIA").Value; 
    Bulkres[41][s-2]=Bulk.ybd(r"WATER").Value; Bulkres[42][s-2]=Bulk.xba(r"AMMONIA").Value; Bulkres[43][s-2]=Bulk.xba(r"WATER").Value; Bulkres[44][s-2]=Bulk.xbd(r"AMMONIA").Value; Bulkres[45][s-2]=Bulk.xbd(r"WATER").Value;
    Bulkres[46][s-2]=Bulk.hga.Value; Bulkres[47][s-2]=Bulk.hla.Value; Bulkres[48][s-2]=Bulk.hgd.Value; Bulkres[49][s-2]=Bulk.hld.Value; 
    Bulkres[50][s-2]=Bulk.cala(r"AMMONIA").Value; Bulkres[51][s-2]=Bulk.cala(r"WATER").Value; Bulkres[52][s-2]=Bulk.cald(r"AMMONIA").Value; Bulkres[53][s-2]=Bulk.cald(r"WATER").Value; 
    Bulkres[54][s-2]=Bulk.ubg.Value; Bulkres[55][s-2]=Bulk.ubl.Value; Bulkres[56][s-2]=Bulk.Gammabl.Value; Bulkres[57][s-2]=Bulk.hpabg.Value; Bulkres[58][s-2]=Bulk.hpwbg.Value; Bulkres[59][s-2]=Bulk.hpabl.Value; Bulkres[60][s-2]=Bulk.hpwbl.Value; 
    Bulkres[61][s-2]=Bulk.Regp.Value; Bulkres[62][s-2]=Bulk.Frlp.Value; Bulkres[63][s-2]=Bulk.Hpr.Value; Bulkres[64][s-2]=Bulk.FSt.Value; Bulkres[65][s-2]=Bulk.CSt.Value; Bulkres[66][s-2]=Bulk.dPdry.Value; Bulkres[67][s-2]=Bulk.H.Value; Bulkres[68][s-2]=Bulk.dPirr.Value; 
    Bulkres[69][s-2]=Bulk.Nas.Value; Bulkres[70][s-2]=Bulk.Nts.Value; Bulkres[71][s-2]=Bulk.Es.Value; 
    Bulkres[72][s-2]=Bulk.yI(r"AMMONIA").Value; Bulkres[73][s-2]=Bulk.yI(r"WATER").Value; Bulkres[74][s-2]=Bulk.xI(r"AMMONIA").Value; Bulkres[75][s-2]=Bulk.xI(r"WATER").Value; Bulkres[76][s-2]=Bulk.TI.Value;
    Bulkres[77][s-2]=Bulk.phiIg(r"AMMONIA").Value; Bulkres[78][s-2]=Bulk.phiIg(r"WATER").Value; Bulkres[79][s-2]=Bulk.phiIl(r"AMMONIA").Value; Bulkres[80][s-2]=Bulk.phiIl(r"WATER").Value;    
ACM.quit(); print(r"Exportación de resultados de Bulk exitosa");
# h de entradas y salidas de E-2/propiedades en E-1 con Aspen Custom Modeler
ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"Unafase.dynf")); Sim=ACM.Simulation; Unafase=Sim.Flowsheet.Blocks(r"Unafase"); 
Unafase.Fase.Value=r"LIQUIDO"; Unafase.T.Value=sheet[r"M37"].value; Unafase.P.Value=sheet[r"V37"].value; Unafase.o(r"AMMONIA").Value=sheet[r"I37"].value; Unafase.o(r"WATER").Value=1-sheet[r"I37"].value; 
Sim.Run(True); sheet[r"R37"].value=Unafase.h.Value*1000000; rhosumidero=Unafase.rho.Value; MWsumidero=Unafase.MW.Value;
Unafase.Fase.Value=r"VAPOR"; Unafase.T.Value=sheet[r"N37"].value; Unafase.P.Value=sheet[r"W37"].value; Unafase.o(r"AMMONIA").Value=sheet[r"J37"].value; Unafase.o(r"WATER").Value=1-sheet[r"J37"].value; 
Sim.Run(True); sheet[r"S37"].value=Unafase.h.Value*1000000; sheet[r"AS"+str(40+ps1+ps2-3)].value=Unafase.h.Value*1000000;
Unafase.Fase.Value=r"LIQUIDO"; Unafase.T.Value=sheet[r"AB36"].value; Unafase.P.Value=sheet[r"AD36"].value; Unafase.o(r"AMMONIA").Value=sheet[r"AA36"].value; Unafase.o(r"WATER").Value=1-sheet[r"AA36"].value; 
Sim.Run(True); sheet[r"AC36"].value=Unafase.h.Value*1000000;
ACM.quit(); print(r"Exportación de resultados de Unafase exitosa");
# Empieza ejecución de archivos de Aspen Custom Modeler exclusivo para obtener valores iniciales y análisis de modelo en estado estacionario implementado en Aspen Custom Modeler
res=input(r"¿Desea simular caso estacionario en Aspen Custom Modeler? [S/N]: ");
if res!=r"S":
    wb.remove(wb[r"Exportar_resultados_ACM"]); wb.save(); wb.close(); exit(); print(r"Guardado de Excel exitoso"); 
# Tdew en E-2/Tbubble en E-3 con Aspen Custom Modeler
ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"Posat.dynf")); Sim=ACM.Simulation; Sat=Sim.Flowsheet.Blocks(r"Sat"); 
Sat.P.Value=sheet[r"BX6"].value; Sat.o(r"AMMONIA").Value=sheet[r"BX7"].value; Sat.o(r"WATER").Value=1-sheet[r"BX7"].value; Sim.Run(True); TdewE2=Sat.Tdew.Value;
Sat.P.Value=sheet[r"O5"].value; Sat.o(r"AMMONIA").Value=sheet[r"O6"].value; Sat.o(r"WATER").Value=1-sheet[r"O6"].value; Sim.Run(True); TbubbleE3=Sat.Tbubble.Value;
ACM.quit(); print(r"Exportación de resultados de Posat exitosa");
# Guardado de valores iniciales de E-1 en E1res
E1res=np.zeros((35,1)); ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"E1.dynf")); 
Sim=ACM.Simulation; E1=Sim.Flowsheet.Blocks(r"E-1");
E1.E_CF_in.T.Value=datos[r"TE,CF,in"][ind]; # Temperatura de entrada al sistema [°C]
E1.E_CF_in.P.Value=18.6326; # Presión de entrada al sistema [bar]
E1.E_CF_in.F.Value=datos[r"FT-1"][ind]/17.8093; # Flujo molar de entrada al sistema [kmol/h]
E1.E_CF_in.z(r"AMMONIA").Value=0.209146; # Fracción molar de entrada al sistema 
E1.E_CF_in.z(r"WATER").Value=1-0.209146; # Fracción molar de entrada al sistema
E1.E_CF_out.T.Value=sheet[r"H15"].value; E1.E_CF_out.P.Value=E1.E_CF_in.P.Value; E1.E_CF_out.F.Value=E1.E_CF_in.F.Value; 
E1.E_CF_out.z(r"AMMONIA").Value=E1.E_CF_in.z(r"AMMONIA").Value; E1.E_CF_out.z(r"WATER").Value=E1.E_CF_in.z(r"WATER").Value; 
E1.E_HF_in.T.Value=sheet[r"F15"].value; E1.E_HF_in.P.Value=sheet[r"F16"].value; 
E1.E_HF_in.F.Value=sheet[r"F14"].value; E1.E_HF_in.z(r"AMMONIA").Value=sheet[r"F17"].value; E1.E_HF_in.z(r"WATER").Value=1-sheet[r"F17"].value; 
E1.E_HF_out.T.Value=sheet[r"F4"].value; E1.E_HF_out.P.Value=E1.E_HF_in.P.Value; E1.E_HF_out.F.Value=E1.E_HF_in.F.Value; 
E1.E_HF_out.z(r"AMMONIA").Value=E1.E_HF_in.z(r"AMMONIA").Value; E1.E_HF_out.z(r"WATER").Value=E1.E_HF_in.z(r"WATER").Value; Sim.Run(True);
E1res[0][0]=E1.hE_HF_in.Value; E1res[1][0]=E1.hE_HF_out.Value; E1res[2][0]=E1.hE_CF_in.Value; E1res[3][0]=E1.hE_CF_out.Value; E1res[4][0]=E1.dT1.Value; E1res[5][0]=E1.dT2.Value; E1res[6][0]=E1.dTln.Value;
E1res[7][0]=E1.RF.Value; E1res[8][0]=E1.PF.Value; E1res[9][0]=E1.alphaF.Value; E1res[10][0]=E1.SF.Value; E1res[11][0]=E1.F.Value; E1res[12][0]=E1.MWint.Value; E1res[13][0]=E1.muint.Value; E1res[14][0]=E1.Cpint.Value;
E1res[15][0]=E1.kappaint.Value; E1res[16][0]=E1.Re_int.Value; E1res[17][0]=E1.Pr_int.Value; E1res[18][0]=E1.Nu_int.Value; E1res[19][0]=E1.hint.Value; E1res[20][0]=E1.MWext.Value; E1res[21][0]=E1.muext.Value;
E1res[22][0]=E1.Cpext.Value; E1res[23][0]=E1.kappaext.Value; E1res[24][0]=E1.Afc.Value; E1res[25][0]=E1.Re_ext.Value; E1res[26][0]=E1.Pr_ext.Value; E1res[27][0]=E1.a1.Value; E1res[28][0]=E1.a2.Value; E1res[29][0]=E1.aBD.Value;
E1res[30][0]=E1.jH.Value; E1res[31][0]=E1.hext.Value; E1res[32][0]=E1.U.Value; E1res[33][0]=E1.rhoE_HF.Value; E1res[34][0]=E1.EHFq.Value;
ACM.quit(); print(r"Exportación de resultados de E1 exitosa");
# Checar teoría de Nusselt en E-3
ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"E3.dynf")); Sim=ACM.Simulation; E3=Sim.Flowsheet.Blocks(r"E-3"); Divisor=Sim.Flowsheet.Blocks(r"Divisor");
Divisor.Reflujo.F.Value=datos[r"FT-2"][ind]*0.585022/17.03518; Divisor.Prod_Liq.F.Value=datos[r"FIT-1"][ind]/17.03518;
Divisor.C_HF_out.F.Value=Divisor.Reflujo.F.Value+Divisor.Prod_Liq.F.Value; Divisor.RR.Value=Divisor.Reflujo.F.Value/Divisor.Prod_Liq.F.Value;
E3.Vap_s_2.T.Value=sheet[r"O4"].value; E3.Vap_s_2.P.Value=sheet[r"O5"].value; E3.Vap_s_2.z(r"AMMONIA").Value=sheet[r"O6"].value; E3.Vap_s_2.z(r"WATER").Value=1-sheet[r"O6"].value;
E3.C_HF_out.T.Value=sheet[r"O14"].value; E3.C_HF_out.P.Value=sheet[r"O5"].value; E3.C_HF_out.z(r"AMMONIA").Value=sheet[r"O6"].value; E3.C_HF_out.z(r"WATER").Value=1-sheet[r"O6"].value;
Divisor.C_HF_out.T.Value=sheet[r"O14"].value; Divisor.C_HF_out.P.Value=sheet[r"O5"].value; Divisor.C_HF_out.z(r"AMMONIA").Value=sheet[r"O6"].value; Divisor.C_HF_out.z(r"WATER").Value=1-sheet[r"O6"].value;
Divisor.Reflujo.T.Value=sheet[r"O14"].value; Divisor.Reflujo.P.Value=sheet[r"O5"].value; Divisor.Reflujo.z(r"AMMONIA").Value=sheet[r"O6"].value; Divisor.Reflujo.z(r"WATER").Value=1-sheet[r"O6"].value;
Divisor.Prod_Liq.T.Value=sheet[r"O14"].value; Divisor.Prod_Liq.P.Value=sheet[r"O5"].value; Divisor.Prod_Liq.z(r"AMMONIA").Value=sheet[r"O6"].value; Divisor.Prod_Liq.z(r"WATER").Value=1-sheet[r"O6"].value;
E3.C_CF_in.T.Value=30; E3.C_CF_in.P.Value=3.43233; E3.C_CF_in.z(r"AMMONIA").Value=0; E3.C_CF_in.z(r"WATER").Value=1;
ToutCFmax=float(fsolve(fFToutCF,x0=34,args=(E3.Vap_s_2.T.Value,E3.C_HF_out.T.Value,E3.C_CF_in.T.Value,E3.np_HF.Value,0.8))); # Máximo ToutCF para un diseño eficiente
Fdiseño=F((34-30)/(64-30),(64-47)/(34-30),1); # F de diseño de E-3
ToutCFdiseño=float(fsolve(fFToutCF,x0=34,args=(E3.Vap_s_2.T.Value,E3.C_HF_out.T.Value,E3.C_CF_in.T.Value,E3.np_HF.Value,Fdiseño))); # ToutCF con Fdiseño
ToutCFdata=np.linspace(E3.C_CF_in.T.Value+0.5,ToutCFmax,50); FCF=np.zeros((50,1)); QU=np.zeros((50,1)); QCF=np.zeros((50,1)); mtCF=np.zeros((50,1)); hintCF=np.zeros((50,1)); hextCF=np.zeros((50,1)); 
for i in range(0,50):
    E3.C_CF_out.T.Value=ToutCFdata[i]; Sim.Run(True); mtCF[i][0]=E3.CCFmt.Value; FCF[i][0]=E3.F.Value; QU[i][0]=E3.QCU.Value*1000000; QCF[i][0]=E3.QCHF.Value*1000000; hintCF[i][0]=E3.hint.Value*3600; hextCF[i][0]=E3.hext.Value*3600;
fig1E3,ax1=plt.subplots(figsize=(7,7)); plt.title(r"Análisis de $\dot{Q}$ respecto a $F$ y $T_{CF}^{out}$",fontweight=r"bold");
ax1.set_xlabel(r"$T_{CF}^{out}$ $[°C]$"); ax1.set_ylabel(r"$\dot{Q}$ $[kJ/h]$",color=r"b"); plt.grid();
ax1.plot(ToutCFdata,QU,r"b--",label=r"Por geometría"); ax1.plot(ToutCFdata,QCF,r"b:",label=r"Por balance de energía HF"); ax1.ticklabel_format(axis=r"y",style=r"sci",scilimits=(6,6));
ax1.tick_params(axis=r"y",labelcolor=r"b"); ax2=ax1.twinx(); ax2.set_ylabel(r"$F$",color=r"r"); 
ax2.plot(ToutCFdata,FCF,r"r-"); ax2.tick_params(axis=r"y",labelcolor=r"r"); ax1.legend(loc=r"upper right");
fig2E3,ax1=plt.subplots(figsize=(7,7)); plt.title(r"Análisis de $\dot{h}$ y $\dot{m}_{t,CF}$ respecto a $F$",fontweight=r"bold");
ax1.set_xlabel(r"$F$"); ax1.set_ylabel(r"$\dot{h}$ $[kJ/h\cdot m^{2}\cdot K]$",color=r"b"); plt.grid();
ax1.plot(FCF,hintCF,r"b--",label=r"Interno"); ax1.plot(FCF,hextCF,r"b:",label=r"Externo"); ax1.ticklabel_format(axis=r"y",style=r"sci",scilimits=(4,4));
ax1.tick_params(axis=r"y",labelcolor=r"b"); ax2=ax1.twinx(); ax2.set_ylabel(r"$\dot{m}_{t,CF}$ $[kg/h]$",color=r"r"); ax2.ticklabel_format(axis=r"y",style=r"sci",scilimits=(5,5));
ax2.plot(FCF,mtCF,r"r-"); ax2.tick_params(axis=r"y",labelcolor=r"r"); ax2.invert_xaxis(); ax1.legend(loc=r"upper right");
# Datos con F=Fdiseño
E3.C_CF_out.T.Value=ToutCFdiseño; Sim.Run(True); E3res=np.zeros((21,1));  
# Guardado de valores iniciales de E-3 en E3res
E3res[0][0]=E3.C_CF_out.T.Value; E3res[1][0]=E3.C_CF_out.F.Value; E3res[2][0]=E3.hVap_s_2.Value; E3res[3][0]=E3.hC_HF_out.Value; E3res[4][0]=E3.hC_CF_in.Value; E3res[5][0]=E3.hC_CF_out.Value;
E3res[6][0]=E3.MWC_CF.Value; E3res[7][0]=E3.CCFmt.Value; E3res[8][0]=E3.dT1.Value; E3res[9][0]=E3.dT2.Value; E3res[10][0]=E3.dTln.Value; E3res[11][0]=E3.RF.Value;
E3res[12][0]=E3.PF.Value; E3res[13][0]=E3.alphaF.Value; E3res[14][0]=E3.SF.Value; E3res[15][0]=E3.F.Value; E3res[16][0]=Divisor.RR.Value; E3res[17][0]=E3.rhoC_CF.Value; E3res[18][0]=E3.CCFq.Value; 
E3res[19][0]=Divisor.rhoProd_Liq.Value; E3res[20][0]=Divisor.Prod_Liqq.Value; ACM.quit(); print(r"Exportación de resultados de E3 exitosa");
sheet=wb.sheets[r"Exportar_resultados_ACM"]; sheet.pictures.add(fig1E3,left=sheet.range(r"BH39").left,top=sheet.range(r"BH39").top); sheet.pictures.add(fig2E3,left=sheet.range(r"BH73").left,top=sheet.range(r"BH73").top); sheet=wb.sheets[r"Exportar_resultados_AP"]; 
# Simulación en estado estacionario en Aspen Custom Modeler 
ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"Estacionario_ACM.dynf")); Sim=ACM.Simulation;
# Referencia a bloques 
E1=Sim.Flowsheet.Blocks(r"E-1"); E3=Sim.Flowsheet.Blocks(r"E-3"); Divisor=Sim.Flowsheet.Blocks(r"Divisor"); Thermosiphon=Sim.Flowsheet.Blocks(r"Thermosiphon"); C1=Sim.Flowsheet.Blocks(r"C-1");
# Asignación de valores fijos en E-1
E1.E_CF_in.T.Value=datos[r"TE,CF,in"][ind]; # Temperatura de entrada al sistema [°C]
E1.E_CF_in.P.Value=18.6326; # Presión de entrada al sistema [bar]
E1.E_CF_in.F.Value=datos[r"FT-1"][ind]/17.8093; # Flujo molar de entrada al sistema [kmol/h]
E1.E_CF_in.z(r"AMMONIA").Value=0.209146; # Fracción molar de entrada al sistema 
E1.E_CF_in.z(r"WATER").Value=1-0.209146; # Fracción molar de entrada al sistema
# Asignación de valores fijos en termosifón
Thermosiphon.z.Value=z_LT1(datos[r"LT-1"][ind]/100); # Altura en el sumidero [m]
# Asignación de valores fijos en E-3
E3.Vap_s_2.P.Value=datos[r"PT-2"][ind]/1.01972; C1.Vap_s_2.P.Value=datos[r"PT-2"][ind]/1.01972; # Presión de vapor en s=2 [bar]
# Asignación de valores fijos en Divisor
Divisor.Prod_Liq.F.Value=datos[r"FIT-1"][ind]/17.03518; # Destilado [kmol/h]
Divisor.Reflujo.F.Value=datos[r"FT-2"][ind]*0.585022/17.03518; C1.Reflujo.F.Value=datos[r"FT-2"][ind]*0.585022/17.03518; # Reflujo [kmol/h]
# Asignación de valores fijos en C-1
C1.ps1.Value=ps1; C1.ps2.Value=ps2; C1.flowmode1.Value=flowmode1; C1.flowmode2.Value=flowmode2;
if simtype==0:
    for i in range(2,ps1):
        C1.Zs(i).Value=1.89/(ps1-2);
    for i in range(ps1,ps1+ps2-2):
        C1.Zs(i).Value=3.99/(ps2-2);
else:
    for i in range(2,nborde1+2):
        C1.Zs(i).Value=(1.89*pborde1)/nborde1;
    for i in range(nborde1+2,ps1-nborde1):
        C1.Zs(i).Value=(1.89*(1-2*pborde1))/(ps1-2-2*nborde1);
    for i in range(ps1-nborde1,ps1):
        C1.Zs(i).Value=(1.89*pborde1)/nborde1;    
    for i in range(ps1,ps1+nborde2):
        C1.Zs(i).Value=(3.99*pborde2)/nborde2;
    for i in range(ps1+nborde2,ps1+ps2-nborde2-2):
        C1.Zs(i).Value=(3.99*(1-2*pborde2))/(ps2-2-2*nborde2);
    for i in range(ps1+ps2-nborde2-2,ps1+ps2-2):
        C1.Zs(i).Value=(3.99*pborde2)/nborde2;   
# Iniciación de valores para evitar errores en primera iteración
# C-1
C1.dh.Value=dh; C1.deq.Value=deq;
for s in range(2,ps1+ps2-2):
    fila=str(40+s); C1.Vs(s).Value=sheet[r"G"+fila].value; C1.Ls(s).Value=sheet[r"H"+fila].value; C1.Tsg(s).Value=sheet[r"AG"+fila].value; C1.Tsl(s).Value=sheet[r"AK"+fila].value; C1.Ps(s).Value=sheet[r"AY"+fila].value;
    C1.ys(r"AMMONIA",s).Value=sheet[r"N"+fila].value; C1.ys(r"WATER",s).Value=1-sheet[r"N"+fila].value; C1.xs(r"AMMONIA",s).Value=sheet[r"S"+fila].value; C1.xs(r"WATER",s).Value=1-sheet[r"S"+fila].value;
    C1.Vb(s).Value=C1.Vs(s).Value; C1.Lb(s).Value=C1.Ls(s).Value; C1.Tbg(s).Value=C1.Tsg(s).Value; C1.Tbl(s).Value=C1.Tsl(s).Value; C1.Pb(s).Value=C1.Ps(s).Value;  
    C1.yb(r"AMMONIA",s).Value=C1.ys(r"AMMONIA",s).Value; C1.yb(r"WATER",s).Value=C1.ys(r"WATER",s).Value; C1.xb(r"AMMONIA",s).Value=C1.xs(r"AMMONIA",s).Value; C1.xb(r"WATER",s).Value=C1.xs(r"WATER",s).Value;
    C1.hsg(s).Value=Bulkres[0][s-2]; C1.hsl(s).Value=Bulkres[1][s-2]; C1.rhobg(s).Value=Bulkres[2][s-2]; C1.rhobl(s).Value=Bulkres[3][s-2]; 
    C1.Dbg(r"AMMONIA",r"AMMONIA",s).Value=Bulkres[4][s-2]; C1.Dbl(r"AMMONIA",r"AMMONIA",s).Value=Bulkres[5][s-2]; C1.Dbg(r"AMMONIA",r"WATER",s).Value=Bulkres[6][s-2]; C1.Dbl(r"AMMONIA",r"WATER",s).Value=Bulkres[7][s-2];
    C1.Dbg(r"WATER",r"AMMONIA",s).Value=Bulkres[8][s-2]; C1.Dbl(r"WATER",r"AMMONIA",s).Value=Bulkres[9][s-2]; C1.Dbg(r"WATER",r"WATER",s).Value=Bulkres[10][s-2]; C1.Dbl(r"WATER",r"WATER",s).Value=Bulkres[11][s-2];
    C1.Cpbg(s).Value=Bulkres[12][s-2]; C1.Cpbl(s).Value=Bulkres[13][s-2]; C1.kappabg(s).Value=Bulkres[14][s-2]; C1.kappabl(s).Value=Bulkres[15][s-2]; C1.mubg(s).Value=Bulkres[16][s-2]; C1.mubl(s).Value=Bulkres[17][s-2]; C1.sigmabl(s).Value=Bulkres[18][s-2];
    C1.Uspg(s).Value=Bulkres[19][s-2]; C1.Uspl(s).Value=Bulkres[20][s-2]; C1.MWg(s).Value=Bulkres[21][s-2]; C1.MWl(s).Value=Bulkres[22][s-2]; C1.Scg(s).Value=Bulkres[23][s-2]; C1.Scl(s).Value=Bulkres[24][s-2];  
    C1.Regc(s).Value=Bulkres[25][s-2]; C1.Relc(s).Value=Bulkres[26][s-2]; C1.Wel(s).Value=Bulkres[27][s-2]; C1.Frlc(s).Value=Bulkres[28][s-2]; C1.kbmg(s).Value=Bulkres[29][s-2]; C1.kbml(s).Value=Bulkres[30][s-2]; 
    C1.khg(s).Value=Bulkres[31][s-2]; C1.khl(s).Value=Bulkres[32][s-2]; C1.aef(s).Value=Bulkres[33][s-2]; C1.hbg(s).Value=Bulkres[34][s-2]; C1.hbl(s).Value=Bulkres[35][s-2]; 
    C1.cabl(r"AMMONIA",s).Value=Bulkres[36][s-2]; C1.cabl(r"WATER",s).Value=Bulkres[37][s-2]; C1.yba(r"AMMONIA",s).Value=Bulkres[38][s-2]; C1.yba(r"WATER",s).Value=Bulkres[39][s-2]; C1.ybd(r"AMMONIA",s).Value=Bulkres[40][s-2]; 
    C1.ybd(r"WATER",s).Value=Bulkres[41][s-2]; C1.xba(r"AMMONIA",s).Value=Bulkres[42][s-2]; C1.xba(r"WATER",s).Value=Bulkres[43][s-2]; C1.xbd(r"AMMONIA",s).Value=Bulkres[44][s-2]; C1.xbd(r"WATER",s).Value=Bulkres[45][s-2];
    C1.hga(s).Value=Bulkres[46][s-2]; C1.hla(s).Value=Bulkres[47][s-2]; C1.hgd(s).Value=Bulkres[48][s-2]; C1.hld(s).Value=Bulkres[49][s-2]; 
    C1.cala(r"AMMONIA",s).Value=Bulkres[50][s-2]; C1.cala(r"WATER",s).Value=Bulkres[51][s-2]; C1.cald(r"AMMONIA",s).Value=Bulkres[52][s-2]; C1.cald(r"WATER",s).Value=Bulkres[53][s-2]; 
    C1.ubg(s).Value=Bulkres[54][s-2]; C1.ubl(s).Value=Bulkres[55][s-2]; C1.Gammabl(s).Value=Bulkres[56][s-2]; C1.hpabg(s).Value=Bulkres[57][s-2]; C1.hpwbg(s).Value=Bulkres[58][s-2]; C1.hpabl(s).Value=Bulkres[59][s-2]; C1.hpwbl(s).Value=Bulkres[60][s-2];
    C1.Regp(s).Value=Bulkres[61][s-2]; C1.Frlp(s).Value=Bulkres[62][s-2]; C1.Hpr(s).Value=Bulkres[63][s-2]; C1.FSt(s).Value=Bulkres[64][s-2]; C1.CSt(s).Value=Bulkres[65][s-2]; C1.dPdry(s).Value=Bulkres[66][s-2]; C1.H(s).Value=Bulkres[67][s-2]; C1.dPirr(s).Value=Bulkres[68][s-2]; 
    C1.Nas(s).Value=Bulkres[69][s-2]; C1.Nts(s).Value=Bulkres[70][s-2]; C1.Es(s).Value=Bulkres[71][s-2]; 
    C1.yI(r"AMMONIA",s).Value=Bulkres[72][s-2]; C1.yI(r"WATER",s).Value=Bulkres[73][s-2]; C1.xI(r"AMMONIA",s).Value=Bulkres[74][s-2]; C1.xI(r"WATER",s).Value=Bulkres[75][s-2]; C1.TI(s).Value=Bulkres[76][s-2];
    C1.phiIg(r"AMMONIA",s).Value=Bulkres[77][s-2]; C1.phiIg(r"WATER",s).Value=Bulkres[78][s-2]; C1.phiIl(r"AMMONIA",s).Value=Bulkres[79][s-2]; C1.phiIl(r"WATER",s).Value=Bulkres[80][s-2];   
C1.hReflujo.Value=sheet[r"O17"].value/1000000; C1.hR_CF_out.Value=sheet[r"BX8"].value/1000000; C1.hE_CF_out.Value=sheet[r"H18"].value/1000000;
C1.Vap_s_2.F.Value=C1.Vs(2).Value; C1.Vap_s_2.T.Value=C1.Tsg(2).Value; C1.Vap_s_2.P.Value=C1.Ps(2).Value; C1.Vap_s_2.z(r"AMMONIA").Value=C1.ys(r"AMMONIA",2).Value; C1.Vap_s_2.z(r"WATER").Value=C1.ys(r"WATER",2).Value;
E3.Vap_s_2.F.Value=C1.Vs(2).Value; E3.Vap_s_2.T.Value=C1.Tsg(2).Value; E3.Vap_s_2.P.Value=C1.Ps(2).Value; E3.Vap_s_2.z(r"AMMONIA").Value=C1.ys(r"AMMONIA",2).Value; E3.Vap_s_2.z(r"WATER").Value=C1.ys(r"WATER",2).Value;
C1.Liq_s_ps1pps2m3.F.Value=C1.Ls(ps1+ps2-3).Value; C1.Liq_s_ps1pps2m3.T.Value=C1.Tsl(ps1+ps2-3).Value; C1.Liq_s_ps1pps2m3.P.Value=C1.Ps(ps1+ps2-3).Value; C1.Liq_s_ps1pps2m3.z(r"AMMONIA").Value=C1.xs(r"AMMONIA",ps1+ps2-3).Value; C1.Liq_s_ps1pps2m3.z(r"WATER").Value=C1.xs(r"WATER",ps1+ps2-3).Value;
Thermosiphon.Liq_s_ps1pps2m3.F.Value=C1.Ls(ps1+ps2-3).Value; Thermosiphon.Liq_s_ps1pps2m3.T.Value=C1.Tsl(ps1+ps2-3).Value; Thermosiphon.Liq_s_ps1pps2m3.P.Value=C1.Ps(ps1+ps2-3).Value; Thermosiphon.Liq_s_ps1pps2m3.z(r"AMMONIA").Value=C1.xs(r"AMMONIA",ps1+ps2-3).Value; Thermosiphon.Liq_s_ps1pps2m3.z(r"WATER").Value=C1.xs(r"WATER",ps1+ps2-3).Value;
# E-1
E1.Aext.Value=3.141593*E1.dext.Value*E1.L.Value; E1.Aint.Value=3.141593*E1.dint.Value*E1.L.Value;
E1.E_CF_out.T.Value=sheet[r"H15"].value; C1.E_CF_out.T.Value=sheet[r"H15"].value; E1.E_CF_out.P.Value=E1.E_CF_in.P.Value; C1.E_CF_out.P.Value=E1.E_CF_in.P.Value; 
E1.E_CF_out.F.Value=E1.E_CF_in.F.Value; C1.E_CF_out.F.Value=E1.E_CF_in.F.Value; E1.E_CF_out.z(r"AMMONIA").Value=E1.E_CF_in.z(r"AMMONIA").Value; C1.E_CF_out.z(r"AMMONIA").Value=E1.E_CF_in.z(r"AMMONIA").Value; 
E1.E_CF_out.z(r"WATER").Value=E1.E_CF_in.z(r"WATER").Value; C1.E_CF_out.z(r"WATER").Value=E1.E_CF_in.z(r"WATER").Value;
E1.E_HF_in.T.Value=sheet[r"F15"].value; Thermosiphon.E_HF_in.T.Value=sheet[r"F15"].value; E1.E_HF_in.P.Value=sheet[r"F16"].value; Thermosiphon.E_HF_in.P.Value=sheet[r"F16"].value; 
E1.E_HF_in.F.Value=sheet[r"F14"].value; Thermosiphon.E_HF_in.F.Value=sheet[r"F14"].value; E1.E_HF_in.z(r"AMMONIA").Value=sheet[r"F17"].value; Thermosiphon.E_HF_in.z(r"AMMONIA").Value=sheet[r"F17"].value; 
E1.E_HF_in.z(r"WATER").Value=1-sheet[r"F17"].value; Thermosiphon.E_HF_in.z(r"WATER").Value=1-sheet[r"F17"].value;
E1.E_HF_out.T.Value=sheet[r"F4"].value; E1.E_HF_out.P.Value=E1.E_HF_in.P.Value; E1.E_HF_out.F.Value=E1.E_HF_in.F.Value; 
E1.E_HF_out.z(r"AMMONIA").Value=E1.E_HF_in.z(r"AMMONIA").Value; E1.E_HF_out.z(r"WATER").Value=E1.E_HF_in.z(r"WATER").Value;
E1.hE_HF_in.Value=E1res[0][0]; E1.hE_HF_out.Value=E1res[1][0]; E1.hE_CF_in.Value=E1res[2][0]; E1.hE_CF_out.Value=E1res[3][0]; E1.dT1.Value=E1res[4][0]; E1.dT2.Value=E1res[5][0]; E1.dTln.Value=E1res[6][0];
E1.RF.Value=E1res[7][0]; E1.PF.Value=E1res[8][0]; E1.alphaF.Value=E1res[9][0]; E1.SF.Value=E1res[10][0]; E1.F.Value=E1res[11][0]; E1.MWint.Value=E1res[12][0]; E1.muint.Value=E1res[13][0]; E1.Cpint.Value=E1res[14][0];
E1.kappaint.Value=E1res[15][0]; E1.Re_int.Value=E1res[16][0]; E1.Pr_int.Value=E1res[17][0]; E1.Nu_int.Value=E1res[18][0]; E1.hint.Value=E1res[19][0]; E1.MWext.Value=E1res[20][0]; E1.muext.Value=E1res[21][0];
E1.Cpext.Value=E1res[22][0]; E1.kappaext.Value=E1res[23][0]; E1.Afc.Value=E1res[24][0]; E1.Re_ext.Value=E1res[25][0]; E1.Pr_ext.Value=E1res[26][0]; E1.a1.Value=E1res[27][0]; E1.a2.Value=E1res[28][0]; E1.aBD.Value=E1res[29][0];
E1.jH.Value=E1res[30][0]; E1.hext.Value=E1res[31][0]; E1.U.Value=E1res[32][0]; E1.rhoE_HF.Value=E1res[33][0]; E1.EHFq.Value=E1res[34][0];
# E-2
Thermosiphon.Liq_s_ps1pps2m2F.Value=sheet[r"BV19"].value; Thermosiphon.Liq_s_ps1pps2m2T.Value=sheet[r"BV20"].value; Thermosiphon.Liq_s_ps1pps2m2P.Value=sheet[r"BV21"].value; Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value=sheet[r"BV22"].value; Thermosiphon.Liq_s_ps1pps2m2z(r"WATER").Value=1-sheet[r"BV22"].value;
Thermosiphon.R_CF_out.F.Value=Thermosiphon.Liq_s_ps1pps2m2F.Value; Thermosiphon.R_CF_out.T.Value=sheet[r"BX5"].value; Thermosiphon.R_CF_out.P.Value=Thermosiphon.Liq_s_ps1pps2m2P.Value; Thermosiphon.R_CF_out.z(r"AMMONIA").Value=Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value; 
Thermosiphon.R_CF_out.z(r"WATER").Value=Thermosiphon.Liq_s_ps1pps2m2z(r"WATER").Value;
C1.R_CF_out.F.Value=Thermosiphon.Liq_s_ps1pps2m2F.Value; C1.R_CF_out.T.Value=sheet[r"BX5"].value; C1.R_CF_out.P.Value=Thermosiphon.Liq_s_ps1pps2m2P.Value; C1.R_CF_out.z(r"AMMONIA").Value=Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value; 
C1.R_CF_out.z(r"WATER").Value=Thermosiphon.Liq_s_ps1pps2m2z(r"WATER").Value;
Thermosiphon.hLiq_s_ps1pps2m3.Value=C1.hsl(ps1+ps2-3).Value; Thermosiphon.hE_HF_in.Value=E1.hE_HF_in.Value;
Thermosiphon.hR_CF_out.Value=sheet[r"S37"].value/1000000; Thermosiphon.hLiq_s_ps1pps2m2.Value=sheet[r"R37"].value/1000000;
Thermosiphon.rhoLiq_s_ps1pps2m2.Value=rhosumidero; Thermosiphon.MWLiq_s_ps1pps2m2.Value=MWsumidero;
# Corrientes de salida de E-3 y Divisor
E3.C_HF_out.T.Value=sheet[r"O14"].value; E3.C_HF_out.F.Value=E3.Vap_s_2.F.Value; E3.C_HF_out.P.Value=E3.Vap_s_2.P.Value; E3.C_HF_out.z(r"AMMONIA").Value=E3.Vap_s_2.z(r"AMMONIA").Value; E3.C_HF_out.z(r"WATER").Value=E3.Vap_s_2.z(r"WATER").Value; 
Divisor.C_HF_out.T.Value=sheet[r"O14"].value; Divisor.C_HF_out.F.Value=E3.Vap_s_2.F.Value; Divisor.C_HF_out.P.Value=E3.Vap_s_2.P.Value; Divisor.C_HF_out.z(r"AMMONIA").Value=E3.Vap_s_2.z(r"AMMONIA").Value; Divisor.C_HF_out.z(r"WATER").Value=E3.Vap_s_2.z(r"WATER").Value;
C1.Reflujo.T.Value=E3.C_HF_out.T.Value; C1.Reflujo.P.Value=E3.C_HF_out.P.Value; C1.Reflujo.z(r"AMMONIA").Value=E3.C_HF_out.z(r"AMMONIA").Value; C1.Reflujo.z(r"WATER").Value=E3.C_HF_out.z(r"WATER").Value;
Divisor.Reflujo.T.Value=E3.C_HF_out.T.Value; Divisor.Reflujo.P.Value=E3.C_HF_out.P.Value; Divisor.Reflujo.z(r"AMMONIA").Value=E3.C_HF_out.z(r"AMMONIA").Value; Divisor.Reflujo.z(r"WATER").Value=E3.C_HF_out.z(r"WATER").Value;
Divisor.Prod_Liq.T.Value=E3.C_HF_out.T.Value; Divisor.Prod_Liq.P.Value=E3.C_HF_out.P.Value; Divisor.Prod_Liq.z(r"AMMONIA").Value=E3.C_HF_out.z(r"AMMONIA").Value; Divisor.Prod_Liq.z(r"WATER").Value=E3.C_HF_out.z(r"WATER").Value; 
E3.C_CF_in.T.Value=30; E3.C_CF_in.P.Value=3.43233; E3.C_CF_in.z(r"AMMONIA").Value=0; E3.C_CF_in.z(r"WATER").Value=1; E3.C_CF_out.P.Value=3.43233; E3.C_CF_out.z(r"AMMONIA").Value=0; E3.C_CF_out.z(r"WATER").Value=1;
E3.C_CF_out.T.Value=E3res[0][0]; E3.C_CF_in.F.Value=E3res[1][0]; E3.C_CF_out.F.Value=E3res[1][0]; E3.hVap_s_2.Value=E3res[2][0]; E3.hC_HF_out.Value=E3res[3][0]; E3.hC_CF_in.Value=E3res[4][0]; E3.hC_CF_out.Value=E3res[5][0];
E3.MWC_CF.Value=E3res[6][0]; E3.CCFmt.Value=E3res[7][0]; E3.dT1.Value=E3res[8][0]; E3.dT2.Value=E3res[9][0]; E3.dTln.Value=E3res[10][0]; E3.RF.Value=E3res[11][0]; E3.PF.Value=E3res[12][0]; E3.alphaF.Value=E3res[13][0]; E3.SF.Value=E3res[14][0]; 
E3.F.Value=E3res[15][0]; Divisor.RR.Value=E3res[16][0]; E3.rhoC_CF.Value=E3res[17][0]; E3.CCFq.Value=E3res[18][0]; Divisor.rhoProd_Liq.Value=E3res[19][0]; Divisor.Prod_Liqq.Value=E3res[20][0]; 
# Q de los tres intercambiadores
E1.QE.Q.Value=sheet[r"E11"].value/1000000; Thermosiphon.QR.Q.Value=sheet[r"BX16"].value/1000000; E3.QC.Q.Value=sheet[r"N11"].value/1000000;
# Exportar resultados de Aspen Custom Modeler
try:
    Sim.Run(True); ACM.SaveDocumentAs(os.path.abspath(nombre_hoja_cal+r".dynf"),True);
    print(r"Aspen Custom Modeler generó resultados exitosamente"); 
except: # Cuando no genera resultados
    print(r"No genera resultados Aspen Custom Modeler exitosamente"); exit();
sheet=wb.sheets[r"Exportar_resultados_ACM"]; 
sheet[r"B1"].value=caso; sheet[r"B2"].value=ps1; sheet[r"B3"].value=ps2; sheet[r"B4"].value=flowmode1; sheet[r"B5"].value=flowmode2; sheet[r"B6"].value=simtype;
if simtype==0:
    sheet[r"B7"].value=r"'-"; sheet[r"B8"].value=r"'-"; sheet[r"B9"].value=r"'-"; sheet[r"B10"].value=r"'-"; 
else:
    sheet[r"B7"].value=pborde1; sheet[r"B8"].value=nborde1; sheet[r"B9"].value=pborde2; sheet[r"B10"].value=nborde2;
sheet[r"B11"].value=Divisor.RR.Value; sheet[r"B12"].value=Thermosiphon.R_CF_out.F.Value/Thermosiphon.Liq_s_ps1pps2m2F.Value;
sheet[r"B13"].value=Divisor.Prod_Liq.z(r"AMMONIA").Value*17.03052/(Divisor.Prod_Liq.z(r"AMMONIA").Value*17.03052+Divisor.Prod_Liq.z(r"WATER").Value*18.01528); 
sheet[r"B14"].value=E1.E_HF_out.z(r"AMMONIA").Value*17.03052/(E1.E_HF_out.z(r"AMMONIA").Value*17.03052+E1.E_HF_out.z(r"WATER").Value*18.01528);
# E-1
sheet[r"G21"].value=E1.F.Value; sheet[r"G22"].value=E1.hint.Value*3600; sheet[r"G23"].value=E1.hext.Value*3600; 
sheet[r"B31"].value=E1.E_CF_in.F.Value; sheet[r"C31"].value=E1.E_CF_out.F.Value; sheet[r"D31"].value=E1.E_HF_in.F.Value; sheet[r"E31"].value=E1.E_HF_out.F.Value;
sheet[r"F31"].value=E1.E_CF_in.z(r"AMMONIA").Value; sheet[r"G31"].value=E1.E_CF_out.z(r"AMMONIA").Value; sheet[r"H31"].value=E1.E_HF_in.z(r"AMMONIA").Value; sheet[r"I31"].value=E1.E_HF_out.z(r"AMMONIA").Value;
sheet[r"J31"].value=E1.E_CF_in.T.Value; sheet[r"K31"].value=E1.E_CF_out.T.Value; sheet[r"L31"].value=E1.E_HF_in.T.Value; sheet[r"M31"].value=E1.E_HF_out.T.Value; sheet[r"N31"].value=E1.QE.Q.Value*1000000;
sheet[r"O31"].value=E1.hE_CF_in.Value*1000000; sheet[r"P31"].value=E1.hE_CF_out.Value*1000000; sheet[r"Q31"].value=E1.hE_HF_in.Value*1000000; sheet[r"R31"].value=E1.hE_HF_out.Value*1000000;
sheet[r"S31"].value=E1.E_CF_in.P.Value; sheet[r"T31"].value=E1.E_CF_out.P.Value; sheet[r"U31"].value=E1.E_HF_in.P.Value; sheet[r"V31"].value=E1.E_HF_out.P.Value;
# E-3
sheet[r"P25"].value=E3.F.Value; 
sheet[r"B36"].value=1; sheet[r"C36"].value=10.2497; sheet[r"D36"].value=r"-"; sheet[r"E36"].value=E3.C_HF_out.F.Value; sheet[r"F36"].value=r"-"; sheet[r"G36"].value=Divisor.Prod_Liq.F.Value; 
sheet[r"H36"].value=r"-"; sheet[r"I36"].value=E3.C_HF_out.z(r"AMMONIA").Value; sheet[r"J36"].value=r"-"; sheet[r"K36"].value=Divisor.Prod_Liq.z(r"AMMONIA").Value; 
sheet[r"L36"].value=r"-"; sheet[r"M36"].value=E3.C_HF_out.T.Value; sheet[r"N36"].value=r"-"; sheet[r"O36"].value=Divisor.Prod_Liq.T.Value; sheet[r"P36"].value=-E3.QC.Q.Value*1000000; 
sheet[r"Q36"].value=r"-"; sheet[r"R36"].value=E3.hC_HF_out.Value*1000000; sheet[r"S36"].value=r"-"; sheet[r"T36"].value=E3.hC_HF_out.Value*1000000; 
sheet[r"U36"].value=r"-"; sheet[r"V36"].value=E3.C_HF_out.P.Value; sheet[r"W36"].value=r"-"; sheet[r"X36"].value=Divisor.Prod_Liq.P.Value;
sheet[r"Z36"].value=E3.C_CF_in.F.Value; sheet[r"AA36"].value=E3.C_CF_out.F.Value; sheet[r"AB36"].value=E3.C_CF_in.z(r"AMMONIA").Value; sheet[r"AC36"].value=E3.C_CF_out.z(r"AMMONIA").Value;
sheet[r"AD36"].value=E3.C_CF_in.T.Value; sheet[r"AE36"].value=E3.C_CF_out.T.Value; sheet[r"AF36"].value=E3.hC_CF_in.Value*1000000; sheet[r"AG36"].value=E3.hC_CF_out.Value*1000000;
sheet[r"AH36"].value=E3.C_CF_in.P.Value; sheet[r"AI36"].value=E3.C_CF_out.P.Value,
# E-2
sheet[r"BT27"].value=TT6-273.15; sheet[r"BT28"].value=TT7-273.15; sheet[r"BV27"].value=FIC1; sheet[r"BV28"].value=FIC1*rhoHO; sheet[r"BX25"].value=(0.45784*(TT6**2-TT7**2)+121.3161*(TT6-TT7))*rhoHO*FIC1; 
sheet[r"B37"].value=ps1+ps2-2; sheet[r"C37"].value=0; sheet[r"D37"].value=r"-"; sheet[r"E37"].value=Thermosiphon.Liq_s_ps1pps2m2F.Value+Thermosiphon.E_HF_in.F.Value; sheet[r"F37"].value=Thermosiphon.R_CF_out.F.Value; sheet[r"G37"].value=Thermosiphon.E_HF_in.F.Value; 
sheet[r"H37"].value=r"-"; sheet[r"I37"].value=Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value; sheet[r"J37"].value=Thermosiphon.R_CF_out.z(r"AMMONIA").Value; sheet[r"K37"].value=Thermosiphon.E_HF_in.z(r"AMMONIA").Value; 
sheet[r"L37"].value=r"-"; sheet[r"M37"].value=Thermosiphon.Liq_s_ps1pps2m2T.Value; sheet[r"N37"].value=Thermosiphon.R_CF_out.T.Value; sheet[r"O37"].value=Thermosiphon.E_HF_in.T.Value; sheet[r"P37"].value=Thermosiphon.QR.Q.Value*1000000; 
sheet[r"Q37"].value=r"-"; sheet[r"R37"].value=Thermosiphon.hLiq_s_ps1pps2m2.Value*1000000; sheet[r"S37"].value=Thermosiphon.hR_CF_out.Value*1000000; sheet[r"T37"].value=Thermosiphon.hE_HF_in.Value*1000000; 
sheet[r"U37"].value=r"-"; sheet[r"V37"].value=Thermosiphon.Liq_s_ps1pps2m2P.Value; sheet[r"W37"].value=Thermosiphon.R_CF_out.P.Value; sheet[r"X37"].value=Thermosiphon.E_HF_in.P.Value;
# C-1
sheet[r"X2"].value=C1.Atr.Value; sheet[r"AO2"].value=C1.Atr.Value; sheet[r"BC2"].value=C1.Atr.Value;
for s in range(2,ps1+ps2-2):
    fila=str(s+40); sheet[r"B"+fila].value=s;
    if s>=2 and s<=ps1-1:
        sheet[r"A"+fila].value=r"Rectificación";
    else:
        sheet[r"A"+fila].value=r"Agotamiento";
    if s==2:
        sheet[r"C"+fila].value=9.6416; sheet[r"D"+fila].value=9.6416-C1.Zs(s).Value;
    elif s==ps1:
        sheet[r"C"+fila].value=6.8706; sheet[r"D"+fila].value=6.8706-C1.Zs(s).Value;
    else:
        sheet[r"C"+fila].value=sheet[r"D"+str(s+39)].value; sheet[r"D"+fila].value=sheet[r"C"+fila].value-C1.Zs(s).Value;
    if s==ps1:
        sheet[r"F"+fila].value=C1.E_CF_out.F.Value; sheet[r"M"+fila].value=C1.E_CF_out.z(r"AMMONIA").Value; sheet[r"AF"+fila].value=C1.E_CF_out.T.Value; sheet[r"AT"+fila].value=C1.hE_CF_out.Value*1000000; sheet[r"AX"+fila].value=C1.E_CF_out.P.Value;
    else:
        sheet[r"F"+fila].value=r"-"; sheet[r"M"+fila].value=r"-"; sheet[r"AF"+fila].value=r"-"; sheet[r"AT"+fila].value=r"-"; sheet[r"AX"+fila].value=r"-";
    if s==ps1+ps2-3:
        sheet[r"E"+fila].value=C1.R_CF_out.F.Value; sheet[r"L"+fila].value=C1.R_CF_out.z(r"AMMONIA").Value; sheet[r"AE"+fila].value=C1.R_CF_out.T.Value; sheet[r"AS"+fila].value=C1.hR_CF_out.Value*1000000; sheet[r"AW"+fila].value=C1.R_CF_out.P.Value;
    else:
        sheet[r"E"+fila].value=r"-"; sheet[r"L"+fila].value=r"-"; sheet[r"AE"+fila].value=r"-"; sheet[r"AS"+fila].value=r"-"; sheet[r"AW"+fila].value=r"-";
    sheet[r"G"+fila].value=C1.Vs(s).Value; sheet[r"H"+fila].value=C1.Ls(s).Value; sheet[r"I"+fila].value=C1.Vb(s).Value; sheet[r"J"+fila].value=C1.Lb(s).Value; sheet[r"K"+fila].value=C1.aef(s).Value*C1.Atr.Value*C1.Zs(s).Value; 
    sheet[r"N"+fila].value=C1.ys(r"AMMONIA",s).Value; sheet[r"O"+fila].value=C1.yb(r"AMMONIA",s).Value; sheet[r"P"+fila].value=C1.yI(r"AMMONIA",s).Value; sheet[r"Q"+fila].value=C1.xI(r"AMMONIA",s).Value; sheet[r"R"+fila].value=C1.xb(r"AMMONIA",s).Value; sheet[r"S"+fila].value=C1.xs(r"AMMONIA",s).Value; 
    sheet[r"T"+fila].value=C1.kbmg(s).Value*3600; sheet[r"U"+fila].value=C1.kbml(s).Value*3600; sheet[r"V"+fila].value=C1.Nas(s).Value; sheet[r"W"+fila].value=C1.Nts(s).Value-C1.Nas(s).Value; sheet[r"X"+fila].value=C1.Nts(s).Value; 
    sheet[r"Y"+fila].value=C1.rhobg(s).Value*C1.kbmg(s).Value*C1.aef(s).Value*C1.Zs(s).Value*C1.Atr.Value*(C1.yb(r"AMMONIA",s).Value-C1.yI(r"AMMONIA",s).Value)*3600; 
    sheet[r"Z"+fila].value=(C1.Nas(s).Value-C1.Nts(s).Value*C1.yb(r"AMMONIA",s).Value)/sheet[r"Y"+fila].value;
    sheet[r"AA"+fila].value=C1.Nts(s).Value*C1.yb(r"AMMONIA",s).Value; 
    sheet[r"AB"+fila].value=C1.Gammabl(s).Value*C1.rhobl(s).Value*C1.kbml(s).Value*C1.aef(s).Value*C1.Zs(s).Value*C1.Atr.Value*(C1.xI(r"AMMONIA",s).Value-C1.xb(r"AMMONIA",s).Value)*3600; 
    sheet[r"AC"+fila].value=C1.Gammabl(s).Value; 
    sheet[r"AD"+fila].value=C1.Nts(s).Value*C1.xb(r"AMMONIA",s).Value;
    sheet[r"AG"+fila].value=C1.Tsg(s).Value; sheet[r"AH"+fila].value=C1.Tbg(s).Value; sheet[r"AI"+fila].value=C1.TI(s).Value; sheet[r"AJ"+fila].value=C1.Tbl(s).Value; sheet[r"AK"+fila].value=C1.Tsl(s).Value; 
    sheet[r"AL"+fila].value=C1.khg(s).Value*3600; sheet[r"AM"+fila].value=C1.khl(s).Value*3600; sheet[r"AN"+fila].value=C1.Es(s).Value*1000000; 
    sheet[r"AO"+fila].value=C1.khg(s).Value*C1.aef(s).Value*C1.Zs(s).Value*C1.Atr.Value*(C1.Tbg(s).Value-C1.TI(s).Value)*3600; 
    sheet[r"AP"+fila].value=(C1.Nas(s).Value*C1.hpabg(s).Value+(C1.Nts(s).Value-C1.Nas(s).Value)*C1.hpwbg(s).Value)*1000000; 
    sheet[r"AQ"+fila].value=C1.khl(s).Value*C1.aef(s).Value*C1.Zs(s).Value*C1.Atr.Value*(C1.TI(s).Value-C1.Tbl(s).Value)*3600; 
    sheet[r"AR"+fila].value=(C1.Nas(s).Value*C1.hpabl(s).Value+(C1.Nts(s).Value-C1.Nas(s).Value)*C1.hpwbl(s).Value)*1000000;
    sheet[r"AU"+fila].value=C1.hsg(s).Value*1000000; sheet[r"AV"+fila].value=C1.hsl(s).Value*1000000; sheet[r"AY"+fila].value=C1.Ps(s).Value;      
# Tranferencia de masa y energía por cada zona
sheet[r"BC48"].value=sheet.range(r"V42:V"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD48"].value=sheet.range(r"V"+str(40+ps1)+r":V"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC49"].value=sheet.range(r"W42:W"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD49"].value=sheet.range(r"W"+str(40+ps1)+r":W"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC50"].value=sheet.range(r"X42:X"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD50"].value=sheet.range(r"X"+str(40+ps1)+r":X"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC51"].value=sheet.range(r"Y42:Y"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD51"].value=sheet.range(r"Y"+str(40+ps1)+r":Y"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC52"].value=sheet.range(r"AA42:AA"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD52"].value=sheet.range(r"AA"+str(40+ps1)+r":AA"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC53"].value=sheet.range(r"AB42:AB"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD53"].value=sheet.range(r"AB"+str(40+ps1)+r":AB"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC54"].value=sheet.range(r"AD42:AD"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD54"].value=sheet.range(r"AD"+str(40+ps1)+r":AD"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC55"].value=sheet.range(r"AN42:AN"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD55"].value=sheet.range(r"AN"+str(40+ps1)+r":AN"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC56"].value=sheet.range(r"AO42:AO"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD56"].value=sheet.range(r"AO"+str(40+ps1)+r":AO"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC57"].value=sheet.range(r"AP42:AP"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD57"].value=sheet.range(r"AP"+str(40+ps1)+r":AP"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC58"].value=sheet.range(r"AQ42:AQ"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD58"].value=sheet.range(r"AQ"+str(40+ps1)+r":AQ"+str(40+ps1+ps2-3)).options(np.array).value.sum();
sheet[r"BC59"].value=sheet.range(r"AR42:AR"+str(40+ps1-1)).options(np.array).value.sum(); sheet[r"BD59"].value=sheet.range(r"AR"+str(40+ps1)+r":AR"+str(40+ps1+ps2-3)).options(np.array).value.sum();
# Resumir resultados de temperatura y generar gráfica
# Arreglos de ubicación y temperatura
if ps1!=3:
    zR_top=sheet.range(r"C42:C"+str(40+ps1-1)).options(np.array).value; zR_lower=sheet.range(r"D42:D"+str(40+ps1-1)).options(np.array).value;
    TgR=sheet.range(r"AH42:AH"+str(40+ps1-1)).options(np.array).value; TlR=sheet.range(r"AJ42:AJ"+str(40+ps1-1)).options(np.array).value;
    yR=sheet.range(r"O42:O"+str(40+ps1-1)).options(np.array).value; xR=sheet.range(r"R42:R"+str(40+ps1-1)).options(np.array).value;
else:
    zR_top=[sheet.range(r"C42:C"+str(40+ps1-1)).options(np.array).value]; zR_lower=[sheet.range(r"D42:D"+str(40+ps1-1)).options(np.array).value];
    TgR=[sheet.range(r"AH42:AH"+str(40+ps1-1)).options(np.array).value]; TlR=[sheet.range(r"AJ42:AJ"+str(40+ps1-1)).options(np.array).value];
    yR=[sheet.range(r"O42:O"+str(40+ps1-1)).options(np.array).value]; xR=[sheet.range(r"R42:R"+str(40+ps1-1)).options(np.array).value];
if ps2!=3:            
    zA_top=sheet.range(r"C"+str(40+ps1)+r":C"+str(40+ps1+ps2-3)).options(np.array).value; zA_lower=sheet.range(r"D"+str(40+ps1)+r":D"+str(40+ps1+ps2-3)).options(np.array).value;
    TgA=sheet.range(r"AH"+str(40+ps1)+r":AH"+str(40+ps1+ps2-3)).options(np.array).value; TlA=sheet.range(r"AJ"+str(40+ps1)+r":AJ"+str(40+ps1+ps2-3)).options(np.array).value;
    yA=sheet.range(r"O"+str(40+ps1)+r":O"+str(40+ps1+ps2-3)).options(np.array).value; xA=sheet.range(r"R"+str(40+ps1)+r":R"+str(40+ps1+ps2-3)).options(np.array).value;
else:
    zA_top=[sheet.range(r"C"+str(40+ps1)+r":C"+str(40+ps1+ps2-3)).options(np.array).value]; zA_lower=[sheet.range(r"D"+str(40+ps1)+r":D"+str(40+ps1+ps2-3)).options(np.array).value];
    TgA=[sheet.range(r"AH"+str(40+ps1)+r":AH"+str(40+ps1+ps2-3)).options(np.array).value]; TlA=[sheet.range(r"AJ"+str(40+ps1)+r":AJ"+str(40+ps1+ps2-3)).options(np.array).value];
    yA=[sheet.range(r"O"+str(40+ps1)+r":O"+str(40+ps1+ps2-3)).options(np.array).value]; xA=[sheet.range(r"R"+str(40+ps1)+r":R"+str(40+ps1+ps2-3)).options(np.array).value];
TgCond=sheet[r"AG42"].value; TlReb=sheet[r"M37"].value; 
yCond=sheet[r"N42"].value; xReb=sheet[r"K37"].value;
# Etapa y ubicación de cada TT
indeT2=np.argmin(np.abs(np.array(zA_top)-3.9246)); indeT3=np.argmin(np.abs(np.array(zA_top)-5.5946)); indeT4=np.argmin(np.abs(np.array(zR_top)-8.7696)); 
sheet[r"BE41"].value=ps1+ps2-2; sheet[r"BF41"].value=10.2497;
sheet[r"BE42"].value=indeT2+ps1; sheet[r"BF42"].value=8.7696;
sheet[r"BE43"].value=indeT3+ps1; sheet[r"BF43"].value=5.5946;
sheet[r"BE44"].value=indeT4+2; sheet[r"BF44"].value=3.9246;
sheet[r"BE45"].value=1; sheet[r"BF45"].value=0;
# Temperaturas reales por TT
sheet[r"BB41"].value=datos[r"TT-1"][ind]; sheet[r"BB42"].value=datos[r"TT-2"][ind]; sheet[r"BB43"].value=datos[r"TT-3"][ind]; sheet[r"BB44"].value=datos[r"TT-4"][ind]; sheet[r"BB45"].value=datos[r"TT-5"][ind];
# Temperaturas de simulación en la ubicación de TT
sheet[r"BC41"].value=r"-"; sheet[r"BD41"].value=TlReb;
sheet[r"BC42"].value=TgA[indeT2]; sheet[r"BD42"].value=TlA[indeT2];
sheet[r"BC43"].value=TgA[indeT3]; sheet[r"BD43"].value=TlA[indeT3];
sheet[r"BC44"].value=TgR[indeT4]; sheet[r"BD44"].value=TlR[indeT4];
sheet[r"BC45"].value=TgCond; sheet[r"BD45"].value=r"-";
# Gráficas
figtodoT=plt.figure(figsize=(6,9)); axtodoT=figtodoT.gca(); axtodoT.set_xlabel(r"$T$ $[°C]$"); axtodoT.set_ylabel(r"$z$ $[m]$"); axtodoT.grid();
figtodoxy=plt.figure(figsize=(6,9)); axtodoxy=figtodoxy.gca(); axtodoxy.set_xlabel(r"$\overline{x}_a/\overline{y}_a$"); axtodoxy.set_ylabel(r"$z$ $[m]$"); axtodoxy.grid();
figRT=plt.figure(figsize=(6,9)); axRT=figRT.gca(); axRT.set_xlabel(r"$T$ $[°C]$"); axRT.set_ylabel(r"$z$ $[m]$"); axRT.grid();
figAT=plt.figure(figsize=(6,9)); axAT=figAT.gca(); axAT.set_xlabel(r"$T$ $[°C]$"); axAT.set_ylabel(r"$z$ $[m]$"); axAT.grid();
figRxy=plt.figure(figsize=(6,9)); axRxy=figRxy.gca(); axRxy.set_xlabel(r"$\overline{x}_a/\overline{y}_a$"); axRxy.set_ylabel(r"$z$ $[m]$"); axRxy.grid();
figAxy=plt.figure(figsize=(6,9)); axAxy=figAxy.gca(); axAxy.set_xlabel(r"$\overline{x}_a/\overline{y}_a$"); axAxy.set_ylabel(r"$z$ $[m]$"); axAxy.grid();
axtodoT.set_title(r"C-1: Perfil de temperaturas",fontweight=r"bold"); axRT.set_title(r"Rectificación: Perfil de temperaturas",fontweight=r"bold"); axAT.set_title(r"Agotamiento: Perfil de temperaturas",fontweight=r"bold");
axtodoxy.set_title(r"C-1: Perfil de composiciones",fontweight=r"bold"); axRxy.set_title(r"Rectificación: Perfil de composiciones",fontweight=r"bold"); axAxy.set_title(r"Rectificación: Perfil de composiciones",fontweight=r"bold");
# Rectificación
for s in range(ps1-2):
    if s!=0:
        axtodoT.plot([TgR[s],TgR[s]],[zR_top[s],zR_lower[s]],r"-r"); axRT.plot([TgR[s],TgR[s]],[zR_top[s],zR_lower[s]],r"-r"); 
        axtodoT.plot([TlR[s],TlR[s]],[zR_top[s],zR_lower[s]],r"-b"); axRT.plot([TlR[s],TlR[s]],[zR_top[s],zR_lower[s]],r"-b"); 
    else:
        axtodoT.plot([TgR[s],TgR[s]],[zR_top[s],zR_lower[s]],r"-r",label=r"Fase vapor en etapa"); axRT.plot([TgR[s],TgR[s]],[zR_top[s],zR_lower[s]],r"-r",label=r"Fase vapor en etapa"); 
        axtodoT.plot([TlR[s],TlR[s]],[zR_top[s],zR_lower[s]],r"-b",label=r"Fase líquida en etapa"); axRT.plot([TlR[s],TlR[s]],[zR_top[s],zR_lower[s]],r"-b",label=r"Fase líquida en etapa"); 
    axtodoT.plot([TlR[s],TgR[s]],[zR_top[s],zR_top[s]],r"-k"); axRT.plot([TlR[s],TgR[s]],[zR_top[s],zR_top[s]],r"-k");
    axtodoT.plot([TlR[s],TgR[s]],[zR_lower[s],zR_lower[s]],r"-k"); axRT.plot([TlR[s],TgR[s]],[zR_lower[s],zR_lower[s]],r"-k");
    axtodoT.fill([TgR[s],TgR[s],TlR[s],TlR[s]],[zR_top[s],zR_lower[s],zR_lower[s],zR_top[s]],r"plum"); axRT.fill([TgR[s],TgR[s],TlR[s],TlR[s]],[zR_top[s],zR_lower[s],zR_lower[s],zR_top[s]],r"plum");
    if s!=0:
        axtodoxy.plot([yR[s],yR[s]],[zR_top[s],zR_lower[s]],r"-r"); axRxy.plot([yR[s],yR[s]],[zR_top[s],zR_lower[s]],r"-r"); 
        axtodoxy.plot([xR[s],xR[s]],[zR_top[s],zR_lower[s]],r"-b"); axRxy.plot([xR[s],xR[s]],[zR_top[s],zR_lower[s]],r"-b");
    else:
        axtodoxy.plot([yR[s],yR[s]],[zR_top[s],zR_lower[s]],r"-r",label=r"Fase vapor en etapa"); axRxy.plot([yR[s],yR[s]],[zR_top[s],zR_lower[s]],r"-r",label=r"Fase vapor en etapa"); 
        axtodoxy.plot([xR[s],xR[s]],[zR_top[s],zR_lower[s]],r"-b",label=r"Fase líquida en etapa"); axRxy.plot([xR[s],xR[s]],[zR_top[s],zR_lower[s]],r"-b",label=r"Fase líquida en etapa");
    axtodoxy.plot([xR[s],yR[s]],[zR_top[s],zR_top[s]],r"-k"); axRxy.plot([xR[s],yR[s]],[zR_top[s],zR_top[s]],r"-k");
    axtodoxy.plot([xR[s],yR[s]],[zR_lower[s],zR_lower[s]],r"-k"); axRxy.plot([xR[s],yR[s]],[zR_lower[s],zR_lower[s]],r"-k");
    axtodoxy.fill([yR[s],yR[s],xR[s],xR[s]],[zR_top[s],zR_lower[s],zR_lower[s],zR_top[s]],r"plum"); axRxy.fill([yR[s],yR[s],xR[s],xR[s]],[zR_top[s],zR_lower[s],zR_lower[s],zR_top[s]],r"plum");
axtodoT.plot(TgCond,10.2497,r"or",label=r"Vapor al condensador"); axRT.plot(TgCond,10.2497,r"or",label=r"Vapor al condensador"); axtodoxy.plot(yCond,10.2497,r"or",label=r"Vapor al condensador"); axRxy.plot(yCond,10.2497,r"or",label=r"Vapor al condensador");
axtodoT.plot(datos[r"TT-5"][ind],10.2497,r"^g"); axRT.plot(datos[r"TT-5"][ind],10.2497,r"^g",label=r"TT real"); axtodoT.plot(datos[r"TT-4"][ind],8.7696,r"^g"); axRT.plot(datos[r"TT-4"][ind],8.7696,r"^g");
# Agotamiento
for s in range(ps2-2):
    axtodoT.plot([TgA[s],TgA[s]],[zA_top[s],zA_lower[s]],r"-r"); axtodoT.plot([TlA[s],TlA[s]],[zA_top[s],zA_lower[s]],r"-b"); 
    if s!=0:
        axAT.plot([TgA[s],TgA[s]],[zA_top[s],zA_lower[s]],r"-r"); axAT.plot([TlA[s],TlA[s]],[zA_top[s],zA_lower[s]],r"-b"); 
    else:
        axAT.plot([TgA[s],TgA[s]],[zA_top[s],zA_lower[s]],r"-r",label=r"Fase vapor en etapa"); axAT.plot([TlA[s],TlA[s]],[zA_top[s],zA_lower[s]],r"-b",label=r"Fase líquida en etapa"); 
    axtodoT.plot([TlA[s],TgA[s]],[zA_top[s],zA_top[s]],r"-k"); axAT.plot([TlA[s],TgA[s]],[zA_top[s],zA_top[s]],r"-k");
    axtodoT.plot([TlA[s],TgA[s]],[zA_lower[s],zA_lower[s]],r"-k"); axAT.plot([TlA[s],TgA[s]],[zA_lower[s],zA_lower[s]],r"-k");
    axtodoT.fill([TgA[s],TgA[s],TlA[s],TlA[s]],[zA_top[s],zA_lower[s],zA_lower[s],zA_top[s]],r"plum"); axAT.fill([TgA[s],TgA[s],TlA[s],TlA[s]],[zA_top[s],zA_lower[s],zA_lower[s],zA_top[s]],r"plum");
    axtodoxy.plot([yA[s],yA[s]],[zA_top[s],zA_lower[s]],r"-r"); axtodoxy.plot([xA[s],xA[s]],[zA_top[s],zA_lower[s]],r"-b"); 
    if s!=0:
        axAxy.plot([yA[s],yA[s]],[zA_top[s],zA_lower[s]],r"-r"); axAxy.plot([xA[s],xA[s]],[zA_top[s],zA_lower[s]],r"-b");
    else:
        axAxy.plot([yA[s],yA[s]],[zA_top[s],zA_lower[s]],r"-r",label=r"Fase vapor en etapa"); axAxy.plot([xA[s],xA[s]],[zA_top[s],zA_lower[s]],r"-b",label=r"Fase líquida en etapa");
    axtodoxy.plot([xA[s],yA[s]],[zA_top[s],zA_top[s]],r"-k"); axAxy.plot([xA[s],yA[s]],[zA_top[s],zA_top[s]],r"-k");
    axtodoxy.plot([xA[s],yA[s]],[zA_lower[s],zA_lower[s]],r"-k"); axAxy.plot([xA[s],yA[s]],[zA_lower[s],zA_lower[s]],r"-k");
    axtodoxy.fill([yA[s],yA[s],xA[s],xA[s]],[zA_top[s],zA_lower[s],zA_lower[s],zA_top[s]],r"plum"); axAxy.fill([yA[s],yA[s],xA[s],xA[s]],[zA_top[s],zA_lower[s],zA_lower[s],zA_top[s]],r"plum");
axtodoT.plot(TlReb,0,r"ob",label=r"Líquido al rehervidor"); axAT.plot(TlReb,0,r"ob",label=r"Líquido al rehervidor"); axtodoxy.plot(xReb,0,r"ob",label=r"Líquido al rehervidor"); axAxy.plot(xReb,0,r"ob",label=r"Líquido al rehervidor");
axtodoT.plot(datos[r"TT-1"][ind],0,r"^g",label=r"TT Real"); axAT.plot(datos[r"TT-1"][ind],0,r"^g",label=r"TT Real"); axtodoT.plot(datos[r"TT-2"][ind],3.9246,r"^g"); axAT.plot(datos[r"TT-2"][ind],3.9246,r"^g");
axtodoT.plot(datos[r"TT-3"][ind],5.5946,r"^g"); axAT.plot(datos[r"TT-3"][ind],5.5946,r"^g");
axtodoT.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0); axtodoxy.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0); axRT.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0); 
axAT.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0); axRxy.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0); axAxy.legend(bbox_to_anchor=(1.05, 0.5),loc=r"center left",borderaxespad=0);
figtodoT.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68); figRT.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68); figAT.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68); 
figtodoxy.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68); figRxy.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68); figAxy.subplots_adjust(top=0.95,bottom=0.11,left=0.11,right=0.68);
fila=63; espacio=44;
sheet.pictures.add(figtodoT,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); fila=fila+espacio;
sheet.pictures.add(figRT,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); fila=fila+espacio;
sheet.pictures.add(figAT,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); fila=fila+espacio;
sheet.pictures.add(figtodoxy,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); fila=fila+espacio;
sheet.pictures.add(figRxy,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); fila=fila+espacio;
sheet.pictures.add(figAxy,left=sheet.range(r"BA"+str(fila)).left,top=sheet.range(r"BA"+str(fila)).top); 
# Resultado de válvulas
sheet[r"K19"].value=datos[r"LV-1"][ind]/100; sheet[r"T25"].value=1-datos[r"PV-2"][ind]/100;
sheet[r"K20"].value=E1.EHFq.Value; sheet[r"T26"].value=E3.CCFq.Value; ACM.quit();
wb.save(); wb.close(); print(r"Exportación de resultados de Aspen Custom Modeler exitosa"); print(r"Guardado de Excel exitoso");