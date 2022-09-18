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
S0=str2double(app.ReferenceEntropy.Value); % Reference Entropy [kJ/kg/K]
S0=S0*MM; % [kJ/kmol/K]
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
R2=8.314; % Ideal Gas Constant [J*K/mol/K]
Er=0.00001;
b=omega*R*Tc/Pc;
% Reference entropy calculation of reference data
if ref==1
    SR0=0;
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
        SR0=R2*(log(Zliquid-beta)+derivate*q*I);
    else
        vapor=@(V) (R*T0/P0+b-a/P0*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
        Vvapor=fsolve(vapor,R*T0/P0,options);
        Zvapor=P0*Vvapor/(R*T0);
        if eos==1
            I=beta/(Zvapor+epsilon*beta);
        else
            I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
        end
        SR0=R2*(log(Zvapor-beta)+derivate*q*I);
    end
end
sizefug=1;
sizeant=1;
Sfug=[];
Pfug=[];
Sant=[];
Pant=[];
Sexp=zeros(1,2*tam);
Vexp=zeros(1,2*tam);
Pexp=zeros(1,2*tam);
method=strings(1,3*tam);
T=strings(1,3*tam);
P=strings(1,3*tam);
Sl=strings(1,3*tam);
Sv=strings(1,3*tam);
Zl=strings(1,3*tam);
Zv=strings(1,3*tam);
% For each T in the compound database: Find Psat, Zliquid, Zvapor, Sliquid, and Svapor
for i=1:tam
    Ti=str2double(aux(i));
    Integralcp_T=Acp*log(Ti/T0)+Bcp*(Ti-T0)+Ccp*(Ti^2-T0^2)/2+Dcp*(Ti^3-T0^3)/3+Ecp*(Ti^4-T0^4)/4; % [kJ/kmol/K]
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
    SR=R2*(log(Zliquid-beta)+derivate*q*I);
    Sfugl=(-SR0+SR+S0+Integralcp_T-R2*log(Paux/P0))/MM;
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    SR=R2*(log(Zvapor-beta)+derivate*q*I);
    Sfugv=(-SR0+SR+S0+Integralcp_T-R2*log(Paux/P0))/MM;
    % Test Fugacity: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pfug(sizefug)=Paux;
        Sfug(sizefug)=Sfugl;
        sizefug=sizefug+1;
        Pfug(sizefug)=Paux;
        Sfug(sizefug)=Sfugv;
        sizefug=sizefug+1;
    end
    P(ft)=string(Paux);
    Sl(ft)=string(Sfugl);
    Sv(ft)=string(Sfugv);
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
    SR=R2*(log(Zliquid-beta)+derivate*q*I);
    Santl=(-SR0+SR+S0+Integralcp_T-R2*log(Paux/P0))/MM;
    if eos==1
        I=beta/(Zvapor+epsilon*beta);
    else
        I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
    end
    SR=R2*(log(Zvapor-beta)+derivate*q*I);
    Santv=(-SR0+SR+S0+Integralcp_T-R2*log(Paux/P0))/MM;
    % Antoine Equation: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pant(sizeant)=Paux;
        Sant(sizeant)=Santl;
        sizeant=sizeant+1;
        Pant(sizeant)=Paux;
        Sant(sizeant)=Santv;
        sizeant=sizeant+1;
    end
    P(ae)=string(Paux);
    Sl(ae)=string(Santl);
    Sv(ae)=string(Santv);
    Zl(ae)=string(Zliquid);
    Zv(ae)=string(Zvapor);
    % Find Psat, Sliquid, and Svapor using the experimental data matrix
    l=2*i-1;
    v=2*i;
    T(ed)=string(Ti);
    method(ed)="Experimental Data";
    data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
    Pexp(l)=table2array(data2(aux(i),1));
    Pexp(v)=table2array(data2(aux(i),1));
    Vexp(l)=table2array(data2(aux(i),2));
    Vexp(v)=table2array(data2(aux(i),3));
    Sexp(l)=table2array(data2(aux(i),6));
    Sexp(v)=table2array(data2(aux(i),7));
    if isnan(Pexp(l))
        P(ed)="NA";
    else
        P(ed)=string(Pexp(l));
    end
    if isnan(Sexp(l))
        Sl(ed)="NA";
    else
        Sl(ed)=string(Sexp(l));
    end
    if isnan(Sexp(v))
        Sv(ed)="NA";
    else
        Sv(ed)=string(Sexp(v));
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
Integralcp_T=Acp*log(Ti/T0)+Bcp*(Ti-T0)+Ccp*(Ti^2-T0^2)/2+Dcp*(Ti^3-T0^3)/3+Ecp*(Ti^4-T0^4)/4; % [kJ/kmol/K]
Tr=Ti/Tc;
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
SR=R2*(log(Zc-beta)+derivate*q*I);
Sc=(-SR0+SR+S0+Integralcp_T-R2*log(Pc/P0))/MM;
Sexp(2*height(aux)+1)=Sc;
app.CriticalPressure.Value=string(Pc);
app.CriticalEntropy.Value=string(Sc);
% Figure: Two-Phase Envelope on a PS Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Sfug,Pfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Sant,Pant,"Marker","^","Linestyle","none","Color","r");
plot(app.Figure1,Sexp,Pexp,"Marker","o","Linestyle","none","Color",[0.1 0.5 0.1]);
Smax=max([max(Sfug) max(Sant) max(Sexp)]);
Smin=min([min(Sfug) min(Sant) min(Sexp)]);
Pmin=max([0 Pt-10]);
if Pmin==0
    Pmax=Pc+Pt;
else
    Pmax=Pt+10;
end
axis(app.Figure1,[Smin-abs(Smax-Smin)*0.5 Smax+abs(Smax-Smin)*0.5 Pmin Pmax]);
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
app.Table1.Data=[method;T;P;Zl;Zv;Sl;Sv]';