# MATLAB Apps and MATLAB Codes: Volume 

## 1. Isotherm given Temperature on a PV Diagram

The first option of the volume menu allows generating on a PV diagram the isotherm of a substance given a temperature and a cubic equation of state ([documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Volume%201%20-%20Isotherm%20given%20Temperature%20on%20a%20PV%20Diagram.md)). **Figure 1** illustrates the access mode and parts of the window for this option: **section a)** allows selecting the compound, the cubic equation of state, and the isotherm temperature to perform the calculations; **section b)** graphs and shows the results of the computed isotherm on a PV diagram; **section c)** displays the number of iterations and its respective pressure of the Fugacity Test taking as initial pressure the maximum point of the analytical isotherm or the saturation pressure estimated by the Antoine equation; and **section d)** shows plot and results of the vapor and liquid lines in a $\mathbf{P_{sat}}$ vs $\mathbf{f}$ graph, where the intersection of these lines corresponds to the saturation pressure to be predicted.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v1-1.jpg" width="1007" height="905">

*Figure 1. Mode of access to and parts of the window of the first option of the volume menu: Isotherm given Temperature on a PV Diagram.*

**Figure 2** shows how to use this option. If there is no isotherm temperature available, it is not possible to perform the calculations. If not, it performs the operations (for example, considering argon as the compound, van der Waals as the cubic equation of state, and 125 K as the isotherm temperature) and when it ends to graph and record the results, you can export the results in an Excel file (**Figure 3**). In general, there is no significant difference between using the maximum point of the analytical isotherm or the saturation pressure estimated by the Antoine equation as the initial pressure in the Fugacity Test.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v1-2.jpg" width="994" height="1298">

*Figure 2. Mode of use and example of results executing the first option of the volume menu: Isotherm given Temperature on a PV Diagram.*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v1-3.jpg" width="938" height="427">

*Figure 3. Excel file with the exported results: Isotherm given Temperature on a PV Diagram.*

## 2. Two-Phase Envelope on a PV Diagram

The second option of the volume menu allows generating on a PV diagram the saturated liquid and vapor line of a substance given the temperatures recorded in the simulator database and a cubic equation of state ([documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Volume%202%20-%20Two-Phase%20Envelope%20on%20a%20PV%20Diagram.md)). **Figure 4** illustrates the access mode and parts of the window for this option: **section a)** allows selecting the compound and the cubic equation of state to perform the calculations; and **section b)** graphs and shows the results of the computed saturated liquid and vapor line on a PV diagram, as well as the critical point.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v2-1.jpg" width="895" height="896">

*Figure 4. Mode of access to and parts of the window of the second option of the volume menu: Two-Phase Envelope on a PV Diagram.*

**Figure 5** shows how to use this option. If there are no isotherm temperatures available in the simulator database, it is not possible to perform the calculations. If not, it performs the operations (for example, considering carbon dioxide as the compound and Redlich-Kwong as the cubic equation of state) and when it ends to graph and record the results, you can export the results in an Excel file (**Figure 6**).

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v2-2.jpg" width="729" height="1258">

*Figure 5. Mode of use and example of results executing the second option of the volume menu: Two-Phase Envelope on a PV Diagram.*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v2-3.jpg" width="603" height="429">

*Figure 6. Excel file with the exported results: Two-Phase Envelope on a PV Diagram.*

## 3. PVT Surface given Isotherm Temperatures

The third option of the volume menu allows generating on a PVT surface the isotherms of a substance given the temperatures recorded in the simulator database and a cubic equation of state ([documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Volume%203%20-%20PVT%20Surface%20given%20Isotherm%20Temperatures.md)). **Figure 7** illustrates the access mode and parts of the window for this option: **section a)** allows selecting the compound and the cubic equation of state to perform the calculations; and **section b)** graphs and shows the results of the computed isotherms on a PVT surface.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v3-1.jpg" width="895" height="853">

*Figure 7. Mode of access to and parts of the window of the third option of the volume menu: PVT Surface given Isotherm Temperatures.*

**Figure 8** shows how to use this option. If there are no isotherm temperatures available in the simulator database, it is not possible to perform the calculations. If not, it performs the operations (for example, considering chlorine as the compound and Peng-Robinson as the cubic equation of state).

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v3-2.jpg" width="699" height="1122">

*Figure 8. Mode of use and example of results executing the third option of the volume menu: PVT Surface given Isotherm Temperatures.*

## 4. Isobar given Pressure on a TV Diagram

