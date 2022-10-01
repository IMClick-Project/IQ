# PHT Surface given Isobar Pressures

This is the sixth option in the enthalpy menu. Its interface is programmed in "Enthalpy6.mlapp" and it uses the function called "PHT_Surface_given_Isobar_Pressures.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/enthalpy6.jpg" width="848" height="569">

*Figure 1. Design View in Enthalpy6.mlapp.*

### 1.2. Code View

```Matlab
classdef Enthalpy6 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        PHTSurfacegivenIsobarPressuresUIFigure  matlab.ui.Figure
        ReferenceEnthalpy          matlab.ui.control.EditField
        EnthalpykJkgLabel          matlab.ui.control.Label
        ReferencePressure          matlab.ui.control.EditField
        PressurebarEditFieldLabel  matlab.ui.control.Label
        ReferenceTemperature       matlab.ui.control.EditField
        TemperatureKLabel          matlab.ui.control.Label
        ReferenceState             matlab.ui.control.EditField
        StateLabel                 matlab.ui.control.Label
        Label                      matlab.ui.control.Label
        CalculateButton            matlab.ui.control.Button
        Compound                   matlab.ui.control.DropDown
        CompoundDropDownLabel      matlab.ui.control.Label
        EoS                        matlab.ui.control.DropDown
        CubicEquationofStateDropDownLabel  matlab.ui.control.Label
        BackButton                 matlab.ui.control.Button
        PHTSurfacegivenIsobarPressuresLabel  matlab.ui.control.Label
        Image                      matlab.ui.control.Image
        Figure1                    matlab.ui.control.UIAxes
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.PHTSurfacegivenIsobarPressuresUIFigure,"north");
            % Compound
            data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds");
            app.Compound.Items=table2cell(data(:,1));
            % Reference State
            data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds","ReadRowNames",1);
            app.ReferenceState.Value=string(table2array(data(app.Compound.Value,11)));
            if ismissing(table2array(data(app.Compound.Value,12))) || string(table2array(data(app.Compound.Value,12)))=="NaN"
                app.ReferenceTemperature.Value="NaN";
            else
                app.ReferenceTemperature.Value=string(table2array(data(app.Compound.Value,12)));
            end
            if ismissing(table2array(data(app.Compound.Value,13))) || string(table2array(data(app.Compound.Value,13)))=="NaN"
                app.ReferencePressure.Value="NaN";
            else
                app.ReferencePressure.Value=string(table2array(data(app.Compound.Value,13)));
            end
            if ismissing(table2array(data(app.Compound.Value,14))) || string(table2array(data(app.Compound.Value,14)))=="NaN"
                app.ReferenceEnthalpy.Value="NaN";
            else
                app.ReferenceEnthalpy.Value=string(table2array(data(app.Compound.Value,14)));
            end
        end

        % Button pushed function: BackButton
        function BackButtonPushed(app, event)
            Enthalpy;
            delete(app);
        end

        % Value changed function: Compound
        function CompoundValueChanged(app, event)
            clc;
            title(app.Figure1,"EoS - Compound");
            cla(app.Figure1);
            % Reference State
            data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds","ReadRowNames",1);
            app.ReferenceState.Value=string(table2array(data(app.Compound.Value,11)));
            if ismissing(table2array(data(app.Compound.Value,12))) || string(table2array(data(app.Compound.Value,12)))=="NaN"
                app.ReferenceTemperature.Value="NaN";
            else
                app.ReferenceTemperature.Value=string(table2array(data(app.Compound.Value,12)));
            end
            if ismissing(table2array(data(app.Compound.Value,13))) || string(table2array(data(app.Compound.Value,13)))=="NaN"
                app.ReferencePressure.Value="NaN";
            else
                app.ReferencePressure.Value=string(table2array(data(app.Compound.Value,13)));
            end
            if ismissing(table2array(data(app.Compound.Value,14))) || string(table2array(data(app.Compound.Value,14)))=="NaN"
                app.ReferenceEnthalpy.Value="NaN";
            else
                app.ReferenceEnthalpy.Value=string(table2array(data(app.Compound.Value,14)));
            end
        end

        % Value changed function: EoS
        function EoSValueChanged(app, event)
            clc;
            title(app.Figure1,"EoS - Compound");
            cla(app.Figure1);
        end

        % Button pushed function: CalculateButton
        function CalculateButtonPushed(app, event)
            % Isobar Pressures
            data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
            tam=0;
            for i=1:height(data2)
                if ~ismissing(table2array(data2(i,2))) && string(table2array(data2(i,2)))~="NaN"
                    tam=tam+1;
                    break;
                end
            end
            if tam>0 && app.ReferenceState.Value~="NaN" && app.ReferenceTemperature.Value~="NaN" && app.ReferencePressure.Value~="NaN" && app.ReferenceEnthalpy.Value~="NaN"
                progressbar=uiprogressdlg(app.PHTSurfacegivenIsobarPressuresUIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                PHT_Surface_given_Isobar_Pressures;
                close(progressbar);
            elseif app.ReferenceState.Value=="NaN" || app.ReferenceTemperature.Value=="NaN" || app.ReferencePressure.Value=="NaN" || app.ReferenceEnthalpy.Value=="NaN"
                uialert(app.PHTSurfacegivenIsobarPressuresUIFigure,"Incomplete Data.","Data Status","Icon","warning");
            else
                uialert(app.PHTSurfacegivenIsobarPressuresUIFigure,"Input isobar pressures not found.","Data Status","Icon","warning");
            end
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create PHTSurfacegivenIsobarPressuresUIFigure and hide until all components are created
            app.PHTSurfacegivenIsobarPressuresUIFigure = uifigure('Visible', 'off');
            app.PHTSurfacegivenIsobarPressuresUIFigure.Color = [1 1 1];
            app.PHTSurfacegivenIsobarPressuresUIFigure.Position = [100 100 943 632];
            app.PHTSurfacegivenIsobarPressuresUIFigure.Name = 'PHT Surface given Isobar Pressures';
            app.PHTSurfacegivenIsobarPressuresUIFigure.Icon = 'Logoico.png';
            app.PHTSurfacegivenIsobarPressuresUIFigure.Resize = 'off';

            % Create Figure1
            app.Figure1 = uiaxes(app.PHTSurfacegivenIsobarPressuresUIFigure);
            title(app.Figure1, 'EoS - Compound')
            xlabel(app.Figure1, 'T [K]')
            ylabel(app.Figure1, 'H [kJ/kg]')
            zlabel(app.Figure1, 'P [bar]')
            app.Figure1.XDir = 'reverse';
            app.Figure1.XGrid = 'on';
            app.Figure1.YGrid = 'on';
            app.Figure1.ZGrid = 'on';
            app.Figure1.Position = [211 53 532 400];

            % Create Image
            app.Image = uiimage(app.PHTSurfacegivenIsobarPressuresUIFigure);
            app.Image.Position = [45 462 127 103];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create PHTSurfacegivenIsobarPressuresLabel
            app.PHTSurfacegivenIsobarPressuresLabel = uilabel(app.PHTSurfacegivenIsobarPressuresUIFigure);
            app.PHTSurfacegivenIsobarPressuresLabel.HorizontalAlignment = 'center';
            app.PHTSurfacegivenIsobarPressuresLabel.FontSize = 20;
            app.PHTSurfacegivenIsobarPressuresLabel.FontWeight = 'bold';
            app.PHTSurfacegivenIsobarPressuresLabel.FontColor = [0.1412 0.302 0.4784];
            app.PHTSurfacegivenIsobarPressuresLabel.Position = [1 589 943 26];
            app.PHTSurfacegivenIsobarPressuresLabel.Text = 'PHT Surface given Isobar Pressures';

            % Create BackButton
            app.BackButton = uibutton(app.PHTSurfacegivenIsobarPressuresUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [805 23 100 22];
            app.BackButton.Text = 'Back';

            % Create CubicEquationofStateDropDownLabel
            app.CubicEquationofStateDropDownLabel = uilabel(app.PHTSurfacegivenIsobarPressuresUIFigure);
            app.CubicEquationofStateDropDownLabel.HorizontalAlignment = 'right';
            app.CubicEquationofStateDropDownLabel.FontWeight = 'bold';
            app.CubicEquationofStateDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CubicEquationofStateDropDownLabel.Position = [182 482 141 22];
            app.CubicEquationofStateDropDownLabel.Text = 'Cubic Equation of State';

            % Create EoS
            app.EoS = uidropdown(app.PHTSurfacegivenIsobarPressuresUIFigure);
            app.EoS.Items = {'van der Waals', 'Redlich-Kwong', 'Soave-Redlich-Kwong', 'Peng-Robinson'};
            app.EoS.ValueChangedFcn = createCallbackFcn(app, @EoSValueChanged, true);
            app.EoS.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EoS.Position = [339 482 241 22];
            app.EoS.Value = 'van der Waals';

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.PHTSurfacegivenIsobarPressuresUIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [183 518 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.PHTSurfacegivenIsobarPressuresUIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [338 518 242 22];
            app.Compound.Value = {};

            % Create CalculateButton
            app.CalculateButton = uibutton(app.PHTSurfacegivenIsobarPressuresUIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [805 431 103 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Label
            app.Label = uilabel(app.PHTSurfacegivenIsobarPressuresUIFigure);
            app.Label.HorizontalAlignment = 'center';
            app.Label.FontWeight = 'bold';
            app.Label.FontColor = [0.1412 0.302 0.4784];
            app.Label.Position = [713 561 93 22];
            app.Label.Text = 'Reference Data';

            % Create StateLabel
            app.StateLabel = uilabel(app.PHTSurfacegivenIsobarPressuresUIFigure);
            app.StateLabel.HorizontalAlignment = 'right';
            app.StateLabel.FontWeight = 'bold';
            app.StateLabel.FontColor = [0.1412 0.302 0.4784];
            app.StateLabel.Position = [612 539 103 22];
            app.StateLabel.Text = 'State';

            % Create ReferenceState
            app.ReferenceState = uieditfield(app.PHTSurfacegivenIsobarPressuresUIFigure, 'text');
            app.ReferenceState.Editable = 'off';
            app.ReferenceState.Position = [732 539 176 22];

            % Create TemperatureKLabel
            app.TemperatureKLabel = uilabel(app.PHTSurfacegivenIsobarPressuresUIFigure);
            app.TemperatureKLabel.HorizontalAlignment = 'right';
            app.TemperatureKLabel.FontWeight = 'bold';
            app.TemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.TemperatureKLabel.Position = [612 513 103 22];
            app.TemperatureKLabel.Text = 'Temperature [K]';

            % Create ReferenceTemperature
            app.ReferenceTemperature = uieditfield(app.PHTSurfacegivenIsobarPressuresUIFigure, 'text');
            app.ReferenceTemperature.Editable = 'off';
            app.ReferenceTemperature.Position = [732 513 176 22];

            % Create PressurebarEditFieldLabel
            app.PressurebarEditFieldLabel = uilabel(app.PHTSurfacegivenIsobarPressuresUIFigure);
            app.PressurebarEditFieldLabel.HorizontalAlignment = 'right';
            app.PressurebarEditFieldLabel.FontWeight = 'bold';
            app.PressurebarEditFieldLabel.FontColor = [0.1412 0.302 0.4784];
            app.PressurebarEditFieldLabel.Position = [612 488 103 22];
            app.PressurebarEditFieldLabel.Text = 'Pressure [bar]';

            % Create ReferencePressure
            app.ReferencePressure = uieditfield(app.PHTSurfacegivenIsobarPressuresUIFigure, 'text');
            app.ReferencePressure.Editable = 'off';
            app.ReferencePressure.Position = [732 488 176 22];

            % Create EnthalpykJkgLabel
            app.EnthalpykJkgLabel = uilabel(app.PHTSurfacegivenIsobarPressuresUIFigure);
            app.EnthalpykJkgLabel.HorizontalAlignment = 'right';
            app.EnthalpykJkgLabel.FontWeight = 'bold';
            app.EnthalpykJkgLabel.FontColor = [0.1412 0.302 0.4784];
            app.EnthalpykJkgLabel.Position = [612 462 103 22];
            app.EnthalpykJkgLabel.Text = 'Enthalpy [kJ/kg]';

            % Create ReferenceEnthalpy
            app.ReferenceEnthalpy = uieditfield(app.PHTSurfacegivenIsobarPressuresUIFigure, 'text');
            app.ReferenceEnthalpy.Editable = 'off';
            app.ReferenceEnthalpy.Position = [732 462 176 22];

            % Show the figure after all components are created
            app.PHTSurfacegivenIsobarPressuresUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Enthalpy6

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.PHTSurfacegivenIsobarPressuresUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.PHTSurfacegivenIsobarPressuresUIFigure)
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
% Cp(T) parameters
Acp=table2array(data(app.Compound.Value,19));
Bcp=table2array(data(app.Compound.Value,20));
Ccp=table2array(data(app.Compound.Value,21));
Dcp=table2array(data(app.Compound.Value,22));
Ecp=table2array(data(app.Compound.Value,23));
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
    derivate=0;
elseif eos==2 || eos==3
    epsilon=0;
    sigma=1;
    omega=0.08664;
    psi=0.42748;
    if eos==2
        derivate=-1/2;
    else
        p=0.480+1.574*w-0.176*w^2;
    end
else
    epsilon=1-2^(1/2);
    sigma=1+2^(1/2);
    omega=0.07780;
    psi=0.45724;
    p=0.37464+1.54226*w-0.26992*w^2;
end
% Available pressures
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
tam=0;
aux=strings;
Pindex=[];
for i=1:height(data2)
    if ~ismissing(table2array(data2(i,2))) && string(table2array(data2(i,2)))~="NaN"
        tam=tam+1;
        aux(tam)=string(table2array(data2(i,2)));
    end
end
% Reference Data
if app.ReferenceState.Value=="Ideal Gas" % Reference State 
    ref=1;
elseif app.ReferenceState.Value=="Real Liquid"
    ref=2;
else
    ref=3;
end
T0=str2double(app.ReferenceTemperature.Value); % Reference Temperature [K]
P0=str2double(app.ReferencePressure.Value); % Reference Pressure [bar]
H0=str2double(app.ReferenceEnthalpy.Value); % Reference Enthalpy [kJ/kg]
H0=H0*MM; % [kJ/kmol]
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
R2=8.314; % Ideal Gas Constant [J*K/mol/K]
Er=0.00001;
b=omega*R*Tc/Pc;
% Reference enthalpy calculation of reference data
if ref==1
    HR0=0;
else
    Tr=T0/Tc;
    beta=P0*b/(R*T0);
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos>2
        alpha=(1+p*(1-Tr^(1/2)))^2;
        derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
    end
    a=psi*alpha*(R*Tc)^2/Pc;
    q=a/(b*R*T0);
    if ref==2
        liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*T0+P0*(b-V))/a)-V;
        Vliquid=fsolve(liquid,b,options);
        Zliquid=P0*Vliquid/(R*T0);
        if eos==1 
            I=beta/(Zliquid+epsilon*beta);
        else
            I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
        end
        HR0=R2*T0*(Zliquid-1+(derivate-1)*q*I);
    else
        vapor=@(V) (R*T0/P0+b-a/P0*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
        Vvapor=fsolve(vapor,R*T0/P0,options);
        Zvapor=P0*Vvapor/(R*T0);
        if eos==1
            I=beta/(Zvapor+epsilon*beta);
        else
            I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
        end
        HR0=R2*T0*(Zvapor-1+(derivate-1)*q*I);
    end
end
Tbracket=[Tt Tc-0.1];
Pbracket=zeros(1,2);
% Fugacity Test to predict Psat for Tt and close to Tc
for i=1:2
    Ti=Tbracket(i);
    Tr=Ti/Tc;
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos>2
        alpha=(1+p*(1-Tr^(1/2)))^2;
        derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
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
    Pbracket(i)=Paux;
end
% For each P in the compound database: Plot isobar
hold(app.Figure1,"on");
Hsatmax=NaN;
Hsatmin=NaN;
for i=1:tam
    Pi=str2double(aux(i));
    if Pi<Pbracket(1) || Pi>Pbracket(2)
        continue;
    else 
        T=[];
        H=[];
        Pstart=Pbracket(1)-Pi;
        Pfinal=Pbracket(2)-Pi;
        Tstart=Tbracket(1);
        Tfinal=Tbracket(2);
        ite=0;
        % Pegasus method
        while abs(Pfinal)>Er && abs(Pstart)>Er && abs(Tstart-Tfinal)>Er
            Ti=Tfinal-(Tfinal-Tstart)*Pfinal/(Pfinal-Pstart);
            Tr=Ti/Tc;
            if eos==2
                alpha=Tr^(-1/2);
            elseif eos>2
                alpha=(1+p*(1-Tr^(1/2)))^2;
                derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
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
            if (Paux-Pi)*Pfinal<0 
                Tstart=Tfinal;  
                Pstart=Pfinal;
            else 
                Pstart=Pstart*Pfinal/(Pfinal+Paux-Pi);
            end
            Tfinal=Ti;  
            Pfinal=Paux-Pi;
        end
        Tsat=Ti;
        Integralcp=Acp*(Ti-T0)+Bcp*(Ti^2-T0^2)/2+Ccp*(Ti^3-T0^3)/3+Dcp*(Ti^4-T0^4)/4+Ecp*(Ti^5-T0^5)/5;
        if eos==1 
            I=beta/(Zliquid+epsilon*beta);
        else
            I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
        end
        HR=R2*Ti*(Zliquid-1+(derivate-1)*q*I);
        Hliquid=(-HR0+HR+H0+Integralcp)/MM;
        if eos==1
            I=beta/(Zvapor+epsilon*beta);
        else
            I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
        end
        HR=R2*Ti*(Zvapor-1+(derivate-1)*q*I);
        Hvapor=(-HR0+HR+H0+Integralcp)/MM;
        if isnan(Hsatmax)
            Hsatmax=Hvapor;
        else
            Hsatmax=max([Hvapor Hsatmax]);
        end
        if isnan(Hsatmin)
            Hsatmin=Hliquid;
        else
            Hsatmin=min([Hliquid Hsatmin]);
        end
        % Save data to graph the loop of the EoS: Liquid 
        % Find first V (with Z<=1)
        Vstart=b+1;
        if eos==1
            Tfunction=@(T) ((Pi+psi*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
        elseif eos==2
            Tfunction=@(T) ((Pi+psi*(T/Tc)^(-1/2)*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
        elseif eos==3
            Tfunction=@(T) ((Pi+psi*(1+(0.480+1.574*w-0.176*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
        else
            Tfunction=@(T) ((Pi+psi*(1+(0.37464+1.54226*w-0.26992*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
        end
        Tstart=fsolve(Tfunction,Ti,options);
        if Pi*Vstart/(R*Tstart)>1
            Zstart=Pi*Vstart/(R*Tstart)-1;
            Tfinal=Ti;
            Vfinal=Vliquid;
            Zfinal=Pi*Vfinal/(R*Tfinal)-1;
            while abs(Zfinal)>Er && abs(Zstart)>Er && abs(Tstart-Tfinal)>Er
                Tm=Tfinal-(Tfinal-Tstart)*Zfinal/(Zfinal-Zstart);
                Tr=Tm/Tc;
                if eos==2
                    alpha=Tr^(-1/2);
                elseif eos>2
                    alpha=(1+p*(1-Tr^(1/2)))^2;
                    derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
                end
                a=psi*alpha*(R*Tc)^2/Pc;
                liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Tm+Pi*(b-V))/a)-V;
                Vm=fsolve(liquid,b,options);
                Zm=Pi*Vm/(R*Tm);
                if (Zm-1)*Zfinal<0 
                    Tstart=Tfinal;  
                    Zstart=Zfinal;
                else 
                    Zstart=Zstart*Zfinal/(Zfinal+Zm-1);
                end
                Tfinal=Tm;  
                Zfinal=Zm-1;
            end
            Vstart=R*Tm*Zm/Pi;
        end
        if eos==1
            Tfunction=@(T) (Pi+psi*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R-T;
        elseif eos==2
            Tfunction=@(T) ((Pi+psi*(T/Tc)^(-1/2)*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
        elseif eos==3
            Tfunction=@(T) ((Pi+psi*(1+(0.480+1.574*w-0.176*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
        else
            Tfunction=@(T) ((Pi+psi*(1+(0.37464+1.54226*w-0.26992*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
        end
        % Liquid
        T(1)=fsolve(Tfunction,Ti,options);
        Integralcp=Acp*(T(1)-T0)+Bcp*(T(1)^2-T0^2)/2+Ccp*(T(1)^3-T0^3)/3+Dcp*(T(1)^4-T0^4)/4+Ecp*(T(1)^5-T0^5)/5;
        Z(1)=Pi*Vstart/(R*T(1));
        Tr=T(1)/Tc;
        if eos==2
            alpha=Tr^(-1/2);
        elseif eos>2
            alpha=(1+p*(1-Tr^(1/2)))^2;
            derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
        end
        a=psi*alpha*(R*Tc)^2/Pc;
        q=a/(b*R*T(1));
        beta=Pi*b/(R*T(1));
        if eos==1 
            I=beta/(Z(1)+epsilon*beta);
        else
            I=log((Z(1)+sigma*beta)/(Z(1)+epsilon*beta))/(sigma-epsilon);
        end
        HR=R2*T(1)*(Z(1)-1+(derivate-1)*q*I);
        H(1)=(-HR0+HR+H0+Integralcp)/MM;
        step=(Vliquid-Vstart)/100;
        Vnext=Vstart+step;
        j=2;
        while Vnext<Vliquid
            if eos==1
                Tfunction=@(T) ((Pi+psi*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
            elseif eos==2
                Tfunction=@(T) ((Pi+psi*(T/Tc)^(-1/2)*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
            elseif eos==3
                Tfunction=@(T) ((Pi+psi*(1+(0.480+1.574*w-0.176*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
            else
                Tfunction=@(T) ((Pi+psi*(1+(0.37464+1.54226*w-0.26992*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
            end
            T(j)=fsolve(Tfunction,Ti,options);
            Integralcp=Acp*(T(j)-T0)+Bcp*(T(j)^2-T0^2)/2+Ccp*(T(j)^3-T0^3)/3+Dcp*(T(j)^4-T0^4)/4+Ecp*(T(j)^5-T0^5)/5;
            Z(j)=Pi*Vnext/(R*T(j));
            Tr=T(j)/Tc;
            if eos==2
                alpha=Tr^(-1/2);
            elseif eos>2
                alpha=(1+p*(1-Tr^(1/2)))^2;
                derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
            end
            a=psi*alpha*(R*Tc)^2/Pc;
            q=a/(b*R*T(j));
            beta=Pi*b/(R*T(j));
            if eos==1 
                I=beta/(Z(j)+epsilon*beta);
            else
                I=log((Z(j)+sigma*beta)/(Z(j)+epsilon*beta))/(sigma-epsilon);
            end
            HR=R2*T(j)*(Z(j)-1+(derivate-1)*q*I);
            H(j)=(-HR0+HR+H0+Integralcp)/MM;
            Vnext=Vnext+step;
            j=j+1;
        end
        % Saturated Liquid-Vapor
        jl=j-1;
        T(j)=Tsat;
        H(j)=Hliquid;
        j=j+1;
        T(j)=Tsat;
        H(j)=Hvapor;
        % Vapor
        Vnext=Vvapor+1;
        Vmax=Vvapor+5000;
        step=(Vmax-Vnext)/100;
        while Vnext<Vmax
            j=j+1;
            if eos==1
                Tfunction=@(T) ((Pi+psi*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
            elseif eos==2
                Tfunction=@(T) ((Pi+psi*(T/Tc)^(-1/2)*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
            elseif eos==3
                Tfunction=@(T) ((Pi+psi*(1+(0.480+1.574*w-0.176*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
            else
                Tfunction=@(T) ((Pi+psi*(1+(0.37464+1.54226*w-0.26992*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
            end
            T(j)=fsolve(Tfunction,Ti,options);
            Integralcp=Acp*(T(j)-T0)+Bcp*(T(j)^2-T0^2)/2+Ccp*(T(j)^3-T0^3)/3+Dcp*(T(j)^4-T0^4)/4+Ecp*(T(j)^5-T0^5)/5;
            Z(j)=Pi*Vnext/(R*T(j));
            Tr=T(j)/Tc;
            if eos==2
                alpha=Tr^(-1/2);
            elseif eos>2
                alpha=(1+p*(1-Tr^(1/2)))^2;
                derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
            end
            a=psi*alpha*(R*Tc)^2/Pc;
            q=a/(b*R*T(j));
            beta=Pi*b/(R*T(j));
            if eos==1 
                I=beta/(Z(j)+epsilon*beta);
            else
                I=log((Z(j)+sigma*beta)/(Z(j)+epsilon*beta))/(sigma-epsilon);
            end
            HR=R2*T(j)*(Z(j)-1+(derivate-1)*q*I);
            H(j)=(-HR0+HR+H0+Integralcp)/MM;
            Vnext=Vnext+step;
        end
        plot3(app.Figure1,T,H,ones(j)*Pi);
    end
end
hold(app.Figure1,"off");
view(app.Figure1,[45,45,45]);
ylim(app.Figure1,[Hsatmin-abs(Hsatmax-Hsatmin)*0.2 Hsatmax+abs(Hsatmax-Hsatmin)*0.2]);
zlim(app.Figure1,[max([0 Pt-10]) Pc*1.1]);
xlim(app.Figure1,[Tt-10 Tc*1.1]);
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