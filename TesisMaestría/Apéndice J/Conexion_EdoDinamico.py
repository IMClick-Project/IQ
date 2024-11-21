# Paqueterí­as y funciones
import os; import win32com.client as win32;  # Para conectar aplicaciones 
import numpy as np; # Para trabajar arreglos
import matplotlib.pyplot as plt; # Para graficar
import warnings; # Evitar avisos de advertencias DeprecationWarning
warnings.filterwarnings(r"ignore",category=DeprecationWarning);
plt.close(r"all"); # Cerrar todas las figuras anteriores
# Casos estacionarios
CasoEst=[[r"Caso1-MIXED-0-16.dynf",r"Caso1-MIXED-1-16.dynf"],
         [r"Caso33-MIXED-0-19.dynf",r"Caso33-MIXED-1-19.dynf"],
         [r"Caso36-MIXED-0-17.dynf",r"Caso36-MIXED-1-17.dynf"]]; 
vpLV1=[14.2857,14.8148,11.0645]; # [%] Apertura de LV-1 para casos 1, 33 y 36
vpPV2=[19.6599,24.0774,30.8772]; # [%] Apertura de PV-2 para casos 1, 33 y 36
TT6=[224.8002,230.0281,222.0683]; # [°C] Medición de TT-6 para casos 1, 33 y 3. TT-7 se calculará respecto al QR del estado estacionario, ya que se comprobó que QR en estado estacionario es similar al calor sensible del aceite térmico, por lo que TT-7 resultante será muy cercano a la medición
FIC1=[291.6980604,289.8264014,292.5952834]; # [kmol/h] Medición de FIC-1 para casos 1, 33 y 36
P_R_HF=7.2569; # [bar] Presión del aceite térmico
# Casos dinámicos: Pruebas en estado estacionario 
print(r"Pruebas en estado estacionario");
for caso in range(3):
    for simtype in range(2):
        print(CasoEst[caso][simtype]);
        # Guardar parametros que determinan el estado completo de cada etapa en C-1
        print(r"Guardar estado estacionario:");
        print("C-1");
        ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(CasoEst[caso][simtype])); Sim=ACM.Simulation; C1=Sim.Flowsheet.Blocks(r"C-1");
        ps1=C1.ps1.Value; ps2=C1.ps2.Value; flowmode1=C1.flowmode1.Value; flowmode2=C1.flowmode2.Value; C1par=np.zeros((19,ps1+ps2-4)); C1res=np.zeros((87,ps1+ps2-4));
        for i in range(2,ps1+ps2-2):
            C1par[0][i-2]=C1.Vs(i).Value; C1par[1][i-2]=C1.Ls(i).Value; C1par[2][i-2]=C1.Tsg(i).Value; C1par[3][i-2]=C1.Tsl(i).Value; C1par[4][i-2]=C1.Ps(i).Value; 
            C1par[5][i-2]=C1.ys(r"AMMONIA",i).Value; C1par[6][i-2]=C1.ys(r"WATER",i).Value; C1par[7][i-2]=C1.xs(r"AMMONIA",i).Value; C1par[8][i-2]=C1.xs(r"WATER",i).Value;
            C1par[9][i-2]=C1.Vb(i).Value; C1par[10][i-2]=C1.Lb(i).Value; C1par[11][i-2]=C1.Tbg(i).Value; C1par[12][i-2]=C1.Tbl(i).Value; C1par[13][i-2]=C1.Pb(i).Value; 
            C1par[14][i-2]=C1.yb(r"AMMONIA",i).Value; C1par[15][i-2]=C1.yb(r"WATER",i).Value; C1par[16][i-2]=C1.xb(r"AMMONIA",i).Value; C1par[17][i-2]=C1.xb(r"WATER",i).Value; C1par[18][i-2]=C1.Zs(i).Value;
            C1res[0][i-2]=C1.hsg(i).Value; C1res[1][i-2]=C1.hsl(i).Value; C1res[2][i-2]=C1.rhobg(i).Value; C1res[3][i-2]=C1.rhobl(i).Value;
            C1res[4][i-2]=C1.Dbg(r"AMMONIA",r"AMMONIA",i).Value; C1res[5][i-2]=C1.Dbg(r"AMMONIA",r"WATER",i).Value; C1res[6][i-2]=C1.Dbg(r"WATER",r"AMMONIA",i).Value; C1res[7][i-2]=C1.Dbg(r"WATER",r"WATER",i).Value;
            C1res[8][i-2]=C1.Dbl(r"AMMONIA",r"AMMONIA",i).Value; C1res[9][i-2]=C1.Dbl(r"AMMONIA",r"WATER",i).Value; C1res[10][i-2]=C1.Dbl(r"WATER",r"AMMONIA",i).Value; C1res[11][i-2]=C1.Dbl(r"WATER",r"WATER",i).Value;
            C1res[12][i-2]=C1.Cpbg(i).Value; C1res[13][i-2]=C1.Cpbl(i).Value; C1res[14][i-2]=C1.kappabg(i).Value; C1res[15][i-2]=C1.kappabl(i).Value; C1res[16][i-2]=C1.mubg(i).Value; C1res[17][i-2]=C1.mubl(i).Value;
            C1res[18][i-2]=C1.sigmabl(i).Value; C1res[19][i-2]=C1.Uspg(i).Value; C1res[20][i-2]=C1.Uspl(i).Value; C1res[21][i-2]=C1.MWg(i).Value; C1res[22][i-2]=C1.MWl(i).Value; C1res[23][i-2]=C1.Scg(i).Value; 
            C1res[24][i-2]=C1.Scl(i).Value; C1res[25][i-2]=C1.Regc(i).Value; C1res[26][i-2]=C1.Relc(i).Value; C1res[27][i-2]=C1.Wel(i).Value; C1res[28][i-2]=C1.Frlc(i).Value; C1res[29][i-2]=C1.kbmg(i).Value;
            C1res[30][i-2]=C1.kbml(i).Value; C1res[31][i-2]=C1.khg(i).Value; C1res[32][i-2]=C1.khl(i).Value; C1res[33][i-2]=C1.aef(i).Value; C1res[34][i-2]=C1.hbg(i).Value; C1res[35][i-2]=C1.hbl(i).Value; 
            C1res[36][i-2]=C1.cabl(r"AMMONIA",i).Value; C1res[37][i-2]=C1.cabl(r"WATER",i).Value; C1res[38][i-2]=C1.yba(r"AMMONIA",i).Value; C1res[39][i-2]=C1.yba(r"WATER",i).Value; 
            C1res[40][i-2]=C1.xba(r"AMMONIA",i).Value; C1res[41][i-2]=C1.xba(r"WATER",i).Value; C1res[42][i-2]=C1.ybd(r"AMMONIA",i).Value; C1res[43][i-2]=C1.ybd(r"WATER",i).Value; 
            C1res[44][i-2]=C1.xbd(r"AMMONIA",i).Value; C1res[45][i-2]=C1.xbd(r"WATER",i).Value; C1res[46][i-2]=C1.hga(i).Value; C1res[47][i-2]=C1.hla(i).Value; C1res[48][i-2]=C1.hgd(i).Value; C1res[49][i-2]=C1.hld(i).Value;
            C1res[50][i-2]=C1.cala(r"AMMONIA",i).Value; C1res[51][i-2]=C1.cala(r"WATER",i).Value; C1res[52][i-2]=C1.cald(r"AMMONIA",i).Value; C1res[53][i-2]=C1.cald(r"WATER",i).Value; C1res[54][i-2]=C1.ubg(i).Value;
            C1res[55][i-2]=C1.ubl(i).Value; C1res[56][i-2]=C1.Gammabl(i).Value; C1res[57][i-2]=C1.hpabg(i).Value; C1res[58][i-2]=C1.hpwbg(i).Value; C1res[59][i-2]=C1.hpabl(i).Value; C1res[60][i-2]=C1.hpwbl(i).Value;
            C1res[61][i-2]=C1.Regp(i).Value; C1res[62][i-2]=C1.Frlp(i).Value; C1res[63][i-2]=C1.Hpr(i).Value; C1res[64][i-2]=C1.FSt(i).Value; C1res[65][i-2]=C1.CSt(i).Value; C1res[66][i-2]=C1.dPdry(i).Value; C1res[67][i-2]=C1.H(i).Value;
            C1res[68][i-2]=C1.dPirr(i).Value; C1res[69][i-2]=C1.Nas(i).Value; C1res[70][i-2]=C1.Nts(i).Value; C1res[71][i-2]=C1.Es(i).Value; C1res[72][i-2]=C1.TI(i).Value; C1res[73][i-2]=C1.yI(r"AMMONIA",i).Value; C1res[74][i-2]=C1.yI(r"WATER",i).Value;
            C1res[75][i-2]=C1.xI(r"AMMONIA",i).Value; C1res[76][i-2]=C1.xI(r"WATER",i).Value; C1res[77][i-2]=C1.phiIg(r"AMMONIA",i).Value; C1res[78][i-2]=C1.phiIg(r"WATER",i).Value; 
            C1res[79][i-2]=C1.phiIl(r"AMMONIA",i).Value; C1res[80][i-2]=C1.phiIl(r"WATER",i).Value; 
        hReflujo=C1.hReflujo.Value; hR_CF_out=C1.hR_CF_out.Value; hE_CF_out=C1.hE_CF_out.Value; 
        Vap_s_2F=C1.Vap_s_2.F.Value; Vap_s_2T=C1.Vap_s_2.T.Value; Vap_s_2P=C1.Vap_s_2.P.Value; Vap_s_2za=C1.Vap_s_2.z(r"AMMONIA").Value; Vap_s_2zw=C1.Vap_s_2.z(r"WATER").Value;
        ReflujoF=C1.Reflujo.F.Value; ReflujoT=C1.Reflujo.T.Value; ReflujoP=C1.Reflujo.P.Value; Reflujoza=C1.Reflujo.z(r"AMMONIA").Value; Reflujozw=C1.Reflujo.z(r"WATER").Value;
        R_CF_outF=C1.R_CF_out.F.Value; R_CF_outT=C1.R_CF_out.T.Value; R_CF_outP=C1.R_CF_out.P.Value; R_CF_outza=C1.R_CF_out.z(r"AMMONIA").Value; R_CF_outzw=C1.R_CF_out.z(r"WATER").Value;
        Liq_s_ps1pps2m3F=C1.Liq_s_ps1pps2m3.F.Value; Liq_s_ps1pps2m3T=C1.Liq_s_ps1pps2m3.T.Value; Liq_s_ps1pps2m3P=C1.Liq_s_ps1pps2m3.P.Value; Liq_s_ps1pps2m3za=C1.Liq_s_ps1pps2m3.z(r"AMMONIA").Value; Liq_s_ps1pps2m3zw=C1.Liq_s_ps1pps2m3.z(r"WATER").Value;
        E_CF_outF=C1.E_CF_out.F.Value; E_CF_outT=C1.E_CF_out.T.Value; E_CF_outP=C1.E_CF_out.P.Value; E_CF_outza=C1.E_CF_out.z(r"AMMONIA").Value; E_CF_outzw=C1.E_CF_out.z(r"WATER").Value; 
        # Guardar datos para E-1
        print("E-1");
        E1=Sim.Flowsheet.Blocks(r"E-1"); E1Est=np.zeros((30,1)); E1Din=np.zeros((20,1));
        hE_HF_in=E1.hE_HF_in.Value; hE_HF_out=E1.hE_HF_out.Value; hE_CF_in=E1.hE_CF_in.Value; 
        E_HF_inF=E1.E_HF_in.F.Value; E_HF_inT=E1.E_HF_in.T.Value; E_HF_inP=E1.E_HF_in.P.Value; E_HF_inza=E1.E_HF_in.z(r"AMMONIA").Value; E_HF_inzw=E1.E_HF_in.z(r"WATER").Value;
        E_HF_outF=E1.E_HF_out.F.Value; E_HF_outT=E1.E_HF_out.T.Value; E_HF_outP=E1.E_HF_out.P.Value; E_HF_outza=E1.E_HF_out.z(r"AMMONIA").Value; E_HF_outzw=E1.E_HF_out.z(r"WATER").Value;
        E_CF_inF=E1.E_CF_in.F.Value; E_CF_inT=E1.E_CF_in.T.Value; E_CF_inP=E1.E_CF_in.P.Value; E_CF_inza=E1.E_CF_in.z(r"AMMONIA").Value; E_CF_inzw=E1.E_CF_in.z(r"WATER").Value;
        E1Est[0][0]=E1.dT1.Value; E1Est[1][0]=E1.dT2.Value; E1Est[2][0]=E1.dTln.Value; E1Est[3][0]=E1.RF.Value; E1Est[4][0]=E1.PF.Value; E1Est[5][0]=E1.alphaF.Value;
        E1Est[6][0]=E1.SF.Value; E1Est[7][0]=E1.F.Value; E1Est[8][0]=E1.MWint.Value; E1Est[9][0]=E1.muint.Value; E1Est[10][0]=E1.Cpint.Value; E1Est[11][0]=E1.kappaint.Value;
        E1Est[12][0]=E1.Re_int.Value; E1Est[13][0]=E1.Pr_int.Value; E1Est[14][0]=E1.Nu_int.Value; E1Est[15][0]=E1.hint.Value; E1Est[16][0]=E1.a1.Value; E1Est[17][0]=E1.a2.Value; 
        E1Est[18][0]=E1.aBD.Value; E1Est[19][0]=E1.MWext.Value; E1Est[20][0]=E1.muext.Value; E1Est[21][0]=E1.Cpext.Value; E1Est[22][0]=E1.kappaext.Value; E1Est[23][0]=E1.Re_ext.Value; 
        E1Est[24][0]=E1.Pr_ext.Value; E1Est[25][0]=E1.jH.Value; E1Est[26][0]=E1.Afc.Value; E1Est[27][0]=E1.hext.Value; E1Est[28][0]=E1.U.Value; E1Est[29][0]=E1.QE.Q.Value; 
        # Guardar datos para Thermosiphon
        print("Thermosiphon");
        Thermosiphon=Sim.Flowsheet.Blocks(r"Thermosiphon"); TEst=np.zeros((11,1)); TDin=np.zeros((42,1));
        TEst[0][0]=Thermosiphon.hLiq_s_ps1pps2m3.Value; TEst[1][0]=Thermosiphon.hLiq_s_ps1pps2m2.Value; TEst[2][0]=Thermosiphon.Liq_s_ps1pps2m2F.Value; TEst[3][0]=Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value;
        TEst[4][0]=Thermosiphon.Liq_s_ps1pps2m2z(r"WATER").Value; TEst[5][0]=Thermosiphon.Liq_s_ps1pps2m2P.Value; TEst[6][0]=Thermosiphon.Liq_s_ps1pps2m2T.Value;
        TEst[7][0]=Thermosiphon.rhoLiq_s_ps1pps2m2.Value; TEst[8][0]=Thermosiphon.MWLiq_s_ps1pps2m2.Value; TEst[9][0]=Thermosiphon.z.Value; TEst[10][0]=Thermosiphon.QR.Q.Value; 
        # Guardar datos para E-3 y Divisor
        print("E-3 y Divisor");
        E3=Sim.Flowsheet.Blocks(r"E-3"); Divisor=Sim.Flowsheet.Blocks(r"Divisor"); E3DEst=np.zeros((12,1)); E3DDin=np.zeros((19,1));
        hVap_s_2=E3.hVap_s_2.Value; hC_HF_out=E3.hC_HF_out.Value; hC_CF_in=E3.hC_CF_in.Value; hC_CF_out=E3.hC_CF_out.Value;
        C_HF_outF=E3.C_HF_out.F.Value; C_HF_outT=E3.C_HF_out.T.Value; C_HF_outP=E3.C_HF_out.P.Value; C_HF_outza=E3.C_HF_out.z(r"AMMONIA").Value; C_HF_outzw=E3.C_HF_out.z(r"WATER").Value;
        C_CF_inF=E3.C_CF_in.F.Value; C_CF_inT=E3.C_CF_in.T.Value; C_CF_inP=E3.C_CF_in.P.Value; C_CF_inza=E3.C_CF_in.z(r"AMMONIA").Value; C_CF_inzw=E3.C_CF_in.z(r"WATER").Value;
        C_CF_outF=E3.C_CF_out.F.Value; C_CF_outT=E3.C_CF_out.T.Value; C_CF_outP=E3.C_CF_out.P.Value; C_CF_outza=E3.C_CF_out.z(r"AMMONIA").Value; C_CF_outzw=E3.C_CF_out.z(r"WATER").Value;
        Prod_LiqF=Divisor.Prod_Liq.F.Value; Prod_LiqT=Divisor.Prod_Liq.T.Value; Prod_LiqP=Divisor.Prod_Liq.P.Value; Prod_Liqza=Divisor.Prod_Liq.z(r"AMMONIA").Value; Prod_Liqzw=Divisor.Prod_Liq.z(r"WATER").Value; 
        E3DEst[0][0]=E3.QC.Q.Value; E3DEst[1][0]=Divisor.RR.Value; E3DEst[2][0]=Divisor.rhoProd_Liq.Value; E3DEst[3][0]=Divisor.Prod_Liqq.Value; E3DEst[4][0]=E3.dT1.Value; E3DEst[5][0]=E3.dT2.Value;
        E3DEst[6][0]=E3.dTln.Value; E3DEst[7][0]=E3.RF.Value; E3DEst[8][0]=E3.PF.Value; E3DEst[9][0]=E3.alphaF.Value; E3DEst[10][0]=E3.SF.Value; E3DEst[11][0]=E3.F.Value; ACM.quit(); 
        print(r"Simular estado estacionario para calcular acumulaciones:");
        # Calcular propiedades de cada etapa
        print("C-1");
        ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"Bulk.dynf")); Sim=ACM.Simulation; Bulk=Sim.Flowsheet.Blocks(r"Bulk"); 
        for i in range(0,ps1+ps2-4):
            Bulk.Vs.Value=C1par[0][i]; Bulk.Ls.Value=C1par[1][i]; Bulk.Tsg.Value=C1par[2][i]; Bulk.Tsl.Value=C1par[3][i]; Bulk.Ps.Value=C1par[4][i]; 
            Bulk.ys(r"AMMONIA").Value=C1par[5][i]; Bulk.ys(r"WATER").Value=C1par[6][i]; Bulk.xs(r"AMMONIA").Value=C1par[7][i]; Bulk.xs(r"WATER").Value=C1par[8][i]; 
            Bulk.Vb.Value=C1par[9][i]; Bulk.Lb.Value=C1par[10][i]; Bulk.Tbg.Value=C1par[11][i]; Bulk.Tbl.Value=C1par[12][i]; Bulk.Pb.Value=C1par[13][i]; 
            Bulk.yb(r"AMMONIA").Value=C1par[14][i]; Bulk.yb(r"WATER").Value=C1par[15][i]; Bulk.xb(r"AMMONIA").Value=C1par[16][i]; Bulk.xb(r"WATER").Value=C1par[17][i]; Bulk.Zs.Value=C1par[18][i]; 
            Bulk.hsg.Value=C1res[0][i]; Bulk.hsl.Value=C1res[1][i]; Bulk.rhobg.Value=C1res[2][i]; Bulk.rhobl.Value=C1res[3][i];
            Bulk.Dbg(r"AMMONIA",r"AMMONIA").Value=C1res[4][i]; Bulk.Dbg(r"AMMONIA",r"WATER").Value=C1res[5][i]; Bulk.Dbg(r"WATER",r"AMMONIA").Value=C1res[6][i]; Bulk.Dbg(r"WATER",r"WATER").Value=C1res[7][i];
            Bulk.Dbl(r"AMMONIA",r"AMMONIA").Value=C1res[8][i]; Bulk.Dbl(r"AMMONIA",r"WATER").Value=C1res[9][i]; Bulk.Dbl(r"WATER",r"AMMONIA").Value=C1res[10][i]; Bulk.Dbl(r"WATER",r"WATER").Value=C1res[11][i];
            Bulk.Cpbg.Value=C1res[12][i]; Bulk.Cpbl.Value=C1res[13][i]; Bulk.kappabg.Value=C1res[14][i]; Bulk.kappabl.Value=C1res[15][i]; Bulk.mubg.Value=C1res[16][i]; Bulk.mubl.Value=C1res[17][i];
            Bulk.sigmabl.Value=C1res[18][i]; Bulk.Uspg.Value=C1res[19][i]; Bulk.Uspl.Value=C1res[20][i]; Bulk.MWg.Value=C1res[21][i]; Bulk.MWl.Value=C1res[22][i]; Bulk.Scg.Value=C1res[23][i]; 
            Bulk.Scl.Value=C1res[24][i]; Bulk.Regc.Value=C1res[25][i]; Bulk.Relc.Value=C1res[26][i]; Bulk.Wel.Value=C1res[27][i]; Bulk.Frlc.Value=C1res[28][i]; Bulk.kbmg.Value=C1res[29][i];
            Bulk.kbml.Value=C1res[30][i]; Bulk.khg.Value=C1res[31][i]; Bulk.khl.Value=C1res[32][i]; Bulk.aef.Value=C1res[33][i]; Bulk.hbg.Value=C1res[34][i]; Bulk.hbl.Value=C1res[35][i]; 
            Bulk.cabl(r"AMMONIA").Value=C1res[36][i]; Bulk.cabl(r"WATER").Value=C1res[37][i]; Bulk.yba(r"AMMONIA").Value=C1res[38][i]; Bulk.yba(r"WATER").Value=C1res[39][i]; 
            Bulk.xba(r"AMMONIA").Value=C1res[40][i]; Bulk.xba(r"WATER").Value=C1res[41][i]; Bulk.ybd(r"AMMONIA").Value=C1res[42][i]; Bulk.ybd(r"WATER").Value=C1res[43][i]; 
            Bulk.xbd(r"AMMONIA").Value=C1res[44][i]; Bulk.xbd(r"WATER").Value=C1res[45][i]; Bulk.hga.Value=C1res[46][i]; Bulk.hla.Value=C1res[47][i]; Bulk.hgd.Value=C1res[48][i]; Bulk.hld.Value=C1res[49][i];
            Bulk.cala(r"AMMONIA").Value=C1res[50][i]; Bulk.cala(r"WATER").Value=C1res[51][i]; Bulk.cald(r"AMMONIA").Value=C1res[52][i]; Bulk.cald(r"WATER").Value=C1res[53][i]; Bulk.ubg.Value=C1res[54][i];
            Bulk.ubl.Value=C1res[55][i]; Bulk.Gammabl.Value=C1res[56][i]; Bulk.hpabg.Value=C1res[57][i]; Bulk.hpwbg.Value=C1res[58][i]; Bulk.hpabl.Value=C1res[59][i]; Bulk.hpwbl.Value=C1res[60][i];
            Bulk.Regp.Value=C1res[61][i]; Bulk.Frlp.Value=C1res[62][i]; Bulk.Hpr.Value=C1res[63][i]; Bulk.FSt.Value=C1res[64][i]; Bulk.CSt.Value=C1res[65][i]; Bulk.dPdry.Value=C1res[66][i]; Bulk.H.Value=C1res[67][i];
            Bulk.dPirr.Value=C1res[68][i]; Bulk.Nas.Value=C1res[69][i]; Bulk.Nts.Value=C1res[70][i]; Bulk.Es.Value=C1res[71][i]; Bulk.TI.Value=C1res[72][i]; Bulk.yI(r"AMMONIA").Value=C1res[73][i]; Bulk.yI(r"WATER").Value=C1res[74][i];
            Bulk.xI(r"AMMONIA").Value=C1res[75][i]; Bulk.xI(r"WATER").Value=C1res[76][i]; Bulk.phiIg(r"AMMONIA").Value=C1res[77][i]; Bulk.phiIg(r"WATER").Value=C1res[78][i]; 
            Bulk.phiIl(r"AMMONIA").Value=C1res[79][i]; Bulk.phiIl(r"WATER").Value=C1res[80][i]; Sim.Run(True);
            C1res[0][i]=Bulk.hsg.Value; C1res[1][i]=Bulk.hsl.Value; C1res[2][i]=Bulk.rhobg.Value; C1res[3][i]=Bulk.rhobl.Value;
            C1res[4][i]=Bulk.Dbg(r"AMMONIA",r"AMMONIA").Value; C1res[5][i]=Bulk.Dbg(r"AMMONIA",r"WATER").Value; C1res[6][i]=Bulk.Dbg(r"WATER",r"AMMONIA").Value; C1res[7][i]=Bulk.Dbg(r"WATER",r"WATER").Value;
            C1res[8][i]=Bulk.Dbl(r"AMMONIA",r"AMMONIA").Value; C1res[9][i]=Bulk.Dbl(r"AMMONIA",r"WATER").Value; C1res[10][i]=Bulk.Dbl(r"WATER",r"AMMONIA").Value; C1res[11][i]=Bulk.Dbl(r"WATER",r"WATER").Value;
            C1res[12][i]=Bulk.Cpbg.Value; C1res[13][i]=Bulk.Cpbl.Value; C1res[14][i]=Bulk.kappabg.Value; C1res[15][i]=Bulk.kappabl.Value; C1res[16][i]=Bulk.mubg.Value; C1res[17][i]=Bulk.mubl.Value;
            C1res[18][i]=Bulk.sigmabl.Value; C1res[19][i]=Bulk.Uspg.Value; C1res[20][i]=Bulk.Uspl.Value; C1res[21][i]=Bulk.MWg.Value; C1res[22][i]=Bulk.MWl.Value; C1res[23][i]=Bulk.Scg.Value; 
            C1res[24][i]=Bulk.Scl.Value; C1res[25][i]=Bulk.Regc.Value; C1res[26][i]=Bulk.Relc.Value; C1res[27][i]=Bulk.Wel.Value; C1res[28][i]=Bulk.Frlc.Value; C1res[29][i]=Bulk.kbmg.Value;
            C1res[30][i]=Bulk.kbml.Value; C1res[31][i]=Bulk.khg.Value; C1res[32][i]=Bulk.khl.Value; C1res[33][i]=Bulk.aef.Value; C1res[34][i]=Bulk.hbg.Value; C1res[35][i]=Bulk.hbl.Value; 
            C1res[36][i]=Bulk.cabl(r"AMMONIA").Value; C1res[37][i]=Bulk.cabl(r"WATER").Value; C1res[38][i]=Bulk.yba(r"AMMONIA").Value; C1res[39][i]=Bulk.yba(r"WATER").Value; 
            C1res[40][i]=Bulk.xba(r"AMMONIA").Value; C1res[41][i]=Bulk.xba(r"WATER").Value; C1res[42][i]=Bulk.ybd(r"AMMONIA").Value; C1res[43][i]=Bulk.ybd(r"WATER").Value; 
            C1res[44][i]=Bulk.xbd(r"AMMONIA").Value; C1res[45][i]=Bulk.xbd(r"WATER").Value; C1res[46][i]=Bulk.hga.Value; C1res[47][i]=Bulk.hla.Value; C1res[48][i]=Bulk.hgd.Value; C1res[49][i]=Bulk.hld.Value;
            C1res[50][i]=Bulk.cala(r"AMMONIA").Value; C1res[51][i]=Bulk.cala(r"WATER").Value; C1res[52][i]=Bulk.cald(r"AMMONIA").Value; C1res[53][i]=Bulk.cald(r"WATER").Value; C1res[54][i]=Bulk.ubg.Value;
            C1res[55][i]=Bulk.ubl.Value; C1res[56][i]=Bulk.Gammabl.Value; C1res[57][i]=Bulk.hpabg.Value; C1res[58][i]=Bulk.hpwbg.Value; C1res[59][i]=Bulk.hpabl.Value; C1res[60][i]=Bulk.hpwbl.Value;
            C1res[61][i]=Bulk.Regp.Value; C1res[62][i]=Bulk.Frlp.Value; C1res[63][i]=Bulk.Hpr.Value; C1res[64][i]=Bulk.FSt.Value; C1res[65][i]=Bulk.CSt.Value; C1res[66][i]=Bulk.dPdry.Value; C1res[67][i]=Bulk.H.Value;
            C1res[68][i]=Bulk.dPirr.Value; C1res[69][i]=Bulk.Nas.Value; C1res[70][i]=Bulk.Nts.Value; C1res[71][i]=Bulk.Es.Value; C1res[72][i]=Bulk.TI.Value; C1res[73][i]=Bulk.yI(r"AMMONIA").Value; C1res[74][i]=Bulk.yI(r"WATER").Value;
            C1res[75][i]=Bulk.xI(r"AMMONIA").Value; C1res[76][i]=Bulk.xI(r"WATER").Value; C1res[77][i]=Bulk.phiIg(r"AMMONIA").Value; C1res[78][i]=Bulk.phiIg(r"WATER").Value; 
            C1res[79][i]=Bulk.phiIl(r"AMMONIA").Value; C1res[80][i]=Bulk.phiIl(r"WATER").Value; C1res[81][i]=Bulk.Msg.Value; C1res[82][i]=Bulk.Msl.Value; C1res[83][i]=Bulk.Msga.Value; C1res[84][i]=Bulk.Msla.Value;
            C1res[85][i]=Bulk.Msgu.Value; C1res[86][i]=Bulk.Mslu.Value;
        ACM.quit(); 
        # Calcular propiedades de E-1
        print("E-1");
        ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"E1.dynf")); Sim=ACM.Simulation; E1=Sim.Flowsheet.Blocks(r"E-1"); LV1=Sim.Flowsheet.Blocks(r"LV-1");
        E1.hE_HF_in.Value=hE_HF_in; E1.hE_HF_out.Value=hE_HF_out; E1.hE_CF_in.Value=hE_CF_in; E1.hE_CF_out.Value=hE_CF_out;
        E1.E_HF_in.F.Value=E_HF_inF; E1.E_HF_in.T.Value=E_HF_inT; E1.E_HF_in.P.Value=E_HF_inP; E1.E_HF_in.z(r"AMMONIA").Value=E_HF_inza; E1.E_HF_in.z(r"WATER").Value=E_HF_inzw;
        E1.E_HF_out.F.Value=E_HF_outF; E1.E_HF_out.T.Value=E_HF_outT; E1.E_HF_out.P.Value=E_HF_outP; E1.E_HF_out.z(r"AMMONIA").Value=E_HF_outza; E1.E_HF_out.z(r"WATER").Value=E_HF_outzw;
        LV1.VIb_in.F.Value=E_HF_outF; LV1.VIb_in.T.Value=E_HF_outT; LV1.VIb_in.P.Value=E_HF_outP; LV1.VIb_in.z(r"AMMONIA").Value=E_HF_outza; LV1.VIb_in.z(r"WATER").Value=E_HF_outzw;
        E1.E_CF_in.F.Value=E_CF_inF; E1.E_CF_in.T.Value=E_CF_inT; E1.E_CF_in.P.Value=E_CF_inP; E1.E_CF_in.z(r"AMMONIA").Value=E_CF_inza; E1.E_CF_in.z(r"WATER").Value=E_CF_inzw;
        E1.E_CF_out.F.Value=E_CF_outF; E1.E_CF_out.T.Value=E_CF_outT; E1.E_CF_out.P.Value=E_CF_outP; E1.E_CF_out.z(r"AMMONIA").Value=E_CF_outza; E1.E_CF_out.z(r"WATER").Value=E_CF_outzw;
        E1.dT1.Value=E1Est[0][0]; E1.dT2.Value=E1Est[1][0]; E1.dTln.Value=E1Est[2][0]; E1.RF.Value=E1Est[3][0]; E1.PF.Value=E1Est[4][0]; E1.alphaF.Value=E1Est[5][0];
        E1.SF.Value=E1Est[6][0]; E1.F.Value=E1Est[7][0]; E1.MWint.Value=E1Est[8][0]; E1.muint.Value=E1Est[9][0]; E1Est[10][0]=E1.Cpint.Value; E1Est[11][0]=E1.kappaint.Value;
        E1.Re_int.Value=E1Est[12][0]; E1.Pr_int.Value=E1Est[13][0]; E1.Nu_int.Value=E1Est[14][0]; E1.hint.Value=E1Est[15][0]; E1.a1.Value=E1Est[16][0]; E1.a2.Value=E1Est[17][0]; 
        E1.aBD.Value=E1Est[18][0]; E1.MWext.Value=E1Est[19][0]; E1.muext.Value=E1Est[20][0]; E1.Cpext.Value=E1Est[21][0]; E1.kappaext.Value=E1Est[22][0]; E1.Re_ext.Value=E1Est[23][0]; 
        E1.Pr_ext.Value=E1Est[24][0]; E1.jH.Value=E1Est[25][0]; E1.Afc.Value=E1Est[26][0]; E1.hext.Value=E1Est[27][0]; E1.U.Value=E1Est[28][0]; E1.QE.Q.Value=E1Est[29][0]; LV1.vp.Value=vpLV1[caso]; Sim.Run(True);
        E1Est[0][0]=E1.dT1.Value; E1Est[1][0]=E1.dT2.Value; E1Est[2][0]=E1.dTln.Value; E1Est[3][0]=E1.RF.Value; E1Est[4][0]=E1.PF.Value; E1Est[5][0]=E1.alphaF.Value;
        E1Est[6][0]=E1.SF.Value; E1Est[7][0]=E1.F.Value; E1Est[8][0]=E1.MWint.Value; E1Est[9][0]=E1.muint.Value; E1Est[10][0]=E1.Cpint.Value; E1Est[11][0]=E1.kappaint.Value;
        E1Est[12][0]=E1.Re_int.Value; E1Est[13][0]=E1.Pr_int.Value; E1Est[14][0]=E1.Nu_int.Value; E1Est[15][0]=E1.hint.Value; E1Est[16][0]=E1.a1.Value; E1Est[17][0]=E1.a2.Value; 
        E1Est[18][0]=E1.aBD.Value; E1Est[19][0]=E1.MWext.Value; E1Est[20][0]=E1.muext.Value; E1Est[21][0]=E1.Cpext.Value; E1Est[22][0]=E1.kappaext.Value; E1Est[23][0]=E1.Re_ext.Value; 
        E1Est[24][0]=E1.Pr_ext.Value; E1Est[25][0]=E1.jH.Value; E1Est[26][0]=E1.Afc.Value; E1Est[27][0]=E1.hext.Value; E1Est[28][0]=E1.U.Value; E1Est[29][0]=E1.QE.Q.Value;
        E1Din[0][0]=E1.Ml_E_CF.Value; E1Din[1][0]=E1.Tl_E_CF.Value; E1Din[2][0]=E1.Pl_E_CF.Value; E1Din[3][0]=E1.x_E_CF(r"AMMONIA").Value; E1Din[4][0]=E1.x_E_CF(r"WATER").Value;
        E1Din[5][0]=E1.Ml_E_HF.Value; E1Din[6][0]=E1.Tl_E_HF.Value; E1Din[7][0]=E1.Pl_E_HF.Value; E1Din[8][0]=E1.x_E_HF(r"AMMONIA").Value; E1Din[9][0]=E1.x_E_HF(r"WATER").Value;
        E1Din[10][0]=E1.rholCF.Value; E1Din[11][0]=E1.hlCF.Value; E1Din[12][0]=E1.ulCF.Value; E1Din[13][0]=E1.rholHF.Value; E1Din[14][0]=E1.hlHF.Value; E1Din[15][0]=E1.ulHF.Value; 
        E1Din[16][0]=E1.MulCF.Value; E1Din[17][0]=LV1.q.Value; E1Din[18][0]=LV1.rho_CF.Value; vpLV1[caso]=LV1.vp.Value; ACM.quit(); 
        # Calcular propiedades de Thermosiphon
        print("Thermosiphon");
        ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"Thermosiphon.dynf")); Sim=ACM.Simulation; Thermosiphon=Sim.Flowsheet.Blocks(r"Thermosiphon");
        Thermosiphon.hR_CF_out.Value=hR_CF_out; Thermosiphon.hE_HF_in.Value=hE_HF_in;
        Thermosiphon.R_CF_out.F.Value=R_CF_outF; Thermosiphon.R_CF_out.T.Value=R_CF_outT; Thermosiphon.R_CF_out.P.Value=R_CF_outP; Thermosiphon.R_CF_out.z(r"AMMONIA").Value=R_CF_outza; Thermosiphon.R_CF_out.z(r"WATER").Value=R_CF_outzw;
        Thermosiphon.E_HF_in.F.Value=E_HF_inF; Thermosiphon.E_HF_in.T.Value=E_HF_inT; Thermosiphon.E_HF_in.P.Value=E_HF_inP; Thermosiphon.E_HF_in.z(r"AMMONIA").Value=E_HF_inza; Thermosiphon.E_HF_in.z(r"WATER").Value=E_HF_inzw;
        Thermosiphon.Liq_s_ps1pps2m3.F.Value=Liq_s_ps1pps2m3F; Thermosiphon.Liq_s_ps1pps2m3.T.Value=Liq_s_ps1pps2m3T; Thermosiphon.Liq_s_ps1pps2m3.P.Value=Liq_s_ps1pps2m3P; Thermosiphon.Liq_s_ps1pps2m3.z(r"AMMONIA").Value=Liq_s_ps1pps2m3za; Thermosiphon.Liq_s_ps1pps2m3.z(r"WATER").Value=Liq_s_ps1pps2m3zw;
        Thermosiphon.hLiq_s_ps1pps2m3.Value=TEst[0][0]; Thermosiphon.hLiq_s_ps1pps2m2.Value=TEst[1][0]; Thermosiphon.Liq_s_ps1pps2m2F.Value=TEst[2][0]; Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value=TEst[3][0];
        Thermosiphon.Liq_s_ps1pps2m2z(r"WATER").Value=TEst[4][0]; Thermosiphon.Liq_s_ps1pps2m2P.Value=TEst[5][0]; Thermosiphon.Liq_s_ps1pps2m2T.Value=TEst[6][0];
        Thermosiphon.rhoLiq_s_ps1pps2m2.Value=TEst[7][0]; Thermosiphon.MWLiq_s_ps1pps2m2.Value=TEst[8][0]; Thermosiphon.z.Value=TEst[9][0]; Thermosiphon.QR.Q.Value=TEst[10][0]; 
        Thermosiphon.R_HF_in.T.Value=TT6[caso]; Thermosiphon.R_HF_out.F.Value=FIC1[caso]; Thermosiphon.R_HF_in.P.Value=P_R_HF; Sim.Run(True);
        TEst[0][0]=Thermosiphon.hLiq_s_ps1pps2m3.Value; TEst[1][0]=Thermosiphon.hLiq_s_ps1pps2m2.Value; TEst[2][0]=Thermosiphon.Liq_s_ps1pps2m2F.Value; TEst[3][0]=Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value;
        TEst[4][0]=Thermosiphon.Liq_s_ps1pps2m2z(r"WATER").Value; TEst[5][0]=Thermosiphon.Liq_s_ps1pps2m2P.Value; TEst[6][0]=Thermosiphon.Liq_s_ps1pps2m2T.Value;
        TEst[7][0]=Thermosiphon.rhoLiq_s_ps1pps2m2.Value; TEst[8][0]=Thermosiphon.MWLiq_s_ps1pps2m2.Value; TEst[9][0]=Thermosiphon.z.Value; TEst[10][0]=Thermosiphon.QR.Q.Value; 
        R_HF_inF=Thermosiphon.R_HF_in.F.Value; R_HF_inT=Thermosiphon.R_HF_in.T.Value; R_HF_inP=Thermosiphon.R_HF_in.P.Value;
        R_HF_outF=Thermosiphon.R_HF_out.F.Value; R_HF_outT=Thermosiphon.R_HF_out.T.Value; R_HF_outP=Thermosiphon.R_HF_out.P.Value;
        TDin[0][0]=Thermosiphon.hR_HF_in.Value; TDin[1][0]=Thermosiphon.hR_HF_out.Value; TDin[2][0]=Thermosiphon.Vl_S.Value; TDin[3][0]=Thermosiphon.Vl_R_CF.Value;
        TDin[4][0]=Thermosiphon.LT1.Value; TDin[5][0]=Thermosiphon.Ml_S.Value; TDin[6][0]=Thermosiphon.Tl_S.Value; TDin[7][0]=Thermosiphon.Pl_S.Value; TDin[8][0]=Thermosiphon.x_S(r"AMMONIA").Value;
        TDin[9][0]=Thermosiphon.x_S(r"WATER").Value; TDin[10][0]=Thermosiphon.Mg_S.Value; TDin[11][0]=Thermosiphon.Tg_S.Value; TDin[12][0]=Thermosiphon.Pg_S.Value;
        TDin[13][0]=Thermosiphon.y_S(r"AMMONIA").Value; TDin[14][0]=Thermosiphon.y_S(r"WATER").Value; TDin[15][0]=Thermosiphon.Ml_R_CF.Value; TDin[16][0]=Thermosiphon.Tl_R_CF.Value;
        TDin[17][0]=Thermosiphon.Pl_R_CF.Value; TDin[18][0]=Thermosiphon.x_R_CF(r"AMMONIA").Value; TDin[19][0]=Thermosiphon.x_R_CF(r"WATER").Value;
        TDin[20][0]=Thermosiphon.Mg_R_CF.Value; TDin[21][0]=Thermosiphon.Tg_R_CF.Value; TDin[22][0]=Thermosiphon.Pg_R_CF.Value; TDin[23][0]=Thermosiphon.y_R_CF(r"AMMONIA").Value;
        TDin[24][0]=Thermosiphon.y_R_CF(r"WATER").Value; TDin[25][0]=Thermosiphon.rholS.Value; TDin[26][0]=Thermosiphon.rhogS.Value; TDin[27][0]=Thermosiphon.rholCF.Value;
        TDin[28][0]=Thermosiphon.rhogCF.Value; TDin[29][0]=Thermosiphon.hlS.Value; TDin[30][0]=Thermosiphon.hgS.Value; TDin[31][0]=Thermosiphon.hlCF.Value;
        TDin[32][0]=Thermosiphon.hgCF.Value; TDin[33][0]=Thermosiphon.ulS.Value; TDin[34][0]=Thermosiphon.ugS.Value; TDin[35][0]=Thermosiphon.ulCF.Value;
        TDin[36][0]=Thermosiphon.ugCF.Value; TDin[37][0]=Thermosiphon.MT.Value; TDin[38][0]=Thermosiphon.MzT.Value; TDin[39][0]=Thermosiphon.MuT.Value;
        TDin[40][0]=Thermosiphon.MRCF.Value; TDin[41][0]=Thermosiphon.MuRCF.Value; ACM.quit(); 
        # Calcular propiedades de E-3 y Divisor
        print("E-3 y Divisor");
        ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"E3.dynf")); Sim=ACM.Simulation; E3=Sim.Flowsheet.Blocks(r"E-3"); Divisor=Sim.Flowsheet.Blocks(r"Divisor"); PV2=Sim.Flowsheet.Blocks(r"PV-2");
        E3.hVap_s_2.Value=hVap_s_2; E3.hC_HF_out.Value=hC_HF_out; E3.hC_CF_in.Value=hC_CF_in; E3.hC_CF_out.Value=hC_CF_out;
        E3.Vap_s_2.F.Value=Vap_s_2F; E3.Vap_s_2.T.Value=Vap_s_2T; E3.Vap_s_2.P.Value=Vap_s_2P; E3.Vap_s_2.z(r"AMMONIA").Value=Vap_s_2za; E3.Vap_s_2.z(r"WATER").Value=Vap_s_2zw;
        Divisor.Reflujo.F.Value=ReflujoF; Divisor.Reflujo.T.Value=ReflujoT; Divisor.Reflujo.P.Value=ReflujoP; Divisor.Reflujo.z(r"AMMONIA").Value=Reflujoza; Divisor.Reflujo.z(r"WATER").Value=Reflujozw;
        E3.C_HF_out.F.Value=C_HF_outF; E3.C_HF_out.T.Value=C_HF_outT; E3.C_HF_out.P.Value=C_HF_outP; E3.C_HF_out.z(r"AMMONIA").Value=C_HF_outza; E3.C_HF_out.z(r"WATER").Value=C_HF_outzw;
        Divisor.C_HF_out.F.Value=C_HF_outF; Divisor.C_HF_out.T.Value=C_HF_outT; Divisor.C_HF_out.P.Value=C_HF_outP; Divisor.C_HF_out.z(r"AMMONIA").Value=C_HF_outza; Divisor.C_HF_out.z(r"WATER").Value=C_HF_outzw;
        E3.C_CF_in.F.Value=C_CF_inF; E3.C_CF_in.T.Value=C_CF_inT; E3.C_CF_in.P.Value=C_CF_inP; E3.C_CF_in.z(r"AMMONIA").Value=C_CF_inza; E3.C_CF_in.z(r"WATER").Value=C_CF_inzw;
        E3.C_CF_out.F.Value=C_CF_outF; E3.C_CF_out.T.Value=C_CF_outT; E3.C_CF_out.P.Value=C_CF_outP; E3.C_CF_out.z(r"AMMONIA").Value=C_CF_outza; E3.C_CF_out.z(r"WATER").Value=C_CF_outzw;
        PV2.VIb_in.F.Value=C_CF_outF; PV2.VIb_in.T.Value=C_CF_outT; PV2.VIb_in.P.Value=C_CF_outP; PV2.VIb_in.z(r"AMMONIA").Value=C_CF_outza; PV2.VIb_in.z(r"WATER").Value=C_CF_outzw;
        Divisor.Prod_Liq.F.Value=Prod_LiqF; Divisor.Prod_Liq.T.Value=Prod_LiqT; Divisor.Prod_Liq.P.Value=Prod_LiqP; Divisor.Prod_Liq.z(r"AMMONIA").Value=Prod_Liqza; Divisor.Prod_Liq.z(r"WATER").Value=Prod_Liqzw; 
        E3.QC.Q.Value=E3DEst[0][0]; Divisor.RR.Value=E3DEst[1][0]; Divisor.rhoProd_Liq.Value=E3DEst[2][0]; Divisor.Prod_Liqq.Value=E3DEst[3][0]; E3.dT1.Value=E3DEst[4][0]; E3.dT2.Value=E3DEst[5][0]; 
        E3.dTln.Value=E3DEst[6][0]; E3.RF.Value=E3DEst[7][0]; E3.PF.Value=E3DEst[8][0]; E3.alphaF.Value=E3DEst[9][0]; E3.SF.Value=E3DEst[10][0]; E3.F.Value=E3DEst[11][0]; PV2.vp.Value=vpPV2[caso]; Sim.Run(True); 
        E3DEst[0][0]=E3.QC.Q.Value; E3DEst[1][0]=Divisor.RR.Value; E3DEst[2][0]=Divisor.rhoProd_Liq.Value; E3DEst[3][0]=Divisor.Prod_Liqq.Value; E3DEst[4][0]=E3.dT1.Value; E3DEst[5][0]=E3.dT2.Value; 
        E3DEst[6][0]=E3.dTln.Value; E3DEst[7][0]=E3.RF.Value; E3DEst[8][0]=E3.PF.Value; E3DEst[9][0]=E3.alphaF.Value; E3DEst[10][0]=E3.SF.Value; E3DEst[11][0]=E3.F.Value;
        E3DDin[0][0]=E3.Ml_C_CF.Value; E3DDin[1][0]=E3.Tl_C_CF.Value; E3DDin[2][0]=E3.Pl_C_CF.Value; E3DDin[3][0]=E3.x_C_CF(r"AMMONIA").Value; E3DDin[4][0]=E3.x_C_CF(r"WATER").Value;
        E3DDin[5][0]=E3.Mg_C_HF.Value; E3DDin[6][0]=E3.Tg_C_HF.Value; E3DDin[7][0]=E3.Pg_C_HF.Value; E3DDin[8][0]=E3.y_C_HF(r"AMMONIA").Value; E3DDin[9][0]=E3.y_C_HF(r"WATER").Value;
        E3DDin[10][0]=E3.rholCF.Value; E3DDin[11][0]=E3.hlCF.Value; E3DDin[12][0]=E3.ulCF.Value; E3DDin[13][0]=E3.rhogHF.Value; E3DDin[14][0]=E3.hgHF.Value; E3DDin[15][0]=E3.ugHF.Value;
        E3DDin[16][0]=E3.MugHF.Value; E3DDin[17][0]=PV2.q.Value; E3DDin[18][0]=PV2.rho_CF.Value; vpPV2[caso]=PV2.vp.Value; ACM.quit(); 
        # Pasar propiedades a estado dinámico para pruebas en estado estacionario
        ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"Dinamico_ACM_Est.dynf")); Sim=ACM.Simulation; 
        C1=Sim.Flowsheet.Blocks(r"C-1"); E3=Sim.Flowsheet.Blocks(r"E-3"); Divisor=Sim.Flowsheet.Blocks(r"Divisor"); Thermosiphon=Sim.Flowsheet.Blocks(r"Thermosiphon"); E1=Sim.Flowsheet.Blocks(r"E-1"); 
        LV1=Sim.Flowsheet.Blocks(r"LV-1"); PV2=Sim.Flowsheet.Blocks(r"PV-2"); print(r"Inicializar con estado estacionario el modelo dinámico:");
        # C-1
        print("C-1");
        C1.ps1.Value=ps1; C1.ps2.Value=ps2; C1.flowmode1.Value=flowmode1; C1.flowmode2.Value=flowmode2;
        for i in range(0,ps1+ps2-4):
            C1.Vs(i+2).Value=C1par[0][i]; C1.Ls(i+2).Value=C1par[1][i]; C1.Tsg(i+2).Value=C1par[2][i]; C1.Tsl(i+2).Value=C1par[3][i]; C1.Ps(i+2).Value=C1par[4][i]; 
            C1.ys(r"AMMONIA",i+2).Value=C1par[5][i]; C1.ys(r"WATER",i+2).Value=C1par[6][i]; C1.xs(r"AMMONIA",i+2).Value=C1par[7][i]; C1.xs(r"WATER",i+2).Value=C1par[8][i]; 
            C1.Vb(i+2).Value=C1par[9][i]; C1.Lb(i+2).Value=C1par[10][i]; C1.Tbg(i+2).Value=C1par[11][i]; C1.Tbl(i+2).Value=C1par[12][i]; C1.Pb(i+2).Value=C1par[13][i]; 
            C1.yb(r"AMMONIA",i+2).Value=C1par[14][i]; C1.yb(r"WATER",i+2).Value=C1par[15][i]; C1.xb(r"AMMONIA",i+2).Value=C1par[16][i]; C1.xb(r"WATER",i+2).Value=C1par[17][i]; C1.Zs(i+2).Value=C1par[18][i];
            C1.hsg(i+2).Value=C1res[0][i]; C1.hsl(i+2).Value=C1res[1][i]; C1.rhobg(i+2).Value=C1res[2][i]; C1.rhobl(i+2).Value=C1res[3][i];
            C1.Dbg(r"AMMONIA",r"AMMONIA",i+2).Value=C1res[4][i]; C1.Dbg(r"AMMONIA",r"WATER",i+2).Value=C1res[5][i]; C1.Dbg(r"WATER",r"AMMONIA",i+2).Value=C1res[6][i]; C1.Dbg(r"WATER",r"WATER",i+2).Value=C1res[7][i];
            C1.Dbl(r"AMMONIA",r"AMMONIA",i+2).Value=C1res[8][i]; C1.Dbl(r"AMMONIA",r"WATER",i+2).Value=C1res[9][i]; C1.Dbl(r"WATER",r"AMMONIA",i+2).Value=C1res[10][i]; C1.Dbl(r"WATER",r"WATER",i+2).Value=C1res[11][i];
            C1.Cpbg(i+2).Value=C1res[12][i]; C1.Cpbl(i+2).Value=C1res[13][i]; C1.kappabg(i+2).Value=C1res[14][i]; C1.kappabl(i+2).Value=C1res[15][i]; C1.mubg(i+2).Value=C1res[16][i]; C1.mubl(i+2).Value=C1res[17][i];
            C1.sigmabl(i+2).Value=C1res[18][i]; C1.Uspg(i+2).Value=C1res[19][i]; C1.Uspl(i+2).Value=C1res[20][i]; C1.MWg(i+2).Value=C1res[21][i]; C1.MWl(i+2).Value=C1res[22][i]; C1.Scg(i+2).Value=C1res[23][i]; 
            C1.Scl(i+2).Value=C1res[24][i]; C1.Regc(i+2).Value=C1res[25][i]; C1.Relc(i+2).Value=C1res[26][i]; C1.Wel(i+2).Value=C1res[27][i]; C1.Frlc(i+2).Value=C1res[28][i]; C1.kbmg(i+2).Value=C1res[29][i];
            C1.kbml(i+2).Value=C1res[30][i]; C1.khg(i+2).Value=C1res[31][i]; C1.khl(i+2).Value=C1res[32][i]; C1.aef(i+2).Value=C1res[33][i]; C1.hbg(i+2).Value=C1res[34][i]; C1.hbl(i+2).Value=C1res[35][i]; 
            C1.cabl(r"AMMONIA",i+2).Value=C1res[36][i]; C1.cabl(r"WATER",i+2).Value=C1res[37][i]; C1.yba(r"AMMONIA",i+2).Value=C1res[38][i]; C1.yba(r"WATER",i+2).Value=C1res[39][i]; 
            C1.xba(r"AMMONIA",i+2).Value=C1res[40][i]; C1.xba(r"WATER",i+2).Value=C1res[41][i]; C1.ybd(r"AMMONIA",i+2).Value=C1res[42][i]; C1.ybd(r"WATER",i+2).Value=C1res[43][i]; 
            C1.xbd(r"AMMONIA",i+2).Value=C1res[44][i]; C1.xbd(r"WATER",i+2).Value=C1res[45][i]; C1.hga(i+2).Value=C1res[46][i]; C1.hla(i+2).Value=C1res[47][i]; C1.hgd(i+2).Value=C1res[48][i]; C1.hld(i+2).Value=C1res[49][i];
            C1.cala(r"AMMONIA",i+2).Value=C1res[50][i]; C1.cala(r"WATER",i+2).Value=C1res[51][i]; C1.cald(r"AMMONIA",i+2).Value=C1res[52][i]; C1.cald(r"WATER",i+2).Value=C1res[53][i]; C1.ubg(i+2).Value=C1res[54][i];
            C1.ubl(i+2).Value=C1res[55][i]; C1.Gammabl(i+2).Value=C1res[56][i]; C1.hpabg(i+2).Value=C1res[57][i]; C1.hpwbg(i+2).Value=C1res[58][i]; C1.hpabl(i+2).Value=C1res[59][i]; C1.hpwbl(i+2).Value=C1res[60][i];
            C1.Regp(i+2).Value=C1res[61][i]; C1.Frlp(i+2).Value=C1res[62][i]; C1.Hpr(i+2).Value=C1res[63][i]; C1.FSt(i+2).Value=C1res[64][i]; C1.CSt(i+2).Value=C1res[65][i]; C1.dPdry(i+2).Value=C1res[66][i]; C1.H(i+2).Value=C1res[67][i];
            C1.dPirr(i+2).Value=C1res[68][i]; C1.Nas(i+2).Value=C1res[69][i]; C1.Nts(i+2).Value=C1res[70][i]; C1.Es(i+2).Value=C1res[71][i]; C1.TI(i+2).Value=C1res[72][i]; C1.yI(r"AMMONIA",i+2).Value=C1res[73][i]; C1.yI(r"WATER",i+2).Value=C1res[74][i];
            C1.xI(r"AMMONIA",i+2).Value=C1res[75][i]; C1.xI(r"WATER",i+2).Value=C1res[76][i]; C1.phiIg(r"AMMONIA",i+2).Value=C1res[77][i]; C1.phiIg(r"WATER",i+2).Value=C1res[78][i]; 
            C1.phiIl(r"AMMONIA",i+2).Value=C1res[79][i]; C1.phiIl(r"WATER",i+2).Value=C1res[80][i]; C1.Msg(i+2).Value=C1res[81][i]; C1.Msl(i+2).Value=C1res[82][i]; C1.Msga(i+2).Value=C1res[83][i]; C1.Msla(i+2).Value=C1res[84][i];
            C1.Msgu(i+2).Value=C1res[85][i]; C1.Mslu(i+2).Value=C1res[86][i];
        C1.hReflujo.Value=hReflujo; C1.hR_CF_out.Value=hR_CF_out; C1.hE_CF_out.Value=hE_CF_out; 
        C1.Vap_s_2.F.Value=Vap_s_2F; C1.Vap_s_2.T.Value=Vap_s_2T; C1.Vap_s_2.P.Value=Vap_s_2P; C1.Vap_s_2.z(r"AMMONIA").Value=Vap_s_2za; C1.Vap_s_2.z(r"WATER").Value=Vap_s_2zw;
        E3.Vap_s_2.F.Value=Vap_s_2F; E3.Vap_s_2.T.Value=Vap_s_2T; E3.Vap_s_2.P.Value=Vap_s_2P; E3.Vap_s_2.z(r"AMMONIA").Value=Vap_s_2za; E3.Vap_s_2.z(r"WATER").Value=Vap_s_2zw;
        C1.Reflujo.F.Value=ReflujoF; C1.Reflujo.T.Value=ReflujoT; C1.Reflujo.P.Value=ReflujoP; C1.Reflujo.z(r"AMMONIA").Value=Reflujoza; C1.Reflujo.z(r"WATER").Value=Reflujozw;
        Divisor.Reflujo.F.Value=ReflujoF; Divisor.Reflujo.T.Value=ReflujoT; Divisor.Reflujo.P.Value=ReflujoP; Divisor.Reflujo.z(r"AMMONIA").Value=Reflujoza; Divisor.Reflujo.z(r"WATER").Value=Reflujozw;
        C1.R_CF_out.F.Value=R_CF_outF; C1.R_CF_out.T.Value=R_CF_outT; C1.R_CF_out.P.Value=R_CF_outP; C1.R_CF_out.z(r"AMMONIA").Value=R_CF_outza; C1.R_CF_out.z(r"WATER").Value=R_CF_outzw;
        Thermosiphon.R_CF_out.F.Value=R_CF_outF; Thermosiphon.R_CF_out.T.Value=R_CF_outT; Thermosiphon.R_CF_out.P.Value=R_CF_outP; Thermosiphon.R_CF_out.z(r"AMMONIA").Value=R_CF_outza; Thermosiphon.R_CF_out.z(r"WATER").Value=R_CF_outzw;
        C1.Liq_s_ps1pps2m3.F.Value=Liq_s_ps1pps2m3F; C1.Liq_s_ps1pps2m3.T.Value=Liq_s_ps1pps2m3T; C1.Liq_s_ps1pps2m3.P.Value=Liq_s_ps1pps2m3P; C1.Liq_s_ps1pps2m3.z(r"AMMONIA").Value=Liq_s_ps1pps2m3za; C1.Liq_s_ps1pps2m3.z(r"WATER").Value=Liq_s_ps1pps2m3zw;
        Thermosiphon.Liq_s_ps1pps2m3.F.Value=Liq_s_ps1pps2m3F; Thermosiphon.Liq_s_ps1pps2m3.T.Value=Liq_s_ps1pps2m3T; Thermosiphon.Liq_s_ps1pps2m3.P.Value=Liq_s_ps1pps2m3P; Thermosiphon.Liq_s_ps1pps2m3.z(r"AMMONIA").Value=Liq_s_ps1pps2m3za; Thermosiphon.Liq_s_ps1pps2m3.z(r"WATER").Value=Liq_s_ps1pps2m3zw;
        C1.E_CF_out.F.Value=E_CF_outF; C1.E_CF_out.T.Value=E_CF_outT; C1.E_CF_out.P.Value=E_CF_outP; C1.E_CF_out.z(r"AMMONIA").Value=E_CF_outza; C1.E_CF_out.z(r"WATER").Value=E_CF_outzw;
        E1.E_CF_out.F.Value=E_CF_outF; E1.E_CF_out.T.Value=E_CF_outT; E1.E_CF_out.P.Value=E_CF_outP; E1.E_CF_out.z(r"AMMONIA").Value=E_CF_outza; E1.E_CF_out.z(r"WATER").Value=E_CF_outzw;
        # E-1
        print("E-1");
        E1.hE_HF_in.Value=hE_HF_in; E1.hE_HF_out.Value=hE_HF_out; E1.hE_CF_in.Value=hE_CF_in; E1.hE_CF_out.Value=hE_CF_out;
        E1.E_HF_in.F.Value=E_HF_inF; E1.E_HF_in.T.Value=E_HF_inT; E1.E_HF_in.P.Value=E_HF_inP; E1.E_HF_in.z(r"AMMONIA").Value=E_HF_inza; E1.E_HF_in.z(r"WATER").Value=E_HF_inzw;
        Thermosiphon.E_HF_in.F.Value=E_HF_inF; Thermosiphon.E_HF_in.T.Value=E_HF_inT; Thermosiphon.E_HF_in.P.Value=E_HF_inP; Thermosiphon.E_HF_in.z(r"AMMONIA").Value=E_HF_inza; Thermosiphon.E_HF_in.z(r"WATER").Value=E_HF_inzw;
        E1.E_HF_out.F.Value=E_HF_outF; E1.E_HF_out.T.Value=E_HF_outT; E1.E_HF_out.P.Value=E_HF_outP; E1.E_HF_out.z(r"AMMONIA").Value=E_HF_outza; E1.E_HF_out.z(r"WATER").Value=E_HF_outzw;
        LV1.VIb_in.F.Value=E_HF_outF; LV1.VIb_in.T.Value=E_HF_outT; LV1.VIb_in.P.Value=E_HF_outP; LV1.VIb_in.z(r"AMMONIA").Value=E_HF_outza; LV1.VIb_in.z(r"WATER").Value=E_HF_outzw;
        E1.E_CF_in.F.Value=E_CF_inF; E1.E_CF_in.T.Value=E_CF_inT; E1.E_CF_in.P.Value=E_CF_inP; E1.E_CF_in.z(r"AMMONIA").Value=E_CF_inza; E1.E_CF_in.z(r"WATER").Value=E_CF_inzw;
        E1.dT1.Value=E1Est[0][0]; E1.dT2.Value=E1Est[1][0]; E1.dTln.Value=E1Est[2][0]; E1.RF.Value=E1Est[3][0]; E1.PF.Value=E1Est[4][0]; E1.alphaF.Value=E1Est[5][0];
        E1.SF.Value=E1Est[6][0]; E1.F.Value=E1Est[7][0]; E1.MWint.Value=E1Est[8][0]; E1.muint.Value=E1Est[9][0]; E1Est[10][0]=E1.Cpint.Value; E1Est[11][0]=E1.kappaint.Value;
        E1.Re_int.Value=E1Est[12][0]; E1.Pr_int.Value=E1Est[13][0]; E1.Nu_int.Value=E1Est[14][0]; E1.hint.Value=E1Est[15][0]; E1.a1.Value=E1Est[16][0]; E1.a2.Value=E1Est[17][0]; 
        E1.aBD.Value=E1Est[18][0]; E1.MWext.Value=E1Est[19][0]; E1.muext.Value=E1Est[20][0]; E1.Cpext.Value=E1Est[21][0]; E1.kappaext.Value=E1Est[22][0]; E1.Re_ext.Value=E1Est[23][0]; 
        E1.Pr_ext.Value=E1Est[24][0]; E1.jH.Value=E1Est[25][0]; E1.Afc.Value=E1Est[26][0]; E1.hext.Value=E1Est[27][0]; E1.U.Value=E1Est[28][0]; E1.QE.Q.Value=E1Est[29][0]; LV1.vp.Value=vpLV1[caso];
        E1.Ml_E_CF.Value=E1Din[0][0]; E1.Tl_E_CF.Value=E1Din[1][0]; E1.Pl_E_CF.Value=E1Din[2][0]; E1.x_E_CF(r"AMMONIA").Value=E1Din[3][0]; E1.x_E_CF(r"WATER").Value=E1Din[4][0];
        E1.Ml_E_HF.Value=E1Din[5][0]; E1.Tl_E_HF.Value=E1Din[6][0]; E1.Pl_E_HF.Value=E1Din[7][0]; E1.x_E_HF(r"AMMONIA").Value=E1Din[8][0]; E1.x_E_HF(r"WATER").Value=E1Din[9][0];
        E1.rholCF.Value=E1Din[10][0]; E1.hlCF.Value=E1Din[11][0]; E1.ulCF.Value=E1Din[12][0]; E1.rholHF.Value=E1Din[13][0]; E1.hlHF.Value=E1Din[14][0]; E1.ulHF.Value=E1Din[15][0]; 
        E1.MulCF.Value=E1Din[16][0]; LV1.q.Value=E1Din[17][0]; LV1.rho_CF.Value=E1Din[18][0]; 
        # Thermosiphon
        print("Thermosiphon");
        Thermosiphon.hR_CF_out.Value=hR_CF_out; Thermosiphon.hE_HF_in.Value=hE_HF_in;
        Thermosiphon.hLiq_s_ps1pps2m3.Value=TEst[0][0]; Thermosiphon.hLiq_s_ps1pps2m2.Value=TEst[1][0]; Thermosiphon.Liq_s_ps1pps2m2F.Value=TEst[2][0]; Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value=TEst[3][0];
        Thermosiphon.Liq_s_ps1pps2m2z(r"WATER").Value=TEst[4][0]; Thermosiphon.Liq_s_ps1pps2m2P.Value=TEst[5][0]; Thermosiphon.Liq_s_ps1pps2m2T.Value=TEst[6][0];
        Thermosiphon.rhoLiq_s_ps1pps2m2.Value=TEst[7][0]; Thermosiphon.MWLiq_s_ps1pps2m2.Value=TEst[8][0]; Thermosiphon.z.Value=TEst[9][0]; Thermosiphon.QR.Q.Value=TEst[10][0]; 
        Thermosiphon.R_HF_in.T.Value=TT6[caso]; Thermosiphon.R_HF_out.F.Value=FIC1[caso]; Thermosiphon.R_HF_in.P.Value=P_R_HF; 
        Thermosiphon.R_HF_in.F.Value=R_HF_inF; Thermosiphon.R_HF_in.T.Value=R_HF_inT; Thermosiphon.R_HF_in.P.Value=R_HF_inP;
        Thermosiphon.R_HF_out.F.Value=R_HF_outF; Thermosiphon.R_HF_out.T.Value=R_HF_outT; Thermosiphon.R_HF_out.P.Value=R_HF_outP;
        Thermosiphon.hR_HF_in.Value=TDin[0][0]; Thermosiphon.hR_HF_out.Value=TDin[1][0]; Thermosiphon.Vl_S.Value=TDin[2][0]; Thermosiphon.Vl_R_CF.Value=TDin[3][0];
        Thermosiphon.LT1.Value=TDin[4][0]; Thermosiphon.Ml_S.Value=TDin[5][0]; Thermosiphon.Tl_S.Value=TDin[6][0]; Thermosiphon.Pl_S.Value=TDin[7][0]; Thermosiphon.x_S(r"AMMONIA").Value=TDin[8][0];
        Thermosiphon.x_S(r"WATER").Value=TDin[9][0]; Thermosiphon.Mg_S.Value=TDin[10][0]; Thermosiphon.Tg_S.Value=TDin[11][0]; Thermosiphon.Pg_S.Value=TDin[12][0];
        Thermosiphon.y_S(r"AMMONIA").Value=TDin[13][0]; Thermosiphon.y_S(r"WATER").Value=TDin[14][0]; Thermosiphon.Ml_R_CF.Value=TDin[15][0]; Thermosiphon.Tl_R_CF.Value=TDin[16][0];
        Thermosiphon.Pl_R_CF.Value=TDin[17][0]; Thermosiphon.x_R_CF(r"AMMONIA").Value=TDin[18][0]; Thermosiphon.x_R_CF(r"WATER").Value=TDin[19][0];
        Thermosiphon.Mg_R_CF.Value=TDin[20][0]; Thermosiphon.Tg_R_CF.Value=TDin[21][0]; Thermosiphon.Pg_R_CF.Value=TDin[22][0]; Thermosiphon.y_R_CF(r"AMMONIA").Value=TDin[23][0];
        Thermosiphon.y_R_CF(r"WATER").Value=TDin[24][0]; Thermosiphon.rholS.Value=TDin[25][0]; Thermosiphon.rhogS.Value=TDin[26][0]; Thermosiphon.rholCF.Value=TDin[27][0];
        Thermosiphon.rhogCF.Value=TDin[28][0]; Thermosiphon.hlS.Value=TDin[29][0]; Thermosiphon.hgS.Value=TDin[30][0]; Thermosiphon.hlCF.Value=TDin[31][0];
        Thermosiphon.hgCF.Value=TDin[32][0]; Thermosiphon.ulS.Value=TDin[33][0]; Thermosiphon.ugS.Value=TDin[34][0]; Thermosiphon.ulCF.Value=TDin[35][0];
        Thermosiphon.ugCF.Value=TDin[36][0]; Thermosiphon.MT.Value=TDin[37][0]; Thermosiphon.MzT.Value=TDin[38][0]; Thermosiphon.MuT.Value=TDin[39][0];
        Thermosiphon.MRCF.Value=TDin[40][0]; Thermosiphon.MuRCF.Value=TDin[41][0];
        # E-3 y Divisor
        print("E-3 y Divisor");
        E3.hVap_s_2.Value=hVap_s_2; E3.hC_HF_out.Value=hC_HF_out; E3.hC_CF_in.Value=hC_CF_in; E3.hC_CF_out.Value=hC_CF_out;
        E3.Vap_s_2.F.Value=Vap_s_2F; E3.Vap_s_2.T.Value=Vap_s_2T; E3.Vap_s_2.P.Value=Vap_s_2P; E3.Vap_s_2.z(r"AMMONIA").Value=Vap_s_2za; E3.Vap_s_2.z(r"WATER").Value=Vap_s_2zw;
        Divisor.Reflujo.F.Value=ReflujoF; Divisor.Reflujo.T.Value=ReflujoT; Divisor.Reflujo.P.Value=ReflujoP; Divisor.Reflujo.z(r"AMMONIA").Value=Reflujoza; Divisor.Reflujo.z(r"WATER").Value=Reflujozw;
        E3.C_HF_out.F.Value=C_HF_outF; E3.C_HF_out.T.Value=C_HF_outT; E3.C_HF_out.P.Value=C_HF_outP; E3.C_HF_out.z(r"AMMONIA").Value=C_HF_outza; E3.C_HF_out.z(r"WATER").Value=C_HF_outzw;
        Divisor.C_HF_out.F.Value=C_HF_outF; Divisor.C_HF_out.T.Value=C_HF_outT; Divisor.C_HF_out.P.Value=C_HF_outP; Divisor.C_HF_out.z(r"AMMONIA").Value=C_HF_outza; Divisor.C_HF_out.z(r"WATER").Value=C_HF_outzw;
        E3.C_CF_in.F.Value=C_CF_inF; E3.C_CF_in.T.Value=C_CF_inT; E3.C_CF_in.P.Value=C_CF_inP; E3.C_CF_in.z(r"AMMONIA").Value=C_CF_inza; E3.C_CF_in.z(r"WATER").Value=C_CF_inzw;
        E3.C_CF_out.F.Value=C_CF_outF; E3.C_CF_out.T.Value=C_CF_outT; E3.C_CF_out.P.Value=C_CF_outP; E3.C_CF_out.z(r"AMMONIA").Value=C_CF_outza; E3.C_CF_out.z(r"WATER").Value=C_CF_outzw;
        PV2.VIb_in.F.Value=C_CF_outF; PV2.VIb_in.T.Value=C_CF_outT; PV2.VIb_in.P.Value=C_CF_outP; PV2.VIb_in.z(r"AMMONIA").Value=C_CF_outza; PV2.VIb_in.z(r"WATER").Value=C_CF_outzw;
        Divisor.Prod_Liq.F.Value=Prod_LiqF; Divisor.Prod_Liq.T.Value=Prod_LiqT; Divisor.Prod_Liq.P.Value=Prod_LiqP; Divisor.Prod_Liq.z(r"AMMONIA").Value=Prod_Liqza; Divisor.Prod_Liq.z(r"WATER").Value=Prod_Liqzw; 
        E3.QC.Q.Value=E3DEst[0][0]; Divisor.RR.Value=E3DEst[1][0]; Divisor.rhoProd_Liq.Value=E3DEst[2][0]; Divisor.Prod_Liqq.Value=E3DEst[3][0]; E3.dT1.Value=E3DEst[4][0]; E3.dT2.Value=E3DEst[5][0]; 
        E3.dTln.Value=E3DEst[6][0]; E3.RF.Value=E3DEst[7][0]; E3.PF.Value=E3DEst[8][0]; E3.alphaF.Value=E3DEst[9][0]; E3.SF.Value=E3DEst[10][0]; E3.F.Value=E3DEst[11][0]; PV2.vp.Value=vpPV2[caso]; 
        E3.Ml_C_CF.Value=E3DDin[0][0]; E3.Tl_C_CF.Value=E3DDin[1][0]; E3.Pl_C_CF.Value=E3DDin[2][0]; E3.x_C_CF(r"AMMONIA").Value=E3DDin[3][0]; E3.x_C_CF(r"WATER").Value=E3DDin[4][0];
        E3.Mg_C_HF.Value=E3DDin[5][0]; E3.Tg_C_HF.Value=E3DDin[6][0]; E3.Pg_C_HF.Value=E3DDin[7][0]; E3.y_C_HF(r"AMMONIA").Value=E3DDin[8][0]; E3.y_C_HF(r"WATER").Value=E3DDin[9][0];
        E3.rholCF.Value=E3DDin[10][0]; E3.hlCF.Value=E3DDin[11][0]; E3.ulCF.Value=E3DDin[12][0]; E3.rhogHF.Value=E3DDin[13][0]; E3.hgHF.Value=E3DDin[14][0]; E3.ugHF.Value=E3DDin[15][0];
        E3.MugHF.Value=E3DDin[16][0]; PV2.q.Value=E3DDin[17][0]; PV2.rho_CF.Value=E3DDin[18][0]; 
        # Prueba con grados de libertad originales
        print(r"Caso estacionario");
        try:
            Sim.Run(True);
            print(r"TT-7 Fijo y z Libre: Sí genera resultados Aspen Custom Modeler");
            ACM.SaveDocumentAs(os.path.abspath(r"Dinamico_Est_Prueba.dynf"),True);
        except: # Cuando no genera resultados
            print(r"TT-7 Fijo y z Libre: No genera resultados Aspen Custom Modeler");
        Thermosiphon.z.Spec=r"Fixed"; Thermosiphon.R_HF_out.T.Spec=r"Free";
        # Prueba cambiando z y TT-7
        try:
            Sim.Run(True);
            print(r"TT-7 Libre y z Fijo: Sí genera resultados Aspen Custom Modeler");
        except: # Cuando no genera resultados
            print(r"TT-7 Libre y z Fijo: No genera resultados Aspen Custom Modeler");
        ACM.quit();
