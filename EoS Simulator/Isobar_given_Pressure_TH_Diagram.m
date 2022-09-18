% Assignment of parameter values depending on the input and through the database
clc;
cla(app.Figure1);
app.Table1.Data={};
format long;
options=optimset("Display","off");
warning("off","all");
% Compound
data=readtable("Thermodynamic Data.xlsx","Sheet","Compounds","ReadRowNames",1);
MM=table2array(data(app.Compound.Value,1)); % Molar Mass [g/mol]
Tt=table2array(data(app.Compound.Value,2)); % Triple Temperature [K]
Pt=table2array(data(app.Compound.Value,3)); % Triple Pressure [bar]
Tc=table2array(data(app.Compound.Value,4)); % Critical Temperature [K]
Pc=table2array(data(app.Compound.Value,5)); % Critical Pressure [bar]
w=table2array(data(app.Compound.Value,6)); % Acentric factor
% Antoine parameters
A=table2array(data(app.Compound.Value,8));
B=table2array(data(app.Compound.Value,9));
C=table2array(data(app.Compound.Value,10));
% Cp(T) parameters
Acp=table2array(data(app.Compound.Value,19));
Bcp=table2array(data(app.Compound.Value,20));
Ccp=table2array(data(app.Compound.Value,21));
Dcp=table2array(data(app.Compound.Value,22));
Ecp=table2array(data(app.Compound.Value,23));
% Cubic Equation of State
if app.EoS.Value=="van der Waals"
    eos=1;
elseif app.EoS.Value=="Redlich-Kwong"
    eos=2;
elseif app.EoS.Value=="Soave-Redlich-Kwong"
    eos=3;
else 
    eos=4;
end
if eos==1
    epsilon=0;
    sigma=0;
    omega=1/8;
    psi=27/64;
    alpha=1;
    derivate=0;
elseif eos==2 || eos==3
    epsilon=0;
    sigma=1;
    omega=0.08664;
    psi=0.42748;
    if eos==2
        derivate=-1/2;
    else
        p=0.480+1.574*w-0.176*w^2;
    end
else
    epsilon=1-2^(1/2);
    sigma=1+2^(1/2);
    omega=0.07780;
    psi=0.45724;
    p=0.37464+1.54226*w-0.26992*w^2;
end
% Isobar Pressure [bar]
Pi=str2double(app.IsobarPressure.Value);
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
for i=1:height(data2)
    if ~ismissing(table2array(data2(i,2))) && string(table2array(data2(i,2)))~="NaN"
        if table2array(data2(i,2))==Pi
            Pindex=i;
            break;
        end
    end
end
% Reference Data
if app.ReferenceState.Value=="Ideal Gas" % Reference State 
    ref=1;
elseif app.ReferenceState.Value=="Real Liquid"
    ref=2;
else
    ref=3;
end
T0=str2double(app.ReferenceTemperature.Value); % Reference Temperature [K]
P0=str2double(app.ReferencePressure.Value); % Reference Pressure [bar]
H0=str2double(app.ReferenceEnthalpy.Value); % Reference Enthalpy [kJ/kg]
H0=H0*MM; % [kJ/kmol]
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
R2=8.314; % Ideal Gas Constant [J*K/mol/K]
Er=0.00001;
b=omega*R*Tc/Pc;
% Reference enthalpy calculation of reference data
if ref==1
    HR0=0;
