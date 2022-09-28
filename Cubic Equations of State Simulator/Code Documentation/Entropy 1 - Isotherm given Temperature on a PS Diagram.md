# Isotherm given Temperature on a PS Diagram

This is the first option in the entropy menu. Its interface is programmed in "Entropy1.mlapp" and it uses the function called "Isotherm_given_Temperature_PS_Diagram.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/entropy1.jpg" width="726" height="532">

*Figure 1. Design View in Entropy1.mlapp.*

### 1.2. Code View

```Matlab
classdef Entropy1 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        IsothermgivenTemperatureonaPSDiagramUIFigure  matlab.ui.Figure
        BackButton                   matlab.ui.control.Button
        ExportButton                 matlab.ui.control.Button
        ReferenceEntropy             matlab.ui.control.EditField
        EnthalpykJkgLabel            matlab.ui.control.Label
        ReferencePressure            matlab.ui.control.EditField
        PressurebarEditFieldLabel_2  matlab.ui.control.Label
        ReferenceTemperature         matlab.ui.control.EditField
        TemperatureKLabel            matlab.ui.control.Label
        ReferenceState               matlab.ui.control.EditField
        StateLabel                   matlab.ui.control.Label
        Label_2                      matlab.ui.control.Label
        Label                        matlab.ui.control.Label
        IsothermTemperature          matlab.ui.control.DropDown
        IsothermTemperatureKLabel    matlab.ui.control.Label
        Compound                     matlab.ui.control.DropDown
        CompoundDropDownLabel        matlab.ui.control.Label
        EoS                          matlab.ui.control.DropDown
        CubicEquationofStateDropDownLabel  matlab.ui.control.Label
        Table1                       matlab.ui.control.Table
        IsothermgivenTemperatureonaPSDiagramLabel  matlab.ui.control.Label
        Image                        matlab.ui.control.Image
        CalculateButton              matlab.ui.control.Button
        Figure1                      matlab.ui.control.UIAxes
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.IsothermgivenTemperatureonaPSDiagramUIFigure,"north");
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
            Entropy;
            delete(app);
        end

        % Value changed function: Compound
        function CompoundValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound @ Isotherm Temperature");
            cla(app.Figure1);
            app.Table1.Data={};
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
            if isempty(convertCharsToStrings(app.IsothermTemperature.Value)) || app.ReferenceState.Value=="NaN" || app.ReferenceTemperature.Value=="NaN" || app.ReferencePressure.Value=="NaN" || app.ReferenceEntropy.Value=="NaN"
                uialert(app.IsothermgivenTemperatureonaPSDiagramUIFigure,"Incomplete Data.","Data Status","Icon","warning");
            else
                progressbar=uiprogressdlg(app.IsothermgivenTemperatureonaPSDiagramUIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                Isotherm_given_Temperature_PS_Diagram;
                app.ExportButton.Visible="on";
                close(progressbar);
            end
        end

        % Value changed function: EoS
        function EoSValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound @ Isotherm Temperature");
            cla(app.Figure1);
            app.Table1.Data={};
        end

        % Value changed function: IsothermTemperature
        function IsothermTemperatureValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound @ Isotherm Temperature");
            cla(app.Figure1);
            app.Table1.Data={};
        end

        % Button pushed function: ExportButton
        function ExportButtonPushed(app, event)
            progressbar=uiprogressdlg(app.IsothermgivenTemperatureonaPSDiagramUIFigure,"Title","Status","Message","Exporting","Indeterminate","on","Cancelable","off");
            drawnow;
            aux=app.Table1.Data;
            table1=table(aux(:,1),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)));
            table1.Properties.VariableNames{'Var1'}='Phase';
            table1.Properties.VariableNames{'Var2'}='P [bar]';
            table1.Properties.VariableNames{'Var3'}='Z';
            table1.Properties.VariableNames{'Var4'}='S [kJ/kg/K]';
            writecell(cell(5000,4),"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A1");
            writetable(table1,"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A8");
            writecell({'Compound'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A1");
            writecell({'Cubic Equation of State'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A2");
            writecell({'Isotherm Temperature [K]'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A3");
            writecell({'Reference State'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A4");
            writecell({'Reference Temperature [K]'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A5");
            writecell({'Reference Pressure [bar]'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A6");
            writecell({'Reference Entropy [kJ/kg/K]'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","A7");
            writecell({app.Compound.Value},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","B1");
            writecell({app.EoS.Value},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","B2");
            writematrix(str2double({app.IsothermTemperature.Value}),"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","B3");
            writecell({app.ReferenceState.Value},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","B4");
            writematrix(str2double({app.ReferenceTemperature.Value}),"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","B5");
            writematrix(str2double({app.ReferencePressure.Value}),"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","B6");
            writematrix(str2double({app.ReferenceEntropy.Value}),"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range","B7");
            for i=1:height(table1)
                if string(table2cell(table1(i,1)))=="Satured Liquid (Experimental Data)" 
                    index=i+8;
                    break;
                end
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index,2,index,2])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['B',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index+1,2,index+1,2])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['B',num2str(index+1)]);
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index,3,index,3])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['C',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index+1,3,index+1,3])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['C',num2str(index+1)]);
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index,4,index,4])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['D',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",[index+1,4,index+1,4])))
                writecell({'NA'},"./Results/Isotherm given Temperature on a PS Diagram.xlsx","Sheet","Isotherm given Temperature","Range",['D',num2str(index+1)]);
            end
            close(progressbar);
            uialert(app.IsothermgivenTemperatureonaPSDiagramUIFigure,"Finished Export.","Export Status","Icon","success");
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create IsothermgivenTemperatureonaPSDiagramUIFigure and hide until all components are created
            app.IsothermgivenTemperatureonaPSDiagramUIFigure = uifigure('Visible', 'off');
            app.IsothermgivenTemperatureonaPSDiagramUIFigure.Color = [1 1 1];
            app.IsothermgivenTemperatureonaPSDiagramUIFigure.Position = [100 100 907 661];
            app.IsothermgivenTemperatureonaPSDiagramUIFigure.Name = 'Isotherm given Temperature on a PS Diagram';
            app.IsothermgivenTemperatureonaPSDiagramUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.IsothermgivenTemperatureonaPSDiagramUIFigure.Resize = 'off';

            % Create Figure1
            app.Figure1 = uiaxes(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            title(app.Figure1, 'EoS - Compound @ Isotherm Temperature')
            xlabel(app.Figure1, 'S [kJ/kg/K]')
            ylabel(app.Figure1, 'P [bar]')
            zlabel(app.Figure1, 'Z')
            app.Figure1.XGrid = 'on';
            app.Figure1.XMinorGrid = 'on';
            app.Figure1.YGrid = 'on';
            app.Figure1.Position = [84 69 488 407];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.IsothermgivenTemperatureonaPSDiagramUIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [764 463 103 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Image
            app.Image = uiimage(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.Image.Position = [25 500 116 101];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create IsothermgivenTemperatureonaPSDiagramLabel
            app.IsothermgivenTemperatureonaPSDiagramLabel = uilabel(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.IsothermgivenTemperatureonaPSDiagramLabel.HorizontalAlignment = 'center';
            app.IsothermgivenTemperatureonaPSDiagramLabel.FontSize = 20;
            app.IsothermgivenTemperatureonaPSDiagramLabel.FontWeight = 'bold';
            app.IsothermgivenTemperatureonaPSDiagramLabel.FontColor = [0.1412 0.302 0.4784];
            app.IsothermgivenTemperatureonaPSDiagramLabel.Position = [1 622 907 26];
            app.IsothermgivenTemperatureonaPSDiagramLabel.Text = 'Isotherm given Temperature on a PS Diagram';

            % Create Table1
            app.Table1 = uitable(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.Table1.ColumnName = {'Phase'; 'P [bar]'; 'Z'; 'S [kJ/kg/K]'};
            app.Table1.RowName = {};
            app.Table1.Position = [589 118 226 326];

            % Create CubicEquationofStateDropDownLabel
            app.CubicEquationofStateDropDownLabel = uilabel(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.CubicEquationofStateDropDownLabel.HorizontalAlignment = 'right';
            app.CubicEquationofStateDropDownLabel.FontWeight = 'bold';
            app.CubicEquationofStateDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CubicEquationofStateDropDownLabel.Position = [163 533 141 22];
            app.CubicEquationofStateDropDownLabel.Text = 'Cubic Equation of State';

            % Create EoS
            app.EoS = uidropdown(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.EoS.Items = {'van der Waals', 'Redlich-Kwong', 'Soave-Redlich-Kwong', 'Peng-Robinson'};
            app.EoS.ValueChangedFcn = createCallbackFcn(app, @EoSValueChanged, true);
            app.EoS.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EoS.Position = [320 533 220 22];
            app.EoS.Value = 'van der Waals';

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [166 572 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [321 572 220 22];
            app.Compound.Value = {};

            % Create IsothermTemperatureKLabel
            app.IsothermTemperatureKLabel = uilabel(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.IsothermTemperatureKLabel.HorizontalAlignment = 'right';
            app.IsothermTemperatureKLabel.FontWeight = 'bold';
            app.IsothermTemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.IsothermTemperatureKLabel.Position = [153 495 151 22];
            app.IsothermTemperatureKLabel.Text = 'Isotherm Temperature [K]';

            % Create IsothermTemperature
            app.IsothermTemperature = uidropdown(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.IsothermTemperature.Items = {};
            app.IsothermTemperature.ValueChangedFcn = createCallbackFcn(app, @IsothermTemperatureValueChanged, true);
            app.IsothermTemperature.BackgroundColor = [0.8588 0.9608 0.9608];
            app.IsothermTemperature.Position = [319 495 222 22];
            app.IsothermTemperature.Value = {};

            % Create Label
            app.Label = uilabel(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.Label.FontWeight = 'bold';
            app.Label.FontColor = [0.1412 0.302 0.4784];
            app.Label.Position = [43 14 584 56];
            app.Label.Text = {'Symbology'; 'NA: Not Available.'; '*: Thermodynamically not possible case because the pressure is less than the triple pressure.'; '**: Thermodynamically not possible case because the pressure is greater than the critical pressure.'};

            % Create Label_2
            app.Label_2 = uilabel(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.Label_2.HorizontalAlignment = 'center';
            app.Label_2.FontWeight = 'bold';
            app.Label_2.FontColor = [0.1412 0.302 0.4784];
            app.Label_2.Position = [672 593 93 22];
            app.Label_2.Text = 'Reference Data';

            % Create StateLabel
            app.StateLabel = uilabel(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.StateLabel.HorizontalAlignment = 'right';
            app.StateLabel.FontWeight = 'bold';
            app.StateLabel.FontColor = [0.1412 0.302 0.4784];
            app.StateLabel.Position = [571 571 103 22];
            app.StateLabel.Text = 'State';

            % Create ReferenceState
            app.ReferenceState = uieditfield(app.IsothermgivenTemperatureonaPSDiagramUIFigure, 'text');
            app.ReferenceState.Editable = 'off';
            app.ReferenceState.Position = [691 571 176 22];

            % Create TemperatureKLabel
            app.TemperatureKLabel = uilabel(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.TemperatureKLabel.HorizontalAlignment = 'right';
            app.TemperatureKLabel.FontWeight = 'bold';
            app.TemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.TemperatureKLabel.Position = [571 545 103 22];
            app.TemperatureKLabel.Text = 'Temperature [K]';

            % Create ReferenceTemperature
            app.ReferenceTemperature = uieditfield(app.IsothermgivenTemperatureonaPSDiagramUIFigure, 'text');
            app.ReferenceTemperature.Editable = 'off';
            app.ReferenceTemperature.Position = [691 545 176 22];

            % Create PressurebarEditFieldLabel_2
            app.PressurebarEditFieldLabel_2 = uilabel(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.PressurebarEditFieldLabel_2.HorizontalAlignment = 'right';
            app.PressurebarEditFieldLabel_2.FontWeight = 'bold';
            app.PressurebarEditFieldLabel_2.FontColor = [0.1412 0.302 0.4784];
            app.PressurebarEditFieldLabel_2.Position = [571 520 103 22];
            app.PressurebarEditFieldLabel_2.Text = 'Pressure [bar]';

            % Create ReferencePressure
            app.ReferencePressure = uieditfield(app.IsothermgivenTemperatureonaPSDiagramUIFigure, 'text');
            app.ReferencePressure.Editable = 'off';
            app.ReferencePressure.Position = [691 520 176 22];

            % Create EnthalpykJkgLabel
            app.EnthalpykJkgLabel = uilabel(app.IsothermgivenTemperatureonaPSDiagramUIFigure);
            app.EnthalpykJkgLabel.HorizontalAlignment = 'right';
            app.EnthalpykJkgLabel.FontWeight = 'bold';
            app.EnthalpykJkgLabel.FontColor = [0.1412 0.302 0.4784];
            app.EnthalpykJkgLabel.Position = [569 494 105 22];
            app.EnthalpykJkgLabel.Text = 'Entropy [kJ/kg/K]';

            % Create ReferenceEntropy
            app.ReferenceEntropy = uieditfield(app.IsothermgivenTemperatureonaPSDiagramUIFigure, 'text');
            app.ReferenceEntropy.Editable = 'off';
            app.ReferenceEntropy.Position = [691 494 176 22];

            % Create ExportButton
            app.ExportButton = uibutton(app.IsothermgivenTemperatureonaPSDiagramUIFigure, 'push');
            app.ExportButton.ButtonPushedFcn = createCallbackFcn(app, @ExportButtonPushed, true);
            app.ExportButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.ExportButton.FontWeight = 'bold';
            app.ExportButton.FontColor = [0.1412 0.302 0.4784];
            app.ExportButton.Visible = 'off';
            app.ExportButton.Position = [764 48 100 22];
            app.ExportButton.Text = 'Export';

            % Create BackButton
            app.BackButton = uibutton(app.IsothermgivenTemperatureonaPSDiagramUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [764 14 100 22];
            app.BackButton.Text = 'Back';

            % Show the figure after all components are created
            app.IsothermgivenTemperatureonaPSDiagramUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Entropy1

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.IsothermgivenTemperatureonaPSDiagramUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.IsothermgivenTemperatureonaPSDiagramUIFigure)
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
% Isotherm Temperature [K]
Ti=str2double(app.IsothermTemperature.Value);
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
Integralcp_T=Acp*log(Ti/T0)+Bcp*(Ti-T0)+Ccp*(Ti^2-T0^2)/2+Dcp*(Ti^3-T0^3)/3+Ecp*(Ti^4-T0^4)/4; % [kJ/kmol/K]
Tr=Ti/Tc;
if eos==2
    alpha=Tr^(-1/2);
elseif eos>2
    alpha=(1+p*(1-Tr^(1/2)))^2;
    derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
end
a=psi*alpha*(R*Tc)^2/Pc;
Sfug=zeros(1,2);
Pfug=zeros(1,2);
Sant=zeros(1,2);
Pant=zeros(1,2);
Zant=zeros(1,2);
Sexp=zeros(1,2);
Vexp=zeros(1,2);
Pexp=zeros(1,2);
Zexp=zeros(1,2);
P=[];
S=[];
Z=[];
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
Pfug(1)=Paux;
Pfug(2)=Paux;
beta=Paux*b/(R*Ti);
if eos==1 
    I=beta/(Zliquid+epsilon*beta);
else
    I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
end
SR=R2*(log(Zliquid-beta)+derivate*q*I);
Sfug(1)=(-SR0+SR+S0+Integralcp_T-R2*log(Pfug(1)/P0))/MM;
if eos==1
    I=beta/(Zvapor+epsilon*beta);
else
    I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
end
SR=R2*(log(Zvapor-beta)+derivate*q*I);
Sfug(2)=(-SR0+SR+S0+Integralcp_T-R2*log(Pfug(2)/P0))/MM;
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
Z(1)=P(1)*Vstart/(R*Ti);
beta=P(1)*b/(R*Ti);
if eos==1 
    I=beta/(Z(1)+epsilon*beta);
else
    I=log((Z(1)+sigma*beta)/(Z(1)+epsilon*beta))/(sigma-epsilon);
end
SR=R2*(log(Z(1)-beta)+derivate*q*I);
S(1)=(-SR0+SR+S0+Integralcp_T-R2*log(P(1)/P0))/MM;
j=2;
while Vnext<Vliquid
    P(j)=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    Z(j)=P(j)*Vnext/(R*Ti);
    beta=P(j)*b/(R*Ti);
    if eos==1 
        I=beta/(Z(j)+epsilon*beta);
    else
        I=log((Z(j)+sigma*beta)/(Z(j)+epsilon*beta))/(sigma-epsilon);
    end
    SR=R2*(log(Z(j)-beta)+derivate*q*I);
    S(j)=(-SR0+SR+S0+Integralcp_T-R2*log(P(j)/P0))/MM;
    Vnext=Vnext+step;
    j=j+1;
end
% Save data to graph the loop of the EoS: Saturated Liquid-Vapor;
jl=j-1;
P(j)=Paux;
S(j)=Sfug(1);
Z(j)=Zliquid;
j=j+1;
P(j)=Paux;
S(j)=Sfug(2);
Z(j)=Zvapor;
j=j+1;
% Save data to graph the loop of the EoS: Vapor
Vnext=Vvapor+1;
Vmax=Vvapor+10000;
step=(Vmax-Vnext)/5000;
while Vnext<Vmax
    P(j)=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    Z(j)=P(j)*Vnext/(R*Ti);
    beta=P(j)*b/(R*Ti);
    if eos==1 
        I=beta/(Z(j)+epsilon*beta);
    else
        I=log((Z(j)+sigma*beta)/(Z(j)+epsilon*beta))/(sigma-epsilon);
    end
    SR=R2*(log(Z(j)-beta)+derivate*q*I);
    S(j)=(-SR0+SR+S0+Integralcp_T-R2*log(P(j)/P0))/MM;
    Vnext=Vnext+step;
    j=j+1;
end
% Find Psat using Antoine Equation
Pant(1)=exp(A-B/(Ti+C))*0.01;
Pant(2)=Pant(1);
liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Pant(1)*(b-V))/a)-V;
Vantl=fsolve(liquid,b,options);
Zant(1)=Pant(1)*Vantl/(R*Ti);
vapor=@(V) (R*Ti/Pant(2)+b-a/Pant(2)*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
Vantv=fsolve(vapor,R*Ti/Pant(2),options);
Zant(2)=Pant(2)*Vantv/(R*Ti);
beta=Pant(1)*b/(R*Ti);
if eos==1 
    I=beta/(Zant(1)+epsilon*beta);
else
    I=log((Zant(1)+sigma*beta)/(Zant(1)+epsilon*beta))/(sigma-epsilon);
end
SR=R2*(log(Zant(1)-beta)+derivate*q*I);
Sant(1)=(-SR0+SR+S0+Integralcp_T-R2*log(Pant(1)/P0))/MM;
if eos==1 
  I=beta/(Zant(2)+epsilon*beta);
else
  I=log((Zant(2)+sigma*beta)/(Zant(2)+epsilon*beta))/(sigma-epsilon);
end
SR=R2*(log(Zant(2)-beta)+derivate*q*I);
Sant(2)=(-SR0+SR+S0+Integralcp_T-R2*log(Pant(2)/P0))/MM;
% Find Psat, Sliquid, and Svapor using the experimental data matrix
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
Pexp(1)=table2array(data2(app.IsothermTemperature.Value,1));
Pexp(2)=table2array(data2(app.IsothermTemperature.Value,1));
Vexp(1)=table2array(data2(app.IsothermTemperature.Value,2));
Vexp(2)=table2array(data2(app.IsothermTemperature.Value,3));
Sexp(1)=table2array(data2(app.IsothermTemperature.Value,6));
Sexp(2)=table2array(data2(app.IsothermTemperature.Value,7));
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
if ~(~ismissing(Sexp(1)) && string(Sexp(1))~="NaN")
    Sexp(1)=NaN;
end
if ~(~ismissing(Sexp(2)) && string(Sexp(2))~="NaN")
    Sexp(2)=NaN;
end
% Figure: Isotherm given Temperature on a PS Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Sfug,Pfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Sant,Pant,"Marker","^","LineStyle","none","Color","r");
plot(app.Figure1,Sexp,Pexp,"Marker","o","LineStyle","none","Color",[0.1 0.5 0.1]);
plot(app.Figure1,Sfug,Pfug,"LineStyle","--","Color","b");
plot(app.Figure1,S,P,"Color",[0.5 0 0.5]);
Smin=min([Sfug(1) Sant(1) Sexp(1)]);
Smax=max([Sfug(2) Sant(2) Sexp(2)]);
Pmin=min([Pfug(1) Pant(1) Pexp(1)]);
Pmax=max([Pfug(1) Pant(1) Pexp(1)]);
axis(app.Figure1,[Smin-abs(Smax-Smin)*0.5 Smax+abs(Smax-Smin)*0.5 max([0 Pmin-10]) Pmax+10]);
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
% Report results: Isotherm given Temperature on a PH Diagram
phase=strings;
Pp=strings;
Zp=strings;
Sp=strings;
k=1;
% Liquid
step=max([floor(jl/100) 1]);
j=1;
while j<=jl
    phase(k)="Liquid";
    Pp(k)=string(P(j));
    Zp(k)=string(Z(j));
    Sp(k)=string(S(j));
    j=j+step;
    k=k+1;
end
% Saturated Liquid-Vapor
% Test Fugacity: Choice of thermodynamically possible cases
if Pfug(1)<Pt
    phase(k)="*Satured Liquid (Fugacity Test)";
elseif Pfug(1)>Pc
    phase(k)="**Satured Liquid (Fugacity Test)";
else
    phase(k)="Satured Liquid (Fugacity Test)";
end
Pp(k)=string(Pfug(1));
Zp(k)=string(Zliquid);
Sp(k)=string(Sfug(1));
k=k+1;
if Pfug(1)<Pt
    phase(k)="*Satured Vapor (Fugacity Test)";
elseif Pfug(1)>Pc
    phase(k)="**Satured Vapor (Fugacity Test)";
else
    phase(k)="Satured Vapor (Fugacity Test)";
end
Pp(k)=string(Pfug(1));
Zp(k)=string(Zvapor);
Sp(k)=string(Sfug(2));
k=k+1;
% Antoine Equation: Choice of thermodynamically possible cases
if Pant(1)<Pt
    phase(k)="*Satured Liquid (Antoine Equation)";
elseif Pant(1)>Pc
    phase(k)="**Satured Liquid (Antoine Equation)";
else
    phase(k)="Satured Liquid (Antoine Equation)";
end
Pp(k)=string(Pant(1));
Zp(k)=string(Zant(1));
Sp(k)=string(Sant(1));
k=k+1;
if Pant(1)<Pt
    phase(k)="*Satured Vapor (Antoine Equation)";
elseif Pant(1)>Pc
    phase(k)="**Satured Vapor (Antoine Equation)";
else
    phase(k)="Satured Vapor (Antoine Equation)";
end
Pp(k)=string(Pant(1));
Zp(k)=string(Zant(2));
Sp(k)=string(Sant(2));
k=k+1;
% Experimental data
if ~isnan(Pexp(1))
    Pex=string(Pexp(1));
else
    Pex="NA";
end
if ~isnan(Sexp(1))
    Sexl=string(Sexp(1));
else
    Sexl="NA";
end
if ~isnan(Sexp(2))
    Sexv=string(Sexp(2));
else
    Sexv="NA";
end
phase(k)="Satured Liquid (Experimental Data)";
Pp(k)=Pex;
Zp(k)=Zexl;
Sp(k)=Sexl;
k=k+1;
phase(k)="Satured Vapor (Experimental Data)";
Pp(k)=Pex;
Zp(k)=Zexv;
Sp(k)=Sexv;
k=k+1;
% Vapor
% Find first point in the vapor phase
step=max([floor((length(P)-jl-2)/100) 1]);
j=jl+3;
while j<=length(P)
    phase(k)="Vapor";
    Pp(k)=string(P(j));
    Zp(k)=string(Z(j));
    Sp(k)=string(S(j));
    j=j+step;
    k=k+1;
end
app.Table1.Data=[phase;Pp;Zp;Sp]';
```