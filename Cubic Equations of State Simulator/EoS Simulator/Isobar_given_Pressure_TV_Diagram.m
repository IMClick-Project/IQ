% Assignment of parameter values depending on the input and through the database
clc;
cla(app.Figure1);
cla(app.Figure2);
cla(app.Figure3);
app.Table1.Data={};
app.Table2.Data={};
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
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
b=omega*R*Tc/Pc;
Er=0.00001;
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
app.TriplePressure.Value=string(Pbracket(1));
app.CriticalPressure.Value=string(Pbracket(2));
% Find Tsat, Zliquid, Zvapor, Vliquid, and Vvapor given P
% Fugacity test method
% Case not thermodynamically possible: Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number)
Vfug=zeros(1,2);
Tfug=zeros(1,2);
Vant=zeros(1,2);
Tant=zeros(1,2);
Vexp=zeros(1,2);
Texp=zeros(1,2);
T=[];
V=[];
TPeg=[];
PPeg=[];
itePeg=[];
if Pi<Pbracket(1) || Pi>Pbracket(2)
    checkNaN=true;
else 
    checkNaN=false;
    Pstart=Pbracket(1)-Pi;
    Pfinal=Pbracket(2)-Pi;
    Tstart=Tbracket(1);
    Tfinal=Tbracket(2);
    ite=0;
    % Pegasus method
    while abs(Pfinal)>Er && abs(Pstart)>Er && abs(Tstart-Tfinal)>Er
        ite=ite+1;
        itePeg(ite)=ite;
        Ti=Tfinal-(Tfinal-Tstart)*Pfinal/(Pfinal-Pstart);
        TPeg(ite)=Ti;
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
        PPeg(ite)=Paux;
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
    Vfug(1)=Vliquid/1000/MM;
    Vfug(2)=Vvapor/1000/MM;
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
            elseif eos==3
                alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
            elseif eos==4
                alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
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
    V(1)=Vstart/1000/MM;
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
        V(j)=Vnext/1000/MM;
        Vnext=Vnext+step;
        j=j+1;
    end
    % Save data to graph the loop of the EoS: Saturated Liquid-Vapor
    jl=j-1;
    T(j)=Ti;
    V(j)=Vfug(1);
    j=j+1;
    T(j)=Ti;
    V(j)=Vfug(2);
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
        V(j)=Vnext/1000/MM;
        Vnext=Vnext+step;
        j=j+1;
    end
end
% Find Tsat using Antoine Equation
Tant(1)=-B/(log(Pi/0.01)-A)-C;
Tant(2)=Tant(1);
Tr=Tant(1)/Tc;
if eos==2
    alpha=Tr^(-1/2);
elseif eos==3
    alpha=(1+(0.480+1.574*w-0.176*w^2)*(1-Tr^(1/2)))^2;
elseif eos==4
    alpha=(1+(0.37464+1.54226*w-0.26992*w^2)*(1-Tr^(1/2)))^2;
end
a=psi*alpha*(R*Tc)^2/Pc;
liquid=@(V) (b+(V+epsilon*b)*(V+sigma*b)*(R*Tant(1)+Pi*(b-V))/a)-V;
Vant(1)=fsolve(liquid,b,options)/1000/MM;
vapor=@(V) (R*Tant(2)/Pi+b-a/Pi*(V-b)/((V+epsilon*b)*(V+sigma*b)))-V;
Vant(2)=fsolve(vapor,R*Tant(2)/Pi,options)/1000/MM;
% Find Tsat, Vliquid, and Vvapor using the experimental data matrix
Texp(1)=table2array(data2(Pindex,1));
Texp(2)=table2array(data2(Pindex,1));
Vexp(1)=table2array(data2(Pindex,3));
Vexp(2)=table2array(data2(Pindex,4));
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
% Figure 1: Isobar given Pressure on a TV Diagram
hold(app.Figure1,"on");
if checkNaN==false
    plot(app.Figure1,Vfug,Tfug,"Marker","*","LineStyle","none","Color","b");
end
plot(app.Figure1,Vant,Tant,"Marker","^","LineStyle","none","Color","r");
plot(app.Figure1,Vexp,Texp,"Marker","o","LineStyle","none","Color",[0.1 0.5 0.1]);
if checkNaN==false
    plot(app.Figure1,V,T,"Color",[0.5 0 0.5]);
end
if checkNaN==true
    Vmin=min([Vant(1) Vexp(1)]);
    Vmax=max([Vant(2) Vexp(2)]);
    Tmin=min([Tant(1) Texp(1)]);
    Tmax=max([Tant(1) Texp(1)]);
else
    Vmin=min([min(V) Vfug(1) Vant(1) Vexp(1)]);
    Vmax=max([max(V) Vfug(2) Vant(2) Vexp(2)]);
    Tmin=min([Tfug(1) Tant(1) Texp(1)]);
    Tmax=max([Tfug(1) Tant(1) Texp(1)]);
