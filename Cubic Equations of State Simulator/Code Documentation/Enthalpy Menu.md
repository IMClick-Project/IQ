# Enthalpy Menu

The "Enthalpy" button on the main menu opens this menu of options for enthalpy-related thermodynamic property prediction functions. This menu is the MATLAB App file called "Enthalpy.mlapp".

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/enthalpy.jpg" width="721" height="279">

*Figure 1. Design View in Enthalpy.mlapp.*

### 1.2. Code View

```Matlab
classdef Enthalpy < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        EnthalpyUIFigure     matlab.ui.Figure
        PHTDiagramgivenIsobarPressuresButton  matlab.ui.control.Button
        TwoPhaseEnvelopeonaTHDiagramButton  matlab.ui.control.Button
        IsobargivenPressureonaTHDiagramButton  matlab.ui.control.Button
        BackButton           matlab.ui.control.Button
        ChooseanoptionLabel  matlab.ui.control.Label
        PHTDiagramgivenIsothermTemperaturesButton  matlab.ui.control.Button
        TwoPhaseEnvelopeonaPHDiagramButton  matlab.ui.control.Button
        IsothermgivenTemperatureonaPHDiagramButton  matlab.ui.control.Button
        Image                matlab.ui.control.Image
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.EnthalpyUIFigure,'center');
        end

        % Button pushed function: BackButton
        function BackButtonPushed(app, event)
            EoS_Simulator;
            delete(app);
        end

        % Button pushed function: 
        % IsothermgivenTemperatureonaPHDiagramButton
        function IsothermgivenTemperatureonaPHDiagramButtonPushed(app, event)
            Enthalpy1;
            delete(app);
        end

        % Button pushed function: TwoPhaseEnvelopeonaPHDiagramButton
        function TwoPhaseEnvelopeonaPHDiagramButtonPushed(app, event)
            Enthalpy2;
            delete(app);
        end

        % Button pushed function: PHTDiagramgivenIsothermTemperaturesButton
        function PHTDiagramgivenIsothermTemperaturesButtonPushed(app, event)
            Enthalpy3;
            delete(app);
        end

        % Button pushed function: IsobargivenPressureonaTHDiagramButton
        function IsobargivenPressureonaTHDiagramButtonPushed(app, event)
            Enthalpy4;
            delete(app);
        end

        % Button pushed function: TwoPhaseEnvelopeonaTHDiagramButton
        function TwoPhaseEnvelopeonaTHDiagramButtonPushed(app, event)
            Enthalpy5;
            delete(app);
        end

        % Button pushed function: PHTDiagramgivenIsobarPressuresButton
        function PHTDiagramgivenIsobarPressuresButtonPushed(app, event)
            Enthalpy6;
            delete(app);
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create EnthalpyUIFigure and hide until all components are created
            app.EnthalpyUIFigure = uifigure('Visible', 'off');
            app.EnthalpyUIFigure.Color = [1 1 1];
            app.EnthalpyUIFigure.Position = [475 325 720 278];
            app.EnthalpyUIFigure.Name = 'Enthalpy';
            app.EnthalpyUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.EnthalpyUIFigure.Resize = 'off';

            % Create Image
            app.Image = uiimage(app.EnthalpyUIFigure);
            app.Image.Position = [512 55 198 162];
            app.Image.ImageSource = 'Logo.PNG';

            % Create IsothermgivenTemperatureonaPHDiagramButton
            app.IsothermgivenTemperatureonaPHDiagramButton = uibutton(app.EnthalpyUIFigure, 'push');
            app.IsothermgivenTemperatureonaPHDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @IsothermgivenTemperatureonaPHDiagramButtonPushed, true);
            app.IsothermgivenTemperatureonaPHDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.IsothermgivenTemperatureonaPHDiagramButton.FontWeight = 'bold';
            app.IsothermgivenTemperatureonaPHDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.IsothermgivenTemperatureonaPHDiagramButton.Position = [15 212 482 22];
            app.IsothermgivenTemperatureonaPHDiagramButton.Text = 'Isotherm given Temperature on a PH Diagram';

            % Create TwoPhaseEnvelopeonaPHDiagramButton
            app.TwoPhaseEnvelopeonaPHDiagramButton = uibutton(app.EnthalpyUIFigure, 'push');
            app.TwoPhaseEnvelopeonaPHDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @TwoPhaseEnvelopeonaPHDiagramButtonPushed, true);
            app.TwoPhaseEnvelopeonaPHDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.TwoPhaseEnvelopeonaPHDiagramButton.FontWeight = 'bold';
            app.TwoPhaseEnvelopeonaPHDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.TwoPhaseEnvelopeonaPHDiagramButton.Position = [15 181 482 22];
            app.TwoPhaseEnvelopeonaPHDiagramButton.Text = 'Two-Phase Envelope on a PH Diagram';

            % Create PHTDiagramgivenIsothermTemperaturesButton
            app.PHTDiagramgivenIsothermTemperaturesButton = uibutton(app.EnthalpyUIFigure, 'push');
            app.PHTDiagramgivenIsothermTemperaturesButton.ButtonPushedFcn = createCallbackFcn(app, @PHTDiagramgivenIsothermTemperaturesButtonPushed, true);
            app.PHTDiagramgivenIsothermTemperaturesButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.PHTDiagramgivenIsothermTemperaturesButton.FontWeight = 'bold';
            app.PHTDiagramgivenIsothermTemperaturesButton.FontColor = [0.1373 0.298 0.4784];
            app.PHTDiagramgivenIsothermTemperaturesButton.Position = [15 150 482 22];
            app.PHTDiagramgivenIsothermTemperaturesButton.Text = 'PHT Diagram given Isotherm Temperatures';

            % Create ChooseanoptionLabel
            app.ChooseanoptionLabel = uilabel(app.EnthalpyUIFigure);
            app.ChooseanoptionLabel.HorizontalAlignment = 'center';
            app.ChooseanoptionLabel.FontWeight = 'bold';
            app.ChooseanoptionLabel.FontColor = [0.1373 0.298 0.4784];
            app.ChooseanoptionLabel.Position = [204 241 107 22];
            app.ChooseanoptionLabel.Text = 'Choose an option';

            % Create BackButton
            app.BackButton = uibutton(app.EnthalpyUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1373 0.298 0.4784];
            app.BackButton.Position = [18 23 479 22];
            app.BackButton.Text = 'Back';

            % Create IsobargivenPressureonaTHDiagramButton
            app.IsobargivenPressureonaTHDiagramButton = uibutton(app.EnthalpyUIFigure, 'push');
            app.IsobargivenPressureonaTHDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @IsobargivenPressureonaTHDiagramButtonPushed, true);
            app.IsobargivenPressureonaTHDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.IsobargivenPressureonaTHDiagramButton.FontWeight = 'bold';
            app.IsobargivenPressureonaTHDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.IsobargivenPressureonaTHDiagramButton.Position = [16 118 481 22];
            app.IsobargivenPressureonaTHDiagramButton.Text = 'Isobar given Pressure on a TH Diagram';

            % Create TwoPhaseEnvelopeonaTHDiagramButton
            app.TwoPhaseEnvelopeonaTHDiagramButton = uibutton(app.EnthalpyUIFigure, 'push');
            app.TwoPhaseEnvelopeonaTHDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @TwoPhaseEnvelopeonaTHDiagramButtonPushed, true);
            app.TwoPhaseEnvelopeonaTHDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.TwoPhaseEnvelopeonaTHDiagramButton.FontWeight = 'bold';
            app.TwoPhaseEnvelopeonaTHDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.TwoPhaseEnvelopeonaTHDiagramButton.Position = [17 87 480 22];
            app.TwoPhaseEnvelopeonaTHDiagramButton.Text = 'Two-Phase Envelope on a TH Diagram';

            % Create PHTDiagramgivenIsobarPressuresButton
            app.PHTDiagramgivenIsobarPressuresButton = uibutton(app.EnthalpyUIFigure, 'push');
            app.PHTDiagramgivenIsobarPressuresButton.ButtonPushedFcn = createCallbackFcn(app, @PHTDiagramgivenIsobarPressuresButtonPushed, true);
            app.PHTDiagramgivenIsobarPressuresButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.PHTDiagramgivenIsobarPressuresButton.FontWeight = 'bold';
            app.PHTDiagramgivenIsobarPressuresButton.FontColor = [0.1373 0.298 0.4784];
            app.PHTDiagramgivenIsobarPressuresButton.Position = [17 55 480 22];
            app.PHTDiagramgivenIsobarPressuresButton.Text = 'PHT Diagram given Isobar Pressures';

            % Show the figure after all components are created
            app.EnthalpyUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Enthalpy

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.EnthalpyUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.EnthalpyUIFigure)
        end
    end
end
```
