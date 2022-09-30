# Simulator Description

EoS Simulator has various functions related to the prediction of thermodynamic properties, such as saturation pressure, saturation temperature, volume, enthalpy, and entropy. This section presents a general description of each function, as well as relevant results for the development of the simulator.

## 1. Simulator Overview

To accurately enter the simulator, you must open the MATLAB App called "EoS_Simulator.mlapp" ([documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Main%20Menu.md)). It is the main menu of the application (**Figure 1**). It contains three buttons to access the menus of the thermodynamic functions related to the property that they indicate respectively. It is essencial in any application window to wait for the file to load and be placed in the central part of the screen, as well as consider that the close button of each window completely closes the application and the screen size of the window cannot be modified.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/simdes6.jpg" width="340" height="194">

*Figure 1. Main Menu.*

The first button on the main menu closes the window and opens the volume menu ([documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Volume%20Menu.md)). The options in the volume menu are (**Figure 2**):

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/simdes7.jpg" width="635" height="303">

*Figure 2. Volume Menu.*

+ Isotherm given Temperature on a PV Diagram: It plots on a PV diagram the isotherm of a substance given a temperature and a cubic equation of state, and using the Fugacity Test. It compares the results at saturation state with those that use Antoine equation and experimental data. It also analyzes the number of iterations of the Fugacity Test taking as initial pressure the maximum point of the analytical isotherm or the saturation pressure estimated by the Antoine equation, and shows the intersection of the vapor and liquid lines in a $\mathbf{P_{sat}}$ vs $\mathbf{f}$ graph, which corresponds to the saturation pressure to be predicted.
+ Two-Phase Envelope on a PV Diagram: It plots on a PV diagram the saturated liquid and vapor line of a substance given the temperatures recorded in the simulator database and a cubic equation of state, and using the Fugacity Test, Antoine equation, and experimental data.
+ PVT Surface given Isotherm Temperatures: It plots on a PVT surface the isotherms of a substance given the temperatures recorded in the simulator database and a cubic equation of state. 
+ **Saturation Temperature given Pressure by applying Different Bracketing Methods:** It performs the analysis of iterations of bracketing methods by predicting the saturation temperature given the pressures recorded in the simulator database, and using the four cubic equations of state and the five proposed bracketing methods.
+ Isobar given Pressure on a TV Diagram: It plots on a TV diagram the isobar of a substance given a pressure and a cubic equation of state, and using the Fugacity Test. It compares the results at saturation state with those that use Antoine equation and experimental data. It also shows the iterations of the selected bracketing method in a $\mathbf{P_{sat}}$ vs $\mathbf{T_{sat}}$ plot and a $\mathbf{T_{sat}}$ vs iteration number plot.
+ Two-Phase Envelope on a TV Diagram: It plots on a TV diagram the saturated liquid and vapor line of a substance given the pressures recorded in the simulator database and a cubic equation of state, and using the Fugacity Test, Antoine equation, and experimental data. 
+ PVT Surface given Isobar Pressures: It plots on a PVT surface the isobars of a substance given the pressures recorded in the simulator database and a cubic equation of state.
+ Back: Close the volume menu and open the main menu again.

Moreover, the second button on the main menu allows access to the enthalpy menu ([documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Enthalpy%20Menu.md)). Its options are (**Figure 3**):

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/simdes8.jpg" width="714" height="304">

*Figure 3. Enthalpy Menu.*

+ Isotherm given Temperature on a PH Diagram: It plots on a PH diagram the isotherm of a substance given a temperature, a reference state, and a cubic equation of state, and using the Fugacity Test. It compares the results at saturation state with those that use Antoine equation and experimental data.
+ Two-Phase Envelope on a PH Diagram: It plots on a PH diagram the saturated liquid and vapor line of a substance given the temperatures recorded in the simulator database, a reference state, and a cubic equation of state, and using the Fugacity Test, Antoine equation, and experimental data. 
+ PHT Surface given Isotherm Temperatures: It plots on a PHT surface the isotherms of a substance given the temperatures recorded in the simulator database, a reference state, and a cubic equation of state. 
+ Isobar given Pressure on a TH Diagram: It plots on a TH diagram the isobar of a substance given a pressure, a reference state, and a cubic equation of state, and using the Fugacity Test. It compares the results at saturation state with those that use Antoine equation and experimental data.
+ Two-Phase Envelope on a TH Diagram: It plots on a TH diagram the saturated liquid and vapor line of a substance given the pressures recorded in the simulator database, a reference state, and a cubic equation of state, and using the Fugacity Test, Antoine equation, and experimental data. 
+ PHT Surface given Isobar Pressures: It plots on a PHT surface the isobars of a substance given the pressures recorded in the simulator database, a reference state, and a cubic equation of state.
+ Back: Close the enthalpy menu and open the main menu again.

Finally, the third button on the main menu allows access to the entropy menu ([documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Entropy%20Menu.md)). Its options are (**Figure 4**):

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/simdes9.jpg" width="713" height="302">

