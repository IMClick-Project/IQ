clear; clc; close all;

% Mediciones
% LIT-1: Nivel de V-1 en %
% PT-1: Presión en V-1 en kg/cm^2
% PV-1: Apertura de válvula de control de PT-1 en %
% FT-1: Flujo de salida de P-1, paso por E-1 y entrada a C-1 en kg/h
% LT-1: Nivel de C-1 en fondos en %
% LV-1: Apertura de válvula de control de LT-1 en %
% TT-1: Temperatura de salida inferior de C-1 en °C
% TT-2: Temperatura por segundo empaque de C-1 en °C
% TT-3: Temperatura por entrada a C-1 en °C
% TT-4: Temperatura por primer empaque de C-1 en °C
% TT-5: Temperatura de parte superior de C-1 en °C
% PT-2: Presión de parte superior de C-1 en kg/cm^2
% TT-6: Temperatura de entrada de HO a E-2 en °C
% TT-7: Temperatura de salida de HOR de E-2 en °C
% TV-1: Apertura de válvula de control en cascada de temperatura en %
% FIC-1: Flujo de salida de HOR en m3/h
% PV-2: Cierre de válvula de control de PT-2 en %
% FT-2: Flujo de reflujo a C-1 en L/h
% FIT-1: Flujo de salida de amoniaco condensado en kg/h
% FV-1: Apertura de válvula que regula FIT-1 en %

% Fechas de mediciones por archivo de Excel
fechas=["01/08/2023-05/08/2023","06/08/2023-10/08/2023","11/08/2023-15/08/2023",...
    "16/08/2023-20/08/2023","21/08/2023-25/08/2023","26/08/2023-31/08/2023",...
    "01/09/2023-10/09/2023","11/09/2023-20/09/2023","21/09/2023-30/09/2023",...
    "01/10/2023-10/10/2023","11/10/2023-20/10/2023","21/10/2023-26/10/2023"];
% Nombre de las mediciones con unidades para etiquetar ejes en gráficas
variables=["LIT-1 [%]","PT-1 [kg/cm^2]","PV-1 [%]","FT-1 [kg/h]",...
    "LT-1 [%]","LV-1 [%]","TT-1 [°C]","TT-2 [°C]","TT-3 [°C]","TT-4 [°C]","TT-5 [°C]","PT-2 [kg/cm^2]",...
    "TT-6 [°C]","TT-7 [°C]","TV-1 [%]","FIC-1 [m^3/h]",...
    "PV-2 [%]","FT-2 [L/h]","FIT-1 [kg/h]","FV-1 [%]"];
% Nombre de los archivos
archivos=["Todos_01082023_05082023.xlsx","Todos_06082023_10082023.xlsx","Todos_11082023_15082023.xlsx",...
    "Todos_16082023_20082023.xlsx","Todos_21082023_25082023.xlsx","Todos_26082023_31082023.xlsx",...
    "Todos_01092023_10092023.xlsx","Todos_11092023_20092023.xlsx","Todos_21092023_30092023.xlsx",...
    "Todos_01102023_10102023.xlsx","Todos_11102023_20102023.xlsx","Todos_21102023_26102023.xlsx"];
% Ubicación de las respectivas columnas de las mediciones en Excel
columnas=["DX","ED","DA","DZ",...
    "DY","DB","DS","DU","DR","DQ","DT","EF",...
    "DV","DW","DE","EC",...
    "DC","EA","EB","DD"];
% Cantidad de filas con mediciones por archivo
filas=["7200","7200","7200","7200","7200","8640","14400","14400","14400","14400","14400","8004"];
% Nombre de las mediciones para guardar gráficas
var=["LIT-1","PT-1","PV-1","FT-1",...
    "LT-1","LV-1","TT-1","TT-2","TT-3","TT-4","TT-5","PT-2",...
    "TT-6","TT-7","TV-1","FIC-1",...
    "PV-2","FT-2","FIT-1","FV-1"];

% Concatenar todas las fechas
fr=[]; 
for j=1:12
    frange=strcat("A1:A",filas(j)); datax=datetime(table2array(readtable(archivos(j),"Range",frange))); fr=[fr datax'];
end
% Extraer las mediciones deseadas, graficar en todo el periodo de medición y guardar gráfica
dfr=fr'; datos=[]; 
for i=1:20
    dr=[];
    for j=1:12
        crange=strcat(columnas(i),"2:",columnas(i),filas(j)); datay=readmatrix(archivos(j),"Range",crange); dr=[dr datay'];
    end
    close all; fig=figure('WindowState', 'maximized'); plot(fr,dr);
    set(gca,'Units','normalized', 'PlotBoxAspectRatioMode','auto','PositionConstraint','innerposition',...
        'PlotBoxAspectRatio',[1 0.2639 0.2639],'Position',[0.0504 0.11 0.9212 0.815]);
    set(gcf,'OuterPosition',[-0.1042 0 1.1886 1],'InnerPosition',[0.0504 0.11 0.9212 0.815]);
    ylabel(variables(i)); xlim([fr(1) fr(end)]); ylim([min(dr) max(dr)]);
    title("01-08-2023-26-10-2023"); saveas(fig,strcat(var(i),".png"));
    datos=[datos dr'];
end
% Guardar datos en matriz de MATLAB
save('Todo','dfr','datos');