# Pasar propiedades a estado dinámico para pruebas en estado dinámico
print(r"Caso dinámico: Caso33-MIXED-1-19.dynf"); caso=1; simtype=1;
# Guardar parametros que determinan el estado completo de cada etapa en C-1
print(r"Guardar estado estacionario:");
print("C-1");
ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(CasoEst[caso][simtype])); Sim=ACM.Simulation; C1=Sim.Flowsheet.Blocks(r"C-1");
ps1=C1.ps1.Value; ps2=C1.ps2.Value; flowmode1=C1.flowmode1.Value; flowmode2=C1.flowmode2.Value; C1par=np.zeros((19,ps1+ps2-4)); C1res=np.zeros((87,ps1+ps2-4));
for i in range(2,ps1+ps2-2):
    C1par[0][i-2]=C1.Vs(i).Value; C1par[1][i-2]=C1.Ls(i).Value; C1par[2][i-2]=C1.Tsg(i).Value; C1par[3][i-2]=C1.Tsl(i).Value; C1par[4][i-2]=C1.Ps(i).Value; 
    C1par[5][i-2]=C1.ys(r"AMMONIA",i).Value; C1par[6][i-2]=C1.ys(r"WATER",i).Value; C1par[7][i-2]=C1.xs(r"AMMONIA",i).Value; C1par[8][i-2]=C1.xs(r"WATER",i).Value;
    C1par[9][i-2]=C1.Vb(i).Value; C1par[10][i-2]=C1.Lb(i).Value; C1par[11][i-2]=C1.Tbg(i).Value; C1par[12][i-2]=C1.Tbl(i).Value; C1par[13][i-2]=C1.Pb(i).Value; 
    C1par[14][i-2]=C1.yb(r"AMMONIA",i).Value; C1par[15][i-2]=C1.yb(r"WATER",i).Value; C1par[16][i-2]=C1.xb(r"AMMONIA",i).Value; C1par[17][i-2]=C1.xb(r"WATER",i).Value; C1par[18][i-2]=C1.Zs(i).Value;
    C1res[0][i-2]=C1.hsg(i).Value; C1res[1][i-2]=C1.hsl(i).Value; C1res[2][i-2]=C1.rhobg(i).Value; C1res[3][i-2]=C1.rhobl(i).Value;
    C1res[4][i-2]=C1.Dbg(r"AMMONIA",r"AMMONIA",i).Value; C1res[5][i-2]=C1.Dbg(r"AMMONIA",r"WATER",i).Value; C1res[6][i-2]=C1.Dbg(r"WATER",r"AMMONIA",i).Value; C1res[7][i-2]=C1.Dbg(r"WATER",r"WATER",i).Value;
    C1res[8][i-2]=C1.Dbl(r"AMMONIA",r"AMMONIA",i).Value; C1res[9][i-2]=C1.Dbl(r"AMMONIA",r"WATER",i).Value; C1res[10][i-2]=C1.Dbl(r"WATER",r"AMMONIA",i).Value; C1res[11][i-2]=C1.Dbl(r"WATER",r"WATER",i).Value;
    C1res[12][i-2]=C1.Cpbg(i).Value; C1res[13][i-2]=C1.Cpbl(i).Value; C1res[14][i-2]=C1.kappabg(i).Value; C1res[15][i-2]=C1.kappabl(i).Value; C1res[16][i-2]=C1.mubg(i).Value; C1res[17][i-2]=C1.mubl(i).Value;
    C1res[18][i-2]=C1.sigmabl(i).Value; C1res[19][i-2]=C1.Uspg(i).Value; C1res[20][i-2]=C1.Uspl(i).Value; C1res[21][i-2]=C1.MWg(i).Value; C1res[22][i-2]=C1.MWl(i).Value; C1res[23][i-2]=C1.Scg(i).Value; 
    C1res[24][i-2]=C1.Scl(i).Value; C1res[25][i-2]=C1.Regc(i).Value; C1res[26][i-2]=C1.Relc(i).Value; C1res[27][i-2]=C1.Wel(i).Value; C1res[28][i-2]=C1.Frlc(i).Value; C1res[29][i-2]=C1.kbmg(i).Value;
    C1res[30][i-2]=C1.kbml(i).Value; C1res[31][i-2]=C1.khg(i).Value; C1res[32][i-2]=C1.khl(i).Value; C1res[33][i-2]=C1.aef(i).Value; C1res[34][i-2]=C1.hbg(i).Value; C1res[35][i-2]=C1.hbl(i).Value; 
    C1res[36][i-2]=C1.cabl(r"AMMONIA",i).Value; C1res[37][i-2]=C1.cabl(r"WATER",i).Value; C1res[38][i-2]=C1.yba(r"AMMONIA",i).Value; C1res[39][i-2]=C1.yba(r"WATER",i).Value; 
    C1res[40][i-2]=C1.xba(r"AMMONIA",i).Value; C1res[41][i-2]=C1.xba(r"WATER",i).Value; C1res[42][i-2]=C1.ybd(r"AMMONIA",i).Value; C1res[43][i-2]=C1.ybd(r"WATER",i).Value; 
    C1res[44][i-2]=C1.xbd(r"AMMONIA",i).Value; C1res[45][i-2]=C1.xbd(r"WATER",i).Value; C1res[46][i-2]=C1.hga(i).Value; C1res[47][i-2]=C1.hla(i).Value; C1res[48][i-2]=C1.hgd(i).Value; C1res[49][i-2]=C1.hld(i).Value;
    C1res[50][i-2]=C1.cala(r"AMMONIA",i).Value; C1res[51][i-2]=C1.cala(r"WATER",i).Value; C1res[52][i-2]=C1.cald(r"AMMONIA",i).Value; C1res[53][i-2]=C1.cald(r"WATER",i).Value; C1res[54][i-2]=C1.ubg(i).Value;
    C1res[55][i-2]=C1.ubl(i).Value; C1res[56][i-2]=C1.Gammabl(i).Value; C1res[57][i-2]=C1.hpabg(i).Value; C1res[58][i-2]=C1.hpwbg(i).Value; C1res[59][i-2]=C1.hpabl(i).Value; C1res[60][i-2]=C1.hpwbl(i).Value;
    C1res[61][i-2]=C1.Regp(i).Value; C1res[62][i-2]=C1.Frlp(i).Value; C1res[63][i-2]=C1.Hpr(i).Value; C1res[64][i-2]=C1.FSt(i).Value; C1res[65][i-2]=C1.CSt(i).Value; C1res[66][i-2]=C1.dPdry(i).Value; C1res[67][i-2]=C1.H(i).Value;
    C1res[68][i-2]=C1.dPirr(i).Value; C1res[69][i-2]=C1.Nas(i).Value; C1res[70][i-2]=C1.Nts(i).Value; C1res[71][i-2]=C1.Es(i).Value; C1res[72][i-2]=C1.TI(i).Value; C1res[73][i-2]=C1.yI(r"AMMONIA",i).Value; C1res[74][i-2]=C1.yI(r"WATER",i).Value;
    C1res[75][i-2]=C1.xI(r"AMMONIA",i).Value; C1res[76][i-2]=C1.xI(r"WATER",i).Value; C1res[77][i-2]=C1.phiIg(r"AMMONIA",i).Value; C1res[78][i-2]=C1.phiIg(r"WATER",i).Value; 
    C1res[79][i-2]=C1.phiIl(r"AMMONIA",i).Value; C1res[80][i-2]=C1.phiIl(r"WATER",i).Value; 
