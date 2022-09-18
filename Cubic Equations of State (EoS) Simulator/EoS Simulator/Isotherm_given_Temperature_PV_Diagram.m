% Assignment of parameter values depending on the input and through the database
clc;
cla(app.Figure1);
cla(app.Figure2);
cla(app.Figure3);
app.Table1.Data={};
app.Table2.Data={};
app.Table3.Data={};
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
elseif eos==2 || eos==3
    epsilon=0;
    sigma=1;
    omega=0.08664;
    psi=0.42748;
else
    epsilon=1-2^(1/2);
    sigma=1+2^(1/2);
    omega=0.07780;
    psi=0.45724;
end
% Isotherm Temperature [K]
Ti=str2double(app.IsothermTemperature.Value);
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
b=omega*R*Tc/Pc;
Er=0.00001;
Tr=Ti/Tc;
if eos==2
    alpha=Tr^(-1/2);
elseif eos==3
    alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
elseif eos==4
    alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
end
a=psi*alpha*(R*Tc)^2/Pc;
Vfug=zeros(1,2);
Pfug=zeros(1,2);
Vant=zeros(1,2);
Pant=zeros(1,2);
Vexp=zeros(1,2);
Pexp=zeros(1,2);
P=[];
V=[];
ite=[];
Pite=[];
iteA=[];
PiteA=[];
IP=strings;
IPA=strings;
Pf=[];
f1=[];
fv=[];
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
Pmax=Paux;
Pmaxbef=Paux2;
Paux=Paux2;
ite(1)=1;
Pite(1)=Paux;
IP(1)="Point close to the Maximum of the Loop of the EoS";
k=2;
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
    % liquid - f=P*e^(GResidual/RT)
    fliquid=Paux*exp(Zliquid-1-log(Zliquid-beta)-q*I);
    vapor=@(V) (R*Ti/Paux+b-a/Paux*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
    Vvapor=fsolve(vapor,R*Ti/Paux,options);
    Zvapor=Paux*Vvapor/(R*Ti);
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    % vapor - f=P*e^(GResidual/RT)
    fvapor=Paux*exp(Zvapor-1-log(Zvapor-beta)-q*I);
    if abs(1-fliquid/fvapor)<Er
        break;
    end
    Paux=Paux*fliquid/fvapor;
    ite(k)=k;
    Pite(k)=Paux;
    IP(k)="Point close to the Maximum of the Loop of the EoS";
    k=k+1;
end
% Save results
Pfug(1)=Paux;
Pfug(2)=Paux;
Vfug(1)=Vliquid/1000/MM;
Vfug(2)=Vvapor/1000/MM;
% Save data to graph the loop of the EoS: Liquid 
% Find first V (with Z<=1)
Vstart=b+1;
Pstart=R*Ti/(Vstart-b)-a/((Vstart+epsilon*b)*(Vstart+sigma*b));
if Pstart*Vstart/(R*Ti)>1
    Zstart=Pstart*Vstart/(R*Ti)-1
    Pfinal=Paux
    Vfinal=Vliquid
    Zfinal=Pfinal*Vfinal/(R*Ti)-1
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
V(1)=Vstart/1000/MM;
P(2)=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
V(2)=Vnext/1000/MM;
Paux=P(1);
Paux2=P(2);
j=2;
% Save data to graph the loop of the EoS: Liquid to Point close to the Maximum of the Loop of the EoS
while Paux>Paux2
    Paux=Paux2;
    Vnext=Vnext+step;
    Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    j=j+1;
    P(j)=Paux2;
    V(j)=Vnext/1000/MM;
    if Vnext<Vliquid
        jl=j;
    end
end
Pminbef=Paux2;
Pmin=Paux;
while Paux<Paux2
    Paux=Paux2;
    Vnext=Vnext+step;
    Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    j=j+1;
    P(j)=Paux2;
    V(j)=Vnext/1000/MM;
end
% Save data to graph the loop of the EoS: Point close to the Maximum of the Loop of the EoS to Vapor
step=max([step (Vvapor-Vnext)/5000]);
while Vnext<Vvapor
    Vnext=Vnext+step;
    Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    j=j+1;
    P(j)=Paux2;
    V(j)=Vnext/1000/MM;
end
% Save data to graph the loop of the EoS: Vapor
jv=j+1;
Vnext=Vvapor+1;
Vmax=Vvapor+10000;
step=(Vmax-Vnext)/5000;
while Vnext<Vmax
    Paux2=R*Ti/(Vnext-b)-a/((Vnext+epsilon*b)*(Vnext+sigma*b));
    j=j+1;
    P(j)=Paux2;
    V(j)=Vnext/1000/MM;
    Vnext=Vnext+step;
end
% Calculate and save fugacity (liquid and vapor) of possible saturation pressures
step=(Pmaxbef-max([Pminbef Er]))/100;
j=1;
for i=max([Pminbef Er]):step:Pmaxbef
    Paux=i;
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
    fl(j)=fliquid;
    fv(j)=fvapor;
    Pf(j)=Paux;
    j=j+1;
end
% Find Psat using Antoine Equation
Pant(1)=exp(A-B/(Ti+C))*0.01;
Pant(2)=Pant(1);
liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Pant(1)*(b-V))/a)-V;
Vant(1)=fsolve(liquid,b,options)/1000/MM;
vapor=@(V) (R*Ti/Pant(2)+b-a/Pant(2)*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
Vant(2)=fsolve(vapor,R*Ti/Pant(1),options)/1000/MM;
% Fugacity Test starting with Psat calculated with Antoine Equation
Paux=Pant(1);
iteA(1)=1;
PiteA(1)=Paux;
IPA(1)="Saturation Pressure calculated with Antoine Equation";
k=2;
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
    iteA(k)=k;
    PiteA(k)=Paux;
    IPA(k)="Saturation Pressure calculated with Antoine Equation";
    k=k+1;
end
% Find Psat, Vliquid, and Vvapor using the experimental data matrix
% Isotherm Temperature
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
Pexp(1)=table2array(data2(app.IsothermTemperature.Value,1));
Pexp(2)=table2array(data2(app.IsothermTemperature.Value,1));
Vexp(1)=table2array(data2(app.IsothermTemperature.Value,2));
Vexp(2)=table2array(data2(app.IsothermTemperature.Value,3));
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
% Figure 1: Isotherm given Temperature on a PV Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Vfug,Pfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Vant,Pant,"Marker","^","LineStyle","none","Color","r");
plot(app.Figure1,Vexp,Pexp,"Marker","o","LineStyle","none","Color",[0.1 0.5 0.1]);
plot(app.Figure1,Vfug,Pfug,"LineStyle","--","Color","b");
plot(app.Figure1,V,P,"Color",[0.5 0 0.5]);
Vmin=min([min(V) Vfug(1) Vant(1) Vexp(1)]);
Vmax=max([max(V) Vfug(2) Vant(2) Vexp(2)]);
axis(app.Figure1,[max([0 Vmin-0.1/MM]) Vmax+0.1/MM Pmin-10 Pmax+10]);
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
% Figure 2: Fugacity Test - Pressure vs Iteration Number
hold(app.Figure2,"on");
plot(app.Figure2,ite,Pite,"Marker","*","LineStyle","none","Color","b","LineStyle","--");
plot(app.Figure2,iteA,PiteA,"Marker","^","LineStyle","none","Color","r","LineStyle","--");
h=legend(app.Figure2,{'Point close to the Maximum of the Loop of the EoS','Saturation Pressure calculated with Antoine Equation'},"Box","on","LineWidth",1,"Location","southoutside");
title(h,"Initial Point");
hold(app.Figure2,"off");
% Figure 3: Fugacity vs Pressure
hold(app.Figure3,"on");
plot(app.Figure3,Pf,fl,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure3,Pf,fv,"Marker","*","LineStyle","none","Color","r");
legend(app.Figure3,{'Liquid Fugacity','Vapor Fugacity'},"Box","on","LineWidth",1,"Location","southoutside");
hold(app.Figure3,"off");
% Report results 3: Fugacity vs Pressure
app.Table3.Data=[string(Pf);string(fl);string(fv)]';
% Report results 2: Fugacity Test - Pressure vs Iteration Number
app.Table2.Data=[IP,IPA;string(ite),string(iteA);string(Pite),string(PiteA)]';
% Report results 1: Isotherm given Temperature on a PV Diagram
phase=strings;
Pp=strings;
Zp=strings;
Vp=strings;
k=1;
% Liquid
step=max([floor(jl/100) 1]);
j=1;
while j<=jl
    phase(k)="Liquid";
    Pp(k)=string(P(j));
    Zp(k)=string(P(j)*V(j)*1000*MM/(R*Ti));
    Vp(k)=string(V(j));
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
Zp(k)=string(Pfug(1)*Vfug(1)*1000*MM/(R*Ti));
Vp(k)=string(Vfug(1));
k=k+1;
if Pfug(1)<Pt
    phase(k)="*Satured Vapor (Fugacity Test)";
