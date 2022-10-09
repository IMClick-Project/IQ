# Task_1 = Reference Solution?

The water is in saturated liquid-vapor mixture. This is a closed system since no mass crosses the system boundary during the process. The direction of heat transfer is to the system (heat gain, $\mathbf{Q_{in}}$). The system does not involve any form of work ($\mathbf{W=0}$). The tank is stationary and thus the kinetic and potential energy changes are zero, $\mathbf{\Delta KE=\Delta PE=0}$. Therefore, the energy balance determines that $\mathbf{Q_{in}=m_{water}(u_2-u_1)}$.

The mass of the water is equal to the mass of the liquid plus the mass of the vapor, that is, $\mathbf{m_{water}=m_{liquid}+m_{vapor}=\frac{0.02\ m^3}{v_{liquid}}+\frac{1.98\ m^3}{v_{vapor}}}$. At state 1, the quality can be calculated as $\mathbf{x_1=\frac{m_{vapor}}{m_{water}}}$. With this quality and pressure, state 1 is specified. State 2 is in saturated vapor, so $\mathbf{x_2=1}$. With this quality and pressure, state 2 is specified.

Pressure unit conversion to bar can be done in the "Extra" tab. The pressure can be registered in the simulator database so that the properties of the saturated state are obtained through the simulator with the options "Two-Phase Envelope on a TV Diagram", "Two-Phase Envelope on a TH Diagram", and "Two-Phase Envelope on a TS Diagram". These results can be used in the "Pressure" tab and "Fugacity Test" option in "Two Phases in Equilibrium.xlsm". **Figure 2** shows a guide to the use of "EoS_Simulator" to calculate the thermodynamic properties necessary to solve this problem.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/Problem%206/Assessment%20and%20Code/T6-1.jpg" width="599" height="1088">

*Figure 2. Guide to the use of "EoS_Simulator" to calculate the thermodynamic properties necessary to solve Task 1.* 