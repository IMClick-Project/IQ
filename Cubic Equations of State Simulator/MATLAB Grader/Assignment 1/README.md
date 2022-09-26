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

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/PV_MAXWELL.jpg" width="781" height="381">

*Figure 1. Representation of the Maxwell Construction for a* $T$ *isotherm.*

This statement is necessary for the calculation of real $\mathbf{PV}$ isotherms because, if we save the intersections that this horizontal line makes with the analytical EoS isotherm on work, we could conclude that these points will concur with the $\mathbf{VLE}$ roots at the $\mathbf{P_{sat}}$ that corresponds to the line height. Hence, if we plot all these points for a $\mathbf{T}$ range between the critical and triple point, the $\mathbf{PV}$ saturation curve for any substance can be obtained since the $\mathbf{P_{sat}}$ values that accomplish the Maxwell Construction are previous calculated.

So, to calculate these pressures, we need to call the **Free Energy Criterion** for any thermodynamic system, which states that the **fugacity** (or effective pressure) in all phases at equilibrium must be equal. Thus, for a $\mathbf{VLE}$ case, this criterion can be written as **Eq. (6)**, where the fugacity of each $\mathbf{n}$-phase $\mathbf{f^n }$, by definition, can be calculated in terms of their residual free energy $\mathbf{G_n^R}$ (**Eq. (7)**).

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

For **Redlich/Kwong (RK), Soave/Redlich/Kwong (SRK)**, and **Peng/Robinson (PR):** $\mathbf{(b) \quad \epsilon \neq \sigma \quad \longleftrightarrow \quad I^n=\frac{1}{\sigma-\epsilon}\ln{\frac{Z^n+\sigma \beta}{Z^n+\epsilon \beta}}}$.

Therefore, if we proposed an error value $\mathbf{Er}$ that describes the minimum relative fugacity difference between both $\mathbf{VLE}$ phases required to obtain an effective saturation pressure that can follow the Maxwell Construction, an iterative scheme can be proposed to predict a real EoS isotherm according to the accomplishment of **Ineq. (10)**, a **Fugacity Test** that will always change pressure values under the **Eq. (11)** until the relative fugacity difference gets equal or lower than the approved $\mathbf{Er}$ value (**Figure 2**).

$$
\begin{aligned}
\mathbf{(10) \quad \left| 1- \frac{f^l_i}{f^v_i} \right| > Er \quad \longrightarrow \quad (11)\quad P_{sat,i+1} = P_{sat,i}\frac{f^l_i}{f^v_i}}
\end{aligned}
$$

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/ESCHEME.jpg" width="905" height="349">

*Figure 2. Iterative Scheme for Fugacity Test calculations.*

This process can be followed when a $\mathbf{f_i^n}$ vs $\mathbf{P_{sat,i}}$ graph is plotted (**Figure 3**), where liquid and vapor lines represent the pressure changes with iterations until both fugacity functions intersect. The behavior of this iterative method allows us to visualize how the quotient of both fugacity for a pressure point always tends to decrease as **Ineq. (10)** is fulfilled, which allows this variable to be brought as close as possible to the real value of $\mathbf{P_{sat,i}}$ as $\mathbf{Er}$ is smaller. In other words, the Fugacity Test evaluates the limit of both fugacity functions when $\mathbf{P \rightarrow P_{sat,i}}$, while $\mathbf{Er}$ symbolizes one of the closeness parameters that define this limit.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/F_VS_P.jpg" width="545" height="378">

*Figure 3. Fugacity vs saturation pressure plot.*

Several iterative calculations of this method can be performed for the range of temperatures previous stablished for the working substance, which can lead to the prediction of $\mathbf{PV}$ saturation diagrams based on a primordial initial estimitation for the first pressure $\mathbf{P_{sat,1}}$ used to commence the **Fugacity Test**. So, either the maximum point of the analytical isotherm or the empirical pressure provided by the Antoine equation, the estimation procedure must consider its pressure range within the $\mathbf{PV}$ saturation area, which implies that the difference between the computational methods that use this criterion will only be the required number of iterations that they need to accomplish the **Ineq. (10)**. This is observed when $\mathbf{P}$ vs $\mathbf{i}$ (iteration number) points of each of these methods are plotted, which their curvature will depend on how close the starting pressure is to the $\mathbf{P_{sat}}$ (**Figure 4**).

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/F_VS_i.jpg" width="543" height="380">