end
axis(app.Figure1,[max([0 Vmin-0.1/MM]) Vmax+0.1/MM Tmin-10 Tmax+10]);
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
if checkNaN==false
    % Figure 2: Saturation Pressure vs Saturation Temperature
    hold(app.Figure2,"on");
    plot(app.Figure2,Tbracket(1),Pbracket(1),"Marker","*","Color","b","LineStyle","none");
    plot(app.Figure2,Tbracket(2),Pbracket(2),"Marker","*","Color","r","LineStyle","none");
    plot(app.Figure2,TPeg,PPeg,"Marker","*","Color",[0.1 0.5 0.1],"LineStyle","none");
    plot(app.Figure2,TPeg(ite),PPeg(ite),"Marker","*","Color",[0.5 0 0.5],"LineStyle","none");
    axis(app.Figure2,[Tbracket(1)-10 Tbracket(2)+10 Pbracket(1)-10 Pbracket(2)+10]);
    leg=legend(app.Figure2,{'Triple','Close to Critical','Intermediate','Final Result'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1);
    title(leg,"Calculated Points");
    hold(app.Figure2,"off");
    % Figure 3: Saturation Temperature vs Iteration Number
    plot(app.Figure3,itePeg,TPeg,"Marker","*","Color","b");
    axis(app.Figure3,[1 ite Tbracket(1)-10 Tbracket(2)+10]);
end
phase=strings;
Tp=strings;
Zp=strings;
Vp=strings;
k=1;
if checkNaN==true
    % Report results 1: Isobar given Pressure on a TV Diagram
    % Saturated Liquid-Vapor
    phase(k)="Satured Liquid (Fugacity Test)";
    Tp(k)="NaN";
    Zp(k)="NaN";
    Vp(k)="NaN";
    k=k+1;
    phase(k)="Satured Vapor (Fugacity Test)";
    Tp(k)="NaN";
    Zp(k)="NaN";
    Vp(k)="NaN";
    k=k+1;
else
    % Report results 2 and 3: Pegasus Method
    app.Table2.Data=[string(itePeg);string(TPeg);string(PPeg)]';
    % Report results 1: Isobar given Pressure on a TV Diagram
    % Liquid
    step=max([floor(jl/100) 1]);
    j=1;
    while j<=jl
        phase(k)="Liquid";
        Tp(k)=string(T(j));
        Zp(k)=string(Pi*V(j)*1000*MM/(R*T(j)));
        Vp(k)=string(V(j));
        j=j+step;
        k=k+1;
    end
    % Saturated Liquid-Vapor
    phase(k)="Satured Liquid (Fugacity Test)";
    Tp(k)=string(Ti);
    Zp(k)=string(Pi*Vfug(1)*1000*MM/(R*Tfug(1)));
    Vp(k)=string(Vfug(1));
    k=k+1;
    phase(k)="Satured Vapor (Fugacity Test)";
    Tp(k)=string(Ti);
    Zp(k)=string(Pi*Vfug(2)*1000*MM/(R*Tfug(2)));
    Vp(k)=string(Vfug(2));
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
Zp(k)=string(Pi*Vant(1)*1000*MM/(R*Tant(1)));
Vp(k)=string(Vant(1));
k=k+1;
if Tant(1)<Tt
    phase(k)="*Satured Vapor (Antoine Equation)";
elseif Tant(1)>Tc
    phase(k)="**Satured Vapor (Antoine Equation)";
else
    phase(k)="Satured Vapor (Antoine Equation)";
end
Tp(k)=string(Tant(1));
Zp(k)=string(Pi*Vant(2)*1000*MM/(R*Tant(2)));
Vp(k)=string(Vant(2));
k=k+1;
% Experimental data
if ~isnan(Texp(1))
    Tex=string(Texp(1));
else
    Tex="NA";
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
Tp(k)=Tex;
Zp(k)=Zexl;
Vp(k)=Vexl;
k=k+1;
phase(k)="Satured Vapor (Experimental Data)";
Tp(k)=Tex;
Zp(k)=Zexv;
Vp(k)=Vexv;
k=k+1;
if checkNaN==false
    % Vapor
    step=max([floor((length(T)-jl-2)/100) 1]);
    j=jl+3;
    while j<=length(T)
        phase(k)="Vapor";
        Tp(k)=string(T(j));
        Zp(k)=string(Pi*V(j)*1000*MM/(R*T(j)));
        Vp(k)=string(V(j));
        j=j+step;
        k=k+1;
    end
end
app.Table1.Data=[phase;Tp;Zp;Vp]';
% Notify if the case is thermodynamically not possible
% Test Fugacity
if checkNaN==true
    msgbox("Test Fugacity: Thermodynamically not possible case because Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number).","Error","error");
end