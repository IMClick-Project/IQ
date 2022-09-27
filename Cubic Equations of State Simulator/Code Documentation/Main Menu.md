# Main Menu

The simulator's main menu is the MATLAB App file called "EoS_Simulator.mlapp".

## 1. MATLAB App

### 1.1. Design View

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/main.jpg" width="342" height="168">

*Figure 1. Design View in EoS_Simulator.mlapp.*

### 1.2. Code View

```Matlab
classdef EoS_Simulator < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        UIFigure             matlab.ui.Figure
        SelectpropertyLabel  matlab.ui.control.Label
        EntropyButton        matlab.ui.control.Button
        EnthalpyButton       matlab.ui.control.Button
        VolumeButton         matlab.ui.control.Button
        Image                matlab.ui.control.Image
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function startupFcn(app)
            clc;
            movegui(app.UIFigure,'center');
        end

        % Button pushed function: VolumeButton
        function VolumeButtonPushed(app, event)
            Volume;
            delete(app);
        end

        % Button pushed function: EnthalpyButton
        function EnthalpyButtonPushed(app, event)
            Enthalpy;
            delete(app);
        end

        % Button pushed function: EntropyButton
        function EntropyButtonPushed(app, event)
            Entropy;
            delete(app);
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Get the file path for locating images
            pathToMLAPP = fileparts(mfilename('fullpath'));

            % Create UIFigure and hide until all components are created
            app.UIFigure = uifigure('Visible', 'off');
            app.UIFigure.Color = [1 1 1];
            app.UIFigure.Position = [475 325 340 167];
            app.UIFigure.Name = 'EoS Simulator';
            app.UIFigure.Icon = fullfile(pathToMLAPP, 'Logoico.png');
            app.UIFigure.Resize = 'off';

            % Create Image
            app.Image = uiimage(app.UIFigure);
            app.Image.Position = [12 6 198 162];
            app.Image.ImageSource = 'Logo.PNG';

            % Create VolumeButton
            app.VolumeButton = uibutton(app.UIFigure, 'push');
            app.VolumeButton.ButtonPushedFcn = createCallbackFcn(app, @VolumeButtonPushed, true);
            app.VolumeButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.VolumeButton.FontWeight = 'bold';
            app.VolumeButton.FontColor = [0.1373 0.298 0.4784];
            app.VolumeButton.Position = [224 89 100 22];
            app.VolumeButton.Text = 'Volume';

            % Create EnthalpyButton
            app.EnthalpyButton = uibutton(app.UIFigure, 'push');
            app.EnthalpyButton.ButtonPushedFcn = createCallbackFcn(app, @EnthalpyButtonPushed, true);
            app.EnthalpyButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EnthalpyButton.FontWeight = 'bold';
            app.EnthalpyButton.FontColor = [0.1373 0.298 0.4784];
            app.EnthalpyButton.Position = [224 58 100 22];
            app.EnthalpyButton.Text = 'Enthalpy';

            % Create EntropyButton
            app.EntropyButton = uibutton(app.UIFigure, 'push');
            app.EntropyButton.ButtonPushedFcn = createCallbackFcn(app, @EntropyButtonPushed, true);
            app.EntropyButton.BackgroundColor = [0.8588 0.9608 0.9608];
            app.EntropyButton.FontWeight = 'bold';
            app.EntropyButton.FontColor = [0.1373 0.298 0.4784];
            app.EntropyButton.Position = [224 27 100 22];
            app.EntropyButton.Text = 'Entropy';

            % Create SelectpropertyLabel
            app.SelectpropertyLabel = uilabel(app.UIFigure);
            app.SelectpropertyLabel.FontWeight = 'bold';
            app.SelectpropertyLabel.FontColor = [0.1373 0.298 0.4784];
            app.SelectpropertyLabel.Position = [229 118 89 22];
            app.SelectpropertyLabel.Text = 'Select property';

            % Show the figure after all components are created
            app.UIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = EoS_Simulator

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.UIFigure)

            % Execute the startup function
            runStartupFcn(app, @startupFcn)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.UIFigure)
        end
    end
end
```