hReflujo=C1.hReflujo.Value; hR_CF_out=C1.hR_CF_out.Value; hE_CF_out=C1.hE_CF_out.Value; 
Vap_s_2F=C1.Vap_s_2.F.Value; Vap_s_2T=C1.Vap_s_2.T.Value; Vap_s_2P=C1.Vap_s_2.P.Value; Vap_s_2za=C1.Vap_s_2.z(r"AMMONIA").Value; Vap_s_2zw=C1.Vap_s_2.z(r"WATER").Value;
ReflujoF=C1.Reflujo.F.Value; ReflujoT=C1.Reflujo.T.Value; ReflujoP=C1.Reflujo.P.Value; Reflujoza=C1.Reflujo.z(r"AMMONIA").Value; Reflujozw=C1.Reflujo.z(r"WATER").Value;
R_CF_outF=C1.R_CF_out.F.Value; R_CF_outT=C1.R_CF_out.T.Value; R_CF_outP=C1.R_CF_out.P.Value; R_CF_outza=C1.R_CF_out.z(r"AMMONIA").Value; R_CF_outzw=C1.R_CF_out.z(r"WATER").Value;
Liq_s_ps1pps2m3F=C1.Liq_s_ps1pps2m3.F.Value; Liq_s_ps1pps2m3T=C1.Liq_s_ps1pps2m3.T.Value; Liq_s_ps1pps2m3P=C1.Liq_s_ps1pps2m3.P.Value; Liq_s_ps1pps2m3za=C1.Liq_s_ps1pps2m3.z(r"AMMONIA").Value; Liq_s_ps1pps2m3zw=C1.Liq_s_ps1pps2m3.z(r"WATER").Value;
E_CF_outF=C1.E_CF_out.F.Value; E_CF_outT=C1.E_CF_out.T.Value; E_CF_outP=C1.E_CF_out.P.Value; E_CF_outza=C1.E_CF_out.z(r"AMMONIA").Value; E_CF_outzw=C1.E_CF_out.z(r"WATER").Value; 
# Guardar datos para E-1
print("E-1");
E1=Sim.Flowsheet.Blocks(r"E-1"); E1Est=np.zeros((30,1)); E1Din=np.zeros((20,1));
hE_HF_in=E1.hE_HF_in.Value; hE_HF_out=E1.hE_HF_out.Value; hE_CF_in=E1.hE_CF_in.Value; 
E_HF_inF=E1.E_HF_in.F.Value; E_HF_inT=E1.E_HF_in.T.Value; E_HF_inP=E1.E_HF_in.P.Value; E_HF_inza=E1.E_HF_in.z(r"AMMONIA").Value; E_HF_inzw=E1.E_HF_in.z(r"WATER").Value;
E_HF_outF=E1.E_HF_out.F.Value; E_HF_outT=E1.E_HF_out.T.Value; E_HF_outP=E1.E_HF_out.P.Value; E_HF_outza=E1.E_HF_out.z(r"AMMONIA").Value; E_HF_outzw=E1.E_HF_out.z(r"WATER").Value;
E_CF_inF=E1.E_CF_in.F.Value; E_CF_inT=E1.E_CF_in.T.Value; E_CF_inP=E1.E_CF_in.P.Value; E_CF_inza=E1.E_CF_in.z(r"AMMONIA").Value; E_CF_inzw=E1.E_CF_in.z(r"WATER").Value;
E1Est[0][0]=E1.dT1.Value; E1Est[1][0]=E1.dT2.Value; E1Est[2][0]=E1.dTln.Value; E1Est[3][0]=E1.RF.Value; E1Est[4][0]=E1.PF.Value; E1Est[5][0]=E1.alphaF.Value;
E1Est[6][0]=E1.SF.Value; E1Est[7][0]=E1.F.Value; E1Est[8][0]=E1.MWint.Value; E1Est[9][0]=E1.muint.Value; E1Est[10][0]=E1.Cpint.Value; E1Est[11][0]=E1.kappaint.Value;
E1Est[12][0]=E1.Re_int.Value; E1Est[13][0]=E1.Pr_int.Value; E1Est[14][0]=E1.Nu_int.Value; E1Est[15][0]=E1.hint.Value; E1Est[16][0]=E1.a1.Value; E1Est[17][0]=E1.a2.Value; 
E1Est[18][0]=E1.aBD.Value; E1Est[19][0]=E1.MWext.Value; E1Est[20][0]=E1.muext.Value; E1Est[21][0]=E1.Cpext.Value; E1Est[22][0]=E1.kappaext.Value; E1Est[23][0]=E1.Re_ext.Value; 
E1Est[24][0]=E1.Pr_ext.Value; E1Est[25][0]=E1.jH.Value; E1Est[26][0]=E1.Afc.Value; E1Est[27][0]=E1.hext.Value; E1Est[28][0]=E1.U.Value; E1Est[29][0]=E1.QE.Q.Value; 
# Guardar datos para Thermosiphon
print("Thermosiphon");
Thermosiphon=Sim.Flowsheet.Blocks(r"Thermosiphon"); TEst=np.zeros((11,1)); TDin=np.zeros((42,1));
TEst[0][0]=Thermosiphon.hLiq_s_ps1pps2m3.Value; TEst[1][0]=Thermosiphon.hLiq_s_ps1pps2m2.Value; TEst[2][0]=Thermosiphon.Liq_s_ps1pps2m2F.Value; TEst[3][0]=Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value;
TEst[4][0]=Thermosiphon.Liq_s_ps1pps2m2z(r"WATER").Value; TEst[5][0]=Thermosiphon.Liq_s_ps1pps2m2P.Value; TEst[6][0]=Thermosiphon.Liq_s_ps1pps2m2T.Value;
TEst[7][0]=Thermosiphon.rhoLiq_s_ps1pps2m2.Value; TEst[8][0]=Thermosiphon.MWLiq_s_ps1pps2m2.Value; TEst[9][0]=Thermosiphon.z.Value; TEst[10][0]=Thermosiphon.QR.Q.Value; 
# Guardar datos para E-3 y Divisor
print("E-3 y Divisor");
E3=Sim.Flowsheet.Blocks(r"E-3"); Divisor=Sim.Flowsheet.Blocks(r"Divisor"); E3DEst=np.zeros((12,1)); E3DDin=np.zeros((19,1));
hVap_s_2=E3.hVap_s_2.Value; hC_HF_out=E3.hC_HF_out.Value; hC_CF_in=E3.hC_CF_in.Value; hC_CF_out=E3.hC_CF_out.Value;
C_HF_outF=E3.C_HF_out.F.Value; C_HF_outT=E3.C_HF_out.T.Value; C_HF_outP=E3.C_HF_out.P.Value; C_HF_outza=E3.C_HF_out.z(r"AMMONIA").Value; C_HF_outzw=E3.C_HF_out.z(r"WATER").Value;
C_CF_inF=E3.C_CF_in.F.Value; C_CF_inT=E3.C_CF_in.T.Value; C_CF_inP=E3.C_CF_in.P.Value; C_CF_inza=E3.C_CF_in.z(r"AMMONIA").Value; C_CF_inzw=E3.C_CF_in.z(r"WATER").Value;
C_CF_outF=E3.C_CF_out.F.Value; C_CF_outT=E3.C_CF_out.T.Value; C_CF_outP=E3.C_CF_out.P.Value; C_CF_outza=E3.C_CF_out.z(r"AMMONIA").Value; C_CF_outzw=E3.C_CF_out.z(r"WATER").Value;
Prod_LiqF=Divisor.Prod_Liq.F.Value; Prod_LiqT=Divisor.Prod_Liq.T.Value; Prod_LiqP=Divisor.Prod_Liq.P.Value; Prod_Liqza=Divisor.Prod_Liq.z(r"AMMONIA").Value; Prod_Liqzw=Divisor.Prod_Liq.z(r"WATER").Value; 
E3DEst[0][0]=E3.QC.Q.Value; E3DEst[1][0]=Divisor.RR.Value; E3DEst[2][0]=Divisor.rhoProd_Liq.Value; E3DEst[3][0]=Divisor.Prod_Liqq.Value; E3DEst[4][0]=E3.dT1.Value; E3DEst[5][0]=E3.dT2.Value;
E3DEst[6][0]=E3.dTln.Value; E3DEst[7][0]=E3.RF.Value; E3DEst[8][0]=E3.PF.Value; E3DEst[9][0]=E3.alphaF.Value; E3DEst[10][0]=E3.SF.Value; E3DEst[11][0]=E3.F.Value; ACM.quit(); 
print(r"Simular estado estacionario para calcular acumulaciones:");
# Calcular propiedades de cada etapa
print("C-1");
ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"Bulk.dynf")); Sim=ACM.Simulation; Bulk=Sim.Flowsheet.Blocks(r"Bulk"); 
for i in range(0,ps1+ps2-4):
    Bulk.Vs.Value=C1par[0][i]; Bulk.Ls.Value=C1par[1][i]; Bulk.Tsg.Value=C1par[2][i]; Bulk.Tsl.Value=C1par[3][i]; Bulk.Ps.Value=C1par[4][i]; 
    Bulk.ys(r"AMMONIA").Value=C1par[5][i]; Bulk.ys(r"WATER").Value=C1par[6][i]; Bulk.xs(r"AMMONIA").Value=C1par[7][i]; Bulk.xs(r"WATER").Value=C1par[8][i]; 
    Bulk.Vb.Value=C1par[9][i]; Bulk.Lb.Value=C1par[10][i]; Bulk.Tbg.Value=C1par[11][i]; Bulk.Tbl.Value=C1par[12][i]; Bulk.Pb.Value=C1par[13][i]; 
    Bulk.yb(r"AMMONIA").Value=C1par[14][i]; Bulk.yb(r"WATER").Value=C1par[15][i]; Bulk.xb(r"AMMONIA").Value=C1par[16][i]; Bulk.xb(r"WATER").Value=C1par[17][i]; Bulk.Zs.Value=C1par[18][i]; 
    Bulk.hsg.Value=C1res[0][i]; Bulk.hsl.Value=C1res[1][i]; Bulk.rhobg.Value=C1res[2][i]; Bulk.rhobl.Value=C1res[3][i];
    Bulk.Dbg(r"AMMONIA",r"AMMONIA").Value=C1res[4][i]; Bulk.Dbg(r"AMMONIA",r"WATER").Value=C1res[5][i]; Bulk.Dbg(r"WATER",r"AMMONIA").Value=C1res[6][i]; Bulk.Dbg(r"WATER",r"WATER").Value=C1res[7][i];
    Bulk.Dbl(r"AMMONIA",r"AMMONIA").Value=C1res[8][i]; Bulk.Dbl(r"AMMONIA",r"WATER").Value=C1res[9][i]; Bulk.Dbl(r"WATER",r"AMMONIA").Value=C1res[10][i]; Bulk.Dbl(r"WATER",r"WATER").Value=C1res[11][i];
    Bulk.Cpbg.Value=C1res[12][i]; Bulk.Cpbl.Value=C1res[13][i]; Bulk.kappabg.Value=C1res[14][i]; Bulk.kappabl.Value=C1res[15][i]; Bulk.mubg.Value=C1res[16][i]; Bulk.mubl.Value=C1res[17][i];
    Bulk.sigmabl.Value=C1res[18][i]; Bulk.Uspg.Value=C1res[19][i]; Bulk.Uspl.Value=C1res[20][i]; Bulk.MWg.Value=C1res[21][i]; Bulk.MWl.Value=C1res[22][i]; Bulk.Scg.Value=C1res[23][i]; 
    Bulk.Scl.Value=C1res[24][i]; Bulk.Regc.Value=C1res[25][i]; Bulk.Relc.Value=C1res[26][i]; Bulk.Wel.Value=C1res[27][i]; Bulk.Frlc.Value=C1res[28][i]; Bulk.kbmg.Value=C1res[29][i];
    Bulk.kbml.Value=C1res[30][i]; Bulk.khg.Value=C1res[31][i]; Bulk.khl.Value=C1res[32][i]; Bulk.aef.Value=C1res[33][i]; Bulk.hbg.Value=C1res[34][i]; Bulk.hbl.Value=C1res[35][i]; 
    Bulk.cabl(r"AMMONIA").Value=C1res[36][i]; Bulk.cabl(r"WATER").Value=C1res[37][i]; Bulk.yba(r"AMMONIA").Value=C1res[38][i]; Bulk.yba(r"WATER").Value=C1res[39][i]; 
    Bulk.xba(r"AMMONIA").Value=C1res[40][i]; Bulk.xba(r"WATER").Value=C1res[41][i]; Bulk.ybd(r"AMMONIA").Value=C1res[42][i]; Bulk.ybd(r"WATER").Value=C1res[43][i]; 
    Bulk.xbd(r"AMMONIA").Value=C1res[44][i]; Bulk.xbd(r"WATER").Value=C1res[45][i]; Bulk.hga.Value=C1res[46][i]; Bulk.hla.Value=C1res[47][i]; Bulk.hgd.Value=C1res[48][i]; Bulk.hld.Value=C1res[49][i];
    Bulk.cala(r"AMMONIA").Value=C1res[50][i]; Bulk.cala(r"WATER").Value=C1res[51][i]; Bulk.cald(r"AMMONIA").Value=C1res[52][i]; Bulk.cald(r"WATER").Value=C1res[53][i]; Bulk.ubg.Value=C1res[54][i];
    Bulk.ubl.Value=C1res[55][i]; Bulk.Gammabl.Value=C1res[56][i]; Bulk.hpabg.Value=C1res[57][i]; Bulk.hpwbg.Value=C1res[58][i]; Bulk.hpabl.Value=C1res[59][i]; Bulk.hpwbl.Value=C1res[60][i];
    Bulk.Regp.Value=C1res[61][i]; Bulk.Frlp.Value=C1res[62][i]; Bulk.Hpr.Value=C1res[63][i]; Bulk.FSt.Value=C1res[64][i]; Bulk.CSt.Value=C1res[65][i]; Bulk.dPdry.Value=C1res[66][i]; Bulk.H.Value=C1res[67][i];
    Bulk.dPirr.Value=C1res[68][i]; Bulk.Nas.Value=C1res[69][i]; Bulk.Nts.Value=C1res[70][i]; Bulk.Es.Value=C1res[71][i]; Bulk.TI.Value=C1res[72][i]; Bulk.yI(r"AMMONIA").Value=C1res[73][i]; Bulk.yI(r"WATER").Value=C1res[74][i];
    Bulk.xI(r"AMMONIA").Value=C1res[75][i]; Bulk.xI(r"WATER").Value=C1res[76][i]; Bulk.phiIg(r"AMMONIA").Value=C1res[77][i]; Bulk.phiIg(r"WATER").Value=C1res[78][i]; 
    Bulk.phiIl(r"AMMONIA").Value=C1res[79][i]; Bulk.phiIl(r"WATER").Value=C1res[80][i]; Sim.Run(True);
    C1res[0][i]=Bulk.hsg.Value; C1res[1][i]=Bulk.hsl.Value; C1res[2][i]=Bulk.rhobg.Value; C1res[3][i]=Bulk.rhobl.Value;
    C1res[4][i]=Bulk.Dbg(r"AMMONIA",r"AMMONIA").Value; C1res[5][i]=Bulk.Dbg(r"AMMONIA",r"WATER").Value; C1res[6][i]=Bulk.Dbg(r"WATER",r"AMMONIA").Value; C1res[7][i]=Bulk.Dbg(r"WATER",r"WATER").Value;
    C1res[8][i]=Bulk.Dbl(r"AMMONIA",r"AMMONIA").Value; C1res[9][i]=Bulk.Dbl(r"AMMONIA",r"WATER").Value; C1res[10][i]=Bulk.Dbl(r"WATER",r"AMMONIA").Value; C1res[11][i]=Bulk.Dbl(r"WATER",r"WATER").Value;
    C1res[12][i]=Bulk.Cpbg.Value; C1res[13][i]=Bulk.Cpbl.Value; C1res[14][i]=Bulk.kappabg.Value; C1res[15][i]=Bulk.kappabl.Value; C1res[16][i]=Bulk.mubg.Value; C1res[17][i]=Bulk.mubl.Value;
    C1res[18][i]=Bulk.sigmabl.Value; C1res[19][i]=Bulk.Uspg.Value; C1res[20][i]=Bulk.Uspl.Value; C1res[21][i]=Bulk.MWg.Value; C1res[22][i]=Bulk.MWl.Value; C1res[23][i]=Bulk.Scg.Value; 
    C1res[24][i]=Bulk.Scl.Value; C1res[25][i]=Bulk.Regc.Value; C1res[26][i]=Bulk.Relc.Value; C1res[27][i]=Bulk.Wel.Value; C1res[28][i]=Bulk.Frlc.Value; C1res[29][i]=Bulk.kbmg.Value;
    C1res[30][i]=Bulk.kbml.Value; C1res[31][i]=Bulk.khg.Value; C1res[32][i]=Bulk.khl.Value; C1res[33][i]=Bulk.aef.Value; C1res[34][i]=Bulk.hbg.Value; C1res[35][i]=Bulk.hbl.Value; 
    C1res[36][i]=Bulk.cabl(r"AMMONIA").Value; C1res[37][i]=Bulk.cabl(r"WATER").Value; C1res[38][i]=Bulk.yba(r"AMMONIA").Value; C1res[39][i]=Bulk.yba(r"WATER").Value; 
    C1res[40][i]=Bulk.xba(r"AMMONIA").Value; C1res[41][i]=Bulk.xba(r"WATER").Value; C1res[42][i]=Bulk.ybd(r"AMMONIA").Value; C1res[43][i]=Bulk.ybd(r"WATER").Value; 
    C1res[44][i]=Bulk.xbd(r"AMMONIA").Value; C1res[45][i]=Bulk.xbd(r"WATER").Value; C1res[46][i]=Bulk.hga.Value; C1res[47][i]=Bulk.hla.Value; C1res[48][i]=Bulk.hgd.Value; C1res[49][i]=Bulk.hld.Value;
    C1res[50][i]=Bulk.cala(r"AMMONIA").Value; C1res[51][i]=Bulk.cala(r"WATER").Value; C1res[52][i]=Bulk.cald(r"AMMONIA").Value; C1res[53][i]=Bulk.cald(r"WATER").Value; C1res[54][i]=Bulk.ubg.Value;
    C1res[55][i]=Bulk.ubl.Value; C1res[56][i]=Bulk.Gammabl.Value; C1res[57][i]=Bulk.hpabg.Value; C1res[58][i]=Bulk.hpwbg.Value; C1res[59][i]=Bulk.hpabl.Value; C1res[60][i]=Bulk.hpwbl.Value;
    C1res[61][i]=Bulk.Regp.Value; C1res[62][i]=Bulk.Frlp.Value; C1res[63][i]=Bulk.Hpr.Value; C1res[64][i]=Bulk.FSt.Value; C1res[65][i]=Bulk.CSt.Value; C1res[66][i]=Bulk.dPdry.Value; C1res[67][i]=Bulk.H.Value;
    C1res[68][i]=Bulk.dPirr.Value; C1res[69][i]=Bulk.Nas.Value; C1res[70][i]=Bulk.Nts.Value; C1res[71][i]=Bulk.Es.Value; C1res[72][i]=Bulk.TI.Value; C1res[73][i]=Bulk.yI(r"AMMONIA").Value; C1res[74][i]=Bulk.yI(r"WATER").Value;
    C1res[75][i]=Bulk.xI(r"AMMONIA").Value; C1res[76][i]=Bulk.xI(r"WATER").Value; C1res[77][i]=Bulk.phiIg(r"AMMONIA").Value; C1res[78][i]=Bulk.phiIg(r"WATER").Value; 
    C1res[79][i]=Bulk.phiIl(r"AMMONIA").Value; C1res[80][i]=Bulk.phiIl(r"WATER").Value; C1res[81][i]=Bulk.Msg.Value; C1res[82][i]=Bulk.Msl.Value; C1res[83][i]=Bulk.Msga.Value; C1res[84][i]=Bulk.Msla.Value;
    C1res[85][i]=Bulk.Msgu.Value; C1res[86][i]=Bulk.Mslu.Value;
