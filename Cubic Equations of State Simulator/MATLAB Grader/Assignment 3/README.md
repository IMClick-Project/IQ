# Exported Results and Macros

In the folder where the simulator results are exported, two Excel Macro-Enabled workbooks allow the results of the three thermodynamic properties to be organized in a single table to perform linear interpolations, search for the exact data required, and calculate other properties, such as $\mathbf{U}$, $\mathbf{A}$, and $\mathbf{G}$. It is also possible to enter experimental data to carry out the same calculations. This section will explain the parts of these spreadsheets, how to use these macros, and an additional tool to perform manual linear interpolation calculations or unit conversions. It is essential to have the "Developer" tab enabled to view, use or manipulate the coding of these macros ([reference](https://support.microsoft.com/en-us/topic/show-the-developer-tab-e1192344-5e56-4d45-931b-e5fd9bea2d45)). For the next exercises and examples of the use of the macros, the experimental data of water, refrigerant 134a, and ammonia provided by Çengel *et al.* (2019) and Perry *et al.* (1997) will be used ([Excel files](https://github.com/IMClick-Project/IQ/tree/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/Experimental%20Data)). The reference data for each compound are:

+ Ammonia: State of aggregation=Real Vapor, $\mathbf{T_0}=$ 280 K, $\mathbf{P_0}=$ 5.5077 bar, $\mathbf{H_0}=$ 506 kJ/kg, and $\mathbf{S_0}=$ 10.228 kJ/kg·K.
+ Refrigerant 134a: State of aggregation=Real Vapor, $\mathbf{T_0}=$ 289.15 K, $\mathbf{P_0}=$ 5.0458 bar, $\mathbf{H_0}=$ 259.51 kJ/kg, and $\mathbf{S_0}=$ 0.92409 kJ/kg·K.
+ Water: State of aggregation=Real Vapor, $\mathbf{T_0}=$ 448.15 K, $\mathbf{P_0}=$ 8.926 bar, $\mathbf{H_0}=$ 2772.7 kJ/kg, and $\mathbf{S_0}=$ 6.6242 kJ/kg·K.

## 1. One Phase.xlsm

In the "One Phase.xlsm" file there are two spreadsheets (**Figure 1**) to perform calculations with the results of the thermodynamic properties in the liquid or vapor phase of an isotherm ("Temperature" tab - [documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Macros%201%20-%20Temperature%20tab%20in%20One%20Phase.md)) or an isobar ("Pressure" tab - [documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Macros%202%20-%20Pressure%20tab%20in%20One%20Phase.md)). Each spreadsheet has five sections: **section a)** shows the general data of the final thermodynamic table, such as the name of the compound, the cubic equation of state used in the Fugacity Test, the temperature of the isotherm or pressure of the isobar, and reference state data for estimates related to $\mathbf{H}$ or $\mathbf{S}$ (this state must be the same in both properties); **section b)** allows the selection of the system of units and the second thermodynamic property to perform searches or linear interpolations, as well as displaying the headers of the final thermodynamic tables depending on the selected options; **section c)** contains the options to run the macro and the buttons to perform the macro operations and clear the work area; **section d)** presents the results for the liquid phase; and **section e)** indicates the results for the vapor phase. In these last two sections, it is possible to perform linear interpolation calculations or search for the exact data required, as well as to estimate other thermodynamic properties. To do this, the value entered in cell G16 or R16 must be a numerical value between the minimum and maximum of the second property selected in section b). In general, it is important not to manipulate cells that contain formulas, most of which contain the "-" character by default.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/one_phase.jpg" width="1075" height="663">

*Figure 1. Parts of "Temperature" tab and "Pressure" tab in "One Phase.xlsm".*

**Figures 2-3** illustrate how both macros are used to order the results provided by the simulator when executing the Fugacity Test. It is essential to save the Excel files created by the simulator in ".xlsm" format and have them open when running the macros. In the "Temperature" tab, the calculations of the isotherm at 250 K of ammonia with the Peng-Robinson cubic equation of state were used, while in the "Pressure" tab the estimates of the isobar at 1.6496 bar = 23.92543 psia of ammonia with the Peng-Robinson cubic equation of state were used. As the second property, pressure and volume were selected, respectively.

Pressing "Compute" organizes all the data obtained by the simulator into two thermodynamic tables, one for the liquid phase and the other for the vapor phase, to carry out searches or linear interpolations of these data and estimate other thermodynamic properties. This macro is not executed if the general data between the simulator results do not match, if the simulator results are not open or in the incorrect format (error 9, press "End" to cancel execution), or if there is information from the cells A14 or L14. In the case of the "Pressure" tab, the macro cannot be executed if the results to be organized coincide with a thermodynamically impossible case and there are no data in the liquid or vapor phase obtained by the Fugacity Test.

At the end of using the thermodynamic table of all properties, it is possible to clean the results in the spreadsheet through the "Clean" button.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/one_phase_1.jpg" width="1100" height="696">

*Figure 2. Example of using the macro of the "Temperature" tab and "Fugacity Test" option in "One Phase.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/one_phase_2.jpg" width="1108" height="705">

*Figure 3. Example of using the macro of the "Pressure" tab and "Fugacity Test" option in "One Phase.xlsm".*