elseif Pfug(1)>Pc
    phase(k)="**Satured Vapor (Fugacity Test)";
else
    phase(k)="Satured Vapor (Fugacity Test)";
end
Pp(k)=string(Pfug(1));
Zp(k)=string(Pfug(2)*Vfug(2)*1000*MM/(R*Ti));
Vp(k)=string(Vfug(2));
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
Zp(k)=string(Pant(1)*Vant(1)*1000*MM/(R*Ti));
Vp(k)=string(Vant(1));
k=k+1;
if Pant(1)<Pt
    phase(k)="*Satured Vapor (Antoine Equation)";
elseif Pant(1)>Pc
    phase(k)="**Satured Vapor (Antoine Equation)";
else
    phase(k)="Satured Vapor (Antoine Equation)";
end
Pp(k)=string(Pant(1));
Zp(k)=string(Pant(2)*Vant(2)*1000*MM/(R*Ti));
Vp(k)=string(Vant(2));
k=k+1;
% Experimental data
if ~isnan(Pexp(1))
    Pex=string(Pexp(1));
else
    Pex="NA";
end
if ~isnan(Vexp(1))
    Vexl=string(Vexp(1));
else
    Vexl="NA";
end
if ~isnan(Vexp(2))
    Vexv=string(Vexp(2));
else
    Vexv="NA";
end
phase(k)="Satured Liquid (Experimental Data)";
Pp(k)=Pex;
Zp(k)=Zexl;
Vp(k)=Vexl;
k=k+1;
phase(k)="Satured Vapor (Experimental Data)";
Pp(k)=Pex;
Zp(k)=Zexv;
Vp(k)=Vexv;
k=k+1;
% Vapor
% Find first point in the vapor phase
j=jv;
step=max([floor((length(P)-jv+1)/100) 1]);
while j<=length(P)
    phase(k)="Vapor";
    Pp(k)=string(P(j));
    Zp(k)=string(P(j)*V(j)*1000*MM/(R*Ti));
    Vp(k)=string(V(j));
    j=j+step;
    k=k+1;
end
app.Table1.Data=[phase;Pp;Zp;Vp]';