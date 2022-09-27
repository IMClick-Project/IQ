# PVT Diagram given Isotherm Temperatures

This is the third option in the volume menu. Its interface is programmed in "Volume3.mlapp" and it uses the function called "PVT_Diagram_given_Isotherm_Temperatures.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/volume3.jpg" width="574" height="572">

*Figure 1. Design View in Volume3.mlapp.*

### 1.2. Code View

```Matlab
classdef Volume3 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        PVTDiagramgivenIsothermTemperaturesUIFigure  matlab.ui.Figure
        Compound               matlab.ui.control.DropDown
        CompoundDropDownLabel  matlab.ui.control.Label
        EoS                    matlab.ui.control.DropDown
        CubicEquationofStateDropDownLabel  matlab.ui.control.Label
        BackButton             matlab.ui.control.Button
        PVTDiagramgivenIsothermTemperaturesLabel  matlab.ui.control.Label
        Image                  matlab.ui.control.Image
        CalculateButton        matlab.ui.control.Button
        Figure1                matlab.ui.control.UIAxes
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.PVTDiagramgivenIsothermTemperaturesUIFigure,"north");
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
                progressbar=uiprogressdlg(app.PVTDiagramgivenIsothermTemperaturesUIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                PVT_Diagram_given_Isotherm_Temperatures;
                close(progressbar);
            else
                uialert(app.PVTDiagramgivenIsothermTemperaturesUIFigure,"Input isotherm temperatures not found.","Data Status","Icon","warning");
            end
        end

        % Button pushed function: BackButton
        function BackButtonPushed(app, event)
            Volume;
            delete(app);
        end

        % Value changed function: Compound
        function CompoundValueChanged(app, event)
            clc;
            title(app.Figure1,"EoS - Compound");
            cla(app.Figure1);
        end

        % Value changed function: EoS
        function EoSValueChanged(app, event)
            clc;
            title(app.Figure1,"EoS - Compound");
            cla(app.Figure1);
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create PVTDiagramgivenIsothermTemperaturesUIFigure and hide until all components are created
            app.PVTDiagramgivenIsothermTemperaturesUIFigure = uifigure('Visible', 'off');
            app.PVTDiagramgivenIsothermTemperaturesUIFigure.Color = [1 1 1];
            app.PVTDiagramgivenIsothermTemperaturesUIFigure.Position = [100 100 634 632];
            app.PVTDiagramgivenIsothermTemperaturesUIFigure.Name = 'PVT Diagram given Isotherm Temperatures';
            app.PVTDiagramgivenIsothermTemperaturesUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.PVTDiagramgivenIsothermTemperaturesUIFigure.Resize = 'off';

            % Create Figure1
            app.Figure1 = uiaxes(app.PVTDiagramgivenIsothermTemperaturesUIFigure);
            title(app.Figure1, 'EoS - Compound')
            xlabel(app.Figure1, 'T [K]')
            ylabel(app.Figure1, 'V [m^3/kg]')
            zlabel(app.Figure1, 'P [bar]')
            app.Figure1.XDir = 'reverse';
            app.Figure1.YScale = 'log';
            app.Figure1.YMinorTick = 'on';
            app.Figure1.XGrid = 'on';
            app.Figure1.YGrid = 'on';
            app.Figure1.ZGrid = 'on';
            app.Figure1.Position = [50 57 532 394];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.PVTDiagramgivenIsothermTemperaturesUIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [478 467 103 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Image
            app.Image = uiimage(app.PVTDiagramgivenIsothermTemperaturesUIFigure);
            app.Image.Position = [50 467 127 103];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create PVTDiagramgivenIsothermTemperaturesLabel
            app.PVTDiagramgivenIsothermTemperaturesLabel = uilabel(app.PVTDiagramgivenIsothermTemperaturesUIFigure);
            app.PVTDiagramgivenIsothermTemperaturesLabel.HorizontalAlignment = 'center';
            app.PVTDiagramgivenIsothermTemperaturesLabel.FontSize = 20;
            app.PVTDiagramgivenIsothermTemperaturesLabel.FontWeight = 'bold';
            app.PVTDiagramgivenIsothermTemperaturesLabel.FontColor = [0.1412 0.302 0.4784];
            app.PVTDiagramgivenIsothermTemperaturesLabel.Position = [44 583 548 26];
            app.PVTDiagramgivenIsothermTemperaturesLabel.Text = 'PVT Diagram given Isotherm Temperatures';

            % Create BackButton
            app.BackButton = uibutton(app.PVTDiagramgivenIsothermTemperaturesUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [519 20 100 22];
            app.BackButton.Text = 'Back';

            % Create CubicEquationofStateDropDownLabel
            app.CubicEquationofStateDropDownLabel = uilabel(app.PVTDiagramgivenIsothermTemperaturesUIFigure);
            app.CubicEquationofStateDropDownLabel.HorizontalAlignment = 'right';
            app.CubicEquationofStateDropDownLabel.FontWeight = 'bold';
            app.CubicEquationofStateDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CubicEquationofStateDropDownLabel.Position = [182 503 141 22];
            app.CubicEquationofStateDropDownLabel.Text = 'Cubic Equation of State';

            % Create EoS
            app.EoS = uidropdown(app.PVTDiagramgivenIsothermTemperaturesUIFigure);
            app.EoS.Items = {'van der Waals', 'Redlich-Kwong', 'Soave-Redlich-Kwong', 'Peng-Robinson'};
            app.EoS.ValueChangedFcn = createCallbackFcn(app, @EoSValueChanged, true);
            app.EoS.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EoS.Position = [339 503 241 22];
            app.EoS.Value = 'van der Waals';

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.PVTDiagramgivenIsothermTemperaturesUIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [183 539 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.PVTDiagramgivenIsothermTemperaturesUIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [338 539 242 22];
            app.Compound.Value = {};

            % Show the figure after all components are created
            app.PVTDiagramgivenIsothermTemperaturesUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Volume3

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.PVTDiagramgivenIsothermTemperaturesUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.PVTDiagramgivenIsothermTemperaturesUIFigure)
        end
    end
end
```

