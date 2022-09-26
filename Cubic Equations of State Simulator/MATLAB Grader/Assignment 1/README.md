# Basis of Theory

## 1. Thermodynamic Background

### 1.1. Cubic Equations of State (EoS)

Giving $(\mathbf{P,V,T})$ the pressure, molar volume and absolute temperature, the $\mathbf{PVT}$ behaviour of a thermodynamic system can be ideally predicted when these variables satisfy the following general EoS:

$$
\begin{aligned}
\mathbf{(1) \quad P=\frac{RT}{V-b}-\frac{\theta(V-\eta)}{(V-b)(V^2+\kappa V+\gamma)}} 
\end{aligned}
$$

Where $\mathbf{\theta}$, $\mathbf{\eta}$, $\mathbf{b}$, $\mathbf{\kappa}$ and $\mathbf{\gamma}$ are parameters that depend on the chemical composition and the temperature of the substance. Several approches along the history have been applied to modify this model, where factors as $\mathbf{\theta}$ and $\mathbf{\eta}$ haven been reduced to constant and variable factors that depend on size, molecular attractions between substance components, and the macroscopic internal energy of the system. Therefore, if we reduce the above terms as $\mathbf{\eta = b}$, $\mathbf{ \theta = a_{(T)} }$, $\mathbf{ \kappa = (\epsilon + \sigma)b }$, and $\mathbf{ \gamma = \epsilon \sigma b^2 }$, the **Eq. (1)** can be rewritten as **Eq. (2)**, where $\mathbf{\epsilon}$ and $\mathbf{\sigma}$ are parameters that depend on the thermodynamic method, and $\mathbf{a_{(T)}}$ and $\mathbf{b}$ are parameters that depend on the composition and temperature of the system:

$$
\begin{aligned}
\mathbf{(2) \quad P=\frac{RT}{V-b}-\frac{a_{(T)}}{(V+\epsilon b)(V+\sigma b)}}
\end{aligned}
$$

This is important because the assignment of appropriate parameters leads not only to the **van der Waals (vdW)** equation and the **Redlich/Kwong (RK)** equation (which consider $\mathbf{a_{(T)}}$ and $\mathbf{b}$ as constant-temperature terms), but also to the **Soave/Redlich/Kwong** (SRK) and the **Peng/Robinson** (PR) models, involving **Eq. (2)** as a generalized form of classical cubic modifications for simple $\mathbf{VLE}$ predictions.

So, if we calculate $\mathbf{a_{(T)}}$ and $\mathbf{b}$ terms considering the critical $\mathbf{PV}$ isotherm of the susbtance using **Eq. (2)** and applying the **first to second derivate test**, functions of these parameters can be obtained with respect to both critical data and $\mathbf{\alpha_{(T_r,w)}}$ function, where $\mathbf{\Psi}$ and $\mathbf{\Omega}$ are pure numbers which depend to a particular EoS. By the other hand, $\mathbf{\alpha_{(T_r,w)}}$ is a dimesionless empirical factor that depends on the reduced temperature $\mathbf{T_r}$ of the system and the acentric factor $\mathbf{w}$, a term introduced by Pitzer and collaborators for empirical correction porpouses that is specific to a given chemical species and is applied in **SRK** and **PR** models, equations which try to correlate the variable attraction forces magnitudes between susbtance molecules considering temperature changes: $\mathbf{a_{(T)}=\Psi\frac{\alpha_{(T_r,w)}(RT_c)^2}{P_c}}$, $\mathbf{b=\Omega\frac{RT_c}{P_c}}$, and $\mathbf{T_r=\frac{T}{T_c}}$. Critical pressure $\mathbf{P_c}$, critical temperature $\mathbf{T_c}$ and acentric factor $\mathbf{w}$ data of some compounds are (Smith *et al.*, 2017):

