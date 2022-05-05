#variables
var w1>=0;
var w2>=0;
var w3>=0;

#objective function
minimize z: 8000*w1+12000*w2+10000*w3;

#constraints
s.t. C1: 6*w2+3*w3>=0.5;
s.t. C2: 10*w1+3*w2+2*w3>=1;
s.t. C3: 3*w2+2*w3>=0.9;
s.t. C4: 8*w1+8*w2+2*w3>=1.1;

