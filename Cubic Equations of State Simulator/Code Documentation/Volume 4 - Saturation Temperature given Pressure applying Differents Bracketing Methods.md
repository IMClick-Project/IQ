# Saturation Temperature given Pressure applying Differents Bracketing Methods

This is the fourth option in the volume menu. Its interface is programmed in "Volume4.mlapp" and it uses the function called "Saturation_Temperature_given_Pressure.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/volume4.jpg" width="1104" height="599">

*Figure 1. Design View in Volume4.mlapp.*

### 1.2. Code View

```Matlab
classdef Volume4 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        UIFigure                     matlab.ui.Figure
        CriticalTemperature          matlab.ui.control.EditField
        CriticalTemperatureKLabel_2  matlab.ui.control.Label
        TitleFigure1                 matlab.ui.control.Label
        TripleTemperature            matlab.ui.control.EditField
        TripleTemperatureKLabel      matlab.ui.control.Label
        Label_7                      matlab.ui.control.Label
        Label_6                      matlab.ui.control.Label
        Label_5                      matlab.ui.control.Label
        Label_4                      matlab.ui.control.Label
        Label_3                      matlab.ui.control.Label
        Label_2                      matlab.ui.control.Label
        Table1                       matlab.ui.control.Table
        Table2PR                     matlab.ui.control.Table
        Table2SRK                    matlab.ui.control.Table
        Table2RK                     matlab.ui.control.Table
        Compound                     matlab.ui.control.DropDown
        CompoundDropDownLabel        matlab.ui.control.Label
        Label                        matlab.ui.control.Label
        BackButton                   matlab.ui.control.Button
        ExportButton                 matlab.ui.control.Button
        Table2vdW                    matlab.ui.control.Table
        TsatgivenPapplyingDifferentsBracketingMethods  matlab.ui.control.Label
        Image                        matlab.ui.control.Image
        CalculateButton              matlab.ui.control.Button
        Figure1PR                    matlab.ui.control.UIAxes
        Figure1SRK                   matlab.ui.control.UIAxes
        Figure1RK                    matlab.ui.control.UIAxes
        Figure2                      matlab.ui.control.UIAxes
        Figure1vdW                   matlab.ui.control.UIAxes
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.UIFigure,"north");
            % Compound
            data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds");
            app.Compound.Items=table2cell(data(:,1));
        end

        % Button pushed function: BackButton
        function BackButtonPushed(app, event)
            Volume;
            delete(app);
        end

        % Button pushed function: CalculateButton
        function CalculateButtonPushed(app, event)
            % Saturation Pressures
            data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
            tam=0;
            aux=strings;
            for i=1:height(data2)
                if ~ismissing(table2array(data2(i,2))) && string(table2array(data2(i,2)))~="NaN"
                    tam=tam+1;
                    aux(tam)=string(table2array(data2(i,2)));
                end
            end
            if tam>0
                progressbar=uiprogressdlg(app.UIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                Saturation_Temperature_given_Pressure;
                app.ExportButton.Visible="on";
                app.TitleFigure1.Text=strcat(app.Compound.Value," - Iterations vs Saturation Pressure");
                close(progressbar);
            else
                uialert(app.UIFigure,"Input saturation pressures not found.","Data Status","Icon","warning");
            end
        end

        % Button pushed function: ExportButton
        function ExportButtonPushed(app, event)
            progressbar=uiprogressdlg(app.UIFigure,"Title","Status","Message","Exporting","Indeterminate","on","Cancelable","off");
            drawnow;
            aux=app.Table1.Data;
            table1=table(aux(:,1),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)),str2double(aux(:,5)),str2double(aux(:,6)),str2double(aux(:,7)),str2double(aux(:,8)));
            table1.Properties.VariableNames{'Var1'}='EoS';
            table1.Properties.VariableNames{'Var2'}='Calculated Triple Pressure [bar]';
            table1.Properties.VariableNames{'Var3'}='Calculated Pressure given CCT [bar]';
            table1.Properties.VariableNames{'Var4'}='Total Iterations-B';
            table1.Properties.VariableNames{'Var5'}='Total Iterations-FP';
            table1.Properties.VariableNames{'Var6'}='Total Iterations-I';
            table1.Properties.VariableNames{'Var7'}='Total Iterations-P';
            table1.Properties.VariableNames{'Var8'}='Total Iterations-AB';
            aux=app.Table2vdW.Data;
            table2vdW=table(str2double(aux(:,1)),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)),str2double(aux(:,5)),str2double(aux(:,6)),str2double(aux(:,7)),str2double(aux(:,8)),str2double(aux(:,9)),str2double(aux(:,10)),str2double(aux(:,11)));
            table2vdW.Properties.VariableNames{'Var1'}='Psat [bar]';
            table2vdW.Properties.VariableNames{'Var2'}='Tsat-B [K]';
            table2vdW.Properties.VariableNames{'Var3'}='Iterations-B';
            table2vdW.Properties.VariableNames{'Var4'}='Tsat-FP [K]';
            table2vdW.Properties.VariableNames{'Var5'}='Iterations-FP';
            table2vdW.Properties.VariableNames{'Var6'}='Tsat-I [K]';
            table2vdW.Properties.VariableNames{'Var7'}='Iterations-I';
            table2vdW.Properties.VariableNames{'Var8'}='Tsat-P [K]';
            table2vdW.Properties.VariableNames{'Var9'}='Iterations-P';
            table2vdW.Properties.VariableNames{'Var10'}='Tsat-AB [K]';
            table2vdW.Properties.VariableNames{'Var11'}='Iterations-AB';
            aux=app.Table2RK.Data;
            table2RK=table(str2double(aux(:,1)),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)),str2double(aux(:,5)),str2double(aux(:,6)),str2double(aux(:,7)),str2double(aux(:,8)),str2double(aux(:,9)),str2double(aux(:,10)),str2double(aux(:,11)));
            table2RK.Properties.VariableNames{'Var1'}='Psat [bar]';
            table2RK.Properties.VariableNames{'Var2'}='Tsat-B [K]';
            table2RK.Properties.VariableNames{'Var3'}='Iterations-B';
            table2RK.Properties.VariableNames{'Var4'}='Tsat-FP [K]';
            table2RK.Properties.VariableNames{'Var5'}='Iterations-FP';
            table2RK.Properties.VariableNames{'Var6'}='Tsat-I [K]';
            table2RK.Properties.VariableNames{'Var7'}='Iterations-I';
            table2RK.Properties.VariableNames{'Var8'}='Tsat-P [K]';
            table2RK.Properties.VariableNames{'Var9'}='Iterations-P';
            table2RK.Properties.VariableNames{'Var10'}='Tsat-AB [K]';
            table2RK.Properties.VariableNames{'Var11'}='Iterations-AB';
            aux=app.Table2SRK.Data;
            table2SRK=table(str2double(aux(:,1)),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)),str2double(aux(:,5)),str2double(aux(:,6)),str2double(aux(:,7)),str2double(aux(:,8)),str2double(aux(:,9)),str2double(aux(:,10)),str2double(aux(:,11)));
            table2SRK.Properties.VariableNames{'Var1'}='Psat [bar]';
            table2SRK.Properties.VariableNames{'Var2'}='Tsat-B [K]';
            table2SRK.Properties.VariableNames{'Var3'}='Iterations-B';
            table2SRK.Properties.VariableNames{'Var4'}='Tsat-FP [K]';
            table2SRK.Properties.VariableNames{'Var5'}='Iterations-FP';
            table2SRK.Properties.VariableNames{'Var6'}='Tsat-I [K]';
            table2SRK.Properties.VariableNames{'Var7'}='Iterations-I';
            table2SRK.Properties.VariableNames{'Var8'}='Tsat-P [K]';
            table2SRK.Properties.VariableNames{'Var9'}='Iterations-P';
            table2SRK.Properties.VariableNames{'Var10'}='Tsat-AB [K]';
            table2SRK.Properties.VariableNames{'Var11'}='Iterations-AB';
            aux=app.Table2PR.Data;
            table2PR=table(str2double(aux(:,1)),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)),str2double(aux(:,5)),str2double(aux(:,6)),str2double(aux(:,7)),str2double(aux(:,8)),str2double(aux(:,9)),str2double(aux(:,10)),str2double(aux(:,11)));
            table2PR.Properties.VariableNames{'Var1'}='Psat [bar]';
            table2PR.Properties.VariableNames{'Var2'}='Tsat-B [K]';
            table2PR.Properties.VariableNames{'Var3'}='Iterations-B';
            table2PR.Properties.VariableNames{'Var4'}='Tsat-FP [K]';
            table2PR.Properties.VariableNames{'Var5'}='Iterations-FP';
            table2PR.Properties.VariableNames{'Var6'}='Tsat-I [K]';
            table2PR.Properties.VariableNames{'Var7'}='Iterations-I';
            table2PR.Properties.VariableNames{'Var8'}='Tsat-P [K]';
            table2PR.Properties.VariableNames{'Var9'}='Iterations-P';
            table2PR.Properties.VariableNames{'Var10'}='Tsat-AB [K]';
            table2PR.Properties.VariableNames{'Var11'}='Iterations-AB';
            writecell(cell(10,8),"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","Total Iterations vs EoS","Range","A1");
            writetable(table1,"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","Total Iterations vs EoS","Range","A4");
            writecell({'Compound'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","Total Iterations vs EoS","Range","A1");
            writecell({'Triple Temperature [K]'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","Total Iterations vs EoS","Range","A2");
            writecell({'Close to Critical Temperature (CCT) [K]'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","Total Iterations vs EoS","Range","A3");
            writecell({app.Compound.Value},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","Total Iterations vs EoS","Range","B1");
            writematrix(str2double({app.TripleTemperature.Value}),"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","Total Iterations vs EoS","Range","B2");
            writematrix(str2double({app.CriticalTemperature.Value}),"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","Total Iterations vs EoS","Range","B3");
            writecell(cell(5000,11),"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range","A1");
            writetable(table2vdW,"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat");
            for i=2:1+height(table2vdW)
                if ismissing(string(readcell("./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range",[i,2,i,2])))
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range",['B',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range",['C',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range",['D',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range",['E',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range",['F',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range",['G',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range",['H',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range",['I',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range",['J',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","vdW - Iterations vs Psat","Range",['K',num2str(i)]);
                end
            end
            writecell(cell(5000,11),"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range","A1");
            writetable(table2RK,"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat");
            for i=2:1+height(table2RK)
                if ismissing(string(readcell("./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range",[i,2,i,2])))
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range",['B',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range",['C',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range",['D',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range",['E',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range",['F',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range",['G',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range",['H',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range",['I',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range",['J',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","RK - Iterations vs Psat","Range",['K',num2str(i)]);
                end
            end
            writecell(cell(5000,11),"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range","A1");
            writetable(table2SRK,"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat");
            for i=2:1+height(table2SRK)
                if ismissing(string(readcell("./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range",[i,2,i,2])))
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range",['B',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range",['C',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range",['D',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range",['E',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range",['F',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range",['G',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range",['H',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range",['I',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range",['J',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","SRK - Iterations vs Psat","Range",['K',num2str(i)]);
                end
            end
            writecell(cell(5000,11),"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range","A1");
            writetable(table2PR,"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat");
            for i=2:1+height(table2PR)
                if ismissing(string(readcell("./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range",[i,2,i,2])))
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range",['B',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range",['C',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range",['D',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range",['E',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range",['F',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range",['G',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range",['H',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range",['I',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range",['J',num2str(i)]);
                    writecell({'NaN'},"./Results/Saturation Temperature given Pressure applying Differents Bracketing Methods.xlsx","Sheet","PR - Iterations vs Psat","Range",['K',num2str(i)]);
                end
            end
            close(progressbar);
            uialert(app.UIFigure,"Finished Export.","Export Status","Icon","success");
        end

        % Value changed function: Compound
        function CompoundValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            app.TitleFigure1.Text="Compound - Iterations vs Saturation Pressure";
            app.TripleTemperature.Value="";
            app.CriticalTemperature.Value="";
            cla(app.Figure1vdW);
            cla(app.Figure1RK);
            cla(app.Figure1SRK);
            cla(app.Figure1PR);
            cla(app.Figure2);
            app.Table1.Data={};
            app.Table2vdW.Data={};
            app.Table2RK.Data={};
            app.Table2SRK.Data={};
            app.Table2PR.Data={};
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create UIFigure and hide until all components are created
            app.UIFigure = uifigure('Visible', 'off');
            app.UIFigure.Color = [1 1 1];
            app.UIFigure.Position = [100 100 1221 665];
            app.UIFigure.Name = 'Saturation Temperature given Pressure applying Differents Bracketing Methods';
            app.UIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.UIFigure.Resize = 'off';

            % Create Figure1vdW
            app.Figure1vdW = uiaxes(app.UIFigure);
            title(app.Figure1vdW, 'van der Waals (vdW)')
            xlabel(app.Figure1vdW, 'Saturation Pressure [bar]')
            ylabel(app.Figure1vdW, 'Iterations')
            zlabel(app.Figure1vdW, 'Z')
            app.Figure1vdW.YScale = 'log';
            app.Figure1vdW.YMinorTick = 'on';
            app.Figure1vdW.XGrid = 'on';
            app.Figure1vdW.XMinorGrid = 'on';
            app.Figure1vdW.YGrid = 'on';
            app.Figure1vdW.YMinorGrid = 'on';
            app.Figure1vdW.FontSize = 11;
            app.Figure1vdW.Position = [24 274 283 209];

            % Create Figure2
            app.Figure2 = uiaxes(app.UIFigure);
            title(app.Figure2, 'Total Iterations vs Cubic Equation of State')
            xlabel(app.Figure2, 'Cubic Equation of State')
            ylabel(app.Figure2, 'Total Iterations')
            zlabel(app.Figure2, 'Z')
            app.Figure2.YScale = 'log';
            app.Figure2.YMinorTick = 'on';
            app.Figure2.XGrid = 'on';
            app.Figure2.YGrid = 'on';
            app.Figure2.YMinorGrid = 'on';
            app.Figure2.Position = [618 351 585 301];

            % Create Figure1RK
            app.Figure1RK = uiaxes(app.UIFigure);
            title(app.Figure1RK, 'Redlich-Kwong (RK)')
            xlabel(app.Figure1RK, 'Saturation Pressure [bar]')
            ylabel(app.Figure1RK, 'Iterations')
            zlabel(app.Figure1RK, 'Z')
            app.Figure1RK.YScale = 'log';
            app.Figure1RK.YMinorTick = 'on';
            app.Figure1RK.XGrid = 'on';
            app.Figure1RK.XMinorGrid = 'on';
            app.Figure1RK.YGrid = 'on';
            app.Figure1RK.YMinorGrid = 'on';
            app.Figure1RK.FontSize = 11;
            app.Figure1RK.Position = [306 273 283 210];

            % Create Figure1SRK
            app.Figure1SRK = uiaxes(app.UIFigure);
            title(app.Figure1SRK, 'Soave-Redlich-Kwong (SRK)')
            xlabel(app.Figure1SRK, 'Saturation Pressure [bar]')
            ylabel(app.Figure1SRK, 'Iterations')
            zlabel(app.Figure1SRK, 'Z')
            app.Figure1SRK.YScale = 'log';
            app.Figure1SRK.YMinorTick = 'on';
            app.Figure1SRK.XGrid = 'on';
            app.Figure1SRK.XMinorGrid = 'on';
            app.Figure1SRK.YGrid = 'on';
            app.Figure1SRK.YMinorGrid = 'on';
            app.Figure1SRK.FontSize = 11;
            app.Figure1SRK.Position = [24 63 283 211];

            % Create Figure1PR
            app.Figure1PR = uiaxes(app.UIFigure);
            title(app.Figure1PR, 'Peng-Robinson (PR)')
            xlabel(app.Figure1PR, 'Saturation Pressure [bar]')
            ylabel(app.Figure1PR, 'Iterations')
            zlabel(app.Figure1PR, 'Z')
            app.Figure1PR.YScale = 'log';
            app.Figure1PR.YMinorTick = 'on';
            app.Figure1PR.XGrid = 'on';
            app.Figure1PR.XMinorGrid = 'on';
            app.Figure1PR.YGrid = 'on';
            app.Figure1PR.YMinorGrid = 'on';
            app.Figure1PR.FontSize = 11;
            app.Figure1PR.Position = [309 63 283 211];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.UIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [424 522 103 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Image
            app.Image = uiimage(app.UIFigure);
            app.Image.Position = [67 504 116 101];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create TsatgivenPapplyingDifferentsBracketingMethods
            app.TsatgivenPapplyingDifferentsBracketingMethods = uilabel(app.UIFigure);
            app.TsatgivenPapplyingDifferentsBracketingMethods.HorizontalAlignment = 'center';
            app.TsatgivenPapplyingDifferentsBracketingMethods.FontSize = 20;
            app.TsatgivenPapplyingDifferentsBracketingMethods.FontWeight = 'bold';
            app.TsatgivenPapplyingDifferentsBracketingMethods.FontColor = [0.1412 0.302 0.4784];
            app.TsatgivenPapplyingDifferentsBracketingMethods.Position = [35 604 543 48];
            app.TsatgivenPapplyingDifferentsBracketingMethods.Text = {'Saturation Temperature '; 'given Pressure applying Differents Bracketing Methods'};

            % Create Table2vdW
            app.Table2vdW = uitable(app.UIFigure);
            app.Table2vdW.ColumnName = {'Psat [bar]'; 'Tsat-B [K]'; 'Iterations-B'; 'Tsat-FP [K]'; 'Iterations-FP'; 'Tsat-I [K]'; 'Iterations-I'; 'Tsat-P [K]'; 'Iterations-P'; 'Tsat-AB [K]'; 'Iterations-AB'};
            app.Table2vdW.RowName = {};
            app.Table2vdW.Position = [617 48 138 136];

            % Create ExportButton
            app.ExportButton = uibutton(app.UIFigure, 'push');
            app.ExportButton.ButtonPushedFcn = createCallbackFcn(app, @ExportButtonPushed, true);
            app.ExportButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.ExportButton.FontWeight = 'bold';
            app.ExportButton.FontColor = [0.1412 0.302 0.4784];
            app.ExportButton.Visible = 'off';
            app.ExportButton.Position = [991 11 100 22];
            app.ExportButton.Text = 'Export';

            % Create BackButton
            app.BackButton = uibutton(app.UIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [1103 11 100 22];
            app.BackButton.Text = 'Back';

            % Create Label
            app.Label = uilabel(app.UIFigure);
            app.Label.FontWeight = 'bold';
            app.Label.FontColor = [0.1412 0.302 0.4784];
            app.Label.Position = [618 15 118 28];
            app.Label.Text = {'Symbology'; 'NaN: Not a Number.'};

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.UIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [130 555 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.UIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [285 555 242 22];
            app.Compound.Value = {};

            % Create Table2RK
            app.Table2RK = uitable(app.UIFigure);
            app.Table2RK.ColumnName = {'Psat [bar]'; 'Tsat-B [K]'; 'Iterations-B'; 'Tsat-FP [K]'; 'Iterations-FP'; 'Tsat-I [K]'; 'Iterations-I'; 'Tsat-P [K]'; 'Iterations-P'; 'Tsat-AB [K]'; 'Iterations-AB'};
            app.Table2RK.RowName = {};
            app.Table2RK.Position = [768 48 138 136];

            % Create Table2SRK
            app.Table2SRK = uitable(app.UIFigure);
            app.Table2SRK.ColumnName = {'Psat [bar]'; 'Tsat-B [K]'; 'Iterations-B'; 'Tsat-FP [K]'; 'Iterations-FP'; 'Tsat-I [K]'; 'Iterations-I'; 'Tsat-P [K]'; 'Iterations-P'; 'Tsat-AB [K]'; 'Iterations-AB'};
            app.Table2SRK.RowName = {};
            app.Table2SRK.Position = [917 48 138 136];

            % Create Table2PR
            app.Table2PR = uitable(app.UIFigure);
            app.Table2PR.ColumnName = {'Psat [bar]'; 'Tsat-B [K]'; 'Iterations-B'; 'Tsat-FP [K]'; 'Iterations-FP'; 'Tsat-I [K]'; 'Iterations-I'; 'Tsat-P [K]'; 'Iterations-P'; 'Tsat-AB [K]'; 'Iterations-AB'};
            app.Table2PR.RowName = {};
            app.Table2PR.Position = [1067 48 138 136];

            % Create Table1
            app.Table1 = uitable(app.UIFigure);
            app.Table1.ColumnName = {'EoS'; 'Calculated Triple Pressure [bar]'; 'Calculated Pressure given CCT [bar]'; 'Total Iterations-B'; 'Total Iterations-FP'; 'Total Iterations-I'; 'Total Iterations-P'; 'Total Iterations-AB'};
            app.Table1.RowName = {};
            app.Table1.Position = [991 213 212 131];

            % Create Label_2
            app.Label_2 = uilabel(app.UIFigure);
            app.Label_2.FontWeight = 'bold';
            app.Label_2.FontColor = [0.1412 0.302 0.4784];
            app.Label_2.Position = [18 6 574 28];
            app.Label_2.Text = {'B: Bisection                                                 FP: False Position                                                   I: Illinois'; '                                   P: Pegasus                                                         AB: Anderson-Björck'};

            % Create Label_3
            app.Label_3 = uilabel(app.UIFigure);
            app.Label_3.HorizontalAlignment = 'center';
            app.Label_3.FontWeight = 'bold';
            app.Label_3.FontColor = [0.1412 0.302 0.4784];
            app.Label_3.Position = [243 33 120 22];
            app.Label_3.Text = 'Bracketing Methods';

            % Create Label_4
            app.Label_4 = uilabel(app.UIFigure);
            app.Label_4.HorizontalAlignment = 'center';
            app.Label_4.FontWeight = 'bold';
            app.Label_4.FontColor = [0.1412 0.302 0.4784];
            app.Label_4.Position = [670 186 31 22];
            app.Label_4.Text = 'vdW';

            % Create Label_5
            app.Label_5 = uilabel(app.UIFigure);
            app.Label_5.HorizontalAlignment = 'center';
            app.Label_5.FontWeight = 'bold';
            app.Label_5.FontColor = [0.1412 0.302 0.4784];
            app.Label_5.Position = [821 186 25 22];
            app.Label_5.Text = 'RK';

            % Create Label_6
            app.Label_6 = uilabel(app.UIFigure);
            app.Label_6.HorizontalAlignment = 'center';
            app.Label_6.FontWeight = 'bold';
            app.Label_6.FontColor = [0.1412 0.302 0.4784];
            app.Label_6.Position = [970 186 31 22];
            app.Label_6.Text = 'SRK';

            % Create Label_7
            app.Label_7 = uilabel(app.UIFigure);
            app.Label_7.HorizontalAlignment = 'center';
            app.Label_7.FontWeight = 'bold';
            app.Label_7.FontColor = [0.1412 0.302 0.4784];
            app.Label_7.Position = [1123 186 25 22];
            app.Label_7.Text = 'PR';

            % Create TripleTemperatureKLabel
            app.TripleTemperatureKLabel = uilabel(app.UIFigure);
            app.TripleTemperatureKLabel.HorizontalAlignment = 'right';
            app.TripleTemperatureKLabel.FontWeight = 'bold';
            app.TripleTemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.TripleTemperatureKLabel.Position = [710 283 133 22];
            app.TripleTemperatureKLabel.Text = 'Triple Temperature [K]';

            % Create TripleTemperature
            app.TripleTemperature = uieditfield(app.UIFigure, 'text');
            app.TripleTemperature.Editable = 'off';
            app.TripleTemperature.Position = [859 283 121 22];

            % Create TitleFigure1
            app.TitleFigure1 = uilabel(app.UIFigure);
            app.TitleFigure1.HorizontalAlignment = 'center';
            app.TitleFigure1.FontSize = 13;
            app.TitleFigure1.FontWeight = 'bold';
            app.TitleFigure1.Position = [24 481 557 22];
            app.TitleFigure1.Text = 'Compound - Iterations vs Saturation Pressure';

            % Create CriticalTemperatureKLabel_2
            app.CriticalTemperatureKLabel_2 = uilabel(app.UIFigure);
            app.CriticalTemperatureKLabel_2.HorizontalAlignment = 'right';
            app.CriticalTemperatureKLabel_2.FontWeight = 'bold';
            app.CriticalTemperatureKLabel_2.FontColor = [0.1412 0.302 0.4784];
            app.CriticalTemperatureKLabel_2.Position = [613 252 230 22];
            app.CriticalTemperatureKLabel_2.Text = 'Close to Critical Temperature (CCT) [K]';

            % Create CriticalTemperature
            app.CriticalTemperature = uieditfield(app.UIFigure, 'text');
            app.CriticalTemperature.Editable = 'off';
            app.CriticalTemperature.Position = [859 253 121 22];

            % Show the figure after all components are created
            app.UIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Volume4

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.UIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.UIFigure)
        end
    end
end
```