+ **Ammonia:** $\mathbf{P_c=}$ 112.80 bar, $\mathbf{T_c=}$ 450.7 K, and $\mathbf{w=}$ 0.253.
+ **Argon:** $\mathbf{P_c=}$ 48.98 bar, $\mathbf{T_c=}$ 150.9 K, and $\mathbf{w=}$ 0.000.
+ **Carbon Dioxide:** $\mathbf{P_c=}$ 73.83 bar, $\mathbf{T_c=}$ 304.2 K, and $\mathbf{w=}$ 0.224.
+ **Chlorine:** $\mathbf{P_c=}$ 77.10 bar, $\mathbf{T_c=}$ 417.2 K, and $\mathbf{w=}$ 0.069.
+ **Hydrogen:** $\mathbf{P_c=}$ 13.13 bar, $\mathbf{T_c=}$ 33.19 K, and $\mathbf{w=}$ -0.216.
+ **Methane:** $\mathbf{P_c=}$ 45.99 bar, $\mathbf{T_c=}$ 190.6 K, and $\mathbf{w=}$ 0.012.
+ **Nitrogen:** $\mathbf{P_c=}$ 34.00 bar, $\mathbf{T_c=}$ 126.2 K, and $\mathbf{w=}$ 0.038.
+ **Oxygen:** $\mathbf{P_c=}$ 50.43 bar, $\mathbf{T_c=}$ 154.6 K, and $\mathbf{w=}$ 0.022.
+ **Refrigerant 134a (Tetrafluoroethane):** $\mathbf{P_c=}$ 40.60 bar, $\mathbf{T_c=}$ 374.2 K, and $\mathbf{w=}$ 0.327.
+ **Water:** $\mathbf{P_c=}$ 220.55 bar, $\mathbf{T_c=}$ 647.1 K, and $\mathbf{w=}$ 0.345.

Based on these facts, $\mathbf{\beta=\frac{bP}{RT}=\Omega\frac{P_r}{T_r}}$ with $\mathbf{P_r=\frac{P}{P_c}}$ and $\mathbf{q=\frac{a_{(T)}}{bRT}=\frac{\Psi \alpha_{(T_r,w)}}{\Omega T_r}}$ parameters can be defined for generalization porpouses and, subsituting their values on **Eq. (2)** and resolving for $\mathbf{V}$, four iterative schemes can be obtained to calculate both liquid and vapor roots under saturated conditions $(\mathbf{P=P_{sat}})$ for a specific cubic isotherm given $\mathbf{T}$ (**Eqs. (3)-(4)**):

$$
\begin{aligned}
\mathbf{(3) \quad V^{v}=\frac{RT}{P}+b-\frac{a_{(T)}}{P}\frac{V^{v}-b}{(V^{v}+\epsilon b)(V^{v}+\sigma b)} \quad \longleftrightarrow \quad Z^{v}=1+\beta-q\beta\frac{Z^{v}-\beta}{(Z^{v}+\epsilon \beta)(Z^{v}+\sigma \beta)} }
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{(4) \quad V^{l}=b+(V^{l}+\epsilon b)(V^{l}+\sigma b)\frac{RT+P(b-V^{l})}{a_{(T)}} \quad \longleftrightarrow \quad Z^{l}=\beta+(Z^{l}+\epsilon \beta)(Z^{l}+\sigma \beta)\frac{1+\beta-Z^{l}}{q\beta}} 
\end{aligned}
$$

Hence, considering initial points for vapor and liquid iterative schemes at $\mathbf{V^v = \frac{RT}{P}}$ (or $\mathbf{Z^v=1}$) and $\mathbf{V^l = b}$ (or $\mathbf{Z^v=\beta}$), respectively, we can compute their roots for several temperature isotherms with the porpoise to plot the $\mathbf{PV}$ saturation curve for any substance using the cubic equation of state that the user prefers, as long as saturation pressures and critical/EoS data are known, according to:

