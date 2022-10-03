% Do not put a semicolon at the end of each line to see the answer to each task.
% Task_1: Check that methane at a pressure of 1.919 bar and entropy of 6 kJ/kg·K is in the saturated liquid-vapor mixture and calculate its quality. Use Redlich-Kwong as cubic equation of state.
Task_1=(6-4.8151)/(9.4393-4.8151) % Methane - x @ P=1.919 bar, EoS=RK
% Task_2: What is the pressure of hydrogen at a temperature of 25 K and entropy of 47.2908 kJ/kg·K, in bar? Use Soave-Redlich-Kwong as cubic equation of state.
Task_2=0.40584 % Hydrogen - P [bar] @ T=25 K, s=47.2908 kJ/kg·K, EoS=SRK
% Task_3: What is the temperature of argon at a pressure of 9.107 bar and entropy of 1.3897 kJ/kg·K, in K? Use Peng-Robinson as cubic equation of state.
Task_3=88.942 % Argon - T [K] @ P=9.107 bar, s=1.3897 kJ/kg·K, EoS=PR
% Task_4: What is the entropy of saturated vapor oxygen at a pressure of 34.45 bar, in kJ/kg·K? Use van der Waals as cubic equation of state.
Task_4=4.6251 % Oxygen - Saturated vapor oxygen - s [kJ/kg·K] @ P=34.45 bar, EoS=vdW
% Task_5 (Challenge - Example 7-3 in Çengel et al., 2019 (Figure 18) - Use Peng-Robinson as cubic equation of state and pressure as a state property. Answer in kJ/K): A rigid tank contains 5 kg of refrigerant-134a initially at 20°C and 140 kPa. The refrigerant is now cooled while being stirred until its pressure drops to 100 kPa. Determine the entropy change of the refrigerant during this process.
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
m=5 % [kg]
Task_5=m*(s2-s1) % Example 7-3 in Çengel et al., 2019 [kJ/K], EoS=PR