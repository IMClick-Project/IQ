# Isotherm given Temperature on a PV Diagram

This is the first option in the volume menu. Its interface is programmed in "Volume1.mlapp" and it uses the function called "Isotherm_given_Temperature_PV_Diagram.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/volume1.jpg" width="928" height="550">

*Figure 1. Design View in Volume1.mlapp.*

### 1.2. Code View

```Matlab
classdef Volume1 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        IsothermgivenTemperatureonaPVDiagramUIFigure  matlab.ui.Figure
        Label                      matlab.ui.control.Label
        BackButton                 matlab.ui.control.Button
        ExportButton               matlab.ui.control.Button
        Table3                     matlab.ui.control.Table
        Table2                     matlab.ui.control.Table
        Table1                     matlab.ui.control.Table
        IsothermgivenTemperatureonaPVDiagramLabel  matlab.ui.control.Label
        Image                      matlab.ui.control.Image
        CalculateButton            matlab.ui.control.Button
        IsothermTemperature        matlab.ui.control.DropDown
        IsothermTemperatureKLabel  matlab.ui.control.Label
        Compound                   matlab.ui.control.DropDown
        CompoundDropDownLabel      matlab.ui.control.Label
        EoS                        matlab.ui.control.DropDown
        CubicEquationofStateDropDownLabel  matlab.ui.control.Label
        Figure3                    matlab.ui.control.UIAxes
        Figure2                    matlab.ui.control.UIAxes
        Figure1                    matlab.ui.control.UIAxes
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.IsothermgivenTemperatureonaPVDiagramUIFigure,"north");
            % Compound
            data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds");
            app.Compound.Items=table2cell(data(:,1));
            % Isotherm Temperature
            data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
            tam=0;
            aux=strings;
            for i=1:height(data2)
                if ~ismissing(table2array(data2(i,1))) && string(table2array(data2(i,1)))~="NaN"
                    tam=tam+1;
                    aux(tam)=string(table2array(data2(i,1)));
                end
            end
            if tam>0
                app.IsothermTemperature.Items=aux;
            else
                app.IsothermTemperature.Items={};
            end
        end

        % Button pushed function: CalculateButton
        function CalculateButtonPushed(app, event)
            if isempty(convertCharsToStrings(app.IsothermTemperature.Value))
                uialert(app.IsothermgivenTemperatureonaPVDiagramUIFigure,"Incomplete Data.","Data Status","Icon","warning");
            else
                progressbar=uiprogressdlg(app.IsothermgivenTemperatureonaPVDiagramUIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                Isotherm_given_Temperature_PV_Diagram;
                app.ExportButton.Visible="on";
                close(progressbar);
            end
        end

        % Value changed function: Compound
        function CompoundValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound @ Isotherm Temperature");
            cla(app.Figure1);
            cla(app.Figure2);
            cla(app.Figure3);
            app.Table1.Data={};
            app.Table2.Data={};
            app.Table3.Data={};
            % Isotherm Temperature
            data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
            tam=0;
            aux=strings;
            for i=1:height(data2)
                if ~ismissing(table2array(data2(i,1))) && string(table2array(data2(i,1)))~="NaN"
                    tam=tam+1;
                    aux(tam)=string(table2array(data2(i,1)));
                end
            end
            if tam>0
                app.IsothermTemperature.Items=aux;
            else
                app.IsothermTemperature.Items={};
            end
        end

        % Button pushed function: BackButton
        function BackButtonPushed(app, event)
            Volume;
            delete(app);
        end

        % Button pushed function: ExportButton
        function ExportButtonPushed(app, event)
            progressbar=uiprogressdlg(app.IsothermgivenTemperatureonaPVDiagramUIFigure,"Title","Status","Message","Exporting","Indeterminate","on","Cancelable","off");
            drawnow;
            aux=app.Table1.Data;
            table1=table(aux(:,1),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)));
            table1.Properties.VariableNames{'Var1'}='Phase';
            table1.Properties.VariableNames{'Var2'}='P [bar]';
            table1.Properties.VariableNames{'Var3'}='Z';
            table1.Properties.VariableNames{'Var4'}='V [m3/kg]';
            aux=app.Table2.Data;
            table2=table(aux(:,1),str2double(aux(:,2)),str2double(aux(:,3)));
            table2.Properties.VariableNames{'Var1'}='Initial Point';
            table2.Properties.VariableNames{'Var2'}='Iteration Number';
            table2.Properties.VariableNames{'Var3'}='P [bar]';
            aux=app.Table3.Data;
            table3=table(str2double(aux(:,1)),str2double(aux(:,2)),str2double(aux(:,3)));
            table3.Properties.VariableNames{'Var1'}='P [bar]';
            table3.Properties.VariableNames{'Var2'}='fliquid [bar]';
            table3.Properties.VariableNames{'Var3'}='fvapor [bar]';
            writecell(cell(5000,4),"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A1");
            writetable(table1,"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A4");
            writecell({'Compound'},"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A1");
            writecell({'Cubic Equation of State'},"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A2");
            writecell({'Isotherm Temperature [K]'},"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A3");
            writecell({app.Compound.Value},"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range","B1");
            writecell({app.EoS.Value},"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range","B2");
            writematrix(str2double({app.IsothermTemperature.Value}),"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range","B3");
            for i=1:height(table1)
                if string(table2cell(table1(i,1)))=="Saturated Liquid (Experimental Data)" 
                    index=i+4;
                    break;
                end
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index,2,index,2])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['B',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index+1,2,index+1,2])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['B',num2str(index+1)]);
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index,3,index,3])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['C',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index+1,3,index+1,3])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['C',num2str(index+1)]);
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index,4,index,4])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['D',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index+1,4,index+1,4])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['D',num2str(index+1)]);
            end
            writecell(cell(5000,3),"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Pressure vs Iteration Number","Range","A1");
            writetable(table2,"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Pressure vs Iteration Number");
            writecell(cell(5000,3),"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Fugacity vs Pressure","Range","A1");
            writetable(table3,"./Results/Isotherm given Temperature on a PV Diagram.xlsx","Sheet","Fugacity vs Pressure");
            close(progressbar);
            uialert(app.IsothermgivenTemperatureonaPVDiagramUIFigure,"Finished Export.","Export Status","Icon","success");
        end

        % Value changed function: EoS
        function EoSValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound @ Isotherm Temperature");
            cla(app.Figure1);
            cla(app.Figure2);
            cla(app.Figure3);
            app.Table1.Data={};
            app.Table2.Data={};
            app.Table3.Data={};
        end

        % Value changed function: IsothermTemperature
        function IsothermTemperatureValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound @ Isotherm Temperature");
            cla(app.Figure1);
            cla(app.Figure2);
            cla(app.Figure3);
            app.Table1.Data={};
            app.Table2.Data={};
            app.Table3.Data={};
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create IsothermgivenTemperatureonaPVDiagramUIFigure and hide until all components are created
            app.IsothermgivenTemperatureonaPVDiagramUIFigure = uifigure('Visible', 'off');
            app.IsothermgivenTemperatureonaPVDiagramUIFigure.Color = [1 1 1];
            app.IsothermgivenTemperatureonaPVDiagramUIFigure.Position = [100 100 1156 685];
            app.IsothermgivenTemperatureonaPVDiagramUIFigure.Name = 'Isotherm given Temperature on a PV Diagram';
            app.IsothermgivenTemperatureonaPVDiagramUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.IsothermgivenTemperatureonaPVDiagramUIFigure.Resize = 'off';

            % Create Figure1
            app.Figure1 = uiaxes(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            title(app.Figure1, 'EoS - Compound @ Isotherm Temperature')
            xlabel(app.Figure1, 'V [m^3/kg]')
            ylabel(app.Figure1, 'P [bar]')
            zlabel(app.Figure1, 'Z')
            app.Figure1.XScale = 'log';
            app.Figure1.XMinorTick = 'on';
            app.Figure1.XGrid = 'on';
            app.Figure1.XMinorGrid = 'on';
            app.Figure1.YGrid = 'on';
            app.Figure1.Position = [12 65 379 417];

            % Create Figure2
            app.Figure2 = uiaxes(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            title(app.Figure2, 'Fugacity Test - Pressure vs Iteration Number')
            xlabel(app.Figure2, 'Iteration Number')
            ylabel(app.Figure2, 'Pressure [bar]')
            zlabel(app.Figure2, 'Z')
            app.Figure2.XGrid = 'on';
            app.Figure2.YGrid = 'on';
            app.Figure2.Position = [588 372 390 300];

            % Create Figure3
            app.Figure3 = uiaxes(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            title(app.Figure3, 'Fugacity vs Pressure')
            xlabel(app.Figure3, 'Pressure [bar]')
            ylabel(app.Figure3, 'Fugacity [bar]')
            zlabel(app.Figure3, 'Z')
            app.Figure3.XGrid = 'on';
            app.Figure3.YGrid = 'on';
            app.Figure3.Position = [588 52 390 312];

            % Create CubicEquationofStateDropDownLabel
            app.CubicEquationofStateDropDownLabel = uilabel(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.CubicEquationofStateDropDownLabel.HorizontalAlignment = 'right';
            app.CubicEquationofStateDropDownLabel.FontWeight = 'bold';
            app.CubicEquationofStateDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CubicEquationofStateDropDownLabel.Position = [163 554 141 22];
            app.CubicEquationofStateDropDownLabel.Text = 'Cubic Equation of State';

            % Create EoS
            app.EoS = uidropdown(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.EoS.Items = {'van der Waals', 'Redlich-Kwong', 'Soave-Redlich-Kwong', 'Peng-Robinson'};
            app.EoS.ValueChangedFcn = createCallbackFcn(app, @EoSValueChanged, true);
            app.EoS.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EoS.Position = [320 554 241 22];
            app.EoS.Value = 'van der Waals';

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [165 587 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [320 587 242 22];
            app.Compound.Value = {};

            % Create IsothermTemperatureKLabel
            app.IsothermTemperatureKLabel = uilabel(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.IsothermTemperatureKLabel.HorizontalAlignment = 'right';
            app.IsothermTemperatureKLabel.FontWeight = 'bold';
            app.IsothermTemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.IsothermTemperatureKLabel.Position = [152 522 151 22];
            app.IsothermTemperatureKLabel.Text = 'Isotherm Temperature [K]';

            % Create IsothermTemperature
            app.IsothermTemperature = uidropdown(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.IsothermTemperature.Items = {};
            app.IsothermTemperature.ValueChangedFcn = createCallbackFcn(app, @IsothermTemperatureValueChanged, true);
            app.IsothermTemperature.BackgroundColor = [0.8588 0.9608 0.9608];
            app.IsothermTemperature.Position = [318 522 243 22];
            app.IsothermTemperature.Value = {};

            % Create CalculateButton
            app.CalculateButton = uibutton(app.IsothermgivenTemperatureonaPVDiagramUIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [459 488 103 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Image
            app.Image = uiimage(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.Image.Position = [24 515 116 101];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create IsothermgivenTemperatureonaPVDiagramLabel
            app.IsothermgivenTemperatureonaPVDiagramLabel = uilabel(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.IsothermgivenTemperatureonaPVDiagramLabel.HorizontalAlignment = 'center';
            app.IsothermgivenTemperatureonaPVDiagramLabel.FontSize = 20;
            app.IsothermgivenTemperatureonaPVDiagramLabel.FontWeight = 'bold';
            app.IsothermgivenTemperatureonaPVDiagramLabel.FontColor = [0.1412 0.302 0.4784];
            app.IsothermgivenTemperatureonaPVDiagramLabel.Position = [13 637 548 26];
            app.IsothermgivenTemperatureonaPVDiagramLabel.Text = 'Isotherm given Temperature on a PV Diagram';

            % Create Table1
            app.Table1 = uitable(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.Table1.ColumnName = {'Phase'; 'P [bar]'; 'Z'; 'V [m3/kg]'};
            app.Table1.RowName = {};
            app.Table1.Position = [403 93 158 373];

            % Create Table2
            app.Table2 = uitable(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.Table2.ColumnName = {'Initial Point'; 'Iteration Number'; 'P [bar]'};
            app.Table2.RowName = {};
            app.Table2.Position = [1000 441 137 208];

            % Create Table3
            app.Table3 = uitable(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.Table3.ColumnName = {'P [bar]'; 'fliquid  [bar]'; 'fvapor [bar]'};
            app.Table3.RowName = {};
            app.Table3.Position = [1000 133 138 203];

            % Create ExportButton
            app.ExportButton = uibutton(app.IsothermgivenTemperatureonaPVDiagramUIFigure, 'push');
            app.ExportButton.ButtonPushedFcn = createCallbackFcn(app, @ExportButtonPushed, true);
            app.ExportButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.ExportButton.FontWeight = 'bold';
            app.ExportButton.FontColor = [0.1412 0.302 0.4784];
            app.ExportButton.Visible = 'off';
            app.ExportButton.Position = [1037 59 100 22];
            app.ExportButton.Text = 'Export';

            % Create BackButton
            app.BackButton = uibutton(app.IsothermgivenTemperatureonaPVDiagramUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [1037 27 100 22];
            app.BackButton.Text = 'Back';

            % Create Label
            app.Label = uilabel(app.IsothermgivenTemperatureonaPVDiagramUIFigure);
            app.Label.FontWeight = 'bold';
            app.Label.FontColor = [0.1412 0.302 0.4784];
            app.Label.Position = [13 10 584 56];
            app.Label.Text = {'Symbology'; 'NA: Not Available.'; '*: Thermodynamically not possible case because the pressure is less than the triple pressure.'; '**: Thermodynamically not possible case because the pressure is greater than the critical pressure.'};

            % Show the figure after all components are created
            app.IsothermgivenTemperatureonaPVDiagramUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Volume1

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.IsothermgivenTemperatureonaPVDiagramUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.IsothermgivenTemperatureonaPVDiagramUIFigure)
        end
    end
end
```