+ **van der Waals (vdW):** $\mathbf{\alpha_{(T_r,w)}}=1$, $\mathbf{\sigma=0}$, $\mathbf{\epsilon=0}$, $\mathbf{\Omega=\frac{1}{8}}$, and $\mathbf{\Psi=\frac{27}{64}}$.
+ **Redlich/Kwong (RK):** $\mathbf{\alpha_{(T_r,w)}=T_r^{-1/2}}$, $\mathbf{\sigma=1}$, $\mathbf{\epsilon=0}$, $\mathbf{\Omega=0.08664}$, and $\mathbf{\Psi=0.42748}$.
+ **Soave/Redlich/Kwong (SRK):** $\mathbf{\alpha_{(T_r,w)}=[1+(0.480+1.574w-0.176w^2)(1-T_r^{1/2})]^2}$, $\mathbf{\sigma=1}$, $\mathbf{\epsilon=0}$, $\mathbf{\Omega=0.08664}$, and $\mathbf{\Psi=0.42748}$.
+ **Peng/Robinson (PR):** $\mathbf{\alpha_{(T_r,w)}=[1+(0.37464+1.54226w-0.26992w^2)(1-T_r^{1/2})]^2}$, $\mathbf{\sigma=1+\sqrt{2}}$, $\mathbf{\epsilon=1-\sqrt{2}}$, $\mathbf{\Omega=0.07780}$, and $\mathbf{\Psi=0.45724}$.

### 1.2. Maxwell Construction and Fugacity Test

Vapor pressures for a pure species are subject to experimental models, such as Antoine's approach (**Eq. (5)**), which uses three empirical constants $(\mathbf{A}$, $\mathbf{B}$ and $\mathbf{C})$ to calculate these data. However, they can also be implicit in an EoS, which makes these models useful as empirical equilibrium data is not known for all compounds.

$$
\begin{aligned}
\mathbf{\ln{P_{sat}} [kPa] = A - \frac{B}{T [K]+C} \quad \longleftrightarrow \quad (5)\quad P_{sat} [bar]=0.01exp\left(A - \frac{B}{T [K]+C}\right)}
\end{aligned}
$$

Empirical constants $\mathbf{A}$, $\mathbf{B}$ and $\mathbf{C}$ data of the above compounds are (Banakar *et al.*, 2013; Reklaitis & Schneider, 1986):

+ **Ammonia:** $\mathbf{A=15.4940}$, $\mathbf{B=2363.24}$, and $\mathbf{C=-22.6207}$.
+ **Argon:** $\mathbf{A=13.9153}$, $\mathbf{B=832.78}$, and $\mathbf{C=2.3608}$.
+ **Carbon Dioxide:** $\mathbf{A=15.3768}$, $\mathbf{B=1956.25}$, and $\mathbf{C=-2.1117}$.
+ **Chlorine:** $\mathbf{A=14.1372}$, $\mathbf{B=2055.15}$, and $\mathbf{C=-23.3117}$.
+ **Hydrogen:** $\mathbf{A=12.7844}$, $\mathbf{B=232.32}$, and $\mathbf{C=8.0800}$.
+ **Methane:** $\mathbf{A=13.5840}$, $\mathbf{B=968.13}$, and $\mathbf{C=-3.7200}$.
+ **Nitrogen:** $\mathbf{A=13.4477}$, $\mathbf{B=658.22}$, and $\mathbf{C=-2.8540}$.
+ **Oxygen:** $\mathbf{A=13.6835}$, $\mathbf{B=780.26}$, and $\mathbf{C=-4.1758}$.
+ **Refrigerant 134a (Tetrafluoroethane):** $\mathbf{A=14.4100}$, $\mathbf{B=2094.00}$, and $\mathbf{C=-33.0600}$.
+ **Water:** $\mathbf{A=16.5362}$, $\mathbf{B=3985.44}$, and $\mathbf{C=-38.9974}$.

In thermodynamic equilibrium, a necessary condition for stability is that pressure must not increase with the volume. This statement is violated by the general EoS function when this is plotted for all its domain $(\mathbf{P}$ vs $\mathbf{V})$. Hence, the **Maxwell Construction** is a way of correcting this deficiency, which stablish that the sinusoidal part of the isotherm must be replaced by a horizontal line whose height is such that the two areas (**EoS loops**) that this line lock up must be equal (**Figure 1**).

