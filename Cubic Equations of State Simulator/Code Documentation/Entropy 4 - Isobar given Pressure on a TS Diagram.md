# Isobar given Pressure on a TS Diagram

This is the fourth option in the entropy menu. Its interface is programmed in "Entropy4.mlapp" and it uses the function called "Isobar_given_Pressure_TS_Diagram.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/entropy4.jpg" width="720" height="531">

*Figure 1. Design View in Entropy4.mlapp.*

### 1.2. Code View

```Matlab
classdef Entropy4 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        IsobargivenPressureonaTSDiagramUIFigure  matlab.ui.Figure
        CriticalPressure              matlab.ui.control.EditField
        CalculatedPressurebarLabel_2  matlab.ui.control.Label
        CriticalTemperature           matlab.ui.control.EditField
        TemperatureKLabel_3           matlab.ui.control.Label
        TriplePressure                matlab.ui.control.EditField
        CalculatedPressurebarLabel    matlab.ui.control.Label
        TripleTemperature             matlab.ui.control.EditField
        TemperatureKLabel_2           matlab.ui.control.Label
        Label_5                       matlab.ui.control.Label
        Label_4                       matlab.ui.control.Label
        Label_3                       matlab.ui.control.Label
        BackButton                    matlab.ui.control.Button
        ExportButton                  matlab.ui.control.Button
        ReferenceEntropy              matlab.ui.control.EditField
        EnthalpykJkgLabel             matlab.ui.control.Label
        ReferencePressure             matlab.ui.control.EditField
        PressurebarEditFieldLabel_2   matlab.ui.control.Label
        ReferenceTemperature          matlab.ui.control.EditField
        TemperatureKLabel             matlab.ui.control.Label
        ReferenceState                matlab.ui.control.EditField
        StateLabel                    matlab.ui.control.Label
        Label_2                       matlab.ui.control.Label
        IsobarPressure                matlab.ui.control.DropDown
        IsothermTemperatureKLabel     matlab.ui.control.Label
        Compound                      matlab.ui.control.DropDown
        CompoundDropDownLabel         matlab.ui.control.Label
        EoS                           matlab.ui.control.DropDown
        CubicEquationofStateDropDownLabel  matlab.ui.control.Label
        Table1                        matlab.ui.control.Table
        IsobargivenPressureonaTSDiagramLabel  matlab.ui.control.Label
        Image                         matlab.ui.control.Image
        CalculateButton               matlab.ui.control.Button
        Figure1                       matlab.ui.control.UIAxes
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.IsobargivenPressureonaTSDiagramUIFigure,"north");
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
            % Isobar Pressure
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
                app.IsobarPressure.Items=aux;
            else
                app.IsobarPressure.Items={};
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
            title(app.Figure1,"EoS - Compound @ Isobar Pressure");
            cla(app.Figure1);
            app.Table1.Data={};
            app.CriticalTemperature.Value="";
            app.CriticalPressure.Value="";
            app.TripleTemperature.Value="";
            app.TriplePressure.Value="";
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
            % Isobar Pressure
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
                app.IsobarPressure.Items=aux;
            else
                app.IsobarPressure.Items={};
            end
        end

        % Button pushed function: CalculateButton
        function CalculateButtonPushed(app, event)
            if isempty(convertCharsToStrings(app.IsobarPressure.Value)) || app.ReferenceState.Value=="NaN" || app.ReferenceTemperature.Value=="NaN" || app.ReferencePressure.Value=="NaN" || app.ReferenceEntropy.Value=="NaN"
                uialert(app.IsobargivenPressureonaTSDiagramUIFigure,"Incomplete Data.","Data Status","Icon","warning");
            else
                progressbar=uiprogressdlg(app.IsobargivenPressureonaTSDiagramUIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                Isobar_given_Pressure_TS_Diagram;
                app.ExportButton.Visible="on";
                close(progressbar);
            end
        end

        % Value changed function: EoS
        function EoSValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound @ Isobar Pressure");
            app.CriticalTemperature.Value="";
            app.CriticalPressure.Value="";
            app.TripleTemperature.Value="";
            app.TriplePressure.Value="";
            cla(app.Figure1);
            app.Table1.Data={};
        end

        % Value changed function: IsobarPressure
        function IsobarPressureValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound @ Isobar Pressure");
            app.CriticalTemperature.Value="";
            app.CriticalPressure.Value="";
            app.TripleTemperature.Value="";
            app.TriplePressure.Value="";
            cla(app.Figure1);
            app.Table1.Data={};
        end

        % Button pushed function: ExportButton
        function ExportButtonPushed(app, event)
            progressbar=uiprogressdlg(app.IsobargivenPressureonaTSDiagramUIFigure,"Title","Status","Message","Exporting","Indeterminate","on","Cancelable","off");
            drawnow;
            aux=app.Table1.Data;
            table1=table(aux(:,1),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)));
            table1.Properties.VariableNames{'Var1'}='Phase';
            table1.Properties.VariableNames{'Var2'}='T [K]';
            table1.Properties.VariableNames{'Var3'}='Z';
            table1.Properties.VariableNames{'Var4'}='S [kJ/kg/K]';
            writecell(cell(5000,4),"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A1");
            writetable(table1,"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A12");
            writecell({'Compound'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A1");
            writecell({'Cubic Equation of State'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A2");
            writecell({'Isobar Pressure [bar]'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A3");
            writecell({'Reference State'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A4");
            writecell({'Reference Temperature [K]'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A5");
            writecell({'Reference Pressure [bar]'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A6");
            writecell({'Reference Entropy [kJ/kg/K]'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A7");
            writecell({'Triple Temperature [K]'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A8");
            writecell({'Calculated Triple Pressure [bar]'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A9");
            writecell({'Close to Critical Temperature (CCT) [K]'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A10");
            writecell({'Calculated Pressure given CCT [bar]'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","A11");
            writecell({app.Compound.Value},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","B1");
            writecell({app.EoS.Value},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","B2");
            writematrix(str2double({app.IsobarPressure.Value}),"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","B3");
            writecell({app.ReferenceState.Value},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","B4");
            writematrix(str2double({app.ReferenceTemperature.Value}),"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","B5");
            writematrix(str2double({app.ReferencePressure.Value}),"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","B6");
            writematrix(str2double({app.ReferenceEntropy.Value}),"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","B7");
            writematrix(str2double({app.TripleTemperature.Value}),"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","B8");
            writematrix(str2double({app.TriplePressure.Value}),"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","B9");
            writematrix(str2double({app.CriticalTemperature.Value}),"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","B10");
            writematrix(str2double({app.CriticalPressure.Value}),"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range","B11");
            for i=1:height(table1)
                if string(table2cell(table1(i,1)))=="Satured Liquid (Experimental Data)"
                    index=i+12;
                    break;
                end
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index,2,index,2])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['B',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index+1,2,index+1,2])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['B',num2str(index+1)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index,3,index,3])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['C',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index+1,3,index+1,3])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['C',num2str(index+1)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index,4,index,4])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['D',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index+1,4,index+1,4])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['D',num2str(index+1)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-4,2,index-4,2])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['B',num2str(index-4)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-3,2,index-3,2])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['B',num2str(index-3)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-4,3,index-4,3])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['C',num2str(index-4)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-3,3,index-3,3])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['C',num2str(index-3)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-4,4,index-4,4])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['D',num2str(index-4)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-3,4,index-3,4])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TS Diagram.xlsx","Sheet","Isobar given Pressure","Range",['D',num2str(index-3)]);
            end
            close(progressbar);
            uialert(app.IsobargivenPressureonaTSDiagramUIFigure,"Finished Export.","Export Status","Icon","success");
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create IsobargivenPressureonaTSDiagramUIFigure and hide until all components are created
            app.IsobargivenPressureonaTSDiagramUIFigure = uifigure('Visible', 'off');
            app.IsobargivenPressureonaTSDiagramUIFigure.Color = [1 1 1];
            app.IsobargivenPressureonaTSDiagramUIFigure.Position = [100 100 896 661];
            app.IsobargivenPressureonaTSDiagramUIFigure.Name = 'Isobar given Pressure on a TS Diagram';
            app.IsobargivenPressureonaTSDiagramUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.IsobargivenPressureonaTSDiagramUIFigure.Resize = 'off';

            % Create Figure1
            app.Figure1 = uiaxes(app.IsobargivenPressureonaTSDiagramUIFigure);
            title(app.Figure1, 'EoS - Compound @ Isobar Pressure')
            xlabel(app.Figure1, 'S [kJ/kg/K]')
            ylabel(app.Figure1, 'T [K]')
            zlabel(app.Figure1, 'Z')
            app.Figure1.XGrid = 'on';
            app.Figure1.XMinorGrid = 'on';
            app.Figure1.YGrid = 'on';
            app.Figure1.Position = [84 78 488 398];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.IsobargivenPressureonaTSDiagramUIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [764 463 99 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Image
            app.Image = uiimage(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.Image.Position = [25 500 116 101];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create IsobargivenPressureonaTSDiagramLabel
            app.IsobargivenPressureonaTSDiagramLabel = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.IsobargivenPressureonaTSDiagramLabel.HorizontalAlignment = 'center';
            app.IsobargivenPressureonaTSDiagramLabel.FontSize = 20;
            app.IsobargivenPressureonaTSDiagramLabel.FontWeight = 'bold';
            app.IsobargivenPressureonaTSDiagramLabel.FontColor = [0.1412 0.302 0.4784];
            app.IsobargivenPressureonaTSDiagramLabel.Position = [1 622 896 26];
            app.IsobargivenPressureonaTSDiagramLabel.Text = 'Isobar given Pressure on a TS Diagram';

            % Create Table1
            app.Table1 = uitable(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.Table1.ColumnName = {'Phase'; 'T [K]'; 'Z'; 'S [kJ/kg/K]'};
            app.Table1.RowName = {};
            app.Table1.Position = [589 271 230 183];

            % Create CubicEquationofStateDropDownLabel
            app.CubicEquationofStateDropDownLabel = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.CubicEquationofStateDropDownLabel.HorizontalAlignment = 'right';
            app.CubicEquationofStateDropDownLabel.FontWeight = 'bold';
            app.CubicEquationofStateDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CubicEquationofStateDropDownLabel.Position = [163 533 141 22];
            app.CubicEquationofStateDropDownLabel.Text = 'Cubic Equation of State';

            % Create EoS
            app.EoS = uidropdown(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.EoS.Items = {'van der Waals', 'Redlich-Kwong', 'Soave-Redlich-Kwong', 'Peng-Robinson'};
            app.EoS.ValueChangedFcn = createCallbackFcn(app, @EoSValueChanged, true);
            app.EoS.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EoS.Position = [320 533 220 22];
            app.EoS.Value = 'van der Waals';

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [166 572 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [321 572 220 22];
            app.Compound.Value = {};

            % Create IsothermTemperatureKLabel
            app.IsothermTemperatureKLabel = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.IsothermTemperatureKLabel.HorizontalAlignment = 'right';
            app.IsothermTemperatureKLabel.FontWeight = 'bold';
            app.IsothermTemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.IsothermTemperatureKLabel.Position = [178 495 126 22];
            app.IsothermTemperatureKLabel.Text = 'Isobar Pressure [bar]';

            % Create IsobarPressure
            app.IsobarPressure = uidropdown(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.IsobarPressure.Items = {};
            app.IsobarPressure.ValueChangedFcn = createCallbackFcn(app, @IsobarPressureValueChanged, true);
            app.IsobarPressure.BackgroundColor = [0.8588 0.9608 0.9608];
            app.IsobarPressure.Position = [319 495 222 22];
            app.IsobarPressure.Value = {};

            % Create Label_2
            app.Label_2 = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.Label_2.HorizontalAlignment = 'center';
            app.Label_2.FontWeight = 'bold';
            app.Label_2.FontColor = [0.1412 0.302 0.4784];
            app.Label_2.Position = [672 593 93 22];
            app.Label_2.Text = 'Reference Data';

            % Create StateLabel
            app.StateLabel = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.StateLabel.HorizontalAlignment = 'right';
            app.StateLabel.FontWeight = 'bold';
            app.StateLabel.FontColor = [0.1412 0.302 0.4784];
            app.StateLabel.Position = [571 571 103 22];
            app.StateLabel.Text = 'State';

            % Create ReferenceState
            app.ReferenceState = uieditfield(app.IsobargivenPressureonaTSDiagramUIFigure, 'text');
            app.ReferenceState.Editable = 'off';
            app.ReferenceState.Position = [691 571 172 22];

            % Create TemperatureKLabel
            app.TemperatureKLabel = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.TemperatureKLabel.HorizontalAlignment = 'right';
            app.TemperatureKLabel.FontWeight = 'bold';
            app.TemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.TemperatureKLabel.Position = [571 545 103 22];
            app.TemperatureKLabel.Text = 'Temperature [K]';

            % Create ReferenceTemperature
            app.ReferenceTemperature = uieditfield(app.IsobargivenPressureonaTSDiagramUIFigure, 'text');
            app.ReferenceTemperature.Editable = 'off';
            app.ReferenceTemperature.Position = [691 545 172 22];

            % Create PressurebarEditFieldLabel_2
            app.PressurebarEditFieldLabel_2 = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.PressurebarEditFieldLabel_2.HorizontalAlignment = 'right';
            app.PressurebarEditFieldLabel_2.FontWeight = 'bold';
            app.PressurebarEditFieldLabel_2.FontColor = [0.1412 0.302 0.4784];
            app.PressurebarEditFieldLabel_2.Position = [571 520 103 22];
            app.PressurebarEditFieldLabel_2.Text = 'Pressure [bar]';

            % Create ReferencePressure
            app.ReferencePressure = uieditfield(app.IsobargivenPressureonaTSDiagramUIFigure, 'text');
            app.ReferencePressure.Editable = 'off';
            app.ReferencePressure.Position = [691 520 172 22];

            % Create EnthalpykJkgLabel
            app.EnthalpykJkgLabel = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.EnthalpykJkgLabel.HorizontalAlignment = 'right';
            app.EnthalpykJkgLabel.FontWeight = 'bold';
            app.EnthalpykJkgLabel.FontColor = [0.1412 0.302 0.4784];
            app.EnthalpykJkgLabel.Position = [569 494 105 22];
            app.EnthalpykJkgLabel.Text = 'Entropy [kJ/kg/K]';

            % Create ReferenceEntropy
            app.ReferenceEntropy = uieditfield(app.IsobargivenPressureonaTSDiagramUIFigure, 'text');
            app.ReferenceEntropy.Editable = 'off';
            app.ReferenceEntropy.Position = [691 494 172 22];

            % Create ExportButton
            app.ExportButton = uibutton(app.IsobargivenPressureonaTSDiagramUIFigure, 'push');
            app.ExportButton.ButtonPushedFcn = createCallbackFcn(app, @ExportButtonPushed, true);
            app.ExportButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.ExportButton.FontWeight = 'bold';
            app.ExportButton.FontColor = [0.1412 0.302 0.4784];
            app.ExportButton.Visible = 'off';
            app.ExportButton.Position = [764 48 100 22];
            app.ExportButton.Text = 'Export';

            % Create BackButton
            app.BackButton = uibutton(app.IsobargivenPressureonaTSDiagramUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [764 14 100 22];
            app.BackButton.Text = 'Back';

            % Create Label_3
            app.Label_3 = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.Label_3.FontSize = 11;
            app.Label_3.FontWeight = 'bold';
            app.Label_3.FontColor = [0.1412 0.302 0.4784];
            app.Label_3.Position = [42 14 571 65];
            app.Label_3.Text = {'Symbology'; 'NaN: Not a Number.'; 'NA: Not Available.'; '*: Thermodynamically not possible case because the temperature is less than the triple temperature.'; '**: Thermodynamically not possible case because the temperature is greater than the critical temperature.'};

            % Create Label_4
            app.Label_4 = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.Label_4.HorizontalAlignment = 'center';
            app.Label_4.FontWeight = 'bold';
            app.Label_4.FontColor = [0.1412 0.302 0.4784];
            app.Label_4.Position = [720 240 71 22];
            app.Label_4.Text = 'Triple Point';

            % Create Label_5
            app.Label_5 = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.Label_5.HorizontalAlignment = 'center';
            app.Label_5.FontWeight = 'bold';
            app.Label_5.FontColor = [0.1412 0.302 0.4784];
            app.Label_5.Position = [689 152 130 22];
            app.Label_5.Text = 'Close to Critical Point';

            % Create TemperatureKLabel_2
            app.TemperatureKLabel_2 = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.TemperatureKLabel_2.HorizontalAlignment = 'right';
            app.TemperatureKLabel_2.FontWeight = 'bold';
            app.TemperatureKLabel_2.FontColor = [0.1412 0.302 0.4784];
            app.TemperatureKLabel_2.Position = [646 215 103 22];
            app.TemperatureKLabel_2.Text = 'Temperature [K]';

            % Create TripleTemperature
            app.TripleTemperature = uieditfield(app.IsobargivenPressureonaTSDiagramUIFigure, 'text');
            app.TripleTemperature.Editable = 'off';
            app.TripleTemperature.Position = [766 215 98 22];

            % Create CalculatedPressurebarLabel
            app.CalculatedPressurebarLabel = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.CalculatedPressurebarLabel.HorizontalAlignment = 'right';
            app.CalculatedPressurebarLabel.FontWeight = 'bold';
            app.CalculatedPressurebarLabel.FontColor = [0.1412 0.302 0.4784];
            app.CalculatedPressurebarLabel.Position = [598 187 151 22];
            app.CalculatedPressurebarLabel.Text = 'Calculated Pressure [bar]';

            % Create TriplePressure
            app.TriplePressure = uieditfield(app.IsobargivenPressureonaTSDiagramUIFigure, 'text');
            app.TriplePressure.Editable = 'off';
            app.TriplePressure.Position = [766 187 98 22];

            % Create TemperatureKLabel_3
            app.TemperatureKLabel_3 = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.TemperatureKLabel_3.HorizontalAlignment = 'right';
            app.TemperatureKLabel_3.FontWeight = 'bold';
            app.TemperatureKLabel_3.FontColor = [0.1412 0.302 0.4784];
            app.TemperatureKLabel_3.Position = [645 127 103 22];
            app.TemperatureKLabel_3.Text = 'Temperature [K]';

            % Create CriticalTemperature
            app.CriticalTemperature = uieditfield(app.IsobargivenPressureonaTSDiagramUIFigure, 'text');
            app.CriticalTemperature.Editable = 'off';
            app.CriticalTemperature.Position = [765 127 98 22];

            % Create CalculatedPressurebarLabel_2
            app.CalculatedPressurebarLabel_2 = uilabel(app.IsobargivenPressureonaTSDiagramUIFigure);
            app.CalculatedPressurebarLabel_2.HorizontalAlignment = 'right';
            app.CalculatedPressurebarLabel_2.FontWeight = 'bold';
            app.CalculatedPressurebarLabel_2.FontColor = [0.1412 0.302 0.4784];
            app.CalculatedPressurebarLabel_2.Position = [597 99 151 22];
            app.CalculatedPressurebarLabel_2.Text = 'Calculated Pressure [bar]';

            % Create CriticalPressure
            app.CriticalPressure = uieditfield(app.IsobargivenPressureonaTSDiagramUIFigure, 'text');
            app.CriticalPressure.Editable = 'off';
            app.CriticalPressure.Position = [765 99 98 22];

            % Show the figure after all components are created
            app.IsobargivenPressureonaTSDiagramUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Entropy4

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.IsobargivenPressureonaTSDiagramUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.IsobargivenPressureonaTSDiagramUIFigure)
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
% Isobar Pressure [bar]
Pi=str2double(app.IsobarPressure.Value);
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
for i=1:height(data2)
    if ~ismissing(table2array(data2(i,2))) && string(table2array(data2(i,2)))~="NaN"
        if table2array(data2(i,2))==Pi
            Pindex=i;
            break;
        end
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
Tbracket=[Tt Tc-0.1];
app.TripleTemperature.Value=string(Tbracket(1));
app.CriticalTemperature.Value=string(Tbracket(2));
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
app.TriplePressure.Value=string(Pbracket(1));
app.CriticalPressure.Value=string(Pbracket(2));
% Find Tsat, Zliquid, Zvapor, Sliquid, and Svapor given P
% Fugacity test method
% Case not thermodynamically possible: Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number)
Sfug=zeros(1,2);
Tfug=zeros(1,2);
Sant=zeros(1,2);
Tant=zeros(1,2);
Zant=zeros(1,2);
Vexp=zeros(1,2);
Sexp=zeros(1,2);
Texp=zeros(1,2);
T=[];
S=[];
Z=[];
if Pi<Pbracket(1) || Pi>Pbracket(2)
    checkNaN=true;
else 
    checkNaN=false;
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
    % Save results
    Tfug(1)=Ti;
    Tfug(2)=Ti;
    beta=Pi*b/(R*Ti);
    Integralcp_T=Acp*log(Ti/T0)+Bcp*(Ti-T0)+Ccp*(Ti^2-T0^2)/2+Dcp*(Ti^3-T0^3)/3+Ecp*(Ti^4-T0^4)/4;
    if eos==1 
        I=beta/(Zliquid+epsilon*beta);
    else
        I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
    end
    SR=R2*(log(Zliquid-beta)+derivate*q*I);
    Sfug(1)=(-SR0+SR+S0+Integralcp_T-R2*log(Pi/P0))/MM;
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    SR=R2*(log(Zvapor-beta)+derivate*q*I);
    Sfug(2)=(-SR0+SR+S0+Integralcp_T-R2*log(Pi/P0))/MM;
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
        Tfunction=@(T) ((Pi+psi*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    elseif eos==2
        Tfunction=@(T) ((Pi+psi*(T/Tc)^(-1/2)*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    elseif eos==3
        Tfunction=@(T) ((Pi+psi*(1+(0.480+1.574*w-0.176*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    else
        Tfunction=@(T) ((Pi+psi*(1+(0.37464+1.54226*w-0.26992*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    end
    T(1)=fsolve(Tfunction,Ti,options);
    Integralcp_T=Acp*log(T(1)/T0)+Bcp*(T(1)-T0)+Ccp*(T(1)^2-T0^2)/2+Dcp*(T(1)^3-T0^3)/3+Ecp*(T(1)^4-T0^4)/4;
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
    SR=R2*(log(Z(1)-beta)+derivate*q*I);
    S(1)=(-SR0+SR+S0+Integralcp_T-R2*log(Pi/P0))/MM;
    step=(Vliquid-Vstart)/5000;
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
        Integralcp_T=Acp*log(T(j)/T0)+Bcp*(T(j)-T0)+Ccp*(T(j)^2-T0^2)/2+Dcp*(T(j)^3-T0^3)/3+Ecp*(T(j)^4-T0^4)/4;
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
        SR=R2*(log(Z(j)-beta)+derivate*q*I);
        S(j)=(-SR0+SR+S0+Integralcp_T-R2*log(Pi/P0))/MM; 
        Vnext=Vnext+step;
        j=j+1;
    end
    % Save data to graph the loop of the EoS: Saturated Liquid-Vapor
    jl=j-1;
    T(j)=Ti;
    S(j)=Sfug(1);
    Z(j)=Zliquid;
    j=j+1;
    T(j)=Ti;
    S(j)=Sfug(2);
    Z(j)=Zvapor;
    j=j+1;
    % Save data to graph the loop of the EoS: Vapor
    Vnext=Vvapor+1;
    Vmax=Vvapor+5000;
    step=(Vmax-Vnext)/5000;
    while Vnext<Vmax
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
        Integralcp_T=Acp*log(T(j)/T0)+Bcp*(T(j)-T0)+Ccp*(T(j)^2-T0^2)/2+Dcp*(T(j)^3-T0^3)/3+Ecp*(T(j)^4-T0^4)/4;
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
        SR=R2*(log(Z(j)-beta)+derivate*q*I);
        S(j)=(-SR0+SR+S0+Integralcp_T-R2*log(Pi/P0))/MM; 
        Vnext=Vnext+step;
        j=j+1;
    end
end
% Find Tsat using Antoine Equation
Tant(1)=-B/(log(Pi/0.01)-A)-C;
Tant(2)=Tant(1);
Tr=Tant(1)/Tc;
beta=Pi*b/(R*Tant(1));
Integralcp_T=Acp*log(Tant(1)/T0)+Bcp*(Tant(1)-T0)+Ccp*(Tant(1)^2-T0^2)/2+Dcp*(Tant(1)^3-T0^3)/3+Ecp*(Tant(1)^4-T0^4)/4;
if eos==2
    alpha=Tr^(-1/2);
elseif eos>2
    alpha=(1+p*(1-Tr^(1/2)))^2;
    derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
end
a=psi*alpha*(R*Tc)^2/Pc;
q=a/(b*R*Tant(1));
liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Tant(1)+Pi*(b-V))/a)-V;
Vantl=fsolve(liquid,b,options);
Zant(1)=Pi*Vantl/(R*Tant(1));
vapor=@(V) (R*Tant(2)/Pi+b-a/Pi*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
Vantv=fsolve(vapor,R*Tant(2)/Pi,options);
Zant(2)=Pi*Vantv/(R*Tant(2));
if eos==1 
    I=beta/(Zant(1)+epsilon*beta);
else
    I=log((Zant(1)+sigma*beta)/(Zant(1)+epsilon*beta))/(sigma-epsilon);
end
SR=R2*(log(Zant(1)-beta)+derivate*q*I);
Sant(1)=(-SR0+SR+S0+Integralcp_T-R2*log(Pi/P0))/MM; 
if eos==1 
    I=beta/(Zant(2)+epsilon*beta);
else
    I=log((Zant(2)+sigma*beta)/(Zant(2)+epsilon*beta))/(sigma-epsilon);
end
SR=R2*(log(Zant(2)-beta)+derivate*q*I);
Sant(2)=(-SR0+SR+S0+Integralcp_T-R2*log(Pi/P0))/MM; 
% Find Tsat, Sliquid, and Svapor using the experimental data matrix
Texp(1)=table2array(data2(Pindex,1));
Texp(2)=table2array(data2(Pindex,1));
Vexp(1)=table2array(data2(Pindex,3));
Vexp(2)=table2array(data2(Pindex,4));
Sexp(1)=table2array(data2(Pindex,7));
Sexp(2)=table2array(data2(Pindex,8));
if ~(~ismissing(Texp(1)) && string(Texp(1))~="NaN")
    Texp(1)=NaN;
    Texp(2)=NaN;
end
if ~(~ismissing(Vexp(1)) && string(Vexp(1))~="NaN")
    Vexp(1)=NaN;
end
if ~(~ismissing(Vexp(2)) && string(Vexp(2))~="NaN")
    Vexp(2)=NaN;
end
if ~isnan(Vexp(1)) && ~isnan(Texp(1))
    Zexl=string(Pi*Vexp(1)*1000*MM/(R*Texp(1)));
else
    Zexl="NA";
end
if ~isnan(Vexp(2)) && ~isnan(Texp(2))
    Zexv=string(Pi*Vexp(2)*1000*MM/(R*Texp(2)));
else
    Zexv="NA";
end
if ~(~ismissing(Sexp(1)) && string(Sexp(1))~="NaN")
    Sexp(1)=NaN;
end
if ~(~ismissing(Sexp(2)) && string(Sexp(2))~="NaN")
    Sexp(2)=NaN;
end
% Figure: Isobar given Pressure on a TS Diagram
hold(app.Figure1,"on");
if checkNaN==false
    plot(app.Figure1,Sfug,Tfug,"Marker","*","LineStyle","none","Color","b");
end
plot(app.Figure1,Sant,Tant,"Marker","^","LineStyle","none","Color","r");
plot(app.Figure1,Sexp,Texp,"Marker","o","LineStyle","none","Color",[0.1 0.5 0.1]);
if checkNaN==false
    plot(app.Figure1,S,T,"Color",[0.5 0 0.5]);
end
if checkNaN==true
    Smin=min([Sant(1) Sexp(1)]);
    Smax=max([Sant(2) Sexp(2)]);
    Tmin=min([Tant(1) Texp(1)]);
    Tmax=max([Tant(1) Texp(1)]);
else
    Smin=min([Sfug(1) Sant(1) Sexp(1)]);
    Smax=max([Sfug(2) Sant(2) Sexp(2)]);
    Tmin=min([Tfug(1) Tant(1) Texp(1)]);
    Tmax=max([Tfug(1) Tant(1) Texp(1)]);
end
axis(app.Figure1,[Smin-abs(Smax-Smin)*0.5 Smax+abs(Smax-Smin)*0.5 Tmin-10 Tmax+10]);
if eos==1
    aux=strcat("van der Waals - ",app.Compound.Value," @ ",num2str(Pi)," bar");
elseif eos==2
    aux=strcat("Redlich-Kwong - ",app.Compound.Value," @ ",num2str(Pi)," bar");
elseif eos==3
    aux=strcat("Soave-Redlich-Kwong - ",app.Compound.Value," @ ",num2str(Pi)," bar");
else
    aux=strcat("Peng-Robinson - ",app.Compound.Value," @ ",num2str(Pi)," bar");
end
title(app.Figure1,aux);
if checkNaN==false
    legend(app.Figure1,{'Fugacity Test','Antoine Equation','Experimental Data'},"Box","on","LineWidth",1,"Location","southoutside");
else
    legend(app.Figure1,{'Antoine Equation','Experimental Data'},"Box","on","LineWidth",1,"Location","southoutside");
end
hold(app.Figure1,"off");
phase=strings;
Tp=strings;
Zp=strings;
Sp=strings;
k=1;
if checkNaN==true
    % Report results: Isobar given Pressure on a TS Diagram
    % Saturated Liquid-Vapor
    phase(k)="Satured Liquid (Fugacity Test)";
    Tp(k)="NaN";
    Zp(k)="NaN";
    Sp(k)="NaN";
    k=k+1;
    phase(k)="Satured Vapor (Fugacity Test)";
    Tp(k)="NaN";
    Zp(k)="NaN";
    Sp(k)="NaN";
    k=k+1;
else
    % Report results: Isobar given Pressure on a TS Diagram
    % Liquid
    step=max([floor(jl/100) 1]);
    j=1;
    while j<=jl
        phase(k)="Liquid";
        Tp(k)=string(T(j));
        Zp(k)=string(Z(j));
        Sp(k)=string(S(j));
        j=j+step;
        k=k+1;
    end
    % Saturated Liquid-Vapor
    phase(k)="Satured Liquid (Fugacity Test)";
    Tp(k)=string(Ti);
    Zp(k)=string(Zliquid);
    Sp(k)=string(Sfug(1));
    k=k+1;
    phase(k)="Satured Vapor (Fugacity Test)";
    Tp(k)=string(Ti);
    Zp(k)=string(Zvapor);
    Sp(k)=string(Sfug(2));
    k=k+1;
end
% Antoine Equation: Choice of thermodynamically possible cases
if Tant(1)<Tt
    phase(k)="*Satured Liquid (Antoine Equation)";
elseif Tant(1)>Tc
    phase(k)="**Satured Liquid (Antoine Equation)";
else
    phase(k)="Satured Liquid (Antoine Equation)";
end
Tp(k)=string(Tant(1));
Zp(k)=string(Zant(1));
Sp(k)=string(Sant(1));
k=k+1;
if Tant(1)<Tt
    phase(k)="*Satured Vapor (Antoine Equation)";
elseif Tant(1)>Tc
    phase(k)="**Satured Vapor (Antoine Equation)";
else
    phase(k)="Satured Vapor (Antoine Equation)";
end
Tp(k)=string(Tant(1));
Zp(k)=string(Zant(2));
Sp(k)=string(Sant(2));
k=k+1;
% Experimental data
if ~isnan(Texp(1))
    Tex=string(Texp(1));
else
    Tex="NA";
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
Tp(k)=Tex;
Zp(k)=Zexl;
Sp(k)=Sexl;
k=k+1;
phase(k)="Satured Vapor (Experimental Data)";
Tp(k)=Tex;
Zp(k)=Zexv;
Sp(k)=Sexv;
k=k+1;
if checkNaN==false
    % Vapor
    step=max([floor((length(T)-jl-2)/100) 1]);
    j=jl+3;
    while j<=length(T)
        phase(k)="Vapor";
        Tp(k)=string(T(j));
        Zp(k)=string(Z(j));
        Sp(k)=string(S(j));
        j=j+step;
        k=k+1;
    end
end
app.Table1.Data=[phase;Tp;Zp;Sp]';
% Notify if the case is thermodynamically not possible
% Test Fugacity
if checkNaN==true
    uialert(app.IsobargivenPressureonaTSDiagramUIFigure,"Test Fugacity: Thermodynamically not possible case because Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number).","Error","Icon","error");
end
```