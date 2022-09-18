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
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
b=omega*R*Tc/Pc;
Er=0.00001;
sizefug=1;
sizeant=1;
Vfug=[];
Tfug=[];
Vant=[];
Tant=[];
Vexp=zeros(1,2*tam);
Texp=zeros(1,2*tam);
method=strings(1,3*tam);
T=strings(1,3*tam);
P=strings(1,3*tam);
Vl=strings(1,3*tam);
Vv=strings(1,3*tam);
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
    elseif eos==3
        alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
    elseif eos==4
        alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
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
% For each P in the compound database: Find Tsat, Zliquid, Zvapor, Vliquid, and Vvapor
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
        Vl(ft)="NaN";
        Vv(ft)="NaN";
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
            elseif eos==3
                alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
            elseif eos==4
                alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
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
        Vfug(sizefug)=Vliquid/1000/MM;
        sizefug=sizefug+1;
        Tfug(sizefug)=Ti;
        Vfug(sizefug)=Vvapor/1000/MM;
        sizefug=sizefug+1;
        method(ft)="Fugacity Test";
        P(ft)=string(Pi);
        T(ft)=string(Ti);
        Vl(ft)=string(Vfug(sizefug-2));
        Vv(ft)=string(Vfug(sizefug-1));
        Zl(ft)=string(Zliquid);
        Zv(ft)=string(Zvapor);
    end
    % Find Tsat using Antoine Equation
    Tantl=-B/(log(Pi/0.01)-A)-C;
    Tantv=Tantl;
    Tr=Tantl/Tc;
    if eos==2
        alpha=Tr^(-1/2);
    elseif eos==3
        alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
    elseif eos==4
        alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
    end
    a=psi*alpha*(R*Tc)^2/Pc;
    liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Tantl+Pi*(b-V))/a)-V;
    Vantl=fsolve(liquid,b,options)/1000/MM;
    vapor=@(V) (R*Tantv/Pi+b-a/Pi*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
    Vantv=fsolve(vapor,R*Tantv/Pi,options)/1000/MM;
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
        Vant(sizeant)=Vantl;
        sizeant=sizeant+1;
        Tant(sizeant)=Tantl;
        Vant(sizeant)=Vantv;
        sizeant=sizeant+1;
    end
    P(ae)=string(Pi);
    T(ae)=string(Tantl);
    Vl(ae)=string(Vantl);
    Vv(ae)=string(Vantv);
    Zl(ae)=string(Pi*Vantl*1000*MM/(R*Tantl));
    Zv(ae)=string(Pi*Vantv*1000*MM/(R*Tantv));
    % Find Tsat, Vliquid, and Vvapor using the experimental data matrix
    l=2*i-1;
    v=2*i;
    P(ed)=string(Pi);
    method(ed)="Experimental Data";
    Texp(l)=table2array(data2(Pindex(i),1));
    Texp(v)=table2array(data2(Pindex(i),1));
    Vexp(l)=table2array(data2(Pindex(i),3));
    Vexp(v)=table2array(data2(Pindex(i),4));
    if isnan(Texp(l))
        T(ed)="NA";
    else
        T(ed)=string(Texp(l));
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
Vexp(2*height(aux)+1)=Vc;
app.CriticalTemperature.Value=string(Tc);
app.CriticalVolume.Value=string(Vc);
% Figure: Two-Phase Envelope on a TV Diagram
hold(app.Figure1,"on");
plot(app.Figure1,Vfug,Tfug,"Marker","*","LineStyle","none","Color","b");
plot(app.Figure1,Vant,Tant,"Marker","^","LineStyle","none","Color","r");
plot(app.Figure1,Vexp,Texp,"Marker","o","LineStyle","none","Color",[0.1 0.5 0.1]);
Vmax=max([max(Vfug) max(Vant) max(Vexp)]);
Vmin=min([min(Vfug) min(Vant) min(Vexp)]);
axis(app.Figure1,[max([0 Vmin-0.1/MM]) Vmax+0.1/MM Tt-10 Tc+10]);
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
app.Table1.Data=[method;P;T;Zl;Zv;Vl;Vv]';