![Figure 1](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/PV_MAXWELL.jpg)

*Figure 1. Representation of the Maxwell Construction for a* $T$ *isotherm.*

This statement is necessary for the calculation of real $\mathbf{PV}$ isotherms because, if we save the intersections that this horizontal line makes with the analytical EoS isotherm on work, we could conclude that these points will concur with the $\mathbf{VLE}$ roots at the $\mathbf{P_{sat}}$ that corresponds to the line height. Hence, if we plot all these points for a $\mathbf{T}$ range between the critical and triple point, the $\mathbf{PV}$ saturation curve for any substance can be obtained since the $\mathbf{P_{sat}}$ values that accomplish the Maxwell Construction are previous calculated.

So, to calculate these pressures, we need to call the Free Energy Criterion for any thermodynamic system, which states that the fugacity (or effective pressure) in all phases at equilibrium must be equal. Thus, for a $\mathbf{VLE}$ case, this criterion can be written as **Eq. (6)**, where the fugacity of each $\mathbf{n}$-phase $\mathbf{f^n }$, by definition, can be calculated in terms of their residual free energy $\mathbf{G_n^R}$ (**Eq. (7)**).

$$
\begin{aligned}
\mathbf{(6) \quad f^v = f^l}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{\ln{\frac{f^n}{P_{sat}}} = \ln{\phi^n} =
 \frac{G^R_{n}}{RT} \quad \longleftrightarrow \quad \mathbf{(7)\quad f^n = P_{sat}exp\left(\frac{G^R_{n}}{RT}\right)}}
\end{aligned}
$$

Given the quotient value between $\mathbf{G_n^R}$ and $\mathbf{RT}$ in terms of a general EoS (**Eq. (8)**), the fugacity for an isotherm can be calculated in both $\mathbf{VLE}$ phases estimating an initial saturated pressure, where $\mathbf{I^n}$ is the integral value of **Eq. (9)**, a result that can be obtained from introducing EoS to residual properties calculations:

$$
\begin{aligned}
\mathbf{(8) \quad \frac{G^R_{n}}{RT} = Z^n-1-\ln{(Z^n-\beta)}-qI^n}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{(9) \quad I^n = \int^{\rho^n}_0\frac{d(\rho^n b)}{(1+\epsilon \rho^n b)(1+\sigma \rho^n b)}}
\end{aligned}
$$

For **van der Waals (vdW):** $\mathbf{(a) \quad \epsilon = \sigma \quad \longleftrightarrow \quad }\mathbf{ I^n = \frac{\beta}{Z^n+\epsilon \beta}}$.

For **Redlich/Kwong (RK), Soave/Redlich/Kwong (SRK)**, and **Peng/Robinson (PR):** $\mathbf{(b) \quad \epsilon \neq \sigma \quad \longleftrightarrow \quad \mathbf{ I^n
= \frac{1}{\sigma - \epsilon}\ln{\frac{Z^n+\sigma \beta}{Z^n+\epsilon \beta}}}}$.

Therefore, if we proposed an error value $\mathbf{Er}$ that describes the minimum relative fugacity difference between both $\mathbf{VLE}$ phases required to obtain an effective saturation pressure that can follow the Maxwell Construction, an iterative scheme can be proposed to predict a real EoS isotherm according to the accomplishment of **Ineq. (10)**, a **Fugacity Test** that will always change pressure values under the **Eq. (11)** until the relative fugacity difference gets equal or lower than the approved  value (**Figure 2**).

$$
\begin{aligned}
\mathbf{(10) \quad \left| 1- \frac{f^l_i}{f^v_i} \right| > Er \quad \longrightarrow \quad (11)\quad P_{sat,i+1} = P_{sat,i}\frac{f^l_i}{f^v_i}}
\end{aligned}
$$

![Figure 2](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/ESCHEME.jpg)

