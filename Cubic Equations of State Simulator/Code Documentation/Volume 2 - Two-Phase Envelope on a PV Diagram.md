# Two-Phase Envelope on a PV Diagram

This is the second option in the volume menu. Its interface is programmed in "Volume2.mlapp" and it uses the function called "Two_Phase_PV_Diagram.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/volume2.jpg" width="628" height="540">

*Figure 1. Design View in Volume2.mlapp.*

### 1.2. Code View

```Matlab
classdef Volume2 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        TwoPhaseEnvelopeonaPVDiagramUIFigure  matlab.ui.Figure
        CriticalVolume             matlab.ui.control.EditField
        Volumem3kgEditFieldLabel   matlab.ui.control.Label
        CriticalPressure           matlab.ui.control.EditField
        PressurebarEditFieldLabel  matlab.ui.control.Label
        BackButton                 matlab.ui.control.Button
        ExportButton               matlab.ui.control.Button
        Label_2                    matlab.ui.control.Label
        Compound                   matlab.ui.control.DropDown
        CompoundDropDownLabel      matlab.ui.control.Label
        EoS                        matlab.ui.control.DropDown
        CubicEquationofStateDropDownLabel  matlab.ui.control.Label
        Label                      matlab.ui.control.Label
        Table1                     matlab.ui.control.Table
        TwoPhaseEnvelopeonaPVDiagramLabel  matlab.ui.control.Label
        Image                      matlab.ui.control.Image
        CalculateButton            matlab.ui.control.Button
        Figure1                    matlab.ui.control.UIAxes
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.TwoPhaseEnvelopeonaPVDiagramUIFigure,"north");
            % Compound
            data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds");
            app.Compound.Items=table2cell(data(:,1));
        end

        % Button pushed function: CalculateButton
        function CalculateButtonPushed(app, event)
            % Isotherm Temperatures
            data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
            tam=0;
            for i=1:height(data2)
                if ~ismissing(table2array(data2(i,1))) && string(table2array(data2(i,1)))~="NaN"
                    tam=tam+1;
                    break;
                end
            end
            if tam>0
                progressbar=uiprogressdlg(app.TwoPhaseEnvelopeonaPVDiagramUIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                Two_Phase_PV_Diagram;
                app.ExportButton.Visible="on";
                close(progressbar);
            else
                uialert(app.TwoPhaseEnvelopeonaPVDiagramUIFigure,"Input isotherm temperatures not found.","Data Status","Icon","warning");
            end
        end

        % Button pushed function: BackButton
        function BackButtonPushed(app, event)
            Volume;
            delete(app);
        end

        % Button pushed function: ExportButton
        function ExportButtonPushed(app, event)
            progressbar=uiprogressdlg(app.TwoPhaseEnvelopeonaPVDiagramUIFigure,"Title","Status","Message","Exporting","Indeterminate","on","Cancelable","off");
            drawnow;
            aux=app.Table1.Data;
            table1=table(aux(:,1),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)),str2double(aux(:,5)),str2double(aux(:,6)),str2double(aux(:,7)));
            table1.Properties.VariableNames{'Var1'}='Method';
            table1.Properties.VariableNames{'Var2'}='Tsat [K]';
            table1.Properties.VariableNames{'Var3'}='Psat [bar]';
            table1.Properties.VariableNames{'Var4'}='Zliquid';
            table1.Properties.VariableNames{'Var5'}='Zvapor';
            table1.Properties.VariableNames{'Var6'}='Vliquid [m3/kg]';
            table1.Properties.VariableNames{'Var7'}='Vvapor [m3/kg]';
            writecell(cell(5000,7),"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range","A1");
            writetable(table1,"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range","A5");
            writecell({'Compound'},"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range","A1");
            writecell({'Cubic Equation of State'},"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range","A2");
            writecell({'Critical Pressure [bar]'},"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range","A3");
            writecell({'Critical Volume [m3/kg]'},"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range","A4");
            writecell({app.Compound.Value},"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range","B1");
            writecell({app.EoS.Value},"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range","B2");
            writematrix(str2double({app.CriticalPressure.Value}),"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range","B3");
            writematrix(str2double({app.CriticalVolume.Value}),"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range","B4");
            for i=8:3:5+height(table1)
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range",[i,3,i,3])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range",['C',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range",[i,4,i,4])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range",['D',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range",[i,5,i,5])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range",['E',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range",[i,6,i,6])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range",['F',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range",[i,7,i,7])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PV Diagram.xlsx","Sheet","PV Diagram","Range",['G',num2str(i)]);
                end
            end
            close(progressbar);
            uialert(app.TwoPhaseEnvelopeonaPVDiagramUIFigure,"Finished Export.","Export Status","Icon","success");
        end

        % Value changed function: Compound
        function CompoundValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound");
            app.CriticalPressure.Value="";
            app.CriticalVolume.Value="";
            cla(app.Figure1);
            app.Table1.Data={};
        end

        % Value changed function: EoS
        function EoSValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound");
            app.CriticalPressure.Value="";
            app.CriticalVolume.Value="";
            cla(app.Figure1);
            app.Table1.Data={};
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create TwoPhaseEnvelopeonaPVDiagramUIFigure and hide until all components are created
            app.TwoPhaseEnvelopeonaPVDiagramUIFigure = uifigure('Visible', 'off');
            app.TwoPhaseEnvelopeonaPVDiagramUIFigure.Color = [1 1 1];
            app.TwoPhaseEnvelopeonaPVDiagramUIFigure.Position = [100 100 784 675];
            app.TwoPhaseEnvelopeonaPVDiagramUIFigure.Name = 'Two-Phase Envelope on a PV Diagram';
            app.TwoPhaseEnvelopeonaPVDiagramUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.TwoPhaseEnvelopeonaPVDiagramUIFigure.Resize = 'off';

            % Create Figure1
            app.Figure1 = uiaxes(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            title(app.Figure1, 'EoS - Compound')
            xlabel(app.Figure1, 'V [m^3/kg]')
            ylabel(app.Figure1, 'P_{sat} [bar]')
            zlabel(app.Figure1, 'Z')
            app.Figure1.XScale = 'log';
            app.Figure1.XMinorTick = 'on';
            app.Figure1.XGrid = 'on';
            app.Figure1.XMinorGrid = 'on';
            app.Figure1.YGrid = 'on';
            app.Figure1.Position = [13 77 463 406];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.TwoPhaseEnvelopeonaPVDiagramUIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [572 508 103 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Image
            app.Image = uiimage(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            app.Image.Position = [126 511 127 103];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create TwoPhaseEnvelopeonaPVDiagramLabel
            app.TwoPhaseEnvelopeonaPVDiagramLabel = uilabel(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            app.TwoPhaseEnvelopeonaPVDiagramLabel.HorizontalAlignment = 'center';
            app.TwoPhaseEnvelopeonaPVDiagramLabel.FontSize = 20;
            app.TwoPhaseEnvelopeonaPVDiagramLabel.FontWeight = 'bold';
            app.TwoPhaseEnvelopeonaPVDiagramLabel.FontColor = [0.1412 0.302 0.4784];
            app.TwoPhaseEnvelopeonaPVDiagramLabel.Position = [129 630 548 26];
            app.TwoPhaseEnvelopeonaPVDiagramLabel.Text = 'Two-Phase Envelope on a PV Diagram';

            % Create Table1
            app.Table1 = uitable(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            app.Table1.ColumnName = {'Method'; 'Tsat [K]'; 'Psat [bar]'; 'Zliquid'; 'Zvapor'; 'Vliquid [m3/kg]'; 'Vvapor [m3/kg]'};
            app.Table1.RowName = {};
            app.Table1.Position = [497 205 271 278];

            % Create Label
            app.Label = uilabel(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            app.Label.FontWeight = 'bold';
            app.Label.FontColor = [0.1412 0.302 0.4784];
            app.Label.Position = [14 11 584 56];
            app.Label.Text = {'Symbology'; 'NA: Not Available.'; '*: Thermodynamically not possible case because the pressure is less than the triple pressure.'; '**: Thermodynamically not possible case because the pressure is greater than the critical pressure.'};

            % Create CubicEquationofStateDropDownLabel
            app.CubicEquationofStateDropDownLabel = uilabel(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            app.CubicEquationofStateDropDownLabel.HorizontalAlignment = 'right';
            app.CubicEquationofStateDropDownLabel.FontWeight = 'bold';
            app.CubicEquationofStateDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CubicEquationofStateDropDownLabel.Position = [278 544 141 22];
            app.CubicEquationofStateDropDownLabel.Text = 'Cubic Equation of State';

            % Create EoS
            app.EoS = uidropdown(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            app.EoS.Items = {'van der Waals', 'Redlich-Kwong', 'Soave-Redlich-Kwong', 'Peng-Robinson'};
            app.EoS.ValueChangedFcn = createCallbackFcn(app, @EoSValueChanged, true);
            app.EoS.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EoS.Position = [435 544 241 22];
            app.EoS.Value = 'van der Waals';

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [280 580 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [435 580 242 22];
            app.Compound.Value = {};

            % Create Label_2
            app.Label_2 = uilabel(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            app.Label_2.HorizontalAlignment = 'center';
            app.Label_2.FontWeight = 'bold';
            app.Label_2.FontColor = [0.1412 0.302 0.4784];
            app.Label_2.Position = [593 173 80 22];
            app.Label_2.Text = 'Critical Point';

            % Create ExportButton
            app.ExportButton = uibutton(app.TwoPhaseEnvelopeonaPVDiagramUIFigure, 'push');
            app.ExportButton.ButtonPushedFcn = createCallbackFcn(app, @ExportButtonPushed, true);
            app.ExportButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.ExportButton.FontWeight = 'bold';
            app.ExportButton.FontColor = [0.1412 0.302 0.4784];
            app.ExportButton.Visible = 'off';
            app.ExportButton.Position = [669 52 100 22];
            app.ExportButton.Text = 'Export';

            % Create BackButton
            app.BackButton = uibutton(app.TwoPhaseEnvelopeonaPVDiagramUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [669 20 100 22];
            app.BackButton.Text = 'Back';

            % Create PressurebarEditFieldLabel
            app.PressurebarEditFieldLabel = uilabel(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            app.PressurebarEditFieldLabel.HorizontalAlignment = 'right';
            app.PressurebarEditFieldLabel.FontWeight = 'bold';
            app.PressurebarEditFieldLabel.FontColor = [0.1412 0.302 0.4784];
            app.PressurebarEditFieldLabel.Position = [497 141 103 22];
            app.PressurebarEditFieldLabel.Text = 'Pressure [bar]';

            % Create CriticalPressure
            app.CriticalPressure = uieditfield(app.TwoPhaseEnvelopeonaPVDiagramUIFigure, 'text');
            app.CriticalPressure.Editable = 'off';
            app.CriticalPressure.Position = [617 141 149 22];

            % Create Volumem3kgEditFieldLabel
            app.Volumem3kgEditFieldLabel = uilabel(app.TwoPhaseEnvelopeonaPVDiagramUIFigure);
            app.Volumem3kgEditFieldLabel.HorizontalAlignment = 'right';
            app.Volumem3kgEditFieldLabel.FontWeight = 'bold';
            app.Volumem3kgEditFieldLabel.FontColor = [0.1412 0.302 0.4784];
            app.Volumem3kgEditFieldLabel.Position = [497 107 103 22];
            app.Volumem3kgEditFieldLabel.Text = 'Volume [m3/kg]';

            % Create CriticalVolume
            app.CriticalVolume = uieditfield(app.TwoPhaseEnvelopeonaPVDiagramUIFigure, 'text');
            app.CriticalVolume.Editable = 'off';
            app.CriticalVolume.Position = [617 107 149 22];

            % Show the figure after all components are created
            app.TwoPhaseEnvelopeonaPVDiagramUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Volume2

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.TwoPhaseEnvelopeonaPVDiagramUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.TwoPhaseEnvelopeonaPVDiagramUIFigure)
        end
    end
end
```

