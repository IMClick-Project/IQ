# PVT Surface given Isobar Pressures

This is the seventh option in the volume menu. Its interface is programmed in "Volume7.mlapp" and it uses the function called "PVT_Surface_given_Isobar_Pressures.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/volume7.jpg" width="571" height="571">

*Figure 1. Design View in Volume7.mlapp.*

### 1.2. Code View

```Matlab
classdef Volume7 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        PVTSurfacegivenIsobarPressuresUIFigure  matlab.ui.Figure
        Compound               matlab.ui.control.DropDown
        CompoundDropDownLabel  matlab.ui.control.Label
        EoS                    matlab.ui.control.DropDown
        CubicEquationofStateDropDownLabel  matlab.ui.control.Label
        BackButton             matlab.ui.control.Button
        PVTSurfacegivenIsobarPressuresLabel  matlab.ui.control.Label
        Image                  matlab.ui.control.Image
        CalculateButton        matlab.ui.control.Button
        Figure1                matlab.ui.control.UIAxes
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.PVTSurfacegivenIsobarPressuresUIFigure,"north");
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
            % Isobar Pressures
            data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
            tam=0;
            for i=1:height(data2)
                if ~ismissing(table2array(data2(i,2))) && string(table2array(data2(i,2)))~="NaN"
                    tam=tam+1;
                    break;
                end
            end
            if tam>0
                progressbar=uiprogressdlg(app.PVTSurfacegivenIsobarPressuresUIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                PVT_Surface_given_Isobar_Pressures;
                close(progressbar);
            else
                uialert(app.PVTSurfacegivenIsobarPressuresUIFigure,"Input isobar pressures not found.","Data Status","Icon","warning");
            end
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

            % Create PVTSurfacegivenIsobarPressuresUIFigure and hide until all components are created
            app.PVTSurfacegivenIsobarPressuresUIFigure = uifigure('Visible', 'off');
            app.PVTSurfacegivenIsobarPressuresUIFigure.Color = [1 1 1];
            app.PVTSurfacegivenIsobarPressuresUIFigure.Position = [100 100 634 632];
            app.PVTSurfacegivenIsobarPressuresUIFigure.Name = 'PVT Surface given Isobar Pressures';
            app.PVTSurfacegivenIsobarPressuresUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.PVTSurfacegivenIsobarPressuresUIFigure.Resize = 'off';

            % Create Figure1
            app.Figure1 = uiaxes(app.PVTSurfacegivenIsobarPressuresUIFigure);
            title(app.Figure1, 'EoS - Compound')
            xlabel(app.Figure1, 'T [K]')
            ylabel(app.Figure1, 'V [m^3/kg]')
            zlabel(app.Figure1, 'P [bar]')
            app.Figure1.XDir = 'reverse';
            app.Figure1.YScale = 'log';
            app.Figure1.YMinorTick = 'on';
            app.Figure1.XGrid = 'on';
            app.Figure1.YGrid = 'on';
            app.Figure1.YMinorGrid = 'on';
            app.Figure1.ZGrid = 'on';
            app.Figure1.Position = [43 58 532 394];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.PVTSurfacegivenIsobarPressuresUIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [471 468 103 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Image
            app.Image = uiimage(app.PVTSurfacegivenIsobarPressuresUIFigure);
            app.Image.Position = [43 468 127 103];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create PVTSurfacegivenIsobarPressuresLabel
            app.PVTSurfacegivenIsobarPressuresLabel = uilabel(app.PVTSurfacegivenIsobarPressuresUIFigure);
            app.PVTSurfacegivenIsobarPressuresLabel.HorizontalAlignment = 'center';
            app.PVTSurfacegivenIsobarPressuresLabel.FontSize = 20;
            app.PVTSurfacegivenIsobarPressuresLabel.FontWeight = 'bold';
            app.PVTSurfacegivenIsobarPressuresLabel.FontColor = [0.1412 0.302 0.4784];
            app.PVTSurfacegivenIsobarPressuresLabel.Position = [37 584 548 26];
            app.PVTSurfacegivenIsobarPressuresLabel.Text = 'PVT Surface given Isobar Pressures';

            % Create BackButton
            app.BackButton = uibutton(app.PVTSurfacegivenIsobarPressuresUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [512 21 100 22];
            app.BackButton.Text = 'Back';

            % Create CubicEquationofStateDropDownLabel
            app.CubicEquationofStateDropDownLabel = uilabel(app.PVTSurfacegivenIsobarPressuresUIFigure);
            app.CubicEquationofStateDropDownLabel.HorizontalAlignment = 'right';
            app.CubicEquationofStateDropDownLabel.FontWeight = 'bold';
            app.CubicEquationofStateDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CubicEquationofStateDropDownLabel.Position = [175 504 141 22];
            app.CubicEquationofStateDropDownLabel.Text = 'Cubic Equation of State';

            % Create EoS
            app.EoS = uidropdown(app.PVTSurfacegivenIsobarPressuresUIFigure);
            app.EoS.Items = {'van der Waals', 'Redlich-Kwong', 'Soave-Redlich-Kwong', 'Peng-Robinson'};
            app.EoS.ValueChangedFcn = createCallbackFcn(app, @EoSValueChanged, true);
            app.EoS.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EoS.Position = [332 504 241 22];
            app.EoS.Value = 'van der Waals';

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.PVTSurfacegivenIsobarPressuresUIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [176 540 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.PVTSurfacegivenIsobarPressuresUIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [331 540 242 22];
            app.Compound.Value = {};

            % Show the figure after all components are created
            app.PVTSurfacegivenIsobarPressuresUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Volume7

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.PVTSurfacegivenIsobarPressuresUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.PVTSurfacegivenIsobarPressuresUIFigure)
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
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
b=omega*R*Tc/Pc;
Er=0.00001;
Tbracket=[Tt Tc-0.1];
Pbracket=zeros(1,2);
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
    Pbracket(i)=Paux;
end
% For each P in the compound database: Plot isobar
hold(app.Figure1,"on");
Vsatmax=0;
Vsatmin=-1;
for i=1:tam
    Pi=str2double(aux(i));
    if Pi<Pbracket(1) || Pi>Pbracket(2)
        continue;
    else 
        T=[];
        V=[];
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
        if Vsatmin==-1
            Vsatmin=Vliquid/1000/MM;
        else
            Vsatmin=min([Vsatmin Vliquid/1000/MM]);
        end
        Vsatmax=max([Vsatmax Vvapor/1000/MM]);
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
                elseif eos==3
                    alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
                elseif eos==4
                    alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
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
        V(1)=Vstart/1000/MM;
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
            V(j)=Vnext/1000/MM;
            Vnext=Vnext+step;
            j=j+1;
        end
        % Saturated Liquid-Vapor
        jl=j-1;
        T(j)=Tsat;
        V(j)=Vliquid/1000/MM;
        j=j+1;
        T(j)=Tsat;
        V(j)=Vvapor/1000/MM;
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
            V(j)=Vnext/1000/MM;
            Vnext=Vnext+step;
        end
        plot3(app.Figure1,T,V,ones(j)*Pi);
    end
end
hold(app.Figure1,"off");
view(app.Figure1,[45,45,45]);
ylim(app.Figure1,[0.95*Vsatmin Vsatmax+0.1/MM]);
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