# Database: Add Compound Data

In addition to explaining the applied theoretical basis for the implementation of the EoS Simulator, this course aims to present a user guide and practical problems to be solved with the results of the simulator. This first problem shows a basic description of the simulator, as well as how to download and install it and which are its components and functions. Also, the ultimate goal is to learn how to add thermodynamic data to the simulator database.

## 1. EoS Simulator

EoS Simulator (**Figure 1**) is a program developed in MATLAB<sup>&reg;</sup> R2022a that calculates and plots $\mathbf{VLE}$ diagrams/surfaces of a pure substance. It also compares its results with experimental values ​​or results obtained by Antoine's equation. The requirements to install and run this application are:

+ Operating System: Windows.
+ MATLAB Version: R2018a or higher. The Optimization Toolbox must be installed.
+ Screen Resolution: 1366x768 or higher.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/Problem%201/logo.jpg" width="402" height="219">

*Figure 1. EoS Simulator logo and icon.*

### 1.1. How to download and install EoS Simulator?

The application is in a zipped folder located in a repository on GitHub<sup>&reg;</sup>. The steps to download and install the simulator are:

1.  Go to [https://github.com/IMClick-Project/IQ/tree/main/Cubic%20Equations%20of%20State%20Simulator](https://github.com/IMClick-Project/IQ/tree/main/Cubic%20Equations%20of%20State%20Simulator).
2.  Click on "EoS Simulator.rar".
3.  Click on the "Download" button.
4.  After the download is complete, unzip the downloaded file to the C drive (C:). A folder with the application icon will appear.

After completing these steps, EoS Simulator will be installed and ready to use.

### 1.2. Components and Functions

When opening the simulator folder, different types of files are shown (**Figure 2**), which will be described below:

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/Problem%201/structure.jpg" width="758" height="336">

*Figure 2. EoS Simulator components.*

+ Exported Results and Macros: The folder includes the results of a simulator task exported in Excel files. It also contains two Excel macros to organize the simulation results of a component in one phase or two phases at equilibrium in thermodynamic tables, in addition to performing interpolations and calculating other thermodynamic properties.
+ Logo Pictures: The program logo in png and ico format. These are used in the visual design of the simulator.
+ **Database:** Excel file that collects experimental data and thermodynamic properties of each compound available to perform the requested thermodynamic calculations and plot the diagrams/surfaces.
+ MATLAB Apps and MATLAB Codes (**Figure 3**): MATLAB files that perform various simulator functions. The app type files (.mlapp) contain the graphic design and programming of its components. Code files (.m) contain the implementation of the thermodynamic calculations.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/Problem%201/codes.jpg" width="986" height="698">

*Figure 3. Organization of MATLAB Apps and MATLAB Codes.*

## 2. Database: Add Compound Data

The Excel file "Thermodynamic Data.xlsx" has a spreadsheet called "Compounds" where there is a table with the necessary properties to perform the calculations and plot the diagrams/surfaces. It is essential to always have at least one compound correctly registered. The columns of this table are:

+ Compound: It cannot: be blank, contain more than 31 characters, contain special characters (/, &#92;, ?, *, :, [, ]), start or end with an apostrophe ('), or be named “History”. These features are because this name will also be used for another spreadsheet.
+ Molar Mass: Molar mass of the Compound in g/mol. This numeric value is necessary and the data cannot be empty.
+ Ttriple: Triple temperature of the Compound in K. This numeric value is necessary and the data cannot be empty.
+ Ptriple: Triple pressure of the Compound in bar. This numeric value is necessary and the data cannot be empty.
+ Tcritical: Critical temperature of the Compound in K. This numeric value is necessary and the data cannot be empty.
+ Pcritical: Critical pressure of the Compound in bar. This numeric value is necessary and the data cannot be empty.
+ w: Acentric factor of the Compound. This numeric value is necessary and the data cannot be empty.
+ Vcritical: Critical volume of the Compound in cm3/mol. This numeric value is necessary and the data cannot be empty.
+ A: $\mathbf{A}$ constant in Antoine equation (**Eq. (5)**). This numeric value is necessary and the data cannot be empty.
+ B: $\mathbf{B}$ constant in Antoine equation (**Eq. (5)**). This numeric value is necessary and the data cannot be empty.
+ C: $\mathbf{C}$ constant in Antoine equation (**Eq. (5)**). This numeric value is necessary and the data cannot be empty.
+ Reference State H: State of aggregation of the reference state for calculations related to enthalpy. This data has three options: "Ideal Gas", "Real Liquid", and "Real Vapor". If these types of calculations are not required and there is no reference data, this data can be "NaN".
+ Treference H: $\mathbf{T_0 [K]}$ for calculations related to enthalpy. In case of not requiring these types of calculations and not having this numerical data, this data can be "NaN".
+ Preference H: $\mathbf{P_0 [bar]}$ for calculations related to enthalpy. In case of not requiring these types of calculations and not having this numerical data, this data can be "NaN".
+ Hreference H: $\mathbf{H_0^{ig} \left[\frac{kJ}{kg}\right]}$ or $\mathbf{H_0 \left[\frac{kJ}{kg}\right]}$ for calculations related to enthalpy. In case of not requiring these types of calculations and not having this numerical data, this data can be "NaN".
+ Reference State S: State of aggregation of the reference state for calculations related to entropy. This data has three options: "Ideal Gas", "Real Liquid", and "Real Vapor". If these types of calculations are not required and there is no reference data, this data can be "NaN".
+ Treference S: $\mathbf{T_0 [K]}$ for calculations related to entropy. In case of not requiring these types of calculations and not having this numerical data, this data can be "NaN".
+ Preference S: $\mathbf{P_0 [bar]}$ for calculations related to entropy. In case of not requiring these types of calculations and not having this numerical data, this data can be "NaN".
+ Sreference S: $\mathbf{S_0^{ig} \left[\frac{kJ}{kg\cdot K}\right]}$ or $\mathbf{S_0 \left[\frac{kJ}{kg\cdot K}\right]}$ for calculations related to entropy. In case of not requiring these types of calculations and not having this numerical data, this data can be "NaN".
+ Acp: $\mathbf{A}$ constant in **Eq. (22)**. This numeric value is necessary and the data cannot be empty.
+ Bcp: $\mathbf{B}$ constant in **Eq. (22)**. This numeric value is necessary and the data cannot be empty.
+ Ccp: $\mathbf{C}$ constant in **Eq. (22)**. This numeric value is necessary and the data cannot be empty.
+ Dcp: $\mathbf{D}$ constant in **Eq. (22)**. This numeric value is necessary and the data cannot be empty.
+ Ecp: $\mathbf{E}$ constant in **Eq. (22)**. This numeric value is necessary and the data cannot be empty.

Also, for each compound, it is necessary to generate a new spreadsheet with the same name as the "Compound" column. This spreadsheet will contain a table with the experimental data in the saturated liquid or saturated vapor state, or the saturation temperatures or pressures of the isotherms or isobars to be predicted, respectively. The columns of this table are:

+ Tsat: Saturation temperature in K. If this data is numerical, it is a temperature considered in the prediction of isotherms and its other recorded data are experimental data. Otherwise, this data is "NaN". 
+ Psat: Saturation pressure in bar. If this data is numerical, it is a pressure considered in the prediction of isobars and its other recorded data are experimental data. Otherwise, this data is "NaN".
+ vf: Volume in saturated liquid state in m3/kg given "Tsat" and "Psat". If this experimental data is not known, it is assigned the value of "NaN". 
+ vg: Volume in saturated vapor state in m3/kg given "Tsat" and "Psat". If this experimental data is not known, it is assigned the value of "NaN".
+ hf: Enthalpy in saturated liquid state in kJ/kg given "Tsat" and "Psat". If this experimental data is not known, it is assigned the value of "NaN". 
+ hg: Enthalpy in saturated vapor state in kJ/kg given "Tsat" and "Psat". If this experimental data is not known, it is assigned the value of "NaN". 
+ sf: Entropy in saturated liquid state in kJ/kg·K given "Tsat" and "Psat". If this experimental data is not known, it is assigned the value of "NaN". 
+ sg: Entropy in saturated vapor state in kJ/kg·K given "Tsat" and "Psat". If this experimental data is not known, it is assigned the value of "NaN".   

Originally, the simulator already has data on the thermodynamic properties and experimental values ​​of five compounds: Ammonia, Argon, Carbon Dioxide, Chlorine, and Hydrogen. The reference state in each compound is an experimental saturation state recorded in their respective tables. The bibliographical references of these data are:

+ Ammonia: Smith *et al.* (2017), Reklaitis & Schneider (1986), and Perry *et al.* (1997).
+ Argon: Smith *et al.* (2017), Reklaitis & Schneider (1986), and Perry *et al.* (1997).
+ Carbon Dioxide: Smith *et al.* (2017), Reklaitis & Schneider (1986), Çengel *et al.* (2019), and Perry *et al.* (1997).
+ Chlorine: Smith *et al.* (2017), Reklaitis & Schneider (1986), U.S. Secretary of Commerce on behalf of the United States of America (2018), and Perry *et al.* (1997).
+ Hydrogen: Smith *et al.* (2017), Reklaitis & Schneider (1986), and Perry *et al.* (1997).

In this problem, the thermodynamic and experimental data of other five compounds will be entered into the simulator database:

+ Methane (Smith *et al.*, 2017; Reklaitis & Schneider, 1986; Perry *et al.*, 1997): Molar Mass=16.043 g/mol, $\mathbf{T_t=}$ 90.7 K, $\mathbf{P_t=}$ 0.117 bar, $\mathbf{T_c=}$ 190.6 K, $\mathbf{P_c=}$ 45.99 bar, $\mathbf{w=}$ 0.012, $\mathbf{V_c=}$ 98.6 cm3/mol, $\mathbf{A=13.5840}$ (**Eq. (5)**), $\mathbf{B=968.13}$ (**Eq. (5)**), $\mathbf{C=-3.7200}$ (**Eq. (5)**), $\mathbf{A=3.83870E+01}$ (**Eq. (22)**), $\mathbf{B=-7.36639E-02}$ (**Eq. (22)**), $\mathbf{C=2.90981E-04}$ (**Eq. (22)**), $\mathbf{D=-2.63849E-07}$ (**Eq. (22)**), and $\mathbf{E=8.00679E-11}$ (**Eq. (22)**).
+ Nitrogen (Smith *et al.*, 2017; Reklaitis & Schneider, 1986; Perry *et al.*, 1997): Molar Mass=28.014 g/mol, $\mathbf{T_t=}$ 63.15 K, $\mathbf{P_t=}$ 0.1253 bar, $\mathbf{T_c=}$ 126.2 K, $\mathbf{P_c=}$ 34 bar, $\mathbf{w=}$ 0.038, $\mathbf{V_c=}$ 89.2 cm3/mol, $\mathbf{A=13.4477}$ (**Eq. (5)**), $\mathbf{B=658.22}$ (**Eq. (5)**), $\mathbf{C=-2.8540}$ (**Eq. (5)**), $\mathbf{A=2.94119E+01}$ (**Eq. (22)**), $\mathbf{B=-3.00681E-03}$ (**Eq. (22)**), $\mathbf{C=5.45064E-05}$ (**Eq. (22)**), $\mathbf{D=5.13186E-09}$ (**Eq. (22)**), and $\mathbf{E=-4.25308E-12}$ (**Eq. (22)**).
+ Oxygen (Smith *et al.*, 2017; Reklaitis & Schneider, 1986; Perry *et al.*, 1997): Molar Mass=31.999 g/mol, $\mathbf{T_t=}$ 54.35 K, $\mathbf{P_t=}$ 0.0015 bar, $\mathbf{T_c=}$ 154.6 K, $\mathbf{P_c=}$ 50.43 bar, $\mathbf{w=}$ 0.022, $\mathbf{V_c=}$ 73.4 cm3/mol, $\mathbf{A=13.6835}$ (**Eq. (5)**), $\mathbf{B=780.26}$ (**Eq. (5)**), $\mathbf{C=-4.1758}$ (**Eq. (5)**), $\mathbf{A=2.98832E+01}$ (**Eq. (22)**), $\mathbf{B=-1.13842E-02}$ (**Eq. (22)**), $\mathbf{C=4.33779E-05}$ (**Eq. (22)**), $\mathbf{D=-3.70082E-08}$ (**Eq. (22)**), and $\mathbf{E=1.01006E-11}$ (**Eq. (22)**).
+ Refrigerant 134a (Smith *et al.*, 2017; Banakar *et al.*, 2013; Perry *et al.*, 1997): Molar Mass=102.03 g/mol, $\mathbf{T_t=}$ 169.85 K, $\mathbf{P_t=}$ 0.0039 bar, $\mathbf{T_c=}$ 374.2 K, $\mathbf{P_c=}$ 40.6 bar, $\mathbf{w=}$ 0.327, $\mathbf{V_c=}$ 198 cm3/mol, $\mathbf{A=14.4100}$ (**Eq. (5)**), $\mathbf{B=2094.00}$ (**Eq. (5)**), $\mathbf{C=-33.0600}$ (**Eq. (5)**), $\mathbf{A=1.94006E+01}$ (**Eq. (22)**), $\mathbf{B=2.58531E-01}$ (**Eq. (22)**), $\mathbf{C=-1.29665E-04}$ (**Eq. (22)**), $\mathbf{D=0}$ (**Eq. (22)**), and $\mathbf{E=0}$ (**Eq. (22)**).
+ Water (Smith *et al.*, 2017; Reklaitis & Schneider, 1986; Çengel *et al.*, 2019): Molar Mass=18.015 g/mol, $\mathbf{T_t=}$ 273.16 K, $\mathbf{P_t=}$ 0.006117 bar, $\mathbf{T_c=}$ 647.1 K, $\mathbf{P_c=}$ 220.55 bar, $\mathbf{w=}$ 0.345, $\mathbf{V_c=}$ 55.9 cm3/mol, $\mathbf{A=16.5362}$ (**Eq. (5)**), $\mathbf{B=3985.44}$ (**Eq. (5)**), $\mathbf{C=-38.9974}$ (**Eq. (5)**), $\mathbf{A=3.40471E+01}$ (**Eq. (22)**), $\mathbf{B=-9.65064E-03}$ (**Eq. (22)**), $\mathbf{C=3.29983E-05}$ (**Eq. (22)**), $\mathbf{D=-2.04467E-08}$ (**Eq. (22)**), and $\mathbf{E=4.30228E-12}$ (**Eq. (22)**).

The experimental data of these compounds will be provided in the following link: [https://github.com/IMClick-Project/IQ/tree/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/Problem%201](https://github.com/IMClick-Project/IQ/tree/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/Problem%201). The reference state information will be a state in saturation provided in these tables:

+ Methane (Perry *et al.*, 1997): Enthalpy-State of aggregation=Real Liquid, $\mathbf{T_0}=$ 150 K, $\mathbf{P_0}=$ 10.41 bar, and $\mathbf{H_0}=$ 429.4 kJ/kg; Entropy-State of aggregation=Real Vapor, $\mathbf{T_0}=$ 150 K, $\mathbf{P_0}=$ 10.41 bar, and $\mathbf{S_0}=$ 8.849 kJ/kg·K.
+ Nitrogen (Perry *et al.*, 1997): Enthalpy-State of aggregation=Real Liquid, $\mathbf{T_0}=$ 90 K, $\mathbf{P_0}=$ 3.6 bar, and $\mathbf{H_0}=$ -95.6 kJ/kg; Entropy-State of aggregation=Real Vapor, $\mathbf{T_0}=$ 90 K, $\mathbf{P_0}=$ 3.6 bar, and $\mathbf{S_0}=$ 5.152 kJ/kg·K.
+ Oxygen (Perry *et al.*, 1997): Enthalpy-State of aggregation=Real Liquid, $\mathbf{T_0}=$ 90.18 K, $\mathbf{P_0}=$ 1.0133 bar, and $\mathbf{H_0}=$ -133.4 kJ/kg; Entropy-State of aggregation=Real Vapor, $\mathbf{T_0}=$ 90.18 K, $\mathbf{P_0}=$ 1.0133 bar, and $\mathbf{S_0}=$ 5.297 kJ/kg·K.
+ Refrigerant 134a (Çengel *et al.*, 2019): Enthalpy-State of aggregation=Real Liquid, $\mathbf{T_0}=$ 289.15 K, $\mathbf{P_0}=$ 5.0458 bar, and $\mathbf{H_0}=$ 73.72 kJ/kg; Entropy-State of aggregation=Real Vapor, $\mathbf{T_0}=$ 289.15 K, $\mathbf{P_0}=$ 5.0458 bar, and $\mathbf{S_0}=$ 0.92409 kJ/kg·K.
+ Water (Çengel *et al.*, 2019): Enthalpy-State of aggregation=Real Liquid, $\mathbf{T_0}=$ 448.15 K, $\mathbf{P_0}=$ 8.926 bar, and $\mathbf{H_0}=$ 741.02 kJ/kg; Entropy-State of aggregation=Real Vapor, $\mathbf{T_0}=$ 448.15 K, $\mathbf{P_0}=$ 8.926 bar, and $\mathbf{S_0}=$ 6.6242 kJ/kg·K.

All compound data from this problem will be used in future exercises and explanations. To evaluate this problem, ten properties will be asked that can be found or calculated with data provided in this problem:

+ Task_1: What is the experimental data of the volume in saturated liquid of chlorine at 303.15 K, in m3/kg?
+ Task_2: What is the experimental data for the saturation temperature at a saturation pressure of 10.83 bar of nitrogen, in K?
+ Task_3: What is the molar mass of hydrogen, in g/mol?
+ Task_4: What is the experimental data of the enthalpy in saturated vapor of methane at 15.94 bar, in kJ/kmol?
+ Task_5: What is the critical temperature of carbon dioxide, in K?
+ Task_6: What is the experimental data for the saturation pressure at a saturation temperature of 100 K of argon, in bar? 
+ Task_7: What is the acentric factor of ammonia?
+ Task_8: What is the triple pressure of oxygen, in bar?
+ Task_9: What is the experimental data of the entropy in saturated liquid of water at 353.15 K, in J/kmol·K?
+ Task_10: What is the experimental data of the enthalpy of vaporization (or latent heat of vaporization) of Refrigerant 134a at 2.1708 bar, in kJ/kg?