## 2. MATLAB Code

```Matlab
% Assignment of parameter values depending on the input and through the database
clc;
cla(app.Figure1);
app.Table1.Data={};
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
Vc=table2array(data(app.Compound.Value,7))/1000/MM; % Critical Volume [m3/kg]
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
% Available temperatures
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
tam=0;
aux=strings;
for i=1:height(data2)
    if ~ismissing(table2array(data2(i,1))) && string(table2array(data2(i,1)))~="NaN"
        tam=tam+1;
        aux(tam)=string(table2array(data2(i,1)));
    end
end
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
b=omega*R*Tc/Pc;
Er=0.00001;
sizefug=1;
sizeant=1;
Vfug=[];
Pfug=[];
Vant=[];
Pant=[];
Vexp=zeros(1,2*tam);
Pexp=zeros(1,2*tam);
method=strings(1,3*tam);
T=strings(1,3*tam);
P=strings(1,3*tam);
Vl=strings(1,3*tam);
Vv=strings(1,3*tam);
Zl=strings(1,3*tam);
Zv=strings(1,3*tam);
% For each T in the compound database: Find Psat, Zliquid, Zvapor, Vliquid, and Vvapor
for i=1:tam
    Ti=str2double(aux(i));
    Tr=Ti/Tc;
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos==3
        alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
    elseif eos==4
        alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
    end
    a=psi*alpha*(R*Tc)^2/Pc;
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
    Paux=Paux2;
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
    % Save results
    ft=3*i-2;
    ae=3*i-1;
    ed=3*i;
    if Paux<Pt
        method(ft)="*Fugacity Test";
    elseif Paux>Pc
        method(ft)="**Fugacity Test";
    else
        method(ft)="Fugacity Test";
    end
    T(ft)=string(Ti);
    % Test Fugacity: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pfug(sizefug)=Paux;
        Vfug(sizefug)=Vliquid/1000/MM;
        sizefug=sizefug+1;
        Pfug(sizefug)=Paux;
        Vfug(sizefug)=Vvapor/1000/MM;
        sizefug=sizefug+1;
    end
    P(ft)=string(Paux);
    Vl(ft)=string(Vliquid/1000/MM);
    Vv(ft)=string(Vvapor/1000/MM);
    Zl(ft)=string(Zliquid);
    Zv(ft)=string(Zvapor);
    % Find Psat using Antoine Equation
    Paux=exp(A-B/(Ti+C))*0.01;
    liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Paux*(b-V))/a)-V;
    Vliquid=fsolve(liquid,b,options)/1000/MM;
    vapor=@(V) (R*Ti/Paux+b-a/Paux*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
    Vvapor=fsolve(vapor,R*Ti/Paux,options)/1000/MM;
    if Paux<Pt
        method(ae)="*Antoine Equation";
    elseif Paux>Pc
        method(ae)="**Antoine Equation";
    else
        method(ae)="Antoine Equation";
    end
    T(ae)=string(Ti);
    % Antoine Equation: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pant(sizeant)=Paux;
        Vant(sizeant)=Vliquid;
        sizeant=sizeant+1;
        Pant(sizeant)=Paux;
        Vant(sizeant)=Vvapor;
        sizeant=sizeant+1;
    end
    P(ae)=string(Paux);
    Vl(ae)=string(Vliquid);
    Vv(ae)=string(Vvapor);
    Zl(ae)=string(Paux*Vliquid*1000*MM/(R*Ti));
    Zv(ae)=string(Paux*Vvapor*1000*MM/(R*Ti));
    % Find Psat, Vliquid, and Vvapor using the experimental data matrix
    l=2*i-1;
    v=2*i;
    T(ed)=string(Ti);
    method(ed)="Experimental Data";
    data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
    Pexp(l)=table2array(data2(aux(i),1));
    Pexp(v)=table2array(data2(aux(i),1));
    Vexp(l)=table2array(data2(aux(i),2));
    Vexp(v)=table2array(data2(aux(i),3));
    if isnan(Pexp(l))
        P(ed)="NA";
    else
        P(ed)=string(Pexp(l));
    end
    if isnan(Vexp(l))
        Vl(ed)="NA";
    else
        Vl(ed)=string(Vexp(l));
    end
    if isnan(Vexp(v))
        Vv(ed)="NA";
    else
        Vv(ed)=string(Vexp(v));
    end
    if ~isnan(Vexp(l)) && ~isnan(Pexp(l))
        Zl(ed)=string(Pexp(l)*Vexp(l)*1000*MM/(R*Ti));
    else
        Zl(ed)="NA";
    end
    if ~isnan(Vexp(v)) && ~isnan(Pexp(v))
        Zv(ed)=string(Pexp(v)*Vexp(v)*1000*MM/(R*Ti));
    else
        Zv(ed)="NA";
    end
end
% Critical Point
Pexp(2*height(aux)+1)=Pc;
Vexp(2*height(aux)+1)=Vc;
app.CriticalPressure.Value=string(Pc);
app.CriticalVolume.Value=string(Vc);
% Figure: Two-Phase Envelope on a PV Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Vfug,Pfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Vant,Pant,"Marker","^","Linestyle","none","Color","r");
plot(app.Figure1,Vexp,Pexp,"Marker","o","Linestyle","none","Color",[0.1 0.5 0.1]);
Vmax=max([max(Vfug) max(Vant) max(Vexp)]);
Vmin=min([min(Vfug) min(Vant) min(Vexp)]);
Pmin=max([0 Pt-10]);
if Pmin==0
    Pmax=Pc+Pt;
else
    Pmax=Pt+10;
end
axis(app.Figure1,[max([0 Vmin-0.1/MM]) Vmax+0.1/MM Pmin Pmax]);
if eos==1
    aux=strcat("van der Waals - ",app.Compound.Value);
elseif eos==2
    aux=strcat("Redlich-Kwong - ",app.Compound.Value);
elseif eos==3
    aux=strcat("Soave-Redlich-Kwong - ",app.Compound.Value);
else
    aux=strcat("Peng-Robinson - ",app.Compound.Value);
end
title(app.Figure1,aux);
legend(app.Figure1,{'Fugacity Test','Antoine Equation','Experimental Data'},"Box","on","LineWidth",1,"Location","southoutside");
hold(app.Figure1,"off");
app.Table1.Data=[method;T;P;Zl;Zv;Vl;Vv]';
```