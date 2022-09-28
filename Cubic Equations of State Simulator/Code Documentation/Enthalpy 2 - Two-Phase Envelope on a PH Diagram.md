# Two-Phase Envelope on a PH Diagram

This is the second option in the enthalpy menu. Its interface is programmed in "Enthalpy2.mlapp" and it uses the function called "Two_Phase_PH_Diagram.m" for thermodynamic calculations.

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/enthalpy2.jpg" width="724" height="534">

*Figure 1. Design View in Enthalpy2.mlapp.*

### 1.2. Code View

```Matlab
classdef Enthalpy2 < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        TwoPhaseEnvelopeonaPHDiagramUIFigure  matlab.ui.Figure
        ReferenceEnthalpy            matlab.ui.control.EditField
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
        TwoPhaseEnvelopeonaPHDiagramLabel  matlab.ui.control.Label
        Image                        matlab.ui.control.Image
        CalculateButton              matlab.ui.control.Button
        CriticalEnthalpy             matlab.ui.control.EditField
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
            movegui(app.TwoPhaseEnvelopeonaPHDiagramUIFigure,"north");
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
            if tam>0 && app.ReferenceState.Value~="NaN" && app.ReferenceTemperature.Value~="NaN" && app.ReferencePressure.Value~="NaN" && app.ReferenceEnthalpy.Value~="NaN"
                progressbar=uiprogressdlg(app.TwoPhaseEnvelopeonaPHDiagramUIFigure,"Title","Status","Message","Calculating","Indeterminate","on","Cancelable","off");
                drawnow;
                Two_Phase_PH_Diagram;
                app.ExportButton.Visible="on";
                close(progressbar);
            elseif app.ReferenceState.Value=="NaN" || app.ReferenceTemperature.Value=="NaN" || app.ReferencePressure.Value=="NaN" || app.ReferenceEnthalpy.Value=="NaN"
                uialert(app.TwoPhaseEnvelopeonaPHDiagramUIFigure,"Incomplete Data.","Data Status","Icon","warning");
            else
                uialert(app.TwoPhaseEnvelopeonaPHDiagramUIFigure,"Input isotherm temperatures not found.","Data Status","Icon","warning");
            end
        end

        % Button pushed function: BackButton
        function BackButtonPushed(app, event)
            Enthalpy;
            delete(app);
        end

        % Button pushed function: ExportButton
        function ExportButtonPushed(app, event)
            progressbar=uiprogressdlg(app.TwoPhaseEnvelopeonaPHDiagramUIFigure,"Title","Status","Message","Exporting","Indeterminate","on","Cancelable","off");
            drawnow;
            aux=app.Table1.Data;
            table1=table(aux(:,1),str2double(aux(:,2)),str2double(aux(:,3)),str2double(aux(:,4)),str2double(aux(:,5)),str2double(aux(:,6)),str2double(aux(:,7)));
            table1.Properties.VariableNames{'Var1'}='Method';
            table1.Properties.VariableNames{'Var2'}='Tsat [K]';
            table1.Properties.VariableNames{'Var3'}='Psat [bar]';
            table1.Properties.VariableNames{'Var4'}='Zliquid';
            table1.Properties.VariableNames{'Var5'}='Zvapor';
            table1.Properties.VariableNames{'Var6'}='Hliquid [kJ/kg]';
            table1.Properties.VariableNames{'Var7'}='Hvapor [kJ/kg]';
            writecell(cell(5000,7),"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","A1");
            writetable(table1,"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","A9");
            writecell({'Compound'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","A1");
            writecell({'Cubic Equation of State'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","A2");
            writecell({'Reference State'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","A3");
            writecell({'Reference Temperature [K]'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","A4");
            writecell({'Reference Pressure [bar]'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","A5");
            writecell({'Reference Enthalpy [kJ/kg]'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","A6");
            writecell({'Critical Pressure [bar]'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","A7");
            writecell({'Calculated Critical Enthalpy [kJ/kg]'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","A8");
            writecell({app.Compound.Value},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","B1");
            writecell({app.EoS.Value},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","B2");
            writecell({app.ReferenceState.Value},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","B3");
            writematrix(str2double({app.ReferenceTemperature.Value}),"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","B4");
            writematrix(str2double({app.ReferencePressure.Value}),"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","B5");
            writematrix(str2double({app.ReferenceEnthalpy.Value}),"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","B6");
            writematrix(str2double({app.CriticalPressure.Value}),"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","B7");
            writematrix(str2double({app.CriticalEnthalpy.Value}),"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range","B8");
            for i=12:3:5+height(table1)
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range",[i,3,i,3])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range",['C',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range",[i,4,i,4])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range",['D',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range",[i,5,i,5])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range",['E',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range",[i,6,i,6])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range",['F',num2str(i)]);
                end
                if ismissing(string(readcell("./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range",[i,7,i,7])))
                    writecell({'NA'},"./Results/Two-Phase Envelope on a PH Diagram.xlsx","Sheet","PH Diagram","Range",['G',num2str(i)]);
                end
            end
            close(progressbar);
            uialert(app.TwoPhaseEnvelopeonaPHDiagramUIFigure,"Finished Export.","Export Status","Icon","success");
        end

        % Value changed function: Compound
        function CompoundValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound");
            app.CriticalPressure.Value="";
            app.CriticalEnthalpy.Value="";
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
            cla(app.Figure1);
            app.Table1.Data={};
        end

        % Value changed function: EoS
        function EoSValueChanged(app, event)
            clc;
            app.ExportButton.Visible="off";
            title(app.Figure1,"EoS - Compound");
            app.CriticalPressure.Value="";
            app.CriticalEnthalpy.Value="";
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

            % Create TwoPhaseEnvelopeonaPHDiagramUIFigure and hide until all components are created
            app.TwoPhaseEnvelopeonaPHDiagramUIFigure = uifigure('Visible', 'off');
            app.TwoPhaseEnvelopeonaPHDiagramUIFigure.Color = [1 1 1];
            app.TwoPhaseEnvelopeonaPHDiagramUIFigure.Position = [100 100 902 667];
            app.TwoPhaseEnvelopeonaPHDiagramUIFigure.Name = 'Two-Phase Envelope on a PH Diagram';
            app.TwoPhaseEnvelopeonaPHDiagramUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.TwoPhaseEnvelopeonaPHDiagramUIFigure.Resize = 'off';

            % Create Figure1
            app.Figure1 = uiaxes(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            title(app.Figure1, 'EoS - Compound')
            xlabel(app.Figure1, 'H [kJ/kg]')
            ylabel(app.Figure1, 'P_{sat} [bar]')
            zlabel(app.Figure1, 'Z')
            app.Figure1.XGrid = 'on';
            app.Figure1.XMinorGrid = 'on';
            app.Figure1.YGrid = 'on';
            app.Figure1.Position = [73 91 479 386];

            % Create Table1
            app.Table1 = uitable(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.Table1.ColumnName = {'Method'; 'Tsat [K]'; 'Psat [bar]'; 'Zliquid'; 'Zvapor'; 'Hliquid [kJ/kg]'; 'Hvapor [kJ/kg]'};
            app.Table1.RowName = {};
            app.Table1.Position = [571 191 249 257];

            % Create Label
            app.Label = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.Label.FontWeight = 'bold';
            app.Label.FontColor = [0.1412 0.302 0.4784];
            app.Label.Position = [43 26 584 56];
            app.Label.Text = {'Symbology'; 'NA: Not Available.'; '*: Thermodynamically not possible case because the pressure is less than the triple pressure.'; '**: Thermodynamically not possible case because the pressure is greater than the critical pressure.'};

            % Create Label_2
            app.Label_2 = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.Label_2.HorizontalAlignment = 'center';
            app.Label_2.FontWeight = 'bold';
            app.Label_2.FontColor = [0.1412 0.302 0.4784];
            app.Label_2.Position = [661 157 144 22];
            app.Label_2.Text = 'Calculated Critical Point';

            % Create ExportButton
            app.ExportButton = uibutton(app.TwoPhaseEnvelopeonaPHDiagramUIFigure, 'push');
            app.ExportButton.ButtonPushedFcn = createCallbackFcn(app, @ExportButtonPushed, true);
            app.ExportButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.ExportButton.FontWeight = 'bold';
            app.ExportButton.FontColor = [0.1412 0.302 0.4784];
            app.ExportButton.Visible = 'off';
            app.ExportButton.Position = [770 50 100 22];
            app.ExportButton.Text = 'Export';

            % Create BackButton
            app.BackButton = uibutton(app.TwoPhaseEnvelopeonaPHDiagramUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1412 0.302 0.4784];
            app.BackButton.Position = [770 19 100 22];
            app.BackButton.Text = 'Back';

            % Create PressurebarEditFieldLabel
            app.PressurebarEditFieldLabel = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.PressurebarEditFieldLabel.HorizontalAlignment = 'right';
            app.PressurebarEditFieldLabel.FontWeight = 'bold';
            app.PressurebarEditFieldLabel.FontColor = [0.1412 0.302 0.4784];
            app.PressurebarEditFieldLabel.Position = [571 125 103 22];
            app.PressurebarEditFieldLabel.Text = 'Pressure [bar]';

            % Create CriticalPressure
            app.CriticalPressure = uieditfield(app.TwoPhaseEnvelopeonaPHDiagramUIFigure, 'text');
            app.CriticalPressure.Editable = 'off';
            app.CriticalPressure.Position = [691 125 176 22];

            % Create Enthlalpym3kgLabel
            app.Enthlalpym3kgLabel = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.Enthlalpym3kgLabel.HorizontalAlignment = 'right';
            app.Enthlalpym3kgLabel.FontWeight = 'bold';
            app.Enthlalpym3kgLabel.FontColor = [0.1412 0.302 0.4784];
            app.Enthlalpym3kgLabel.Position = [576 91 98 22];
            app.Enthlalpym3kgLabel.Text = 'Enthalpy [kJ/kg]';

            % Create CriticalEnthalpy
            app.CriticalEnthalpy = uieditfield(app.TwoPhaseEnvelopeonaPHDiagramUIFigure, 'text');
            app.CriticalEnthalpy.Editable = 'off';
            app.CriticalEnthalpy.Position = [691 91 176 22];

            % Create CalculateButton
            app.CalculateButton = uibutton(app.TwoPhaseEnvelopeonaPHDiagramUIFigure, 'push');
            app.CalculateButton.ButtonPushedFcn = createCallbackFcn(app, @CalculateButtonPushed, true);
            app.CalculateButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.CalculateButton.FontWeight = 'bold';
            app.CalculateButton.FontColor = [0.1412 0.302 0.4784];
            app.CalculateButton.Position = [764 469 103 22];
            app.CalculateButton.Text = 'Calculate';

            % Create Image
            app.Image = uiimage(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.Image.Position = [25 506 116 101];
            app.Image.ImageSource = fullfile(pathToMLAPP, 'Logoico.png');

            % Create TwoPhaseEnvelopeonaPHDiagramLabel
            app.TwoPhaseEnvelopeonaPHDiagramLabel = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.TwoPhaseEnvelopeonaPHDiagramLabel.HorizontalAlignment = 'center';
            app.TwoPhaseEnvelopeonaPHDiagramLabel.FontSize = 20;
            app.TwoPhaseEnvelopeonaPHDiagramLabel.FontWeight = 'bold';
            app.TwoPhaseEnvelopeonaPHDiagramLabel.FontColor = [0.1412 0.302 0.4784];
            app.TwoPhaseEnvelopeonaPHDiagramLabel.Position = [1 628 907 26];
            app.TwoPhaseEnvelopeonaPHDiagramLabel.Text = 'Two-Phase Envelope on a PH Diagram';

            % Create Label_3
            app.Label_3 = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.Label_3.HorizontalAlignment = 'center';
            app.Label_3.FontWeight = 'bold';
            app.Label_3.FontColor = [0.1412 0.302 0.4784];
            app.Label_3.Position = [672 599 93 22];
            app.Label_3.Text = 'Reference Data';

            % Create CubicEquationofStateDropDownLabel
            app.CubicEquationofStateDropDownLabel = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.CubicEquationofStateDropDownLabel.HorizontalAlignment = 'right';
            app.CubicEquationofStateDropDownLabel.FontWeight = 'bold';
            app.CubicEquationofStateDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CubicEquationofStateDropDownLabel.Position = [165 521 141 22];
            app.CubicEquationofStateDropDownLabel.Text = 'Cubic Equation of State';

            % Create EoS
            app.EoS = uidropdown(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.EoS.Items = {'van der Waals', 'Redlich-Kwong', 'Soave-Redlich-Kwong', 'Peng-Robinson'};
            app.EoS.ValueChangedFcn = createCallbackFcn(app, @EoSValueChanged, true);
            app.EoS.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EoS.Position = [322 521 220 22];
            app.EoS.Value = 'van der Waals';

            % Create CompoundDropDownLabel
            app.CompoundDropDownLabel = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.CompoundDropDownLabel.HorizontalAlignment = 'right';
            app.CompoundDropDownLabel.FontWeight = 'bold';
            app.CompoundDropDownLabel.FontColor = [0.1412 0.302 0.4784];
            app.CompoundDropDownLabel.Position = [168 560 140 22];
            app.CompoundDropDownLabel.Text = 'Compound';

            % Create Compound
            app.Compound = uidropdown(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.Compound.Items = {};
            app.Compound.ValueChangedFcn = createCallbackFcn(app, @CompoundValueChanged, true);
            app.Compound.BackgroundColor = [0.8588 0.9608 0.9608];
            app.Compound.Position = [323 560 220 22];
            app.Compound.Value = {};

            % Create StateLabel
            app.StateLabel = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.StateLabel.HorizontalAlignment = 'right';
            app.StateLabel.FontWeight = 'bold';
            app.StateLabel.FontColor = [0.1412 0.302 0.4784];
            app.StateLabel.Position = [571 577 103 22];
            app.StateLabel.Text = 'State';

            % Create ReferenceState
            app.ReferenceState = uieditfield(app.TwoPhaseEnvelopeonaPHDiagramUIFigure, 'text');
            app.ReferenceState.Editable = 'off';
            app.ReferenceState.Position = [691 577 176 22];

            % Create TemperatureKLabel
            app.TemperatureKLabel = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.TemperatureKLabel.HorizontalAlignment = 'right';
            app.TemperatureKLabel.FontWeight = 'bold';
            app.TemperatureKLabel.FontColor = [0.1412 0.302 0.4784];
            app.TemperatureKLabel.Position = [571 551 103 22];
            app.TemperatureKLabel.Text = 'Temperature [K]';

            % Create ReferenceTemperature
            app.ReferenceTemperature = uieditfield(app.TwoPhaseEnvelopeonaPHDiagramUIFigure, 'text');
            app.ReferenceTemperature.Editable = 'off';
            app.ReferenceTemperature.Position = [691 551 176 22];

            % Create PressurebarEditFieldLabel_2
            app.PressurebarEditFieldLabel_2 = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.PressurebarEditFieldLabel_2.HorizontalAlignment = 'right';
            app.PressurebarEditFieldLabel_2.FontWeight = 'bold';
            app.PressurebarEditFieldLabel_2.FontColor = [0.1412 0.302 0.4784];
            app.PressurebarEditFieldLabel_2.Position = [571 526 103 22];
            app.PressurebarEditFieldLabel_2.Text = 'Pressure [bar]';

            % Create ReferencePressure
            app.ReferencePressure = uieditfield(app.TwoPhaseEnvelopeonaPHDiagramUIFigure, 'text');
            app.ReferencePressure.Editable = 'off';
            app.ReferencePressure.Position = [691 526 176 22];

            % Create EnthalpykJkgLabel
            app.EnthalpykJkgLabel = uilabel(app.TwoPhaseEnvelopeonaPHDiagramUIFigure);
            app.EnthalpykJkgLabel.HorizontalAlignment = 'right';
            app.EnthalpykJkgLabel.FontWeight = 'bold';
            app.EnthalpykJkgLabel.FontColor = [0.1412 0.302 0.4784];
            app.EnthalpykJkgLabel.Position = [571 500 103 22];
            app.EnthalpykJkgLabel.Text = 'Enthalpy [kJ/kg]';

            % Create ReferenceEnthalpy
            app.ReferenceEnthalpy = uieditfield(app.TwoPhaseEnvelopeonaPHDiagramUIFigure, 'text');
            app.ReferenceEnthalpy.Editable = 'off';
            app.ReferenceEnthalpy.Position = [691 500 176 22];

            % Show the figure after all components are created
            app.TwoPhaseEnvelopeonaPHDiagramUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Enthalpy2

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.TwoPhaseEnvelopeonaPHDiagramUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.TwoPhaseEnvelopeonaPHDiagramUIFigure)
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
sizefug=1;
sizeant=1;
Hfug=[];
Pfug=[];
Hant=[];
Pant=[];
Hexp=zeros(1,2*tam);
Vexp=zeros(1,2*tam);
Pexp=zeros(1,2*tam);
method=strings(1,3*tam);
T=strings(1,3*tam);
P=strings(1,3*tam);
Hl=strings(1,3*tam);
Hv=strings(1,3*tam);
Zl=strings(1,3*tam);
Zv=strings(1,3*tam);
% For each T in the compound database: Find Psat, Zliquid, Zvapor, Hliquid, and Hvapor
for i=1:tam
    Ti=str2double(aux(i));
    Integralcp=Acp*(Ti-T0)+Bcp*(Ti^2-T0^2)/2+Ccp*(Ti^3-T0^3)/3+Dcp*(Ti^4-T0^4)/4+Ecp*(Ti^5-T0^5)/5; % [kJ/kmol]
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
    HR=R2*Ti*(Zliquid-1+(derivate-1)*q*I);
    Hfugl=(-HR0+HR+H0+Integralcp)/MM;
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Ti*(Zvapor-1+(derivate-1)*q*I);
    Hfugv=(-HR0+HR+H0+Integralcp)/MM;
    % Test Fugacity: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pfug(sizefug)=Paux;
        Hfug(sizefug)=Hfugl;
        sizefug=sizefug+1;
        Pfug(sizefug)=Paux;
        Hfug(sizefug)=Hfugv;
        sizefug=sizefug+1;
    end
    P(ft)=string(Paux);
    Hl(ft)=string(Hfugl);
    Hv(ft)=string(Hfugv);
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
    HR=R2*Ti*(Zliquid-1+(derivate-1)*q*I);
    Hantl=(-HR0+HR+H0+Integralcp)/MM;
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Ti*(Zvapor-1+(derivate-1)*q*I);
    Hantv=(-HR0+HR+H0+Integralcp)/MM;
    % Antoine Equation: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pant(sizeant)=Paux;
        Hant(sizeant)=Hantl;
        sizeant=sizeant+1;
        Pant(sizeant)=Paux;
        Hant(sizeant)=Hantv;
        sizeant=sizeant+1;
    end
    P(ae)=string(Paux);
    Hl(ae)=string(Hantl);
    Hv(ae)=string(Hantv);
    Zl(ae)=string(Zliquid);
    Zv(ae)=string(Zvapor);
    % Find Psat, Hliquid, and Hvapor using the experimental data matrix
    l=2*i-1;
    v=2*i;
    T(ed)=string(Ti);
    method(ed)="Experimental Data";
    data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
    Pexp(l)=table2array(data2(aux(i),1));
    Pexp(v)=table2array(data2(aux(i),1));
    Vexp(l)=table2array(data2(aux(i),2));
    Vexp(v)=table2array(data2(aux(i),3));
    Hexp(l)=table2array(data2(aux(i),4));
    Hexp(v)=table2array(data2(aux(i),5));
    if isnan(Pexp(l))
        P(ed)="NA";
    else
        P(ed)=string(Pexp(l));
    end
    if isnan(Hexp(l))
        Hl(ed)="NA";
    else
        Hl(ed)=string(Hexp(l));
    end
    if isnan(Hexp(v))
        Hv(ed)="NA";
    else
        Hv(ed)=string(Hexp(v));
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
Integralcp=Acp*(Tc-T0)+Bcp*(Tc^2-T0^2)/2+Ccp*(Tc^3-T0^3)/3+Dcp*(Tc^4-T0^4)/4+Ecp*(Tc^5-T0^5)/5;
Tr=1; % Tc/Tc
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
HR=R2*Tc*(Zc-1+(derivate-1)*q*I);
Hc=(-HR0+HR+H0+Integralcp)/MM;
Hexp(2*height(aux)+1)=Hc;
app.CriticalPressure.Value=string(Pc);
app.CriticalEnthalpy.Value=string(Hc);
% Figure: Two-Phase Envelope on a PH Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Hfug,Pfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Hant,Pant,"Marker","^","Linestyle","none","Color","r");
plot(app.Figure1,Hexp,Pexp,"Marker","o","Linestyle","none","Color",[0.1 0.5 0.1]);
Hmax=max([max(Hfug) max(Hant) max(Hexp)]);
Hmin=min([min(Hfug) min(Hant) min(Hexp)]);
Pmin=max([0 Pt-10]);
if Pmin==0
    Pmax=Pc+Pt;
else
    Pmax=Pt+10;
end
axis(app.Figure1,[Hmin-abs(Hmax-Hmin)*0.5 Hmax+abs(Hmax-Hmin)*0.5 Pmin Pmax]);
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
app.Table1.Data=[method;T;P;Zl;Zv;Hl;Hv]';
```