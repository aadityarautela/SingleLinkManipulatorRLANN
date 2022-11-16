function [x1dot, x2dot, x3dot]= SingleLinkManipulator(x1, x2, x3, u) 
J = 1.625103;
m = 0.506;
M0 = 0.434;
L0 = 0.305;
R0 = 0.023;
B0 = 16.25163;
L = 25.0103;
R = 5.0;
Kt = 0.90;
Kb = 0.90;
g = 9.8;
M = J + m*L0*L0/3.0 + M0*L0*L0 + 2*M0*R0*R0/5/Kt;
N = m*L0*g/2.0 + M0*L0*g/Kt;
B = B0/Kt;

x1dot = x2;
x2dot = -(N/M)*sin(x1) - (B/M)*x2 + (x3/M);
x3dot = -(Kb/L)*x2 - (R/L)*x3 + (u/L);

end