The fifth option of the volume menu allows generating on a TV diagram the isobar of a substance given a pressure and a cubic equation of state ([documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Volume%205%20-%20Isobar%20given%20Pressure%20on%20a%20TV%20Diagram.md)). **Figure 9** illustrates the access mode and parts of the window for this option: **section a)** allows selecting the compound, the cubic equation of state, and the isobar pressure to perform the calculations; **section b)** graphs and shows the results of the computed isobar on a TV diagram; **section c)** shows the iterations of the selected bracketing method in a $\mathbf{P_{sat}}$ vs $\mathbf{T_{sat}}$ plot, as well as the calculation of the initial extremes of the function , which are the triple point and a point close to the critical point, as $\mathbf{T=T_c-0.1}$; and **section d)** displays the iterations of the selected bracketing method in a $\mathbf{T_{sat}}$ vs iteration number plot.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v5-1.jpg" width="1007" height="892">

*Figure 9. Mode of access to and parts of the window of the fifth option of the volume menu: Isobar given Pressure on a TV Diagram.*

**Figure 10** shows how to use this option. If there is no isobar pressure available, it is not possible to perform the calculations. If not, it performs the operations (for example, considering argon as the compound, van der Waals as the cubic equation of state, and 15.81 bar as the isobar pressure) and when it ends to graph and record the results, you can export the results in an Excel file (**Figure 11**). 

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v5-2.jpg" width="994" height="1292">

*Figure 10. Mode of use and example of results executing the fifth option of the volume menu: Isobar given Pressure on a TV Diagram.*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v5-3.jpg" width="440" height="626">

*Figure 11. Excel file with the exported results: Isobar given Pressure on a TV Diagram.*

There is a thermodynamically impossible case that does not allow the prediction to be made through the Fugacity Test. This is when $\mathbf{P_{sat}}$ is not between the $\mathbf{P_{sat}}$ calculated from $\mathbf{T_t}$ and close to $\mathbf{T_c}$. **Figure 12** shows the results of this case in the simulator and exported to an Excel file.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v5-4.jpg" width="994" height="1012">

*Figure 12. Results in the case not thermodynamically possible and the calculations of the Fugacity Test cannot be performed: Isobar given Pressure on a TV Diagram.*

## 5. Two-Phase Envelope on a TV Diagram

The sixth option of the volume menu allows generating on a TV diagram the saturated liquid and vapor line of a substance given the pressures recorded in the simulator database and a cubic equation of state ([documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Volume%206%20-%20Two-Phase%20Envelope%20on%20a%20TV%20Diagram.md)). **Figure 13** illustrates the access mode and parts of the window for this option: **section a)** allows selecting the compound and the cubic equation of state to perform the calculations; and **section b)** graphs and shows the results of the computed saturated liquid and vapor line on a TV diagram, as well as the critical point.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v6-1.jpg" width="895" height="891">

*Figure 13. Mode of access to and parts of the window of the sixth option of the volume menu: Two-Phase Envelope on a TV Diagram.*

**Figure 14** shows how to use this option. If there are no isobar pressures available in the simulator database, it is not possible to perform the calculations. If not, it performs the operations (for example, considering carbon dioxide as the compound and Soave-Redlich-Kwong as the cubic equation of state) and when it ends to graph and record the results, you can export the results in an Excel file (**Figure 15**).

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v6-2.jpg" width="729" height="1256">

*Figure 14. Mode of use and example of results executing the sixth option of the volume menu: Two-Phase Envelope on a TV Diagram.*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v6-3.jpg" width="585" height="418">

*Figure 15. Excel file with the exported results: Two-Phase Envelope on a TV Diagram.*

## 6. PVT Surface given Isobar Pressures

The seventh option of the volume menu allows generating on a PVT surface the isobars of a substance given the pressures recorded in the simulator database and a cubic equation of state ([documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Volume%207%20-%20PVT%20Surface%20given%20Isobar%20Pressures.md)). **Figure 16** illustrates the access mode and parts of the window for this option: **section a)** allows selecting the compound and the cubic equation of state to perform the calculations; and **section b)** graphs and shows the results of the computed isobars on a PVT surface.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v7-1.jpg" width="895" height="849">

*Figure 16. Mode of access to and parts of the window of the seventh option of the volume menu: PVT Surface given Isobar Pressures.*

**Figure 17** shows how to use this option. If there are no isobar pressures available in the simulator database, it is not possible to perform the calculations. If not, it performs the operations (for example, considering chlorine as the compound and Peng-Robinson as the cubic equation of state).

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%202/Problem%202/v7-2.jpg" width="699" height="1122">

*Figure 17. Mode of use and example of results executing the seventh option of the volume menu: PVT Surface given Isobar Pressures.*

## 7. Exercises