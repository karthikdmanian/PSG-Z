#variables
var x1>=0;
var x2>=0;
var x3>=0;
var x4>=0;
var x5>=0;

#objective function
maximize z:0.7*x1+0.5*x2+x3+0.9*x4+1.1*x5;

#constraints
s.t. C1: 6*x1+10*x3+8*x5<=8000;
s.t. C2: 6*x1+6*x2+3*x3+3*x4+8*x5<=12000;
s.t. C3: 3*x1+3*x2+2*x3+2*x4+2*x5<=10000;
