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

The values ​​of $\mathbf{h_1}$ and $\mathbf{h_2}$ can be calculated using the "Pressure" tab in "Two Phases in Equilibrium.xlsm" and "One Phase.xlsm" (**Figure 5-7**) option. Unit conversions can be done in the "Extra" tab (**Figure 8**). With this result, it can be determined that using the predictions with the Peng-Robinson cubic equation of state we obtain a percentage error of less than 1% compared to using experimental values, concluding that the result with the simulator is very close to the expected real experimental behavior.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/Problem%205/Assessment%20and%20Code/T5-2-1.jpg" width="1100" height="843">

*Figure 5. Data to know state phase 1 using "Pressure" tab and "Experimental Data" option in "Two Phases in Equilibrium.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/Problem%205/Assessment%20and%20Code/T5-2-2.jpg" width="1084" height="873">

*Figure 6. Data to calculate $h_1$ using "Pressure" tab and "Experimental Data" option in "One Phase.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/Problem%205/Assessment%20and%20Code/T5-2-3.jpg" width="1100" height="824">

*Figure 7. Data to calculate $h_2$ using "Pressure" tab and "Experimental Data" option in "Two Phases in Equilibrium.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/Problem%205/Assessment%20and%20Code/T5-2-4.jpg" width="540" height="217">

*Figure 8. Conversion factors and unit conversions to solve Task 2 using "Extra" tab.*