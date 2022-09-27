# Entropy Menu

The "Entropy" button on the main menu opens this menu of options for entropy-related thermodynamic property prediction functions. This menu is the MATLAB app file called "Entropy.mlapp".

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/entropy.jpg" width="722" height="282">

*Figure 1. Design View in Entropy.mlapp*

### 1.2. Code View

```Matlab
classdef Entropy < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        EntropyUIFigure      matlab.ui.Figure
        PSTDiagramgivenIsobarPressuresButton  matlab.ui.control.Button
        TwoPhaseEnvelopeonaTSDiagramButton  matlab.ui.control.Button
        IsobargivenPressureonaTSDiagramButton  matlab.ui.control.Button
        BackButton           matlab.ui.control.Button
        ChooseanoptionLabel  matlab.ui.control.Label
        PSTDiagramgivenIsothermTemperaturesButton  matlab.ui.control.Button
        TwoPhaseEnvelopeonaPSDiagramButton  matlab.ui.control.Button
        IsothermgivenTemperatureonaPSDiagramButton  matlab.ui.control.Button
        Image                matlab.ui.control.Image
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.EntropyUIFigure,'center');
        end

        % Button pushed function: BackButton
        function BackButtonPushed(app, event)
            EoS_Simulator;
            delete(app);
        end

        % Button pushed function: 
        % IsothermgivenTemperatureonaPSDiagramButton
        function IsothermgivenTemperatureonaPSDiagramButtonPushed(app, event)
            Entropy1;
            delete(app);
        end

        % Button pushed function: TwoPhaseEnvelopeonaPSDiagramButton
        function TwoPhaseEnvelopeonaPSDiagramButtonPushed(app, event)
            Entropy2;
            delete(app);
        end

        % Button pushed function: PSTDiagramgivenIsothermTemperaturesButton
        function PSTDiagramgivenIsothermTemperaturesButtonPushed(app, event)
            Entropy3;
            delete(app);
        end

        % Button pushed function: IsobargivenPressureonaTSDiagramButton
        function IsobargivenPressureonaTSDiagramButtonPushed(app, event)
            Entropy4;
            delete(app);
        end

        % Button pushed function: TwoPhaseEnvelopeonaTSDiagramButton
        function TwoPhaseEnvelopeonaTSDiagramButtonPushed(app, event)
            Entropy5;
            delete(app);
        end

        % Button pushed function: PSTDiagramgivenIsobarPressuresButton
        function PSTDiagramgivenIsobarPressuresButtonPushed(app, event)
            Entropy6;
            delete(app);
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create EntropyUIFigure and hide until all components are created
            app.EntropyUIFigure = uifigure('Visible', 'off');
            app.EntropyUIFigure.Color = [1 1 1];
            app.EntropyUIFigure.Position = [475 325 720 278];
            app.EntropyUIFigure.Name = 'Entropy';
            app.EntropyUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.EntropyUIFigure.Resize = 'off';

            % Create Image
            app.Image = uiimage(app.EntropyUIFigure);
            app.Image.Position = [513 54 198 162];
            app.Image.ImageSource = 'Logo.PNG';

            % Create IsothermgivenTemperatureonaPSDiagramButton
            app.IsothermgivenTemperatureonaPSDiagramButton = uibutton(app.EntropyUIFigure, 'push');
            app.IsothermgivenTemperatureonaPSDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @IsothermgivenTemperatureonaPSDiagramButtonPushed, true);
            app.IsothermgivenTemperatureonaPSDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.IsothermgivenTemperatureonaPSDiagramButton.FontWeight = 'bold';
            app.IsothermgivenTemperatureonaPSDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.IsothermgivenTemperatureonaPSDiagramButton.Position = [16 211 482 22];
            app.IsothermgivenTemperatureonaPSDiagramButton.Text = 'Isotherm given Temperature on a PS Diagram';

            % Create TwoPhaseEnvelopeonaPSDiagramButton
            app.TwoPhaseEnvelopeonaPSDiagramButton = uibutton(app.EntropyUIFigure, 'push');
            app.TwoPhaseEnvelopeonaPSDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @TwoPhaseEnvelopeonaPSDiagramButtonPushed, true);
            app.TwoPhaseEnvelopeonaPSDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.TwoPhaseEnvelopeonaPSDiagramButton.FontWeight = 'bold';
            app.TwoPhaseEnvelopeonaPSDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.TwoPhaseEnvelopeonaPSDiagramButton.Position = [16 180 482 22];
            app.TwoPhaseEnvelopeonaPSDiagramButton.Text = 'Two-Phase Envelope on a PS Diagram';

            % Create PSTDiagramgivenIsothermTemperaturesButton
            app.PSTDiagramgivenIsothermTemperaturesButton = uibutton(app.EntropyUIFigure, 'push');
            app.PSTDiagramgivenIsothermTemperaturesButton.ButtonPushedFcn = createCallbackFcn(app, @PSTDiagramgivenIsothermTemperaturesButtonPushed, true);
            app.PSTDiagramgivenIsothermTemperaturesButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.PSTDiagramgivenIsothermTemperaturesButton.FontWeight = 'bold';
            app.PSTDiagramgivenIsothermTemperaturesButton.FontColor = [0.1373 0.298 0.4784];
            app.PSTDiagramgivenIsothermTemperaturesButton.Position = [16 149 482 22];
            app.PSTDiagramgivenIsothermTemperaturesButton.Text = 'PST Diagram given Isotherm Temperatures';

            % Create ChooseanoptionLabel
            app.ChooseanoptionLabel = uilabel(app.EntropyUIFigure);
            app.ChooseanoptionLabel.HorizontalAlignment = 'center';
            app.ChooseanoptionLabel.FontWeight = 'bold';
            app.ChooseanoptionLabel.FontColor = [0.1373 0.298 0.4784];
            app.ChooseanoptionLabel.Position = [205 240 107 22];
            app.ChooseanoptionLabel.Text = 'Choose an option';

            % Create BackButton
            app.BackButton = uibutton(app.EntropyUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1373 0.298 0.4784];
            app.BackButton.Position = [19 22 479 22];
            app.BackButton.Text = 'Back';

            % Create IsobargivenPressureonaTSDiagramButton
            app.IsobargivenPressureonaTSDiagramButton = uibutton(app.EntropyUIFigure, 'push');
            app.IsobargivenPressureonaTSDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @IsobargivenPressureonaTSDiagramButtonPushed, true);
            app.IsobargivenPressureonaTSDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.IsobargivenPressureonaTSDiagramButton.FontWeight = 'bold';
            app.IsobargivenPressureonaTSDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.IsobargivenPressureonaTSDiagramButton.Position = [17 117 481 22];
            app.IsobargivenPressureonaTSDiagramButton.Text = 'Isobar given Pressure on a TS Diagram';

            % Create TwoPhaseEnvelopeonaTSDiagramButton
            app.TwoPhaseEnvelopeonaTSDiagramButton = uibutton(app.EntropyUIFigure, 'push');
            app.TwoPhaseEnvelopeonaTSDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @TwoPhaseEnvelopeonaTSDiagramButtonPushed, true);
            app.TwoPhaseEnvelopeonaTSDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.TwoPhaseEnvelopeonaTSDiagramButton.FontWeight = 'bold';
            app.TwoPhaseEnvelopeonaTSDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.TwoPhaseEnvelopeonaTSDiagramButton.Position = [18 86 480 22];
            app.TwoPhaseEnvelopeonaTSDiagramButton.Text = 'Two-Phase Envelope on a TS Diagram';

            % Create PSTDiagramgivenIsobarPressuresButton
            app.PSTDiagramgivenIsobarPressuresButton = uibutton(app.EntropyUIFigure, 'push');
            app.PSTDiagramgivenIsobarPressuresButton.ButtonPushedFcn = createCallbackFcn(app, @PSTDiagramgivenIsobarPressuresButtonPushed, true);
            app.PSTDiagramgivenIsobarPressuresButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.PSTDiagramgivenIsobarPressuresButton.FontWeight = 'bold';
            app.PSTDiagramgivenIsobarPressuresButton.FontColor = [0.1373 0.298 0.4784];
            app.PSTDiagramgivenIsobarPressuresButton.Position = [18 54 480 22];
            app.PSTDiagramgivenIsobarPressuresButton.Text = 'PST Diagram given Isobar Pressures';

            % Show the figure after all components are created
            app.EntropyUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Entropy

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.EntropyUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.EntropyUIFigure)
        end
    end
end
```
