# Two-Phase Envelope on a TV Diagram

This is the sixth option in the volume menu. Its interface is programmed in "Volume6.mlapp" and it uses the function called "Two_Phase_TV_Diagram.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/volume6.jpg" width="629" height="543">

*Figure 1. Design View in Volume6.mlapp.*

### 1.2. Code View

```Matlab
classdef Volume6 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        TwoPhaseEnvelopeonaTVDiagramUIFigure  matlab.ui.Figure
        CriticalVolume            matlab.ui.control.EditField
        Volumem3kgEditFieldLabel  matlab.ui.control.Label
        CriticalTemperature       matlab.ui.control.EditField
        TemperatureKLabel         matlab.ui.control.Label
        Compound                  matlab.ui.control.DropDown
        CompoundDropDownLabel     matlab.ui.control.Label
        EoS                       matlab.ui.control.DropDown
        CubicEquationofStateDropDownLabel  matlab.ui.control.Label
        BackButton                matlab.ui.control.Button
        ExportButton              matlab.ui.control.Button
        Label_2                   matlab.ui.control.Label
        Label                     matlab.ui.control.Label
        Table1                    matlab.ui.control.Table
        TwoPhaseEnvelopeonaTVDiagramLabel  matlab.ui.control.Label
        Image                     matlab.ui.control.Image
        CalculateButton           matlab.ui.control.Button
        Figure1                   matlab.ui.control.UIAxes
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.TwoPhaseEnvelopeonaTVDiagramUIFigure,"north");
            % Compound
            data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds");
            app.Compound.Items=table2cell(data(:,1));
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
                progressbar=uiprogressdlg(app.TwoPhaseEnvelopeonaTVDiagramUIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                Two_Phase_TV_Diagram;
                app.ExportButton.Visible="on";
                close(progressbar);
            else
                uialert(app.TwoPhaseEnvelopeonaTVDiagramUIFigure,"Input isobar pressures not found.","Data Status","Icon","warning");
            end
        end

        % Button pushed function: BackButton
        function BackButtonPushed(app, event)
            Volume;
            delete(app);
        end

        % Button pushed function: ExportButton
        function ExportButtonPushed(app, event)
            progressbar=uiprogressdlg(app.TwoPhaseEnvelopeonaTVDiagramUIFigure,"Title","Status","Message","Exporting","Indeterminate","on","Cancelable","off");
            drawnow;
            aux=app.Table1.Data;
            table1=table(aux(:,1),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)),str2double(aux(:,5)),str2double(aux(:,6)),str2double(aux(:,7)));
            table1.Properties.VariableNames{'Var1'}='Method';
            table1.Properties.VariableNames{'Var2'}='Psat [bar]';
            table1.Properties.VariableNames{'Var3'}='Tsat [K]';
            table1.Properties.VariableNames{'Var4'}='Zliquid';
            table1.Properties.VariableNames{'Var5'}='Zvapor';
            table1.Properties.VariableNames{'Var6'}='Vliquid [m3/kg]';
            table1.Properties.VariableNames{'Var7'}='Vvapor [m3/kg]';
            writecell(cell(5000,7),"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range","A1");
            writetable(table1,"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range","A5");
            writecell({'Compound'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range","A1");
            writecell({'Cubic Equation of State'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range","A2");
            writecell({'Critical Temperature [K]'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range","A3");
            writecell({'Critical Volume [m3/kg]'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range","A4");
            writecell({app.Compound.Value},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range","B1");
            writecell({app.EoS.Value},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range","B2");
            writematrix(str2double({app.CriticalTemperature.Value}),"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range","B3");
            writematrix(str2double({app.CriticalVolume.Value}),"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range","B4");
            for i=8:3:5+height(table1)
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",[i,3,i,3])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",['C',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",[i,4,i,4])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",['D',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",[i,5,i,5])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",['E',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",[i,6,i,6])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",['F',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",[i,7,i,7])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",['G',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",[i-2,3,i-2,3])))
                    writecell({'NaN'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",['C',num2str(i-2)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",[i-2,4,i-2,4])))
                    writecell({'NaN'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",['D',num2str(i-2)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",[i-2,5,i-2,5])))
                    writecell({'NaN'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",['E',num2str(i-2)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",[i-2,6,i-2,6])))
                    writecell({'NaN'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",['F',num2str(i-2)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",[i-2,7,i-2,7])))
                    writecell({'NaN'},"./Results/Two-Phase Envelope on a TV Diagram.xlsx","Sheet","TV Diagram","Range",['G',num2str(i-2)]);
                end
            end
            close(progressbar);
            uialert(app.TwoPhaseEnvelopeonaTVDiagramUIFigure,"Finished Export.","Export Status","Icon","success");
        end

        % Value changed function: Compound
        function CompoundValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound");
            app.CriticalTemperature.Value="";
            app.CriticalVolume.Value="";
            cla(app.Figure1);
            app.Table1.Data={};
        end

        % Value changed function: EoS
        function EoSValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound");
            app.CriticalTemperature.Value="";
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

            % Create TwoPhaseEnvelopeonaTVDiagramUIFigure and hide until all components are created
            app.TwoPhaseEnvelopeonaTVDiagramUIFigure = uifigure('Visible', 'off');
            app.TwoPhaseEnvelopeonaTVDiagramUIFigure.Color = [1 1 1];
            app.TwoPhaseEnvelopeonaTVDiagramUIFigure.Position = [100 100 784 675];
            app.TwoPhaseEnvelopeonaTVDiagramUIFigure.Name = 'Two-Phase Envelope on a TV Diagram';
            app.TwoPhaseEnvelopeonaTVDiagramUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.TwoPhaseEnvelopeonaTVDiagramUIFigure.Resize = 'off';

            % Create Figure1
            app.Figure1 = uiaxes(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            title(app.Figure1, 'EoS - Compound')
            xlabel(app.Figure1, 'V [m^3/kg]')
            ylabel(app.Figure1, 'T_{sat} [K]')
            zlabel(app.Figure1, 'Z')
            app.Figure1.XScale = 'log';
            app.Figure1.XMinorTick = 'on';
            app.Figure1.XGrid = 'on';
            app.Figure1.XMinorGrid = 'on';
            app.Figure1.YGrid = 'on';
            app.Figure1.Position = [15 78 463 406];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.TwoPhaseEnvelopeonaTVDiagramUIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [574 509 103 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Image
            app.Image = uiimage(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            app.Image.Position = [128 512 127 103];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create TwoPhaseEnvelopeonaTVDiagramLabel
            app.TwoPhaseEnvelopeonaTVDiagramLabel = uilabel(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            app.TwoPhaseEnvelopeonaTVDiagramLabel.HorizontalAlignment = 'center';
            app.TwoPhaseEnvelopeonaTVDiagramLabel.FontSize = 20;
            app.TwoPhaseEnvelopeonaTVDiagramLabel.FontWeight = 'bold';
            app.TwoPhaseEnvelopeonaTVDiagramLabel.FontColor = [0.1412 0.302 0.4784];
            app.TwoPhaseEnvelopeonaTVDiagramLabel.Position = [131 631 548 26];
            app.TwoPhaseEnvelopeonaTVDiagramLabel.Text = 'Two-Phase Envelope on a TV Diagram';

            % Create Table1
            app.Table1 = uitable(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            app.Table1.ColumnName = {'Method'; 'Psat [bar]'; 'Tsat [K]'; 'Zliquid'; 'Zvapor'; 'Vliquid [m3/kg]'; 'Vvapor [m3/kg]'};
            app.Table1.RowName = {};
            app.Table1.Position = [499 206 271 278];

            % Create Label
            app.Label = uilabel(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            app.Label.FontSize = 11;
            app.Label.FontWeight = 'bold';
            app.Label.FontColor = [0.1412 0.302 0.4784];
            app.Label.Position = [16 10 571 65];
            app.Label.Text = {'Symbology'; 'NaN: Not a Number.'; 'NA: Not Available.'; '*: Thermodynamically not possible case because the temperature is less than the triple temperature.'; '**: Thermodynamically not possible case because the temperature is greater than the critical temperature.'};

            % Create Label_2
            app.Label_2 = uilabel(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            app.Label_2.HorizontalAlignment = 'center';
            app.Label_2.FontWeight = 'bold';
            app.Label_2.FontColor = [0.1412 0.302 0.4784];
            app.Label_2.Position = [595 174 80 22];
            app.Label_2.Text = 'Critical Point';

            % Create ExportButton
            app.ExportButton = uibutton(app.TwoPhaseEnvelopeonaTVDiagramUIFigure, 'push');
            app.ExportButton.ButtonPushedFcn = createCallbackFcn(app, @ExportButtonPushed, true);
            app.ExportButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.ExportButton.FontWeight = 'bold';
            app.ExportButton.FontColor = [0.1412 0.302 0.4784];
            app.ExportButton.Visible = 'off';
            app.ExportButton.Position = [671 53 100 22];
            app.ExportButton.Text = 'Export';

            % Create BackButton
            app.BackButton = uibutton(app.TwoPhaseEnvelopeonaTVDiagramUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [671 21 100 22];
            app.BackButton.Text = 'Back';

            % Create CubicEquationofStateDropDownLabel
            app.CubicEquationofStateDropDownLabel = uilabel(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            app.CubicEquationofStateDropDownLabel.HorizontalAlignment = 'right';
            app.CubicEquationofStateDropDownLabel.FontWeight = 'bold';
            app.CubicEquationofStateDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CubicEquationofStateDropDownLabel.Position = [280 545 141 22];
            app.CubicEquationofStateDropDownLabel.Text = 'Cubic Equation of State';

            % Create EoS
            app.EoS = uidropdown(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            app.EoS.Items = {'van der Waals', 'Redlich-Kwong', 'Soave-Redlich-Kwong', 'Peng-Robinson'};
            app.EoS.ValueChangedFcn = createCallbackFcn(app, @EoSValueChanged, true);
            app.EoS.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EoS.Position = [437 545 241 22];
            app.EoS.Value = 'van der Waals';

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [282 581 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [437 581 242 22];
            app.Compound.Value = {};

            % Create TemperatureKLabel
            app.TemperatureKLabel = uilabel(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            app.TemperatureKLabel.HorizontalAlignment = 'right';
            app.TemperatureKLabel.FontWeight = 'bold';
            app.TemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.TemperatureKLabel.Position = [499 142 103 22];
            app.TemperatureKLabel.Text = 'Temperature [K]';

            % Create CriticalTemperature
            app.CriticalTemperature = uieditfield(app.TwoPhaseEnvelopeonaTVDiagramUIFigure, 'text');
            app.CriticalTemperature.Editable = 'off';
            app.CriticalTemperature.Position = [619 142 149 22];

            % Create Volumem3kgEditFieldLabel
            app.Volumem3kgEditFieldLabel = uilabel(app.TwoPhaseEnvelopeonaTVDiagramUIFigure);
            app.Volumem3kgEditFieldLabel.HorizontalAlignment = 'right';
            app.Volumem3kgEditFieldLabel.FontWeight = 'bold';
            app.Volumem3kgEditFieldLabel.FontColor = [0.1412 0.302 0.4784];
            app.Volumem3kgEditFieldLabel.Position = [499 108 103 22];
            app.Volumem3kgEditFieldLabel.Text = 'Volume [m3/kg]';

            % Create CriticalVolume
            app.CriticalVolume = uieditfield(app.TwoPhaseEnvelopeonaTVDiagramUIFigure, 'text');
            app.CriticalVolume.Editable = 'off';
            app.CriticalVolume.Position = [619 108 149 22];

            % Show the figure after all components are created
            app.TwoPhaseEnvelopeonaTVDiagramUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Volume6

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.TwoPhaseEnvelopeonaTVDiagramUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.TwoPhaseEnvelopeonaTVDiagramUIFigure)
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
% Available pressures
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
tam=0;
aux=strings;
Pindex=[];
for i=1:height(data2)
    if ~ismissing(table2array(data2(i,2))) && string(table2array(data2(i,2)))~="NaN"
        tam=tam+1;
        aux(tam)=string(table2array(data2(i,2)));
        Pindex(tam)=i;
    end
end
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
b=omega*R*Tc/Pc;
Er=0.00001;
sizefug=1;
sizeant=1;
Vfug=[];
Tfug=[];
Vant=[];
Tant=[];
Vexp=zeros(1,2*tam);
Texp=zeros(1,2*tam);
method=strings(1,3*tam);
T=strings(1,3*tam);
P=strings(1,3*tam);
Vl=strings(1,3*tam);
Vv=strings(1,3*tam);
Zl=strings(1,3*tam);
Zv=strings(1,3*tam);
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
% For each P in the compound database: Find Tsat, Zliquid, Zvapor, Vliquid, and Vvapor
sizefug=1;
sizeant=1;
for i=1:tam
    Pi=str2double(aux(i));
    ft=3*i-2;
    ae=3*i-1;
    ed=3*i;
    % Fugacity test method
    % Case not thermodynamically possible: Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number)
    if Pi<Pbracket(1) || Pi>Pbracket(2)
        method(ft)="Fugacity Test";
        P(ft)=string(Pi);
        T(ft)="NaN";
        Vl(ft)="NaN";
        Vv(ft)="NaN";
        Zl(ft)="NaN";
        Zv(ft)="NaN";
    else 
        Pstart=Pbracket(1)-Pi;
        Pfinal=Pbracket(2)-Pi;
        Tstart=Tbracket(1);
        Tfinal=Tbracket(2);
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
        % Save and report results
        Tfug(sizefug)=Ti;
        Vfug(sizefug)=Vliquid/1000/MM;
        sizefug=sizefug+1;
        Tfug(sizefug)=Ti;
        Vfug(sizefug)=Vvapor/1000/MM;
        sizefug=sizefug+1;
        method(ft)="Fugacity Test";
        P(ft)=string(Pi);
        T(ft)=string(Ti);
        Vl(ft)=string(Vfug(sizefug-2));
        Vv(ft)=string(Vfug(sizefug-1));
        Zl(ft)=string(Zliquid);
        Zv(ft)=string(Zvapor);
    end
    % Find Tsat using Antoine Equation
    Tantl=-B/(log(Pi/0.01)-A)-C;
    Tantv=Tantl;
    Tr=Tantl/Tc;
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos==3
        alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
    elseif eos==4
        alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
    end
    a=psi*alpha*(R*Tc)^2/Pc;
    liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Tantl+Pi*(b-V))/a)-V;
    Vantl=fsolve(liquid,b,options)/1000/MM;
    vapor=@(V) (R*Tantv/Pi+b-a/Pi*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
    Vantv=fsolve(vapor,R*Tantv/Pi,options)/1000/MM;
    if Tantl<Tt
        method(ae)="*Antoine Equation";
    elseif Tantl>Tc
        method(ae)="**Antoine Equation";
    else
        method(ae)="Antoine Equation";
    end
    % Antoine Equation: Condition to check what points will be plotted
    if Tantl>=Tt && Tantl<=Tc
        Tant(sizeant)=Tantl;
        Vant(sizeant)=Vantl;
        sizeant=sizeant+1;
        Tant(sizeant)=Tantl;
        Vant(sizeant)=Vantv;
        sizeant=sizeant+1;
    end
    P(ae)=string(Pi);
    T(ae)=string(Tantl);
    Vl(ae)=string(Vantl);
    Vv(ae)=string(Vantv);
    Zl(ae)=string(Pi*Vantl*1000*MM/(R*Tantl));
    Zv(ae)=string(Pi*Vantv*1000*MM/(R*Tantv));
    % Find Tsat, Vliquid, and Vvapor using the experimental data matrix
    l=2*i-1;
    v=2*i;
    P(ed)=string(Pi);
    method(ed)="Experimental Data";
    Texp(l)=table2array(data2(Pindex(i),1));
    Texp(v)=table2array(data2(Pindex(i),1));
    Vexp(l)=table2array(data2(Pindex(i),3));
    Vexp(v)=table2array(data2(Pindex(i),4));
    if isnan(Texp(l))
        T(ed)="NA";
    else
        T(ed)=string(Texp(l));
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
    if ~isnan(Vexp(l)) && ~isnan(Texp(l))
        Zl(ed)=string(Pi*Vexp(l)*1000*MM/(R*Texp(l)));
    else
        Zl(ed)="NA";
    end
    if ~isnan(Vexp(v)) && ~isnan(Texp(v))
        Zv(ed)=string(Pi*Vexp(v)*1000*MM/(R*Texp(v)));
    else
        Zv(ed)="NA";
    end
end
% Critical Point
Texp(2*height(aux)+1)=Tc;
Vexp(2*height(aux)+1)=Vc;
app.CriticalTemperature.Value=string(Tc);
app.CriticalVolume.Value=string(Vc);
% Figure: Two-Phase Envelope on a TV Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Vfug,Tfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Vant,Tant,"Marker","^","LineStyle","none","Color","r");
plot(app.Figure1,Vexp,Texp,"Marker","o","LineStyle","none","Color",[0.1 0.5 0.1]);
Vmax=max([max(Vfug) max(Vant) max(Vexp)]);
Vmin=min([min(Vfug) min(Vant) min(Vexp)]);
axis(app.Figure1,[max([0 Vmin-0.1/MM]) Vmax+0.1/MM Tt-10 Tc+10]);
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
app.Table1.Data=[method;P;T;Zl;Zv;Vl;Vv]';
```