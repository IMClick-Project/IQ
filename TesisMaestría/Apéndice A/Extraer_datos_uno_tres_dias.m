clear; clc; close all;

% Fecha 1 día
fechas1=["01-08-2023","02-08-2023","03-08-2023","04-08-2023","05-08-2023","06-08-2023",...
    "07-08-2023","08-08-2023","09-08-2023","10-08-2023","11-08-2023","12-08-2023",...
    "13-08-2023","14-08-2023","15-08-2023","16-08-2023","17-08-2023","18-08-2023",...
    "19-08-2023","20-08-2023","21-08-2023","22-08-2023","23-08-2023","24-08-2023",...
    "25-08-2023","26-08-2023","27-08-2023","28-08-2023","29-08-2023","30-08-2023",...
    "31-08-2023","01-09-2023","02-09-2023","03-09-2023","04-09-2023","05-09-2023",...
    "06-09-2023","07-09-2023","08-09-2023","09-09-2023","10-09-2023","11-09-2023",...
    "12-09-2023","13-09-2023","14-09-2023","15-09-2023","16-09-2023","17-09-2023",...
    "18-09-2023","19-09-2023","20-09-2023","21-09-2023","22-09-2023","23-09-2023",...
    "24-09-2023","25-09-2023","26-09-2023","27-09-2023","28-09-2023","29-09-2023",...
    "30-09-2023","01-10-2023","02-10-2023","03-10-2023","04-10-2023","05-10-2023",...
    "06-10-2023","07-10-2023","08-10-2023","09-10-2023","10-10-2023","11-10-2023",...
    "12-10-2023","13-10-2023","14-10-2023","15-10-2023","16-10-2023","17-10-2023",...
    "18-10-2023","19-10-2023","20-10-2023","21-10-2023","22-10-2023","23-10-2023",...
    "24-10-2023","25-10-2023","26-10-2023"];
% Fecha 3 días
fechas3=["01-08-2023-03-08-2023","04-08-2023-06-08-2023","07-08-2023-09-08-2023",...
    "10-08-2023-12-08-2023","13-08-2023-15-08-2023","16-08-2023-18-08-2023",...
    "19-08-2023-21-08-2023","22-08-2023-24-08-2023","25-08-2023-27-08-2023",...
    "28-08-2023-30-08-2023","31-08-2023-02-09-2023","03-09-2023-05-09-2023",...
    "06-09-2023-08-09-2023","09-09-2023-11-09-2023","12-09-2023-14-09-2023",...
    "15-09-2023-17-09-2023","18-09-2023-20-09-2023","21-09-2023-23-09-2023",...
    "24-09-2023-26-09-2023","27-09-2023-29-09-2023","30-09-2023-02-10-2023",...
    "03-10-2023-05-10-2023","06-10-2023-08-10-2023","09-10-2023-11-10-2023",...
    "12-10-2023-14-10-2023","15-10-2023-17-10-2023","18-10-2023-20-10-2023",...
    "21-10-2023-23-10-2023","24-10-2023-26-10-2023"];