ACM.quit(); 
# Calcular propiedades de E-1
print("E-1");
ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"E1.dynf")); Sim=ACM.Simulation; E1=Sim.Flowsheet.Blocks(r"E-1"); LV1=Sim.Flowsheet.Blocks(r"LV-1");
E1.hE_HF_in.Value=hE_HF_in; E1.hE_HF_out.Value=hE_HF_out; E1.hE_CF_in.Value=hE_CF_in; E1.hE_CF_out.Value=hE_CF_out;
E1.E_HF_in.F.Value=E_HF_inF; E1.E_HF_in.T.Value=E_HF_inT; E1.E_HF_in.P.Value=E_HF_inP; E1.E_HF_in.z(r"AMMONIA").Value=E_HF_inza; E1.E_HF_in.z(r"WATER").Value=E_HF_inzw;
E1.E_HF_out.F.Value=E_HF_outF; E1.E_HF_out.T.Value=E_HF_outT; E1.E_HF_out.P.Value=E_HF_outP; E1.E_HF_out.z(r"AMMONIA").Value=E_HF_outza; E1.E_HF_out.z(r"WATER").Value=E_HF_outzw;
LV1.VIb_in.F.Value=E_HF_outF; LV1.VIb_in.T.Value=E_HF_outT; LV1.VIb_in.P.Value=E_HF_outP; LV1.VIb_in.z(r"AMMONIA").Value=E_HF_outza; LV1.VIb_in.z(r"WATER").Value=E_HF_outzw;
E1.E_CF_in.F.Value=E_CF_inF; E1.E_CF_in.T.Value=E_CF_inT; E1.E_CF_in.P.Value=E_CF_inP; E1.E_CF_in.z(r"AMMONIA").Value=E_CF_inza; E1.E_CF_in.z(r"WATER").Value=E_CF_inzw;
E1.E_CF_out.F.Value=E_CF_outF; E1.E_CF_out.T.Value=E_CF_outT; E1.E_CF_out.P.Value=E_CF_outP; E1.E_CF_out.z(r"AMMONIA").Value=E_CF_outza; E1.E_CF_out.z(r"WATER").Value=E_CF_outzw;
E1.dT1.Value=E1Est[0][0]; E1.dT2.Value=E1Est[1][0]; E1.dTln.Value=E1Est[2][0]; E1.RF.Value=E1Est[3][0]; E1.PF.Value=E1Est[4][0]; E1.alphaF.Value=E1Est[5][0];
E1.SF.Value=E1Est[6][0]; E1.F.Value=E1Est[7][0]; E1.MWint.Value=E1Est[8][0]; E1.muint.Value=E1Est[9][0]; E1Est[10][0]=E1.Cpint.Value; E1Est[11][0]=E1.kappaint.Value;
E1.Re_int.Value=E1Est[12][0]; E1.Pr_int.Value=E1Est[13][0]; E1.Nu_int.Value=E1Est[14][0]; E1.hint.Value=E1Est[15][0]; E1.a1.Value=E1Est[16][0]; E1.a2.Value=E1Est[17][0]; 
E1.aBD.Value=E1Est[18][0]; E1.MWext.Value=E1Est[19][0]; E1.muext.Value=E1Est[20][0]; E1.Cpext.Value=E1Est[21][0]; E1.kappaext.Value=E1Est[22][0]; E1.Re_ext.Value=E1Est[23][0]; 
E1.Pr_ext.Value=E1Est[24][0]; E1.jH.Value=E1Est[25][0]; E1.Afc.Value=E1Est[26][0]; E1.hext.Value=E1Est[27][0]; E1.U.Value=E1Est[28][0]; E1.QE.Q.Value=E1Est[29][0]; LV1.vp.Value=vpLV1[caso]; Sim.Run(True);
E1Est[0][0]=E1.dT1.Value; E1Est[1][0]=E1.dT2.Value; E1Est[2][0]=E1.dTln.Value; E1Est[3][0]=E1.RF.Value; E1Est[4][0]=E1.PF.Value; E1Est[5][0]=E1.alphaF.Value;
E1Est[6][0]=E1.SF.Value; E1Est[7][0]=E1.F.Value; E1Est[8][0]=E1.MWint.Value; E1Est[9][0]=E1.muint.Value; E1Est[10][0]=E1.Cpint.Value; E1Est[11][0]=E1.kappaint.Value;
E1Est[12][0]=E1.Re_int.Value; E1Est[13][0]=E1.Pr_int.Value; E1Est[14][0]=E1.Nu_int.Value; E1Est[15][0]=E1.hint.Value; E1Est[16][0]=E1.a1.Value; E1Est[17][0]=E1.a2.Value; 
E1Est[18][0]=E1.aBD.Value; E1Est[19][0]=E1.MWext.Value; E1Est[20][0]=E1.muext.Value; E1Est[21][0]=E1.Cpext.Value; E1Est[22][0]=E1.kappaext.Value; E1Est[23][0]=E1.Re_ext.Value; 
E1Est[24][0]=E1.Pr_ext.Value; E1Est[25][0]=E1.jH.Value; E1Est[26][0]=E1.Afc.Value; E1Est[27][0]=E1.hext.Value; E1Est[28][0]=E1.U.Value; E1Est[29][0]=E1.QE.Q.Value;
E1Din[0][0]=E1.Ml_E_CF.Value; E1Din[1][0]=E1.Tl_E_CF.Value; E1Din[2][0]=E1.Pl_E_CF.Value; E1Din[3][0]=E1.x_E_CF(r"AMMONIA").Value; E1Din[4][0]=E1.x_E_CF(r"WATER").Value;
E1Din[5][0]=E1.Ml_E_HF.Value; E1Din[6][0]=E1.Tl_E_HF.Value; E1Din[7][0]=E1.Pl_E_HF.Value; E1Din[8][0]=E1.x_E_HF(r"AMMONIA").Value; E1Din[9][0]=E1.x_E_HF(r"WATER").Value;
E1Din[10][0]=E1.rholCF.Value; E1Din[11][0]=E1.hlCF.Value; E1Din[12][0]=E1.ulCF.Value; E1Din[13][0]=E1.rholHF.Value; E1Din[14][0]=E1.hlHF.Value; E1Din[15][0]=E1.ulHF.Value; 
E1Din[16][0]=E1.MulCF.Value; E1Din[17][0]=LV1.q.Value; E1Din[18][0]=LV1.rho_CF.Value; vpLV1[caso]=LV1.vp.Value; ACM.quit(); 
# Calcular propiedades de Thermosiphon
print("Thermosiphon");
ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"Thermosiphon.dynf")); Sim=ACM.Simulation; Thermosiphon=Sim.Flowsheet.Blocks(r"Thermosiphon");
Thermosiphon.hR_CF_out.Value=hR_CF_out; Thermosiphon.hE_HF_in.Value=hE_HF_in;
Thermosiphon.R_CF_out.F.Value=R_CF_outF; Thermosiphon.R_CF_out.T.Value=R_CF_outT; Thermosiphon.R_CF_out.P.Value=R_CF_outP; Thermosiphon.R_CF_out.z(r"AMMONIA").Value=R_CF_outza; Thermosiphon.R_CF_out.z(r"WATER").Value=R_CF_outzw;
Thermosiphon.E_HF_in.F.Value=E_HF_inF; Thermosiphon.E_HF_in.T.Value=E_HF_inT; Thermosiphon.E_HF_in.P.Value=E_HF_inP; Thermosiphon.E_HF_in.z(r"AMMONIA").Value=E_HF_inza; Thermosiphon.E_HF_in.z(r"WATER").Value=E_HF_inzw;
Thermosiphon.Liq_s_ps1pps2m3.F.Value=Liq_s_ps1pps2m3F; Thermosiphon.Liq_s_ps1pps2m3.T.Value=Liq_s_ps1pps2m3T; Thermosiphon.Liq_s_ps1pps2m3.P.Value=Liq_s_ps1pps2m3P; Thermosiphon.Liq_s_ps1pps2m3.z(r"AMMONIA").Value=Liq_s_ps1pps2m3za; Thermosiphon.Liq_s_ps1pps2m3.z(r"WATER").Value=Liq_s_ps1pps2m3zw;
Thermosiphon.hLiq_s_ps1pps2m3.Value=TEst[0][0]; Thermosiphon.hLiq_s_ps1pps2m2.Value=TEst[1][0]; Thermosiphon.Liq_s_ps1pps2m2F.Value=TEst[2][0]; Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value=TEst[3][0];
Thermosiphon.Liq_s_ps1pps2m2z(r"WATER").Value=TEst[4][0]; Thermosiphon.Liq_s_ps1pps2m2P.Value=TEst[5][0]; Thermosiphon.Liq_s_ps1pps2m2T.Value=TEst[6][0];
Thermosiphon.rhoLiq_s_ps1pps2m2.Value=TEst[7][0]; Thermosiphon.MWLiq_s_ps1pps2m2.Value=TEst[8][0]; Thermosiphon.z.Value=TEst[9][0]; Thermosiphon.QR.Q.Value=TEst[10][0]; 
Thermosiphon.R_HF_in.T.Value=TT6[caso]; Thermosiphon.R_HF_out.F.Value=FIC1[caso]; Thermosiphon.R_HF_in.P.Value=P_R_HF; Sim.Run(True);
TEst[0][0]=Thermosiphon.hLiq_s_ps1pps2m3.Value; TEst[1][0]=Thermosiphon.hLiq_s_ps1pps2m2.Value; TEst[2][0]=Thermosiphon.Liq_s_ps1pps2m2F.Value; TEst[3][0]=Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value;
TEst[4][0]=Thermosiphon.Liq_s_ps1pps2m2z(r"WATER").Value; TEst[5][0]=Thermosiphon.Liq_s_ps1pps2m2P.Value; TEst[6][0]=Thermosiphon.Liq_s_ps1pps2m2T.Value;
TEst[7][0]=Thermosiphon.rhoLiq_s_ps1pps2m2.Value; TEst[8][0]=Thermosiphon.MWLiq_s_ps1pps2m2.Value; TEst[9][0]=Thermosiphon.z.Value; TEst[10][0]=Thermosiphon.QR.Q.Value; 
R_HF_inF=Thermosiphon.R_HF_in.F.Value; R_HF_inT=Thermosiphon.R_HF_in.T.Value; R_HF_inP=Thermosiphon.R_HF_in.P.Value;
R_HF_outF=Thermosiphon.R_HF_out.F.Value; R_HF_outT=Thermosiphon.R_HF_out.T.Value; R_HF_outP=Thermosiphon.R_HF_out.P.Value;
TDin[0][0]=Thermosiphon.hR_HF_in.Value; TDin[1][0]=Thermosiphon.hR_HF_out.Value; TDin[2][0]=Thermosiphon.Vl_S.Value; TDin[3][0]=Thermosiphon.Vl_R_CF.Value;
TDin[4][0]=Thermosiphon.LT1.Value; TDin[5][0]=Thermosiphon.Ml_S.Value; TDin[6][0]=Thermosiphon.Tl_S.Value; TDin[7][0]=Thermosiphon.Pl_S.Value; TDin[8][0]=Thermosiphon.x_S(r"AMMONIA").Value;
TDin[9][0]=Thermosiphon.x_S(r"WATER").Value; TDin[10][0]=Thermosiphon.Mg_S.Value; TDin[11][0]=Thermosiphon.Tg_S.Value; TDin[12][0]=Thermosiphon.Pg_S.Value;
TDin[13][0]=Thermosiphon.y_S(r"AMMONIA").Value; TDin[14][0]=Thermosiphon.y_S(r"WATER").Value; TDin[15][0]=Thermosiphon.Ml_R_CF.Value; TDin[16][0]=Thermosiphon.Tl_R_CF.Value;
TDin[17][0]=Thermosiphon.Pl_R_CF.Value; TDin[18][0]=Thermosiphon.x_R_CF(r"AMMONIA").Value; TDin[19][0]=Thermosiphon.x_R_CF(r"WATER").Value;
TDin[20][0]=Thermosiphon.Mg_R_CF.Value; TDin[21][0]=Thermosiphon.Tg_R_CF.Value; TDin[22][0]=Thermosiphon.Pg_R_CF.Value; TDin[23][0]=Thermosiphon.y_R_CF(r"AMMONIA").Value;
TDin[24][0]=Thermosiphon.y_R_CF(r"WATER").Value; TDin[25][0]=Thermosiphon.rholS.Value; TDin[26][0]=Thermosiphon.rhogS.Value; TDin[27][0]=Thermosiphon.rholCF.Value;
TDin[28][0]=Thermosiphon.rhogCF.Value; TDin[29][0]=Thermosiphon.hlS.Value; TDin[30][0]=Thermosiphon.hgS.Value; TDin[31][0]=Thermosiphon.hlCF.Value;
TDin[32][0]=Thermosiphon.hgCF.Value; TDin[33][0]=Thermosiphon.ulS.Value; TDin[34][0]=Thermosiphon.ugS.Value; TDin[35][0]=Thermosiphon.ulCF.Value;
TDin[36][0]=Thermosiphon.ugCF.Value; TDin[37][0]=Thermosiphon.MT.Value; TDin[38][0]=Thermosiphon.MzT.Value; TDin[39][0]=Thermosiphon.MuT.Value;
TDin[40][0]=Thermosiphon.MRCF.Value; TDin[41][0]=Thermosiphon.MuRCF.Value; ACM.quit(); 
# Calcular propiedades de E-3 y Divisor
print("E-3 y Divisor");
ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"E3.dynf")); Sim=ACM.Simulation; E3=Sim.Flowsheet.Blocks(r"E-3"); Divisor=Sim.Flowsheet.Blocks(r"Divisor"); PV2=Sim.Flowsheet.Blocks(r"PV-2");
E3.hVap_s_2.Value=hVap_s_2; E3.hC_HF_out.Value=hC_HF_out; E3.hC_CF_in.Value=hC_CF_in; E3.hC_CF_out.Value=hC_CF_out;
E3.Vap_s_2.F.Value=Vap_s_2F; E3.Vap_s_2.T.Value=Vap_s_2T; E3.Vap_s_2.P.Value=Vap_s_2P; E3.Vap_s_2.z(r"AMMONIA").Value=Vap_s_2za; E3.Vap_s_2.z(r"WATER").Value=Vap_s_2zw;
Divisor.Reflujo.F.Value=ReflujoF; Divisor.Reflujo.T.Value=ReflujoT; Divisor.Reflujo.P.Value=ReflujoP; Divisor.Reflujo.z(r"AMMONIA").Value=Reflujoza; Divisor.Reflujo.z(r"WATER").Value=Reflujozw;
E3.C_HF_out.F.Value=C_HF_outF; E3.C_HF_out.T.Value=C_HF_outT; E3.C_HF_out.P.Value=C_HF_outP; E3.C_HF_out.z(r"AMMONIA").Value=C_HF_outza; E3.C_HF_out.z(r"WATER").Value=C_HF_outzw;
Divisor.C_HF_out.F.Value=C_HF_outF; Divisor.C_HF_out.T.Value=C_HF_outT; Divisor.C_HF_out.P.Value=C_HF_outP; Divisor.C_HF_out.z(r"AMMONIA").Value=C_HF_outza; Divisor.C_HF_out.z(r"WATER").Value=C_HF_outzw;
E3.C_CF_in.F.Value=C_CF_inF; E3.C_CF_in.T.Value=C_CF_inT; E3.C_CF_in.P.Value=C_CF_inP; E3.C_CF_in.z(r"AMMONIA").Value=C_CF_inza; E3.C_CF_in.z(r"WATER").Value=C_CF_inzw;
E3.C_CF_out.F.Value=C_CF_outF; E3.C_CF_out.T.Value=C_CF_outT; E3.C_CF_out.P.Value=C_CF_outP; E3.C_CF_out.z(r"AMMONIA").Value=C_CF_outza; E3.C_CF_out.z(r"WATER").Value=C_CF_outzw;
PV2.VIb_in.F.Value=C_CF_outF; PV2.VIb_in.T.Value=C_CF_outT; PV2.VIb_in.P.Value=C_CF_outP; PV2.VIb_in.z(r"AMMONIA").Value=C_CF_outza; PV2.VIb_in.z(r"WATER").Value=C_CF_outzw;
Divisor.Prod_Liq.F.Value=Prod_LiqF; Divisor.Prod_Liq.T.Value=Prod_LiqT; Divisor.Prod_Liq.P.Value=Prod_LiqP; Divisor.Prod_Liq.z(r"AMMONIA").Value=Prod_Liqza; Divisor.Prod_Liq.z(r"WATER").Value=Prod_Liqzw; 
E3.QC.Q.Value=E3DEst[0][0]; Divisor.RR.Value=E3DEst[1][0]; Divisor.rhoProd_Liq.Value=E3DEst[2][0]; Divisor.Prod_Liqq.Value=E3DEst[3][0]; E3.dT1.Value=E3DEst[4][0]; E3.dT2.Value=E3DEst[5][0]; 
E3.dTln.Value=E3DEst[6][0]; E3.RF.Value=E3DEst[7][0]; E3.PF.Value=E3DEst[8][0]; E3.alphaF.Value=E3DEst[9][0]; E3.SF.Value=E3DEst[10][0]; E3.F.Value=E3DEst[11][0]; PV2.vp.Value=vpPV2[caso]; Sim.Run(True); 
E3DEst[0][0]=E3.QC.Q.Value; E3DEst[1][0]=Divisor.RR.Value; E3DEst[2][0]=Divisor.rhoProd_Liq.Value; E3DEst[3][0]=Divisor.Prod_Liqq.Value; E3DEst[4][0]=E3.dT1.Value; E3DEst[5][0]=E3.dT2.Value; 
E3DEst[6][0]=E3.dTln.Value; E3DEst[7][0]=E3.RF.Value; E3DEst[8][0]=E3.PF.Value; E3DEst[9][0]=E3.alphaF.Value; E3DEst[10][0]=E3.SF.Value; E3DEst[11][0]=E3.F.Value;
E3DDin[0][0]=E3.Ml_C_CF.Value; E3DDin[1][0]=E3.Tl_C_CF.Value; E3DDin[2][0]=E3.Pl_C_CF.Value; E3DDin[3][0]=E3.x_C_CF(r"AMMONIA").Value; E3DDin[4][0]=E3.x_C_CF(r"WATER").Value;
E3DDin[5][0]=E3.Mg_C_HF.Value; E3DDin[6][0]=E3.Tg_C_HF.Value; E3DDin[7][0]=E3.Pg_C_HF.Value; E3DDin[8][0]=E3.y_C_HF(r"AMMONIA").Value; E3DDin[9][0]=E3.y_C_HF(r"WATER").Value;
E3DDin[10][0]=E3.rholCF.Value; E3DDin[11][0]=E3.hlCF.Value; E3DDin[12][0]=E3.ulCF.Value; E3DDin[13][0]=E3.rhogHF.Value; E3DDin[14][0]=E3.hgHF.Value; E3DDin[15][0]=E3.ugHF.Value;
E3DDin[16][0]=E3.MugHF.Value; E3DDin[17][0]=PV2.q.Value; E3DDin[18][0]=PV2.rho_CF.Value; vpPV2[caso]=PV2.vp.Value; ACM.quit(); 
# Pasar propiedades a estado dinámico para pruebas en estado estacionario
ACM=win32.Dispatch(r"ACM Application"); ACM.OpenDocument(os.path.abspath(r"Dinamico_ACM_Din.dynf")); Sim=ACM.Simulation; 
C1=Sim.Flowsheet.Blocks(r"C-1"); E3=Sim.Flowsheet.Blocks(r"E-3"); Divisor=Sim.Flowsheet.Blocks(r"Divisor"); Thermosiphon=Sim.Flowsheet.Blocks(r"Thermosiphon"); E1=Sim.Flowsheet.Blocks(r"E-1"); 
LV1=Sim.Flowsheet.Blocks(r"LV-1"); PV2=Sim.Flowsheet.Blocks(r"PV-2"); print(r"Inicializar con estado estacionario el modelo dinámico:");
# C-1
print("C-1");
C1.ps1.Value=ps1; C1.ps2.Value=ps2; C1.flowmode1.Value=flowmode1; C1.flowmode2.Value=flowmode2;
for i in range(0,ps1+ps2-4):
    C1.Vs(i+2).Value=C1par[0][i]; C1.Ls(i+2).Value=C1par[1][i]; C1.Tsg(i+2).Value=C1par[2][i]; C1.Tsl(i+2).Value=C1par[3][i]; C1.Ps(i+2).Value=C1par[4][i]; 
    C1.ys(r"AMMONIA",i+2).Value=C1par[5][i]; C1.ys(r"WATER",i+2).Value=C1par[6][i]; C1.xs(r"AMMONIA",i+2).Value=C1par[7][i]; C1.xs(r"WATER",i+2).Value=C1par[8][i]; 
    C1.Vb(i+2).Value=C1par[9][i]; C1.Lb(i+2).Value=C1par[10][i]; C1.Tbg(i+2).Value=C1par[11][i]; C1.Tbl(i+2).Value=C1par[12][i]; C1.Pb(i+2).Value=C1par[13][i]; 
    C1.yb(r"AMMONIA",i+2).Value=C1par[14][i]; C1.yb(r"WATER",i+2).Value=C1par[15][i]; C1.xb(r"AMMONIA",i+2).Value=C1par[16][i]; C1.xb(r"WATER",i+2).Value=C1par[17][i]; C1.Zs(i+2).Value=C1par[18][i];
    C1.hsg(i+2).Value=C1res[0][i]; C1.hsl(i+2).Value=C1res[1][i]; C1.rhobg(i+2).Value=C1res[2][i]; C1.rhobl(i+2).Value=C1res[3][i];
    C1.Dbg(r"AMMONIA",r"AMMONIA",i+2).Value=C1res[4][i]; C1.Dbg(r"AMMONIA",r"WATER",i+2).Value=C1res[5][i]; C1.Dbg(r"WATER",r"AMMONIA",i+2).Value=C1res[6][i]; C1.Dbg(r"WATER",r"WATER",i+2).Value=C1res[7][i];
    C1.Dbl(r"AMMONIA",r"AMMONIA",i+2).Value=C1res[8][i]; C1.Dbl(r"AMMONIA",r"WATER",i+2).Value=C1res[9][i]; C1.Dbl(r"WATER",r"AMMONIA",i+2).Value=C1res[10][i]; C1.Dbl(r"WATER",r"WATER",i+2).Value=C1res[11][i];
    C1.Cpbg(i+2).Value=C1res[12][i]; C1.Cpbl(i+2).Value=C1res[13][i]; C1.kappabg(i+2).Value=C1res[14][i]; C1.kappabl(i+2).Value=C1res[15][i]; C1.mubg(i+2).Value=C1res[16][i]; C1.mubl(i+2).Value=C1res[17][i];
    C1.sigmabl(i+2).Value=C1res[18][i]; C1.Uspg(i+2).Value=C1res[19][i]; C1.Uspl(i+2).Value=C1res[20][i]; C1.MWg(i+2).Value=C1res[21][i]; C1.MWl(i+2).Value=C1res[22][i]; C1.Scg(i+2).Value=C1res[23][i]; 
    C1.Scl(i+2).Value=C1res[24][i]; C1.Regc(i+2).Value=C1res[25][i]; C1.Relc(i+2).Value=C1res[26][i]; C1.Wel(i+2).Value=C1res[27][i]; C1.Frlc(i+2).Value=C1res[28][i]; C1.kbmg(i+2).Value=C1res[29][i];
    C1.kbml(i+2).Value=C1res[30][i]; C1.khg(i+2).Value=C1res[31][i]; C1.khl(i+2).Value=C1res[32][i]; C1.aef(i+2).Value=C1res[33][i]; C1.hbg(i+2).Value=C1res[34][i]; C1.hbl(i+2).Value=C1res[35][i]; 
    C1.cabl(r"AMMONIA",i+2).Value=C1res[36][i]; C1.cabl(r"WATER",i+2).Value=C1res[37][i]; C1.yba(r"AMMONIA",i+2).Value=C1res[38][i]; C1.yba(r"WATER",i+2).Value=C1res[39][i]; 
    C1.xba(r"AMMONIA",i+2).Value=C1res[40][i]; C1.xba(r"WATER",i+2).Value=C1res[41][i]; C1.ybd(r"AMMONIA",i+2).Value=C1res[42][i]; C1.ybd(r"WATER",i+2).Value=C1res[43][i]; 
    C1.xbd(r"AMMONIA",i+2).Value=C1res[44][i]; C1.xbd(r"WATER",i+2).Value=C1res[45][i]; C1.hga(i+2).Value=C1res[46][i]; C1.hla(i+2).Value=C1res[47][i]; C1.hgd(i+2).Value=C1res[48][i]; C1.hld(i+2).Value=C1res[49][i];
    C1.cala(r"AMMONIA",i+2).Value=C1res[50][i]; C1.cala(r"WATER",i+2).Value=C1res[51][i]; C1.cald(r"AMMONIA",i+2).Value=C1res[52][i]; C1.cald(r"WATER",i+2).Value=C1res[53][i]; C1.ubg(i+2).Value=C1res[54][i];
    C1.ubl(i+2).Value=C1res[55][i]; C1.Gammabl(i+2).Value=C1res[56][i]; C1.hpabg(i+2).Value=C1res[57][i]; C1.hpwbg(i+2).Value=C1res[58][i]; C1.hpabl(i+2).Value=C1res[59][i]; C1.hpwbl(i+2).Value=C1res[60][i];
    C1.Regp(i+2).Value=C1res[61][i]; C1.Frlp(i+2).Value=C1res[62][i]; C1.Hpr(i+2).Value=C1res[63][i]; C1.FSt(i+2).Value=C1res[64][i]; C1.CSt(i+2).Value=C1res[65][i]; C1.dPdry(i+2).Value=C1res[66][i]; C1.H(i+2).Value=C1res[67][i];
    C1.dPirr(i+2).Value=C1res[68][i]; C1.Nas(i+2).Value=C1res[69][i]; C1.Nts(i+2).Value=C1res[70][i]; C1.Es(i+2).Value=C1res[71][i]; C1.TI(i+2).Value=C1res[72][i]; C1.yI(r"AMMONIA",i+2).Value=C1res[73][i]; C1.yI(r"WATER",i+2).Value=C1res[74][i];
    C1.xI(r"AMMONIA",i+2).Value=C1res[75][i]; C1.xI(r"WATER",i+2).Value=C1res[76][i]; C1.phiIg(r"AMMONIA",i+2).Value=C1res[77][i]; C1.phiIg(r"WATER",i+2).Value=C1res[78][i]; 
    C1.phiIl(r"AMMONIA",i+2).Value=C1res[79][i]; C1.phiIl(r"WATER",i+2).Value=C1res[80][i]; C1.Msg(i+2).Value=C1res[81][i]; C1.Msl(i+2).Value=C1res[82][i]; C1.Msga(i+2).Value=C1res[83][i]; C1.Msla(i+2).Value=C1res[84][i];
    C1.Msgu(i+2).Value=C1res[85][i]; C1.Mslu(i+2).Value=C1res[86][i];
