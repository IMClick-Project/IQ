# Two-Phase Envelope on a PS Diagram

This is the second option in the entropy menu. Its interface is programmed in "Entropy2.mlapp" and it uses the function called "Two_Phase_PS_Diagram.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/entropy2.jpg" width="724" height="534">

*Figure 1. Design View in Entropy2.mlapp.*

### 1.2. Code View

```Matlab
classdef Entropy2 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        TwoPhaseEnvelopeonaPSDiagramUIFigure  matlab.ui.Figure
        ReferenceEntropy             matlab.ui.control.EditField
        EnthalpykJkgLabel            matlab.ui.control.Label
        ReferencePressure            matlab.ui.control.EditField
        PressurebarEditFieldLabel_2  matlab.ui.control.Label
        ReferenceTemperature         matlab.ui.control.EditField
        TemperatureKLabel            matlab.ui.control.Label
        ReferenceState               matlab.ui.control.EditField
        StateLabel                   matlab.ui.control.Label
        Compound                     matlab.ui.control.DropDown
        CompoundDropDownLabel        matlab.ui.control.Label
        EoS                          matlab.ui.control.DropDown
        CubicEquationofStateDropDownLabel  matlab.ui.control.Label
        Label_3                      matlab.ui.control.Label
        TwoPhaseEnvelopeonaPSDiagramLabel  matlab.ui.control.Label
        Image                        matlab.ui.control.Image
        CalculateButton              matlab.ui.control.Button
        CriticalEntropy              matlab.ui.control.EditField
        Enthlalpym3kgLabel           matlab.ui.control.Label
        CriticalPressure             matlab.ui.control.EditField
        PressurebarEditFieldLabel    matlab.ui.control.Label
        BackButton                   matlab.ui.control.Button
        ExportButton                 matlab.ui.control.Button
        Label_2                      matlab.ui.control.Label
        Label                        matlab.ui.control.Label
        Table1                       matlab.ui.control.Table
        Figure1                      matlab.ui.control.UIAxes
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.TwoPhaseEnvelopeonaPSDiagramUIFigure,"north");
            % Compound
            data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds");
            app.Compound.Items=table2cell(data(:,1));
            % Reference State
            data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds","ReadRowNames",1);
            app.ReferenceState.Value=string(table2array(data(app.Compound.Value,15)));
            if ismissing(table2array(data(app.Compound.Value,16))) || string(table2array(data(app.Compound.Value,16)))=="NaN"
                app.ReferenceTemperature.Value="NaN";
            else
                app.ReferenceTemperature.Value=string(table2array(data(app.Compound.Value,16)));
            end
            if ismissing(table2array(data(app.Compound.Value,17))) || string(table2array(data(app.Compound.Value,17)))=="NaN"
                app.ReferencePressure.Value="NaN";
            else
                app.ReferencePressure.Value=string(table2array(data(app.Compound.Value,17)));
            end
            if ismissing(table2array(data(app.Compound.Value,18))) || string(table2array(data(app.Compound.Value,18)))=="NaN"
                app.ReferenceEntropy.Value="NaN";
            else
                app.ReferenceEntropy.Value=string(table2array(data(app.Compound.Value,18)));
            end
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
            if tam>0 && app.ReferenceState.Value~="NaN" && app.ReferenceTemperature.Value~="NaN" && app.ReferencePressure.Value~="NaN" && app.ReferenceEntropy.Value~="NaN"
                progressbar=uiprogressdlg(app.TwoPhaseEnvelopeonaPSDiagramUIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                Two_Phase_PS_Diagram;
                app.ExportButton.Visible="on";
                close(progressbar);
            elseif app.ReferenceState.Value=="NaN" || app.ReferenceTemperature.Value=="NaN" || app.ReferencePressure.Value=="NaN" || app.ReferenceEntropy.Value=="NaN"
                uialert(app.TwoPhaseEnvelopeonaPSDiagramUIFigure,"Incomplete Data.","Data Status","Icon","warning");
            else
                uialert(app.TwoPhaseEnvelopeonaPSDiagramUIFigure,"Input isotherm temperatures not found.","Data Status","Icon","warning");
            end
        end

        % Button pushed function: BackButton
        function BackButtonPushed(app, event)
            Entropy;
            delete(app);
        end

        % Button pushed function: ExportButton
        function ExportButtonPushed(app, event)
            progressbar=uiprogressdlg(app.TwoPhaseEnvelopeonaPSDiagramUIFigure,"Title","Status","Message","Exporting","Indeterminate","on","Cancelable","off");
            drawnow;
            aux=app.Table1.Data;
            table1=table(aux(:,1),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)),str2double(aux(:,5)),str2double(aux(:,6)),str2double(aux(:,7)));
            table1.Properties.VariableNames{'Var1'}='Method';
            table1.Properties.VariableNames{'Var2'}='Tsat [K]';
            table1.Properties.VariableNames{'Var3'}='Psat [bar]';
            table1.Properties.VariableNames{'Var4'}='Zliquid';
            table1.Properties.VariableNames{'Var5'}='Zvapor';
            table1.Properties.VariableNames{'Var6'}='Sliquid [kJ/kg/K]';
            table1.Properties.VariableNames{'Var7'}='Svapor [kJ/kg/K]';
            writecell(cell(5000,7),"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","A1");
            writetable(table1,"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","A9");
            writecell({'Compound'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","A1");
            writecell({'Cubic Equation of State'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","A2");
            writecell({'Reference State'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","A3");
            writecell({'Reference Temperature [K]'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","A4");
            writecell({'Reference Pressure [bar]'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","A5");
            writecell({'Reference Entropy [kJ/kg/K]'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","A6");
            writecell({'Critical Pressure [bar]'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","A7");
            writecell({'Calculated Critical Entropy [kJ/kg/K]'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","A8");
            writecell({app.Compound.Value},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","B1");
            writecell({app.EoS.Value},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","B2");
            writecell({app.ReferenceState.Value},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","B3");
            writematrix(str2double({app.ReferenceTemperature.Value}),"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","B4");
            writematrix(str2double({app.ReferencePressure.Value}),"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","B5");
            writematrix(str2double({app.ReferenceEntropy.Value}),"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","B6");
            writematrix(str2double({app.CriticalPressure.Value}),"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","B7");
            writematrix(str2double({app.CriticalEntropy.Value}),"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range","B8");
            for i=12:3:5+height(table1)
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range",[i,3,i,3])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range",['C',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range",[i,4,i,4])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range",['D',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range",[i,5,i,5])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range",['E',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range",[i,6,i,6])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range",['F',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range",[i,7,i,7])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PS Diagram.xlsx","Sheet","PS Diagram","Range",['G',num2str(i)]);
                end
            end
            close(progressbar);
            uialert(app.TwoPhaseEnvelopeonaPSDiagramUIFigure,"Finished Export.","Export Status","Icon","success");
        end

        % Value changed function: Compound
        function CompoundValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound");
            app.CriticalPressure.Value="";
            app.CriticalEntropy.Value="";
            % Reference State
            data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds","ReadRowNames",1);
            app.ReferenceState.Value=string(table2array(data(app.Compound.Value,15)));
            if ismissing(table2array(data(app.Compound.Value,16))) || string(table2array(data(app.Compound.Value,16)))=="NaN"
                app.ReferenceTemperature.Value="NaN";
            else
                app.ReferenceTemperature.Value=string(table2array(data(app.Compound.Value,16)));
            end
            if ismissing(table2array(data(app.Compound.Value,17))) || string(table2array(data(app.Compound.Value,17)))=="NaN"
                app.ReferencePressure.Value="NaN";
            else
                app.ReferencePressure.Value=string(table2array(data(app.Compound.Value,17)));
            end
            if ismissing(table2array(data(app.Compound.Value,18))) || string(table2array(data(app.Compound.Value,18)))=="NaN"
                app.ReferenceEntropy.Value="NaN";
            else
                app.ReferenceEntropy.Value=string(table2array(data(app.Compound.Value,18)));
            end
            cla(app.Figure1);
            app.Table1.Data={};
        end

        % Value changed function: EoS
        function EoSValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound");
            app.CriticalPressure.Value="";
            app.CriticalEntropy.Value="";
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

            % Create TwoPhaseEnvelopeonaPSDiagramUIFigure and hide until all components are created
            app.TwoPhaseEnvelopeonaPSDiagramUIFigure = uifigure('Visible', 'off');
            app.TwoPhaseEnvelopeonaPSDiagramUIFigure.Color = [1 1 1];
            app.TwoPhaseEnvelopeonaPSDiagramUIFigure.Position = [100 100 902 667];
            app.TwoPhaseEnvelopeonaPSDiagramUIFigure.Name = 'Two-Phase Envelope on a PS Diagram';
            app.TwoPhaseEnvelopeonaPSDiagramUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.TwoPhaseEnvelopeonaPSDiagramUIFigure.Resize = 'off';

            % Create Figure1
            app.Figure1 = uiaxes(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            title(app.Figure1, 'EoS - Compound')
            xlabel(app.Figure1, 'S [kJ/kg/K]')
            ylabel(app.Figure1, 'P_{sat} [bar]')
            zlabel(app.Figure1, 'Z')
            app.Figure1.XGrid = 'on';
            app.Figure1.XMinorGrid = 'on';
            app.Figure1.YGrid = 'on';
            app.Figure1.Position = [73 91 479 386];

            % Create Table1
            app.Table1 = uitable(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.Table1.ColumnName = {'Method'; 'Tsat [K]'; 'Psat [bar]'; 'Zliquid'; 'Zvapor'; 'Sliquid [kJ/kg/K]'; 'Svapor [kJ/kg/K]'};
            app.Table1.RowName = {};
            app.Table1.Position = [571 191 249 257];

            % Create Label
            app.Label = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.Label.FontWeight = 'bold';
            app.Label.FontColor = [0.1412 0.302 0.4784];
            app.Label.Position = [43 26 584 56];
            app.Label.Text = {'Symbology'; 'NA: Not Available.'; '*: Thermodynamically not possible case because the pressure is less than the triple pressure.'; '**: Thermodynamically not possible case because the pressure is greater than the critical pressure.'};

            % Create Label_2
            app.Label_2 = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.Label_2.HorizontalAlignment = 'center';
            app.Label_2.FontWeight = 'bold';
            app.Label_2.FontColor = [0.1412 0.302 0.4784];
            app.Label_2.Position = [661 157 144 22];
            app.Label_2.Text = 'Calculated Critical Point';

            % Create ExportButton
            app.ExportButton = uibutton(app.TwoPhaseEnvelopeonaPSDiagramUIFigure, 'push');
            app.ExportButton.ButtonPushedFcn = createCallbackFcn(app, @ExportButtonPushed, true);
            app.ExportButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.ExportButton.FontWeight = 'bold';
            app.ExportButton.FontColor = [0.1412 0.302 0.4784];
            app.ExportButton.Visible = 'off';
            app.ExportButton.Position = [770 50 100 22];
            app.ExportButton.Text = 'Export';

            % Create BackButton
            app.BackButton = uibutton(app.TwoPhaseEnvelopeonaPSDiagramUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [770 19 100 22];
            app.BackButton.Text = 'Back';

            % Create PressurebarEditFieldLabel
            app.PressurebarEditFieldLabel = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.PressurebarEditFieldLabel.HorizontalAlignment = 'right';
            app.PressurebarEditFieldLabel.FontWeight = 'bold';
            app.PressurebarEditFieldLabel.FontColor = [0.1412 0.302 0.4784];
            app.PressurebarEditFieldLabel.Position = [571 125 103 22];
            app.PressurebarEditFieldLabel.Text = 'Pressure [bar]';

            % Create CriticalPressure
            app.CriticalPressure = uieditfield(app.TwoPhaseEnvelopeonaPSDiagramUIFigure, 'text');
            app.CriticalPressure.Editable = 'off';
            app.CriticalPressure.Position = [691 125 176 22];

            % Create Enthlalpym3kgLabel
            app.Enthlalpym3kgLabel = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.Enthlalpym3kgLabel.HorizontalAlignment = 'right';
            app.Enthlalpym3kgLabel.FontWeight = 'bold';
            app.Enthlalpym3kgLabel.FontColor = [0.1412 0.302 0.4784];
            app.Enthlalpym3kgLabel.Position = [569 91 105 22];
            app.Enthlalpym3kgLabel.Text = 'Entropy [kJ/kg/K]';

            % Create CriticalEntropy
            app.CriticalEntropy = uieditfield(app.TwoPhaseEnvelopeonaPSDiagramUIFigure, 'text');
            app.CriticalEntropy.Editable = 'off';
            app.CriticalEntropy.Position = [691 91 176 22];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.TwoPhaseEnvelopeonaPSDiagramUIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [764 469 103 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Image
            app.Image = uiimage(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.Image.Position = [25 506 116 101];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create TwoPhaseEnvelopeonaPSDiagramLabel
            app.TwoPhaseEnvelopeonaPSDiagramLabel = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.TwoPhaseEnvelopeonaPSDiagramLabel.HorizontalAlignment = 'center';
            app.TwoPhaseEnvelopeonaPSDiagramLabel.FontSize = 20;
            app.TwoPhaseEnvelopeonaPSDiagramLabel.FontWeight = 'bold';
            app.TwoPhaseEnvelopeonaPSDiagramLabel.FontColor = [0.1412 0.302 0.4784];
            app.TwoPhaseEnvelopeonaPSDiagramLabel.Position = [1 628 907 26];
            app.TwoPhaseEnvelopeonaPSDiagramLabel.Text = 'Two-Phase Envelope on a PS Diagram';

            % Create Label_3
            app.Label_3 = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.Label_3.HorizontalAlignment = 'center';
            app.Label_3.FontWeight = 'bold';
            app.Label_3.FontColor = [0.1412 0.302 0.4784];
            app.Label_3.Position = [672 599 93 22];
            app.Label_3.Text = 'Reference Data';

            % Create CubicEquationofStateDropDownLabel
            app.CubicEquationofStateDropDownLabel = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.CubicEquationofStateDropDownLabel.HorizontalAlignment = 'right';
            app.CubicEquationofStateDropDownLabel.FontWeight = 'bold';
            app.CubicEquationofStateDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CubicEquationofStateDropDownLabel.Position = [165 521 141 22];
            app.CubicEquationofStateDropDownLabel.Text = 'Cubic Equation of State';

            % Create EoS
            app.EoS = uidropdown(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.EoS.Items = {'van der Waals', 'Redlich-Kwong', 'Soave-Redlich-Kwong', 'Peng-Robinson'};
            app.EoS.ValueChangedFcn = createCallbackFcn(app, @EoSValueChanged, true);
            app.EoS.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EoS.Position = [322 521 220 22];
            app.EoS.Value = 'van der Waals';

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [168 560 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [323 560 220 22];
            app.Compound.Value = {};

            % Create StateLabel
            app.StateLabel = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.StateLabel.HorizontalAlignment = 'right';
            app.StateLabel.FontWeight = 'bold';
            app.StateLabel.FontColor = [0.1412 0.302 0.4784];
            app.StateLabel.Position = [571 577 103 22];
            app.StateLabel.Text = 'State';

            % Create ReferenceState
            app.ReferenceState = uieditfield(app.TwoPhaseEnvelopeonaPSDiagramUIFigure, 'text');
            app.ReferenceState.Editable = 'off';
            app.ReferenceState.Position = [691 577 176 22];

            % Create TemperatureKLabel
            app.TemperatureKLabel = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.TemperatureKLabel.HorizontalAlignment = 'right';
            app.TemperatureKLabel.FontWeight = 'bold';
            app.TemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.TemperatureKLabel.Position = [571 551 103 22];
            app.TemperatureKLabel.Text = 'Temperature [K]';

            % Create ReferenceTemperature
            app.ReferenceTemperature = uieditfield(app.TwoPhaseEnvelopeonaPSDiagramUIFigure, 'text');
            app.ReferenceTemperature.Editable = 'off';
            app.ReferenceTemperature.Position = [691 551 176 22];

            % Create PressurebarEditFieldLabel_2
            app.PressurebarEditFieldLabel_2 = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.PressurebarEditFieldLabel_2.HorizontalAlignment = 'right';
            app.PressurebarEditFieldLabel_2.FontWeight = 'bold';
            app.PressurebarEditFieldLabel_2.FontColor = [0.1412 0.302 0.4784];
            app.PressurebarEditFieldLabel_2.Position = [571 526 103 22];
            app.PressurebarEditFieldLabel_2.Text = 'Pressure [bar]';

            % Create ReferencePressure
            app.ReferencePressure = uieditfield(app.TwoPhaseEnvelopeonaPSDiagramUIFigure, 'text');
            app.ReferencePressure.Editable = 'off';
            app.ReferencePressure.Position = [691 526 176 22];

            % Create EnthalpykJkgLabel
            app.EnthalpykJkgLabel = uilabel(app.TwoPhaseEnvelopeonaPSDiagramUIFigure);
            app.EnthalpykJkgLabel.HorizontalAlignment = 'right';
            app.EnthalpykJkgLabel.FontWeight = 'bold';
            app.EnthalpykJkgLabel.FontColor = [0.1412 0.302 0.4784];
            app.EnthalpykJkgLabel.Position = [569 500 105 22];
            app.EnthalpykJkgLabel.Text = 'Entropy [kJ/kg/K]';

            % Create ReferenceEntropy
            app.ReferenceEntropy = uieditfield(app.TwoPhaseEnvelopeonaPSDiagramUIFigure, 'text');
            app.ReferenceEntropy.Editable = 'off';
            app.ReferenceEntropy.Position = [691 500 176 22];

            % Show the figure after all components are created
            app.TwoPhaseEnvelopeonaPSDiagramUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Entropy2

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.TwoPhaseEnvelopeonaPSDiagramUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.TwoPhaseEnvelopeonaPSDiagramUIFigure)
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
S0=str2double(app.ReferenceEntropy.Value); % Reference Entropy [kJ/kg/K]
S0=S0*MM; % [kJ/kmol/K]
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
R2=8.314; % Ideal Gas Constant [J*K/mol/K]
Er=0.00001;
b=omega*R*Tc/Pc;
% Reference entropy calculation of reference data
if ref==1
    SR0=0;
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
        SR0=R2*(log(Zliquid-beta)+derivate*q*I);
    else
        vapor=@(V) (R*T0/P0+b-a/P0*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
        Vvapor=fsolve(vapor,R*T0/P0,options);
        Zvapor=P0*Vvapor/(R*T0);
        if eos==1
            I=beta/(Zvapor+epsilon*beta);
        else
            I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
        end
        SR0=R2*(log(Zvapor-beta)+derivate*q*I);
    end
end
sizefug=1;
sizeant=1;
Sfug=[];
Pfug=[];
Sant=[];
Pant=[];
Sexp=zeros(1,2*tam);
Vexp=zeros(1,2*tam);
Pexp=zeros(1,2*tam);
method=strings(1,3*tam);
T=strings(1,3*tam);
P=strings(1,3*tam);
Sl=strings(1,3*tam);
Sv=strings(1,3*tam);
Zl=strings(1,3*tam);
Zv=strings(1,3*tam);
% For each T in the compound database: Find Psat, Zliquid, Zvapor, Sliquid, and Svapor
for i=1:tam
    Ti=str2double(aux(i));
    Integralcp_T=Acp*log(Ti/T0)+Bcp*(Ti-T0)+Ccp*(Ti^2-T0^2)/2+Dcp*(Ti^3-T0^3)/3+Ecp*(Ti^4-T0^4)/4; % [kJ/kmol/K]
    Tr=Ti/Tc;
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos>2
        alpha=(1+p*(1-Tr^(1/2)))^2;
        derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
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
    beta=Paux*b/(R*Ti);
    if eos==1 
        I=beta/(Zliquid+epsilon*beta);
    else
        I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
    end
    SR=R2*(log(Zliquid-beta)+derivate*q*I);
    Sfugl=(-SR0+SR+S0+Integralcp_T-R2*log(Paux/P0))/MM;
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    SR=R2*(log(Zvapor-beta)+derivate*q*I);
    Sfugv=(-SR0+SR+S0+Integralcp_T-R2*log(Paux/P0))/MM;
    % Test Fugacity: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pfug(sizefug)=Paux;
        Sfug(sizefug)=Sfugl;
        sizefug=sizefug+1;
        Pfug(sizefug)=Paux;
        Sfug(sizefug)=Sfugv;
        sizefug=sizefug+1;
    end
    P(ft)=string(Paux);
    Sl(ft)=string(Sfugl);
    Sv(ft)=string(Sfugv);
    Zl(ft)=string(Zliquid);
    Zv(ft)=string(Zvapor);
    % Find Psat using Antoine Equation
    Paux=exp(A-B/(Ti+C))*0.01;
    liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Paux*(b-V))/a)-V;
    Vliquid=fsolve(liquid,b,options);
    vapor=@(V) (R*Ti/Paux+b-a/Paux*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
    Vvapor=fsolve(vapor,R*Ti/Paux,options);
    Zliquid=Paux*Vliquid/(R*Ti);
    Zvapor=Paux*Vvapor/(R*Ti);
    beta=Paux*b/(R*Ti);
    if Paux<Pt
        method(ae)="*Antoine Equation";
    elseif Paux>Pc
        method(ae)="**Antoine Equation";
    else
        method(ae)="Antoine Equation";
    end
    T(ae)=string(Ti);
    if eos==1 
        I=beta/(Zliquid+epsilon*beta);
    else
        I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
    end
    SR=R2*(log(Zliquid-beta)+derivate*q*I);
    Santl=(-SR0+SR+S0+Integralcp_T-R2*log(Paux/P0))/MM;
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    SR=R2*(log(Zvapor-beta)+derivate*q*I);
    Santv=(-SR0+SR+S0+Integralcp_T-R2*log(Paux/P0))/MM;
    % Antoine Equation: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pant(sizeant)=Paux;
        Sant(sizeant)=Santl;
        sizeant=sizeant+1;
        Pant(sizeant)=Paux;
        Sant(sizeant)=Santv;
        sizeant=sizeant+1;
    end
    P(ae)=string(Paux);
    Sl(ae)=string(Santl);
    Sv(ae)=string(Santv);
    Zl(ae)=string(Zliquid);
    Zv(ae)=string(Zvapor);
    % Find Psat, Sliquid, and Svapor using the experimental data matrix
    l=2*i-1;
    v=2*i;
    T(ed)=string(Ti);
    method(ed)="Experimental Data";
    data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
    Pexp(l)=table2array(data2(aux(i),1));
    Pexp(v)=table2array(data2(aux(i),1));
    Vexp(l)=table2array(data2(aux(i),2));
    Vexp(v)=table2array(data2(aux(i),3));
    Sexp(l)=table2array(data2(aux(i),6));
    Sexp(v)=table2array(data2(aux(i),7));
    if isnan(Pexp(l))
        P(ed)="NA";
    else
        P(ed)=string(Pexp(l));
    end
    if isnan(Sexp(l))
        Sl(ed)="NA";
    else
        Sl(ed)=string(Sexp(l));
    end
    if isnan(Sexp(v))
        Sv(ed)="NA";
    else
        Sv(ed)=string(Sexp(v));
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
Zc=Pc*Vc*1000*MM/(R*Tc);
Integralcp_T=Acp*log(Ti/T0)+Bcp*(Ti-T0)+Ccp*(Ti^2-T0^2)/2+Dcp*(Ti^3-T0^3)/3+Ecp*(Ti^4-T0^4)/4; % [kJ/kmol/K]
Tr=Ti/Tc;
if eos==2
    alpha=Tr^(-1/2);
elseif eos>2
    alpha=(1+p*(1-Tr^(1/2)))^2;
    derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
end
a=psi*alpha*(R*Tc)^2/Pc;
q=a/(b*R*Tc);
beta=Pc*b/(R*Tc);
if eos==1 
    I=beta/(Zc+epsilon*beta);
else
    I=log((Zc+sigma*beta)/(Zc+epsilon*beta))/(sigma-epsilon);
end
SR=R2*(log(Zc-beta)+derivate*q*I);
Sc=(-SR0+SR+S0+Integralcp_T-R2*log(Pc/P0))/MM;
Sexp(2*height(aux)+1)=Sc;
app.CriticalPressure.Value=string(Pc);
app.CriticalEntropy.Value=string(Sc);
% Figure: Two-Phase Envelope on a PS Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Sfug,Pfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Sant,Pant,"Marker","^","Linestyle","none","Color","r");
plot(app.Figure1,Sexp,Pexp,"Marker","o","Linestyle","none","Color",[0.1 0.5 0.1]);
Smax=max([max(Sfug) max(Sant) max(Sexp)]);
Smin=min([min(Sfug) min(Sant) min(Sexp)]);
Pmin=max([0 Pt-10]);
if Pmin==0
    Pmax=Pc+Pt;
else
    Pmax=Pt+10;
end
axis(app.Figure1,[Smin-abs(Smax-Smin)*0.5 Smax+abs(Smax-Smin)*0.5 Pmin Pmax]);
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
app.Table1.Data=[method;T;P;Zl;Zv;Sl;Sv]';
```