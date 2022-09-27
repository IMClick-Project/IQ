# Volume Menu

The "Volume" button on the main menu opens this menu of options for volume-related thermodynamic property prediction functions. This menu is the MATLAB app file called "Volume.mlapp".

## 1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/volume.jpg" width="721" height="314">

*Figure 1. Design View in Volume.mlapp*

## 2. Code View

```Matlab
classdef Volume < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        VolumeUIFigure       matlab.ui.Figure
        PVTDiagramgivenIsobarPressuresButton  matlab.ui.control.Button
        TwoPhaseEnvelopeonaTVDiagramButton  matlab.ui.control.Button
        IsobargivenPressureonaTVDiagramButton  matlab.ui.control.Button
        PsatgivenTapplyingDifferentsBracketingMethods  matlab.ui.control.Button
        BackButton           matlab.ui.control.Button
        ChooseanoptionLabel  matlab.ui.control.Label
        PVTDiagramgivenIsothermTemperaturesButton  matlab.ui.control.Button
        TwoPhaseEnvelopeonaPVDiagramButton  matlab.ui.control.Button
        IsothermgivenTemperatureonaPVDiagramButton  matlab.ui.control.Button
        Image                matlab.ui.control.Image
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.VolumeUIFigure,'center');
        end

        % Button pushed function: 
        % IsothermgivenTemperatureonaPVDiagramButton
        function IsothermgivenTemperatureonaPVDiagramButtonPushed(app, event)
            Volume1;
            delete(app);
        end

        % Button pushed function: BackButton
        function BackButtonPushed(app, event)
            EoS_Simulator;
            delete(app);
        end

        % Button pushed function: TwoPhaseEnvelopeonaPVDiagramButton
        function TwoPhaseEnvelopeonaPVDiagramButtonPushed(app, event)
            Volume2;
            delete(app);
        end

        % Button pushed function: PVTDiagramgivenIsothermTemperaturesButton
        function PVTDiagramgivenIsothermTemperaturesButtonPushed(app, event)
            Volume3;
            delete(app); 
        end

        % Button pushed function: 
        % PsatgivenTapplyingDifferentsBracketingMethods
        function PsatgivenTapplyingDifferentsBracketingMethodsButtonPushed(app, event)
            Volume4;
            delete(app); 
        end

        % Button pushed function: IsobargivenPressureonaTVDiagramButton
        function IsobargivenPressureonaTVDiagramButtonPushed(app, event)
            Volume5;
            delete(app); 
        end

        % Button pushed function: TwoPhaseEnvelopeonaTVDiagramButton
        function TwoPhaseEnvelopeonaTVDiagramButtonPushed(app, event)
            Volume6;
            delete(app); 
        end

        % Button pushed function: PVTDiagramgivenIsobarPressuresButton
        function PVTDiagramgivenIsobarPressuresButtonPushed(app, event)
            Volume7;
            delete(app); 
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create VolumeUIFigure and hide until all components are created
            app.VolumeUIFigure = uifigure('Visible', 'off');
            app.VolumeUIFigure.Color = [1 1 1];
            app.VolumeUIFigure.Position = [475 325 720 313];
            app.VolumeUIFigure.Name = 'Volume';
            app.VolumeUIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.VolumeUIFigure.Resize = 'off';

            % Create Image
            app.Image = uiimage(app.VolumeUIFigure);
            app.Image.Position = [507 72 198 162];
            app.Image.ImageSource = 'Logo.PNG';

            % Create IsothermgivenTemperatureonaPVDiagramButton
            app.IsothermgivenTemperatureonaPVDiagramButton = uibutton(app.VolumeUIFigure, 'push');
            app.IsothermgivenTemperatureonaPVDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @IsothermgivenTemperatureonaPVDiagramButtonPushed, true);
            app.IsothermgivenTemperatureonaPVDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.IsothermgivenTemperatureonaPVDiagramButton.FontWeight = 'bold';
            app.IsothermgivenTemperatureonaPVDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.IsothermgivenTemperatureonaPVDiagramButton.Position = [11 243 482 22];
            app.IsothermgivenTemperatureonaPVDiagramButton.Text = 'Isotherm given Temperature on a PV Diagram';

            % Create TwoPhaseEnvelopeonaPVDiagramButton
            app.TwoPhaseEnvelopeonaPVDiagramButton = uibutton(app.VolumeUIFigure, 'push');
            app.TwoPhaseEnvelopeonaPVDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @TwoPhaseEnvelopeonaPVDiagramButtonPushed, true);
            app.TwoPhaseEnvelopeonaPVDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.TwoPhaseEnvelopeonaPVDiagramButton.FontWeight = 'bold';
            app.TwoPhaseEnvelopeonaPVDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.TwoPhaseEnvelopeonaPVDiagramButton.Position = [11 212 482 22];
            app.TwoPhaseEnvelopeonaPVDiagramButton.Text = 'Two-Phase Envelope on a PV Diagram';

            % Create PVTDiagramgivenIsothermTemperaturesButton
            app.PVTDiagramgivenIsothermTemperaturesButton = uibutton(app.VolumeUIFigure, 'push');
            app.PVTDiagramgivenIsothermTemperaturesButton.ButtonPushedFcn = createCallbackFcn(app, @PVTDiagramgivenIsothermTemperaturesButtonPushed, true);
            app.PVTDiagramgivenIsothermTemperaturesButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.PVTDiagramgivenIsothermTemperaturesButton.FontWeight = 'bold';
            app.PVTDiagramgivenIsothermTemperaturesButton.FontColor = [0.1373 0.298 0.4784];
            app.PVTDiagramgivenIsothermTemperaturesButton.Position = [11 181 482 22];
            app.PVTDiagramgivenIsothermTemperaturesButton.Text = 'PVT Diagram given Isotherm Temperatures';

            % Create ChooseanoptionLabel
            app.ChooseanoptionLabel = uilabel(app.VolumeUIFigure);
            app.ChooseanoptionLabel.HorizontalAlignment = 'center';
            app.ChooseanoptionLabel.FontWeight = 'bold';
            app.ChooseanoptionLabel.FontColor = [0.1373 0.298 0.4784];
            app.ChooseanoptionLabel.Position = [200 272 107 22];
            app.ChooseanoptionLabel.Text = 'Choose an option';

            % Create BackButton
            app.BackButton = uibutton(app.VolumeUIFigure, 'push');
            app.BackButton.ButtonPushedFcn = createCallbackFcn(app, @BackButtonPushed, true);
            app.BackButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.BackButton.FontWeight = 'bold';
            app.BackButton.FontColor = [0.1373 0.298 0.4784];
            app.BackButton.Position = [14 23 479 22];
            app.BackButton.Text = 'Back';

            % Create PsatgivenTapplyingDifferentsBracketingMethods
            app.PsatgivenTapplyingDifferentsBracketingMethods = uibutton(app.VolumeUIFigure, 'push');
            app.PsatgivenTapplyingDifferentsBracketingMethods.ButtonPushedFcn = createCallbackFcn(app, @PsatgivenTapplyingDifferentsBracketingMethodsButtonPushed, true);
            app.PsatgivenTapplyingDifferentsBracketingMethods.BackgroundColor = [0.8588 0.9608 0.9608];
            app.PsatgivenTapplyingDifferentsBracketingMethods.FontWeight = 'bold';
            app.PsatgivenTapplyingDifferentsBracketingMethods.FontColor = [0.1373 0.298 0.4784];
            app.PsatgivenTapplyingDifferentsBracketingMethods.Position = [13 149 480 22];
            app.PsatgivenTapplyingDifferentsBracketingMethods.Text = 'Saturation Pressure given Temperature applying Differents Bracketing Methods';

            % Create IsobargivenPressureonaTVDiagramButton
            app.IsobargivenPressureonaTVDiagramButton = uibutton(app.VolumeUIFigure, 'push');
            app.IsobargivenPressureonaTVDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @IsobargivenPressureonaTVDiagramButtonPushed, true);
            app.IsobargivenPressureonaTVDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.IsobargivenPressureonaTVDiagramButton.FontWeight = 'bold';
            app.IsobargivenPressureonaTVDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.IsobargivenPressureonaTVDiagramButton.Position = [12 118 481 22];
            app.IsobargivenPressureonaTVDiagramButton.Text = 'Isobar given Pressure on a TV Diagram';

            % Create TwoPhaseEnvelopeonaTVDiagramButton
            app.TwoPhaseEnvelopeonaTVDiagramButton = uibutton(app.VolumeUIFigure, 'push');
            app.TwoPhaseEnvelopeonaTVDiagramButton.ButtonPushedFcn = createCallbackFcn(app, @TwoPhaseEnvelopeonaTVDiagramButtonPushed, true);
            app.TwoPhaseEnvelopeonaTVDiagramButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.TwoPhaseEnvelopeonaTVDiagramButton.FontWeight = 'bold';
            app.TwoPhaseEnvelopeonaTVDiagramButton.FontColor = [0.1373 0.298 0.4784];
            app.TwoPhaseEnvelopeonaTVDiagramButton.Position = [13 87 480 22];
            app.TwoPhaseEnvelopeonaTVDiagramButton.Text = 'Two-Phase Envelope on a TV Diagram';

            % Create PVTDiagramgivenIsobarPressuresButton
            app.PVTDiagramgivenIsobarPressuresButton = uibutton(app.VolumeUIFigure, 'push');
            app.PVTDiagramgivenIsobarPressuresButton.ButtonPushedFcn = createCallbackFcn(app, @PVTDiagramgivenIsobarPressuresButtonPushed, true);
            app.PVTDiagramgivenIsobarPressuresButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.PVTDiagramgivenIsobarPressuresButton.FontWeight = 'bold';
            app.PVTDiagramgivenIsobarPressuresButton.FontColor = [0.1373 0.298 0.4784];
            app.PVTDiagramgivenIsobarPressuresButton.Position = [13 55 480 22];
            app.PVTDiagramgivenIsobarPressuresButton.Text = 'PVT Diagram given Isobar Pressures';

            % Show the figure after all components are created
            app.VolumeUIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = Volume

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.VolumeUIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.VolumeUIFigure)
        end
    end
end
```