*Figure 4. Saturation pressure vs* $i$ *(iteration number) plot* $(P_{sat,1}^{(1)}>P_{sat,1}^{(2)}>P_{sat,1}^{(3)})$.

Considering the maximum point of the analytical isotherm as the initial pressure for the Fugacity Test allows establishing a prediction method of the saturation pressure without using empirical parameters such as those of the Antoine equation. This initial pressure is a single value in the analytical isotherm, is always positive (as it is a point above the saturation pressure to be predicted), and depends only on the properties of the substance and the parameters of the cubic equation of state.

On the other hand, the $\mathbf{VLE}$ curve in a $\mathbf{P}$ vs $\mathbf{T}$ diagram demonstrates a continuous increasing behavior between the triple point and the critical point. Therefore, given a saturation pressure $\mathbf{P_{sat,i}}$ (between $\mathbf{P_t}$ and $\mathbf{P_c}$) at which it is intended to estimate its respective $\mathbf{T_{sat,i}}$ (between $\mathbf{T_t}$ and $\mathbf{T_c}$), a function $\mathbf{f(T_{sat})=P_{sat}(T_{sat})-P_{sat,i}}$ can be defined where $\mathbf{f(T_{sat,i})=0}$ and also $\mathbf{f(T_{sat})<0}$ and $\mathbf{f(T_{sat})>0}$ for $\mathbf{T_{sat}}$ $<$ $\mathbf{T_{sat,i}}$ and $\mathbf{T_{sat}}$ $>$ $\mathbf{T_{sat,i}}$, respectively (**Figure 5**).

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/bracketing.jpg" width="1021" height="319">

*Figure 5. Pressure vs temperature plot and representation of the function* $f(T_{sat})$*.*

Finding the zero of the nonlinear function $\mathbf{f(T_{sat})}$ given its characteristics is possible by some **bracketing method**. In addition, by using the Fugacity Test to estimate $\mathbf{P_{sat}(T_{sat})}$, a way of predicting $\mathbf{T_{sat}}$ given a pressure depending only on the properties of the substance and parameters of the cubic equation of state is being proposed, additionally to use the iterative method already developed. The next sections will be explained in more detail the bracketing methods and their study/implementation for the isobars, isotherms, and two-phase envelopes predictions.

## 2. Bracketing Methods

The bracketing methods require two initial guess points, $\mathbf{a}$ and $\mathbf{b}$, that contain the root, and $\mathbf{f(a)}$ and $\mathbf{f(b)}$ have a different parity, that is, $\mathbf{f(a)f(b)<0}$. By the **Intermediate Value Theorem**, there is at least one real root $\mathbf{p}$ in the interval $\mathbf{[a,b]}$ such that $\mathbf{f(p)=0}$. Given the increasing function of $\mathbf{P_{sat}}$ concerning $\mathbf{T_{sat}}$, there is only one zero in the real and continuos function $\mathbf{f(T_{sat})}$.

As the iteration progresses, the width of the bracket is reduced until the approximate solution to the desired accuracy is reached.  Some of the known bracketing methods are the **Bisection method**, Regula Falsi method (or **False Position**), and **improved or modified False Position method**.

### 2.1. Bisection Method