## 2. MATLAB Code

```Matlab
% Assignment of parameter values depending on the input and through the database
clc;
cla(app.Figure1);
cla(app.Figure2);
cla(app.Figure3);
app.Table1.Data={};
app.Table2.Data={};
app.Table3.Data={};
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
% Cubic Equation of State
if app.EoS.Value=="van der Waals"
    eos=1;
elseif app.EoS.Value=="Redlich-Kwong"
    eos=2;
elseif app.EoS.Value=="Soave-Redlich-Kwong"
    eos=3;
else 
    eos=4;
end
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
% Isotherm Temperature [K]
Ti=str2double(app.IsothermTemperature.Value);
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
b=omega*R*Tc/Pc;
Er=0.00001;
Tr=Ti/Tc;
if eos==2
    alpha=Tr^(-1/2);
elseif eos==3
    alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
elseif eos==4
    alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
end
a=psi*alpha*(R*Tc)^2/Pc;
Vfug=zeros(1,2);
Pfug=zeros(1,2);
Vant=zeros(1,2);
Pant=zeros(1,2);
Vexp=zeros(1,2);
Pexp=zeros(1,2);
P=[];
V=[];
ite=[];
Pite=[];
iteA=[];
PiteA=[];
IP=strings;
IPA=strings;
Pf=[];
f1=[];
fv=[];
% Find first P to use in Fugacity Test: Point close to the Maximum of the Loop of the EoS
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
Pmax=Paux;
Pmaxbef=Paux2;
Paux=Paux2;
ite(1)=1;
Pite(1)=Paux;
IP(1)="Point close to the Maximum of the Loop of the EoS";
k=2;
q=a/(b*R*Ti);
% Algorithm to find Psat with the Fugacity Test
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
    % liquid - f=P*e^(GResidual/RT)
    fliquid=Paux*exp(Zliquid-1-log(Zliquid-beta)-q*I);
    vapor=@(V) (R*Ti/Paux+b-a/Paux*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
    Vvapor=fsolve(vapor,R*Ti/Paux,options);
    Zvapor=Paux*Vvapor/(R*Ti);
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    % vapor - f=P*e^(GResidual/RT)
    fvapor=Paux*exp(Zvapor-1-log(Zvapor-beta)-q*I);
    if abs(1-fliquid/fvapor)<Er
        break;
    end
    Paux=Paux*fliquid/fvapor;
    ite(k)=k;
    Pite(k)=Paux;
    IP(k)="Point close to the Maximum of the Loop of the EoS";
    k=k+1;
end
% Save results
Pfug(1)=Paux;
Pfug(2)=Paux;
Vfug(1)=Vliquid/1000/MM;
Vfug(2)=Vvapor/1000/MM;
% Save data to graph the loop of the EoS: Liquid 
% Find first V (with Z<=1)
Vstart=b+1;
Pstart=R*Ti/(Vstart-b)-a/((Vstart+epsilon*b)*(Vstart+sigma*b));
if Pstart*Vstart/(R*Ti)>1
    Zstart=Pstart*Vstart/(R*Ti)-1;
    Pfinal=Paux;
    Vfinal=Vliquid;
    Zfinal=Pfinal*Vfinal/(R*Ti)-1;
    while abs(Zfinal)>Er && abs(Zstart)>Er && abs(Pstart-Pfinal)>Er
        Pm=Pfinal-(Pfinal-Pstart)*Zfinal/(Zfinal-Zstart);
        liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Pm*(b-V))/a)-V;
        Vm=fsolve(liquid,b,options);
        Zm=Pm*Vm/(R*Ti);
        if (Zm-1)*Zfinal<0 
            Pstart=Pfinal;  
            Zstart=Zfinal;  
        else 
            Zstart=Zstart*Zfinal/(Zfinal+Zm-1);
        end
        Pfinal=Pm;  
        Zfinal=Zm-1;
    end
    Vstart=R*Ti*Zm/Pm;
end
% Find first P to use in Fugacity Test: Point close to the Maximum of the Loop of the EoS
step=(Vliquid-Vstart)/5000;
Vnext=Vstart+step;
P(1)=R*Ti/(Vstart-b)-a/((Vstart+epsilon*b)*(Vstart+sigma*b));
V(1)=Vstart/1000/MM;
P(2)=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
V(2)=Vnext/1000/MM;
Paux=P(1);
Paux2=P(2);
j=2;
% Save data to graph the loop of the EoS: Liquid to Point close to the Maximum of the Loop of the EoS
while Paux>Paux2
    Paux=Paux2;
    Vnext=Vnext+step;
    Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    j=j+1;
    P(j)=Paux2;
    V(j)=Vnext/1000/MM;
    if Vnext<Vliquid
        jl=j;
    end
end
Pminbef=Paux2;
Pmin=Paux;
while Paux<Paux2
    Paux=Paux2;
    Vnext=Vnext+step;
    Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    j=j+1;
    P(j)=Paux2;
    V(j)=Vnext/1000/MM;
end
% Save data to graph the loop of the EoS: Point close to the Maximum of the Loop of the EoS to Vapor
step=max([step (Vvapor-Vnext)/5000]);
while Vnext<Vvapor
    Vnext=Vnext+step;
    Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    j=j+1;
    P(j)=Paux2;
    V(j)=Vnext/1000/MM;
end
% Save data to graph the loop of the EoS: Vapor
jv=j+1;
Vnext=Vvapor+1;
Vmax=Vvapor+10000;
step=(Vmax-Vnext)/5000;
while Vnext<Vmax
    Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    j=j+1;
    P(j)=Paux2;
    V(j)=Vnext/1000/MM;
    Vnext=Vnext+step;
end
% Calculate and save fugacity (liquid and vapor) of possible saturation pressures
step=(Pmaxbef-max([Pminbef Er]))/100;
j=1;
for i=max([Pminbef Er]):step:Pmaxbef
    Paux=i;
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
    fl(j)=fliquid;
    fv(j)=fvapor;
    Pf(j)=Paux;
    j=j+1;
end
% Find Psat using Antoine Equation
Pant(1)=exp(A-B/(Ti+C))*0.01;
Pant(2)=Pant(1);
liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Pant(1)*(b-V))/a)-V;
Vant(1)=fsolve(liquid,b,options)/1000/MM;
vapor=@(V) (R*Ti/Pant(2)+b-a/Pant(2)*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
Vant(2)=fsolve(vapor,R*Ti/Pant(1),options)/1000/MM;
% Fugacity Test starting with Psat calculated with Antoine Equation
Paux=Pant(1);
iteA(1)=1;
PiteA(1)=Paux;
IPA(1)="Saturation Pressure calculated with Antoine Equation";
k=2;
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
    iteA(k)=k;
    PiteA(k)=Paux;
    IPA(k)="Saturation Pressure calculated with Antoine Equation";
    k=k+1;
end
% Find Psat, Vliquid, and Vvapor using the experimental data matrix
% Isotherm Temperature
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
Pexp(1)=table2array(data2(app.IsothermTemperature.Value,1));
Pexp(2)=table2array(data2(app.IsothermTemperature.Value,1));
Vexp(1)=table2array(data2(app.IsothermTemperature.Value,2));
Vexp(2)=table2array(data2(app.IsothermTemperature.Value,3));
if ~(~ismissing(Pexp(1)) && string(Pexp(1))~="NaN")
    Pexp(1)=NaN;
    Pexp(2)=NaN;
end
if ~(~ismissing(Vexp(1)) && string(Vexp(1))~="NaN")
    Vexp(1)=NaN;
end
if ~(~ismissing(Vexp(2)) && string(Vexp(2))~="NaN")
    Vexp(2)=NaN;
end
if ~isnan(Vexp(1)) && ~isnan(Pexp(1))
    Zexl=string(Pexp(1)*Vexp(1)*1000*MM/(R*Ti));
else
    Zexl="NA";
end
if ~isnan(Vexp(2)) && ~isnan(Pexp(2))
    Zexv=string(Pexp(2)*Vexp(2)*1000*MM/(R*Ti));
else
    Zexv="NA";
end
% Figure 1: Isotherm given Temperature on a PV Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Vfug,Pfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Vant,Pant,"Marker","^","LineStyle","none","Color","r");
plot(app.Figure1,Vexp,Pexp,"Marker","o","LineStyle","none","Color",[0.1 0.5 0.1]);
plot(app.Figure1,Vfug,Pfug,"LineStyle","--","Color","b");
plot(app.Figure1,V,P,"Color",[0.5 0 0.5]);
Vmin=min([min(V) Vfug(1) Vant(1) Vexp(1)]);
Vmax=max([max(V) Vfug(2) Vant(2) Vexp(2)]);
axis(app.Figure1,[max([0 Vmin-0.1/MM]) Vmax+0.1/MM Pmin-10 Pmax+10]);
if eos==1
    aux=strcat("van der Waals - ",app.Compound.Value," @ ",num2str(Ti)," K");
elseif eos==2
    aux=strcat("Redlich-Kwong - ",app.Compound.Value," @ ",num2str(Ti)," K");
elseif eos==3
    aux=strcat("Soave-Redlich-Kwong - ",app.Compound.Value," @ ",num2str(Ti)," K");
else
    aux=strcat("Peng-Robinson - ",app.Compound.Value," @ ",num2str(Ti)," K");
end
title(app.Figure1,aux);
legend(app.Figure1,{'Fugacity Test','Antoine Equation','Experimental Data'},"Box","on","LineWidth",1,"Location","southoutside");
hold(app.Figure1,"off");
% Figure 2: Fugacity Test - Pressure vs Iteration Number
hold(app.Figure2,"on");
plot(app.Figure2,ite,Pite,"Marker","*","LineStyle","none","Color","b","LineStyle","--");
plot(app.Figure2,iteA,PiteA,"Marker","^","LineStyle","none","Color","r","LineStyle","--");
h=legend(app.Figure2,{'Point close to the Maximum of the Loop of the EoS','Saturation Pressure calculated with Antoine Equation'},"Box","on","LineWidth",1,"Location","southoutside");
title(h,"Initial Point");
hold(app.Figure2,"off");
% Figure 3: Fugacity vs Pressure
hold(app.Figure3,"on");
plot(app.Figure3,Pf,fl,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure3,Pf,fv,"Marker","*","LineStyle","none","Color","r");
legend(app.Figure3,{'Liquid Fugacity','Vapor Fugacity'},"Box","on","LineWidth",1,"Location","southoutside");
hold(app.Figure3,"off");
% Report results 3: Fugacity vs Pressure
app.Table3.Data=[string(Pf);string(fl);string(fv)]';
% Report results 2: Fugacity Test - Pressure vs Iteration Number
app.Table2.Data=[IP,IPA;string(ite),string(iteA);string(Pite),string(PiteA)]';
% Report results 1: Isotherm given Temperature on a PV Diagram
phase=strings;
Pp=strings;
Zp=strings;
Vp=strings;
k=1;
% Liquid
step=max([floor(jl/100) 1]);
j=1;
while j<=jl
    phase(k)="Liquid";
    Pp(k)=string(P(j));
    Zp(k)=string(P(j)*V(j)*1000*MM/(R*Ti));
    Vp(k)=string(V(j));
    j=j+step;
    k=k+1;
end
% Saturated Liquid-Vapor
% Test Fugacity: Choice of thermodynamically possible cases
if Pfug(1)<Pt
    phase(k)="*Saturated Liquid (Fugacity Test)";
elseif Pfug(1)>Pc
    phase(k)="**Saturated Liquid (Fugacity Test)";
else
    phase(k)="Saturated Liquid (Fugacity Test)";
end
Pp(k)=string(Pfug(1));
Zp(k)=string(Pfug(1)*Vfug(1)*1000*MM/(R*Ti));
Vp(k)=string(Vfug(1));
k=k+1;
if Pfug(1)<Pt
    phase(k)="*Saturated Vapor (Fugacity Test)";
elseif Pfug(1)>Pc
    phase(k)="**Saturated Vapor (Fugacity Test)";
else
    phase(k)="Saturated Vapor (Fugacity Test)";
end
Pp(k)=string(Pfug(1));
Zp(k)=string(Pfug(2)*Vfug(2)*1000*MM/(R*Ti));
Vp(k)=string(Vfug(2));
k=k+1;
% Antoine Equation: Choice of thermodynamically possible cases
if Pant(1)<Pt
    phase(k)="*Saturated Liquid (Antoine Equation)";
elseif Pant(1)>Pc
    phase(k)="**Saturated Liquid (Antoine Equation)";
else
    phase(k)="Saturated Liquid (Antoine Equation)";
end
Pp(k)=string(Pant(1));
Zp(k)=string(Pant(1)*Vant(1)*1000*MM/(R*Ti));
Vp(k)=string(Vant(1));
k=k+1;
if Pant(1)<Pt
    phase(k)="*Saturated Vapor (Antoine Equation)";
elseif Pant(1)>Pc
    phase(k)="**Saturated Vapor (Antoine Equation)";
else
    phase(k)="Saturated Vapor (Antoine Equation)";
end
Pp(k)=string(Pant(1));
Zp(k)=string(Pant(2)*Vant(2)*1000*MM/(R*Ti));
Vp(k)=string(Vant(2));
k=k+1;
% Experimental data
if ~isnan(Pexp(1))
    Pex=string(Pexp(1));
else
    Pex="NA";
end
if ~isnan(Vexp(1))
    Vexl=string(Vexp(1));
else
    Vexl="NA";
end
if ~isnan(Vexp(2))
    Vexv=string(Vexp(2));
else
    Vexv="NA";
end
phase(k)="Saturated Liquid (Experimental Data)";
Pp(k)=Pex;
Zp(k)=Zexl;
Vp(k)=Vexl;
k=k+1;
phase(k)="Saturated Vapor (Experimental Data)";
Pp(k)=Pex;
Zp(k)=Zexv;
Vp(k)=Vexv;
k=k+1;
% Vapor
% Find first point in the vapor phase
j=jv;
step=max([floor((length(P)-jv+1)/100) 1]);
while j<=length(P)
    phase(k)="Vapor";
    Pp(k)=string(P(j));
    Zp(k)=string(P(j)*V(j)*1000*MM/(R*Ti));
    Vp(k)=string(V(j));
    j=j+step;
    k=k+1;
end
app.Table1.Data=[phase;Pp;Zp;Vp]';
```