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
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
b=omega*R*Tc/Pc;
Er=0.00001;
sizefug=1;
sizeant=1;
Vfug=[];
Pfug=[];
Vant=[];
Pant=[];
Vexp=zeros(1,2*tam);
Pexp=zeros(1,2*tam);
method=strings(1,3*tam);
T=strings(1,3*tam);
P=strings(1,3*tam);
Vl=strings(1,3*tam);
Vv=strings(1,3*tam);
Zl=strings(1,3*tam);
Zv=strings(1,3*tam);
% For each T in the compound database: Find Psat, Zliquid, Zvapor, Vliquid, and Vvapor
for i=1:tam
    Ti=str2double(aux(i));
    Tr=Ti/Tc;
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos==3
        alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
    elseif eos==4
        alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
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
    % Test Fugacity: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pfug(sizefug)=Paux;
        Vfug(sizefug)=Vliquid/1000/MM;
        sizefug=sizefug+1;
        Pfug(sizefug)=Paux;
        Vfug(sizefug)=Vvapor/1000/MM;
        sizefug=sizefug+1;
    end
    P(ft)=string(Paux);
    Vl(ft)=string(Vliquid/1000/MM);
    Vv(ft)=string(Vvapor/1000/MM);
    Zl(ft)=string(Zliquid);
    Zv(ft)=string(Zvapor);
    % Find Psat using Antoine Equation
    Paux=exp(A-B/(Ti+C))*0.01;
    liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Ti+Paux*(b-V))/a)-V;
    Vliquid=fsolve(liquid,b,options)/1000/MM;
    vapor=@(V) (R*Ti/Paux+b-a/Paux*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
    Vvapor=fsolve(vapor,R*Ti/Paux,options)/1000/MM;
    if Paux<Pt
        method(ae)="*Antoine Equation";
    elseif Paux>Pc
        method(ae)="**Antoine Equation";
    else
        method(ae)="Antoine Equation";
    end
    T(ae)=string(Ti);
    % Antoine Equation: Condition to check what points will be plotted
    if Paux>=Pt && Paux<=Pc
        Pant(sizeant)=Paux;
        Vant(sizeant)=Vliquid;
        sizeant=sizeant+1;
        Pant(sizeant)=Paux;
        Vant(sizeant)=Vvapor;
        sizeant=sizeant+1;
    end
    P(ae)=string(Paux);
    Vl(ae)=string(Vliquid);
    Vv(ae)=string(Vvapor);
    Zl(ae)=string(Paux*Vliquid*1000*MM/(R*Ti));
    Zv(ae)=string(Paux*Vvapor*1000*MM/(R*Ti));
    % Find Psat, Vliquid, and Vvapor using the experimental data matrix
    l=2*i-1;
    v=2*i;
    T(ed)=string(Ti);
    method(ed)="Experimental Data";
    data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value),"ReadRowNames",1);
    Pexp(l)=table2array(data2(aux(i),1));
    Pexp(v)=table2array(data2(aux(i),1));
    Vexp(l)=table2array(data2(aux(i),2));
    Vexp(v)=table2array(data2(aux(i),3));
    if isnan(Pexp(l))
        P(ed)="NA";
    else
        P(ed)=string(Pexp(l));
    end
    if isnan(Vexp(l))
        Vl(ed)="NA";
    else
        Vl(ed)=string(Vexp(l));
    end
    if isnan(Vexp(v))
        Vv(ed)="NA";
    else
        Vv(ed)=string(Vexp(v));
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
Vexp(2*height(aux)+1)=Vc;
app.CriticalPressure.Value=string(Pc);
app.CriticalVolume.Value=string(Vc);
% Figure: Two-Phase Envelope on a PV Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Vfug,Pfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Vant,Pant,"Marker","^","Linestyle","none","Color","r");
plot(app.Figure1,Vexp,Pexp,"Marker","o","Linestyle","none","Color",[0.1 0.5 0.1]);
Vmax=max([max(Vfug) max(Vant) max(Vexp)]);
Vmin=min([min(Vfug) min(Vant) min(Vexp)]);
Pmin=max([0 Pt-10]);
if Pmin==0
    Pmax=Pc+Pt;
else
    Pmax=Pt+10;
end
axis(app.Figure1,[max([0 Vmin-0.1/MM]) Vmax+0.1/MM Pmin Pmax]);
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
app.Table1.Data=[method;T;P;Zl;Zv;Vl;Vv]';