Also known as dichotomy, binary chopping, or half-interval method, Bisection is one of the elementary bracketing methods for finding a root of nonlinear equation $\mathbf{f(x)=0}$. It requires repeatedly halving subintervals $\mathbf{[a,b]}$ and, at each step $\mathbf{i}$, locating the midpoint between $\mathbf{a_i}$ and $\mathbf{b_i}$, which is calculated as $\mathbf{p_i=\frac{a_i+b_i}{2}}$. If $\mathbf{f(p_i)=0}$, the zero of the function will have been found. In contrast, if $\mathbf{f(p_i)\neq0}$, then $\mathbf{f(p_i)}$ has the same sign as either $\mathbf{f(a_i)}$ or $\mathbf{f(b_i)}$: when $\mathbf{f(p_i)}$ and $\mathbf{f(a_i)}$ have the same sign $(\mathbf{f(a_i)f(p_i)>0}$ or $\mathbf{f(b_i)f(p_i)<0})$, the zero of the function is in $\mathbf{[p_i,b_i]}$, and we set $\mathbf{a_{i+1}=p_i}$ and $\mathbf{b_{i+1}=b_i}$; meanwhile when $\mathbf{f(p_i)}$ and $\mathbf{f(a_i)}$ have opposite signs $(\mathbf{f(a_i)f(p_i)<0}$ or $\mathbf{f(b_i)f(p_i)>0})$, the zero of the function is in $\mathbf{[a_i,p_i]}$, and we set $\mathbf{a_{i+1}=a_i}$ and $\mathbf{b_{i+1}=p_i}$ (**Figure 6**). In each iteration $\mathbf{i}$, $\mathbf{f(a)}$ and $\mathbf{f(b)}$ are modified to the corresponding ones in the range of the function given the new values ​​of $\mathbf{a}$ and $\mathbf{b}$ assigned from iteration $\mathbf{i}$ for iteration $\mathbf{i+1}$. It is also important to note that obtaining the exact zero of the function $\mathbf{f(x)}$ could require a large number of iterations, so an error value $\mathbf{Er}$ is defined to consider the root found as valid, which limits the iterative process while $\mathbf{|f(b)|>Er}$, $\mathbf{|f(a)|>Er}$, and $\mathbf{|a-b|>Er}$.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/bisection.jpg" width="600" height="571">

*Figure 6. Model that demonstrates how the Bisection method generates successive iterates.*

### 2.2. False Position Method

The Bisection method is time-consuming in some cases because it does not consider that $\mathbf{f(a)}$ or $\mathbf{f(b)}$ is closer to the zero of $\mathbf{f(x)}$. For example, if $\mathbf{f(a)=-1}$ and $\mathbf{f(b)=100}$, the approximate root $\mathbf{p}$ should be chosen closer to $\mathbf{a}$ than $\mathbf{b}$. The False Position method takes this observation and, instead of considering the midpoint between $\mathbf{a}$ and $\mathbf{b}$, it finds the secant line from point $\mathbf{(a,f(a))}$ to point $\mathbf{(b,f(b))}$, and then estimates the root at the $\mathbf{x}$-intercept of the line. Therefore, the secant line has slope $\mathbf{\frac{f(b)-f(a)}{b-a}}$ and passes through the point $\mathbf{(b,f(b))}$, defining the equation of the line $\mathbf{y-f(b)=\frac{f(b)-f(a)}{b-a}(x-b)}$. The point where it intersects the $\mathbf{x}$-axis is $\mathbf{(p_i,0)}$, so $\mathbf{-f(b)=\frac{f(b)-f(a)}{b-a}(p_i-b)}$ and finally $\mathbf{p_i=b_i-\frac{f(b)_i(b_i-a_i)}{f(b)_i-f(a)_i}}$ (**Figure 7**).  In general cases, the sequence of approximate roots using the False Position method converges to the real root of equation $\mathbf{f(x)=0}$ faster than that using the Bisection method.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/secant.jpg" width="600" height="571">

*Figure 7. Model that demonstrates how the False Position method generates successive iterates.*

### 2.3. Improved False Position Method: Illinois, Pegasus, and Anderson & Björk 

