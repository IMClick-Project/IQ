# Cubic Equations of State Simulator

## Course Description

Cubic Equations of State (EoS) have represent a simplicity solution to predict $\mathbf{PVT}$ properties of several substances due to their facility to calculate Vapor-Liquid Equlibrium $(\mathbf{VLE})$ data below critical conditions. The Antoine Equation, an empirical model, is commonly applied on iterative schemes were cubic roots are determined to predict $\mathbf{VLE}$ diagrams at saturated pressure points $(\mathbf{P_{sat}})$. However, because empirical correlations that generate accurate data for the $\mathbf{VLE}$ behavior of complex substances are not always known, fugacity test is another correction approach that can be applied in $\mathbf{PVT}$ programs to calculate accurate $\mathbf{PV}$ saturation diagrams and $\mathbf{VLE}$ data tables.

Likewise, the increasing behavior of the saturation pressure between the values ​​of triple temperature and critical temperature allows establishing a real and continuous function $\mathbf{P_{sat}(T_{sat})}$ that solves the question of the saturation temperature given a pressure employing some numerical method such as the bracketing method and the proposed fugacity test. These algorithms allow describing of the $\mathbf{PVT}$ diagram of a pure substance through the predicted isobars or isotherms. 

Finally, enthalpy and entropy are other important properties to predict, and a reference state is essential for this. Therefore, it is necessary to derive the equations that allow the calculation of enthalpy and entropy values ​​​​from $\mathbf{PVT}$ and heat-capacity data, as well as the use of the concept of residual properties.

Therefore, along this document it is intended to report the important notes and documentation needed to develop a simulator that can eject these functions according to thermodynamic theory and computation tools from MATLAB<sup>&reg;</sup>, where equilibrium phase diagrams/surfaces are plotted and compared according to both experimental and Antoine approches. Also, applications of this simulator in chemical engineering problems will be shown.

## Bibliography

+ Banakar, S., Asapu, R., Panneerselvam, V., Cornelio, A. A., & Limperich, D. (2013). Retrospective on Cubic Equation of State for R134a Refrigerant Used in Automotive Application. *SAE Technical Paper Series*. [https://doi.org/10.4271/2013-26-0061](https://doi.org/10.4271/2013-26-0061)
+ Çengel, Y. A., Boles, M. A., & Kanoğlu, M. (2019). *Thermodynamics: An Engineering Approach* (9th ed.). United States: McGraw-Hill Education.
+ Chemours. (2018). *Freon 134a Refrigerant (R-134a): Thermodynamic Properties (SI Units)*. The Chemours Company FC, LLC. [https://www.freon.com/en/-/media/files/freon/freon-134a-si-thermodynamic-properties.pdf?rev=7519d264dfd74fe68c04c9e119f7361f](https://www.freon.com/en/-/media/files/freon/freon-134a-si-thermodynamic-properties.pdf?rev=7519d264dfd74fe68c04c9e119f7361f)
+ Elliott, J. R. & Lira, C. T. (2012). *Introductory Chemical Engineering Thermodynamics* (2nd ed.). United States: Prentice Hall.
+ Galdino, S. (2011). A family of regula falsi root-finding methods. In *Proceedings of the 2011 World Congress on Engineering and Technology*.
+ Intep, S. (2018). A review of bracketing methods for finding zeros of nonlinear functions. *Applied Mathematical Sciences, 12*(3), 137-146. [https://doi.org/10.12988/ams.2018.811](https://doi.org/10.12988/ams.2018.811)
+ Perry, R. H., Green, D. W., & Maloney, J. O. (1997). *Perry's Chemical Engineers' Handbook* (7th ed.). United States: McGraw-Hill.
+ Reklaitis, G. V. & Schneider, D. R. (1986). *Balances de materia y energía* (José Luis Torres Vázquez, trad.). Mexico: Nueva Editorial Interamericana.
+ Sandler, S. I. (2017). *Chemical, Biochemical, and Engineering Thermodynamics* (5th ed.). United States: John Wiley & Sons.
+ Smith, J. M., Ness, V. H., Abbott, M., & Swihart, M. (2017). *Introduction to Chemical Engineering Thermodynamics* (8th ed.). United States: McGraw Hill.
+ U.S. Secretary of Commerce on behalf of the United States of America. (2018). *Chlorine*. NIST Standard Reference Data. [https://webbook.nist.gov/cgi/inchi?ID=C7782505&Mask=4](https://webbook.nist.gov/cgi/inchi?ID=C7782505&Mask=4)
+ Whitacre, J. H. (2011). *A Hybrid Method For Solving A Single Nonlinear Equation* (Masters dissertation, Youngstown State University).