% Assignment of parameter values depending on the input and through the database
clc;
cla(app.Figure1vdW);
cla(app.Figure1RK);
cla(app.Figure1SRK);
cla(app.Figure1PR);
cla(app.Figure2);
app.Table1.Data={};
app.Table2vdW.Data={};
app.Table2RK.Data={};
app.Table2SRK.Data={};
app.Table2PR.Data={};
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
% Available pressures
data2=readtable("Thermodynamic Data.xlsx","Sheet",convertCharsToStrings(app.Compound.Value));
tam=0;
aux=strings;
for i=1:height(data2)
    if ~ismissing(table2array(data2(i,2))) && string(table2array(data2(i,2)))~="NaN"
        tam=tam+1;
        aux(tam)=string(table2array(data2(i,2)));
    end
end
% Variables and Constants
R=83.14; % Ideal Gas Constant [cm3*bar/mol/K]
Er=0.00001;
Tbracket=[Tt Tc-0.1];
app.TripleTemperature.Value=string(Tbracket(1));
app.CriticalTemperature.Value=string(Tbracket(2));
eosname=["van der Waals","Redlich-Kwong","Soave-Redlich-Kwong","Peng-Robinson"];
Pbracket=zeros(2,4);
Tsat=zeros(4,tam,5);
totalite=zeros(4,tam,5);
sumi=zeros(4,5);
Tsatstr=strings(4,tam,5);
totalitestr=strings(4,tam,5);
% Saturation Pressure given Temperature applying Differents Bracketing Methods
for eos=1:4
    % Cubic Equation of State
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
    b=omega*R*Tc/Pc;
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
        Pbracket(i,eos)=Paux;
    end
    % For each pressure in the database: Calculate Tsat and number of iterations for each bracketing methods
    % Tsat(eos,i,method): Tsat for Psat "i", estimate with cubic equation of state "eos" and bracketing methods "method"
    % totalite(eos,i,method): Number of iterations for Psat "i", estimate with cubic equation of state "eos" and bracketing methods "method"
    for i=1:tam
        Pi=str2double(aux(i));
        % Case not thermodynamically possible: Psat is not between the Psat calculated from Tt and close to Tc = NaN (Not a Number)
        if Pi<Pbracket(1,eos) || Pi>Pbracket(2,eos) 
            Tsat(eos,i,:)=[NaN NaN NaN NaN NaN];
            totalite(eos,i,:)=[NaN NaN NaN NaN NaN];
            Tsatstr(eos,i,:)=["NaN" "NaN" "NaN" "NaN" "NaN"];
            totalitestr(eos,i,:)=["NaN" "NaN" "NaN" "NaN" "NaN"];
            continue;
        end  
        % For each method: Calculate Tsat(eos,i,method) and totalite(eos,i,method)
        for method=1:5
            Pstart=Pbracket(1,eos)-Pi;
            Pfinal=Pbracket(2,eos)-Pi;
            Tstart=Tbracket(1);
            Tfinal=Tbracket(2);
            ite=0;
            while abs(Pfinal)>Er && abs(Pstart)>Er && abs(Tstart-Tfinal)>Er
                ite=ite+1;
                if method==1 % B
                    Ti=(Tstart+Tfinal)/2;
                else % FP or FP improvements
                    Ti=Tfinal-(Tfinal-Tstart)*Pfinal/(Pfinal-Pstart);
                end  
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
                if method==1 || method==2 % B or FP
                    if (Paux-Pi)*Pfinal<0
                        Tstart=Ti;  
                        Pstart=Paux-Pi;
                    else
                        Tfinal=Ti;  
                        Pfinal=Paux-Pi;
                    end
                else % FP improvements
                    if (Paux-Pi)*Pfinal<0 
                        Tstart=Tfinal;  
                        Pstart=Pfinal;
                    else
                        if method==3 % I
                            Pstart=Pstart/2;
                        elseif method==4 % P
                            Pstart=Pstart*Pfinal/(Pfinal+Paux-Pi);
                        else %AB
                            if 1-(Paux-Pi)/Pfinal>0
                                m=1-(Paux-Pi)/Pfinal;
                            else
                                m=1/2;
                            end
                            Pstart=Pstart*m;
                        end 
                    end
                    Tfinal=Ti;  
                    Pfinal=Paux-Pi;
                end
            end
            Tsat(eos,i,method)=Ti;
            totalite(eos,i,method)=ite;
            Tsatstr(eos,i,method)=string(Ti);
            totalitestr(eos,i,method)=string(ite);
        end
    end