## 2. MATLAB Code

```Matlab
% Assignment of parameter values depending on the input and through the database
clc;
cla(app.Figure1);
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
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
b=omega*R*Tc/Pc;
Er=0.00001;
% For each T in the compound database: Plot isotherms
hold(app.Figure1,"on");
Vsatmax=0;
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
    P=[];
    V=[];
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
    Psat=Paux;
    Vsatmax=max([Vsatmax Vvapor/1000/MM]);
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
    % Liquid
    step=(Vliquid-Vstart)/100;
    Vnext=Vstart+step;
    P(1)=R*Ti/(Vstart-b)-a/((Vstart+epsilon*b)*(Vstart+sigma*b));
    V(1)=Vstart/1000/MM;
    P(2)=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    V(2)=Vnext/1000/MM;
    j=2;
    while Vnext<Vliquid
        Paux=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
        j=j+1;
        P(j)=Paux;
        V(j)=Vnext/1000/MM;
        Vnext=Vnext+step;
    end
    % Saturated Liquid-Vapor
    j=j+1;
    P(j)=Psat;
    V(j)=Vliquid/1000/MM;
    j=j+1;
    P(j)=Psat;
    V(j)=Vvapor/1000/MM;
    % Vapor
    Vnext=Vvapor+1;
    Vmax=Vvapor+10000;
    step=(Vmax-Vnext)/100;
    while Vnext<Vmax
        Paux=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
        j=j+1;
        P(j)=Paux;
        V(j)=Vnext/1000/MM;
        Vnext=Vnext+step;
    end
    plot3(app.Figure1,ones(j)*Ti,V,P);
end
hold(app.Figure1,"off");
view(app.Figure1,[45,45,45]);
ylim(app.Figure1,[0 Vsatmax*5]);
zlim(app.Figure1,[max([0 Pt-10]) Pc*1.1]);
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
```