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
Vc=table2array(data(app.Compound.Value,7))/1000/MM; % Critical Volume [m3/kg]
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
sizefug=1;
sizeant=1;
Hfug=[];
Pfug=[];
Hant=[];
Pant=[];
Hexp=zeros(1,2*tam);
Vexp=zeros(1,2*tam);
Pexp=zeros(1,2*tam);
method=strings(1,3*tam);
T=strings(1,3*tam);
P=strings(1,3*tam);
Hl=strings(1,3*tam);
Hv=strings(1,3*tam);
Zl=strings(1,3*tam);
Zv=strings(1,3*tam);
% For each T in the compound database: Find Psat, Zliquid, Zvapor, Hliquid, and Hvapor
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
    ft=3*i-2;
    ae=3*i-1;
    ed=3*i;
    if Paux<Pt
        method(ft)="*Fugacity Test";
    elseif Paux>Pc
        method(ft)="**Fugacity Test";
    else
        method(ft)="Fugacity Test";
    end
    T(ft)=string(Ti);
    beta=Paux*b/(R*Ti);
    if eos==1 
        I=beta/(Zliquid+epsilon*beta);
    else
        I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Ti*(Zliquid-1+(derivate-1)*q*I);
    Hfugl=(-HR0+HR+H0+Integralcp)/MM;
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Ti*(Zvapor-1+(derivate-1)*q*I);
    Hfugv=(-HR0+HR+H0+Integralcp)/MM;
    % Test Fugacity: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pfug(sizefug)=Paux;
        Hfug(sizefug)=Hfugl;
        sizefug=sizefug+1;
        Pfug(sizefug)=Paux;
        Hfug(sizefug)=Hfugv;
        sizefug=sizefug+1;
    end
    P(ft)=string(Paux);
    Hl(ft)=string(Hfugl);
    Hv(ft)=string(Hfugv);
    Zl(ft)=string(Zliquid);
    Zv(ft)=string(Zvapor);
    % Find Psat using Antoine Equation
    Paux=exp(A-B/(Ti+C))*0.01;
    liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Paux*(b-V))/a)-V;
    Vliquid=fsolve(liquid,b,options);
    vapor=@(V) (R*Ti/Paux+b-a/Paux*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
    Vvapor=fsolve(vapor,R*Ti/Paux,options);
    Zliquid=Paux*Vliquid/(R*Ti);
    Zvapor=Paux*Vvapor/(R*Ti);
    beta=Paux*b/(R*Ti);
    if Paux<Pt
        method(ae)="*Antoine Equation";
    elseif Paux>Pc
        method(ae)="**Antoine Equation";
    else
        method(ae)="Antoine Equation";
    end
    T(ae)=string(Ti);
    if eos==1 
        I=beta/(Zliquid+epsilon*beta);
    else
        I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Ti*(Zliquid-1+(derivate-1)*q*I);
    Hantl=(-HR0+HR+H0+Integralcp)/MM;
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Ti*(Zvapor-1+(derivate-1)*q*I);
    Hantv=(-HR0+HR+H0+Integralcp)/MM;
    % Antoine Equation: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pant(sizeant)=Paux;
        Hant(sizeant)=Hantl;
        sizeant=sizeant+1;
        Pant(sizeant)=Paux;
        Hant(sizeant)=Hantv;
        sizeant=sizeant+1;
    end
    P(ae)=string(Paux);
    Hl(ae)=string(Hantl);
    Hv(ae)=string(Hantv);
    Zl(ae)=string(Zliquid);
    Zv(ae)=string(Zvapor);
    % Find Psat, Hliquid, and Hvapor using the experimental data matrix
    l=2*i-1;
    v=2*i;
    T(ed)=string(Ti);
    method(ed)="Experimental Data";
    data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
    Pexp(l)=table2array(data2(aux(i),1));
    Pexp(v)=table2array(data2(aux(i),1));
    Vexp(l)=table2array(data2(aux(i),2));
    Vexp(v)=table2array(data2(aux(i),3));
    Hexp(l)=table2array(data2(aux(i),4));
    Hexp(v)=table2array(data2(aux(i),5));
    if isnan(Pexp(l))
        P(ed)="NA";
    else
        P(ed)=string(Pexp(l));
    end
    if isnan(Hexp(l))
        Hl(ed)="NA";
    else
        Hl(ed)=string(Hexp(l));
    end
    if isnan(Hexp(v))
        Hv(ed)="NA";
    else
        Hv(ed)=string(Hexp(v));
    end
    if ~isnan(Vexp(l)) && ~isnan(Pexp(l))
        Zl(ed)=string(Pexp(l)*Vexp(l)*1000*MM/(R*Ti));
    else
        Zl(ed)="NA";
    end
    if ~isnan(Vexp(v)) && ~isnan(Pexp(v))
        Zv(ed)=string(Pexp(v)*Vexp(v)*1000*MM/(R*Ti));
    else
        Zv(ed)="NA";
    end
end
% Critical Point
Pexp(2*height(aux)+1)=Pc;
Zc=Pc*Vc*1000*MM/(R*Tc);
Integralcp=Acp*(Tc-T0)+Bcp*(Tc^2-T0^2)/2+Ccp*(Tc^3-T0^3)/3+Dcp*(Tc^4-T0^4)/4+Ecp*(Tc^5-T0^5)/5;
Tr=1; % Tc/Tc
if eos==2
    alpha=Tr^(-1/2);
elseif eos>2
    alpha=(1+p*(1-Tr^(1/2)))^2;
    derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
end
a=psi*alpha*(R*Tc)^2/Pc;
q=a/(b*R*Tc);
beta=Pc*b/(R*Tc);
if eos==1 
    I=beta/(Zc+epsilon*beta);
else
    I=log((Zc+sigma*beta)/(Zc+epsilon*beta))/(sigma-epsilon);
end
HR=R2*Tc*(Zc-1+(derivate-1)*q*I);
Hc=(-HR0+HR+H0+Integralcp)/MM;
Hexp(2*height(aux)+1)=Hc;
app.CriticalPressure.Value=string(Pc);
app.CriticalEnthalpy.Value=string(Hc);
% Figure: Two-Phase Envelope on a PH Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Hfug,Pfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Hant,Pant,"Marker","^","Linestyle","none","Color","r");
plot(app.Figure1,Hexp,Pexp,"Marker","o","Linestyle","none","Color",[0.1 0.5 0.1]);
Hmax=max([max(Hfug) max(Hant) max(Hexp)]);
Hmin=min([min(Hfug) min(Hant) min(Hexp)]);
Pmin=max([0 Pt-10]);
if Pmin==0
    Pmax=Pc+Pt;
else
    Pmax=Pt+10;
end
axis(app.Figure1,[Hmin-abs(Hmax-Hmin)*0.5 Hmax+abs(Hmax-Hmin)*0.5 Pmin Pmax]);
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
legend(app.Figure1,{'Fugacity Test','Antoine Equation','Experimental Data'},"Box","on","LineWidth",1,"Location","southoutside");
hold(app.Figure1,"off");
app.Table1.Data=[method;T;P;Zl;Zv;Hl;Hv]';