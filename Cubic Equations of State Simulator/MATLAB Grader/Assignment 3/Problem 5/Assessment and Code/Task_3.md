# Task_3 = Reference Solution?

Consider that the volume of the tank is constant and thus $\mathbf{v=v_1=v_2}$. We take the refrigerant in the tank as the system. This is a closed system since no mass crosses the system boundary during the process. We note that the change in entropy of a substance during a process is simply the difference between the entropy values at the final and initial states. The initial state of the refrigerant is completely specified. By estimating the volume of state 1 it is possible to specify state 2. The values ​​of $\mathbf{v}$, $\mathbf{s_1}$, and $\mathbf{s_2}$ can be calculated using the "Pressure" tab in "Two Phases in Equilibrium.xlsm" and "One Phase.xlsm" (**Figure 9-11**) option. Unit conversions can be done in the "Extra" tab (**Figure 12**). Finally, the entropy change of the refrigerant during this process is $\mathbf{\Delta S=m(s_2-s_1)}$. With this result, it can be determined that using the predictions with the Peng-Robinson cubic equation of state we obtain an absolute error of less than 2% compared to using experimental values, concluding that the result with the simulator is very close to the expected real experimental behavior.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/Problem%205/Assessment%20and%20Code/T5-3-1.jpg" width="1100" height="842">

*Figure 9. Data to know state phase 1 using "Pressure" tab and "Experimental Data" option in "Two Phases in Equilibrium.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/Problem%205/Assessment%20and%20Code/T5-3-2.jpg" width="1100" height="810">

*Figure 10. Data to calculate* $s_1$ *and* $v$ *using "Pressure" tab and "Experimental Data" option in "One Phase.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/Problem%205/Assessment%20and%20Code/T5-3-3.jpg" width="1100" height="848">

*Figure 11. Data to calculate* $s_2$ *using "Pressure" tab and "Experimental Data" option in "Two Phases in Equilibrium.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/Problem%205/Assessment%20and%20Code/T5-3-4.jpg" width="551" height="218">

*Figure 12. Unit conversions to solve Task 3 using "Extra" tab.*