Even though the False Position method does consider the relative magnitudes of $\mathbf{f(a)}$ and $\mathbf{f(b)}$, it retains one of the endpoints of the interval bracketing the real root. Therefore it converges to the root very slowly for convex or concave function $\mathbf{f(x)}$. There are several modifications of the False Position method. They are similar to False Position, except here we multiply $\mathbf{f(a)}$ or $\mathbf{f(b)}$ by $\mathbf{\lambda}$ when calculating $\mathbf{p}$ to avoid the retention of the left or right end point over successive iterations and accelerate the convergence of the method (**Figure 8**). Three known improvements to False Position are the Illinois, Pegasus, and Anderson & Björk methods. These modify the change rules of $\mathbf{a}$, $\mathbf{b}$, $\mathbf{f(a)}$, and $\mathbf{f(b)}$ for each iteration. For all three methods, if $\mathbf{f(a_i)f(p_i)>0}$ or $\mathbf{f(b_i)f(p_i)<0}$, $\mathbf{a_{i+1}=b_i}$ and $\mathbf{b_{i+1}=p_i}$, as well as $\mathbf{f(a)}$ and $\mathbf{f(b)}$ are updated for the next iteration with respect to the new values ​​of $\mathbf{a}$ and $\mathbf{b}$. However, when $\mathbf{f(a_i)f(p_i)<0}$ or $\mathbf{f(b_i)f(p_i)>0}$, $\mathbf{b_{i+1}=p_i}$ and $\mathbf{f(b) _{i+1}=f(p_i)}$, as well as (note that the value of $\mathbf{a _{i+1}}$ in all three method is not updated):

+ **Illinois method:** $\mathbf{f(a)_{i+1}=\frac{f(a)_i}{2}}$.
+ **Pegasus method:** $\mathbf{f(a)_{i+1}=\frac{f(a)_i f(b)_i}{f(b)_i+f(p_i)}}$.
+ **Anderson & Björk method:** $\mathbf{f(a)_{i+1}=mf(a)_i}$, where $\mathbf{m=1-\frac{f(p_i)}{f(b)_i}}$ when $\mathbf{1-\frac{f(p_i)}{f(b)_i}}$ is positive or $\mathbf{m=\frac{1}{2}}$ in the contrary case.

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/modified.jpg" width="600" height="571">

*Figure 8. Model that demonstrates how the Modified False Position method generates successive iterates.*

An analysis of iterations of these five methods allows determining the best one to find the zero in $\mathbf{f(T_{sat})}$ and having an algorithm that allows obtaining the $\mathbf{T_{sat}}$ given a certain pressure. Additionally, a fundamental aspect in the simulation of the liquid phase is to select the initial volume to generate the part of the isobar or isotherm in that phase. It is known that this value must be greater than $\mathbf{b}$. However, a volume close to $\mathbf{b}$ can generate large and even unrealistic $\mathbf{Z}$ values. To solve this problem, it should be noted that $\mathbf{Z=\frac{PV}{RT}}$ in the liquid phase has a decreasing behavior with increasing volume. This is due to the little change in volume in the liquid phase that in isobars the temperature increases and in isotherms the pressure decreases. This behavior of $\mathbf{Z}$ in relation to $\mathbf{V}$ in the liquid phase allows establishing a decreasing function between a volume greater than $\mathbf{b}$, such as $\mathbf{b+1}$, and the volume in the saturated liquid phase. Sometimes this function starts at a $\mathbf{Z}$ value greater than 1. Therefore, in case $\mathbf{Z}$ at $\mathbf{V=b+1}$ is greater than 1, some bracketing method can be used to find the volume where $\mathbf{Z=1}$.

Otherwise, if we wanted to generate a table of the thermodynamic properties of a substance, enthalpy and entropy are other important properties to predict, and a reference state is essential for this. Therefore, it is necessary to derive the equations that allow the calculation of enthalpy and entropy values ​​from $\mathbf{PVT}$ and heat-capacity data, as well as the use of the concept of residual properties.

## 3. Enthalpy and Entropy as Functions of T and P