## 2. MATLAB Code

```Matlab
% Assignment of parameter values depending on the input and through the database
clc;
cla(app.Figure1vdW);
cla(app.Figure1RK);
cla(app.Figure1SRK);
cla(app.Figure1PR);
cla(app.Figure2);
app.Table1.Data={};
app.Table2vdW.Data={};
app.Table2RK.Data={};
app.Table2SRK.Data={};
app.Table2PR.Data={};
format long;
options=optimset("Display","off");
warning("off","all");
% Compound
data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds","ReadRowNames",1);
MM=table2array(data(app.Compound.Value,1)); % Molar Mass [g/mol]
Tt=table2array(data(app.Compound.Value,2)); % Triple Temperature [K]
Pt=table2array(data(app.Compound.Value,3)); % Triple Pressure [bar]
Tc=table2array(data(app.Compound.Value,4)); % Critical Temperature [K]
Pc=table2array(data(app.Compound.Value,5)); % Critical Pressure [bar]
w=table2array(data(app.Compound.Value,6)); % Acentric factor
% Antoine parameters
A=table2array(data(app.Compound.Value,8));
B=table2array(data(app.Compound.Value,9));
C=table2array(data(app.Compound.Value,10));
% Available pressures
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
tam=0;
aux=strings;
for i=1:height(data2)
    if ~ismissing(table2array(data2(i,2))) && string(table2array(data2(i,2)))~="NaN"
        tam=tam+1;
        aux(tam)=string(table2array(data2(i,2)));
    end
end
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
Er=0.00001;
Tbracket=[Tt Tc-0.1];
app.TripleTemperature.Value=string(Tbracket(1));
app.CriticalTemperature.Value=string(Tbracket(2));
eosname=["van der Waals","Redlich-Kwong","Soave-Redlich-Kwong","Peng-Robinson"];
Pbracket=zeros(2,4);
Tsat=zeros(4,tam,5);
totalite=zeros(4,tam,5);
sumi=zeros(4,5);
Tsatstr=strings(4,tam,5);
totalitestr=strings(4,tam,5);
% Saturation Pressure given Temperature applying Differents Bracketing Methods
for eos=1:4
    % Cubic Equation of State
    if eos==1
        epsilon=0;
        sigma=0;
        omega=1/8;
        psi=27/64;
        alpha=1;
    elseif eos==2 || eos==3
        epsilon=0;
        sigma=1;
        omega=0.08664;
        psi=0.42748;
    else
        epsilon=1-2^(1/2);
        sigma=1+2^(1/2);
        omega=0.07780;
        psi=0.45724;
    end
    b=omega*R*Tc/Pc;
    % Fugacity Test to predict Psat for Tt and close to Tc
    for i=1:2
        Ti=Tbracket(i);
        Tr=Ti/Tc;
        if eos==2
            alpha=Tr^(-1/2);
        elseif eos==3
            alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
        elseif eos==4
            alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
        end
        a=psi*alpha*(R*Tc)^2/Pc;
        Vstart=b+1;
        Vnext=b+2;
        Paux=R*Ti/(Vstart-b)-a/((Vstart+epsilon*b)*(Vstart+sigma*b));
        Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
        while Paux>Paux2
            Paux=Paux2;
            Vnext=Vnext+1;
            Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
        end
        while Paux<Paux2
            Paux=Paux2;
            Vnext=Vnext+1;
            Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
        end
        Paux=Paux2;
        q=a/(b*R*Ti);
        while true
            beta=Paux*b/(R*Ti);
            liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Paux*(b-V))/a)-V;
            Vliquid=fsolve(liquid,b,options);
            Zliquid=Paux*Vliquid/(R*Ti);
            if eos==1
                I=beta/(Zliquid+epsilon*beta);
            else
                I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
            end
            fliquid=Paux*exp(Zliquid-1-log(Zliquid-beta)-q*I);
            vapor=@(V) (R*Ti/Paux+b-a/Paux*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
            Vvapor=fsolve(vapor,R*Ti/Paux,options);
            Zvapor=Paux*Vvapor/(R*Ti);
            if eos==1
                I=beta/(Zvapor+epsilon*beta);
            else
                I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
            end
            fvapor=Paux*exp(Zvapor-1-log(Zvapor-beta)-q*I);
            if abs(1-fliquid/fvapor)<Er
                break;
            end
            Paux=Paux*fliquid/fvapor;
        end
        Pbracket(i,eos)=Paux;
    end
    % For each pressure in the database: Calculate Tsat and number of iterations for each bracketing methods
    % Tsat(eos,i,method): Tsat for Psat "i", estimate with cubic equation of state "eos" and bracketing methods "method"
    % totalite(eos,i,method): Number of iterations for Psat "i", estimate with cubic equation of state "eos" and bracketing methods "method"
    for i=1:tam
        Pi=str2double(aux(i));
        % Case not thermodynamically possible: Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number)
        if Pi<Pbracket(1,eos) || Pi>Pbracket(2,eos) 
            Tsat(eos,i,:)=[NaN NaN NaN NaN NaN];
            totalite(eos,i,:)=[NaN NaN NaN NaN NaN];
            Tsatstr(eos,i,:)=["NaN" "NaN" "NaN" "NaN" "NaN"];
            totalitestr(eos,i,:)=["NaN" "NaN" "NaN" "NaN" "NaN"];
            continue;
        end  
        % For each method: Calculate Tsat(eos,i,method) and totalite(eos,i,method)
        for method=1:5
            Pstart=Pbracket(1,eos)-Pi;
            Pfinal=Pbracket(2,eos)-Pi;
            Tstart=Tbracket(1);
            Tfinal=Tbracket(2);
            ite=0;
            while abs(Pfinal)>Er && abs(Pstart)>Er && abs(Tstart-Tfinal)>Er
                ite=ite+1;
                if method==1 % B
                    Ti=(Tstart+Tfinal)/2;
                else % FP or FP improvements
                    Ti=Tfinal-(Tfinal-Tstart)*Pfinal/(Pfinal-Pstart);
                end  
                Tr=Ti/Tc;
                if eos==2
                    alpha=Tr^(-1/2);
                elseif eos==3
                    alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
                elseif eos==4
                    alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
                end
                a=psi*alpha*(R*Tc)^2/Pc;
                Vstart=b+1;
                Vnext=b+2;
                Paux=R*Ti/(Vstart-b)-a/((Vstart+epsilon*b)*(Vstart+sigma*b));
                Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
                while Paux>Paux2
                    Paux=Paux2;
                    Vnext=Vnext+1;
                    Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
                end
                while Paux<Paux2
                    Paux=Paux2;
                    Vnext=Vnext+1;
                    Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
                end
                Paux=Paux2;
                q=a/(b*R*Ti);
                while true
                    beta=Paux*b/(R*Ti);
                    liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Paux*(b-V))/a)-V;
                    Vliquid=fsolve(liquid,b,options);
                    Zliquid=Paux*Vliquid/(R*Ti);
                    if eos==1
                        I=beta/(Zliquid+epsilon*beta);
                    else
                        I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
                    end
                    fliquid=Paux*exp(Zliquid-1-log(Zliquid-beta)-q*I);
                    vapor=@(V) (R*Ti/Paux+b-a/Paux*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
                    Vvapor=fsolve(vapor,R*Ti/Paux,options);
                    Zvapor=Paux*Vvapor/(R*Ti);
                    if eos==1
                        I=beta/(Zvapor+epsilon*beta);
                    else
                        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
                    end
                    fvapor=Paux*exp(Zvapor-1-log(Zvapor-beta)-q*I);
                    if abs(1-fliquid/fvapor)<Er
                        break;
                    end
                    Paux=Paux*fliquid/fvapor;
                end
                if method==1 || method==2 % B or FP
                    if (Paux-Pi)*Pfinal<0
                        Tstart=Ti;  
                        Pstart=Paux-Pi;
                    else
                        Tfinal=Ti;  
                        Pfinal=Paux-Pi;
                    end
                else % FP improvements
                    if (Paux-Pi)*Pfinal<0 
                        Tstart=Tfinal;  
                        Pstart=Pfinal;
                    else
                        if method==3 % I
                            Pstart=Pstart/2;
                        elseif method==4 % P
                            Pstart=Pstart*Pfinal/(Pfinal+Paux-Pi);
                        else %AB
                            if 1-(Paux-Pi)/Pfinal>0
                                m=1-(Paux-Pi)/Pfinal;
                            else
                                m=1/2;
                            end
                            Pstart=Pstart*m;
                        end 
                    end
                    Tfinal=Ti;  
                    Pfinal=Paux-Pi;
                end
            end
            Tsat(eos,i,method)=Ti;
            totalite(eos,i,method)=ite;
            Tsatstr(eos,i,method)=string(Ti);
            totalitestr(eos,i,method)=string(ite);
        end
    end
end
% Figure 1: Saturation Pressure given Temperature applying Differents Bracketing Methods
hold(app.Figure1vdW,"on");
plot(app.Figure1vdW,str2double(aux),totalite(1,:,1).',"Marker","*","MarkerSize",2);
plot(app.Figure1vdW,str2double(aux),totalite(1,:,2).',"Marker","*","MarkerSize",2);
plot(app.Figure1vdW,str2double(aux),totalite(1,:,3).',"Marker","*","MarkerSize",2);
plot(app.Figure1vdW,str2double(aux),totalite(1,:,4).',"Marker","*","MarkerSize",2);
plot(app.Figure1vdW,str2double(aux),totalite(1,:,5).',"Marker","*","MarkerSize",2);
axis(app.Figure1vdW,[0 str2double(aux(tam))+str2double(aux(1)) 0 max(max(totalite(1,:,:)))]);
legend(app.Figure1vdW,{'B','FP','I','P','AB'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1,"FontSize",6);
hold(app.Figure1vdW,"off");
hold(app.Figure1RK,"on");
plot(app.Figure1RK,str2double(aux),totalite(2,:,1).',"Marker","*","MarkerSize",2);
plot(app.Figure1RK,str2double(aux),totalite(2,:,2).',"Marker","*","MarkerSize",2);
plot(app.Figure1RK,str2double(aux),totalite(2,:,3).',"Marker","*","MarkerSize",2);
plot(app.Figure1RK,str2double(aux),totalite(2,:,4).',"Marker","*","MarkerSize",2);
plot(app.Figure1RK,str2double(aux),totalite(2,:,5).',"Marker","*","MarkerSize",2);
axis(app.Figure1RK,[0 str2double(aux(tam))+str2double(aux(1)) 0 max(max(totalite(2,:,:)))]);
legend(app.Figure1RK,{'B','FP','I','P','AB'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1,"FontSize",6);
hold(app.Figure1RK,"off");
hold(app.Figure1SRK,"on");
plot(app.Figure1SRK,str2double(aux),totalite(3,:,1).',"Marker","*","MarkerSize",2);
plot(app.Figure1SRK,str2double(aux),totalite(3,:,2).',"Marker","*","MarkerSize",2);
plot(app.Figure1SRK,str2double(aux),totalite(3,:,3).',"Marker","*","MarkerSize",2);
plot(app.Figure1SRK,str2double(aux),totalite(3,:,4).',"Marker","*","MarkerSize",2);
plot(app.Figure1SRK,str2double(aux),totalite(3,:,5).',"Marker","*","MarkerSize",2);
axis(app.Figure1SRK,[0 str2double(aux(tam))+str2double(aux(1)) 0 max(max(totalite(3,:,:)))]);
legend(app.Figure1SRK,{'B','FP','I','P','AB'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1,"FontSize",6);
hold(app.Figure1SRK,"off");
hold(app.Figure1PR,"on");
plot(app.Figure1PR,str2double(aux),totalite(4,:,1).',"Marker","*","MarkerSize",2);
plot(app.Figure1PR,str2double(aux),totalite(4,:,2).',"Marker","*","MarkerSize",2);
plot(app.Figure1PR,str2double(aux),totalite(4,:,3).',"Marker","*","MarkerSize",2);
plot(app.Figure1PR,str2double(aux),totalite(4,:,4).',"Marker","*","MarkerSize",2);
plot(app.Figure1PR,str2double(aux),totalite(4,:,5).',"Marker","*","MarkerSize",2);
axis(app.Figure1PR,[0 str2double(aux(tam))+str2double(aux(1)) 0 max(max(totalite(4,:,:)))]);
legend(app.Figure1PR,{'B','FP','I','P','AB'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1,"FontSize",6);
hold(app.Figure1PR,"off");
% Figure 2: Total Iterations per Method of All Pressures
for i=1:4
    for j=1:5
        sumi(i,j)=sum(totalite(i,:,j).',"omitnan");
    end
end
bar(app.Figure2,sumi);
set(app.Figure2,"xticklabel",{'vdW','RK','SRK','PR'},"ylim",[1 max(max(sumi))+5]);
leg=legend(app.Figure2,{'B','FP','I','P','AB'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1);
title(leg,"Method");
% Report results
app.Table1.Data=[eosname;string(Pbracket(1,:));string(Pbracket(2,:));string(sumi(:,1)');string(sumi(:,2)');string(sumi(:,3)');string(sumi(:,4)');string(sumi(:,5)')]';
app.Table2vdW.Data=[string(aux);Tsatstr(1,:,1);totalitestr(1,:,1);Tsatstr(1,:,2);totalitestr(1,:,2);Tsatstr(1,:,3);totalitestr(1,:,3);Tsatstr(1,:,4);totalitestr(1,:,4);Tsatstr(1,:,5);totalitestr(1,:,5)]';
app.Table2RK.Data=[string(aux);Tsatstr(2,:,1);totalitestr(2,:,1);Tsatstr(2,:,2);totalitestr(2,:,2);Tsatstr(2,:,3);totalitestr(2,:,3);Tsatstr(2,:,4);totalitestr(2,:,4);Tsatstr(2,:,5);totalitestr(2,:,5)]';
app.Table2SRK.Data=[string(aux);Tsatstr(3,:,1);totalitestr(3,:,1);Tsatstr(3,:,2);totalitestr(3,:,2);Tsatstr(3,:,3);totalitestr(3,:,3);Tsatstr(3,:,4);totalitestr(3,:,4);Tsatstr(3,:,5);totalitestr(3,:,5)]';
app.Table2PR.Data=[string(aux);Tsatstr(4,:,1);totalitestr(4,:,1);Tsatstr(4,:,2);totalitestr(4,:,2);Tsatstr(4,:,3);totalitestr(4,:,3);Tsatstr(4,:,4);totalitestr(4,:,4);Tsatstr(4,:,5);totalitestr(4,:,5)]';
```