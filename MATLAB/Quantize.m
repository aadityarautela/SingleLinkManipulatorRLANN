function [x1, x2, x3] = Quantize(state, X1,X2,X3)
deltax1 = (X1(2)-X1(1))/2;
deltax2 = (X2(2)-X2(1))/2;
deltax3 = (X3(2)-X3(1))/2;

if state(1)>X1(end)+deltax1
    x1 = length(X1);
end

if state(2)>X2(end)+deltax2
    x2 = length(X2);
end

if state(3)>X3(end)+deltax3
    x3 = length(X3);
end

if state(1) <= X1(end) + deltax1
    x1 = find(abs(X1-state(1)) <= deltax1,1);
end

if state(2) <= X2(end) + deltax2
    x2 = find(abs(X2-state(2)) <= deltax2,1);
end

if state(3) <= X3(end) + deltax3
    x3 = find(abs(X3-state(3)) <= deltax3,1);
end

end
