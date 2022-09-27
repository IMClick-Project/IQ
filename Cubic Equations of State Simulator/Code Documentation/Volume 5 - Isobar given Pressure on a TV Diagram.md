# Isobar given Pressure on a TV Diagram

This is the fifth option in the volume menu. Its interface is programmed in "Volume5.mlapp" and it uses the function called "Isobar_given_Pressure_TV_Diagram.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/volume5.jpg" width="928" height="551">

*Figure 1. Design View in Volume5.mlapp.*

### 1.2. Code View

```Matlab
classdef Volume5 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        IsobargivenPressureonaTVDiagramUIFigure  matlab.ui.Figure
        CriticalPressure              matlab.ui.control.EditField
        CalculatedPressurebarLabel_2  matlab.ui.control.Label
        CriticalTemperature           matlab.ui.control.EditField
        TemperatureKLabel_2           matlab.ui.control.Label
        Label_3                       matlab.ui.control.Label
        TriplePressure                matlab.ui.control.EditField
        CalculatedPressurebarLabel    matlab.ui.control.Label
        TripleTemperature             matlab.ui.control.EditField
        TemperatureKLabel             matlab.ui.control.Label
        Label_2                       matlab.ui.control.Label
        IsobarPressure                matlab.ui.control.DropDown
        IsothermTemperatureKLabel     matlab.ui.control.Label
        Compound                      matlab.ui.control.DropDown
        CompoundDropDownLabel         matlab.ui.control.Label
        EoS                           matlab.ui.control.DropDown
        CubicEquationofStateDropDownLabel  matlab.ui.control.Label
        Label                         matlab.ui.control.Label
        BackButton                    matlab.ui.control.Button
        Table1                        matlab.ui.control.Table
        ExportButton                  matlab.ui.control.Button
        Table2                        matlab.ui.control.Table
        IsobargivenPressureonaTVDiagramLabel  matlab.ui.control.Label
        Image                         matlab.ui.control.Image
        CalculateButton               matlab.ui.control.Button
        Figure3                       matlab.ui.control.UIAxes
        Figure2                       matlab.ui.control.UIAxes
        Figure1                       matlab.ui.control.UIAxes
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.IsobargivenPressureonaTVDiagramUIFigure,"north");
            % Compound
            data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds");
            app.Compound.Items=table2cell(data(:,1));
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
            Volume;
            delete(app);
        end

        % Button pushed function: CalculateButton
        function CalculateButtonPushed(app, event)
            if isempty(convertCharsToStrings(app.IsobarPressure.Value))
                uialert(app.IsobargivenPressureonaTVDiagramUIFigure,"Incomplete Data.","Data Status","Icon","warning");
            else
                progressbar=uiprogressdlg(app.IsobargivenPressureonaTVDiagramUIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                Isobar_given_Pressure_TV_Diagram;
                app.ExportButton.Visible="on";
                close(progressbar);
            end
        end

        % Value changed function: Compound
        function CompoundValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound @ Isobar Pressure");
            app.CriticalTemperature.Value="";
            app.CriticalPressure.Value="";
            app.TripleTemperature.Value="";
            app.TriplePressure.Value="";
            cla(app.Figure1);
            cla(app.Figure2);
            cla(app.Figure3);
            app.Table1.Data={};
            app.Table2.Data={};
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

        % Button pushed function: ExportButton
        function ExportButtonPushed(app, event)
            progressbar=uiprogressdlg(app.IsobargivenPressureonaTVDiagramUIFigure,"Title","Status","Message","Exporting","Indeterminate","on","Cancelable","off");
            drawnow;
            aux=app.Table1.Data;
            table1=table(aux(:,1),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)));
            table1.Properties.VariableNames{'Var1'}='Phase';
            table1.Properties.VariableNames{'Var2'}='T [K]';
            table1.Properties.VariableNames{'Var3'}='Z';
            table1.Properties.VariableNames{'Var4'}='V [m3/kg]';
            writecell(cell(5000,4),"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range","A1");
            writetable(table1,"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range","A4");
            writecell({'Compound'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range","A1");
            writecell({'Cubic Equation of State'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range","A2");
            writecell({'Isobar Pressure [bar]'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range","A3");
            writecell({app.Compound.Value},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range","B1");
            writecell({app.EoS.Value},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range","B2");
            writematrix(str2double({app.IsobarPressure.Value}),"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range","B3");
            for i=1:height(table1)
                if string(table2cell(table1(i,1)))=="Satured Liquid (Experimental Data)"
                    index=i+4;
                    break;
                end
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index,2,index,2])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['B',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index+1,2,index+1,2])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['B',num2str(index+1)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index,3,index,3])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['C',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index+1,3,index+1,3])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['C',num2str(index+1)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index,4,index,4])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['D',num2str(index)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index+1,4,index+1,4])))
                writecell({'NA'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['D',num2str(index+1)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-4,2,index-4,2])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['B',num2str(index-4)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-3,2,index-3,2])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['B',num2str(index-3)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-4,3,index-4,3])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['C',num2str(index-4)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-3,3,index-3,3])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['C',num2str(index-3)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-4,4,index-4,4])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['D',num2str(index-4)]);
            end
            if ismissing(string(readcell("./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",[index-3,4,index-3,4])))
                writecell({'NaN'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Isobar given Pressure","Range",['D',num2str(index-3)]);
            end
            writecell(cell(5000,3),"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","A1");
            writecell({'Triple Temperature [K]'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","A1");
            writecell({'Calculated Triple Pressure [bar]'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","A2");
            writecell({'Close to Critical Temperature (CCT) [K]'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","A3");
            writecell({'Calculated Pressure given CCT [bar]'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","A4");
            writematrix(str2double({app.TripleTemperature.Value}),"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","B1");
            writematrix(str2double({app.TriplePressure.Value}),"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","B2");
            writematrix(str2double({app.CriticalTemperature.Value}),"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","B3");
            writematrix(str2double({app.CriticalPressure.Value}),"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","B4");
            if ~isempty(app.Table2.Data)
                aux=app.Table2.Data;
                table2=table(str2double(aux(:,1)),str2double(aux(:,2)),str2double(aux(:,3)));
                table2.Properties.VariableNames{'Var1'}='Iteration Number';
                table2.Properties.VariableNames{'Var2'}='Tsat [K]';
                table2.Properties.VariableNames{'Var3'}='Psat [bar]';
                writetable(table2,"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","A5");
            else
                writecell({'Iteration Number'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","A5");
                writecell({'Tsat [K]'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","B5");
                writecell({'Psat [bar]'},"./Results/Isobar given Pressure on a TV Diagram.xlsx","Sheet","Pegasus Method","Range","C5");
            end
            close(progressbar);
            uialert(app.IsobargivenPressureonaTVDiagramUIFigure,"Finished Export.","Export Status","Icon","success");
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
            cla(app.Figure2);
            cla(app.Figure3);
            app.Table1.Data={};
            app.Table2.Data={};
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
            cla(app.Figure2);
            cla(app.Figure3);
            app.Table1.Data={};
            app.Table2.Data={};
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create IsobargivenPressureonaTVDiagramUIFigure and hide until all components are created
            app.IsobargivenPressureonaTVDiagramUIFigure = uifigure('Visible', 'off');
            app.IsobargivenPressureonaTVDiagramUIFigure.Color = [1 1 1];
            app.IsobargivenPressureonaTVDiagramUIFigure.Position = [100 100 1156 685];
            app.IsobargivenPressureonaTVDiagramUIFigure.Name = 'Isobar given Pressure on a TV Diagram';
            app.IsobargivenPressureonaTVDiagramUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.IsobargivenPressureonaTVDiagramUIFigure.Resize = 'off';

            % Create Figure1
            app.Figure1 = uiaxes(app.IsobargivenPressureonaTVDiagramUIFigure);
            title(app.Figure1, 'EoS - Compound @ Isobar Pressure')
            xlabel(app.Figure1, 'V [m^3/kg]')
            ylabel(app.Figure1, 'T [K]')
            zlabel(app.Figure1, 'Z')
            app.Figure1.XScale = 'log';
            app.Figure1.XMinorTick = 'on';
            app.Figure1.XGrid = 'on';
            app.Figure1.XMinorGrid = 'on';
            app.Figure1.YGrid = 'on';
            app.Figure1.Position = [15 89 379 390];

            % Create Figure2
            app.Figure2 = uiaxes(app.IsobargivenPressureonaTVDiagramUIFigure);
            title(app.Figure2, 'Saturation Pressure vs Saturation Temperature')
            xlabel(app.Figure2, 'Saturation Temperature [K]')
            ylabel(app.Figure2, 'Saturation Pressure [bar]')
            zlabel(app.Figure2, 'Z')
            app.Figure2.XGrid = 'on';
            app.Figure2.YGrid = 'on';
            app.Figure2.Position = [591 437 550 232];

            % Create Figure3
            app.Figure3 = uiaxes(app.IsobargivenPressureonaTVDiagramUIFigure);
            title(app.Figure3, 'Saturation Temperature vs Iteration Number')
            xlabel(app.Figure3, 'Iteration Number')
            ylabel(app.Figure3, 'Saturation Temperature [K]')
            zlabel(app.Figure3, 'Z')
            app.Figure3.XGrid = 'on';
            app.Figure3.YGrid = 'on';
            app.Figure3.Position = [591 44 390 283];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.IsobargivenPressureonaTVDiagramUIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [462 485 103 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Image
            app.Image = uiimage(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.Image.Position = [27 512 116 101];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create IsobargivenPressureonaTVDiagramLabel
            app.IsobargivenPressureonaTVDiagramLabel = uilabel(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.IsobargivenPressureonaTVDiagramLabel.HorizontalAlignment = 'center';
            app.IsobargivenPressureonaTVDiagramLabel.FontSize = 20;
            app.IsobargivenPressureonaTVDiagramLabel.FontWeight = 'bold';
            app.IsobargivenPressureonaTVDiagramLabel.FontColor = [0.1412 0.302 0.4784];
            app.IsobargivenPressureonaTVDiagramLabel.Position = [16 634 548 26];
            app.IsobargivenPressureonaTVDiagramLabel.Text = 'Isobar given Pressure on a TV Diagram';

            % Create Table2
            app.Table2 = uitable(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.Table2.ColumnName = {'Iteration Number'; 'Tsat [K]'; 'Psat [bar]'};
            app.Table2.RowName = {};
            app.Table2.Position = [1003 110 138 203];

            % Create ExportButton
            app.ExportButton = uibutton(app.IsobargivenPressureonaTVDiagramUIFigure, 'push');
            app.ExportButton.ButtonPushedFcn = createCallbackFcn(app, @ExportButtonPushed, true);
            app.ExportButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.ExportButton.FontWeight = 'bold';
            app.ExportButton.FontColor = [0.1412 0.302 0.4784];
            app.ExportButton.Visible = 'off';
            app.ExportButton.Position = [1040 56 100 22];
            app.ExportButton.Text = 'Export';

            % Create Table1
            app.Table1 = uitable(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.Table1.ColumnName = {'Phase'; 'T [K]'; 'Z'; 'V [m3/kg]'};
            app.Table1.RowName = {};
            app.Table1.Position = [406 112 158 351];

            % Create BackButton
            app.BackButton = uibutton(app.IsobargivenPressureonaTVDiagramUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [1040 24 100 22];
            app.BackButton.Text = 'Back';

            % Create Label
            app.Label = uilabel(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.Label.FontSize = 11;
            app.Label.FontWeight = 'bold';
            app.Label.FontColor = [0.1412 0.302 0.4784];
            app.Label.Position = [15 14 571 65];
            app.Label.Text = {'Symbology'; 'NaN: Not a Number.'; 'NA: Not Available.'; '*: Thermodynamically not possible case because the temperature is less than the triple temperature.'; '**: Thermodynamically not possible case because the temperature is greater than the critical temperature.'};

            % Create CubicEquationofStateDropDownLabel
            app.CubicEquationofStateDropDownLabel = uilabel(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.CubicEquationofStateDropDownLabel.HorizontalAlignment = 'right';
            app.CubicEquationofStateDropDownLabel.FontWeight = 'bold';
            app.CubicEquationofStateDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CubicEquationofStateDropDownLabel.Position = [166 551 141 22];
            app.CubicEquationofStateDropDownLabel.Text = 'Cubic Equation of State';

            % Create EoS
            app.EoS = uidropdown(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.EoS.Items = {'van der Waals', 'Redlich-Kwong', 'Soave-Redlich-Kwong', 'Peng-Robinson'};
            app.EoS.ValueChangedFcn = createCallbackFcn(app, @EoSValueChanged, true);
            app.EoS.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EoS.Position = [323 551 241 22];
            app.EoS.Value = 'van der Waals';

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [168 584 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [323 584 242 22];
            app.Compound.Value = {};

            % Create IsothermTemperatureKLabel
            app.IsothermTemperatureKLabel = uilabel(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.IsothermTemperatureKLabel.HorizontalAlignment = 'right';
            app.IsothermTemperatureKLabel.FontWeight = 'bold';
            app.IsothermTemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.IsothermTemperatureKLabel.Position = [180 519 126 22];
            app.IsothermTemperatureKLabel.Text = 'Isobar Pressure [bar]';

            % Create IsobarPressure
            app.IsobarPressure = uidropdown(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.IsobarPressure.Items = {};
            app.IsobarPressure.ValueChangedFcn = createCallbackFcn(app, @IsobarPressureValueChanged, true);
            app.IsobarPressure.BackgroundColor = [0.8588 0.9608 0.9608];
            app.IsobarPressure.Position = [321 519 243 22];
            app.IsobarPressure.Value = {};

            % Create Label_2
            app.Label_2 = uilabel(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.Label_2.HorizontalAlignment = 'center';
            app.Label_2.FontWeight = 'bold';
            app.Label_2.FontColor = [0.1412 0.302 0.4784];
            app.Label_2.Position = [711 403 71 22];
            app.Label_2.Text = 'Triple Point';

            % Create TemperatureKLabel
            app.TemperatureKLabel = uilabel(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.TemperatureKLabel.HorizontalAlignment = 'right';
            app.TemperatureKLabel.FontWeight = 'bold';
            app.TemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.TemperatureKLabel.Position = [637 378 103 22];
            app.TemperatureKLabel.Text = 'Temperature [K]';

            % Create TripleTemperature
            app.TripleTemperature = uieditfield(app.IsobargivenPressureonaTVDiagramUIFigure, 'text');
            app.TripleTemperature.Editable = 'off';
            app.TripleTemperature.Position = [757 378 98 22];

            % Create CalculatedPressurebarLabel
            app.CalculatedPressurebarLabel = uilabel(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.CalculatedPressurebarLabel.HorizontalAlignment = 'right';
            app.CalculatedPressurebarLabel.FontWeight = 'bold';
            app.CalculatedPressurebarLabel.FontColor = [0.1412 0.302 0.4784];
            app.CalculatedPressurebarLabel.Position = [589 350 151 22];
            app.CalculatedPressurebarLabel.Text = 'Calculated Pressure [bar]';

            % Create TriplePressure
            app.TriplePressure = uieditfield(app.IsobargivenPressureonaTVDiagramUIFigure, 'text');
            app.TriplePressure.Editable = 'off';
            app.TriplePressure.Position = [757 350 98 22];

            % Create Label_3
            app.Label_3 = uilabel(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.Label_3.HorizontalAlignment = 'center';
            app.Label_3.FontWeight = 'bold';
            app.Label_3.FontColor = [0.1412 0.302 0.4784];
            app.Label_3.Position = [966 400 130 22];
            app.Label_3.Text = 'Close to Critical Point';

            % Create TemperatureKLabel_2
            app.TemperatureKLabel_2 = uilabel(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.TemperatureKLabel_2.HorizontalAlignment = 'right';
            app.TemperatureKLabel_2.FontWeight = 'bold';
            app.TemperatureKLabel_2.FontColor = [0.1412 0.302 0.4784];
            app.TemperatureKLabel_2.Position = [922 375 103 22];
            app.TemperatureKLabel_2.Text = 'Temperature [K]';

            % Create CriticalTemperature
            app.CriticalTemperature = uieditfield(app.IsobargivenPressureonaTVDiagramUIFigure, 'text');
            app.CriticalTemperature.Editable = 'off';
            app.CriticalTemperature.Position = [1042 375 98 22];

            % Create CalculatedPressurebarLabel_2
            app.CalculatedPressurebarLabel_2 = uilabel(app.IsobargivenPressureonaTVDiagramUIFigure);
            app.CalculatedPressurebarLabel_2.HorizontalAlignment = 'right';
            app.CalculatedPressurebarLabel_2.FontWeight = 'bold';
            app.CalculatedPressurebarLabel_2.FontColor = [0.1412 0.302 0.4784];
            app.CalculatedPressurebarLabel_2.Position = [874 347 151 22];
            app.CalculatedPressurebarLabel_2.Text = 'Calculated Pressure [bar]';

            % Create CriticalPressure
            app.CriticalPressure = uieditfield(app.IsobargivenPressureonaTVDiagramUIFigure, 'text');
            app.CriticalPressure.Editable = 'off';
            app.CriticalPressure.Position = [1042 347 98 22];

            % Show the figure after all components are created
            app.IsobargivenPressureonaTVDiagramUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Volume5

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.IsobargivenPressureonaTVDiagramUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.IsobargivenPressureonaTVDiagramUIFigure)
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
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
b=omega*R*Tc/Pc;
Er=0.00001;
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
app.TriplePressure.Value=string(Pbracket(1));
app.CriticalPressure.Value=string(Pbracket(2));
% Find Tsat, Zliquid, Zvapor, Vliquid, and Vvapor given P
% Fugacity test method
% Case not thermodynamically possible: Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number)
Vfug=zeros(1,2);
Tfug=zeros(1,2);
Vant=zeros(1,2);
Tant=zeros(1,2);
Vexp=zeros(1,2);
Texp=zeros(1,2);
T=[];
V=[];
TPeg=[];
PPeg=[];
itePeg=[];
if Pi<Pbracket(1) || Pi>Pbracket(2)
    checkNaN=true;
else 
    checkNaN=false;
    Pstart=Pbracket(1)-Pi;
    Pfinal=Pbracket(2)-Pi;
    Tstart=Tbracket(1);
    Tfinal=Tbracket(2);
    ite=0;
    % Pegasus method
    while abs(Pfinal)>Er && abs(Pstart)>Er && abs(Tstart-Tfinal)>Er
        ite=ite+1;
        itePeg(ite)=ite;
        Ti=Tfinal-(Tfinal-Tstart)*Pfinal/(Pfinal-Pstart);
        TPeg(ite)=Ti;
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
        PPeg(ite)=Paux;
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
    Vfug(1)=Vliquid/1000/MM;
    Vfug(2)=Vvapor/1000/MM;
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
        Tfunction=@(T) ((Pi+psi*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    elseif eos==2
        Tfunction=@(T) ((Pi+psi*(T/Tc)^(-1/2)*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    elseif eos==3
        Tfunction=@(T) ((Pi+psi*(1+(0.480+1.574*w-0.176*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    else
        Tfunction=@(T) ((Pi+psi*(1+(0.37464+1.54226*w-0.26992*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    end
    T(1)=fsolve(Tfunction,Ti,options);
    V(1)=Vstart/1000/MM;
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
        V(j)=Vnext/1000/MM;
        Vnext=Vnext+step;
        j=j+1;
    end
    % Save data to graph the loop of the EoS: Saturated Liquid-Vapor
    jl=j-1;
    T(j)=Ti;
    V(j)=Vfug(1);
    j=j+1;
    T(j)=Ti;
    V(j)=Vfug(2);
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
        V(j)=Vnext/1000/MM;
        Vnext=Vnext+step;
        j=j+1;
    end
end
% Find Tsat using Antoine Equation
Tant(1)=-B/(log(Pi/0.01)-A)-C;
Tant(2)=Tant(1);
Tr=Tant(1)/Tc;
if eos==2
    alpha=Tr^(-1/2);
elseif eos==3
    alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
elseif eos==4
    alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
end
a=psi*alpha*(R*Tc)^2/Pc;
liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Tant(1)+Pi*(b-V))/a)-V;
Vant(1)=fsolve(liquid,b,options)/1000/MM;
vapor=@(V) (R*Tant(2)/Pi+b-a/Pi*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
Vant(2)=fsolve(vapor,R*Tant(2)/Pi,options)/1000/MM;
% Find Tsat, Vliquid, and Vvapor using the experimental data matrix
Texp(1)=table2array(data2(Pindex,1));
Texp(2)=table2array(data2(Pindex,1));
Vexp(1)=table2array(data2(Pindex,3));
Vexp(2)=table2array(data2(Pindex,4));
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
% Figure 1: Isobar given Pressure on a TV Diagram
hold(app.Figure1,"on");
if checkNaN==false
    plot(app.Figure1,Vfug,Tfug,"Marker","*","LineStyle","none","Color","b");
end
plot(app.Figure1,Vant,Tant,"Marker","^","LineStyle","none","Color","r");
plot(app.Figure1,Vexp,Texp,"Marker","o","LineStyle","none","Color",[0.1 0.5 0.1]);
if checkNaN==false
    plot(app.Figure1,V,T,"Color",[0.5 0 0.5]);
end
if checkNaN==true
    Vmin=min([Vant(1) Vexp(1)]);
    Vmax=max([Vant(2) Vexp(2)]);
    Tmin=min([Tant(1) Texp(1)]);
    Tmax=max([Tant(1) Texp(1)]);
else
    Vmin=min([min(V) Vfug(1) Vant(1) Vexp(1)]);
    Vmax=max([max(V) Vfug(2) Vant(2) Vexp(2)]);
    Tmin=min([Tfug(1) Tant(1) Texp(1)]);
    Tmax=max([Tfug(1) Tant(1) Texp(1)]);
end
axis(app.Figure1,[max([0 Vmin-0.1/MM]) Vmax+0.1/MM Tmin-10 Tmax+10]);
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
if checkNaN==false
    % Figure 2: Saturation Pressure vs Saturation Temperature
    hold(app.Figure2,"on");
    plot(app.Figure2,Tbracket(1),Pbracket(1),"Marker","*","Color","b","LineStyle","none");
    plot(app.Figure2,Tbracket(2),Pbracket(2),"Marker","*","Color","r","LineStyle","none");
    plot(app.Figure2,TPeg,PPeg,"Marker","*","Color",[0.1 0.5 0.1],"LineStyle","none");
    plot(app.Figure2,TPeg(ite),PPeg(ite),"Marker","*","Color",[0.5 0 0.5],"LineStyle","none");
    axis(app.Figure2,[Tbracket(1)-10 Tbracket(2)+10 Pbracket(1)-10 Pbracket(2)+10]);
    leg=legend(app.Figure2,{'Triple','Close to Critical','Intermediate','Final Result'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1);
    title(leg,"Calculated Points");
    hold(app.Figure2,"off");
    % Figure 3: Saturation Temperature vs Iteration Number
    plot(app.Figure3,itePeg,TPeg,"Marker","*","Color","b");
    axis(app.Figure3,[1 ite Tbracket(1)-10 Tbracket(2)+10]);
end
phase=strings;
Tp=strings;
Zp=strings;
Vp=strings;
k=1;
if checkNaN==true
    % Report results 1: Isobar given Pressure on a TV Diagram
    % Saturated Liquid-Vapor
    phase(k)="Satured Liquid (Fugacity Test)";
    Tp(k)="NaN";
    Zp(k)="NaN";
    Vp(k)="NaN";
    k=k+1;
    phase(k)="Satured Vapor (Fugacity Test)";
    Tp(k)="NaN";
    Zp(k)="NaN";
    Vp(k)="NaN";
    k=k+1;
else
    % Report results 2 and 3: Pegasus Method
    app.Table2.Data=[string(itePeg);string(TPeg);string(PPeg)]';
    % Report results 1: Isobar given Pressure on a TV Diagram
    % Liquid
    step=max([floor(jl/100) 1]);
    j=1;
    while j<=jl
        phase(k)="Liquid";
        Tp(k)=string(T(j));
        Zp(k)=string(Pi*V(j)*1000*MM/(R*T(j)));
        Vp(k)=string(V(j));
        j=j+step;
        k=k+1;
    end
    % Saturated Liquid-Vapor
    phase(k)="Satured Liquid (Fugacity Test)";
    Tp(k)=string(Ti);
    Zp(k)=string(Pi*Vfug(1)*1000*MM/(R*Tfug(1)));
    Vp(k)=string(Vfug(1));
    k=k+1;
    phase(k)="Satured Vapor (Fugacity Test)";
    Tp(k)=string(Ti);
    Zp(k)=string(Pi*Vfug(2)*1000*MM/(R*Tfug(2)));
    Vp(k)=string(Vfug(2));
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
Zp(k)=string(Pi*Vant(1)*1000*MM/(R*Tant(1)));
Vp(k)=string(Vant(1));
k=k+1;
if Tant(1)<Tt
    phase(k)="*Satured Vapor (Antoine Equation)";
elseif Tant(1)>Tc
    phase(k)="**Satured Vapor (Antoine Equation)";
else
    phase(k)="Satured Vapor (Antoine Equation)";
end
Tp(k)=string(Tant(1));
Zp(k)=string(Pi*Vant(2)*1000*MM/(R*Tant(2)));
Vp(k)=string(Vant(2));
k=k+1;
% Experimental data
if ~isnan(Texp(1))
    Tex=string(Texp(1));
else
    Tex="NA";
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
phase(k)="Satured Liquid (Experimental Data)";
Tp(k)=Tex;
Zp(k)=Zexl;
Vp(k)=Vexl;
k=k+1;
phase(k)="Satured Vapor (Experimental Data)";
Tp(k)=Tex;
Zp(k)=Zexv;
Vp(k)=Vexv;
k=k+1;
if checkNaN==false
    % Vapor
    step=max([floor((length(T)-jl-2)/100) 1]);
    j=jl+3;
    while j<=length(T)
        phase(k)="Vapor";
        Tp(k)=string(T(j));
        Zp(k)=string(Pi*V(j)*1000*MM/(R*T(j)));
        Vp(k)=string(V(j));
        j=j+step;
        k=k+1;
    end
end
app.Table1.Data=[phase;Tp;Zp;Vp]';
% Notify if the case is thermodynamically not possible
% Test Fugacity
if checkNaN==true
    uialert(app.IsobargivenPressureonaTVDiagramUIFigure,"Test Fugacity: Thermodynamically not possible case because Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number).","Error","Icon","error");
end
```