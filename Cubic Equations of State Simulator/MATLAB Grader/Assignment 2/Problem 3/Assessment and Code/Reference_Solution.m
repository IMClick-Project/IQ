% Do not put a semicolon at the end of each line to see the answer to each task.
% Task_1: What is the temperature of ammonia at a pressure of 3.81 bar and enthalpy of 758.5853 kJ/kg, in K? Use Peng-Robinson as cubic equation of state.
Task_1=390.4776 % Ammonia - T [K] @ P=3.81 bar, h=758.5853 kJ/kg, EoS=PR
% Task_2: What is the enthalpy of chlorine at a saturation temperature of 373.15 K and quality of 0.84, in kJ/kg? Use Soave-Redlich-Kwong as cubic equation of state.
Task_2=(548.6774-381.848)*0.84+381.848 % Chlorine - havg @ T=373.15 K, x=0.84, EoS=SRK
% Task_3: What is the enthalpy of saturated liquid carbon dioxide at a temperature of 255 K, in kJ/kg? Use van der Waals as cubic equation of state.
Task_3=596.4208 % Saturated liquid carbon dioxide - h [kJ/kg] @ T=255 K, EoS=vdW
% Task_4: What is the pressure of nitrogen at a temperature of 120 K and enthalpy of -12.747 kJ/kg, in bar? Use Redlich-Kwong as cubic equation of state.
Task_4=191.3867 % Nitrogen - P [bar] @ T=120 K, h=-12.747 kJ/kg, EoS=RK
% Task_5 (Challenge - Problem 5-48 in Çengel et al., 2019 (Figure 18) - Use Peng-Robinson as cubic equation of state and pressure as a state property. Answer in MW): Steam flows steadily through an adiabatic turbine. The inlet conditions of the steam are 4 MPa, 500°C, and 80 m/s, and the exit conditions are 30 kPa, 92 percent quality, and 50 m/s. The mass flow rate of the steam is 12 kg/s. Determine the power output.
V1=80 % [m/s]
V2=50 % [m/s]
m=12 % [kg/s]
deltake=m*(V1^2-V2^2)/2/1000 % [kW] - 1000 m2/s2=1 kJ/kg
h1=interp1([763.8811 785.6496],[3456.41 3505.5852],773.15) % [kJ/kg]
h2=(2671.0051-254.6992)*0.92+254.6992 % [kJ/kg]
deltah=m*(h1-h2) % [kW]
Task_5=(deltake+deltah)/1000 % Problem 5-48 in Çengel et al., 2019 [MW], EoS=PR