clc;
clear all;

gamma = 0.99;
X1 = linspace(0,3.0, 30);
X2 = linspace(0,1.5,15);
X3 = linspace(0,1.5,15);
N1 = length(X1);
N2 = length(X2);
N3 = length(X3);
U = linspace(-10,10,40);
policy = zeros(N1,N2,N3);
pol = zeros(N1,N2,N3);
V = zeros(N1,N2,N3);

for runs = 1:10
    for i=1:N1
        for j=1:N2
            for k=1:N3
                if i==1 && j==15 && k==1
                    temp = 2+2;
                end
                curr_state=zeros(1,3);
                curr_state(1) = X1(i);
                curr_state(2) = X2(j);
                curr_state(3) = X3(k);
                for u=1:length(U)
                    action = U(u);
                    dyndot = SingleLinkManipulator(curr_state, action);
                    next_state = curr_state+0.1*dyndot;
                    quant_state = Quantize(next_state, X1,X2,X3);
                    x1 = quant_state(1,1);
                    x2 = quant_state(1,2);
                    x3 = quant_state(1,3);
                    nextV(u) = V(x1,x2,x3);
                    clear x1 x2 x3;
                    clear next_state;
                    clear quant_state;
                    clear action;
                end
                [Vbest,bestind] = max(nextV);
                V(i,j,k)= Reward(X1(i)) +  gamma*Vbest ;
                pol(i,j,k) = U(bestind);
            end
        end
    end
end

for i=1:N1
    for j=1:N2
        for k=1:N3
            for u=1:length(U)
                action = U(u);
                next_state = [X1(i) X2(j) X3(k)]+0.1*SingleLinkManipulator(X1(i) ,X2(j), X3(k), action);
                quant_state = Quantize(next_state, X1,X2,X3);
                x1 = quant_state(1,1);
                x2 = quant_state(1,2);
                x3 = quant_state(1,3);
                nextV(u) = V(x1,x2,x3);
                clear x1 x2 x3;
                clear next_state;
                clear quant_state;
                clear action;
                
            end
            [Vbest,bestind] = max(nextV);
            policy(i,j,k) = U(bestind);
        end
    end
end