% Archivo de Excel correspondiente por día
archivos=["Todos_01082023_05082023.xlsx","Todos_01082023_05082023.xlsx","Todos_01082023_05082023.xlsx",...
    "Todos_01082023_05082023.xlsx","Todos_01082023_05082023.xlsx","Todos_06082023_10082023.xlsx",...
    "Todos_06082023_10082023.xlsx","Todos_06082023_10082023.xlsx","Todos_06082023_10082023.xlsx",...
    "Todos_06082023_10082023.xlsx","Todos_11082023_15082023.xlsx","Todos_11082023_15082023.xlsx",...
    "Todos_11082023_15082023.xlsx","Todos_11082023_15082023.xlsx","Todos_11082023_15082023.xlsx",...
    "Todos_16082023_20082023.xlsx","Todos_16082023_20082023.xlsx","Todos_16082023_20082023.xlsx",...
    "Todos_16082023_20082023.xlsx","Todos_16082023_20082023.xlsx","Todos_21082023_25082023.xlsx",...
    "Todos_21082023_25082023.xlsx","Todos_21082023_25082023.xlsx","Todos_21082023_25082023.xlsx",...
    "Todos_21082023_25082023.xlsx","Todos_26082023_31082023.xlsx","Todos_26082023_31082023.xlsx",...
    "Todos_26082023_31082023.xlsx","Todos_26082023_31082023.xlsx","Todos_26082023_31082023.xlsx",...
    "Todos_26082023_31082023.xlsx","Todos_01092023_10092023.xlsx","Todos_01092023_10092023.xlsx",...
    "Todos_01092023_10092023.xlsx","Todos_01092023_10092023.xlsx","Todos_01092023_10092023.xlsx",...
    "Todos_01092023_10092023.xlsx","Todos_01092023_10092023.xlsx","Todos_01092023_10092023.xlsx",...
    "Todos_01092023_10092023.xlsx","Todos_01092023_10092023.xlsx","Todos_11092023_20092023.xlsx",...
    "Todos_11092023_20092023.xlsx","Todos_11092023_20092023.xlsx","Todos_11092023_20092023.xlsx",...
    "Todos_11092023_20092023.xlsx","Todos_11092023_20092023.xlsx","Todos_11092023_20092023.xlsx",...
    "Todos_11092023_20092023.xlsx","Todos_11092023_20092023.xlsx","Todos_11092023_20092023.xlsx",...
    "Todos_21092023_30092023.xlsx","Todos_21092023_30092023.xlsx","Todos_21092023_30092023.xlsx",...
    "Todos_21092023_30092023.xlsx","Todos_21092023_30092023.xlsx","Todos_21092023_30092023.xlsx",...
    "Todos_21092023_30092023.xlsx","Todos_21092023_30092023.xlsx","Todos_21092023_30092023.xlsx",...
    "Todos_21092023_30092023.xlsx","Todos_01102023_10102023.xlsx","Todos_01102023_10102023.xlsx",...
    "Todos_01102023_10102023.xlsx","Todos_01102023_10102023.xlsx","Todos_01102023_10102023.xlsx",...
    "Todos_01102023_10102023.xlsx","Todos_01102023_10102023.xlsx","Todos_01102023_10102023.xlsx",...
    "Todos_01102023_10102023.xlsx","Todos_01102023_10102023.xlsx","Todos_11102023_20102023.xlsx",...
    "Todos_11102023_20102023.xlsx","Todos_11102023_20102023.xlsx","Todos_11102023_20102023.xlsx",...
    "Todos_11102023_20102023.xlsx","Todos_11102023_20102023.xlsx","Todos_11102023_20102023.xlsx",...
    "Todos_11102023_20102023.xlsx","Todos_11102023_20102023.xlsx","Todos_11102023_20102023.xlsx",...
    "Todos_21102023_26102023.xlsx","Todos_21102023_26102023.xlsx","Todos_21102023_26102023.xlsx",...
    "Todos_21102023_26102023.xlsx","Todos_21102023_26102023.xlsx","Todos_21102023_26102023.xlsx"];
% Ubicación de las respectivas columnas de las mediciones en Excel
columnas=["DX","ED","DA","DZ",...
    "DY","DB","DS","DU","DR","DQ","DT","EF",...
    "DV","DW","DE","EC",...
    "DC","EA","EB","DD"];
% Nombre de las mediciones para guardar gráficas
var=["LIT-1","PT-1","PV-1","FT-1",...
    "LT-1","LV-1","TT-1","TT-2","TT-3","TT-4","TT-5","PT-2",...
    "TT-6","TT-7","TV-1","FIC-1",...
    "PV-2","FT-2","FIT-1","FV-1"];
% Nombre de las mediciones con unidades para etiquetar ejes en gráficas
variables=["LIT-1 [%]","PT-1 [kg/cm^2]","PV-1 [%]","FT-1 [kg/h]",...
    "LT-1 [%]","LV-1 [%]","TT-1 [°C]","TT-2 [°C]","TT-3 [°C]","TT-4 [°C]","TT-5 [°C]","PT-2 [kg/cm^2]",...
    "TT-6 [°C]","TT-7 [°C]","TV-1 [%]","FIC-1 [m^3/h]",...
    "PV-2 [%]","FT-2 [L/h]","FIT-1 [kg/h]","FV-1 [%]"];
