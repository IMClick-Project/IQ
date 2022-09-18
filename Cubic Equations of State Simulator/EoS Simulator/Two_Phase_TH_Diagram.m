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
% Available pressures
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
tam=0;
aux=strings;
Pindex=[];
for i=1:height(data2)
    if ~ismissing(table2array(data2(i,2))) && string(table2array(data2(i,2)))~="NaN"
        tam=tam+1;
        aux(tam)=string(table2array(data2(i,2)));
        Pindex(tam)=i;
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
Tfug=[];
Hant=[];
Tant=[];
Hexp=zeros(1,2*tam);
Texp=zeros(1,2*tam);
Vexp=zeros(1,2*tam);
method=strings(1,3*tam);
T=strings(1,3*tam);
P=strings(1,3*tam);
Hl=strings(1,3*tam);
Hv=strings(1,3*tam);
Zl=strings(1,3*tam);
Zv=strings(1,3*tam);
Tbracket=[Tt Tc-0.1];
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
% For each P in the compound database: Find Tsat, Zliquid, Zvapor, Hliquid, and Hvapor
sizefug=1;
sizeant=1;
for i=1:tam
    Pi=str2double(aux(i));
    ft=3*i-2;
    ae=3*i-1;
    ed=3*i;
    % Fugacity test method
    % Case not thermodynamically possible: Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number)
    if Pi<Pbracket(1) || Pi>Pbracket(2)
        method(ft)="Fugacity Test";
        P(ft)=string(Pi);
        T(ft)="NaN";
        Hl(ft)="NaN";
        Hv(ft)="NaN";
        Zl(ft)="NaN";
        Zv(ft)="NaN";
    else 
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
        % Save and report results
        Tfug(sizefug)=Ti;
        sizefug=sizefug+1;
        Tfug(sizefug)=Ti;
        sizefug=sizefug+1;
        beta=Pi*b/(R*Ti);
        Integralcp=Acp*(Ti-T0)+Bcp*(Ti^2-T0^2)/2+Ccp*(Ti^3-T0^3)/3+Dcp*(Ti^4-T0^4)/4+Ecp*(Ti^5-T0^5)/5;
        if eos==1 
            I=beta/(Zliquid+epsilon*beta);
        else
            I=log((Zliquid+sigma*beta)/(Zliquid+epsilon*beta))/(sigma-epsilon);
        end
        HR=R2*Ti*(Zliquid-1+(derivate-1)*q*I);
        Hfug(sizefug-2)=(-HR0+HR+H0+Integralcp)/MM;
        if eos==1
            I=beta/(Zvapor+epsilon*beta);
        else
            I=log((Zvapor+sigma*beta)/(Zvapor+epsilon*beta))/(sigma-epsilon);
        end
        HR=R2*Ti*(Zvapor-1+(derivate-1)*q*I);
        Hfug(sizefug-1)=(-HR0+HR+H0+Integralcp)/MM;
        method(ft)="Fugacity Test";
        P(ft)=string(Pi);
        T(ft)=string(Ti);
        Hl(ft)=string(Hfug(sizefug-2));
        Hv(ft)=string(Hfug(sizefug-1));
        Zl(ft)=string(Zliquid);
        Zv(ft)=string(Zvapor);
    end
    % Find Tsat using Antoine Equation
    Tantl=-B/(log(Pi/0.01)-A)-C;
    Tantv=Tantl;
    Tr=Tantl/Tc;
    beta=Pi*b/(R*Tantl);
    Integralcp=Acp*(Tantl-T0)+Bcp*(Tantl^2-T0^2)/2+Ccp*(Tantl^3-T0^3)/3+Dcp*(Tantl^4-T0^4)/4+Ecp*(Tantl^5-T0^5)/5;
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos>2
        alpha=(1+p*(1-Tr^(1/2)))^2;
        derivate=-p*(1+p*(1-Tr^(1/2)))*Tr^(1/2)/alpha;
    end
    a=psi*alpha*(R*Tc)^2/Pc;
    q=a/(b*R*Tantl);
    liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Tantl+Pi*(b-V))/a)-V;
    Vantl=fsolve(liquid,b,options)/1000/MM;
    vapor=@(V) (R*Tantv/Pi+b-a/Pi*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
    Vantv=fsolve(vapor,R*Tantv/Pi,options)/1000/MM;
    Zantl=Pi*Vantl*1000*MM/(R*Tantl);
    Zantv=Pi*Vantv*1000*MM/(R*Tantv);
    if eos==1 
        I=beta/(Zantl+epsilon*beta);
    else
        I=log((Zantl+sigma*beta)/(Zantl+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Tantl*(Zantl-1+(derivate-1)*q*I);
    Hantl=(-HR0+HR+H0+Integralcp)/MM;
    if eos==1 
        I=beta/(Zantv+epsilon*beta);
    else
        I=log((Zantv+sigma*beta)/(Zantv+epsilon*beta))/(sigma-epsilon);
    end
    HR=R2*Tantv*(Zantv-1+(derivate-1)*q*I);
    Hantv=(-HR0+HR+H0+Integralcp)/MM;
    if Tantl<Tt
        method(ae)="*Antoine Equation";
    elseif Tantl>Tc
        method(ae)="**Antoine Equation";
    else
        method(ae)="Antoine Equation";
    end
    % Antoine Equation: Condition to check what points will be plotted
    if Tantl>=Tt && Tantl<=Tc
        Tant(sizeant)=Tantl;
        Hant(sizeant)=Hantl;
        sizeant=sizeant+1;
        Tant(sizeant)=Tantl;
        Hant(sizeant)=Hantv;
        sizeant=sizeant+1;
    end
    P(ae)=string(Pi);
    T(ae)=string(Tantl);
    Hl(ae)=string(Hantl);
    Hv(ae)=string(Hantv);
    Zl(ae)=string(Zantl);
    Zv(ae)=string(Zantv);
    % Find Tsat, Hliquid, and Hvapor using the experimental data matrix
    l=2*i-1;
    v=2*i;
    P(ed)=string(Pi);
    method(ed)="Experimental Data";
    Texp(l)=table2array(data2(Pindex(i),1));
    Texp(v)=table2array(data2(Pindex(i),1));
    Vexp(l)=table2array(data2(Pindex(i),3));
    Vexp(v)=table2array(data2(Pindex(i),4));
    Hexp(l)=table2array(data2(Pindex(i),5));
    Hexp(v)=table2array(data2(Pindex(i),6));
    if isnan(Texp(l))
        T(ed)="NA";
    else
        T(ed)=string(Texp(l));
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
    if ~isnan(Vexp(l)) && ~isnan(Texp(l))
        Zl(ed)=string(Pi*Vexp(l)*1000*MM/(R*Texp(l)));
    else
        Zl(ed)="NA";
    end
    if ~isnan(Vexp(v)) && ~isnan(Texp(v))
        Zv(ed)=string(Pi*Vexp(v)*1000*MM/(R*Texp(v)));
    else
        Zv(ed)="NA";
    end
end
% Critical Point
Texp(2*height(aux)+1)=Tc;
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
app.CriticalTemperature.Value=string(Tc);
app.CriticalEnthalpy.Value=string(Hc);
% Figure: Two-Phase Envelope on a TH Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Hfug,Tfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Hant,Tant,"Marker","^","LineStyle","none","Color","r");
plot(app.Figure1,Hexp,Texp,"Marker","o","LineStyle","none","Color",[0.1 0.5 0.1]);
Hmax=max([max(Hfug) max(Hant) max(Hexp)]);
Hmin=min([min(Hfug) min(Hant) min(Hexp)]);
axis(app.Figure1,[Hmin-abs(Hmax-Hmin)*0.5 Hmax+abs(Hmax-Hmin)*0.5 Tt-10 Tc+10]);
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
app.Table1.Data=[method;P;T;Zl;Zv;Hl;Hv]';