**Figures 4-5** illustrate how both macros are used to execute calculations related to experimental data. In the "Temperature" tab, the experimental data of the isotherm at 859.67 R of water were used, while in the "Pressure" tab the experimental data of the isobar at 0.6 bar of refrigerant 134a were used. As the second property, enthalpy and entropy were selected, respectively. Pressing "Compute" organizes all the data in their respective thermodynamic table by phase to carry out searches or linear interpolations of these data and estimate other thermodynamic properties. This macro is not executed if the compound, the isotherm temperature or the isobar pressure is unknown, or if there is no information from the cells A14 and L14. It is not necessary to fill in the Z values. At the end of using the thermodynamic table of all properties, it also is possible to clean the results in the spreadsheet through the "Clean" button.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/one_phase_3.jpg" width="987" height="517">

*Figure 4. Example of using the macro of the "Temperature" tab and "Experimental Data" option in "One Phase.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/one_phase_4.jpg" width="966" height="615">

*Figure 5. Example of using the macro of the "Pressure" tab and "Experimental Data" option in "One Phase.xlsm".*

## 2. Two Phases in Equilibrium.xlsm

In the "Two Phases in Equilibrium.xlsm" file there are two spreadsheets (**Figure 6**) to perform calculations with the results of the thermodynamic properties in saturated liquid–vapor mixture based on temperature ("Temperature" tab - [documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Macros%203%20-%20Temperature%20tab%20in%20Two%20Phases%20in%20Equilibrium.md)) or pressure ("Pressure" tab - [documented code](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Macros%204%20-%20Pressure%20tab%20in%20Two%20Phases%20in%20Equilibrium.md)). Each spreadsheet has four sections: **section a)** shows the general data of the final thermodynamic table, such as the name of the compound, the cubic equation of state used in the Fugacity Test, and reference state data for estimates related to $\mathbf{H}$ or $\mathbf{S}$ (this state must be the same in both properties); **section b)** allows the selection of the system of units to perform searches or linear interpolations, as well as displaying the headers of the final thermodynamic tables depending on the selected option; **section c)** contains the options to run the macro and the buttons to perform the macro operations and clear the work area; and **section d)** displays the thermodynamic table with all the simulator results or experimantal data, and it is possible to perform linear interpolation calculations or search for the exact data required, as well as to estimate other thermodynamic properties. To do this, the value entered in cell L14 must be a numerical value between the minimum and maximum of the base property of the macro. Through the selection of the second property in cell O18 and assigning a numerical value in cell P18 it is possible to define a state in saturated liquid–vapor mixture. In case this second property defines a state in a single phase, cell P20 shows the corresponding state as a guide for further calculations.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/two_phases.jpg" width="1039" height="835">

*Figure 6. Parts of "Temperature" tab and "Pressure" tab in "Two Phases in Equilibrium.xlsm".*

**Figures 7-8** illustrate how both macros are used to order the results provided by the simulator when executing the Fugacity Test. Like the previous macros, it is essential to save the Excel files created by the simulator in ".xlsm" format and have them open when running the macros. In the "Temperature" tab, the calculations of water properties with the Peng-Robinson cubic equation of state were used, while in the "Pressure" tab the estimates of refrigerant 134a properties with the Peng-Robinson cubic equation of state were used. As a second property, quality and volume were selected, respectively.

Pressing "Compute" organizes all the data obtained by the simulator into one thermodynamic table to carry out searches or linear interpolations of these data and estimate other thermodynamic properties. This macro is not executed if the general data between the simulator results do not match, if the simulator results are not open or in the incorrect format (error 9, press "End" to cancel execution), or if there is information from the cells A12. In the case of the "Pressure" tab, the macro cannot be executed if the results to be organized coincide with a thermodynamically impossible case and there are no data in the saturated liquid–vapor mixture obtained by the Fugacity Test.

At the end of using the thermodynamic table of all properties, it is possible to clean the results in the spreadsheet through the "Clean" button.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/two_phases_1.jpg" width="1154" height="772">

*Figure 7. Example of using the macro of the "Temperature" tab and "Fugacity Test" option in "Two Phases in Equilibrium.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/two_phases_2.jpg" width="1140" height="771">

*Figure 8. Example of using the macro of the "Pressure" tab and "Fugacity Test" option in "Two Phases in Equilibrium.xlsm".*

**Figures 9-10** illustrate how both macros are used to execute calculations related to experimental data. In both examples the experimental data of ammonia were used. As a second property, enthalpy and entropy were selected, respectively. Pressing "Compute" organizes all the data in one thermodynamic table to carry out searches or linear interpolations of these data and estimate other thermodynamic properties. This macro is not executed if the compound is unknown or if there is no information from the cells A12. It is not necessary to fill in the Z values. At the end of using the thermodynamic table of all properties, it also is possible to clean the results in the spreadsheet through the "Clean" button.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/two_phases_3.jpg" width="995" height="663">

*Figure 9. Example of using the macro of the "Temperature" tab and "Experimental Data" option in "Two Phases in Equilibrium.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/two_phases_4.jpg" width="1008" height="691">

*Figure 10. Example of using the macro of the "Pressure" tab and "Experimental Data" option in "Two Phases in Equilibrium.xlsm".*

## 3. "Extra" tab

Both Excel files have a tab called "Extra" (**Figure 11** - for a more detailed description, see its [documentation](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/Macros%205%20-%20Extra%20tab.md)). In this spreadsheet, it is possible to carry out three options: **a)** manually write the data to perform linear interpolations of up to ten properties; **b)** shows some important constants to solve problems related to the thermodynamic properties discussed in this course; and **c)** it has twenty forms to perform unit conversions. The last two options are based on information provided by Çengel *et al.* (2019).

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%203/extra.jpg" width="1009" height="409">

*Figure 11. Parts of "Extra" tab in "One Phase.xlsm" and "Two Phases in Equilibrium.xlsm".*