% Ubicación de la fila donde inicia mediciones por día
filasini=["2","1441","2881","4321","5761","2",...
    "1441","2881","4321","5761","2","1441",...
    "2881","4321","5761","2","1441","2881",...
    "4321","5761","2","1441","2881","4321",...
    "5761","2","1441","2881","4321","5761",...
    "7201","2","1441","2881","4321","5761",...
    "7201","8641","10081","11521","12961","2",...
    "1441","2881","4321","5761","7201","8641",...
    "10081","11521","12961","2","1441","2881",...
    "4321","5761","7201","8641","10081","11521",...
    "12961","2","1441","2881","4321","5761",...
    "7201","8641","10081","11521","12961","2",...
    "1441","2881","4321","5761","7201","8641",...
    "10081","11521","12961","2","1441","2881",...
    "4321","5761","7201"];
% Ubicación de la fila donde termina mediciones por día
filasfin=["1440","2880","4320","5760","7200","1440",...
    "2880","4320","5760","7200","1440","2880",...
    "4320","5760","7200","1440","2880","4320",...
    "5760","7200","1440","2880","4320","5760",...
    "7200","1440","2880","4320","5760","7200",...
    "8640","1440","2880","4320","5760","7200",...
    "8640","10080","11520","12960","14400","1440",...
    "2880","4320","5760","7200","8640","10080",...
    "11520","12960","14400","1440","2880","4320",...
    "5760","7200","8640","10080","11520","12960",...
    "14400","1440","2880","4320","5760","7200",...
    "8640","10080","11520","12960","14400","1440",...
    "2880","4320","5760","7200","8640","10080",...
    "11520","12960","14400","1440","2880","4320",...
    "5760","7200","8004"];

% Extraer las mediciones deseadas, graficar en todo el periodo de medición y guardar gráfica
for k=1:20
    for i=1:29 % cada 3 días
        fr3=[]; datay3=[]; 
        for j=1:3 % cada 1 día
            frange=strcat("A",filasini(3*(i-1)+j),":A",filasfin(3*(i-1)+j)); fr1=datetime(table2array(readtable(archivos(3*(i-1)+j),"Range",frange,"ReadVariableNames",false)),'Format','dd-MMM-uuuu HH:mm:ss'); fr3=[fr3 fr1'];
            crange=strcat(columnas(k),filasini(3*(i-1)+j),":",columnas(k),filasfin(3*(i-1)+j)); datay1=readmatrix(archivos(3*(i-1)+j),"Range",crange); datay3=[datay3 datay1'];
            close all; fig=figure('WindowState', 'maximized'); plot(fr1',datay1');
            set(gca,'Units','normalized', 'PlotBoxAspectRatioMode','auto','PositionConstraint','innerposition',...
                'PlotBoxAspectRatio',[1 0.2639 0.2639],'Position',[0.0504 0.11 0.9212 0.815]);
            set(gcf,'OuterPosition',[-0.1042 0 1.1886 1],'InnerPosition',[0.0504 0.11 0.9212 0.815]);
            ylabel(variables(k)); xlim([fr1(1) fr1(end)]);
            % En caso de ser una línea horizonal, cambiar los límites 
            if min(datay1')==max(datay1')
                if min(datay1')==0 ylim([-5 5]); else ylim([min(datay1')*0.5 max(datay1')*1.5]); end
            else
                ylim([min(datay1')*0.9 max(datay1')*1.1]);
            end
            title(fechas1(3*(i-1)+j)); saveas(fig,strcat(fechas1(3*(i-1)+j)," ",var(k),".png"));
        end
        close all; fig=figure('WindowState', 'maximized'); plot(fr3,datay3);
        set(gca,'Units','normalized', 'PlotBoxAspectRatioMode','auto','PositionConstraint','innerposition',...
            'PlotBoxAspectRatio',[1 0.2639 0.2639],'Position',[0.0504 0.11 0.9212 0.815]);
        set(gcf,'OuterPosition',[-0.1042 0 1.1886 1],'InnerPosition',[0.0504 0.11 0.9212 0.815]);
        ylabel(variables(k)); xlim([fr3(1) fr3(end)]);
        % En caso de ser una línea horizonal, cambiar los límites 
        if min(datay3')==max(datay3')
            if min(datay3')==0 ylim([-5 5]); else ylim([min(datay3')*0.5 max(datay3')*1.5]); end
        else
            ylim([min(datay3')*0.9 max(datay3')*1.1]);
        end
        title(fechas3(i)); saveas(fig,strcat(fechas3(i)," ",var(k),".png"));
    end
end