*Figure 4. Entropy Menu.*

+ Isotherm given Temperature on a PS Diagram: It plots on a PS diagram the isotherm of a substance given a temperature, a reference state, and a cubic equation of state, and using the Fugacity Test. It compares the results at saturation state with those that use Antoine equation and experimental data.
+ Two-Phase Envelope on a PS Diagram: It plots on a PS diagram the saturated liquid and vapor line of a substance given the temperatures recorded in the simulator database, a reference state, and a cubic equation of state, and using the Fugacity Test, Antoine equation, and experimental data. 
+ PST Surface given Isotherm Temperatures: It plots on a PST surface the isotherms of a substance given the temperatures recorded in the simulator database, a reference state, and a cubic equation of state. 
+ Isobar given Pressure on a TS Diagram: It plots on a TS diagram the isobar of a substance given a pressure, a reference state, and a cubic equation of state, and using the Fugacity Test. It compares the results at saturation state with those that use Antoine equation and experimental data.
+ Two-Phase Envelope on a TS Diagram: It plots on a TS diagram the saturated liquid and vapor line of a substance given the pressures recorded in the simulator database, a reference state, and a cubic equation of state, and using the Fugacity Test, Antoine equation, and experimental data. 
+ PST Surface given Isobar Pressures: It plots on a PST surface the isobars of a substance given the pressures recorded in the simulator database, a reference state, and a cubic equation of state.
+ Back: Close the entropy menu and open the main menu again.

## 2. Analysis of Iterations of Bracketing Methods

The fourth option of the volume menu allows performing the analysis of iterations of bracketing methods ([documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Volume%204%20-%20Saturation%20Temperature%20given%20Pressure%20by%20applying%20Different%20Bracketing%20Methods.md)). **Figure 5** illustrates the access mode and parts of the window for this option: **section a)** allows selecting the compound to perform the calculations; **section b)** graphs and shows the results of the number of iterations for each bracketing method and each cubic equation of state to estimate the saturation temperature given the pressures recorded in the compound database; and **section c)** displays the total number of iterations for each cubic equation of state and each bracketing method, as well as the calculation of the initial extremes of the function $\mathbf{P_{sat}(T_{sat})}$, which are the triple point and a point close to the critical point, as $\mathbf{T=T_c-0.1}$ (since at the critical point, the cubic equations of state can generate some errors in its approximation to the real behavior and the function used in the calculations that involve the bracketing methods uses these EoS).

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/simdes1.jpg" width="1053" height="886">

*Figure 5. Mode of access to and parts of the window of the fourth option of the volume menu: Saturation Temperature given Pressure by applying Different Bracketing Methods.*

**Figure 6** shows how to use this option. If there are no pressures available in the database, it is not possible to perform the calculations. If not, it performs the operations (for example, considering ammonia as the compound) and when it ends to graph and record the results, you can export the results in an Excel file (**Figure 7**). In general, if the Excel file of this option was previously generated, the results are rewritten (if any of the spreadsheets have text in more than the first 5000 rows, it is recommended to delete the previous Excel file); otherwise, a new Excel file is created to export the results. It is also important to highlight that all graphics in the simulator have editing and display options, as shown in **Figure 8**.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/simdes2.jpg" width="1048" height="1284">

*Figure 6. Mode of use and example of results executing the fourth option of the volume menu: Saturation Temperature given Pressure by applying Different Bracketing Methods.*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/simdes3.jpg" width="1021" height="982">

*Figure 7. Excel file with the exported results: Saturation Temperature given Pressure by applying Different Bracketing Methods.*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/simdes4.jpg" width="559" height="203">

*Figure 8. Graph editing and display options.*

To perform the analysis of iterations of bracketing methods this option was executed with each of the ten compounds and data proposed in this course. The results are summarized in **Figure 9** ([Excel files with results](https://github.com/IMClick-Project/IQ/tree/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Analysis%20of%20Iterations%20of%20Bracketing%20Methods)). In the four EoS, there is no significant difference between the predictions of $\mathbf{T_{sat}}$ using the five bracketing methods. On the other hand, FP presents decreasing numbers of iterations as $\mathbf{P_{sat}}$ increases, even being less than the number of iterations of B and similar to the iterations of FP improvements. However, the number of total iterations is extremely high (at most values ​​close to 50,000 iterations) and the iteration ranges are very high compared to the other four methods (at most 450 times greater). Among the other bracketing methods, B has the largest iteration range, AB and P have iteration ranges close to each other, and I has iteration ranges similar to AB and P or in most cases greater than these. P and AB present the lowest total amounts of iterations in the ten compounds studied. For the cases where AB has fewer total iterations than P, the difference with P is 1-28 iterations. However, when P has the smallest total number of iterations, the difference with AB is significantly larger (3-186 iterations). Therefore, **Pegasus is chosen as the bracketing method** to implement in the simulator.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/simdes5.jpg" width="625" height="1049">

*Figure 9. Summary of analysis of iterations of bracketing methods results.*