In engineering applications, enthalpy and entropy are often the thermodynamic properties of interest, and $\mathbf{T}$ and $\mathbf{P}$ are the most common measurable properties of a substance or system. Thus, their mathematical connections, expressing the variation of $\mathbf{H}$ and $\mathbf{S}$ with changes in $\mathbf{T}$ and $\mathbf{P}$, are required. The **Eqs. (12)-(13)** are general equations relating enthalpy and entropy to temperature and pressure for homogeneous fluids of constant composition. The coefficients of $\mathbf{dT}$ and $\mathbf{dP}$ are evaluated from heat-capacity and $\mathbf{PVT}$ data. The ideal-gas state $(\mathbf{ig})$ provides an example of $\mathbf{PVT}$ behavior: $\mathbf{PV^{ig}=RT}$ and $\mathbf{\left(\frac{\partial V^{ig}}{\partial T}\right)_P=\frac{R}{P}}$. Substituting these equations into **Eqs. (12)-(13)** reduces them to **Eqs. (14)-(15)**. General expressions for $\mathbf{H^{ig}}$ and $\mathbf{S^{ig}}$ are found by integration of **Eqs. (14)-(15)** from an ideal-gas state at reference conditions $\mathbf{T_0}$ and $\mathbf{P_0}$ to an ideal-gas state at $\mathbf{T}$ and $\mathbf{P}$ (**Eqs. (16)-(17)**).

$$
\begin{aligned}
\mathbf{(12) \quad dH=C_PdT+\left[V-T\left(\frac{\partial V}{\partial T} \right)_P\right]dP \quad \longrightarrow \quad (14) \quad dH^{ig}=C_P^{ig}dT \quad \longrightarrow \quad (16) \quad H^{ig}=H_0^{ig}+\int_{T_0}^T C_P^{ig} dT}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{(13) \quad dS=C_P\frac{dT}{T}+\left(\frac{\partial V}{\partial T} \right)_PdP \quad \longrightarrow \quad (15) \quad dS^{ig}=C_P^{ig}\frac{dT}{T}-R\frac{dP}{P} \quad \longrightarrow \quad (17) \quad S^{ig}=S_0^{ig}+\int_{T_0}^T C_P^{ig}\frac{dT}{T}-R\ln{\frac{P}{P_0}}}
\end{aligned}
$$

The properties of the ideal gas state reflect the real molecular configurations but suppose the absence of intermolecular interactions. Residual properties represent the effect of such interactions. The generic residual property is defined by $\mathbf{M^R=M-M^{ig}}$, where $\mathbf{M}$ and $\mathbf{M^{ig}}$ are actual and ideal-gas-state properties at the same $\mathbf{T}$ and $\mathbf{P}$. They represent molar values for any extensive thermodynamic property like $\mathbf{V}$, $\mathbf{U}$, $\mathbf{H}$, $\mathbf{S}$, $\mathbf{G}$, or $\mathbf{A}$. Hence, because of $\mathbf{H=H^{ig}+H^R}$ and $\mathbf{S=S^{ig}+S^R}$, the **Eqs. (16)-(17)** can be expressed as **Eqs. (18)-(19)**. These expressions allow calculating the enthalpy and entropy using an ideal gas as a reference state.

$$
\begin{aligned}
\mathbf{(18) \quad H=H_0^{ig}+\int_{T_0}^T C_P^{ig} dT+H^R}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{(19) \quad S=S_0^{ig}+\int_{T_0}^T C_P^{ig}\frac{dT}{T}-R\ln{\frac{P}{P_0}}+S^R}
\end{aligned}
$$

Likewise, if the state of aggregation of the reference state is real liquid or real vapor, the residual property concept can be used to go from the real reference state to the ideal gas reference state, that is, $\mathbf{M^{ig}_0=M_0-M_0^R}$. The calculation of the enthalpy or entropy from ideal gas properties as a reference state is already known, therefore, the **Eqs. (20)-(21)** express the estimation of enthalpy and entropy from a real reference state. In general, the **Figure 9** illustrates the computation of changes of state to calculate a property $\mathbf{M}$ from an ideal gas or real reference state and using residual properties.

$$
\begin{aligned}
\mathbf{(20) \quad H=H_0-H_0^R+\int_{T_0}^T C_P^{ig} dT+H^R}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{(21) \quad S=S_0-S_0^R+\int_{T_0}^T C_P^{ig}\frac{dT}{T}-R\ln{\frac{P}{P_0}}+S^R}
\end{aligned}
$$

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/MATLAB%20Grader/Assignment%201/reference.jpg" width="802" height="397">