else
    Tr=T0/Tc;
    beta=P0*b/(R*T0);
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos>2
        alpha=(1+p*(1-Tr^(1/2)))^2;
        derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
    end
    a=psi*alpha*(R*Tc)^2/Pc;
    q=a/(b*R*T0);
    if ref==2
        liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*T0+P0*(b-V))/a)-V;
        Vliquid=fsolve(liquid,b,options);
        Zliquid=P0*Vliquid/(R*T0);
        if eos==1 
            I=beta/(Zliquid+epsilon*beta);
        else
            I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
        end
        HR0=R2*T0*(Zliquid-1+(derivate-1)*q*I);
    else
        vapor=@(V) (R*T0/P0+b-a/P0*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
        Vvapor=fsolve(vapor,R*T0/P0,options);
        Zvapor=P0*Vvapor/(R*T0);
        if eos==1
            I=beta/(Zvapor+epsilon*beta);
        else
            I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
        end
        HR0=R2*T0*(Zvapor-1+(derivate-1)*q*I);
    end
end
Tbracket=[Tt Tc-0.1];
app.TripleTemperature.Value=string(Tbracket(1));
app.CriticalTemperature.Value=string(Tbracket(2));
Pbracket=zeros(1,2);
% Fugacity Test to predict Psat for Tt and close to Tc
for i=1:2
    Ti=Tbracket(i);
    Tr=Ti/Tc;
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos>2
        alpha=(1+p*(1-Tr^(1/2)))^2;
        derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
    end
    a=psi*alpha*(R*Tc)^2/Pc;
    Vstart=b+1;
    Vnext=b+2;
    Paux=R*Ti/(Vstart-b)-a/((Vstart+epsilon*b)*(Vstart+sigma*b));
    Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    while Paux>Paux2
        Paux=Paux2;
        Vnext=Vnext+1;
        Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    end
    while Paux<Paux2
        Paux=Paux2;
        Vnext=Vnext+1;
        Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    end
    Paux=Paux2;
    q=a/(b*R*Ti);
    while true
        beta=Paux*b/(R*Ti);
        liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Paux*(b-V))/a)-V;
        Vliquid=fsolve(liquid,b,options);
        Zliquid=Paux*Vliquid/(R*Ti);
        if eos==1
            I=beta/(Zliquid+epsilon*beta);
        else
            I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
        end
        fliquid=Paux*exp(Zliquid-1-log(Zliquid-beta)-q*I);
        vapor=@(V) (R*Ti/Paux+b-a/Paux*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
        Vvapor=fsolve(vapor,R*Ti/Paux,options);
        Zvapor=Paux*Vvapor/(R*Ti);
        if eos==1
            I=beta/(Zvapor+epsilon*beta);
        else
            I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
        end
        fvapor=Paux*exp(Zvapor-1-log(Zvapor-beta)-q*I);
        if abs(1-fliquid/fvapor)<Er
            break;
        end
        Paux=Paux*fliquid/fvapor;
    end
    Pbracket(i)=Paux;
end
app.TriplePressure.Value=string(Pbracket(1));
app.CriticalPressure.Value=string(Pbracket(2));
% Find Tsat, Zliquid, Zvapor, Hliquid, and Hvapor given P
% Fugacity test method
% Case not thermodynamically possible: Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number)
Hfug=zeros(1,2);
Tfug=zeros(1,2);
Hant=zeros(1,2);
Tant=zeros(1,2);
Zant=zeros(1,2);
Vexp=zeros(1,2);
Hexp=zeros(1,2);
Texp=zeros(1,2);
T=[];
H=[];
Z=[];
if Pi<Pbracket(1) || Pi>Pbracket(2)
    checkNaN=true;
