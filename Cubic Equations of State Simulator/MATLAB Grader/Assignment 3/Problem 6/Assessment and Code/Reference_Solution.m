% Do not put a semicolon at the end of each line to see the answer to each task.
% Task_1 (Problem 6.31 in Smith et al., 2017 - Answer in kJ): A vessel of 2 m3 capacity contains 0.02 m3 of liquid water and 1.98 m3 of water vapor at 101.33 kPa. How much heat must be added to the contents of the vessel so that the liquid water is just evaporated?
V_liquid=0.02 % [m3]
V_vapor=1.98 % [m3]
v_liquid=0.0012512 % [m3/kg]
v_vapor=1.6915 % [m3/kg]
m_liquid=V_liquid/v_liquid % [kg]
m_vapor=V_vapor/v_vapor % [kg]
m_water=m_liquid+m_vapor % [kg]
x_1=m_vapor/m_water
u_1=471.1748261 % [kJ/kg]
u_2=2484.934305 % [kJ/kg]
Task_1=m_water*(u_2-u_1) % Problem 6.31 in Smith et al., 2017 [kJ]
% Task_2 (Example 16-7 in Çengel et al., 2019 - Answer in BTU/lbm): Calculate the value of the Gibbs function for saturated refrigerant-134a at −30°F as a mixture of liquid and vapor with a quality of 30 percent.
Task_2=-0.304986272 % Example 16-7 in Çengel et al., 2019 [BTU/lbm]
% Task_3 (Example 10-1 in Çengel et al., 2019 (Figure 1)): Consider a steam power plant operating on the simple ideal Rankine cycle. Steam enters the turbine at 3 MPa and 350°C and is condensed in the condenser at a pressure of 75 kPa. Determine the thermal efficiency of this cycle.
h1=286.8413 % [kJ/kg]
s1=0.99441 % [kJ/kg/K]
h2=290.4764033 % [kJ/kg]
h3=3090.184607 % [kJ/kg]
s3=6.692658638 % [kJ/kg/K]
h4=2375.566447 % [kJ/kg]
qin=h3-h2 % [kJ/kg]
qout=h4-h1 % [kJ/kg]
Task_3=1-qout/qin % Example 10-1 in Çengel et al., 2019 