# Task_5 = Reference Solution?

Consider that the volume of the tank is constant and thus $\mathbf{v\left[\frac{m^3}{kg}\right]=v_1=\frac{Z_1RT_1}{1000P_1MM}=v_2=\frac{Z_2RT_2}{1000P_2MM}}$ with $\mathbf{T[K]}$, $\mathbf{P[bar]}$, $\mathbf{MM=}$ 102.03 $\mathbf{\frac{g}{mol}}$, and $\mathbf{R=}$ 83.14 $\mathbf{\frac{cm^3\cdot bar}{mol\cdot K}}$. We take the refrigerant in the tank as the system. This is a closed system since no mass crosses the system boundary during the process. We note that the change in entropy of a substance during a process is simply the difference between the entropy values at the final and initial states. The initial state of the refrigerant is completely specified. By estimating the volume of state 1 it is possible to specify state 2. The values ​​of $\mathbf{s_1}$ and $\mathbf{s_2}$ can be calculated entering the pressure data into the database (**Figure 25**) and using the "Isobar given Pressure on a PS Diagram" (**Figure 26-27**) option. To estimate $\mathbf{s_1}$ it is necessary to perform a linear interpolation. The use of the interp1 ([reference](https://la.mathworks.com/help/matlab/ref/interp1.html?lang=en)) function is recommended. To calculate $\mathbf{s_2}$, it is observed that the volume is between the saturation values ​​at the pressure of state 2, therefore it is a saturated mixture of liquid vapor and $\mathbf{x_2=\frac{v-v_f}{v_{fg}}\longleftrightarrow s_2=s_{fg}x_2+s_f}$ at saturation values ​​at state 2 pressure. Finally, the entropy change of the refrigerant during this process is $\mathbf{\Delta S=m(s_2-s_1)}$.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%204/Assessment%20and%20Code/T4-5-1.jpg" width="407" height="98">

*Figure 25. Pressure data of Task 5 in the database.*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%204/Assessment%20and%20Code/T4-5-2.jpg" width="765" height="877">

*Figure 26. Data to calculate state 1 using "Isobar given Pressure on a TS Diagram" option.*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%204/Assessment%20and%20Code/T4-5-3.jpg" width="765" height="894">

*Figure 27. Data to calculate state 2 using "Isobar given Pressure on a TS Diagram" option.*