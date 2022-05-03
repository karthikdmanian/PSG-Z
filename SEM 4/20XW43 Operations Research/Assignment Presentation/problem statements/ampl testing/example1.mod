#variables
var x1>=0;
var x2>=0;

#obj. fn
maximize z:300*x1+200*x2;

#constraints
s.t. C1: 2*x1+x2<=8;
s.t. C2: x1+2*x2<=8;