else 
    checkNaN=false;
    Pstart=Pbracket(1)-Pi;
    Pfinal=Pbracket(2)-Pi;
    Tstart=Tbracket(1);
    Tfinal=Tbracket(2);
    % Pegasus method
    while abs(Pfinal)>Er && abs(Pstart)>Er && abs(Tstart-Tfinal)>Er
        Ti=Tfinal-(Tfinal-Tstart)*Pfinal/(Pfinal-Pstart);
        Tr=Ti/Tc;
        if eos==2
            alpha=Tr^(-1/2);
        elseif eos>2
            alpha=(1+p*(1-Tr^(1/2)))^2;
            derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
        end
        a=psi*alpha*(R*Tc)^2/Pc;
        Vstart=b+1;
        Vnext=b+2;
        Paux=R*Ti/(Vstart-b)-a/((Vstart+epsilon*b)*(Vstart+sigma*b));
        Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
        while Paux>Paux2
            Paux=Paux2;
            Vnext=Vnext+1;
            Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
        end
        while Paux<Paux2
            Paux=Paux2;
            Vnext=Vnext+1;
            Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
        end
        Paux=Paux2;
        q=a/(b*R*Ti);
        while true
            beta=Paux*b/(R*Ti);
            liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Paux*(b-V))/a)-V;
            Vliquid=fsolve(liquid,b,options);
            Zliquid=Paux*Vliquid/(R*Ti);
            if eos==1
                I=beta/(Zliquid+epsilon*beta);
            else
                I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
            end
            fliquid=Paux*exp(Zliquid-1-log(Zliquid-beta)-q*I);
            vapor=@(V) (R*Ti/Paux+b-a/Paux*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
            Vvapor=fsolve(vapor,R*Ti/Paux,options);
            Zvapor=Paux*Vvapor/(R*Ti);
            if eos==1
                I=beta/(Zvapor+epsilon*beta);
            else
                I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
            end
            fvapor=Paux*exp(Zvapor-1-log(Zvapor-beta)-q*I);
            if abs(1-fliquid/fvapor)<Er
                break;
            end
            Paux=Paux*fliquid/fvapor;
        end
        if (Paux-Pi)*Pfinal<0 
            Tstart=Tfinal;  
            Pstart=Pfinal;
        else 
            Pstart=Pstart*Pfinal/(Pfinal+Paux-Pi);
        end
        Tfinal=Ti;  
        Pfinal=Paux-Pi;
    end
    % Save results
    Tfug(1)=Ti;
    Tfug(2)=Ti;
    beta=Pi*b/(R*Ti);
    Integralcp=Acp*(Ti-T0)+Bcp*(Ti^2-T0^2)/2+Ccp*(Ti^3-T0^3)/3+Dcp*(Ti^4-T0^4)/4+Ecp*(Ti^5-T0^5)/5;
    if eos==1 
        I=beta/(Zliquid+epsilon*beta);
    else
        I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Ti*(Zliquid-1+(derivate-1)*q*I);
    Hfug(1)=(-HR0+HR+H0+Integralcp)/MM;
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Ti*(Zvapor-1+(derivate-1)*q*I);
    Hfug(2)=(-HR0+HR+H0+Integralcp)/MM;  
    % Save data to graph the loop of the EoS: Liquid 
    % Find first V (with Z<=1)
    Vstart=b+1;
    if eos==1
        Tfunction=@(T) ((Pi+psi*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    elseif eos==2
        Tfunction=@(T) ((Pi+psi*(T/Tc)^(-1/2)*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    elseif eos==3
        Tfunction=@(T) ((Pi+psi*(1+(0.480+1.574*w-0.176*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    else
        Tfunction=@(T) ((Pi+psi*(1+(0.37464+1.54226*w-0.26992*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    end
    Tstart=fsolve(Tfunction,Ti,options);
    if Pi*Vstart/(R*Tstart)>1
        Zstart=Pi*Vstart/(R*Tstart)-1;
        Tfinal=Ti;
        Vfinal=Vliquid;
        Zfinal=Pi*Vfinal/(R*Tfinal)-1;
        while abs(Zfinal)>Er && abs(Zstart)>Er && abs(Tstart-Tfinal)>Er
            Tm=Tfinal-(Tfinal-Tstart)*Zfinal/(Zfinal-Zstart);
            Tr=Tm/Tc;
            if eos==2
                alpha=Tr^(-1/2);
            elseif eos>2
                alpha=(1+p*(1-Tr^(1/2)))^2;
                derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
            end
            a=psi*alpha*(R*Tc)^2/Pc;
            liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Tm+Pi*(b-V))/a)-V;
            Vm=fsolve(liquid,b,options);
            Zm=Pi*Vm/(R*Tm);
            if (Zm-1)*Zfinal<0 
                Tstart=Tfinal;  
                Zstart=Zfinal;
            else 
                Zstart=Zstart*Zfinal/(Zfinal+Zm-1);
            end
            Tfinal=Tm;  
            Zfinal=Zm-1;
        end
        Vstart=R*Tm*Zm/Pi;
    end
    if eos==1
        Tfunction=@(T) ((Pi+psi*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    elseif eos==2
        Tfunction=@(T) ((Pi+psi*(T/Tc)^(-1/2)*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    elseif eos==3
        Tfunction=@(T) ((Pi+psi*(1+(0.480+1.574*w-0.176*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    else
        Tfunction=@(T) ((Pi+psi*(1+(0.37464+1.54226*w-0.26992*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vstart+epsilon*b)*(Vstart+sigma*b)))*(Vstart-b)/R)-T;
    end
    T(1)=fsolve(Tfunction,Ti,options);
    Integralcp=Acp*(T(1)-T0)+Bcp*(T(1)^2-T0^2)/2+Ccp*(T(1)^3-T0^3)/3+Dcp*(T(1)^4-T0^4)/4+Ecp*(T(1)^5-T0^5)/5;
    Z(1)=Pi*Vstart/(R*T(1));
    Tr=T(1)/Tc;
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos>2
        alpha=(1+p*(1-Tr^(1/2)))^2;
        derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
    end
    a=psi*alpha*(R*Tc)^2/Pc;
    q=a/(b*R*T(1));
    beta=Pi*b/(R*T(1));
    if eos==1 
        I=beta/(Z(1)+epsilon*beta);
    else
        I=log((Z(1)+sigma*beta)/(Z(1)+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*T(1)*(Z(1)-1+(derivate-1)*q*I);
    H(1)=(-HR0+HR+H0+Integralcp)/MM;
    step=(Vliquid-Vstart)/5000;
    Vnext=Vstart+step;
    j=2;
    while Vnext<Vliquid
        if eos==1
            Tfunction=@(T) ((Pi+psi*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
        elseif eos==2
            Tfunction=@(T) ((Pi+psi*(T/Tc)^(-1/2)*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
        elseif eos==3
            Tfunction=@(T) ((Pi+psi*(1+(0.480+1.574*w-0.176*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
        else
            Tfunction=@(T) ((Pi+psi*(1+(0.37464+1.54226*w-0.26992*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
        end
        T(j)=fsolve(Tfunction,Ti,options);
        Integralcp=Acp*(T(j)-T0)+Bcp*(T(j)^2-T0^2)/2+Ccp*(T(j)^3-T0^3)/3+Dcp*(T(j)^4-T0^4)/4+Ecp*(T(j)^5-T0^5)/5;
        Z(j)=Pi*Vnext/(R*T(j));
        Tr=T(j)/Tc;
        if eos==2
            alpha=Tr^(-1/2);
        elseif eos>2
            alpha=(1+p*(1-Tr^(1/2)))^2;
            derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
        end
        a=psi*alpha*(R*Tc)^2/Pc;
        q=a/(b*R*T(j));
        beta=Pi*b/(R*T(j));
        if eos==1 
            I=beta/(Z(j)+epsilon*beta);
        else
            I=log((Z(j)+sigma*beta)/(Z(j)+epsilon*beta))/(sigma-epsilon);
        end
        HR=R2*T(j)*(Z(j)-1+(derivate-1)*q*I);
        H(j)=(-HR0+HR+H0+Integralcp)/MM;
        Vnext=Vnext+step;
        j=j+1;
    end
    % Save data to graph the loop of the EoS: Saturated Liquid-Vapor
    jl=j-1;
    T(j)=Ti;
    H(j)=Hfug(1);
    Z(j)=Zliquid;
    j=j+1;
    T(j)=Ti;
    H(j)=Hfug(2);
    Z(j)=Zvapor;
    j=j+1;
    % Save data to graph the loop of the EoS: Vapor
    Vnext=Vvapor+1;
    Vmax=Vvapor+5000;
    step=(Vmax-Vnext)/5000;
    while Vnext<Vmax
        if eos==1
            Tfunction=@(T) ((Pi+psi*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
        elseif eos==2
            Tfunction=@(T) ((Pi+psi*(T/Tc)^(-1/2)*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
        elseif eos==3
            Tfunction=@(T) ((Pi+psi*(1+(0.480+1.574*w-0.176*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
        else
            Tfunction=@(T) ((Pi+psi*(1+(0.37464+1.54226*w-0.26992*w^2)*(1-(T/Tc)^(1/2)))^2*(R*Tc)^2/Pc/((Vnext+epsilon*b)*(Vnext+sigma*b)))*(Vnext-b)/R)-T;
        end
        T(j)=fsolve(Tfunction,Ti,options);
        Integralcp=Acp*(T(j)-T0)+Bcp*(T(j)^2-T0^2)/2+Ccp*(T(j)^3-T0^3)/3+Dcp*(T(j)^4-T0^4)/4+Ecp*(T(j)^5-T0^5)/5;
        Z(j)=Pi*Vnext/(R*T(j));
        Tr=T(j)/Tc;
        if eos==2
            alpha=Tr^(-1/2);
        elseif eos>2
            alpha=(1+p*(1-Tr^(1/2)))^2;
            derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
        end
        a=psi*alpha*(R*Tc)^2/Pc;
        q=a/(b*R*T(j));
        beta=Pi*b/(R*T(j));
        if eos==1 
            I=beta/(Z(j)+epsilon*beta);
        else
            I=log((Z(j)+sigma*beta)/(Z(j)+epsilon*beta))/(sigma-epsilon);
        end
        HR=R2*T(j)*(Z(j)-1+(derivate-1)*q*I);
        H(j)=(-HR0+HR+H0+Integralcp)/MM;
        Vnext=Vnext+step;
        j=j+1;
    end
end
% Find Tsat using Antoine Equation
Tant(1)=-B/(log(Pi/0.01)-A)-C;
Tant(2)=Tant(1);
Tr=Tant(1)/Tc;
beta=Pi*b/(R*Tant(1));
Integralcp=Acp*(Tant(1)-T0)+Bcp*(Tant(1)^2-T0^2)/2+Ccp*(Tant(1)^3-T0^3)/3+Dcp*(Tant(1)^4-T0^4)/4+Ecp*(Tant(1)^5-T0^5)/5;
if eos==2
    alpha=Tr^(-1/2);
elseif eos>2
    alpha=(1+p*(1-Tr^(1/2)))^2;
    derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
end
a=psi*alpha*(R*Tc)^2/Pc;
q=a/(b*R*Tant(1));
liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Tant(1)+Pi*(b-V))/a)-V;
Vantl=fsolve(liquid,b,options);
Zant(1)=Pi*Vantl/(R*Tant(1));
vapor=@(V) (R*Tant(2)/Pi+b-a/Pi*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
Vantv=fsolve(vapor,R*Tant(2)/Pi,options);
Zant(2)=Pi*Vantv/(R*Tant(2));
if eos==1 
    I=beta/(Zant(1)+epsilon*beta);
else
    I=log((Zant(1)+sigma*beta)/(Zant(1)+epsilon*beta))/(sigma-epsilon);
end
HR=R2*Tant(1)*(Zant(1)-1+(derivate-1)*q*I);
Hant(1)=(-HR0+HR+H0+Integralcp)/MM;
if eos==1 
    I=beta/(Zant(2)+epsilon*beta);
else
    I=log((Zant(2)+sigma*beta)/(Zant(2)+epsilon*beta))/(sigma-epsilon);
end
HR=R2*Tant(2)*(Zant(2)-1+(derivate-1)*q*I);
Hant(2)=(-HR0+HR+H0+Integralcp)/MM;
% Find Tsat, Hliquid, and Hvapor using the experimental data matrix
Texp(1)=table2array(data2(Pindex,1));
Texp(2)=table2array(data2(Pindex,1));
Vexp(1)=table2array(data2(Pindex,3));
Vexp(2)=table2array(data2(Pindex,4));
Hexp(1)=table2array(data2(Pindex,5));
Hexp(2)=table2array(data2(Pindex,6));
if ~(~ismissing(Texp(1)) && string(Texp(1))~="NaN")
    Texp(1)=NaN;
    Texp(2)=NaN;
end
if ~(~ismissing(Vexp(1)) && string(Vexp(1))~="NaN")
    Vexp(1)=NaN;
end
if ~(~ismissing(Vexp(2)) && string(Vexp(2))~="NaN")
    Vexp(2)=NaN;
end
if ~isnan(Vexp(1)) && ~isnan(Texp(1))
    Zexl=string(Pi*Vexp(1)*1000*MM/(R*Texp(1)));
else
    Zexl="NA";
end
if ~isnan(Vexp(2)) && ~isnan(Texp(2))
    Zexv=string(Pi*Vexp(2)*1000*MM/(R*Texp(2)));
else
    Zexv="NA";
end
if ~(~ismissing(Hexp(1)) && string(Hexp(1))~="NaN")
    Hexp(1)=NaN;
end
if ~(~ismissing(Hexp(2)) && string(Hexp(2))~="NaN")
    Hexp(2)=NaN;
end
% Figure: Isobar given Pressure on a TH Diagram
hold(app.Figure1,"on");
if checkNaN==false
    plot(app.Figure1,Hfug,Tfug,"Marker","*","LineStyle","none","Color","b");
end
plot(app.Figure1,Hant,Tant,"Marker","^","LineStyle","none","Color","r");
plot(app.Figure1,Hexp,Texp,"Marker","o","LineStyle","none","Color",[0.1 0.5 0.1]);
if checkNaN==false
    plot(app.Figure1,H,T,"Color",[0.5 0 0.5]);
end
if checkNaN==true
    Hmin=min([Hant(1) Hexp(1)]);
    Hmax=max([Hant(2) Hexp(2)]);
    Tmin=min([Tant(1) Texp(1)]);
    Tmax=max([Tant(1) Texp(1)]);
else
    Hmin=min([Hfug(1) Hant(1) Hexp(1)]);
    Hmax=max([Hfug(2) Hant(2) Hexp(2)]);
    Tmin=min([Tfug(1) Tant(1) Texp(1)]);
    Tmax=max([Tfug(1) Tant(1) Texp(1)]);
end
axis(app.Figure1,[Hmin-abs(Hmax-Hmin)*0.5 Hmax+abs(Hmax-Hmin)*0.5 Tmin-10 Tmax+10]);
if eos==1
    aux=strcat("van der Waals - ",app.Compound.Value," @ ",num2str(Pi)," bar");
elseif eos==2
    aux=strcat("Redlich-Kwong - ",app.Compound.Value," @ ",num2str(Pi)," bar");
elseif eos==3
    aux=strcat("Soave-Redlich-Kwong - ",app.Compound.Value," @ ",num2str(Pi)," bar");
else
    aux=strcat("Peng-Robinson - ",app.Compound.Value," @ ",num2str(Pi)," bar");
end
title(app.Figure1,aux);
if checkNaN==false
    legend(app.Figure1,{'Fugacity Test','Antoine Equation','Experimental Data'},"Box","on","LineWidth",1,"Location","southoutside");
else
    legend(app.Figure1,{'Antoine Equation','Experimental Data'},"Box","on","LineWidth",1,"Location","southoutside");
end
hold(app.Figure1,"off");
phase=strings;
Tp=strings;
Zp=strings;
Hp=strings;
k=1;
if checkNaN==true
    % Report results: Isobar given Pressure on a TH Diagram
    % Saturated Liquid-Vapor
    phase(k)="Satured Liquid (Fugacity Test)";
    Tp(k)="NaN";
    Zp(k)="NaN";
    Hp(k)="NaN";
    k=k+1;
    phase(k)="Satured Vapor (Fugacity Test)";
    Tp(k)="NaN";
    Zp(k)="NaN";
    Hp(k)="NaN";
    k=k+1;
else
    % Report results: Isobar given Pressure on a TH Diagram
    % Liquid
    step=max([floor(jl/100) 1]);
    j=1;
    while j<=jl
        phase(k)="Liquid";
        Tp(k)=string(T(j));
        Zp(k)=string(Z(j));
        Hp(k)=string(H(j));
        j=j+step;
        k=k+1;
    end
    % Saturated Liquid-Vapor
    phase(k)="Satured Liquid (Fugacity Test)";
    Tp(k)=string(Ti);
    Zp(k)=string(Zliquid);
    Hp(k)=string(Hfug(1));
    k=k+1;
    phase(k)="Satured Vapor (Fugacity Test)";
    Tp(k)=string(Ti);
    Zp(k)=string(Zvapor);
    Hp(k)=string(Hfug(2));
    k=k+1;
end
% Antoine Equation: Choice of thermodynamically possible cases
if Tant(1)<Tt
    phase(k)="*Satured Liquid (Antoine Equation)";
elseif Tant(1)>Tc
    phase(k)="**Satured Liquid (Antoine Equation)";
else
    phase(k)="Satured Liquid (Antoine Equation)";
end
Tp(k)=string(Tant(1));
Zp(k)=string(Zant(1));
Hp(k)=string(Hant(1));
k=k+1;
if Tant(1)<Tt
    phase(k)="*Satured Vapor (Antoine Equation)";
elseif Tant(1)>Tc
    phase(k)="**Satured Vapor (Antoine Equation)";
else
    phase(k)="Satured Vapor (Antoine Equation)";
end
Tp(k)=string(Tant(1));
Zp(k)=string(Zant(2));
Hp(k)=string(Hant(2));
k=k+1;
% Experimental data
if ~isnan(Texp(1))
    Tex=string(Texp(1));
else
    Tex="NA";
end
if ~isnan(Hexp(1))
    Hexl=string(Hexp(1));
else
    Hexl="NA";
end
if ~isnan(Hexp(2))
    Hexv=string(Hexp(2));
else
    Hexv="NA";
end
phase(k)="Satured Liquid (Experimental Data)";
Tp(k)=Tex;
Zp(k)=Zexl;
Hp(k)=Hexl;
k=k+1;
phase(k)="Satured Vapor (Experimental Data)";
Tp(k)=Tex;
Zp(k)=Zexv;
Hp(k)=Hexv;
k=k+1;
if checkNaN==false
    % Vapor
    step=max([floor((length(T)-jl-2)/100) 1]);
    j=jl+3;
    while j<=length(T)
        phase(k)="Vapor";
        Tp(k)=string(T(j));
        Zp(k)=string(Z(j));
        Hp(k)=string(H(j));
        j=j+step;
        k=k+1;
    end
end
app.Table1.Data=[phase;Tp;Zp;Hp]';
% Notify if the case is thermodynamically not possible
% Test Fugacity
if checkNaN==true
    msgbox("Test Fugacity: Thermodynamically not possible case because Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number).","Error","error");
end