end
% Figure 1: Saturation Pressure given Temperature applying Differents Bracketing Methods
hold(app.Figure1vdW,"on");
plot(app.Figure1vdW,str2double(aux),totalite(1,:,1).',"Marker","*","MarkerSize",2);
plot(app.Figure1vdW,str2double(aux),totalite(1,:,2).',"Marker","*","MarkerSize",2);
plot(app.Figure1vdW,str2double(aux),totalite(1,:,3).',"Marker","*","MarkerSize",2);
plot(app.Figure1vdW,str2double(aux),totalite(1,:,4).',"Marker","*","MarkerSize",2);
plot(app.Figure1vdW,str2double(aux),totalite(1,:,5).',"Marker","*","MarkerSize",2);
axis(app.Figure1vdW,[0 str2double(aux(tam))+str2double(aux(1)) 0 max(max(totalite(1,:,:)))]);
legend(app.Figure1vdW,{'B','FP','I','P','AB'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1,"FontSize",6);
hold(app.Figure1vdW,"off");
hold(app.Figure1RK,"on");
plot(app.Figure1RK,str2double(aux),totalite(2,:,1).',"Marker","*","MarkerSize",2);
plot(app.Figure1RK,str2double(aux),totalite(2,:,2).',"Marker","*","MarkerSize",2);
plot(app.Figure1RK,str2double(aux),totalite(2,:,3).',"Marker","*","MarkerSize",2);
plot(app.Figure1RK,str2double(aux),totalite(2,:,4).',"Marker","*","MarkerSize",2);
plot(app.Figure1RK,str2double(aux),totalite(2,:,5).',"Marker","*","MarkerSize",2);
axis(app.Figure1RK,[0 str2double(aux(tam))+str2double(aux(1)) 0 max(max(totalite(2,:,:)))]);
legend(app.Figure1RK,{'B','FP','I','P','AB'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1,"FontSize",6);
hold(app.Figure1RK,"off");
hold(app.Figure1SRK,"on");
plot(app.Figure1SRK,str2double(aux),totalite(3,:,1).',"Marker","*","MarkerSize",2);
plot(app.Figure1SRK,str2double(aux),totalite(3,:,2).',"Marker","*","MarkerSize",2);
plot(app.Figure1SRK,str2double(aux),totalite(3,:,3).',"Marker","*","MarkerSize",2);
plot(app.Figure1SRK,str2double(aux),totalite(3,:,4).',"Marker","*","MarkerSize",2);
plot(app.Figure1SRK,str2double(aux),totalite(3,:,5).',"Marker","*","MarkerSize",2);
axis(app.Figure1SRK,[0 str2double(aux(tam))+str2double(aux(1)) 0 max(max(totalite(3,:,:)))]);
legend(app.Figure1SRK,{'B','FP','I','P','AB'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1,"FontSize",6);
hold(app.Figure1SRK,"off");
hold(app.Figure1PR,"on");
plot(app.Figure1PR,str2double(aux),totalite(4,:,1).',"Marker","*","MarkerSize",2);
plot(app.Figure1PR,str2double(aux),totalite(4,:,2).',"Marker","*","MarkerSize",2);
plot(app.Figure1PR,str2double(aux),totalite(4,:,3).',"Marker","*","MarkerSize",2);
plot(app.Figure1PR,str2double(aux),totalite(4,:,4).',"Marker","*","MarkerSize",2);
plot(app.Figure1PR,str2double(aux),totalite(4,:,5).',"Marker","*","MarkerSize",2);
axis(app.Figure1PR,[0 str2double(aux(tam))+str2double(aux(1)) 0 max(max(totalite(4,:,:)))]);
legend(app.Figure1PR,{'B','FP','I','P','AB'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1,"FontSize",6);
hold(app.Figure1PR,"off");
% Figure 2: Total Iterations per Method of All Pressures
for i=1:4
    for j=1:5
        sumi(i,j)=sum(totalite(i,:,j).',"omitnan");
    end
end
bar(app.Figure2,sumi);
set(app.Figure2,"xticklabel",{'vdW','RK','SRK','PR'},"ylim",[1 max(max(sumi))+5]);
leg=legend(app.Figure2,{'B','FP','I','P','AB'},"Orientation","vertical","Location","eastoutside","Box","on","LineWidth",1);
title(leg,"Method");
% Report results
app.Table1.Data=[eosname;string(Pbracket(1,:));string(Pbracket(2,:));string(sumi(:,1)');string(sumi(:,2)');string(sumi(:,3)');string(sumi(:,4)');string(sumi(:,5)')]';
app.Table2vdW.Data=[string(aux);Tsatstr(1,:,1);totalitestr(1,:,1);Tsatstr(1,:,2);totalitestr(1,:,2);Tsatstr(1,:,3);totalitestr(1,:,3);Tsatstr(1,:,4);totalitestr(1,:,4);Tsatstr(1,:,5);totalitestr(1,:,5)]';
app.Table2RK.Data=[string(aux);Tsatstr(2,:,1);totalitestr(2,:,1);Tsatstr(2,:,2);totalitestr(2,:,2);Tsatstr(2,:,3);totalitestr(2,:,3);Tsatstr(2,:,4);totalitestr(2,:,4);Tsatstr(2,:,5);totalitestr(2,:,5)]';
app.Table2SRK.Data=[string(aux);Tsatstr(3,:,1);totalitestr(3,:,1);Tsatstr(3,:,2);totalitestr(3,:,2);Tsatstr(3,:,3);totalitestr(3,:,3);Tsatstr(3,:,4);totalitestr(3,:,4);Tsatstr(3,:,5);totalitestr(3,:,5)]';
app.Table2PR.Data=[string(aux);Tsatstr(4,:,1);totalitestr(4,:,1);Tsatstr(4,:,2);totalitestr(4,:,2);Tsatstr(4,:,3);totalitestr(4,:,3);Tsatstr(4,:,4);totalitestr(4,:,4);Tsatstr(4,:,5);totalitestr(4,:,5)]';