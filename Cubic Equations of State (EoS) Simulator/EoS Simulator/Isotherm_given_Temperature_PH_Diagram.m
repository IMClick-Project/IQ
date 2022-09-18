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
% Isotherm Temperature [K]
Ti=str2double(app.IsothermTemperature.Value);
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
Integralcp=Acp*(Ti-T0)+Bcp*(Ti^2-T0^2)/2+Ccp*(Ti^3-T0^3)/3+Dcp*(Ti^4-T0^4)/4+Ecp*(Ti^5-T0^5)/5; % [kJ/kmol]
Tr=Ti/Tc;
if eos==2
    alpha=Tr^(-1/2);
elseif eos>2
    alpha=(1+p*(1-Tr^(1/2)))^2;
    derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
end
a=psi*alpha*(R*Tc)^2/Pc;
Hfug=zeros(1,2);
Pfug=zeros(1,2);
Hant=zeros(1,2);
Pant=zeros(1,2);
Zant=zeros(1,2);
Hexp=zeros(1,2);
Vexp=zeros(1,2);
Pexp=zeros(1,2);
Zexp=zeros(1,2);
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
% Save results
Pfug(1)=Paux;
Pfug(2)=Paux;
beta=Paux*b/(R*Ti);
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
% Find first P to use in Fugacity Test: Point close to the Maximum of the Loop of the EoS
step=(Vliquid-Vstart)/5000;
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
% Save data to graph the loop of the EoS: Saturated Liquid-Vapor;
jl=j-1;
P(j)=Paux;
H(j)=Hfug(1);
Z(j)=Zliquid;
j=j+1;
P(j)=Paux;
H(j)=Hfug(2);
Z(j)=Zvapor;
j=j+1;
% Save data to graph the loop of the EoS: Vapor
Vnext=Vvapor+1;
Vmax=Vvapor+10000;
step=(Vmax-Vnext)/5000;
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
% Find Psat using Antoine Equation
Pant(1)=exp(A-B/(Ti+C))*0.01;
Pant(2)=Pant(1);
liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Pant(1)*(b-V))/a)-V;
Vantl=fsolve(liquid,b,options);
Zant(1)=Pant(1)*Vantl/(R*Ti);
vapor=@(V) (R*Ti/Pant(2)+b-a/Pant(2)*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
Vantv=fsolve(vapor,R*Ti/Pant(2),options);
Zant(2)=Pant(2)*Vantv/(R*Ti);
beta=Pant(1)*b/(R*Ti);
if eos==1 
    I=beta/(Zant(1)+epsilon*beta);
else
    I=log((Zant(1)+sigma*beta)/(Zant(1)+epsilon*beta))/(sigma-epsilon);
end
HR=R2*Ti*(Zant(1)-1+(derivate-1)*q*I);
Hant(1)=(-HR0+HR+H0+Integralcp)/MM;
if eos==1 
    I=beta/(Zant(2)+epsilon*beta);
else
    I=log((Zant(2)+sigma*beta)/(Zant(2)+epsilon*beta))/(sigma-epsilon);
end
HR=R2*Ti*(Zant(2)-1+(derivate-1)*q*I);
Hant(2)=(-HR0+HR+H0+Integralcp)/MM;
% Find Psat, Hliquid, and Hvapor using the experimental data matrix
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
Pexp(1)=table2array(data2(app.IsothermTemperature.Value,1));
Pexp(2)=table2array(data2(app.IsothermTemperature.Value,1));
Vexp(1)=table2array(data2(app.IsothermTemperature.Value,2));
Vexp(2)=table2array(data2(app.IsothermTemperature.Value,3));
Hexp(1)=table2array(data2(app.IsothermTemperature.Value,4));
Hexp(2)=table2array(data2(app.IsothermTemperature.Value,5));
if ~(~ismissing(Pexp(1)) && string(Pexp(1))~="NaN")
    Pexp(1)=NaN;
    Pexp(2)=NaN;
end
if ~(~ismissing(Vexp(1)) && string(Vexp(1))~="NaN")
    Vexp(1)=NaN;
end
if ~(~ismissing(Vexp(2)) && string(Vexp(2))~="NaN")
    Vexp(2)=NaN;
end
if ~isnan(Vexp(1)) && ~isnan(Pexp(1))
    Zexl=string(Pexp(1)*Vexp(1)*1000*MM/(R*Ti));
else
    Zexl="NA";
end
if ~isnan(Vexp(2)) && ~isnan(Pexp(2))
    Zexv=string(Pexp(2)*Vexp(2)*1000*MM/(R*Ti));
else
    Zexv="NA";
end
if ~(~ismissing(Hexp(1)) && string(Hexp(1))~="NaN")
    Hexp(1)=NaN;
end
if ~(~ismissing(Hexp(2)) && string(Hexp(2))~="NaN")
    Hexp(2)=NaN;
end
% Figure: Isotherm given Temperature on a PH Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Hfug,Pfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Hant,Pant,"Marker","^","LineStyle","none","Color","r");
plot(app.Figure1,Hexp,Pexp,"Marker","o","LineStyle","none","Color",[0.1 0.5 0.1]);
plot(app.Figure1,Hfug,Pfug,"LineStyle","--","Color","b");
plot(app.Figure1,H,P,"Color",[0.5 0 0.5]);
Hmin=min([Hfug(1) Hant(1) Hexp(1)]);
Hmax=max([Hfug(2) Hant(2) Hexp(2)]);
Pmin=min([Pfug(1) Pant(1) Pexp(1)]);
Pmax=max([Pfug(1) Pant(1) Pexp(1)]);
axis(app.Figure1,[Hmin-abs(Hmax-Hmin)*0.5 Hmax+abs(Hmax-Hmin)*0.5 max([0 Pmin-10]) Pmax+10]);
if eos==1
    aux=strcat("van der Waals - ",app.Compound.Value," @ ",num2str(Ti)," K");