C1.hReflujo.Value=hReflujo; C1.hR_CF_out.Value=hR_CF_out; C1.hE_CF_out.Value=hE_CF_out; 
C1.Vap_s_2.F.Value=Vap_s_2F; C1.Vap_s_2.T.Value=Vap_s_2T; C1.Vap_s_2.P.Value=Vap_s_2P; C1.Vap_s_2.z(r"AMMONIA").Value=Vap_s_2za; C1.Vap_s_2.z(r"WATER").Value=Vap_s_2zw;
E3.Vap_s_2.F.Value=Vap_s_2F; E3.Vap_s_2.T.Value=Vap_s_2T; E3.Vap_s_2.P.Value=Vap_s_2P; E3.Vap_s_2.z(r"AMMONIA").Value=Vap_s_2za; E3.Vap_s_2.z(r"WATER").Value=Vap_s_2zw;
C1.Reflujo.F.Value=ReflujoF; C1.Reflujo.T.Value=ReflujoT; C1.Reflujo.P.Value=ReflujoP; C1.Reflujo.z(r"AMMONIA").Value=Reflujoza; C1.Reflujo.z(r"WATER").Value=Reflujozw;
Divisor.Reflujo.F.Value=ReflujoF; Divisor.Reflujo.T.Value=ReflujoT; Divisor.Reflujo.P.Value=ReflujoP; Divisor.Reflujo.z(r"AMMONIA").Value=Reflujoza; Divisor.Reflujo.z(r"WATER").Value=Reflujozw;
C1.R_CF_out.F.Value=R_CF_outF; C1.R_CF_out.T.Value=R_CF_outT; C1.R_CF_out.P.Value=R_CF_outP; C1.R_CF_out.z(r"AMMONIA").Value=R_CF_outza; C1.R_CF_out.z(r"WATER").Value=R_CF_outzw;
Thermosiphon.R_CF_out.F.Value=R_CF_outF; Thermosiphon.R_CF_out.T.Value=R_CF_outT; Thermosiphon.R_CF_out.P.Value=R_CF_outP; Thermosiphon.R_CF_out.z(r"AMMONIA").Value=R_CF_outza; Thermosiphon.R_CF_out.z(r"WATER").Value=R_CF_outzw;
C1.Liq_s_ps1pps2m3.F.Value=Liq_s_ps1pps2m3F; C1.Liq_s_ps1pps2m3.T.Value=Liq_s_ps1pps2m3T; C1.Liq_s_ps1pps2m3.P.Value=Liq_s_ps1pps2m3P; C1.Liq_s_ps1pps2m3.z(r"AMMONIA").Value=Liq_s_ps1pps2m3za; C1.Liq_s_ps1pps2m3.z(r"WATER").Value=Liq_s_ps1pps2m3zw;
Thermosiphon.Liq_s_ps1pps2m3.F.Value=Liq_s_ps1pps2m3F; Thermosiphon.Liq_s_ps1pps2m3.T.Value=Liq_s_ps1pps2m3T; Thermosiphon.Liq_s_ps1pps2m3.P.Value=Liq_s_ps1pps2m3P; Thermosiphon.Liq_s_ps1pps2m3.z(r"AMMONIA").Value=Liq_s_ps1pps2m3za; Thermosiphon.Liq_s_ps1pps2m3.z(r"WATER").Value=Liq_s_ps1pps2m3zw;
C1.E_CF_out.F.Value=E_CF_outF; C1.E_CF_out.T.Value=E_CF_outT; C1.E_CF_out.P.Value=E_CF_outP; C1.E_CF_out.z(r"AMMONIA").Value=E_CF_outza; C1.E_CF_out.z(r"WATER").Value=E_CF_outzw;
E1.E_CF_out.F.Value=E_CF_outF; E1.E_CF_out.T.Value=E_CF_outT; E1.E_CF_out.P.Value=E_CF_outP; E1.E_CF_out.z(r"AMMONIA").Value=E_CF_outza; E1.E_CF_out.z(r"WATER").Value=E_CF_outzw;
# E-1
print("E-1");
E1.hE_HF_in.Value=hE_HF_in; E1.hE_HF_out.Value=hE_HF_out; E1.hE_CF_in.Value=hE_CF_in; E1.hE_CF_out.Value=hE_CF_out;
E1.E_HF_in.F.Value=E_HF_inF; E1.E_HF_in.T.Value=E_HF_inT; E1.E_HF_in.P.Value=E_HF_inP; E1.E_HF_in.z(r"AMMONIA").Value=E_HF_inza; E1.E_HF_in.z(r"WATER").Value=E_HF_inzw;
Thermosiphon.E_HF_in.F.Value=E_HF_inF; Thermosiphon.E_HF_in.T.Value=E_HF_inT; Thermosiphon.E_HF_in.P.Value=E_HF_inP; Thermosiphon.E_HF_in.z(r"AMMONIA").Value=E_HF_inza; Thermosiphon.E_HF_in.z(r"WATER").Value=E_HF_inzw;
E1.E_HF_out.F.Value=E_HF_outF; E1.E_HF_out.T.Value=E_HF_outT; E1.E_HF_out.P.Value=E_HF_outP; E1.E_HF_out.z(r"AMMONIA").Value=E_HF_outza; E1.E_HF_out.z(r"WATER").Value=E_HF_outzw;
LV1.VIb_in.F.Value=E_HF_outF; LV1.VIb_in.T.Value=E_HF_outT; LV1.VIb_in.P.Value=E_HF_outP; LV1.VIb_in.z(r"AMMONIA").Value=E_HF_outza; LV1.VIb_in.z(r"WATER").Value=E_HF_outzw;
E1.E_CF_in.F.Value=E_CF_inF; E1.E_CF_in.T.Value=E_CF_inT; E1.E_CF_in.P.Value=E_CF_inP; E1.E_CF_in.z(r"AMMONIA").Value=E_CF_inza; E1.E_CF_in.z(r"WATER").Value=E_CF_inzw;
E1.dT1.Value=E1Est[0][0]; E1.dT2.Value=E1Est[1][0]; E1.dTln.Value=E1Est[2][0]; E1.RF.Value=E1Est[3][0]; E1.PF.Value=E1Est[4][0]; E1.alphaF.Value=E1Est[5][0];
E1.SF.Value=E1Est[6][0]; E1.F.Value=E1Est[7][0]; E1.MWint.Value=E1Est[8][0]; E1.muint.Value=E1Est[9][0]; E1Est[10][0]=E1.Cpint.Value; E1Est[11][0]=E1.kappaint.Value;
E1.Re_int.Value=E1Est[12][0]; E1.Pr_int.Value=E1Est[13][0]; E1.Nu_int.Value=E1Est[14][0]; E1.hint.Value=E1Est[15][0]; E1.a1.Value=E1Est[16][0]; E1.a2.Value=E1Est[17][0]; 
E1.aBD.Value=E1Est[18][0]; E1.MWext.Value=E1Est[19][0]; E1.muext.Value=E1Est[20][0]; E1.Cpext.Value=E1Est[21][0]; E1.kappaext.Value=E1Est[22][0]; E1.Re_ext.Value=E1Est[23][0]; 
E1.Pr_ext.Value=E1Est[24][0]; E1.jH.Value=E1Est[25][0]; E1.Afc.Value=E1Est[26][0]; E1.hext.Value=E1Est[27][0]; E1.U.Value=E1Est[28][0]; E1.QE.Q.Value=E1Est[29][0]; LV1.vp.Value=vpLV1[caso];
E1.Ml_E_CF.Value=E1Din[0][0]; E1.Tl_E_CF.Value=E1Din[1][0]; E1.Pl_E_CF.Value=E1Din[2][0]; E1.x_E_CF(r"AMMONIA").Value=E1Din[3][0]; E1.x_E_CF(r"WATER").Value=E1Din[4][0];
E1.Ml_E_HF.Value=E1Din[5][0]; E1.Tl_E_HF.Value=E1Din[6][0]; E1.Pl_E_HF.Value=E1Din[7][0]; E1.x_E_HF(r"AMMONIA").Value=E1Din[8][0]; E1.x_E_HF(r"WATER").Value=E1Din[9][0];
E1.rholCF.Value=E1Din[10][0]; E1.hlCF.Value=E1Din[11][0]; E1.ulCF.Value=E1Din[12][0]; E1.rholHF.Value=E1Din[13][0]; E1.hlHF.Value=E1Din[14][0]; E1.ulHF.Value=E1Din[15][0]; 
E1.MulCF.Value=E1Din[16][0]; LV1.q.Value=E1Din[17][0]; LV1.rho_CF.Value=E1Din[18][0]; 
# Thermosiphon
print("Thermosiphon");
Thermosiphon.hR_CF_out.Value=hR_CF_out; Thermosiphon.hE_HF_in.Value=hE_HF_in;
Thermosiphon.hLiq_s_ps1pps2m3.Value=TEst[0][0]; Thermosiphon.hLiq_s_ps1pps2m2.Value=TEst[1][0]; Thermosiphon.Liq_s_ps1pps2m2F.Value=TEst[2][0]; Thermosiphon.Liq_s_ps1pps2m2z(r"AMMONIA").Value=TEst[3][0];
Thermosiphon.Liq_s_ps1pps2m2z(r"WATER").Value=TEst[4][0]; Thermosiphon.Liq_s_ps1pps2m2P.Value=TEst[5][0]; Thermosiphon.Liq_s_ps1pps2m2T.Value=TEst[6][0];
Thermosiphon.rhoLiq_s_ps1pps2m2.Value=TEst[7][0]; Thermosiphon.MWLiq_s_ps1pps2m2.Value=TEst[8][0]; Thermosiphon.z.Value=TEst[9][0]; Thermosiphon.QR.Q.Value=TEst[10][0]; 
Thermosiphon.R_HF_in.T.Value=TT6[caso]; Thermosiphon.R_HF_out.F.Value=FIC1[caso]; Thermosiphon.R_HF_in.P.Value=P_R_HF; 
Thermosiphon.R_HF_in.F.Value=R_HF_inF; Thermosiphon.R_HF_in.T.Value=R_HF_inT; Thermosiphon.R_HF_in.P.Value=R_HF_inP;
Thermosiphon.R_HF_out.F.Value=R_HF_outF; Thermosiphon.R_HF_out.T.Value=R_HF_outT; Thermosiphon.R_HF_out.P.Value=R_HF_outP;
Thermosiphon.hR_HF_in.Value=TDin[0][0]; Thermosiphon.hR_HF_out.Value=TDin[1][0]; Thermosiphon.Vl_S.Value=TDin[2][0]; Thermosiphon.Vl_R_CF.Value=TDin[3][0];
Thermosiphon.LT1.Value=TDin[4][0]; Thermosiphon.Ml_S.Value=TDin[5][0]; Thermosiphon.Tl_S.Value=TDin[6][0]; Thermosiphon.Pl_S.Value=TDin[7][0]; Thermosiphon.x_S(r"AMMONIA").Value=TDin[8][0];
Thermosiphon.x_S(r"WATER").Value=TDin[9][0]; Thermosiphon.Mg_S.Value=TDin[10][0]; Thermosiphon.Tg_S.Value=TDin[11][0]; Thermosiphon.Pg_S.Value=TDin[12][0];
Thermosiphon.y_S(r"AMMONIA").Value=TDin[13][0]; Thermosiphon.y_S(r"WATER").Value=TDin[14][0]; Thermosiphon.Ml_R_CF.Value=TDin[15][0]; Thermosiphon.Tl_R_CF.Value=TDin[16][0];
Thermosiphon.Pl_R_CF.Value=TDin[17][0]; Thermosiphon.x_R_CF(r"AMMONIA").Value=TDin[18][0]; Thermosiphon.x_R_CF(r"WATER").Value=TDin[19][0];
Thermosiphon.Mg_R_CF.Value=TDin[20][0]; Thermosiphon.Tg_R_CF.Value=TDin[21][0]; Thermosiphon.Pg_R_CF.Value=TDin[22][0]; Thermosiphon.y_R_CF(r"AMMONIA").Value=TDin[23][0];
Thermosiphon.y_R_CF(r"WATER").Value=TDin[24][0]; Thermosiphon.rholS.Value=TDin[25][0]; Thermosiphon.rhogS.Value=TDin[26][0]; Thermosiphon.rholCF.Value=TDin[27][0];
Thermosiphon.rhogCF.Value=TDin[28][0]; Thermosiphon.hlS.Value=TDin[29][0]; Thermosiphon.hgS.Value=TDin[30][0]; Thermosiphon.hlCF.Value=TDin[31][0];
Thermosiphon.hgCF.Value=TDin[32][0]; Thermosiphon.ulS.Value=TDin[33][0]; Thermosiphon.ugS.Value=TDin[34][0]; Thermosiphon.ulCF.Value=TDin[35][0];
Thermosiphon.ugCF.Value=TDin[36][0]; Thermosiphon.MT.Value=TDin[37][0]; Thermosiphon.MzT.Value=TDin[38][0]; Thermosiphon.MuT.Value=TDin[39][0];
Thermosiphon.MRCF.Value=TDin[40][0]; Thermosiphon.MuRCF.Value=TDin[41][0];
# E-3 y Divisor
print("E-3 y Divisor");
E3.hVap_s_2.Value=hVap_s_2; E3.hC_HF_out.Value=hC_HF_out; E3.hC_CF_in.Value=hC_CF_in; E3.hC_CF_out.Value=hC_CF_out;
E3.Vap_s_2.F.Value=Vap_s_2F; E3.Vap_s_2.T.Value=Vap_s_2T; E3.Vap_s_2.P.Value=Vap_s_2P; E3.Vap_s_2.z(r"AMMONIA").Value=Vap_s_2za; E3.Vap_s_2.z(r"WATER").Value=Vap_s_2zw;
Divisor.Reflujo.F.Value=ReflujoF; Divisor.Reflujo.T.Value=ReflujoT; Divisor.Reflujo.P.Value=ReflujoP; Divisor.Reflujo.z(r"AMMONIA").Value=Reflujoza; Divisor.Reflujo.z(r"WATER").Value=Reflujozw;
E3.C_HF_out.F.Value=C_HF_outF; E3.C_HF_out.T.Value=C_HF_outT; E3.C_HF_out.P.Value=C_HF_outP; E3.C_HF_out.z(r"AMMONIA").Value=C_HF_outza; E3.C_HF_out.z(r"WATER").Value=C_HF_outzw;
Divisor.C_HF_out.F.Value=C_HF_outF; Divisor.C_HF_out.T.Value=C_HF_outT; Divisor.C_HF_out.P.Value=C_HF_outP; Divisor.C_HF_out.z(r"AMMONIA").Value=C_HF_outza; Divisor.C_HF_out.z(r"WATER").Value=C_HF_outzw;
E3.C_CF_in.F.Value=C_CF_inF; E3.C_CF_in.T.Value=C_CF_inT; E3.C_CF_in.P.Value=C_CF_inP; E3.C_CF_in.z(r"AMMONIA").Value=C_CF_inza; E3.C_CF_in.z(r"WATER").Value=C_CF_inzw;
E3.C_CF_out.F.Value=C_CF_outF; E3.C_CF_out.T.Value=C_CF_outT; E3.C_CF_out.P.Value=C_CF_outP; E3.C_CF_out.z(r"AMMONIA").Value=C_CF_outza; E3.C_CF_out.z(r"WATER").Value=C_CF_outzw;
PV2.VIb_in.F.Value=C_CF_outF; PV2.VIb_in.T.Value=C_CF_outT; PV2.VIb_in.P.Value=C_CF_outP; PV2.VIb_in.z(r"AMMONIA").Value=C_CF_outza; PV2.VIb_in.z(r"WATER").Value=C_CF_outzw;
Divisor.Prod_Liq.F.Value=Prod_LiqF; Divisor.Prod_Liq.T.Value=Prod_LiqT; Divisor.Prod_Liq.P.Value=Prod_LiqP; Divisor.Prod_Liq.z(r"AMMONIA").Value=Prod_Liqza; Divisor.Prod_Liq.z(r"WATER").Value=Prod_Liqzw; 
E3.QC.Q.Value=E3DEst[0][0]; Divisor.RR.Value=E3DEst[1][0]; Divisor.rhoProd_Liq.Value=E3DEst[2][0]; Divisor.Prod_Liqq.Value=E3DEst[3][0]; E3.dT1.Value=E3DEst[4][0]; E3.dT2.Value=E3DEst[5][0]; 
E3.dTln.Value=E3DEst[6][0]; E3.RF.Value=E3DEst[7][0]; E3.PF.Value=E3DEst[8][0]; E3.alphaF.Value=E3DEst[9][0]; E3.SF.Value=E3DEst[10][0]; E3.F.Value=E3DEst[11][0]; PV2.vp.Value=vpPV2[caso]; 
E3.Ml_C_CF.Value=E3DDin[0][0]; E3.Tl_C_CF.Value=E3DDin[1][0]; E3.Pl_C_CF.Value=E3DDin[2][0]; E3.x_C_CF(r"AMMONIA").Value=E3DDin[3][0]; E3.x_C_CF(r"WATER").Value=E3DDin[4][0];
E3.Mg_C_HF.Value=E3DDin[5][0]; E3.Tg_C_HF.Value=E3DDin[6][0]; E3.Pg_C_HF.Value=E3DDin[7][0]; E3.y_C_HF(r"AMMONIA").Value=E3DDin[8][0]; E3.y_C_HF(r"WATER").Value=E3DDin[9][0];
E3.rholCF.Value=E3DDin[10][0]; E3.hlCF.Value=E3DDin[11][0]; E3.ulCF.Value=E3DDin[12][0]; E3.rhogHF.Value=E3DDin[13][0]; E3.hgHF.Value=E3DDin[14][0]; E3.ugHF.Value=E3DDin[15][0];
E3.MugHF.Value=E3DDin[16][0]; PV2.q.Value=E3DDin[17][0]; PV2.rho_CF.Value=E3DDin[18][0]; 
# Prueba con grados de libertad originales
for metodo in [r"RK4",r"Gear12"]: 
    Sim.Options.Integrator=metodo; 
    try:
        Sim.Step(True);
        print(metodo+r": Sí genera resultados Aspen Custom Modeler");
    except: # Cuando no genera resultados
        print(metodo+r": No genera resultados Aspen Custom Modeler");
ACM.SaveDocumentAs(os.path.abspath(r"Dinamico_Din_Prueba.dynf"),True); ACM.quit();