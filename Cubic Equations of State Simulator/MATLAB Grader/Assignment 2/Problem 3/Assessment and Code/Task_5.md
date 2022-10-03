# Task_5 = Reference Solution?

Consider the following assumptions:

+ This is a steady-flow process since there is no change with time.
+ Potential energy changes are negligible.
+ The device is adiabatic and thus heat transfer is negligible.

There is only one inlet and one exit, and thus $\mathbf{\dot{m}_1=\dot{m}_2=\dot{m}}$. We take the turbine as the system, which is a control volume since mass crosses the boundary. The energy balance for this steady-flow system can be expressed in the rate form as:

$$
\begin{aligned}
\mathbf{\dot{E}_{in}-\dot{E}_{out}=0\longleftrightarrow \dot{E}_{in}=\dot{E}_{out}}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{\longleftrightarrow \dot{m}\left(h_1+\frac{V_1^2}{2}\right)=\dot{W}_{out}+\dot{m}\left(h_2+\frac{V_2^2}{2}\right) \longleftrightarrow \dot{W}_{out}=\dot{m}\left(h_1-h_2+\frac{V_1^2-V_2^2}{2}\right) }
\end{aligned}
$$


The values ​​of $\mathbf{h_1}$ and $\mathbf{h_2}$ can be calculated entering the pressure data into the database (**Figure 25**) and using the "Isobar given Pressure on a PH Diagram" (**Figure 26-27**) option. To estimate $\mathbf{h_1}$ it is necessary to perform a linear interpolation. The use of the interp1 ([reference](https://la.mathworks.com/help/matlab/ref/interp1.html?lang=en)) function is recommended. To calculate $\mathbf{h_2}$, $\mathbf{h_{2}=h_{fg}x+h_f}$ at P=30 kPa=0.3 bar.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%203/Assessment%20and%20Code/T3-5-1.jpg" width="399" height="99">

*Figure 25. Pressure data of Task 5 in the database.*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%203/Assessment%20and%20Code/T3-5-2.jpg" width="770" height="992">

*Figure 26. Data to calculate $h_1$ using "Isobar given Pressure on a TH Diagram" option.*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%203/Assessment%20and%20Code/T3-5-3.jpg" width="768" height="896">

*Figure 27. Data to calculate $h_2$ using "Isobar given Pressure on a TH Diagram" option.*