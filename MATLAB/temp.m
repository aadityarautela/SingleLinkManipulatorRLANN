clc;
clear all;

X1 = linspace(0,3.0, 30);
X2 = linspace(0,1.5,15);
X3 = linspace(0,1.5,15);
[x1,x2,x3] = Quantize([0.0536 0.5893 0.0536], X1,X2,X3);