*Figure 9. Calculation of state changes for a generic property  using residual functions where* $M$ *is* $U$*,* $H$*,* $S$*,* $G$*, or* $A$*.*

In **Eqs. (18)-(21)**, to facilitate the calculation of the integrals, the $\mathbf{C_P^{ig}}$ can be expressed as a polynomial function of $\mathbf{T}$ with constants tabulated in tables in the bibliography. The polynomial function used is expressed in **Eq. (22)**  with $\mathbf{T[K]}$ and the integrals are estimated using **Eqs. (23)-(24)**.

$$
\begin{aligned}
\mathbf{(22) \quad C_P^{ig}\left[\frac{J}{mol\cdot K}\right]=A+BT+CT^2+DT^3+ET^4}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{(23) \quad \int_{T_0}^T C_P^{ig}dT=A(T-T_0)+\frac{B}{2}(T^2-T_0^2)+\frac{C}{3}(T^3-T_0^3)+\frac{D}{4}(T^4-T_0^4)+\frac{E}{5}(T^5-T_0^5)}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{(24) \quad \int_{T_0}^T C_P^{ig}\frac{dT}{T}=A\ln{\frac{T}{T_0}}+B(T-T_0)+\frac{C}{2}(T^2-T_0^2)+\frac{D}{3}(T^3-T_0^3)+\frac{E}{4}(T^4-T_0^4)}
\end{aligned}
$$

The constants of **Eq. (22)** of some compounds are (Chemours, 2018; Reklaitis & Schneider, 1986): 

+ **Ammonia:** $\mathbf{A=2.75500E+01}$, $\mathbf{B=2.56278E-02}$, $\mathbf{C=9.90042E-06}$, $\mathbf{D=-6.68639E-09}$, and $\mathbf{E=0}$.
+ **Argon:** $\mathbf{A=2.07723E+01}$, $\mathbf{B=0}$, $\mathbf{C=0}$, $\mathbf{D=0}$, and $\mathbf{E=0}$.
+ **Carbon Dioxide:** $\mathbf{A=1.90223E+01}$, $\mathbf{B=7.96291E-02}$, $\mathbf{C=-7.37067E-05}$, $\mathbf{D=3.74572E-08}$, and $\mathbf{E=-8.13304E-12}$.
+ **Chlorine:** $\mathbf{A=2.85463E+01}$, $\mathbf{B=2.38795E-02}$, $\mathbf{C=-2.13631E-05}$, $\mathbf{D=6.47263E-09}$, and $\mathbf{E=0}$.
+ **Hydrogen:** $\mathbf{A=1.76386E+01}$, $\mathbf{B=6.70055E-02}$, $\mathbf{C=-1.31485E-04}$, $\mathbf{D=1.05883E-07}$, and $\mathbf{E=-2.91803E-11}$.
+ **Methane:** $\mathbf{A=3.83870E+01}$, $\mathbf{B=-7.36639E-02}$, $\mathbf{C=2.90981E-04}$, $\mathbf{D=-2.63849E-07}$, and $\mathbf{E=8.00679E-11}$.
+ **Nitrogen:** $\mathbf{A=2.94119E+01}$, $\mathbf{B=-3.00681E-03}$, $\mathbf{C=5.45064E-05}$, $\mathbf{D=5.13186E-09}$, and $\mathbf{E=-4.25308E-12}$.
+ **Oxygen:** $\mathbf{A=2.98832E+01}$, $\mathbf{B=-1.13842E-02}$, $\mathbf{C=4.33779E-05}$, $\mathbf{D=-3.70082E-08}$, and $\mathbf{E=1.01006E-11}$.
+ **Refrigerant 134a (Tetrafluoroethane):** $\mathbf{A=1.94006E+01}$, $\mathbf{B=2.58531E-01}$, $\mathbf{C=-1.29665E-04}$, $\mathbf{D=0}$, and $\mathbf{E=0}$.
+ **Water:** $\mathbf{A=3.40471E+01}$, $\mathbf{B=-9.65064E-03}$, $\mathbf{C=3.29983E-05}$, $\mathbf{D=-2.04467E-08}$, and $\mathbf{E=4.30228E-12}$.