elseif eos==2
    aux=strcat("Redlich-Kwong - ",app.Compound.Value," @ ",num2str(Ti)," K");
elseif eos==3
    aux=strcat("Soave-Redlich-Kwong - ",app.Compound.Value," @ ",num2str(Ti)," K");
else
    aux=strcat("Peng-Robinson - ",app.Compound.Value," @ ",num2str(Ti)," K");
end
title(app.Figure1,aux);
legend(app.Figure1,{'Fugacity Test','Antoine Equation','Experimental Data'},"Box","on","LineWidth",1,"Location","southoutside");
hold(app.Figure1,"off");
% Report results: Isotherm given Temperature on a PH Diagram
phase=strings;
Pp=strings;
Zp=strings;
Hp=strings;
k=1;
% Liquid
step=max([floor(jl/100) 1]);
j=1;
while j<=jl
    phase(k)="Liquid";
    Pp(k)=string(P(j));
    Zp(k)=string(Z(j));
    Hp(k)=string(H(j));
    j=j+step;
    k=k+1;
end
% Saturated Liquid-Vapor
% Test Fugacity: Choice of thermodynamically possible cases
if Pfug(1)<Pt
    phase(k)="*Satured Liquid (Fugacity Test)";
elseif Pfug(1)>Pc
    phase(k)="**Satured Liquid (Fugacity Test)";
else
    phase(k)="Satured Liquid (Fugacity Test)";
end
Pp(k)=string(Pfug(1));
Zp(k)=string(Zliquid);
Hp(k)=string(Hfug(1));
k=k+1;
if Pfug(1)<Pt
    phase(k)="*Satured Vapor (Fugacity Test)";
elseif Pfug(1)>Pc
    phase(k)="**Satured Vapor (Fugacity Test)";
else
    phase(k)="Satured Vapor (Fugacity Test)";
end
Pp(k)=string(Pfug(1));
Zp(k)=string(Zvapor);
Hp(k)=string(Hfug(2));
k=k+1;
% Antoine Equation: Choice of thermodynamically possible cases
if Pant(1)<Pt
    phase(k)="*Satured Liquid (Antoine Equation)";
elseif Pant(1)>Pc
    phase(k)="**Satured Liquid (Antoine Equation)";
else
    phase(k)="Satured Liquid (Antoine Equation)";
end
Pp(k)=string(Pant(1));
Zp(k)=string(Zant(1));
Hp(k)=string(Hant(1));
k=k+1;
if Pant(1)<Pt
    phase(k)="*Satured Vapor (Antoine Equation)";
elseif Pant(1)>Pc
    phase(k)="**Satured Vapor (Antoine Equation)";
else
    phase(k)="Satured Vapor (Antoine Equation)";
end
Pp(k)=string(Pant(1));
Zp(k)=string(Zant(2));
Hp(k)=string(Hant(2));
k=k+1;
% Experimental data
if ~isnan(Pexp(1))
    Pex=string(Pexp(1));
else
    Pex="NA";
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
Pp(k)=Pex;
Zp(k)=Zexl;
Hp(k)=Hexl;
k=k+1;
phase(k)="Satured Vapor (Experimental Data)";
Pp(k)=Pex;
Zp(k)=Zexv;
Hp(k)=Hexv;
k=k+1;
% Vapor
% Find first point in the vapor phase
step=max([floor((length(P)-jl-2)/100) 1]);
j=jl+3;
while j<=length(P)
    phase(k)="Vapor";
    Pp(k)=string(P(j));
    Zp(k)=string(Z(j));
    Hp(k)=string(H(j));
    j=j+step;
    k=k+1;
end
app.Table1.Data=[phase;Pp;Zp;Hp]';