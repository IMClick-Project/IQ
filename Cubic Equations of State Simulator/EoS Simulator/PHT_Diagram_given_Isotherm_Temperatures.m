% Assignment of parameter values depending on the input and through the database
clc;
cla(app.Figure1);
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
% Available temperatures
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
tam=0;
aux=strings;
for i=1:height(data2)
    if ~ismissing(table2array(data2(i,1))) && string(table2array(data2(i,1)))~="NaN"
        tam=tam+1;
        aux(tam)=string(table2array(data2(i,1)));
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
% For each T in the compound database: Plot isotherms
hold(app.Figure1,"on");
Hsatmin=NaN;
Hsatmax=NaN;
for i=1:tam
    Ti=str2double(aux(i));
    Integralcp=Acp*(Ti-T0)+Bcp*(Ti^2-T0^2)/2+Ccp*(Ti^3-T0^3)/3+Dcp*(Ti^4-T0^4)/4+Ecp*(Ti^5-T0^5)/5; % [kJ/kmol]
    Tr=Ti/Tc;
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos>2
        alpha=(1+p*(1-Tr^(1/2)))^2;
        derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
    end
    a=psi*alpha*(R*Tc)^2/Pc;
    P=[];
    H=[];
    Z=[];
    % Find first P to use in Fugacity Test: Point close to the Maximum of the Loop of the EoS
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
    % Algorithm to find Psat with the Fugacity Test
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
    Psat=Paux;
    beta=Paux*b/(R*Ti);
    if eos==1 
        I=beta/(Zliquid+epsilon*beta);
    else
        I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Ti*(Zliquid-1+(derivate-1)*q*I);
    Hliquid=(-HR0+HR+H0+Integralcp)/MM;
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Ti*(Zvapor-1+(derivate-1)*q*I);
    Hvapor=(-HR0+HR+H0+Integralcp)/MM;
    if isnan(Hsatmax)
        Hsatmax=Hvapor;
    else
        Hsatmax=max([Hvapor Hsatmax]);
    end
    if isnan(Hsatmin)
        Hsatmin=Hliquid;
    else
        Hsatmin=min([Hliquid Hsatmin]);
    end
    % Save data to graph the loop of the EoS: Liquid 
    % Find first V (with Z<=1)
    Vstart=b+1;
    Pstart=R*Ti/(Vstart-b)-a/((Vstart+epsilon*b)*(Vstart+sigma*b));
    if Pstart*Vstart/(R*Ti)>1
        Zstart=Pstart*Vstart/(R*Ti)-1;
        Pfinal=Paux;
        Vfinal=Vliquid;
        Zfinal=Pfinal*Vfinal/(R*Ti)-1;
        while abs(Zfinal)>Er && abs(Zstart)>Er && abs(Pstart-Pfinal)>Er
            Pm=Pfinal-(Pfinal-Pstart)*Zfinal/(Zfinal-Zstart);
            liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Pm*(b-V))/a)-V;
            Vm=fsolve(liquid,b,options);
            Zm=Pm*Vm/(R*Ti);
            if (Zm-1)*Zfinal<0 
                Pstart=Pfinal;  
                Zstart=Zfinal;  
            else 
                Zstart=Zstart*Zfinal/(Zfinal+Zm-1);
            end
            Pfinal=Pm;  
            Zfinal=Zm-1;
        end
        Vstart=R*Ti*Zm/Pm;
    end
    % Liquid
    step=(Vliquid-Vstart)/100;
    Vnext=Vstart+step;
    P(1)=R*Ti/(Vstart-b)-a/((Vstart+epsilon*b)*(Vstart+sigma*b));
    Z(1)=P(1)*Vstart/(R*Ti);
    beta=P(1)*b/(R*Ti);
    if eos==1 
        I=beta/(Z(1)+epsilon*beta);
    else
        I=log((Z(1)+sigma*beta)/(Z(1)+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Ti*(Z(1)-1+(derivate-1)*q*I);
    H(1)=(-HR0+HR+H0+Integralcp)/MM;
    j=2;
    while Vnext<Vliquid
        P(j)=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
        Z(j)=P(j)*Vnext/(R*Ti);
        beta=P(j)*b/(R*Ti);
        if eos==1 
            I=beta/(Z(j)+epsilon*beta);
        else
            I=log((Z(j)+sigma*beta)/(Z(j)+epsilon*beta))/(sigma-epsilon);
        end
        HR=R2*Ti*(Z(j)-1+(derivate-1)*q*I);
        H(j)=(-HR0+HR+H0+Integralcp)/MM;
        Vnext=Vnext+step;
        j=j+1;
    end
    % Saturated Liquid-Vapor
    P(j)=Psat;
    H(j)=Hliquid;
    j=j+1;
    P(j)=Psat;
    H(j)=Hvapor;
    j=j+1;
    % Vapor
    Vnext=Vvapor+1;
    Vmax=Vvapor+10000;
    step=(Vmax-Vnext)/100;
    while Vnext<Vmax
        P(j)=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
        Z(j)=P(j)*Vnext/(R*Ti);
        beta=P(j)*b/(R*Ti);
        if eos==1 
            I=beta/(Z(j)+epsilon*beta);
        else
            I=log((Z(j)+sigma*beta)/(Z(j)+epsilon*beta))/(sigma-epsilon);
        end
        HR=R2*Ti*(Z(j)-1+(derivate-1)*q*I);
        H(j)=(-HR0+HR+H0+Integralcp)/MM;
        Vnext=Vnext+step;
        j=j+1;
    end
    plot3(app.Figure1,ones(j-1)*Ti,H,P);
end
hold(app.Figure1,"off");
view(app.Figure1,[45,45,45]);
ylim(app.Figure1,[Hsatmin-abs(Hsatmax-Hsatmin)*0.2 Hsatmax+abs(Hsatmax-Hsatmin)*0.2]);
zlim(app.Figure1,[max([0 Pt-10]) Pc*1.1]);
if eos==1
    aux=strcat("van der Waals - ",app.Compound.Value);
elseif eos==2
    aux=strcat("Redlich-Kwong - ",app.Compound.Value);
elseif eos==3
    aux=strcat("Soave-Redlich-Kwong - ",app.Compound.Value);
else
    aux=strcat("Peng-Robinson - ",app.Compound.Value);
end
title(app.Figure1,aux);