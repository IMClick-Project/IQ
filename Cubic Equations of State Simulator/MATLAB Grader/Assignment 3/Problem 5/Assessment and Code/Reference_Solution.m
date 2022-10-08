% Do not put a semicolon at the end of each line to see the answer to each task.
% Task_1 (Problem 3.73 in Smith et al., 2017 - Use temperature as a state property. Answer in m3/kg): Estimate the volume change of vaporization for ammonia at 20°C. At this temperature the vapor pressure of ammonia is 857 kPa.
Task_1=0.15114-0.0016386 % Problem 3.73 in Smith et al., 2017 [m3/kg]
% Comparison of results with the predictions in the "Simulator Description" section
Task_1_pred=0.15513-0.001842 % [m3/kg]
Error_1=abs((Task_1-Task_1_pred)/Task_1)
% Task_2 (Problem 5-48 in Çengel et al., 2019 (Figure 1) - Use pressure as a state property. Answer in MW): Steam flows steadily through an adiabatic turbine. The inlet conditions of the steam are 4 MPa, 500°C, and 80 m/s, and the exit conditions are 30 kPa, 92 percent quality, and 50 m/s. The mass flow rate of the steam is 12 kg/s. Determine the power output.
V1=80 % [m/s]
V2=50 % [m/s]
m=12 % [kg/s]
deltake=m*(V1^2-V2^2)/2*0.001 % [kW]
h1=3446 % [kJ/kg]
h2=2437.7736 % [kJ/kg]
deltah=m*(h1-h2) % [kW]
Task_2=(deltake+deltah)/1000 % Problem 5-48 in Çengel et al., 2019 [MW]
% Comparison of results with the predictions in the "Simulator Description" section
h1=interp1([763.8811 785.6496],[3456.41 3505.5852],773.15) % [kJ/kg]
h2=(2671.0051-254.6992)*0.92+254.6992 % [kJ/kg]
deltah=m*(h1-h2) % [kW]
Task_2_pred=(deltake+deltah)/1000 % [MW]
Error_2=abs((Task_2-Task_2_pred)/Task_2)
% Task_3 (Example 7-3 in Çengel et al., 2019 (Figure 2) - Use pressure as a state property. Answer in kJ/K): A rigid tank contains 5 kg of refrigerant-134a initially at 20°C and 140 kPa. The refrigerant is now cooled while being stirred until its pressure drops to 100 kPa. Determine the entropy change of the refrigerant during this process.
s1=1.0625 % [kJ/kg·K]
v=0.16544 % [m3/kg]
s2=0.827529239 % [kJ/kg·K]
m=5 % [kg]
Task_3=m*(s2-s1) % Example 7-3 in Çengel et al., 2019 [kJ/K]
% Comparison of results with the predictions in the "Simulator Description" section
MM=102.03 % [g/mol]
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
T1=293.15; % [K]
P1=1.4; % [bar]
Z1=interp1([293.1142 293.9119],[0.9719 0.97213],T1)
v1=Z1*R*T1/1000/P1/MM % [m3/kg]
s1=interp1([293.1142 293.9119],[1.0533 1.0556],T1) % [kJ/kg·K]
P2=1 % [bar]
T2sat=246.789 % [K]
Z2f=0.0036568
Z2g=0.96722
v2f=Z2f*R*T2sat/1000/P2/MM % [m3/kg]
v2g=Z2g*R*T2sat/1000/P2/MM % [m3/kg]
x2=(v1-v2f)/(v2g-v2f)
s2f=0.062549 % [kJ/kg·K]
s2g=0.94624 % [kJ/kg·K]
s2=(s2g-s2f)*x2+s2f % [kJ/kg·K]
Task_3_pred=m*(s2-s1) % [kJ/K]
Error_3=abs((Task_3-Task_3_pred)/Task_3)