*Figure 2. Iterative Scheme for Fugacity Test calculations.*

This process can be followed when a $\mathbf{f_i^n}$ vs $\mathbf{P_{sat,i}}$ graph is plotted (**Figure 3**), where liquid and vapor lines represent the pressure changes with iterations until both fugacity functions intersect. The behavior of this iterative method allows us to visualize how the quotient of both fugacity for a pressure point always tends to decrease as **Ineq. (10)** is fulfilled, which allows this variable to be brought as close as possible to the real value of $\mathbf{P_{sat,i}}$ as $\mathbf{Er}$ is smaller. In other words, the Fugacity Test evaluates the limit of both fugacity functions when $\mathbf{P \rightarrow P_{sat,i}}$, while $\mathbf{Er}$ symbolizes one of the closeness parameters that define this limit.

![Figure 3](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/F_VS_P.jpg)

*Figure 3. Fugacity vs saturation pressure plot.*

Several iterative calculations of this method can be performed for the range of temperatures previous stablished for the working substance, which can lead to the prediction of $\mathbf{PV}$ saturation diagrams based on a primordial initial estimitation for the first pressure $\mathbf{P_{sat,1}}$ used to commence the **Fugacity Test**. So, either the maximum point of the analytical isotherm or the empirical pressure provided by the Antoine equation, the estimation procedure must consider its pressure range within the $\mathbf{PV}$ saturation area, which implies that the difference between the computational methods that use this criterion will only be the required number of iterations that they need to accomplish the **Ineq. (10)**. This is observed when $\mathbf{P}$ vs $\mathbf{i}$ (iteration number) points of each of these methods are plotted, which their curvature will depend on how close the starting pressure is to the $\mathbf{P_{sat}}$ (**Figure 4**).

![Figure 4](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/F_VS_i.jpg)

*Figure 4. Saturation pressure vs* $i$ *(iteration number) plot ($P_{sat,1}^{(1)}>P_{sat,1}^{(2)}>P_{sat,1}^{(3)}$).*

Considering the maximum point of the analytical isotherm as the initial pressure for the Fugacity Test allows establishing a prediction method of the saturation pressure without using empirical parameters such as those of the Antoine equation. This initial pressure is a single value in the analytical isotherm, is always positive (as it is a point above the saturation pressure to be predicted), and depends only on the properties of the substance and the parameters of the cubic equation of state.

On the other hand, the $\mathbf{VLE}$ curve in a $\mathbf{P}$ vs $\mathbf{T}$ diagram demonstrates a continuous increasing behavior between the triple point and the critical point. Therefore, given a saturation pressure $\mathbf{P_{sat,i}}$ (between $\mathbf{P_t}$ and $\mathbf{P_c}$) at which it is intended to estimate its respective $\mathbf{T_{sat,i}}$ (between $\mathbf{T_t}$ and $\mathbf{T_c}$), a function $\mathbf{f(T_{sat})=P_{sat}(T_{sat})-P_{sat,i}}$ can be defined where $\mathbf{f(T_{sat,i})=0}$ and also $\mathbf{f(T_{sat})<0}$ and $\mathbf{f(T_{sat})>0}$ for $\mathbf{T_{sat}<T_{sat,i}}$ and $\mathbf{T_{sat}>T_{sat,i}}$, respectively (**Figure 5**).

![Figure 5](https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/bracketing.jpg)

*Figure 5. Figure 5. Pressure vs temperature plot and representation of the function* $f(T_{sat})$*.*

Finding the zero of the nonlinear function $\mathbf{f(T_{sat})}$ given its characteristics is possible by some **bracketing method**. In addition, by using the Fugacity Test to estimate $\mathbf{P_{sat}(T_{sat})}$, a way of predicting $\mathbf{T_{sat}}$ given a pressure depending only on the properties of the substance and parameters of the cubic equation of state is being proposed, additionally to use the iterative method already developed. The next sections will be explained in more detail the bracketing methods and their study/implementation for the isobars, isotherms, and two-phase envelopes predictions.