Also, based on the cubic equation of state the residual enthalpy and entropy can be calculated using **Eqs. (25)-(26)**. It is easy to estimate that the value of $\mathbf{\frac{d\ln{\alpha(T_r)}}{d\ln{T_r}}}$ in the cubic equation of state of vdW and RK is $\mathbf{\frac{d\ln{1}}{d\ln{T_r}}=0}$ and $\mathbf{\frac{d\ln{T_r^{-1/2}}}{d\ln{T_r}}=\frac{-\frac{1}{2}d\ln{T_r}}{d\ln{T_r}}=-\frac{1}{2}}$, respectively. 

$$
\begin{aligned}
\mathbf{(25) \quad H^R=RT\left[ Z-1+T\left(\frac{dq}{dT}\right)I\right]=RT\left[ Z-1+T_r\left(\frac{dq}{dT_r}\right)I\right]=RT\left[ Z-1+\left(\frac{d\ln{\alpha(T_r)}}{d\ln{T_r}}-1\right)qI\right]}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{(26) \quad S^R=R\left[ \ln{(Z-\beta)+\left(q+T\frac{dq}{dT}\right)I}\right]=R\left[ \ln{(Z-\beta)+\left(q+T_r\frac{dq}{dT_r}\right)I}\right]=R\left[ \ln{(Z-\beta)}+\frac{d\ln{\alpha(T_r)}}{d\ln{T_r}}qI \right]}
\end{aligned}
$$

In the case of SRK and PR, $\mathbf{p=0.480+1.574\omega-0.176\omega^2}$ and $\mathbf{p=0.37464+1.54226\omega-0.26992\omega^2}$ can be defined, respectively, so:

$$
\begin{aligned}
\mathbf{\alpha(T_r)=[1+p(1-T_r^{1/2})]^2 \quad \longleftrightarrow \quad exp[\ln{\alpha(T_r)}]=\left[1+p\left(1-exp\left(\frac{\ln{T_r}}{2}\right) \right)\right]^2}
\end{aligned}
$$

With $\mathbf{y=\ln{\alpha(T_r)}}$ and $\mathbf{x=\ln{T_r}}$, then $\mathbf{\frac{d\ln{\alpha(T_r)}}{d\ln{T_r}}=\frac{dy}{dx}}$ and:

$$
\begin{aligned}
\mathbf{exp(y)=\left[1+p\left(1-exp\left(\frac{x}{2}\right) \right)\right]^2 \quad \longleftrightarrow \quad exp(y)\frac{dy}{dx}=2\left[1+p\left(1-exp\left(\frac{x}{2}\right) \right)\right]\frac{d}{dx}\left[1+p\left(1-exp\left(\frac{x}{2}\right) \right)\right]=2\left[1+p\left(1-exp\left(\frac{x}{2}\right) \right)\right]\left[-\frac{p}{2}exp\left(\frac{x}{2} \right)\right]}
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{ \longleftrightarrow \quad \frac{dy}{dx}=\left[1+p\left(1-exp\left(\frac{x}{2}\right) \right)\right]\left[-pexp\left(\frac{x}{2}-y \right)\right]}
\end{aligned}
$$

Substituting $\mathbf{x}$ and $\mathbf{y}$:

$$
\begin{aligned}
\mathbf{(27) \quad \frac{d\ln{\alpha(T_r)}}{d\ln{T_r}}=-p\left[1+p\left(1-exp\left(\frac{\ln{T_r}}{2}\right) \right)\right]exp\left(\frac{\ln{T_r}}{2}-\ln{\alpha(T_r)} \right)}
\end{aligned}
$$

From these results to calculate $\mathbf{H}$ and $\mathbf{S}$ from a reference state and volume prediction, it is possible to calculate other properties, for example, $\mathbf{G=H-TS}$, $\mathbf{A=U-TS}$, and $\mathbf{U=H-PV}$. For calculate state changes in a property, the reference state is not important, and all reference state information drops out of the calculation. However, if we need to solve unsteady-state problems, the reference state is crucial.